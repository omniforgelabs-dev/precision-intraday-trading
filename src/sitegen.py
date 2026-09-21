"""
sitegen.py — static site generator for Precision Intraday Trading.
Rebuilt from surviving output HTML after the original build/ directory
was lost to the workspace snapshot's directory-name exclusion list
(never name this source tree "build" again — use "src").

Exports content helpers used by content_mN.py modules, plus page()/CSS/JS
used by make.py.
"""
import base64
import os

# ---------------------------------------------------------------------------
# module registry (filled in by make.py via set_toc before any page() call)
# ---------------------------------------------------------------------------
_TOC = []  # list of dicts: {slug, num, title}


def set_toc(modules):
    global _TOC
    _TOC = modules


# ---------------------------------------------------------------------------
# small content helpers
# ---------------------------------------------------------------------------
def b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")


def h2(num, title):
    return f'<h2><span class="num">{num}</span>{title}</h2>\n'


def h3(title):
    return f'<h3>{title}</h3>\n'


def p(html):
    return f'<p>{html}</p>\n'


def chart(img_path, caption):
    data = b64(img_path)
    return (
        f'<figure class="chart"><img src="data:image/png;base64,{data}" '
        f'alt="" loading="lazy"><figcaption>{caption}</figcaption></figure>\n'
    )


def look(title, items, ordered=True):
    tag = "ol" if ordered else "ul"
    lis = "".join(f"<li>{it}</li>" for it in items)
    return f'<div class="look"><h4>{title}</h4><{tag}>{lis}</{tag}></div>\n'


def key(label, body_html):
    return f'<div class="key"><div class="lbl">{label}</div><p>{body_html}</p></div>\n'


def warn(label, paragraphs):
    if isinstance(paragraphs, str):
        paragraphs = [paragraphs]
    ps = "".join(f"<p>{x}</p>" for x in paragraphs)
    return f'<div class="warn"><div class="lbl">{label}</div>{ps}</div>\n'


def dev(label, paragraphs):
    if isinstance(paragraphs, str):
        paragraphs = [paragraphs]
    ps = "".join(f"<p>{x}</p>" for x in paragraphs)
    return f'<div class="dev"><div class="lbl">{label}</div>{ps}</div>\n'


def defn(term, body_html):
    return (
        f'<div class="defn"><span class="term">{term}</span>'
        f'<span class="body">{body_html}</span></div>\n'
    )


def table(headers, rows, cls=""):
    clsattr = f' class="{cls}"' if cls else ""
    thead = "".join(f"<th>{hh}</th>" for hh in headers)
    trs = ""
    for row in rows:
        tds = "".join(f"<td>{c}</td>" for c in row)
        trs += f"<tr>{tds}</tr>"
    return (
        f'<table{clsattr}><thead><tr>{thead}</tr></thead>'
        f'<tbody>{trs}</tbody></table>\n'
    )


def flow(text):
    return f'<pre class="flow">{text}</pre>\n'


def prac(number, title, meta, body_html):
    return (
        f'<div class="prac"><div class="lbl">Practical {number}</div>'
        f'<h4>{title}</h4><div class="meta">{meta}</div>{body_html}</div>\n'
    )


def pre(text):
    return f'<pre>{text}</pre>\n'


def summary(items):
    lis = "".join(f"<li>{it}</li>" for it in items)
    return f'<div class="summary"><ol>{lis}</ol></div>\n'


def split(halves):
    """halves: list of (kind, heading, body_html) where kind in good/bad/neutral"""
    cards = ""
    for kind, heading, body_html in halves:
        cards += f'<div class="half {kind}"><h5>{heading}</h5><p>{body_html}</p></div>'
    return f'<div class="split">{cards}</div>\n'


_quiz_counter = {"n": 0}


def quiz(question, options, hint=None):
    """
    options: list of dicts {label, correct(bool), feedback(html)}
    Renders the click-to-reveal quiz block with per-option unique feedback.
    """
    _quiz_counter["n"] += 1
    qid = f"q{_quiz_counter['n']}"
    letters = "ABCDEFGH"
    opts_html = ""
    for i, opt in enumerate(options):
        r = "correct" if opt.get("correct") else "wrong"
        fbclass = "correct" if opt.get("correct") else "wrong"
        opts_html += (
            f'<button class="opt" data-q="{qid}" data-i="{i}" data-r="{r}">'
            f'<span class="ltr">{letters[i]}</span>'
            f'<span class="txt">{opt["label"]}</span>'
            f'<span class="mark"></span></button>'
        )
        opts_html += (
            f'<div class="fb {fbclass}" id="{qid}-fb{i}">'
            f'<div class="fb-head"></div>{opt["feedback"]}</div>'
        )
    note = f'<p class="qnote">{hint}</p>' if hint else ""
    return (
        f'<div class="quiz" id="{qid}"><div class="lbl">Check your understanding</div>'
        f'<div class="q">{question}</div>'
        f'<div class="opts">{opts_html}</div>{note}</div>\n'
    )


# ---------------------------------------------------------------------------
# CSS / JS — recovered verbatim from the surviving module-03.html output
# ---------------------------------------------------------------------------
CSS = """
:root{
--bg:#0b0f1a;--panel:#131a29;--panel2:#0e1626;--line:#1f2a3d;--line2:#24324d;
--txt:#e8edf7;--txt2:#c3cfe3;--muted:#8c9bb5;
--up:#26a69a;--dn:#ef5350;--acc:#ffb300;--blue:#4fa3ff;--purp:#b07cff;
--pink:#ff7ab8;--cyan:#4fd1e0;--green:#34d399;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--txt);
font:16px/1.72 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
padding-bottom:0;-webkit-font-smoothing:antialiased}
.wrap{max-width:1000px;margin:0 auto;padding:0 26px}

/* top bar */
.topbar{position:sticky;top:0;z-index:60;background:rgba(11,15,26,.93);
backdrop-filter:blur(12px);border-bottom:1px solid var(--line);
display:flex;align-items:center;justify-content:space-between;
padding:11px 26px;gap:14px}
.home{display:flex;align-items:center;gap:10px;text-decoration:none;min-width:0}
.logo{color:var(--blue);font-size:19px}
.name{color:var(--txt);font-weight:700;font-size:15px;letter-spacing:-.2px;
white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.topright{display:flex;align-items:center;gap:14px;flex-shrink:0}
.modlabel{color:var(--muted);font-size:12.5px;font-weight:600;
letter-spacing:.6px;white-space:nowrap}
.menubtn{background:#18233a;border:1px solid var(--line2);color:var(--txt);
width:36px;height:34px;border-radius:8px;font-size:16px;cursor:pointer;
line-height:1}
.menubtn:hover{background:#1f2c48}

/* drawer */
.drawer{position:fixed;top:0;right:-380px;width:360px;max-width:88vw;height:100%;
background:#0d1424;border-left:1px solid var(--line2);z-index:80;
transition:right .26s ease;overflow-y:auto;padding:26px 0}
.drawer.open{right:0}
.drawer-inner{padding:0 24px}
.drawer h4{color:var(--muted);font-size:11.5px;letter-spacing:2px;
text-transform:uppercase;margin-bottom:16px;font-weight:750}
.toc-mod{margin-bottom:6px}
.toc-mod>a{display:flex;gap:11px;align-items:baseline;padding:9px 12px;
border-radius:8px;text-decoration:none;color:var(--txt2);font-size:14.4px;
transition:background .15s}
.toc-mod>a:hover{background:#18233a;color:#fff}
.toc-mod>a.active{background:#1b2a47;color:#fff}
.toc-mod .n{color:var(--blue);font-weight:750;font-size:12px;min-width:20px}
.toc-mod a .done-dot{margin-left:auto;color:var(--green);font-size:12px;
opacity:0;transition:opacity .2s}
.toc-mod a.done .done-dot{opacity:1}
.scrim{position:fixed;inset:0;background:rgba(0,0,0,.6);z-index:70;
opacity:0;pointer-events:none;transition:opacity .26s}
.scrim.open{opacity:1;pointer-events:auto}

/* page header */
.pagehead{background:linear-gradient(135deg,#131c30,#0d1424);
border-bottom:1px solid #22304a;padding:46px 0 36px;margin-bottom:42px}
.kicker{color:var(--blue);font-size:12.5px;font-weight:700;letter-spacing:2.4px;
text-transform:uppercase;margin-bottom:13px}
.pagehead h1{font-size:34px;line-height:1.2;font-weight:800;letter-spacing:-.5px}
.sub{color:var(--muted);font-size:15.4px;margin-top:15px;max-width:700px}
.recap{background:#101a2c;border:1px solid var(--line2);border-radius:10px;
padding:16px 20px;margin-top:24px;font-size:14.4px;color:#9fb2d0;max-width:760px}
.recap b{color:var(--green)}

/* typography */
h2{font-size:26px;font-weight:750;margin:58px 0 10px;letter-spacing:-.3px;
padding-top:24px;border-top:1px solid var(--line);scroll-margin-top:70px}
main>h2:first-child{border-top:none;padding-top:0;margin-top:0}
h2 .num{color:var(--blue);font-size:13.5px;display:block;font-weight:700;
letter-spacing:2px;margin-bottom:8px;text-transform:uppercase}
h3{font-size:19px;font-weight:700;margin:36px 0 11px;color:#d7e2f5}
h4{font-weight:700}
p{margin:15px 0;color:var(--txt2)}
strong,b{color:#fff;font-weight:650}
em{color:#ffd580;font-style:normal;font-weight:600}
a{color:var(--blue)}
ul,ol{margin:15px 0 15px 24px}
li{margin:9px 0;color:var(--txt2)}
code{background:#0a1418;border:1px solid #1d4653;border-radius:4px;
padding:1px 7px;font-size:13.6px;color:#7fe3f0;
font-family:ui-monospace,SFMono-Regular,Menlo,monospace}

/* charts */
.chart{margin:36px 0;background:var(--panel2);border:1px solid var(--line2);
border-radius:13px;overflow:hidden}
.chart img{width:100%;display:block}
.chart figcaption{padding:15px 20px;font-size:13.6px;color:#93a4c0;
border-top:1px solid #1e2a42;background:#0c1322;line-height:1.62}
.chart figcaption b{color:#cfe0ff}

/* blocks */
.look{background:#111c30;border-left:4px solid var(--blue);padding:21px 25px;
margin:28px 0;border-radius:0 10px 10px 0}
.look h4{color:var(--blue);font-size:13px;letter-spacing:1.6px;font-weight:750;
text-transform:uppercase;margin-bottom:13px}
.look ol,.look ul{margin:0 0 0 21px}
.look li{margin:12px 0}
.key{background:linear-gradient(135deg,#132a24,#0f2119);border:1px solid #1f6b52;
border-radius:11px;padding:23px 27px;margin:32px 0}
.key .lbl{color:var(--green);font-size:11.5px;letter-spacing:2px;font-weight:750;
text-transform:uppercase;margin-bottom:10px}
.key p{color:#d8f5e9;font-size:17.5px;margin:0;font-weight:600;line-height:1.56}
.warn{background:#2a1618;border:1px solid #6b2430;border-radius:11px;
padding:21px 26px;margin:30px 0}
.warn .lbl{color:#ff8a8a;font-size:11.5px;letter-spacing:2px;font-weight:750;
text-transform:uppercase;margin-bottom:10px}
.warn p{color:#f6d5d5;margin:9px 0}
.warn p:first-of-type{margin-top:0}
.warn ol,.warn ul{margin:10px 0 0 22px}
.warn li{color:#f6d5d5;margin:7px 0}
.dev{background:#0d1a1f;border:1px solid #1f5a6b;border-radius:11px;
padding:21px 26px;margin:30px 0}
.dev .lbl{color:var(--cyan);font-size:11.5px;letter-spacing:2px;font-weight:750;
text-transform:uppercase;margin-bottom:10px}
.dev p{color:#c9e8ef;margin:9px 0}
.dev p:first-of-type{margin-top:0}
.defn{background:#101a2c;border:1px solid var(--line2);border-radius:9px;
padding:14px 18px;margin:12px 0}
.defn .term{display:block;color:var(--acc);font-weight:750;font-size:14px;
letter-spacing:.4px;text-transform:uppercase;margin-bottom:5px}
.defn .body{color:var(--txt2);font-size:15px}

/* tables */
table{width:100%;border-collapse:collapse;margin:28px 0;font-size:14.6px;
display:block;overflow-x:auto;white-space:normal}
thead th{background:#182338;color:#a9bcd8;text-align:left;padding:12px 15px;
font-size:12.4px;letter-spacing:.9px;text-transform:uppercase;font-weight:700;
border-bottom:2px solid var(--line2);white-space:nowrap}
td{padding:12px 15px;border-bottom:1px solid var(--line);color:var(--txt2);
vertical-align:top;min-width:120px}
tbody tr:last-child td{border-bottom:none}
td.no{color:#ff8a8a;font-weight:650}
td.yes{color:var(--green);font-weight:650}
td.mid{color:var(--acc);font-weight:650}

pre.flow{background:var(--panel2);border:1px solid var(--line2);
border-radius:11px;padding:22px 24px;margin:28px 0;
font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:13px;
color:#9fb2d0;overflow-x:auto;line-height:1.72}
pre{font-family:ui-monospace,SFMono-Regular,Menlo,monospace}

/* split cards */
.split{display:flex;gap:16px;flex-wrap:wrap;margin:28px 0}
.half{flex:1;min-width:265px;border-radius:11px;padding:20px 23px}
.half.bad{background:#2a1618;border:1px solid #6b2430}
.half.good{background:#0f2119;border:1px solid #1f6b52}
.half.neutral{background:#101a2c;border:1px solid var(--line2)}
.half h5{font-size:12.8px;letter-spacing:1.5px;text-transform:uppercase;
font-weight:750;margin-bottom:11px}
.half.bad h5{color:#ff8a8a}
.half.good h5{color:var(--green)}
.half.neutral h5{color:var(--blue)}
.half p{margin:0;font-size:14.6px}
.half.bad p{color:#f6d5d5}
.half.good p{color:#d8f5e9}
.half.neutral p{color:var(--txt2)}

/* practical */
.prac{background:#1a1430;border:1px solid #4a3a7c;border-radius:12px;
padding:25px 29px;margin:32px 0}
.prac .lbl{color:var(--purp);font-size:11.5px;letter-spacing:2px;font-weight:750;
text-transform:uppercase;margin-bottom:7px}
.prac h4{color:#fff;font-size:20px;font-weight:700;margin-bottom:6px}
.prac .meta{color:#9b8cc4;font-size:13.2px;margin-bottom:15px}
.prac p,.prac li{color:#d5cbf0}
.prac pre{background:#0d0a18;border:1px solid #3a2f63;border-radius:8px;
padding:16px 18px;margin:15px 0;font-size:12.7px;color:#b9a9e8;overflow-x:auto;
line-height:1.74;white-space:pre}

/* quiz */
.quiz{background:#16203a;border:2px solid #3b5a8c;border-radius:14px;
padding:29px 31px;margin:46px 0}
.quiz .lbl{color:var(--acc);font-size:12px;letter-spacing:2.2px;font-weight:750;
text-transform:uppercase;margin-bottom:14px}
.quiz .q{font-size:19.5px;font-weight:650;color:#fff;margin-bottom:22px;
line-height:1.5}
.opts{display:flex;flex-direction:column;gap:0}
.opt{background:#0f1930;border:1px solid #2a3b5c;border-radius:10px;
padding:15px 18px;margin:0 0 11px;display:flex;gap:14px;align-items:flex-start;
width:100%;text-align:left;cursor:pointer;font:inherit;color:inherit;
transition:border-color .16s,background .16s;position:relative}
.opt:hover{background:#142139;border-color:#42618f}
.opt .ltr{background:#2a3b5c;color:#cfe0ff;width:28px;height:28px;flex:0 0 28px;
border-radius:7px;display:flex;align-items:center;justify-content:center;
font-weight:750;font-size:14px;transition:background .16s,color .16s}
.opt .txt{color:#c9d6ea;font-size:15.2px;line-height:1.56;flex:1}
.opt .mark{flex:0 0 auto;font-weight:800;font-size:15px;opacity:0;
transition:opacity .2s;align-self:center}
.opt.picked{cursor:default}
.opt.picked.correct{border-color:var(--green);background:#11261e}
.opt.picked.correct .ltr{background:var(--green);color:#08130f}
.opt.picked.correct .mark{opacity:1;color:var(--green)}
.opt.picked.correct .mark::after{content:"✓"}
.opt.picked.wrong{border-color:var(--dn);background:#251518}
.opt.picked.wrong .ltr{background:var(--dn);color:#1a0808}
.opt.picked.wrong .mark{opacity:1;color:var(--dn)}
.opt.picked.wrong .mark::after{content:"✕"}
.quiz.answered .opt:not(.picked){opacity:.5}
.quiz.answered .opt:not(.picked).correct{opacity:1;border-color:#1f6b52;
background:#0f1f1a}
.quiz.answered .opt:not(.picked).correct .ltr{background:#1f6b52;color:#d8f5e9}
.quiz.answered .opt:not(.picked).correct .mark{opacity:.85;color:var(--green)}
.quiz.answered .opt:not(.picked).correct .mark::after{content:"✓"}
.fb{display:none;border-radius:10px;padding:19px 22px;margin:-3px 0 15px;
font-size:15px;line-height:1.68;animation:fbin .28s ease}
@keyframes fbin{from{opacity:0;transform:translateY(-5px)}to{opacity:1;transform:none}}
.fb.show{display:block}
.fb.correct{background:#0f2119;border:1px solid #1f6b52;color:#d8f5e9}
.fb.wrong{background:#231518;border:1px solid #5e2530;color:#f0d8dc}
.fb p{margin:10px 0}
.fb p:first-of-type{margin-top:0}
.fb p:last-child{margin-bottom:0}
.fb strong{color:#fff}
.fb em{color:#ffd580}
.fb .fb-head{font-size:11.5px;letter-spacing:2px;text-transform:uppercase;
font-weight:750;margin-bottom:11px}
.fb.correct .fb-head{color:var(--green)}
.fb.correct .fb-head::after{content:"✓  Correct"}
.fb.wrong .fb-head{color:#ff8a8a}
.fb.wrong .fb-head::after{content:"✕  Not quite — here is why"}
.qnote{color:#93a4c0;font-size:14.4px;margin-top:18px}

.summary{background:var(--panel2);border:1px solid var(--line2);
border-radius:12px;padding:27px 31px;margin:36px 0}
.summary ol{margin-left:21px}
.summary li{margin:11px 0}
.summary li b{color:#fff}

/* nav */
.pagenav{display:flex;gap:16px;margin:60px 0 20px;justify-content:space-between}
.navbtn{flex:1;max-width:48%;background:var(--panel2);
border:1px solid var(--line2);border-radius:12px;padding:18px 22px;
text-decoration:none;display:block;transition:border-color .16s,background .16s}
.navbtn:hover{border-color:#42618f;background:#141e33}
.navbtn .dir{display:block;color:var(--blue);font-size:12.4px;font-weight:700;
letter-spacing:1.2px;text-transform:uppercase;margin-bottom:6px}
.navbtn .ttl{display:block;color:var(--txt);font-size:15.4px;font-weight:600;
line-height:1.42}
.navbtn.next{text-align:right}

/* index page */
.hero{padding:70px 0 20px}
.hero h1{font-size:46px;line-height:1.1;letter-spacing:-1.2px;font-weight:850;
margin-bottom:20px}
.hero .lede{font-size:18.5px;color:var(--muted);max-width:720px;line-height:1.65}
.pills{display:flex;flex-wrap:wrap;gap:9px;margin:26px 0 0}
.pill{background:#1b2740;border:1px solid #2c3d5c;color:#9fb2d0;font-size:12.6px;
padding:6px 14px;border-radius:99px;font-weight:600}
.pill.no{background:#241619;border-color:#5e2530;color:#ffa9a9}
.modgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(310px,1fr));
gap:16px;margin:34px 0}
.modcard{background:var(--panel2);border:1px solid var(--line2);
border-radius:13px;padding:22px 24px;text-decoration:none;display:block;
transition:border-color .16s,transform .16s,background .16s;position:relative}
.modcard:hover{border-color:#42618f;background:#141e33;transform:translateY(-2px)}
.modcard .mnum{color:var(--blue);font-size:12px;font-weight:750;
letter-spacing:2px;text-transform:uppercase;margin-bottom:9px;display:block}
.modcard h3{color:#fff;font-size:18.5px;margin:0 0 9px;line-height:1.32}
.modcard p{color:var(--muted);font-size:14.2px;margin:0;line-height:1.6}
.modcard .tick{position:absolute;top:18px;right:20px;color:var(--green);
font-size:15px;opacity:0;transition:opacity .2s}
.modcard.done .tick{opacity:1}
.modcard.done{border-color:#1f6b52}
.startbtn{display:inline-block;background:var(--blue);color:#06101f;
font-weight:750;font-size:16px;padding:15px 34px;border-radius:11px;
text-decoration:none;margin-top:10px;transition:transform .14s,box-shadow .14s}
.startbtn:hover{transform:translateY(-2px);box-shadow:0 8px 26px rgba(79,163,255,.28)}
.resetbtn{background:none;border:1px solid var(--line2);color:var(--muted);
font-size:13px;padding:8px 16px;border-radius:8px;cursor:pointer;
margin-left:14px;font-family:inherit}
.resetbtn:hover{border-color:#42618f;color:var(--txt)}
.notice{background:#1a1430;border:1px solid #4a3a7c;border-radius:12px;
padding:22px 26px;margin:34px 0}
.notice h4{color:var(--purp);font-size:12px;letter-spacing:2px;
text-transform:uppercase;margin-bottom:10px}
.notice p{color:#d5cbf0;margin:9px 0}
.notice p:first-of-type{margin-top:0}

/* footer */
.sitefoot{margin-top:70px;border-top:1px solid var(--line);
background:#0a0e18;padding:34px 0 40px}
.sitefoot p{color:#6e7f99;font-size:13.2px;line-height:1.7;max-width:820px}
.sitefoot strong{color:#93a4c0}
.foot2{margin-top:14px;font-size:12.4px;color:#4f5d74}

@media(max-width:700px){
.wrap{padding:0 18px}
.pagehead h1{font-size:27px}
.hero h1{font-size:33px}
.hero .lede{font-size:16.5px}
h2{font-size:22px}
.quiz{padding:22px 19px}
.quiz .q{font-size:17.5px}
.opt{padding:13px 14px;gap:11px}
.opt .txt{font-size:14.4px}
.pagenav{flex-direction:column}
.navbtn{max-width:100%}
.navbtn.next{text-align:left}
.modlabel{display:none}
.prac{padding:20px 18px}
.look{padding:18px 19px}
}
@media print{
.topbar,.drawer,.scrim,.pagenav{display:none}
body{background:#fff;color:#000}
.fb{display:block!important}
}
"""

JS = """
(function(){
  // drawer
  var mb=document.getElementById('menubtn'),dr=document.getElementById('drawer'),
      sc=document.getElementById('scrim');
  function close(){dr.classList.remove('open');sc.classList.remove('open');}
  if(mb){mb.addEventListener('click',function(){
    dr.classList.toggle('open');sc.classList.toggle('open');});}
  if(sc){sc.addEventListener('click',close);}
  document.addEventListener('keydown',function(e){if(e.key==='Escape')close();});

  // quiz interaction — unique feedback per option
  document.querySelectorAll('.opt').forEach(function(btn){
    btn.addEventListener('click',function(){
      var quiz=btn.closest('.quiz');
      if(quiz.classList.contains('answered'))return;
      var i=btn.dataset.i,qid=btn.dataset.q;
      quiz.classList.add('answered');
      btn.classList.add('picked');
      var fb=document.getElementById(qid+'-fb'+i);
      if(fb)fb.classList.add('show');
      // if they were wrong, also reveal the correct option's explanation
      if(btn.dataset.r==='wrong'){
        var right=quiz.querySelector('.opt[data-r="correct"]');
        if(right){
          var ri=right.dataset.i;
          var rfb=document.getElementById(qid+'-fb'+ri);
          if(rfb)setTimeout(function(){rfb.classList.add('show');},260);
        }
      }
      setTimeout(function(){
        var r=fb.getBoundingClientRect();
        if(r.bottom>window.innerHeight){
          fb.scrollIntoView({behavior:'smooth',block:'nearest'});}
      },80);
    });
  });

  // progress tracking
  var KEY='pit_progress_v1';
  function read(){try{return JSON.parse(localStorage.getItem(KEY)||'{}');}
    catch(e){return {};}}
  function write(o){try{localStorage.setItem(KEY,JSON.stringify(o));}catch(e){}}
  var pg=document.body.dataset.page;
  if(pg&&pg!=='index'){
    var seen=false;
    window.addEventListener('scroll',function(){
      if(seen)return;
      var d=document.documentElement;
      var pct=(window.scrollY+window.innerHeight)/d.scrollHeight;
      if(pct>0.82){seen=true;var o=read();o[pg]=1;write(o);}
    },{passive:true});
  }
  var prog=read();
  document.querySelectorAll('[data-modkey]').forEach(function(el){
    if(prog[el.dataset.modkey]){el.classList.add('done');}
  });
  document.querySelectorAll('.toc-mod > a').forEach(function(a){
    var k=a.dataset.key;
    if(k&&prog[k])a.classList.add('done');
    if(k===pg)a.classList.add('active');
  });
  var rb=document.getElementById('resetprog');
  if(rb){rb.addEventListener('click',function(){
    localStorage.removeItem(KEY);location.reload();});}
})();
"""

FOOTER = """<footer class="sitefoot"><div class="wrap">
  <p><strong>Educational material only.</strong> Nothing here is financial
  advice, a solicitation, or a promise of results. Trading involves substantial
  risk of loss. All charts are illustrative and synthetic; they depict decision
  logic, not historical performance. Test any method in simulation before
  risking capital.</p>
  <p class="foot2">Precision Intraday Trading &middot; Price Action &amp; Structure
  System &middot; 11 modules</p>
</div></footer>"""


def _drawer_html():
    items = ""
    for m in _TOC:
        items += (
            f'<div class="toc-mod"><a href="{m["slug"]}.html" data-key="{m["slug"]}">'
            f'<span class="n">{m["num"]}</span><span>{m["short"]}</span>'
            f'<span class="done-dot">\u2713</span></a></div>'
        )
    return (
        '<div class="drawer" id="drawer"><div class="drawer-inner">\n'
        '  <h4>Course contents</h4>\n'
        f'  {items}\n'
        '</div></div>\n'
        '<div class="scrim" id="scrim"></div>\n'
    )


def _topbar_html(modlabel):
    return (
        '<div class="topbar">\n'
        '  <a class="home" href="index.html">\n'
        '    <span class="logo">\u25c8</span>\n'
        '    <span class="name">Precision Intraday Trading</span>\n'
        '  </a>\n'
        '  <div class="topright">\n'
        f'    <span class="modlabel">{modlabel}</span>\n'
        '    <button class="menubtn" id="menubtn" aria-label="Contents">\u2630</button>\n'
        '  </div>\n'
        '</div>\n'
    )


def page(slug, title, kicker, h1, sub, body_html, prev=None, nxt=None,
         is_index=False, modlabel=None):
    """
    Build a full HTML page.
    prev / nxt: optional dict {slug, title} for pagenav.
    is_index: True for the homepage (different body wrapper, no pagehead).
    """
    head_html = (
        "<!DOCTYPE html>\n<html lang=\"en\"><head>\n"
        "<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">\n"
        f"<title>{title}</title>\n"
        '<meta name="description" content="Precision Intraday Trading — price '
        'action, market structure, liquidity and structural risk management. '
        'A complete 11-module course.">\n'
        f"<style>{CSS}</style>\n</head>\n"
    )

    if modlabel is None:
        modlabel = "11-module course" if is_index else kicker

    out = [head_html]
    out.append(f'<body data-page="{slug}">\n\n')
    out.append(_topbar_html(modlabel))
    out.append(_drawer_html())
    out.append("\n")

    if is_index:
        out.append(f'\n<main class="wrap">\n{body_html}\n</main>\n\n')
    else:
        out.append(
            f'<header class="pagehead"><div class="wrap"><div class="kicker">'
            f'{kicker}</div><h1>{h1}</h1><p class="sub">{sub}</p></div></header>\n\n'
        )
        out.append(f'<main class="wrap">\n{body_html}\n')
        nav_prev = (
            f'<a class="navbtn prev" href="{prev["slug"]}.html">'
            f'<span class="dir">\u2190 Previous</span>'
            f'<span class="ttl">{prev["title"]}</span></a>'
            if prev else '<span></span>'
        )
        nav_next = (
            f'<a class="navbtn next" href="{nxt["slug"]}.html">'
            f'<span class="dir">Next \u2192</span>'
            f'<span class="ttl">{nxt["title"]}</span></a>'
            if nxt else '<span></span>'
        )
        out.append(f'<nav class="pagenav">{nav_prev}{nav_next}</nav>\n</main>\n\n')

    out.append(FOOTER + "\n\n")
    out.append(f"<script>{JS}</script>\n")
    out.append("</body></html>\n")
    return "".join(out)
