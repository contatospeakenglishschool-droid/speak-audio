# Speak! Bridge A2 - Unit 13 "Climate challenges" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 13", audio_json="audio_a2-unit-13.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["a2-unit-13"]
NAMES = {"Host": "Host", "Doctor": "Dr. Rivera"}
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["13.1 Podcast"].split("\n")]
S132 = [x.split(": ", 1)[1] for x in _r["13.2 Repeat words"].split("\n")]
S133 = [x.split(": ", 1)[1] for x in _r["13.3 Repeat sentences"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1: big photo + vocabulary (abstract)
    cover = cover_html(T, "LEVEL A2 · UNIT 13", "Climate challenges", "Climate change · <b>zero and first conditionals</b>",
                       [("YOU CAN", "explain causes and effects and talk about possible futures"),
                        ("LANGUAGE", "When ice melts, sea levels rise. · If we protect forests, the trees will help us."),
                        ("PRONUNCIATION", "CLImate · ATmosphere · diOXide · TEMperature (3 syllables)")])
    vw = [("the gases around the Earth", "atmosphere"), ("the gas we produce when we burn things (CO₂)", "carbon dioxide"),
          ("the usual weather in a place", "climate"), ("oil, gas and coal", "fossil fuels"), ("change from ice to water", "melt"),
          ("go up", "rise"), ("the height of the ocean", "sea level"), ("a very big piece of ice in the sea", "iceberg")]
    vl = [f'<li value="{i+1}">{d} {A(w, "min-width:20mm")}</li>' for i, (d, w) in enumerate(vw)]
    b.page(f"""{sec(1, "Warm-up: our planet", "8 min")}
<div style="display:flex;gap:4mm;align-items:flex-start">
<div style="width:52mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo('A')}" style="width:52mm;height:40mm;object-fit:cover;display:block"></div>
<div style="flex:1">{sub("A", "Match the words with their meanings.", "5 min")}
<div class="bank">atmosphere · carbon dioxide · climate · fossil fuels · iceberg · melt · rise · sea level</div></div></div>
{twocol(vl, 5)}
{sub("B", "Talk about it.", "3 min")}
<ol><li>What can you see in the photo? What's happening to it?</li><li>Has the weather in your city changed in the last few years? How?</li></ol>""",
    22, """<ol><li>A: <b>fuel</b> = /ˈfjuːəl/; <b>carbon dioxide</b> = CO₂ (dai-OX-ide). <i>Global warming</i> and <i>climate change</i> are used for the same idea in everyday English.</li>
<li>B: keep it short; the podcast explains the science.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Climate vocabulary</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Green City podcast: climate change for beginners</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Zero conditional (facts) vs first conditional (predictions)</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Zero and first conditionals · when / if · commas · unless</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>5 min</td><td>Word stress · conditional intonation</td><td>5</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Complete the conditionals · Word builder: green actions</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Finish the sentences · climate and Brazil</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework (50–75 words)</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>The <i>Green City</i> podcast (Unit 03; host voice Studio-O) is back. The guest is Dr. Mark Rivera (invented; one-off male voice Chirp 3 HD Charon), a climate scientist in New York. Facts: Earth's average surface temperature has risen about 2 °F (a little more than 1 °C) since the late 19th century (NASA); global sea level has risen about 8–9 inches (21–24 cm) since 1880 (NOAA, Climate.gov, "Climate Change: Global Sea Level"). Carbon dioxide traps heat in the atmosphere; trees take in carbon dioxide.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Portuguese uses a future form after <i>if / when</i>, so students say <i>If it will rain, I'll stay home</i> ✗ → <b>If it rains, I'll stay home</b>. They also forget the third-person -s in zero conditionals (<i>When ice melt</i> ✗ → <b>melts</b>) and use the present in the result of a prediction (<i>If we protect forests, the trees help us</i> ✗ → <b>will help</b>).</div>
<div class="box"><h4>AUDIO</h4>Track 13.1 The podcast (slow and natural) · Track 13.2 Word stress · Track 13.3 Conditional sentences</div>""")

    # Page 2
    tf = [("Climate change and global warming mean the same thing here.", "T: some people call it global warming."), ("Burning oil, gas and coal produces carbon dioxide.", "T"),
          ("The Earth is about 5 °C warmer than in the late 1800s.", "F: a little more than 1 °C (about 2 °F)."), ("The sea is about 8 or 9 inches higher than in 1880.", "T"),
          ("Forests can take in carbon dioxide.", "T: like the Amazon."), ("Dr. Rivera says small actions at home don't help.", "F: he says small things help.")]
    tfl = [f'<li value="{i+1}">{s} <b>T / F</b> {R(a)}</li>' for i, (s, a) in enumerate(tf)]
    cw = [(["produce", "will produce"], "produce", "When we burn them, they", "carbon dioxide."), (["go up", "will go up"], "go up", "When there's more carbon dioxide, temperatures", "."),
          (["get", "will get"], "get", "When the oceans get warmer, storms", "stronger."), (["rise", "will rise"], "rise", "When ice melts, sea levels", "."),
          (["keep", "will keep"], "will keep", "If we continue like this, temperatures", "rising."), (["take in", "will take in"], "will take in", "If we protect forests, the trees", "some carbon dioxide."),
          (["produce", "'ll produce"], "'ll produce", "If you ride a bike, you", "less carbon dioxide."), (["use", "will use"], "use", "When you turn off the lights, you", "less energy.")]
    cwl = [f'<li value="{i+1}">{a} {ch(o, r)} {c}</li>' for i, (o, r, a, c) in enumerate(cw)]
    b.page(f"""{sec(2, "Listening: climate change for beginners", "10 min")}
<p>The <i>Green City</i> podcast is back! Today the host talks to Dr. Mark Rivera, a climate scientist in New York.</p>
{audiocard(["13.1 · SLOW", "13.1 · NATURAL"])}
{sub("A", "Listen. True (T) or false (F)? Correct the false sentences.", "4 min", "13.1 · SLOW")}
{twocol(tfl, 4)}
{sub("B", "Listen again. Choose the form you hear.", "4 min", "13.1 · NATURAL")}
{twocol(cwl, 5)}
{sub("C", "Which two forms are you choosing between? Which sentences are facts and which are predictions?", "2 min")}
<p class="small">{R("present simple / will + verb · facts: 1–4, 8 · predictions: 5–7")}</p>""",
    22, """<p>A: numbers are written as words in the audio; write 2 °F / 1 °C and 8–9 inches on the board. B: guess first, then listen. C leads to page 3. Sources: NASA (temperature), NOAA (sea level).</p>""")

    # Page 3
    b.page(f"""{sec(3, "Language focus: facts and predictions", "10 min")}
{sub("A", "Read the sentences. Then answer the questions.", "4 min")}
<table style="table-layout:fixed;margin-top:0;font-size:9pt"><tr><th>group 1</th><th>group 2</th></tr>
<tr><td>When we burn fossil fuels, we produce carbon dioxide.<br>When ice melts, sea levels rise.</td><td>If we continue like this, temperatures will keep rising.<br>If you ride a bike, you'll produce less carbon dioxide.</td></tr></table>
<ol><li>Which group is about facts that are always true? {R("group 1 (zero conditional)")} Which is about a possible future? {R("group 2 (first conditional)")}</li>
<li>Zero conditional: <i>when / if</i> + {ch(["present simple", "will"], "present simple")}, {ch(["present simple", "will"], "present simple")}.</li>
<li>First conditional: <i>if</i> + {ch(["present simple", "will"], "present simple")}, {ch(["present simple", "will"], "will")} + verb.</li>
<li>When the <i>if / when</i> part comes first, we use a {ch(["comma", "period"], "comma")}.</li></ol>
{sub("B", "Zero (0) or first (1) conditional? Then rewrite one sentence with the result first.", "3 min")}
<ol><li>If you heat ice, it melts. {R("0")}</li><li>If it rains tomorrow, we'll stay home. {R("1")}</li><li>When people cut down forests, animals lose their homes. {R("0")}</li><li>If Kate opens a second bakery, she'll need more help. {R("1")}</li></ol>
<div class="wline">{R("We'll stay home if it rains tomorrow. (no comma)")}</div>
<div class="box sand"><h4>RULE</h4>Never use <b>will</b> in the <i>if</i> part: <i>If it <b>rains</b> tomorrow</i>, not <s>If it will rain</s>. More on the next page: <b>Grammar reference</b>.</div>""",
    24, """<ol><li>A: circle the subjects and underline the verbs in each clause with the student.</li>
<li>B: practice the intonation: the first clause goes up, the second comes down.</li></ol>""")

    grammar_ref.zero_first_conditional(b)

    # Page 4 (now 5)
    b.page(f"""{sub("C", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>If it will rain, I'll stay home.</td><td><b>If it rains, I'll stay home.</b></td><td>no will after if.</td></tr>
<tr><td>When ice melt, sea levels rises.</td><td><b>When ice melts, sea levels rise.</b></td><td>check the -s.</td></tr>
<tr><td>If we plant trees, the air is better next year.</td><td><b>… the air will be better next year.</b></td><td>prediction = will.</td></tr>
<tr><td>If I will have time, I call you.</td><td><b>If I have time, I'll call you.</b></td><td>if + present, will.</td></tr>
<tr><td>The temperature is rising up.</td><td><b>The temperature is rising.</b></td><td>rise = go up.</td></tr>
<tr><td>Will you come if it will be sunny?</td><td><b>Will you come if it's sunny?</b></td><td>no will after if.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "5 min")}
{audiocard(["13.2", "13.3"])}
{sub("A", "Word stress. Listen and repeat. Underline the stressed syllable.", "2 min", "13.2")}
<table style="table-layout:fixed;margin-top:0"><tr>{"".join(f"<td style='text-align:center'><b>{w}</b></td>" for w in S132)}</tr></table>
<p class="small">{R("CLImate · FOSsil · exTREME · inCREASE (verb) · diOXide · ATmosphere · TEMperature · enVIronment")}</p>
{sub("B", "Conditional sentences. Listen and repeat. The first part goes up ↗, the second part comes down ↘.", "2 min", "13.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S133)}</div>
<div class="box" style="margin-top:1mm"><h4>FEWER SYLLABLES</h4><b>temperature</b> = TEM-prə-chər (3 syllables, not 4) · <b>environment</b> = en-VI-rən-mənt · <b>you'll</b> = /juːl/, one syllable.</div>""",
    24, """<ol><li>4A: <i>increase</i> is in-CREASE as a verb and IN-crease as a noun (<i>an increase in temperature</i>).</li>
<li>4B: exaggerate the hump intonation first, then say it naturally.</li></ol>""")

    # Page 5 (now 6)
    gp = [("When we", "burn", "fossil fuels, CO₂ levels", "rise", "(burn / rise)"), ("If we", "plant", "more trees, CO₂ levels", "will go", "down. (plant / go)"),
          ("When ice caps", "melt", ", sea levels", "rise", ". (melt / rise)"), ("If temperatures", "continue", "to rise, there", "will be", "more storms. (continue / be)"),
          ("As the Earth", "gets", "hotter, storms", "get", "stronger. (get / get)"), ("If we", "don't stop", "burning coal, the problem", "will get", "worse. (not stop / get)")]
    gpl = [f'<li value="{i+1}">{a} {A(v1, "min-width:16mm")} {m} {A(v2, "min-width:14mm")} {c}</li>' for i, (a, v1, m, v2, c) in enumerate(gp)]
    ga = [("recycle", "plastic and glass"), ("save", "energy"), ("turn off", "the lights"), ("use", "public transportation"), ("plant", "trees"), ("reduce", "waste")]
    gal = [f'<li value="{i+1}">{A(v, "min-width:16mm")} {n}</li>' for i, (v, n) in enumerate(ga)]
    b.page(f"""{sec(5, "Practice", "8 min")}
{sub("A", "Complete with the correct form of the verbs. Then write 0 (zero) or 1 (first) for each sentence.", "5 min")}
<ol>{"".join(x.replace('<li value=', '<li data-v=') for x in gpl)}</ol>
<p class="small">{R("Zero: 1, 3, 5 · First: 2, 4, 6")}</p>
{sub("B", "Word builder: green actions. Complete with the verbs.", "3 min")}
<div class="bank">plant · recycle · reduce · save · turn off · use</div>
{twocol(gal, 4)}
<p class="small">Make two first conditionals: <i>If I recycle more, I'll…</i></p>""",
    22, """<ol><li>A: 5 uses <i>as</i> (= while it changes): zero conditional. Accept <i>increase</i> for <i>rise</i>.</li>
<li>B: from the bonus lesson <i>Weather and climate</i> (Vocabulary to Go). American English: <b>public transportation</b> (British: transport).</li></ol>""")

    # Page 6 (now 7)
    st = ["When I'm stressed, I…", "If I have time this weekend, I'll…", "When it rains a lot in my city,…", "If I learn English very well,…", "If everybody rides a bike to work,…", "If Brazil protects the Amazon,…"]
    stl = "".join(f"<li>{s}<div class='wline'></div></li>" for s in st)
    b.page(f"""{sec(6, "Speaking", "12 min")}
{sub("A", "Finish the sentences so they are true or logical. Read them to your teacher. Your teacher writes them in the right column: zero or first conditional.", "7 min")}
<ol>{stl}</ol>
<table style="table-layout:fixed;margin-top:1mm;font-size:9pt"><tr><th>zero conditional (facts, habits)</th><th>first conditional (predictions)</th></tr><tr><td style="height:14mm"></td><td></td></tr></table>
{sub("B", "Climate and you.", "5 min")}
<ol><li>Have you seen extreme weather in Brazil? What happened?</li><li>What green actions do you do at home? What will you start doing?</li></ol>""",
    26, """<ol><li>A: write the student's sentences in the table and correct <i>will</i> after <i>if</i>. Then change roles: you read, the student writes.</li>
<li>B: be sensitive: some students may have been affected by floods or droughts.</li></ol>""")

    # Page 7 (now 8)
    pc = [("A2 Unit 08", "I can ask about life experiences and give details with the past simple."), ("A2 Unit 09", "I can say how long things have been true with for and since."),
          ("A2 Unit 11", "I can check what's done and not done with already, yet and still."), ("A2 Unit 12", "I can write a friendly email with the right phrases."),
          ("A2 Unit 13", "I can explain causes and effects with zero and first conditionals.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    mt = [("When people cut down forests,", "e"), ("As CO₂ levels increase,", "d"), ("If temperatures keep rising,", "b"), ("If we find new types of energy,", "a"), ("Storms get stronger", "c")]
    ends = ["a. we'll protect the planet.", "b. it will be difficult to grow food.", "c. when the oceans get warmer.", "d. temperatures rise.", "e. animals lose their homes."]
    mtl = "".join(f"<tr><td>{i+1}. {a} {R(k)}</td><td>{ends[i]}</td></tr>" for i, (a, k) in enumerate(mt))
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Match the beginnings and the endings.</b></p>
<table style="table-layout:fixed;margin-top:0;font-size:9pt">{mtl}</table>
<p style="margin-top:2mm"><b>2. My green promises (50–75 words).</b> Write about three things you will do for the planet and their results. Use first conditionals: <i>If I take the bus to work, I'll…</i> Add one zero conditional fact.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class: the student reads the promises; ask <i>What will happen if…?</i> Check: no <i>will</i> after <i>if</i>, commas, third-person -s.</p>""")

    b.extra("Audio scripts", f"""
{sub("13.1", "Green City: climate change for beginners (slow and natural)")}
<p style="line-height:1.42">{"<br>".join(f"<b>{NAMES[n]}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("13.2", "Word stress")}
<p>{" · ".join(S132)}</p>
{sub("13.3", "Conditional sentences")}
<p>{" ".join(S133)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 13 - Climate challenges")
