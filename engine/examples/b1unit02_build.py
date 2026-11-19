# Speak! Progress B1 - Unit 02 "Character and feelings" (all English) - lean B1 format (rebuilt 2026-11-19)
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Progress"
import lean
from lean import talk
setup(band="B1 · UNIT 02", audio_json="audio_b1-unit-02.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-02"]
S021 = [x.split(": ", 1) for x in _r["02.1 Danny calls his mom"].split("\n")]
S022 = [x.split(": ", 1)[1] for x in _r["02.2 Repeat: word stress in word families"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'
    def lines(n):
        return '<div class="wline"></div>' * n

    # 1 Warm-up
    cover = cover_html(T, "LEVEL B1 · UNIT 02", "Character and feelings", "Describing people · <b>personality adjectives, softening, feelings</b>",
                       [("YOU CAN", "describe people's personality politely and talk about feelings"),
                        ("LANGUAGE", "She's usually cheerful. · He can be a bit moody. · She tends to… · He's not very tidy. · pride, embarrassment"),
                        ("PRONUNCIATION", "word stress in word families: GENerous → geneROSity")])
    q = ["arrogant", "boring", "clever", "generous", "loyal", "moody", "outgoing", "patient", "pessimistic", "rude"]
    qual = ["clever", "generous", "loyal", "outgoing", "patient"]
    fl = ["arrogant", "boring", "moody", "pessimistic", "rude"]
    b.page(f"""{sec(1, "Warm-up: what are they like?", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["What do you think these friends are like? Why?", "What makes a good friend?", "Which three words would your friends use to describe you?"], "START TALKING")}</div></div>
{sub("A", "Qualities or flaws? Write the adjectives in the correct column.", "3 min")}
<div class="bank">{" · ".join(q)}</div>
<div style="display:flex;gap:5mm;font-size:8.8pt"><div style="flex:1"><b>qualities (positive)</b>{('<p style="margin:1mm 0">' + R(", ".join(qual)) + '</p>') if T else lines(2)}</div><div style="flex:1"><b>flaws (negative)</b>{('<p style="margin:1mm 0">' + R(", ".join(fl)) + '</p>') if T else lines(2)}</div></div>
{talk(["Describe a friend or a family member with three adjectives from A.", "Which quality is the most important in a boss? And in a friend?"], "USE THE WORDS")}""",
    26, """<ol><li>Start with the questions in the top box (4 minutes).</li>
<li>A: <i>clever</i> (US often <i>smart</i>). Let the student describe people freely in the last box; you'll focus on softening (<i>a bit, not very</i>) on pages 3–4.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Danny's video call: who he talks about · what they're like · Talk about it", "Describing character: frequency, can be, tend to, seem, softening",
                      "Choose the meaning · make it softer · Use it (oral)", "Functional language · word stress (02.2) · long turn about a feeling",
                      "Kate's blog (feeling nouns) · opposites · word choice · writing"),
        "Danny (Chirp3-HD-Puck) is in his second week in São Paulo. On a video call with his mom Rita (Chirp3-HD-Aoede), he describes Ana, his hostel roommate Bruno (from Porto Alegre) and the hostel owner Mrs. Lima. In the homework, Kate writes a new post for her Sweet Kate Bakery blog (A2 Unit 46). No real-world facts.",
        "Students say <i>She's a bit friendly</i>, start sentences with <i>Always</i>, and use false friends: <i>sympathetic</i> (≠ nice), <i>sensible</i> (≠ sensitive), <i>educated</i> (≠ polite), <i>nervous</i> (≠ angry). They also stress word families wrongly (<i>geNEROus, generoSIty</i>).",
        "Track 02.1 Danny calls his mom (natural and slow) · Track 02.2 Repeat: word stress in word families"))

    # 2 Listening
    ppl = [("Ana", True), ("Tom", False), ("Bruno", True), ("Mrs. Lima", True), ("a teacher", False)]
    ppll = " &nbsp; ".join(f"☐ {t}{(' ' + R('✓')) if ok else ''}" for t, ok in ppl)
    tb = [("Ana", "cheerful, generous", "a bit impatient in traffic"), ("Bruno", "outgoing, funny", "not very tidy; a bit moody in the morning"), ("Mrs. Lima", "really kind (deep down)", "seems a bit cold at first")]
    tbr = "".join(f"<tr><td><b>{n}</b></td><td style='height:7mm'>{R(g) if T else ''}</td><td>{R(x) if T else ''}</td></tr>" for n, g, x in tb)
    b.page(f"""{sec(2, "Listening: new people, new life", "12 min")}
<div style="display:flex;gap:3mm;align-items:center"><p style="flex:1;margin:0">It's Danny's second week in São Paulo. He's on a video call with his mom, Rita, in Chicago. She wants to know about the people he has met.</p>{img('B', 34, 22)}</div>
{audiocard(["02.1 · NATURAL", "02.1 · SLOW"])}
{sub("A", "Listen at natural speed. Which people does Danny talk about? Check (✓).", "2 min", "02.1 · NATURAL")}
<p style="font-weight:600;margin:.3mm 0">{ppll}</p>
{sub("B", "Listen again. What are they like? Complete the table.", "4 min", "02.1 · NATURAL")}
<table style="margin:0;font-size:8.8pt"><tr><th style="width:24mm">person</th><th>good side</th><th>not so good side</th></tr>{tbr}</table>
{talk(["How does Rita feel when she hears that Danny was sick? How do you know?", "Is Danny happy in São Paulo? Why?", "Who in your life tends to worry a lot? Who is a bit impatient?"])}""",
    26, """<ol><li>A–B: 6 minutes. Pause after each person in B. <i>Honk</i> = use the car horn. <i>Homesick</i> = sad because you miss home.</li>
<li>Talk about it: 6 minutes. 1: worried and a bit upset (she asks why he didn't tell her). 2: yes: he has made friends and people are kind; he's only a little homesick.</li></ol>""")

    # 3 Grammar reference
    lean.grammar_in_class(b, grammar_ref.describing_character)

    # 4 Practice
    lf = [("She's a bit impatient. / He's not very tidy.", ["negative", "positive"], "negative", "We use <i>a bit</i> with", "adjectives."),
          ("He can be a bit moody in the morning.", ["sometimes true", "always true"], "sometimes true", "<i>Can be</i> means it is", "."),
          ("She tends to honk a lot.", ["infinitive", "-ing form"], "infinitive", "<i>Tend to</i> + ", "= something that usually happens."),
          ("She seems a bit cold at first.", ["a first impression", "a fact"], "a first impression", "<i>Seem</i> describes", ".")]
    lfl = "".join(f"<li><i>\"{e}\"</i><br>{a} {ch(o, r)} {z}</li>" for e, o, r, a, z in lf)
    use = ["Describe your boss or a teacher. Use <i>can be a bit…</i>", "Describe a relative. Use <i>tends to…</i>", "Describe someone you met recently. Use <i>seems…</i>",
           "Describe yourself honestly. Use <i>not very…</i>", "Your teacher says a direct sentence (<i>He's lazy.</i>). Make it softer."]
    b.page(f"""{sec(4, "Practice: describing character", "10 min")}
{sub("A", "Read the sentences from the conversation. Choose the correct option.", "3 min")}
<ol style="line-height:1.55;font-size:9pt;margin:0">{lfl}</ol>
{sub("B", "Make it softer. Rewrite with a bit or not very.", "1 min")}
<p style="margin:.5mm 0;line-height:1.8">He's rude. → {A("He's a bit rude. / He's not very polite.", "min-width:54mm")}</p>
<div class="box sand"><h4>RULE</h4><b>adverbs of frequency</b>: after <i>be</i>, before the main verb · <b>can be</b> + adjective = sometimes true · <b>tend to</b> + infinitive = usually · <b>seem</b> = first impression · <b>softening</b>: <i>a bit</i> + negative adjective, <i>not very</i> + positive adjective. See the <b>Grammar reference</b> on page 3.</div>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    24, """<ol><li>A–B: 4 minutes. In American English, direct negative adjectives about a person (<i>He's lazy.</i>) can sound rude; softening is the norm at work.</li>
<li>Use it: 6 minutes, all oral. Ask a follow-up after each answer: <i>Can you give me an example?</i></li></ol>""")

    # 5 Speaking
    fc = ["pride", "embarrassment", "jealousy", "anger", "happiness", "boredom"]
    b.page(f"""{sec(5, "Speaking: people and feelings", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>describe a person</th><th>be polite</th><th>tell a story about a feeling</th><th>react</th></tr>
<tr><td><i>What's he like? · She's the kind of person who… · He comes across as…</i></td><td><i>She can be a bit… · He's not very… · To be fair, he's…</i></td><td><i>I'll never forget the time… · I felt so… · I was full of…</i></td><td><i>I know what you mean. · How embarrassing! · You must have been so proud!</i></td></tr></table></div>
{audiocard(["02.2"])}
{sub("A", "Word stress. Listen and repeat. The stress often moves: GENerous → geneROSity.", "4 min", "02.2")}
<p style="margin:.3mm 0;line-height:1.6;font-size:8.6pt">{" &nbsp;·&nbsp; ".join(S022).replace(".", "") if not T else "<b>GEN</b>erous / gene<b>ROS</b>ity · <b>CU</b>rious / curi<b>OS</b>ity · <b>SYM</b>pathy / sympa<b>THET</b>ic · <b>CON</b>fident / <b>CON</b>fidence · em<b>BAR</b>rassed / em<b>BAR</b>rassment · <b>PES</b>simist / pessi<b>MIS</b>tic · <b>PUNC</b>tual / punctu<b>AL</b>ity · <b>AR</b>rogant / <b>AR</b>rogance"}</p>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("B", "Long turn. Choose a feeling. Prepare for one minute, then talk for two minutes about a time you or someone you know felt it.", "8 min")}
<p style="margin:.5mm 0;font-weight:700;color:#176074">{" · ".join(fc)}</p>
<ul style="line-height:1.45;font-size:8.9pt;margin:0"><li>when and where it happened, and who was there</li><li>what happened and why you felt that way</li><li>what you did, and how you feel about it now</li></ul></div>{img('D', 32, 24)}</div>
{talk(["What stereotypes have you heard about Brazilians? And about Americans?", "How true are they, in your experience? Can stereotypes be dangerous?"])}""",
    28, """<ol><li>B: don't interrupt; then ask follow-ups with the reactions in the box. Fluency option (3-2-1): the same story in 2 minutes, then in 1 minute.</li>
<li>Talk about it: keep it respectful; encourage <i>tend to / can be</i> for generalizations. Last 3 minutes: wrap-up (two corrections and <i>Can you describe people politely?</i>).</li></ol>""")

    # H Homework
    fe = [("angry", "anger"), ("generous", "generosity"), ("bored", "boredom"), ("embarrassed", "embarrassment"), ("proud", "pride"), ("lazy", "laziness")]
    g = [A(n, "min-width:22mm") + f" ({a})" for a, n in fe]
    px = [("honest", "dishonest"), ("patient", "impatient"), ("responsible", "irresponsible"), ("reliable", "unreliable")]
    pxl = " &nbsp;·&nbsp; ".join(f"{a} → {A(o, 'min-width:20mm')}" for a, o in px)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Kate writes a post for her bakery blog. Complete it with the nouns of the adjectives.", "")}</div>{img('C', 28, 18)}</div>
<div class="box" style="line-height:1.8;font-size:8.8pt;margin:.5mm 0"><b>A week of feelings at Sweet Kate Bakery</b><br>What a week! On Monday, our oven broke and I couldn't hide my {g[0]}. On Tuesday, a regular customer brought me flowers for no reason. What {g[1]}! Wednesday was very slow, and by three o'clock {g[2]} set in. On Thursday, I dropped a whole wedding cake in front of the customers. The {g[3]}! On Friday, my assistant decorated her first cake alone, and I felt so much {g[4]}. And Saturday? I planned to clean the kitchen, but {g[5]} won. See you next week!</div>
{sub("B", "Write the opposites with un-, im-, dis- or ir-.", "")}
<p style="margin:.3mm 0;line-height:1.9;font-size:8.8pt">{pxl}</p>
{lean.watch_out([("She's very sympathetic. (= nice)", "She's very nice / friendly.", "<i>sympathetic</i> = shows understanding when you have a problem."), ("He's very sensible. He cries at movies.", "He's very sensitive.", "<i>sensible</i> = practical, makes good decisions."), ("Your son is very educated. (= good manners)", "Your son is very polite.", "<i>educated</i> = has studied a lot.")])}
{lean.writing_task(sub, "Describe a person you admire: a friend, a family member or a coworker. Use softening and one feeling noun.", "The person I admire most is… She's usually… To be fair, she can be a bit…", ["four adjectives", "softening", "a feeling noun", "100–150 words"], "I can describe people's personality politely.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class. When you correct the writing, focus on adverb position, softening and false friends.</p>""")

    b.extra("Audio script", f"""
{sub("02.1", "Danny calls his mom (natural and slow)")}
<p style="line-height:1.4;font-size:9pt">{"<br>".join(f"<b>{n}:</b> {t}" if n != "Narrator" else f"<i>{t}</i>" for n, t in S021)}</p>
{sub("02.2", "Repeat: word stress in word families")}
<p>{" · ".join(S022)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 02 - Character and feelings")
