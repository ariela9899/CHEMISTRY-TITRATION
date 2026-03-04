<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>סימולטור טיטרציה מתקדם</title>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=Rubik:wght@300;400;600;700&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>
:root {
  --bg:#080c14; --panel:#0f1826; --panel2:#162030; --border:#1c2d42;
  --accent:#00d4ff; --accent-dim:rgba(0,212,255,.1); --accent-glow:rgba(0,212,255,.3);
  --green:#00e5a0; --green-dim:rgba(0,229,160,.1);
  --red:#ff4d6d; --red-dim:rgba(255,77,109,.1);
  --yellow:#ffd166; --yellow-dim:rgba(255,209,102,.1);
  --purple:#a78bfa; --purple-dim:rgba(167,139,250,.1);
  --orange:#ff9f43;
  --text:#e2eaf6; --text2:#6a84a0; --text3:#2e4460;
  --mono:'IBM Plex Mono',monospace; --sans:'Rubik',sans-serif;
  --r:12px;
}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:var(--sans);background:var(--bg);color:var(--text);min-height:100vh;padding:20px;
  background-image:radial-gradient(ellipse 70% 40% at 50% -5%,rgba(0,212,255,.06) 0%,transparent 60%)}
.app{max-width:1160px;margin:0 auto;display:flex;flex-direction:column;gap:18px;
  animation:fadeIn .5s ease}
@keyframes fadeIn{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:translateY(0)}}

/* ── HEADER ── */
header{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;
  padding:16px 24px;background:var(--panel);border:1px solid var(--border);border-radius:var(--r);
  border-top:2px solid var(--accent)}
.hdr-left h1{font-size:1.1rem;font-weight:700;letter-spacing:.02em}
.hdr-left p{font-size:.72rem;color:var(--text2);font-family:var(--mono);margin-top:2px}
.hdr-right{display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.status-pill{display:flex;align-items:center;gap:7px;padding:5px 13px;
  border-radius:20px;font-family:var(--mono);font-size:.72rem;
  background:var(--green-dim);border:1px solid rgba(0,229,160,.25);color:var(--green)}
.status-dot{width:6px;height:6px;border-radius:50%;background:var(--green);
  animation:pulse 2s infinite}
@keyframes pulse{0%,100%{box-shadow:0 0 0 0 rgba(0,229,160,.5)}50%{box-shadow:0 0 0 5px rgba(0,229,160,0)}}
.challenge-pill{display:flex;align-items:center;gap:7px;padding:5px 13px;
  border-radius:20px;font-family:var(--mono);font-size:.72rem;
  background:var(--yellow-dim);border:1px solid rgba(255,209,102,.3);color:var(--yellow)}
.challenge-dot{width:6px;height:6px;border-radius:50%;background:var(--yellow);
  animation:pulseyel 1.2s infinite}
@keyframes pulseyel{0%,100%{box-shadow:0 0 0 0 rgba(255,209,102,.6)}50%{box-shadow:0 0 0 5px rgba(255,209,102,0)}}

/* ── BUTTONS ── */
.btn{padding:9px 16px;border-radius:9px;border:1px solid var(--border);cursor:pointer;
  font-family:var(--sans);font-weight:600;font-size:.8rem;letter-spacing:.02em;
  transition:all .18s;display:inline-flex;align-items:center;justify-content:center;gap:6px}
.btn-accent{background:var(--accent-dim);border-color:rgba(0,212,255,.35);color:var(--accent)}
.btn-accent:hover{background:rgba(0,212,255,.18);border-color:var(--accent);box-shadow:0 0 14px rgba(0,212,255,.18)}
.btn-yellow{background:var(--yellow-dim);border-color:rgba(255,209,102,.35);color:var(--yellow)}
.btn-yellow:hover{background:rgba(255,209,102,.2);border-color:var(--yellow)}
.btn-red{background:var(--red-dim);border-color:rgba(255,77,109,.3);color:var(--red)}
.btn-red:hover{background:rgba(255,77,109,.2);border-color:var(--red)}
.btn-green{background:var(--green-dim);border-color:rgba(0,229,160,.3);color:var(--green)}
.btn-green:hover{background:rgba(0,229,160,.2);border-color:var(--green)}
.btn-purple{background:var(--purple-dim);border-color:rgba(167,139,250,.3);color:var(--purple)}
.btn-purple:hover{background:rgba(167,139,250,.2);border-color:var(--purple)}
.btn:active{transform:scale(.97)}
.btn:disabled{opacity:.4;cursor:not-allowed;transform:none}

/* ── PANELS ── */
.panel{background:var(--panel);border:1px solid var(--border);border-radius:var(--r);padding:20px}
.plabel{font-size:.65rem;font-family:var(--mono);color:var(--text3);text-transform:uppercase;
  letter-spacing:.1em;margin-bottom:8px}

/* ── MAIN GRID ── */
.main-grid{display:grid;grid-template-columns:290px 1fr;gap:18px}
@media(max-width:780px){.main-grid{grid-template-columns:1fr}}

/* ── LEFT PANEL ── */
.left-col{display:flex;flex-direction:column;gap:14px}

/* Acid type selector */
.acid-toggle{display:grid;grid-template-columns:1fr 1fr;gap:6px}
.acid-btn{padding:9px 8px;text-align:center;border-radius:8px;border:1px solid var(--border);
  cursor:pointer;font-size:.75rem;font-family:var(--mono);font-weight:600;
  color:var(--text2);background:var(--panel2);transition:all .2s}
.acid-btn.active-strong{background:var(--red-dim);border-color:rgba(255,77,109,.5);color:var(--red)}
.acid-btn.active-weak{background:rgba(255,159,67,.1);border-color:rgba(255,159,67,.5);color:var(--orange)}
.acid-btn:hover:not(.active-strong):not(.active-weak){background:var(--panel2);border-color:var(--text3);color:var(--text)}

/* LAB VISUAL */
.lab-visual{position:relative;display:flex;flex-direction:column;align-items:center;
  background:var(--panel2);border:1px solid var(--border);border-radius:10px;
  padding:18px 10px 14px;gap:4px}
.burette-label{font-size:.65rem;font-family:var(--mono);color:var(--accent);margin-bottom:4px;text-align:center}
.burette-outer{display:flex;flex-direction:column;align-items:center;margin-bottom:-2px;z-index:2}
.burette-body{width:20px;height:72px;background:linear-gradient(180deg,var(--panel) 0%,rgba(0,212,255,.12) 100%);
  border:1.5px solid rgba(0,212,255,.5);border-radius:3px 3px 0 0;position:relative;overflow:hidden}
.burette-fill{position:absolute;bottom:0;width:100%;background:rgba(0,212,255,.45);
  transition:height .5s cubic-bezier(.4,0,.2,1);height:80%}
.burette-scale{position:absolute;right:-8px;top:0;height:100%;display:flex;flex-direction:column;justify-content:space-between}
.burette-scale span{font-size:6px;font-family:var(--mono);color:var(--text3);line-height:1}
.burette-tap{width:8px;height:14px;background:rgba(0,212,255,.6);border-radius:0 0 3px 3px;position:relative}
.drip{width:4px;height:0;background:rgba(0,212,255,.85);border-radius:50% 50% 50% 50%/60% 60% 40% 40%;
  position:absolute;top:-3px;left:50%;transform:translateX(-50%)}
.drip.go{animation:dripfall .55s ease-in forwards}
@keyframes dripfall{0%{height:0;top:-3px;opacity:1}40%{height:7px;top:-3px;opacity:1}100%{height:5px;top:24px;opacity:0}}

/* Flask */
.flask-wrap{position:relative;width:130px;height:140px}
.flask-wrap canvas#vortex-canvas{position:absolute;top:0;left:0;pointer-events:none}

/* Ph bar */
.ph-bar-area{display:flex;flex-direction:column;gap:5px}
.ph-bar{height:9px;border-radius:5px;position:relative;
  background:linear-gradient(90deg,#ff4d6d 0%,#ff8c42 20%,#ffd166 35%,#00e5a0 50%,#00d4ff 65%,#a78bfa 100%)}
.ph-needle{position:absolute;top:-4px;width:3px;height:17px;background:#fff;border-radius:2px;
  box-shadow:0 0 8px rgba(255,255,255,.8);transition:left .4s cubic-bezier(.4,0,.2,1)}
.ph-ticks{display:flex;justify-content:space-between;font-family:var(--mono);font-size:.58rem;color:var(--text3)}

/* Metrics */
.metrics-row{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.metric{background:var(--panel2);border:1px solid var(--border);border-radius:9px;padding:12px;
  display:flex;flex-direction:column;gap:3px;transition:border-color .3s}
.metric-val{font-family:var(--mono);font-size:1.6rem;font-weight:600;line-height:1;
  color:var(--accent);transition:color .35s}
.metric-val.acidic{color:var(--red)}
.metric-val.neutral{color:var(--green)}
.metric-val.basic{color:var(--purple)}
.metric-unit{font-family:var(--mono);font-size:.65rem;color:var(--text2)}

/* Burette mode toggle */
.mode-toggle{display:flex;gap:0;border:1px solid var(--border);border-radius:8px;overflow:hidden}
.mode-btn{flex:1;padding:8px 6px;text-align:center;font-size:.72rem;font-family:var(--mono);
  cursor:pointer;border:none;background:var(--panel2);color:var(--text2);transition:all .2s}
.mode-btn.active{background:var(--accent-dim);color:var(--accent)}

/* Add buttons */
.add-btns{display:grid;grid-template-columns:1fr 1fr;gap:6px}
.add-btns .btn{font-family:var(--mono);font-size:.8rem;padding:10px 6px}

/* Indicator select */
.styled-sel{width:100%;background:var(--panel2);border:1px solid var(--border);border-radius:8px;
  color:var(--text);font-family:var(--sans);font-size:.78rem;padding:9px 11px;
  outline:none;cursor:pointer;transition:border-color .2s;-webkit-appearance:none}
.styled-sel:focus{border-color:var(--accent)}

/* Challenge banner */
.challenge-banner{display:none;background:linear-gradient(135deg,rgba(255,209,102,.08),rgba(255,159,67,.06));
  border:1px solid rgba(255,209,102,.3);border-radius:10px;padding:14px;
  font-size:.78rem;line-height:1.6;color:var(--yellow)}
.challenge-banner.show{display:block}
.challenge-banner strong{font-family:var(--mono)}

/* ── RIGHT COLUMN ── */
.right-col{display:flex;flex-direction:column;gap:18px}

/* Chart */
.chart-panel{background:var(--panel);border:1px solid var(--border);border-radius:var(--r);padding:20px}
.chart-hdr{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:14px;flex-wrap:wrap;gap:8px}
.chart-title{font-size:.88rem;font-weight:600}
.chart-sub{font-size:.7rem;color:var(--text2);font-family:var(--mono);margin-top:2px}
.eq-tag{display:none;font-family:var(--mono);font-size:.68rem;padding:4px 10px;
  border-radius:6px;background:var(--green-dim);border:1px solid rgba(0,229,160,.35);color:var(--green)}
.eq-tag.show{display:inline-flex;align-items:center;gap:5px}
.chart-box{position:relative;height:230px}

/* ── QUIZ ── */
.quiz-panel{background:var(--panel);border:1px solid var(--border);border-radius:var(--r);padding:20px;
  display:flex;flex-direction:column;gap:14px}
.quiz-phases{display:flex;gap:6px;flex-wrap:wrap}
.qphase{padding:4px 12px;border-radius:6px;font-size:.68rem;font-family:var(--mono);
  border:1px solid var(--border);color:var(--text3);background:var(--panel2);transition:all .3s}
.qphase.done{border-color:rgba(0,229,160,.4);color:var(--green);background:var(--green-dim)}
.qphase.active{border-color:rgba(255,209,102,.5);color:var(--yellow);background:var(--yellow-dim)}
.quiz-body{background:var(--panel2);border:1px solid var(--border);border-radius:10px;padding:16px;
  display:flex;flex-direction:column;gap:12px;min-height:110px;transition:all .3s}
.quiz-q{font-size:.82rem;line-height:1.65;color:var(--text)}
.quiz-hint{font-size:.73rem;font-family:var(--mono);color:var(--text2);padding:8px 10px;
  background:rgba(0,212,255,.05);border:1px solid rgba(0,212,255,.15);border-radius:6px}
/* Multiple choice */
.mc-options{display:grid;grid-template-columns:1fr 1fr;gap:7px}
.mc-opt{padding:9px 12px;border-radius:8px;border:1px solid var(--border);font-size:.78rem;
  cursor:pointer;transition:all .2s;background:var(--panel);color:var(--text2);text-align:right}
.mc-opt:hover{border-color:var(--accent);color:var(--text)}
.mc-opt.correct{background:var(--green-dim);border-color:rgba(0,229,160,.5);color:var(--green)}
.mc-opt.wrong{background:var(--red-dim);border-color:rgba(255,77,109,.4);color:var(--red)}
/* Text input question */
.quiz-input-row{display:flex;gap:8px}
.quiz-inp{flex:1;background:var(--panel);border:1px solid var(--border);border-radius:8px;
  color:var(--text);font-family:var(--mono);font-size:.82rem;padding:9px 12px;outline:none;
  transition:border-color .2s}
.quiz-inp:focus{border-color:var(--yellow)}
/* Feedback */
.qfb{padding:10px 13px;border-radius:8px;font-size:.78rem;font-family:var(--mono);display:none}
.qfb.ok{display:block;background:var(--green-dim);border:1px solid rgba(0,229,160,.3);color:var(--green)}
.qfb.no{display:block;background:var(--red-dim);border:1px solid rgba(255,77,109,.3);color:var(--red)}
/* Locked quiz */
.quiz-locked{text-align:center;padding:20px;font-size:.8rem;color:var(--text3);font-family:var(--mono)}

/* ── BOTTOM ROW ── */
.bottom-row{display:grid;grid-template-columns:1fr 340px;gap:18px}
@media(max-width:780px){.bottom-row{grid-template-columns:1fr}}

/* Table */
.table-panel{background:var(--panel);border:1px solid var(--border);border-radius:var(--r);overflow:hidden}
.table-hdr{display:flex;align-items:center;justify-content:space-between;padding:13px 18px;
  border-bottom:1px solid var(--border)}
.table-hdr-title{font-size:.78rem;font-weight:600;font-family:var(--mono);color:var(--text2)}
.table-hdr-right{display:flex;align-items:center;gap:8px}
.row-cnt{font-family:var(--mono);font-size:.68rem;color:var(--text3)}
.table-scroll{max-height:170px;overflow-y:auto}
.table-scroll::-webkit-scrollbar{width:4px}
.table-scroll::-webkit-scrollbar-thumb{background:var(--border);border-radius:2px}
table{width:100%;border-collapse:collapse}
thead th{padding:9px 14px;text-align:center;font-family:var(--mono);font-size:.63rem;
  color:var(--text3);text-transform:uppercase;letter-spacing:.08em;
  background:var(--panel2);border-bottom:1px solid var(--border);position:sticky;top:0}
tbody td{padding:8px 14px;text-align:center;font-family:var(--mono);font-size:.75rem;
  border-bottom:1px solid rgba(28,45,66,.5)}
tbody tr:hover td{background:var(--panel2)}
tbody tr:last-child td{border-bottom:none}
.swatch{width:26px;height:16px;border-radius:4px;margin:0 auto;border:1px solid var(--border)}
@keyframes rowIn{from{opacity:0;background:rgba(0,212,255,.07)}to{opacity:1;background:transparent}}
tbody tr.fresh{animation:rowIn .45s ease}

/* Params panel */
.params-panel{background:var(--panel);border:1px solid var(--border);border-radius:var(--r);padding:20px;
  display:flex;flex-direction:column;gap:14px}
.params-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.param-card{background:var(--panel2);border:1px solid var(--border);border-radius:9px;padding:12px}
.param-val{font-family:var(--mono);font-size:.95rem;font-weight:600;margin-top:2px;transition:all .3s}
.param-val.hidden-val{color:var(--yellow);letter-spacing:.05em}
.param-sub{font-family:var(--mono);font-size:.65rem;color:var(--text3);margin-top:2px}

/* Challenge answer row */
.challenge-answer{display:none;flex-direction:column;gap:10px;background:rgba(255,209,102,.05);
  border:1px solid rgba(255,209,102,.25);border-radius:10px;padding:14px}
.challenge-answer.show{display:flex}
.challenge-answer-row{display:flex;gap:8px}
.challenge-answer-inp{flex:1;background:var(--panel);border:1px solid var(--border);border-radius:8px;
  color:var(--text);font-family:var(--mono);font-size:.82rem;padding:9px 12px;outline:none;
  transition:border-color .2s}
.challenge-answer-inp:focus{border-color:var(--yellow)}
.challenge-fb{padding:9px 12px;border-radius:7px;font-family:var(--mono);font-size:.75rem;display:none}
.challenge-fb.ok{display:block;background:var(--green-dim);border:1px solid rgba(0,229,160,.3);color:var(--green)}
.challenge-fb.no{display:block;background:var(--red-dim);border:1px solid rgba(255,77,109,.3);color:var(--red)}

/* Eq flash */
@keyframes eqFlash{0%{border-color:var(--green);box-shadow:0 0 0 0 rgba(0,229,160,.5)}
  50%{box-shadow:0 0 0 10px rgba(0,229,160,0)}100%{border-color:var(--border)}}
.eq-flash{animation:eqFlash 1s ease}

/* Confetti */
.confetti-wrap{position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:9999}
.confetti-piece{position:absolute;width:8px;height:10px;border-radius:2px;
  animation:confettiFall 2.5s ease-in forwards}
@keyframes confettiFall{0%{transform:translateY(-20px) rotate(0deg);opacity:1}
  100%{transform:translateY(110vh) rotate(720deg);opacity:0}}
</style>
</head>
<body>
<div class="app">

<!-- ══ HEADER ══ -->
<header>
  <div class="hdr-left">
    <h1>סימולטור טיטרציה מתקדם &mdash; חומצה × בסיס חזק</h1>
    <p id="hdr-sub">HCl (חומצה הידרוכלורית) ← NaOH (נתרן הידרוקסידי) 0.1M</p>
  </div>
  <div class="hdr-right">
    <div id="normal-status" class="status-pill"><div class="status-dot"></div>מצב רגיל</div>
    <div id="challenge-status" class="challenge-pill" style="display:none"><div class="challenge-dot"></div>מצב בחינה פעיל</div>
    <button class="btn btn-yellow" onclick="startChallenge()">⬡ התחל מצב בחינה</button>
  </div>
</header>

<!-- ══ MAIN GRID ══ -->
<div class="main-grid">

  <!-- LEFT -->
  <div class="left-col">

    <!-- Acid type -->
    <div class="panel" style="padding:14px">
      <div class="plabel">סוג חומצה</div>
      <div class="acid-toggle">
        <div class="acid-btn active-strong" id="btn-strong" onclick="setAcidType('strong')">
          <div style="font-size:.8rem">HCl</div>
          <div style="font-size:.62rem;margin-top:2px;opacity:.7">חומצה הידרוכלורית</div>
        </div>
        <div class="acid-btn" id="btn-weak" onclick="setAcidType('weak')">
          <div style="font-size:.8rem">CH₃COOH</div>
          <div style="font-size:.62rem;margin-top:2px;opacity:.7">חומצה אצטית (pKa=4.76)</div>
        </div>
      </div>
    </div>

    <!-- Lab visual -->
    <div class="panel" id="lab-panel" style="padding:14px">
      <div class="lab-visual">
        <div class="burette-label">ביורטה — NaOH נתרן הידרוקסידי</div>
        <div class="burette-outer">
          <div class="burette-body">
            <div class="burette-fill" id="burette-fill"></div>
            <div class="burette-scale">
              <span>0</span><span>10</span><span>20</span><span>30</span><span>40</span>
            </div>
          </div>
          <div class="burette-tap">
            <div class="drip" id="drip"></div>
          </div>
        </div>
        <div class="flask-wrap">
          <svg width="130" height="140" viewBox="0 0 130 140" id="flask-svg">
            <defs>
              <clipPath id="fc"><polygon points="52,10 78,10 78,58 118,128 12,128"/></clipPath>
            </defs>
            <rect id="flask-liquid" x="0" y="0" width="130" height="140"
              fill="rgba(200,230,255,.1)" clip-path="url(#fc)" style="transition:fill .5s ease"/>
            <polygon points="52,10 78,10 78,58 118,128 12,128"
              fill="none" stroke="#2e4460" stroke-width="2.2" stroke-linejoin="round"/>
            <line x1="48" y1="10" x2="82" y2="10" stroke="#2e4460" stroke-width="2.2" stroke-linecap="round"/>
            <line x1="56" y1="22" x2="60" y2="72" stroke="rgba(255,255,255,.06)" stroke-width="5" stroke-linecap="round"/>
          </svg>
          <canvas id="vortex-canvas" width="130" height="140" style="position:absolute;top:0;left:0;pointer-events:none"></canvas>
        </div>
        <div style="font-size:.65rem;font-family:var(--mono);color:var(--text3);margin-top:2px">
          ארלנמייר — 25 מ"ל
        </div>
      </div>

      <!-- pH bar -->
      <div class="ph-bar-area" style="margin-top:12px">
        <div class="plabel">סקלת pH</div>
        <div class="ph-bar">
          <div class="ph-needle" id="ph-needle" style="left:7.14%"></div>
        </div>
        <div class="ph-ticks">
          <span>0</span><span>2</span><span>4</span><span>7</span><span>9</span><span>11</span><span>14</span>
        </div>
      </div>

      <!-- Metrics -->
      <div class="metrics-row" style="margin-top:12px">
        <div class="metric">
          <div class="plabel">נפח בסיס</div>
          <div class="metric-val acidic" id="vol-display">0.0</div>
          <div class="metric-unit">מ"ל</div>
        </div>
        <div class="metric">
          <div class="plabel">pH נוכחי</div>
          <div class="metric-val acidic" id="ph-display">1.00</div>
          <div class="metric-unit">ערך</div>
        </div>
      </div>
    </div>

    <!-- Burette mode -->
    <div class="panel" style="padding:14px">
      <div class="plabel">מצב ביורטה</div>
      <div class="mode-toggle" style="margin-bottom:10px">
        <div class="mode-btn active" id="mode-stream" onclick="setMode('stream')">⥤ זרם (מ"ל)</div>
        <div class="mode-btn" id="mode-drops" onclick="setMode('drops')">💧 טיפות (מ"ל)</div>
      </div>
      <div class="add-btns" id="add-btns">
        <button class="btn btn-accent" onclick="addTitrant(1.0)">＋ 1.0 מ"ל</button>
        <button class="btn btn-accent" onclick="addTitrant(0.5)">＋ 0.5 מ"ל</button>
        <button class="btn btn-accent" onclick="addTitrant(0.1)">＋ 0.1 מ"ל</button>
        <button class="btn btn-red" onclick="resetSimulation()">↺ איפוס</button>
      </div>
    </div>

    <!-- Indicator -->
    <div class="panel" style="padding:14px">
      <div class="plabel">אינדיקטור</div>
      <select class="styled-sel" id="indicator" onchange="updateLiquid()">
        <option value="phenolphthalein">פנולפתלאין (חסר צבע / ורוד)</option>
        <option value="universal">אינדיקטור אוניברסלי</option>
      </select>
    </div>

  </div><!-- /left-col -->

  <!-- RIGHT -->
  <div class="right-col">

    <!-- Chart -->
    <div class="chart-panel">
      <div class="chart-hdr">
        <div>
          <div class="chart-title">עקומת טיטרציה</div>
          <div class="chart-sub" id="chart-sub-lbl">pH כפונקציה של נפח NaOH</div>
        </div>
        <div id="eq-tag" class="eq-tag">⬥ נ.מ. — pH = <span id="eq-ph-val">7.00</span></div>
      </div>
      <div class="chart-box">
        <canvas id="titrationChart"></canvas>
      </div>
    </div>

    <!-- Dynamic Quiz -->
    <div class="quiz-panel">
      <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px">
        <div style="font-size:.88rem;font-weight:600;display:flex;align-items:center;gap:8px">
          <span style="color:var(--yellow)">⬡</span> מרכז שאלות אינטראקטיבי
        </div>
        <div class="quiz-phases">
          <div class="qphase active" id="qp0">לפני הניסוי</div>
          <div class="qphase" id="qp1">אמצע הניסוי</div>
          <div class="qphase" id="qp2">נקודת מקבילות</div>
        </div>
      </div>
      <div class="quiz-body" id="quiz-body">
        <!-- populated by JS -->
      </div>
    </div>

  </div><!-- /right-col -->
</div><!-- /main-grid -->

<!-- ══ BOTTOM ROW ══ -->
<div class="bottom-row">

  <!-- Data table -->
  <div class="table-panel">
    <div class="table-hdr">
      <div class="table-hdr-title">יומן מדידות</div>
      <div class="table-hdr-right">
        <span class="row-cnt" id="row-cnt">0 רשומות</span>
        <button class="btn btn-green" style="padding:6px 12px;font-size:.72rem" onclick="exportCSV()">
          ⬇ ייצוא CSV
        </button>
      </div>
    </div>
    <div class="table-scroll">
      <table>
        <thead>
          <tr>
            <th>נפח בסיס (מ"ל)</th>
            <th>pH</th>
            <th>שלב</th>
            <th>מולים H⁺ נותרים</th>
            <th>צבע</th>
          </tr>
        </thead>
        <tbody id="data-body"></tbody>
      </table>
    </div>
  </div>

  <!-- Params + challenge answer -->
  <div class="params-panel">
    <div class="plabel">פרמטרי הניסוי</div>
    <div class="params-grid">
      <div class="param-card">
        <div class="plabel">חומצה</div>
        <div class="param-val" id="p-acid-name" style="color:var(--red);font-size:.82rem">HCl</div>
        <div class="param-sub">25.0 מ"ל</div>
      </div>
      <div class="param-card">
        <div class="plabel">ריכוז חומצה</div>
        <div class="param-val" id="p-acid-conc" style="color:var(--red)">0.100 M</div>
        <div class="param-sub">c<sub>a</sub></div>
      </div>
      <div class="param-card">
        <div class="plabel">בסיס (NaOH)</div>
        <div class="param-val" style="color:var(--purple);font-size:.82rem">נתרן הידרוקסידי</div>
        <div class="param-sub">0.100 M</div>
      </div>
      <div class="param-card">
        <div class="plabel">נ.מ. תיאורטית</div>
        <div class="param-val" id="p-eq" style="color:var(--green)">25.0 מ"ל</div>
        <div class="param-sub" id="p-eq-ph">pH = 7.00</div>
      </div>
    </div>

    <!-- Challenge answer box -->
    <div class="challenge-answer" id="challenge-answer-box">
      <div style="font-size:.75rem;color:var(--yellow);font-family:var(--mono)">
        ⬡ נקודת המקבילות הושגה! חשב את ריכוז החומצה:
      </div>
      <div style="font-size:.7rem;color:var(--text2);font-family:var(--mono)">
        C<sub>a</sub> = (C<sub>b</sub> × V<sub>b</sub>) / V<sub>a</sub>
      </div>
      <div class="challenge-answer-row">
        <input class="challenge-answer-inp" type="number" id="challenge-ans-inp"
          placeholder="0.000" step="0.001" min="0">
        <button class="btn btn-yellow" style="padding:9px 14px" onclick="checkChallengeAnswer()">בדוק</button>
      </div>
      <div class="challenge-fb" id="challenge-fb"></div>
    </div>
  </div>

</div><!-- /bottom-row -->
</div><!-- /app -->

<script>
// ══════════════════════════════════════════════
//  STATE
// ══════════════════════════════════════════════
let vAcid = 25, cAcid = 0.1, cBase = 0.1, vBaseTotal = 0;
let acidType = 'strong';   // 'strong' | 'weak'
let buretteMode = 'stream';
let challengeMode = false;
let hiddenConc = 0.1;
let chart, rowCount = 0;
let eqReached = false;
let eqVolume = 0;
let dataLog = [];
const dataPoints = [{x:0, y:calculatePH(0)}];
// Quiz state
let quizPhase = 0; // 0=pre, 1=mid, 2=post
let quizDone = [false, false, false];
let midQuizTriggered = false;
let postQuizTriggered = false;
// Vortex
let vortexAngle = 0, vortexRAF = null, vortexActive = false;

// ══════════════════════════════════════════════
//  pH ENGINE
// ══════════════════════════════════════════════
function calculatePH(vBase) {
  const pKa = 4.76;
  const molesAcid = (cAcid * vAcid) / 1000;
  const molesBase = (cBase * vBase) / 1000;
  const totalVol = (vAcid + vBase) / 1000;

  if (acidType === 'strong') {
    if (vBase === 0) return -Math.log10(cAcid);
    if (molesAcid > molesBase) {
      return -Math.log10((molesAcid - molesBase) / totalVol);
    } else if (molesBase > molesAcid) {
      const concOH = (molesBase - molesAcid) / totalVol;
      return 14 + Math.log10(concOH);
    }
    return 7.0;
  }

  // WEAK ACID (acetic acid)
  if (vBase === 0) {
    const Ka = Math.pow(10, -pKa);
    const H = (-Ka + Math.sqrt(Ka * Ka + 4 * Ka * cAcid)) / 2;
    return -Math.log10(H);
  }
  if (molesBase < molesAcid) {
    // Buffer region — Henderson-Hasselbalch
    if (molesBase < 0.00001) {
      const Ka = Math.pow(10, -pKa);
      const H = (-Ka + Math.sqrt(Ka * Ka + 4 * Ka * cAcid)) / 2;
      return -Math.log10(H);
    }
    return pKa + Math.log10(molesBase / (molesAcid - molesBase));
  } else if (molesBase > molesAcid) {
    // Excess base
    const concOH = (molesBase - molesAcid) / totalVol;
    return 14 + Math.log10(concOH);
  }
  // Equivalence point — acetate hydrolysis
  const Kw = 1e-14, Ka = Math.pow(10, -pKa);
  const Kb = Kw / Ka;
  const cSalt = molesAcid / totalVol;
  const OH = Math.sqrt(Kb * cSalt);
  return 14 - (-Math.log10(OH));
}

function getEqPH() {
  if (acidType === 'strong') return 7.0;
  const pKa = 4.76, Kw = 1e-14, Ka = Math.pow(10, -pKa), Kb = Kw / Ka;
  const molesAcid = (cAcid * vAcid) / 1000;
  const totalVol = (vAcid + vAcid) / 1000; // at equivalence Vb = Va (equal conc)
  const cSalt = molesAcid / totalVol;
  const OH = Math.sqrt(Kb * cSalt);
  return 14 - (-Math.log10(OH));
}

function theoreticalEqVol() {
  return (cAcid * vAcid) / cBase;
}

// ══════════════════════════════════════════════
//  LIQUID COLOR
// ══════════════════════════════════════════════
function getLiquidColor(ph) {
  const ind = document.getElementById('indicator').value;
  if (ind === 'phenolphthalein') {
    return ph > 8.2 ? 'rgba(220,80,200,.6)' : 'rgba(200,230,255,.12)';
  }
  if (ph < 3)  return 'rgba(255,77,109,.6)';
  if (ph < 5)  return 'rgba(255,140,66,.6)';
  if (ph < 7)  return 'rgba(255,209,102,.5)';
  if (ph < 8.5)return 'rgba(0,229,160,.45)';
  if (ph < 11) return 'rgba(0,212,255,.5)';
  return 'rgba(167,139,250,.6)';
}

function getPhaseLabel(ph) {
  if (ph < 6.9) return 'חומצי';
  if (ph > 7.1) return 'בסיסי';
  return '⬥ נ.מ.';
}

function getPhaseColor(ph) {
  if (ph < 6.9) return 'var(--red)';
  if (ph > 7.1) return 'var(--purple)';
  return 'var(--green)';
}

// ══════════════════════════════════════════════
//  UI UPDATE
// ══════════════════════════════════════════════
function updateUI(ph) {
  const color = getLiquidColor(ph);
  document.getElementById('flask-liquid').setAttribute('fill', color);

  // pH needle
  const pct = Math.max(0, Math.min(100, (ph / 14) * 100));
  document.getElementById('ph-needle').style.left = `calc(${pct}% - 1.5px)`;

  // pH value color
  const el = document.getElementById('ph-display');
  el.className = 'metric-val';
  if (ph < 6.9) el.classList.add('acidic');
  else if (ph > 7.1) el.classList.add('basic');
  else el.classList.add('neutral');

  // Burette depletion
  const pctUsed = Math.min(vBaseTotal / 50, 1);
  document.getElementById('burette-fill').style.height = `${Math.max(0,(1-pctUsed)*100)}%`;

  return color;
}

function updateLiquid() {
  const ph = parseFloat(document.getElementById('ph-display').innerText) || 1;
  updateUI(ph);
}

// ══════════════════════════════════════════════
//  VORTEX ANIMATION
// ══════════════════════════════════════════════
function startVortex() {
  if (vortexActive) return;
  vortexActive = true;
  const canvas = document.getElementById('vortex-canvas');
  const ctx = canvas.getContext('2d');
  const cx = 65, cy = 96; // center of flask liquid

  function frame() {
    ctx.clearRect(0,0,130,140);
    vortexAngle += 0.07;
    ctx.save();
    ctx.beginPath();
    ctx.moveTo(52,10); ctx.lineTo(78,10); ctx.lineTo(78,58);
    ctx.lineTo(118,128); ctx.lineTo(12,128); ctx.closePath();
    ctx.clip();
    for (let i=0; i<5; i++) {
      const a = vortexAngle + (i * Math.PI * 2 / 5);
      const r = 6 + i * 5;
      ctx.beginPath();
      ctx.strokeStyle = `rgba(255,255,255,${0.18 - i*0.03})`;
      ctx.lineWidth = 1.5;
      ctx.arc(cx, cy, r, a, a + Math.PI * 1.6);
      ctx.stroke();
    }
    ctx.restore();
    vortexRAF = requestAnimationFrame(frame);
  }
  frame();
  setTimeout(() => {
    vortexActive = false;
    cancelAnimationFrame(vortexRAF);
    const ctx2 = document.getElementById('vortex-canvas').getContext('2d');
    ctx2.clearRect(0,0,130,140);
  }, 1600);
}

function triggerDrip() {
  const d = document.getElementById('drip');
  d.classList.remove('go');
  void d.offsetWidth;
  d.classList.add('go');
}

// ══════════════════════════════════════════════
//  ADD TITRANT
// ══════════════════════════════════════════════
function addTitrant(amt) {
  vBaseTotal = parseFloat((vBaseTotal + amt).toFixed(3));
  const ph = calculatePH(vBaseTotal);

  document.getElementById('vol-display').innerText = vBaseTotal.toFixed(2);
  document.getElementById('ph-display').innerText = ph.toFixed(2);

  const color = updateUI(ph);
  triggerDrip();
  startVortex();

  // Equivalence detection
  const eqVol = theoreticalEqVol();
  const eqPH = getEqPH();
  if (!eqReached && Math.abs(vBaseTotal - eqVol) < (buretteMode === 'drops' ? 0.1 : 0.6)) {
    const measuredPH = calculatePH(eqVol);
    if (Math.abs(ph - eqPH) < 0.25 || vBaseTotal >= eqVol) {
      eqReached = true;
      eqVolume = vBaseTotal;
      document.getElementById('eq-tag').classList.add('show');
      document.getElementById('eq-ph-val').innerText = ph.toFixed(2);
      document.getElementById('lab-panel').classList.add('eq-flash');
      setTimeout(() => document.getElementById('lab-panel').classList.remove('eq-flash'), 1000);
      if (challengeMode) {
        document.getElementById('challenge-answer-box').classList.add('show');
      }
      showQuiz(2);
    }
  }

  // Mid-point quiz trigger (at ~50% of eq vol)
  if (!midQuizTriggered && vBaseTotal >= eqVol * 0.45 && vBaseTotal <= eqVol * 0.6) {
    midQuizTriggered = true;
    if (!quizDone[0]) { quizDone[0] = true; markPhase(0,'done'); }
    showQuiz(1);
  }

  addRow(vBaseTotal, ph, color);
  dataPoints.push({x: vBaseTotal, y: parseFloat(ph.toFixed(3))});
  chart.update();
}

// ══════════════════════════════════════════════
//  TABLE
// ══════════════════════════════════════════════
function addRow(v, ph, color) {
  rowCount++;
  document.getElementById('row-cnt').innerText = `${rowCount} רשומות`;
  const molesH = Math.max(0, (cAcid*vAcid - cBase*v) / 1000);
  const phase = getPhaseLabel(ph);
  const phColor = getPhaseColor(ph);
  const tr = document.createElement('tr');
  tr.className = 'fresh';
  tr.innerHTML = `
    <td>${v.toFixed(2)}</td>
    <td style="color:${phColor}">${ph.toFixed(2)}</td>
    <td style="color:${phColor};font-size:.68rem">${phase}</td>
    <td style="font-family:var(--mono);font-size:.7rem">${molesH < 1e-9 ? '0.000000' : molesH.toExponential(3)}</td>
    <td><div class="swatch" style="background:${color}"></div></td>
  `;
  dataLog.push({v: v.toFixed(2), ph: ph.toFixed(2), phase, color});
  document.getElementById('data-body').prepend(tr);
  setTimeout(() => tr.classList.remove('fresh'), 500);
}

// ══════════════════════════════════════════════
//  EXPORT CSV
// ══════════════════════════════════════════════
function exportCSV() {
  if (dataLog.length === 0) { alert('אין נתונים לייצוא. בצע טיטרציה תחילה.'); return; }
  const header = 'נפח NaOH (מ"ל),pH,שלב\n';
  const rows = dataLog.map(r => `${r.v},${r.ph},${r.phase}`).join('\n');
  const bom = '\uFEFF';
  const blob = new Blob([bom + header + rows], {type:'text/csv;charset=utf-8'});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url; a.download = 'titration_data.csv'; a.click();
  URL.revokeObjectURL(url);
}

// ══════════════════════════════════════════════
//  DYNAMIC QUIZ
// ══════════════════════════════════════════════
const quizDefs = [
  // Phase 0 — pre
  {
    phase: 'לפני הניסוי',
    type: 'input',
    q: () => acidType === 'strong'
      ? 'מהו ה-pH ההתחלתי של תמיסת HCl בריכוז 0.1M? (חשב –log[H⁺])'
      : 'מהו ה-pH ההתחלתי המשוער של תמיסת CH₃COOH בריכוז 0.1M? (pKa = 4.76)',
    hint: () => acidType === 'strong'
      ? 'רמז: pH = –log(0.1)'
      : 'רמז: pH ≈ ½(pKa – log C) ≈ ½(4.76 – (–1))',
    check: (v) => {
      const expected = parseFloat(calculatePH(0).toFixed(2));
      return Math.abs(parseFloat(v) - expected) < 0.1;
    },
    successText: () => `✓ נכון! pH ≈ ${calculatePH(0).toFixed(2)}`,
    failText: () => `✗ נסה שוב. pH = ${calculatePH(0).toFixed(2)} — ודא את החישוב`
  },
  // Phase 1 — mid
  {
    phase: 'אמצע הניסוי',
    type: 'mc',
    q: () => `הוספת ~${(theoreticalEqVol()/2).toFixed(1)} מ"ל בסיס (חצי הדרך לנ.מ.). מה נכון?`,
    opts: [
      () => 'n(H⁺) = n(OH⁻)',
      () => `n(H⁺) ≈ 2·n(OH⁻)`,
      () => 'n(OH⁻) > n(H⁺)',
      () => 'pH = 7'
    ],
    correct: 1,
    successText: () => '✓ נכון! הוספת חצי מהכמות הנדרשת, לכן n(H⁺) ≈ 2·n(OH⁻)',
    failText: () => '✗ שגוי. בחצי הדרך טרם הסתיים הנטרול — n(H⁺) עדיין גדול מ-n(OH⁻)'
  },
  // Phase 2 — post
  {
    phase: 'נקודת מקבילות',
    type: 'input',
    q: () => challengeMode
      ? `נ.מ. הושגה בנפח ${eqVolume.toFixed(1)} מ"ל! השתמש בנוסחה לחישוב ריכוז החומצה.`
      : `נ.מ. הושגה! בנפח ${eqVolume.toFixed(1)} מ"ל, מהו ריכוז החומצה? (M)`,
    hint: () => `Ca = (Cb × Vb) / Va = (0.1 × Vb) / 25`,
    check: (v) => Math.abs(parseFloat(v) - cAcid) < 0.008,
    successText: () => `✓ מצוין! Ca = (0.1 × ${eqVolume.toFixed(1)}) / 25 = ${cAcid.toFixed(3)} M`,
    failText: () => `✗ נסה שוב. Ca = (Cb × Vb) / Va`
  }
];

function showQuiz(phase) {
  quizPhase = phase;
  markPhase(phase, 'active');
  const def = quizDefs[phase];
  const body = document.getElementById('quiz-body');
  body.style.opacity='0';
  setTimeout(() => {
    body.style.opacity='1';
    if (quizDone[phase]) {
      body.innerHTML = `<div style="color:var(--green);font-family:var(--mono);font-size:.8rem;display:flex;align-items:center;gap:8px;padding:10px 0">
        ✓ שאלה זו נענתה בהצלחה!</div>`;
      return;
    }
    let html = `<div class="quiz-q">${def.q()}</div>`;
    if (def.hint) html += `<div class="quiz-hint">${def.hint()}</div>`;
    if (def.type === 'mc') {
      html += `<div class="mc-options" id="mc-opts">`;
      def.opts.forEach((o,i) => {
        html += `<div class="mc-opt" onclick="answerMC(${i})">${String.fromCharCode(65+i)}. ${o()}</div>`;
      });
      html += '</div>';
    } else {
      html += `<div class="quiz-input-row">
        <input class="quiz-inp" id="q-inp" type="number" placeholder="0.00" step="0.01">
        <button class="btn btn-yellow" style="padding:9px 14px;font-size:.78rem" onclick="answerInput(${phase})">בדוק ↵</button>
      </div>`;
    }
    html += `<div class="qfb" id="qfb"></div>`;
    body.innerHTML = html;
    if (def.type === 'input') {
      const inp = document.getElementById('q-inp');
      inp && inp.addEventListener('keydown', e => {
        if (e.key === 'Enter') answerInput(phase);
      });
    }
  }, 200);
  body.style.transition = 'opacity .2s';
}

function answerMC(idx) {
  const def = quizDefs[1];
  const opts = document.querySelectorAll('.mc-opt');
  opts.forEach((o,i) => {
    o.style.pointerEvents = 'none';
    if (i === def.correct) o.classList.add('correct');
    else if (i === idx && idx !== def.correct) o.classList.add('wrong');
  });
  const fb = document.getElementById('qfb');
  if (idx === def.correct) {
    fb.className = 'qfb ok'; fb.innerText = def.successText();
    quizDone[1] = true; markPhase(1,'done');
  } else {
    fb.className = 'qfb no'; fb.innerText = def.failText();
  }
}

function answerInput(phase) {
  const inp = document.getElementById('q-inp');
  const val = inp ? inp.value : '';
  const def = quizDefs[phase];
  const fb = document.getElementById('qfb');
  if (def.check(val)) {
    fb.className = 'qfb ok'; fb.innerText = def.successText();
    quizDone[phase] = true; markPhase(phase,'done');
  } else {
    fb.className = 'qfb no'; fb.innerText = def.failText();
  }
}

function markPhase(idx, state) {
  const el = document.getElementById(`qp${idx}`);
  el.className = 'qphase ' + state;
}

// ══════════════════════════════════════════════
//  CHALLENGE MODE
// ══════════════════════════════════════════════
function startChallenge() {
  const choices = [0.05,0.06,0.07,0.08,0.09,0.10,0.11,0.12,0.13,0.14,0.15];
  hiddenConc = choices[Math.floor(Math.random() * choices.length)];
  cAcid = hiddenConc;
  challengeMode = true;
  resetSimulation(true);

  document.getElementById('normal-status').style.display='none';
  document.getElementById('challenge-status').style.display='flex';
  document.getElementById('p-acid-conc').textContent = '??? M';
  document.getElementById('p-acid-conc').className = 'param-val hidden-val';

  // Recalculate eq vol
  const eqVol = theoreticalEqVol().toFixed(1);
  document.getElementById('p-eq').textContent = '? מ"ל';
  document.getElementById('p-eq-ph').textContent = acidType==='strong' ? 'pH = 7.00' : 'pH > 7';
}

function checkChallengeAnswer() {
  const val = parseFloat(document.getElementById('challenge-ans-inp').value);
  const fb = document.getElementById('challenge-fb');
  if (Math.abs(val - hiddenConc) < 0.008) {
    fb.className = 'challenge-fb ok';
    fb.innerText = `✓ מדויק! הריכוז הסודי היה ${hiddenConc.toFixed(3)} M — חישוב נהדר!`;
    document.getElementById('p-acid-conc').textContent = `${hiddenConc.toFixed(3)} M`;
    document.getElementById('p-acid-conc').className = 'param-val';
    document.getElementById('p-acid-conc').style.color = 'var(--green)';
    launchConfetti();
  } else {
    fb.className = 'challenge-fb no';
    const diff = (val - hiddenConc).toFixed(3);
    const dir = val > hiddenConc ? 'גבוה מדי' : 'נמוך מדי';
    fb.innerText = `✗ לא מדויק (${dir}). נסה שוב — רמז: Vב = ${eqVolume.toFixed(2)} מ"ל`;
  }
}

// ══════════════════════════════════════════════
//  CONFETTI
// ══════════════════════════════════════════════
function launchConfetti() {
  const wrap = document.createElement('div');
  wrap.className = 'confetti-wrap';
  document.body.appendChild(wrap);
  const colors = ['#00d4ff','#00e5a0','#ffd166','#ff4d6d','#a78bfa','#ff9f43'];
  for (let i=0; i<60; i++) {
    const p = document.createElement('div');
    p.className = 'confetti-piece';
    p.style.cssText = `left:${Math.random()*100}%;top:-10px;background:${colors[i%colors.length]};
      animation-delay:${Math.random()*.8}s;animation-duration:${1.8+Math.random()}s;
      transform:rotate(${Math.random()*360}deg);width:${6+Math.random()*6}px;height:${8+Math.random()*6}px`;
    wrap.appendChild(p);
  }
  setTimeout(() => wrap.remove(), 4000);
}

// ══════════════════════════════════════════════
//  ACID TYPE & BURETTE MODE
// ══════════════════════════════════════════════
function setAcidType(type) {
  acidType = type;
  document.getElementById('btn-strong').className = 'acid-btn' + (type==='strong'?' active-strong':'');
  document.getElementById('btn-weak').className = 'acid-btn' + (type==='weak'?' active-weak':'');
  const nameEl = document.getElementById('p-acid-name');
  const subEl = document.getElementById('p-eq-ph');
  if (type === 'weak') {
    nameEl.textContent = 'CH₃COOH'; nameEl.style.color = 'var(--orange)';
    subEl.textContent = 'pH > 7 (הידרוליזה)';
    document.getElementById('hdr-sub').textContent = 'CH₃COOH (חומצה אצטית) ← NaOH 0.1M';
  } else {
    nameEl.textContent = 'HCl'; nameEl.style.color = 'var(--red)';
    subEl.textContent = 'pH = 7.00';
    document.getElementById('hdr-sub').textContent = 'HCl (חומצה הידרוכלורית) ← NaOH 0.1M';
  }
  resetSimulation();
}

function setMode(mode) {
  buretteMode = mode;
  document.getElementById('mode-stream').className = 'mode-btn' + (mode==='stream' ? ' active':'');
  document.getElementById('mode-drops').className = 'mode-btn' + (mode==='drops' ? ' active':'');
  const btns = document.getElementById('add-btns');
  if (mode === 'stream') {
    btns.innerHTML = `
      <button class="btn btn-accent" onclick="addTitrant(1.0)">＋ 1.0 מ"ל</button>
      <button class="btn btn-accent" onclick="addTitrant(0.5)">＋ 0.5 מ"ל</button>
      <button class="btn btn-accent" onclick="addTitrant(0.1)">＋ 0.1 מ"ל</button>
      <button class="btn btn-red" onclick="resetSimulation()">↺ איפוס</button>`;
  } else {
    btns.innerHTML = `
      <button class="btn btn-accent" onclick="addTitrant(0.05)">💧 0.05 מ"ל</button>
      <button class="btn btn-accent" onclick="addTitrant(0.02)">💧 0.02 מ"ל</button>
      <button class="btn btn-accent" onclick="addTitrant(0.1)">＋ 0.1 מ"ל</button>
      <button class="btn btn-red" onclick="resetSimulation()">↺ איפוס</button>`;
  }
}

// ══════════════════════════════════════════════
//  RESET
// ══════════════════════════════════════════════
function resetSimulation(keepChallenge) {
  vBaseTotal = 0; rowCount = 0; eqReached = false; eqVolume = 0;
  midQuizTriggered = false; postQuizTriggered = false;
  quizDone = [false,false,false]; quizPhase = 0;
  dataLog = [];
  dataPoints.length = 0;
  const initPH = calculatePH(0);
  dataPoints.push({x:0, y:initPH});
  chart && chart.update();
  document.getElementById('data-body').innerHTML='';
  document.getElementById('row-cnt').innerText='0 רשומות';
  document.getElementById('vol-display').innerText='0.00';
  document.getElementById('ph-display').innerText=initPH.toFixed(2);
  document.getElementById('ph-display').className='metric-val acidic';
  document.getElementById('eq-tag').classList.remove('show');
  document.getElementById('ph-needle').style.left=`${(initPH/14)*100}%`;
  document.getElementById('flask-liquid').setAttribute('fill','rgba(200,230,255,.1)');
  document.getElementById('burette-fill').style.height='80%';
  document.getElementById('challenge-answer-box').classList.remove('show');
  document.getElementById('challenge-fb').className='challenge-fb';
  document.getElementById('challenge-ans-inp') && (document.getElementById('challenge-ans-inp').value='');
  if (!keepChallenge) {
    challengeMode = false;
    document.getElementById('normal-status').style.display='flex';
    document.getElementById('challenge-status').style.display='none';
    document.getElementById('p-acid-conc').textContent = `${cAcid.toFixed(3)} M`;
    document.getElementById('p-acid-conc').className='param-val';
    document.getElementById('p-acid-conc').style.color='var(--red)';
    const eqVol = theoreticalEqVol();
    document.getElementById('p-eq').textContent = `${eqVol.toFixed(1)} מ"ל`;
  }
  // Reset quiz phases
  [0,1,2].forEach(i => { document.getElementById(`qp${i}`).className='qphase'+(i===0?' active':'') });
  showQuiz(0);
}

// ══════════════════════════════════════════════
//  CHART INIT
// ══════════════════════════════════════════════
function initChart() {
  const ctx = document.getElementById('titrationChart').getContext('2d');
  chart = new Chart(ctx, {
    type:'line',
    data:{
      datasets:[{
        label:'pH',
        data: dataPoints,
        borderColor:'#00d4ff',
        borderWidth:2.5,
        pointRadius:0,
        pointHoverRadius:5,
        pointHoverBackgroundColor:'#00d4ff',
        tension:0.35,
        fill:{target:'origin',above:'rgba(0,212,255,.03)'}
      }]
    },
    options:{
      responsive:true, maintainAspectRatio:false,
      animation:{duration:150},
      plugins:{
        legend:{display:false},
        tooltip:{
          backgroundColor:'#0f1826', borderColor:'#1c2d42', borderWidth:1,
          titleColor:'#6a84a0', bodyColor:'#e2eaf6',
          titleFont:{family:'IBM Plex Mono',size:11},
          bodyFont:{family:'IBM Plex Mono',size:12},
          callbacks:{
            title: items => `נפח: ${items[0].raw.x.toFixed(2)} מ"ל`,
            label: item => `pH = ${item.raw.y.toFixed(2)}`
          }
        }
      },
      scales:{
        x:{type:'linear',
          title:{display:true,text:'נפח NaOH (מ"ל)',color:'#6a84a0',font:{family:'IBM Plex Mono',size:11}},
          grid:{color:'rgba(28,45,66,.7)'},
          ticks:{color:'#2e4460',font:{family:'IBM Plex Mono',size:10}},
          border:{color:'#1c2d42'}},
        y:{min:0,max:14,
          title:{display:true,text:'pH',color:'#6a84a0',font:{family:'IBM Plex Mono',size:11}},
          grid:{color:'rgba(28,45,66,.7)'},
          ticks:{color:'#2e4460',font:{family:'IBM Plex Mono',size:10}},
          border:{color:'#1c2d42'}}
      }
    }
  });
}

window.onload = () => {
  initChart();
  showQuiz(0);
  const initPH = calculatePH(0);
  document.getElementById('ph-display').innerText = initPH.toFixed(2);
  document.getElementById('ph-needle').style.left = `${(initPH/14)*100}%`;
};
</script>
</body>
</html>
