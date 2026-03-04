import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# הגדרות דף
st.set_page_config(page_title="סימולטור טיטרציה כימית", layout="wide")

# פונקציית חישוב pH (לוגיקה כימית)
def calculate_ph(v_base, v_acid, c_acid, c_base, acid_type='strong'):
    p_ka = 4.76  # עבור חומצה אצטית
    kw = 1e-14
    
    moles_acid = (c_acid * v_acid) / 1000
    moles_base = (c_base * v_base) / 1000
    total_vol = (v_acid + v_base) / 1000
    
    if total_vol == 0: return 7.0

    if acid_type == 'strong':
        if v_base == 0:
            return -np.log10(c_acid)
        if moles_acid > moles_base:
            return -np.log10((moles_acid - moles_base) / total_vol)
        elif moles_base > moles_acid:
            conc_oh = (moles_base - moles_acid) / total_vol
            return 14 + np.log10(conc_oh)
        return 7.0
    
    else:  # חומצה חלשה
        ka = 10**(-p_ka)
        if v_base == 0:
            h = (-ka + np.sqrt(ka**2 + 4 * ka * c_acid)) / 2
            return -np.log10(h)
        if moles_base < moles_acid:
            # Henderson-Hasselbalch
            # הימנעות מחילוק באפס בנקודת המקבילות
            ratio = moles_base / (moles_acid - moles_base) if moles_acid != moles_base else 1e10
            return p_ka + np.log10(ratio)
        elif moles_base > moles_acid:
            conc_oh = (moles_base - moles_acid) / total_vol
            return 14 + np.log10(conc_oh)
        else:  # נקודת מקבילות - הידרוליזה של מלח
            kb = kw / ka
            c_salt = moles_acid / total_vol
            oh = np.sqrt(kb * c_salt)
            return 14 - (-np.log10(oh))

# ניהול מצב (State) - כדי שהנתונים לא יימחקו בכל לחיצה
if 'v_added' not in st.session_state:
    st.session_state.v_added = [0.0]
    # ערך התחלתי כברירת מחדל
    st.session_state.ph_values = [1.0] 

# ממשק משתמש - Sidebar
st.sidebar.header("🧪 פרמטרי הניסוי")
acid_choice = st.sidebar.selectbox("סוג חומצה", ["HCl (חזקה)", "CH3COOH (חלשה)"])
type_key = 'strong' if "HCl" in acid_choice else 'weak'

c_acid = st.sidebar.number_input("ריכוז חומצה (M)", value=0.1, step=0.01, format="%.3f")
v_acid = st.sidebar.number_input("נפח חומצה בארלנמייר (מ"ל)", value=25.0, step=1.0)
c_base = st.sidebar.number_input("ריכוז בסיס בביורטה NaOH (M)", value=0.1, step=0.01, format="%.3f")

# עדכון pH התחלתי אם הפרמטרים השתנו ואין עדיין טיטרציה
if len(st.session_state.v_added) == 1:
    st.session_state.ph_values = [calculate_ph(0, v_acid, c_acid, c_base, type_key)]

# כפתור איפוס
if st.sidebar.button("נקה נתונים"):
    st.session_state.v_added = [0.0]
    st.session_state.ph_values = [calculate_ph(0, v_acid, c_acid, c_base, type_key)]
    st.rerun()

# אזור עבודה ראשי
st.title("🔬 סימולטור טיטרציה מתקדם")
st.markdown(f"**מערכת:** {acid_choice} ⟵ NaOH {c_base}M")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("שליטה בביורטה")
    add_val = st.number_input("הוסף נפח בסיס (מ"ל)", value=1.0, step=0.1, min_value=0.0)
    
    if st.button("💧 הוסף לתמיסה"):
        new_v = st.session_state.v_added[-1] + add_val
        new_ph = calculate_ph(new_v, v_acid, c_acid, c_base, type_key)
        st.session_state.v_added.append(new_v)
        st.session_state.ph_values.append(new_ph)

    # הצגת נתונים נוכחיים
    current_ph = st.session_state.ph_values[-1]
    st.metric("pH נוכחי", f"{current_ph:.2f}")
    st.metric("נפח בסיס כולל", f"{st.session_state.v_added[-1]:.2f} מ"ל")

with col2:
    # יצירת הגרף בעזרת Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=st.session_state.v_added, 
        y=st.session_state.ph_values,
        mode='lines+markers',
        name='עקומת טיטרציה',
        line=dict(color='#00d4ff', width=3),
        marker=dict(size=8)
    ))
    
    fig.update_layout(
        title="עקומת pH כפונקציה של נפח בסיס",
        xaxis_title="נפח NaOH (מ"ל)",
        yaxis_title="pH",
        yaxis=dict(range=[0, 14]),
        template="plotly_dark",
        margin=dict(l=20, r=20, t=40, b=20)
    )
    st.plotly_chart(fig, use_container_width=True)

# טבלת נתונים
st.divider()
st.subheader("📊 יומן מדידות")
df = pd.DataFrame({
    "נפח בסיס (מ"ל)": st.session_state.v_added,
    "pH": st.session_state.ph_values
})
st.dataframe(df.style.format({"pH": "{:.2f}", "נפח בסיס (מ"ל)": "{:.2f}"}), use_container_width=True)

# הורדת נתונים
csv = df.to_csv(index=False).encode('utf-8')
st.download_button("⬇️ ייצוא נתוני מעבדה (CSV)", csv, "titration_results.csv", "text/csv")
