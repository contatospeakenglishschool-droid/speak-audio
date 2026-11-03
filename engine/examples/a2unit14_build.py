# Speak! Bridge A2 - Unit 14 "A green future" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 14", audio_json="audio_a2-unit-14.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["a2-unit-14"]
NAMES = {"Host": "Host", "Doctor": "Dr. Rivera"}
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["14.1 Podcast"].split("\n")]
S142 = [x.split(": ", 1)[1] for x in _r["14.2 Repeat words"].split("\n")]
S143 = [x.split(": ", 1)[1] for x in _r["14.3 Repeat sentences"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1: big photo + vocabulary
    cover = cover_html(T, "LEVEL A2 · UNIT 14", "A green future", "Clean energy · <b>conjunctions: and, but, so, because, although</b>",
                       [("YOU CAN", "compare types of energy and join ideas in longer sentences"),
                        ("LANGUAGE", "Wind turbines are cheap, although they can be noisy. · Solar panels are cheaper now, so many people install them."),
                        ("PRONUNCIATION", "reNEWable · reLIable · elecTRIcity · alTHOUGH")])
    vw = [("they turn sunlight into electricity", "solar panels"), ("tall machines that use the wind", "wind turbines"),
          ("electricity from moving water", "hydropower"), ("it uses heat from the ground", "geothermal heat pump"),
          ("it never runs out", "renewable"), ("you can trust it; it works well", "reliable"),
          ("stop working", "break down"), ("put a system in a house", "install")]
    vl = [f'<li value="{i+1}">{d} {A(w, "min-width:24mm")}</li>' for i, (d, w) in enumerate(vw)]
    b.page(f"""{sec(1, "Warm-up: energy for the future", "8 min")}
<div style="display:flex;gap:4mm;align-items:flex-start">
<div style="width:52mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo('A')}" style="width:52mm;height:36mm;object-fit:cover;display:block"></div>
<div style="flex:1">{sub("A", "Match the words with their meanings.", "5 min")}
<div class="bank">break down · geothermal heat pump · hydropower · install · reliable · renewable · solar panels · wind turbines</div></div></div>
{twocol(vl, 4)}
{sub("B", "Talk about it.", "3 min")}
<ol><li>Which two things in exercise A can you see in the photo?</li><li>Do you know anyone with solar panels at home? Where does the electricity in your city come from?</li></ol>""",
    22, """<ol><li>A: <b>renewable</b> = re-NEW-a-ble; <b>reliable</b> = re-LI-a-ble. <i>Geothermal heat pump</i> is the common American term (the British course says <i>ground source heating</i>).</li>
<li>B: keep it short; many students will know that Brazil uses a lot of hydropower. The podcast confirms it.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Clean energy vocabulary</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Green City podcast: clean energy for beginners</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Conjunctions: adding, contrast, cause and effect · commas</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>and · but · although · while · because · so · if · commas</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>5 min</td><td>Word stress · pausing at the comma</td><td>5</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Find the mistakes · Word builder: energy opposites</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Energy in Brazil: pros and cons with conjunctions</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework (50–75 words)</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Last episode ended with "In our next episode, we'll talk about clean energy." Dr. Mark Rivera (Unit 13, voice Chirp 3 HD Charon) is back on <i>Green City</i> (host voice Studio-O). Facts: since 2010, the cost of residential solar systems in the U.S. has fallen 64% (NREL, "Documenting a Decade of Cost Declines for PV Systems", 2021); Texas generates more wind electricity than any other state (U.S. Energy Information Administration, EIA); hydropower supplied about 66% of Brazil's electricity in 2020 (EIA, Today in Energy); geothermal heat pumps use the stable temperature of the ground to heat and cool buildings, are durable, and have a high installation cost (U.S. Department of Energy, energy.gov, "Geothermal Heat Pumps"). In the U.S. most ethanol is made from corn; in Brazil, from sugar cane (EIA, "Biofuels explained").</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Portuguese allows two connectors in one sentence and drops the subject, so students say <i>Because it's cheap, so I use it</i> ✗, <i>Although they're noisy, but they're cheap</i> ✗ and <i>…because is reliable</i> ✗. They also start a written sentence with <i>Because…</i> and stop there (<i>I like it. Because it's clean.</i> ✗).</div>
<div class="box"><h4>AUDIO</h4>Track 14.1 The podcast (slow and natural) · Track 14.2 Word stress · Track 14.3 Sentences with conjunctions</div>""")

    # Page 2
    order = [("fossil fuels", "1"), ("geothermal heat pumps", "4"), ("hydropower", "5"), ("solar panels", "2"), ("wind turbines", "3")]
    ordl = " &nbsp;·&nbsp; ".join(f"{w} {A(n, 'min-width:6mm')}" for w, n in order)
    tf = [("There are three big differences between fossil fuels and renewable energy.", "F: two differences."),
          ("A home solar system in the U.S. is much cheaper than in 2010.", "T: more than 60% cheaper."),
          ("Wind turbines only work during the day.", "F: day or night, when the wind blows."),
          ("Texas produces more wind power than any other U.S. state.", "T"),
          ("Geothermal heat pumps are cheap to install.", "F: they're expensive to install."),
          ("Hydropower can have problems when it doesn't rain.", "T: the rivers get low.")]
    tfl = [f'<li value="{i+1}">{s} <b>T / F</b> {R(a)}</li>' for i, (s, a) in enumerate(tf)]
    cw = [(["but", "so"], "but", "Renewable energy will never run out,", "there's a limited amount of oil, gas and coal."),
          (["while", "because"], "while", "Fossil fuels cause climate change,", "renewable energy is much cleaner."),
          (["so", "because"], "so", "Solar panels don't work at night,", "many homes have a battery."),
          (["although", "because"], "although", "They're cheap to operate,", "they can be noisy."),
          (["so", "because"], "because", "Heat pumps are very reliable", "they rarely break down."),
          (["Because", "Although"], "Because", "", "every type has problems, we need a mix of clean energy.")]
    cwl = [f'<li value="{i+1}">{a} {ch(o, r)} {c}</li>' for i, (o, r, a, c) in enumerate(cw)]
    b.page(f"""{sec(2, "Listening: clean energy for beginners", "10 min")}
<p>Dr. Mark Rivera is back on the <i>Green City</i> podcast. Today's topic: clean energy.</p>
{audiocard(["14.1 · SLOW", "14.1 · NATURAL"])}
{sub("A", "Listen. Number the topics in the order you hear them (1–5).", "2 min", "14.1 · SLOW")}
<p style="margin:1mm 0">{ordl}</p>
{sub("B", "True (T) or false (F)? Correct the false sentences.", "4 min", "14.1 · SLOW")}
{twocol(tfl, 3)}
{sub("C", "Listen again. Choose the word you hear.", "4 min", "14.1 · NATURAL")}
<ol>{"".join(cwl)}</ol>""",
    22, """<p>A–B: numbers are words in the audio; write <i>2010</i>, <i>60%</i> and <i>2020</i> on the board. Ask "Why is that surprising?" about Texas (it's famous for oil). C: guess first, then listen; C leads to page 3. Sources: NREL, EIA, energy.gov (see the overview).</p>""")

    # Page 3
    b.page(f"""{sec(3, "Language focus: joining ideas", "10 min")}
{sub("A", "Read the sentences from the podcast. Then answer the questions.", "5 min")}
<table style="table-layout:fixed;margin-top:0;font-size:9pt"><tr><th>group 1</th><th>group 2</th><th>group 3</th></tr>
<tr><td>Heat pumps are reliable <b>because</b> they rarely break down.<br>Solar panels don't work at night<b>, so</b> many homes have a battery.</td>
<td>Wind turbines are cheap to operate<b>, although</b> they can be noisy.<br>Fossil fuels will run out<b>, but</b> the sun's energy won't.</td>
<td>Solar power works in many parts of the world<b>, and</b> it's much cheaper now.</td></tr></table>
<ol><li>Which group adds a similar idea? {R("3")} Which shows a contrast? {R("2")} Which shows cause and effect? {R("1")}</li>
<li>{ch(["because", "so"], "because")} introduces the reason. {ch(["because", "so"], "so")} introduces the result.</li>
<li>A clause has a subject and a verb. How many clauses are there in each sentence? {R("two")}</li>
<li>Look: <i><b>Although</b> they can be noisy<b>,</b> wind turbines are cheap.</i> When <i>although / because / if</i> comes first, we use a {ch(["comma", "period"], "comma")} after the first clause.</li></ol>
{sub("B", "Join the ideas with the word in parentheses.", "3 min")}
<ol><li>Hydropower is reliable. It's expensive to build. (but)<div class="wline">{R("Hydropower is reliable, but it's expensive to build.")}</div></li>
<li>It didn't rain. The rivers got low. (so)<div class="wline">{R("It didn't rain, so the rivers got low.")}</div></li>
<li>I want solar panels. They're cheaper now. (because)<div class="wline">{R("I want solar panels because they're cheaper now.")}</div></li></ol>
<div class="box sand"><h4>RULE</h4>Use <b>one</b> conjunction to join two clauses: <i>Because it's cheap, I use it</i> or <i>It's cheap, so I use it</i>, not <s>Because it's cheap, so I use it</s>. More on the next page: <b>Grammar reference</b>.</div>""",
    24, """<ol><li>A: circle the subjects and underline the verbs in each clause with the student. The comma before <i>although</i> in the middle is optional.</li>
<li>B: accept <i>although</i> in 1 (no comma needed when it's in the middle).</li></ol>""")

    grammar_ref.conjunctions(b)

    # Page 5
    b.page(f"""{sub("C", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>Because it's cheap, so I use it.</td><td><b>Because it's cheap, I use it.</b></td><td>one conjunction only.</td></tr>
<tr><td>Although it's old, but it's reliable.</td><td><b>Although it's old, it's reliable.</b></td><td>no but after although.</td></tr>
<tr><td>I like solar energy because is clean.</td><td><b>… because it's clean.</b></td><td>every clause needs a subject.</td></tr>
<tr><td>I take the bus. Because it's cheaper.</td><td><b>I take the bus because it's cheaper.</b></td><td>don't cut the sentence.</td></tr>
<tr><td>If it doesn't rain the rivers get low.</td><td><b>If it doesn't rain, the rivers get low.</b></td><td>comma after the if clause.</td></tr>
<tr><td>Wind energy is renovable.</td><td><b>Wind energy is renewable.</b></td><td>spelling: renew.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "5 min")}
{audiocard(["14.2", "14.3"])}
{sub("A", "Word stress. Listen and repeat. Underline the stressed syllable.", "2 min", "14.2")}
<table style="table-layout:fixed;margin-top:0"><tr>{"".join(f"<td style='text-align:center'><b>{w}</b></td>" for w in S142)}</tr></table>
<p class="small">{R("reNEWable · reLIable · TURbine · HYdropower · elecTRIcity · geoTHERmal · inSTALL · alTHOUGH")}</p>
{sub("B", "Sentences with conjunctions. Listen and repeat. Make a short pause at the comma.", "2 min", "14.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S143)}</div>
<div class="box" style="margin-top:1mm"><h4>SILENT LETTERS</h4><b>although</b> = /ɔːlˈðoʊ/: the <i>gh</i> is silent, and <i>th</i> is like the <i>th</i> in <i>the</i> · <b>turbine</b> = TUR-bine (two syllables) · <b>because</b> = /bɪˈkʌz/, often <i>'cause</i> in fast speech.</div>""",
    24, """<ol><li>4A: <i>electricity</i> has five syllables (e-lec-TRI-ci-ty); <i>hydropower</i> starts with "high".</li>
<li>4B: tap the table at each comma; the voice goes up before the comma and down at the end.</li></ol>""")

    # Page 6
    fm = [("If you don't have a lot of money a heat pump isn't a good option.", "comma after money"),
          ("Solar panels can't work at night, so many homes have a battery.", "✓"),
          ("Hydropower is a very old idea, so it's reliable.", "but / and: no cause and effect"),
          ("Because wind turbines can be noisy, so some people don't like them.", "delete so"),
          ("Fossil fuels will run out, but the sun's energy won't.", "✓"),
          ("Although solar power works in most places, takes up a lot of space.", "add it: it takes up"),
          ("While some people think turbines are beautiful, others think they're ugly.", "✓"),
          ("Although it may rain less in the future, hydropower won't always work.", "because, not although")]
    fml = [f'<li value="{i+1}">{s} {R(a)}</li>' for i, (s, a) in enumerate(fm)]
    op = [("renewable", "non-renewable"), ("save energy", "waste energy"), ("turn on", "turn off"), ("plug in", "unplug"), ("reliable", "unreliable"), ("cheap", "expensive")]
    opl = [f'<li value="{i+1}">{a} ≠ {A(o, "min-width:20mm")}</li>' for i, (a, o) in enumerate(op)]
    b.page(f"""{sec(5, "Practice", "8 min")}
{sub("A", "Find and correct the mistakes. Some sentences are correct (✓). Think about meaning, grammar and commas.", "5 min")}
<ol>{"".join(fml)}</ol>
{sub("B", "Word builder: energy opposites. Write the opposite.", "3 min")}
<div class="bank">expensive · non-renewable · turn off · unplug · unreliable · waste energy</div>
{twocol(opl, 3)}
<p class="small">Make two sentences with conjunctions: <i>I unplug my phone charger because…</i></p>""",
    22, """<ol><li>A: do number 1 together. 3: <i>It's a very old idea, and it's reliable</i> (or <i>but</i>, if the student sees a contrast). 8: <i>Because it may rain less in the future, hydropower won't always work.</i></li>
<li>B: adapted from the bonus lesson <i>Weather and climate</i> (Vocabulary to Go). Fossil fuels are <b>non-renewable</b>.</li></ol>""")

    # Page 7
    tbl = [("ethanol (fuel for cars)", "made from sugar cane in Brazil and corn in the U.S. · Brazil makes its own fuel", "uses land that could grow food · some forests are cut down"),
           ("solar panels at home", "cheaper now · lower electricity bills", "don't work at night · need a battery"),
           ("hydropower", "reliable · works day and night", "needs rain · big dams flood land")]
    tr = "".join(f"<tr><td><b>{a}</b></td><td>{p}</td><td>{n}</td></tr>" for a, p, n in tbl)
    b.page(f"""{sec(6, "Speaking: energy in Brazil", "12 min")}
<div style="display:flex;gap:3mm">
<div style="width:40mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo('B')}" style="width:40mm;height:27mm;object-fit:cover;display:block"></div>
<div style="width:40mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo('C')}" style="width:40mm;height:27mm;object-fit:cover;display:block"></div>
<p class="small" style="flex:1;margin:0">Brazil gets most of its electricity from water, and many cars use ethanol. Is that a green future?</p></div>
{sub("A", "Read the table. Make sentences with the conjunctions. Your teacher checks the conjunction and the comma.", "7 min")}
<table style="table-layout:fixed;margin-top:1mm;font-size:8.8pt"><tr><th style="width:30mm"></th><th>good points</th><th>problems</th></tr>{tr}</table>
<p class="small" style="margin:1mm 0">Use: <b>and · but · although · while · because · so · if</b> &nbsp; <i>Ethanol is made from sugar cane, so… · Although solar panels are cheaper now, … · If it doesn't rain, …</i></p>
{sub("B", "Your opinion.", "5 min")}
<ol><li>Which type of energy is best for your city? Why?</li><li>Would you install solar panels or buy an electric car? Why or why not?</li></ol>""",
    26, """<ol><li>A: the student says one sentence per conjunction; write the best ones on the board and mark the commas. Then change roles: you say a sentence with a mistake, and the student corrects it.</li>
<li>B: encourage <i>because</i> and <i>although</i> in the answers. Facts: EIA (hydropower and ethanol, see the overview).</li></ol>""")

    # Page 8
    pc = [("A2 Unit 09", "I can say how long things have been true with for and since."), ("A2 Unit 11", "I can check what's done and not done with already, yet and still."),
          ("A2 Unit 12", "I can write a friendly email with the right phrases."), ("A2 Unit 13", "I can explain causes and effects with zero and first conditionals."),
          ("A2 Unit 14", "I can join ideas with and, but, so, because and although.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    gap = [("We need new types of fuel", "because", "fossil fuels cause climate change."), ("There are several types of biofuel", ", but", "they are all expensive."),
           ("", "If", "countries make their own fuel, they will depend less on oil."), ("People cut down forests to grow sugar cane", ", so", "many animals lose their homes."),
           ("", "Although", "green diesel can grow in many places, it needs a lot of water."), ("Biodiesel is made from vegetable oil", "while", "green diesel is made from algae.")]
    gapl = "".join(f"<li>{a} {A(c, 'min-width:16mm')} {z}</li>" for a, c, z in gap)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Complete with a conjunction. Add a comma if you need one.</b></p>
<div class="bank">although · because · but · if · so · while</div>
<ol>{gapl}</ol>
<p style="margin-top:2mm"><b>2. A green future for my city (50–75 words).</b> Which types of energy does your city use? Which is the best for the future? Use at least four conjunctions and check your commas.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>1: from the original lesson's biofuel table (algae = very small plants that grow in water). Accept <i>although</i> in 6. Next class: the student reads the text; count the conjunctions together and check the commas.</p>""")

    b.extra("Audio scripts", f"""
{sub("14.1", "Green City: clean energy for beginners (slow and natural)")}
<p style="line-height:1.42">{"<br>".join(f"<b>{NAMES[n]}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("14.2", "Word stress")}
<p>{" · ".join(S142)}</p>
{sub("14.3", "Sentences with conjunctions")}
<p>{" ".join(S143)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 14 - A green future")
