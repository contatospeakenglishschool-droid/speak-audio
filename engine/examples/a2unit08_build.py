# Speak! Bridge A2 - Unit 08 "Adventure vacation" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 08", audio_json="audio_a2-unit-08.json", img_dir="img")

WARM = [("A", "They've", "climbed", "a mountain.", "climb"), ("B", "They've", "swum", "with fish.", "swim"), ("C", "She's", "ridden", "a horse.", "ride"),
        ("D", "He's", "gone", "kayaking.", "go"), ("E", "They've", "camped", "in the mountains.", "camp"), ("F", "He's", "jumped", "out of a plane.", "jump"),
        ("G", "He's", "done", "a zip line.", "do"), ("H", "He's", "run", "a marathon.", "run")]
PHOTOS = [(l, f"{p} {c[:-1]}", c) for l, s, p, c, v in WARM]

_r = json.load(open("roteiro.json"))["units"]["a2-unit-08"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["08.1 First day"].split("\n")]
S082 = [x.split(": ", 1)[1] for x in _r["08.2 Repeat participles"].split("\n")]
S083 = [x.split(": ", 1)[1] for x in _r["08.3 Repeat questions"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 08", "Adventure vacation", "Life experiences · <b>present perfect (ever / never) and past simple</b>",
                       [("YOU CAN", "ask about life experiences and give details about them"),
                        ("LANGUAGE", "Have you ever swum with manatees? · I've never camped. · I did one when I was twenty."),
                        ("PRONUNCIATION", "been · done · swum · ridden · Have you ever…? /həvjə/")])
    wl = [f'<li value="{i+1}"><b>{l}</b> {s} {A(p, "min-width:16mm")} {c} <span class="small">({v})</span></li>' for i, (l, s, p, c, v) in enumerate(WARM)]
    b.page(f"""{sec(1, "Warm-up: adventure experiences", "8 min")}
{sub("A", "Look at the photos. Complete the sentences with the past participle of the verbs.", "4 min")}
{photo_grid(T, PHOTOS)}
{twocol(wl, 5)}
{sub("B", "Answer the questions.", "4 min")}
<ol><li>Which three participles are regular (-ed)? {R("climbed, camped, jumped")} Which verb has the same form in the infinitive and the participle? {R("run")}</li>
<li>Which activity is the most dangerous? Which is the most fun?</li></ol>""",
    22, """<ol><li>A: <b>go kayaking</b> → <i>gone</i>; Americans also say <i>been kayaking</i> (= went and came back). <b>swim → swam → swum</b>; <b>ride → rode → ridden</b>.</li>
<li>B: don't ask about the student's own experiences yet; that comes in the Speaking.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Adventure activities · past participles</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Ana and Marcos's first day of an adventure vacation in Florida</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Present perfect for experiences vs past simple for details · been / gone</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>The present perfect: form, uses, present perfect or past simple</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>5 min</td><td>Irregular participles · Have you ever…?</td><td>5</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Ana's message · Word builder: go / do / ride</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Truth or lie? · find out more</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework (50–75 words)</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>It's summer in Brazil and winter in Florida: <b>Ana and Marcos</b> are on an adventure vacation near cousin Carol's home. On the first day, their guide Jake (invented; one-off male voice, Chirp 3 HD Charon) asks about their experiences: kayaking, swimming with manatees, a zip line, camping. Facts: Crystal River, Florida, is the largest natural winter refuge for manatees in the world; hundreds gather at its warm springs in winter, and it is the only place in the US where swimming with wild manatees is legal (Smithsonian Magazine, "There's Only One Place in the United States Where It's Legal to Swim With Wild Manatees"; US Fish and Wildlife Service, Crystal River National Wildlife Refuge).</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Portuguese uses one past form for all finished experiences, so students mix the forms: <i>I have been in Florida last year</i> ✗ → <b>I went to Florida last year</b>; <i>Have you ever went…?</i> ✗ → <b>been</b>; and answer <i>Have you ever…?</i> with <i>Yes, I did</i> ✗ → <b>Yes, I have</b>. Also <i>I have gone to Orlando twice</i> ✗ → <b>been</b> (gone = still there). Note: Americans sometimes say <i>Did you ever…?</i>; teach <i>Have you ever…?</i> as the standard form.</div>
<div class="box"><h4>AUDIO</h4>Track 08.1 The first day (slow and natural) · Track 08.2 Past participles · Track 08.3 Questions and answers</div>""")

    # Page 2
    acts = [("kayaking", True), ("running a marathon", False), ("swimming with manatees", True), ("horseback riding", False), ("a zip line", True), ("skydiving", False), ("camping", True)]
    al = " &nbsp; ".join(f"☐ {w}{(' ' + R('✓')) if ok else ''}" for w, ok in acts)
    tf = [("Ana has kayaked before.", "T: many times, with Carol."), ("Marcos has seen a manatee.", "F: he's never seen one."),
          ("Ana has seen a manatee in real life.", "F: only in a documentary."), ("Marcos did a zip line when he was twenty.", "T: in the mountains in Brazil."),
          ("Ana loves high places.", "F: she's a little afraid of heights."), ("Ana has camped before.", "F: Marcos has; she hasn't.")]
    tfl = [f'<li value="{i+1}">{s} <b>T / F</b> {R(a)}</li>' for i, (s, a) in enumerate(tf)]
    b.page(f"""{sec(2, "Listening: the first day", "10 min")}
<p>It's winter in Florida and summer in Brazil. Ana and Marcos are on an adventure vacation near Carol's home. On the first day, they meet their guide, Jake.</p>
{audiocard(["08.1 · SLOW", "08.1 · NATURAL"])}
{sub("A", "Listen. Which four activities do they talk about? Check (✓).", "2 min", "08.1 · SLOW")}
<p style="font-weight:600">{al}</p>
{sub("B", "Listen again. True (T) or false (F)? Correct the false sentences.", "5 min", "08.1 · NATURAL")}
{twocol(tfl, 4)}
{sub("C", "Which activity would you like to try? Which one would you never do?", "3 min")}""",
    22, """<p>A: explain <b>manatee</b> (a big, slow sea animal that also lives in Brazil; show a photo) and <b>zip line</b>. B: ask for the exact words: <i>I've never seen a manatee. I did one when I was twenty.</i> If there's time, read the script together (TB last page).</p>""")

    # Page 3
    qc = [(["climbed", "has climbed"], "has climbed", "Marcos", "a mountain, but he doesn't remember the year."), (["did", "has done"], "did", "He", "a zip line when he was twenty."),
          (["never camped", "has never camped"], "has never camped", "Ana", "."), (["saw", "has seen"], "saw", "She", "a manatee in a documentary last month."),
          (["Did you ever go", "Have you ever been"], "Have you ever been", "", "to Florida?"), (["went", "have been"], "went", "Yes, I", "to Orlando in 2023.")]
    qcl = [f'<li value="{i+1}">{a} {ch(o, r)} {c}</li>' for i, (o, r, a, c) in enumerate(qc)]
    b.page(f"""{sec(3, "Language focus: experiences and details", "10 min")}
{sub("A", "Read the sentences from the conversation. Then choose the correct option.", "3 min")}
<table style="table-layout:fixed;margin-top:0;font-size:9pt"><tr><th>1</th><th>2</th></tr>
<tr><td>Have you ever been kayaking? · Yes, I have. · I've never seen a manatee.</td><td>Last year we kayaked on a river. · I did one when I was twenty.</td></tr></table>
<ol><li>Group 1 uses the {ch(["present perfect", "past simple"], "present perfect")}. We {ch(["say", "don't say"], "don't say")} when it happened.</li>
<li>Group 2 uses the {ch(["present perfect", "past simple"], "past simple")}. We {ch(["say", "don't say"], "say")} when it happened.</li></ol>
<div class="box" style="margin-top:1mm"><h4>HOW IT WORKS</h4>
<b>Experience (in your life, no time):</b> Have you <b>ever</b> + participle? → Yes, I have. / No, I haven't. · I've <b>never</b> + participle.<br>
<b>Details (when, where, how):</b> past simple → When did you go? Did you like it? I went last year. It was amazing!<br>
<b>been / gone:</b> She's <b>been</b> to Florida (she went and came back). · She's <b>gone</b> to Florida (she's there now).</div>
{sub("B", "Quick check. Choose the correct form.", "5 min")}
{twocol(qcl, 4)}
<div class="box sand"><h4>TIME WORDS</h4>Present perfect: <b>ever, never, before, many times, twice</b> · Past simple: <b>yesterday, last year, in 2023, when I was twenty, two weeks ago</b></div>""",
    24, """<ol><li>A: draw a "life line": experiences anywhere on the line (present perfect) vs a point with a date (past simple). A conversation usually starts with the present perfect and continues with the past simple.</li>
<li>B: 5–6 show the typical pattern: question in present perfect, details in past simple.</li></ol>""")

    # Grammar reference (before Common mistakes)
    grammar_ref.present_perfect(b)

    # Page 4
    b.page(f"""{sub("C", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>I have been in Florida last year.</td><td><b>I went to Florida last year.</b></td><td>last year = past simple.</td></tr>
<tr><td>Have you ever went to the US?</td><td><b>Have you ever been to the US?</b></td><td>participle: been.</td></tr>
<tr><td>Have you ever ridden a horse? — Yes, I did.</td><td><b>Yes, I have.</b></td><td>same auxiliary.</td></tr>
<tr><td>I never have swum with dolphins.</td><td><b>I've never swum with dolphins.</b></td><td>have + never + participle.</td></tr>
<tr><td>I have gone to Orlando twice.</td><td><b>I've been to Orlando twice.</b></td><td>been = went and came back.</td></tr>
<tr><td>She has swimmed in the ocean.</td><td><b>She has swum in the ocean.</b></td><td>swim – swam – swum.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "5 min")}
{audiocard(["08.2", "08.3"])}
{sub("A", "Irregular past participles. Listen and repeat.", "2 min", "08.2")}
<table style="table-layout:fixed;margin-top:0"><tr>{"".join(f"<td style='text-align:center'><b>{w}</b></td>" for w in S082)}</tr></table>
{sub("B", "Questions and answers. Listen and repeat.", "2 min", "08.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S083)}</div>
<div class="box" style="margin-top:1mm"><h4>WEAK AND STRONG HAVE</h4>In questions, <i>have</i> is weak: <b>Have you ever…?</b> /həvjə ˈevər/. In short answers, it's strong: <i>Yes, I <b>HAVE</b>.</i> <b>been</b> = /bɪn/ in American English; <b>done</b> and <b>swum</b> rhyme with <i>sun</i>.</div>""",
    24, """<ol><li>4A: Brazilians often say <i>been</i> like <i>bean</i>; Americans usually say /bɪn/. <i>ridden</i> = RID-n.</li>
<li>4B: <i>When did you go?</i> goes down at the end; <i>Did you like it?</i> goes up.</li></ol>""")

    # Page 5
    msg = [("ever / be", "Have you ever been"), ("never / see", "'ve never seen"), ("swim", "swam"), ("be", "was"), ("do", "did"),
           ("watch", "watched"), ("never / do", "'ve never done"), ("camp", "has camped"), ("love", "loved")]
    g = [A(v, "min-width:22mm") for _, v in msg]
    h = [f"<span class='small'>({x})</span>" for x, _ in msg]
    text = (f"Hi Carol! <sup>1</sup>{g[0]} {h[0]} to Crystal River? Before this week, I <sup>2</sup>{g[1]} {h[1]} a manatee. On Tuesday we <sup>3</sup>{g[2]} {h[2]} with six of them! "
            f"The water <sup>4</sup>{g[3]} {h[3]} warm and clear. On Thursday Marcos <sup>5</sup>{g[4]} {h[4]} the zip line, but I <sup>6</sup>{g[5]} {h[5]} from the ground. "
            f"I <sup>7</sup>{g[6]} {h[6]} a zip line, and I'm still afraid! Marcos <sup>8</sup>{g[7]} {h[7]} many times, but last night was my first night in a tent… and I <sup>9</sup>{g[8]} {h[8]} it! See you on Saturday. Ana")
    wb = [("go", "kayaking · camping · hiking · skydiving"), ("do", "a zip line · yoga · a marathon"), ("ride", "a horse · a bike · a motorcycle")]
    wbt = "".join(f"<tr><td style='width:16mm'>{A(v, 'min-width:12mm')}</td><td>{n}</td></tr>" for v, n in wb)
    b.page(f"""{sec(5, "Practice", "8 min")}
{sub("A", "Ana writes to Carol. Complete with the present perfect or the past simple.", "5 min")}
<p style="line-height:1.95;margin:1mm 0">{text}</p>
{sub("B", "Word builder: adventure verbs. Write go, do or ride.", "3 min")}
<table style="table-layout:fixed;margin-top:0;font-size:9pt;width:80%">{wbt}</table>
<p class="small">Make three sentences about you: <i>I've never gone skydiving. I rode a horse last summer…</i></p>""",
    22, """<ol><li>A: 1, 2, 7 and 8 are experiences (no time); 3–6 and 9 are details of this week (past simple). Ask the student to underline the time words.</li>
<li>B: <b>go + -ing</b> for activities (go kayaking); <b>do</b> for events; <b>ride</b> for things you sit on.</li></ol>""")

    # Page 6
    exp = ["ride a horse", "climb a mountain", "swim in a waterfall", "camp in the forest", "do a zip line", "run more than 10 km", "see a famous person", "my own idea: …"]
    et = "".join(f"<tr><td>{e}</td><td></td><td></td><td>☐ true ☐ lie</td></tr>" for e in exp)
    b.page(f"""{sec(6, "Speaking", "12 min")}
{sub("A", "Truth or lie? Ask your teacher about these experiences. Then ask for details with the past simple. Your teacher must lie at least twice. Can you find the lies?", "7 min")}
<table style="table-layout:fixed;margin-top:0;font-size:9pt"><tr><th>Have you ever…?</th><th style="width:14mm">yes / no</th><th>details (when? where? how?)</th><th style="width:28mm">true or lie?</th></tr>{et}</table>
<div class="msg" style="max-width:none;padding:1.5mm 4mm;line-height:1.5"><b>You:</b> Have you ever ridden a horse? <b>Teacher:</b> Yes, I have. <b>You:</b> When did you ride it? What was its name? <b>Teacher:</b> In Minas, in 2019. Its name was Lucky. <b>You:</b> I think that's a lie!</div>
{sub("B", "Change roles. Your teacher asks you. Lie at least twice!", "5 min")}""",
    26, """<ol><li>A: lie twice with confident details. The student must ask at least two past simple follow-up questions before deciding.</li>
<li>B: correct <i>Yes, I did</i> → <i>Yes, I have</i> and time words with the present perfect.</li></ol>""")

    # Page 7
    pc = [("A2 Unit 04", "I can use adjectives and nouns with the right preposition."), ("A2 Unit 05", "I can ask about words in class and name parts of speech."),
          ("A2 Unit 06", "I can praise, compliment and congratulate people, and respond politely."), ("A2 Unit 07", "I can talk about accidents that just happened with the present perfect."),
          ("A2 Unit 08", "I can ask about life experiences and give details with the past simple.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [(["Did you ever break", "Have you ever broken"], "Have you ever broken", "Jake:", "a bone?"), (["I never broke", "I've never broken"], "I've never broken", "Marcos: No,", "a bone, but"),
          (["I sprained", "I've sprained"], "I sprained", "", "my ankle last year."), (["did you sprain", "have you sprained"], "did you sprain", "Jake: How", "it?"),
          (["I tripped", "I've tripped"], "I tripped", "Marcos:", "on the stairs at work."), (["Did you ever have", "Have you ever had"], "Have you ever had", "Jake: And you, Ana?", "a head injury?")]
    hl = "".join(f"<li>{a} {ch(o, r)} {c}</li>" for o, r, a, c in hw)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Jake asks about their health. Choose the correct form.</b></p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. My best adventure (50–75 words).</b> Write about an exciting experience. Start with the present perfect (<i>I've been… / I've done…</i>), then give details with the past simple: when, where, who with, how you felt.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class: ask follow-up questions about the student's adventure (<i>When did you…? Was it scary?</i>). Check present perfect vs past simple and the participles.</p>""")


    b.extra("Audio scripts", f"""
{sub("08.1", "The first day (slow and natural)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("08.2", "Past participles")}
<p>{" · ".join(S082)}</p>
{sub("08.3", "Questions and answers")}
<p>{" ".join(S083)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 08 - Adventure vacation")
