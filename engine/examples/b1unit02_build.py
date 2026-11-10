# Speak! Progress B1 - Unit 02 "Character and feelings" (all English) - B1 format (2026-11-09)
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Progress"
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

    # Page 1 - Warm-up
    cover = cover_html(T, "LEVEL B1 · UNIT 02", "Character and feelings", "Describing people · <b>personality adjectives, softening, feelings</b>",
                       [("YOU CAN", "describe people's personality politely and talk about feelings"),
                        ("LANGUAGE", "She's usually cheerful. · He can be a bit moody. · She tends to… · He's not very tidy. · pride, embarrassment"),
                        ("PRONUNCIATION", "word stress in word families: GENerous → geneROSity")])
    q = ["funny", "punctual", "loyal", "tolerant", "clever", "generous", "outgoing", "moody", "pessimistic", "rude", "boring", "reserved", "arrogant", "patient"]
    qual = ["clever", "funny", "generous", "loyal", "outgoing", "patient", "punctual", "tolerant"]
    fl = ["arrogant", "boring", "moody", "pessimistic", "reserved", "rude"]
    b.page(f"""{sec(1, "Warm-up: what are they like?", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 58, 38)}<div style="flex:1">
{sub("A", "Look at the photo and discuss.", "3 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0"><li>What do you think these friends are like? Why?</li><li>What makes a good friend?</li><li>Which three words would your friends use to describe you?</li></ol></div></div>
{sub("B", "Qualities or flaws? Write the adjectives in the correct column.", "3 min")}
<div class="bank">{" · ".join(sorted(q))}</div>
<div style="display:flex;gap:5mm;font-size:8.8pt"><div style="flex:1"><b>qualities (positive)</b>{('<p style="margin:1mm 0">' + R(", ".join(qual)) + '</p>') if T else lines(2)}</div><div style="flex:1"><b>flaws (negative)</b>{('<p style="margin:1mm 0">' + R(", ".join(fl)) + '</p>') if T else lines(2)}</div></div>
{sub("C", "Describe a friend or a family member to your teacher. Use three adjectives from B.", "2 min")}
<p class="small" style="margin:0"><i>My brother is usually outgoing, but he can be a bit moody. He's never boring!</i></p>""",
    25, """<ol><li>B: <i>reserved</i> and <i>clever</i> can be positive or negative, depending on the context; accept either column if the student explains. <i>Clever</i> (US) is often <i>smart</i>.</li>
<li>C: let the student talk freely; you'll focus on softening (<i>a bit, not very</i>) on page 3.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 60 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Discussion · qualities and flaws</td><td>1</td></tr>
<tr><td>2 Listening</td><td>12 min</td><td>Danny's video call: people he has met in São Paulo</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>8 min</td><td>Describing character: frequency, can be, tend to, seem, softening</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Describing character (study at home)</td><td>4</td></tr>
<tr><td>4 Vocabulary lab + pronunciation</td><td>8 min</td><td>Negative prefixes · opposites · false friends · word stress</td><td>5</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Kate's blog: feeling nouns · what should they be like?</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Functional language · long turn about a feeling · stereotypes</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>4 min</td><td>Can-do · language notes · writing homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Danny (Chirp3-HD-Puck) is in his second week in São Paulo. On a video call with his mom Rita (Chirp3-HD-Aoede), he describes Ana, his hostel roommate Bruno (from Porto Alegre) and the hostel owner Mrs. Lima (both new, no voice yet). In the Practice, Kate writes a new post for her Sweet Kate Bakery blog (A2 Unit 46). No real-world facts.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students say <i>She's a bit friendly</i>, start sentences with <i>Always</i>, and use false friends: <i>sympathetic</i> (≠ nice), <i>sensible</i> (≠ sensitive), <i>educated</i> (≠ polite), <i>nervous</i> (≠ angry). They also stress word families wrongly (<i>geNEROus, generoSIty</i>).</div>
<div class="box"><h4>AUDIO</h4>Track 02.1 Danny calls his mom (natural and slow) · Track 02.2 Repeat: word stress in word families</div>
<p class="small">Source: Linguahouse <i>Character and feelings</i> (vocabulary lesson, no audio). The listening, the blog and the speaking tasks are original Speak! material.</p>""")

    # Page 2 - Listening
    ppl = [("Ana", True), ("Tom", False), ("Bruno", True), ("Mrs. Lima", True), ("a teacher", False)]
    ppll = " &nbsp; ".join(f"☐ {t}{(' ' + R('✓')) if ok else ''}" for t, ok in ppl)
    tb = [("Ana", "cheerful, generous", "a bit impatient in traffic"), ("Bruno", "outgoing, funny", "not very tidy; a bit moody in the morning"), ("Mrs. Lima", "really kind (deep down)", "seems a bit cold at first")]
    tbr = "".join(f"<tr><td><b>{n}</b></td><td style='height:7mm'>{R(g) if T else ''}</td><td>{R(x) if T else ''}</td></tr>" for n, g, x in tb)
    b.page(f"""{sec(2, "Listening: new people, new life", "12 min")}
<div style="display:flex;gap:3mm;align-items:center"><p style="flex:1;margin:0">It's Danny's second week in São Paulo. He's on a video call with his mom, Rita, in Chicago. She wants to know about the people he has met.</p>{img('B', 34, 22)}</div>
{audiocard(["02.1 · NATURAL", "02.1 · SLOW"])}
{sub("A", "Listen at natural speed. Which people does Danny talk about? Check (✓).", "2 min", "02.1 · NATURAL")}
<p style="font-weight:600;margin:.3mm 0">{ppll}</p>
{sub("B", "Listen again. What are they like? Complete the table. Use the slow version only if you need it.", "5 min", "02.1 · NATURAL")}
<table style="margin:0;font-size:8.8pt"><tr><th style="width:24mm">person</th><th>good side</th><th>not so good side</th></tr>{tbr}</table>
{sub("C", "Think about it. Discuss with your teacher.", "3 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0"><li>How does Rita feel when she hears that Danny was sick? How do you know? {R("Worried and a bit upset: she asks why he didn't tell her, and says she always worries.") if T else ""}</li>
<li>Is Danny happy in São Paulo? Find two reasons in the conversation. {R("Yes: he has made friends, people are kind to him, he says he's really happy. He's only a little homesick.") if T else ""}</li></ol>
<div class="box sand" style="margin-top:1.2mm"><h4>NOTICE: USEFUL CHUNKS</h4><i>That's so thoughtful of her. · She's a bit impatient, though. · She tends to honk a lot. · He's not very tidy. · Deep down, she's really kind. · You're not very tidy either!</i></div>""",
    24, """<ol><li>Play the natural version for A; for B, play it again and pause after each person. <i>Honk</i> = use the car horn. <i>Homesick</i> = sad because you miss home.</li>
<li>C: accept any answer the student supports with words from the audio. Ask: <i>Who in your life tends to worry a lot?</i></li></ol>""")

    # Page 3 - Language focus
    lf = [("She's a bit impatient. / He's not very tidy.", ["negative", "positive"], "negative", "We use <i>a bit</i> with", "adjectives. <i>Not very</i> + a positive adjective sounds more polite."),
          ("He can be a bit moody in the morning.", ["sometimes true", "always true"], "sometimes true", "<i>Can be</i> means it is", "of the person."),
          ("She tends to honk a lot.", ["infinitive", "-ing form"], "infinitive", "<i>Tend to</i> + ", "= something that usually happens."),
          ("She seems a bit cold at first, but deep down she's really kind.", ["a first impression", "a fact"], "a first impression", "<i>Seem</i> describes", ". <i>Deep down</i> = the real personality.")]
    lfl = "".join(f"<li><i>\"{e}\"</i><br>{a} {ch(o, r)} {z}</li>" for e, o, r, a, z in lf)
    fr = [("She is never boring.", ["after", "before"], "after", "the verb <i>be</i>"), ("He always leaves his clothes on the floor.", ["after", "before"], "before", "the main verb")]
    frl = "".join(f"<li><i>\"{e}\"</i> → the adverb goes {ch(o, r)} {z}.</li>" for e, o, r, z in fr)
    b.page(f"""{sec(3, "Language focus: describing character", "8 min")}
{sub("A", "Read the sentences from the conversation. Choose the correct option.", "5 min")}
<ol style="line-height:1.55;font-size:9pt;margin:0">{lfl}</ol>
{sub("B", "Adverbs of frequency. Choose.", "2 min")}
<ol style="line-height:1.6;font-size:9pt;margin:0">{frl}</ol>
{sub("C", "Make it softer. Rewrite with a bit or not very.", "1 min")}
<p style="margin:.5mm 0;line-height:1.8">He's rude. → {A("He's a bit rude. / He's not very polite.", "min-width:54mm")}<br>She's lazy. → {A("She's a bit lazy. / She's not very hard-working.", "min-width:54mm")}</p>
<div class="box sand"><h4>RULE</h4><b>adverbs of frequency</b>: after <i>be</i>, before the main verb · <b>can be</b> + adjective = sometimes true · <b>tend to</b> + infinitive = usually · <b>seem</b> = first impression · <b>softening</b>: <i>a bit</i> + negative adjective, <i>not very</i> + positive adjective, <i>…, though</i>. More on the next page: <b>Grammar reference</b>.</div>""",
    20, """<ol><li>A: ask for personal examples after each item: <i>Who do you know who can be a bit moody?</i></li>
<li>C: in American English, direct negative adjectives about a person (<i>He's lazy.</i>) can sound rude; softening is the norm at work.</li></ol>""")

    grammar_ref.describing_character(b)

    # Page 5 - Vocabulary lab
    px = [("honest", "dishonest"), ("sociable", "unsociable"), ("polite", "impolite"), ("tolerant", "intolerant"), ("kind", "unkind"), ("patient", "impatient"), ("responsible", "irresponsible"), ("reliable", "unreliable")]
    pxl = [f'<li value="{i+1}">{a} → {A(o, "min-width:22mm")}</li>' for i, (a, o) in enumerate(px)]
    op = [("kind", "mean"), ("relaxed", "tense"), ("shy", "confident"), ("tough", "soft"), ("cheerful", "miserable"), ("thoughtful", "selfish")]
    opl = " &nbsp;·&nbsp; ".join(f"<b>{a}</b> ↔ {A(o, 'min-width:15mm')}" for a, o in op)
    b.page(f"""{sec(4, "Vocabulary lab: opposites", "4 min")}
{sub("A", "Make the opposites with un-, im-, in-, dis- or ir-.", "2 min")}
<div style="font-size:8.8pt">{twocol(pxl, 4)}</div>
{sub("B", "Write the opposites from the box.", "2 min")}
<div class="bank">confident · mean · miserable · selfish · soft · tense</div>
<p style="margin:.3mm 0;line-height:1.9;font-size:8.8pt">{opl}</p>
<div class="box sand"><h4>WATCH OUT: FALSE FRIENDS AND WORD CHOICE</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>She's very sympathetic. (= nice)</td><td><b>She's very nice / friendly.</b></td><td><i>sympathetic</i> = shows understanding when you have a problem.</td></tr>
<tr><td>He's very sensible. He cries at movies.</td><td><b>He's very sensitive.</b></td><td><i>sensible</i> = practical, makes good decisions.</td></tr>
<tr><td>Your son is very educated. (= good manners)</td><td><b>Your son is very polite.</b></td><td><i>educated</i> = has studied a lot.</td></tr>
<tr><td>My boss was nervous with me. (= angry)</td><td><b>My boss was angry / mad at me.</b></td><td><i>nervous</i> = worried, anxious.</td></tr>
<tr><td>I'm boring. Nothing to do.</td><td><b>I'm bored.</b></td><td><i>boring</i> = makes others bored.</td></tr></table></div>
{sec(5, "Pronunciation lab: word stress", "4 min")}
<p class="small" style="margin:.3mm 0">In word families, the stress often moves: <b>GEN</b>erous → gene<b>ROS</b>ity · <b>SYM</b>pathy → sympa<b>THET</b>ic. Words ending in <i>-ity</i> and <i>-ic</i> are stressed just before the ending.</p>
{audiocard(["02.2"])}
{sub("A", "Listen and repeat. Then underline the stressed syllable.", "4 min", "02.2")}
<p style="margin:.3mm 0;line-height:1.7;font-size:8.8pt">{" &nbsp;·&nbsp; ".join(S022).replace(".", "") if not T else "<b>GEN</b>erous / gene<b>ROS</b>ity · <b>CU</b>rious / curi<b>OS</b>ity · <b>SYM</b>pathy / sympa<b>THET</b>ic · <b>CON</b>fident / <b>CON</b>fidence · em<b>BAR</b>rassed / em<b>BAR</b>rassment · <b>PES</b>simist / pessi<b>MIS</b>tic · <b>PUNC</b>tual / punctu<b>AL</b>ity · <b>AR</b>rogant / <b>AR</b>rogance"}</p>""",
    26, """<ol><li>A: <i>im-</i> before p (impolite, impatient), <i>ir-</i> before r (irresponsible), <i>in-</i> often before t (intolerant). Ask: <i>Do you know anyone unreliable?</i></li>
<li>False friends: check the student uses <i>nice</i> for a pleasant person, <i>sensitive</i> for emotions, <i>polite</i> for good manners and <i>angry / mad</i> for anger. Pronunciation: the stress in <i>-ment</i> and <i>-ce</i> nouns does not move.</li></ol>""")

    # Page 6 - Practice
    fe = [("angry", "anger"), ("generous", "generosity"), ("bored", "boredom"), ("embarrassed", "embarrassment"), ("sympathetic", "sympathy"), ("brave", "bravery"), ("jealous", "jealousy"), ("proud", "pride"), ("lazy", "laziness")]
    g = [A(n, "min-width:24mm") + f" ({a})" for a, n in fe]
    sh = [("a good teacher", "A good teacher should be patient and cheerful. They shouldn't be impatient."), ("a police officer", "A police officer should be honest and tough. They shouldn't be rude."),
          ("a manager", "A manager should be confident and fair. They shouldn't be arrogant."), ("a partner (husband or wife)", "A partner should be loyal and thoughtful. They shouldn't be selfish.")]
    shl = "".join(f"<li><b>{p}</b><br>{A(s, 'min-width:110mm') if T else '<div class=\"wline\"></div>'}</li>" for p, s in sh)
    b.page(f"""{sec(6, "Practice", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Kate writes a post for her bakery blog. Complete it with the nouns of the adjectives.", "4 min")}</div>{img('C', 30, 20)}</div>
<div class="box" style="line-height:1.85;font-size:9pt"><b>A week of feelings at Sweet Kate Bakery</b><br>What a week! On Monday, our oven broke and I couldn't hide my {g[0]}. On Tuesday, a regular customer brought me flowers for no reason. What {g[1]}! Wednesday was very slow, and by three o'clock {g[2]} set in. On Thursday, I dropped a whole wedding cake in front of the customers. The {g[3]}! But they showed real {g[4]} and helped me clean up. My dog Pepper chased a much bigger dog away from the door – that's {g[5]}! She's also full of {g[6]} when I pet other dogs. On Friday, my assistant decorated her first cake alone, and I felt so much {g[7]}. And Saturday? I planned to clean the kitchen, but {g[8]} won. See you next week!</div>
{sub("B", "What should these people be like? Write one sentence with should and one with shouldn't.", "4 min")}
<ol style="line-height:1.4;font-size:9pt;margin:0">{shl}</ol>""",
    22, """<ol><li>A: other nouns from this family: <i>happiness, kindness, honesty, patience, confidence</i>. Spelling: <i>lazy → laziness</i> (y → i).</li>
<li>B: answers are personal (red = possible answers). Discuss: <i>Do you agree? What about a politician?</i></li></ol>""")

    # Page 7 - Speaking
    fc = ["pride", "embarrassment", "jealousy", "anger", "happiness", "boredom"]
    b.page(f"""{sec(7, "Speaking: people and feelings", "12 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>describe a person</th><th>be polite</th><th>tell a story about a feeling</th><th>react</th></tr>
<tr><td><i>What's he like? · She's the kind of person who… · He comes across as…</i></td><td><i>She can be a bit… · He's not very… · To be fair, he's…</i></td><td><i>I'll never forget the time… · I felt so… · I was full of…</i></td><td><i>I know what you mean. · How embarrassing! · You must have been so proud!</i></td></tr></table></div>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("A", "Long turn. Choose a feeling. Prepare for one minute, then talk for two minutes about a time you or someone you know felt it.", "6 min")}
<p style="margin:.5mm 0;font-weight:700;color:#176074">{" · ".join(fc)}</p>
<ul style="line-height:1.45;font-size:8.9pt;margin:0"><li>when and where it happened, and who was there</li><li>what happened and why you felt that way</li><li>what you did, and how you feel about it now</li></ul></div>{img('D', 32, 24)}</div>
{sub("B", "Talking point. Discuss with your teacher.", "6 min")}
<ol style="line-height:1.5;font-size:8.9pt;margin:0"><li>What stereotypes have you heard about Brazilians? And about Americans?</li><li>Are they positive or negative? How true are they, in your experience?</li><li>Why do you think stereotypes exist? Can they be dangerous?</li></ol>""",
    28, """<ol><li>A: don't interrupt; note mistakes for the error log (page 8). Then ask follow-ups with the reactions in the box. Fluency option (3-2-1): the student tells the same story again in 2 minutes, then in 1 minute.</li>
<li>B: keep it respectful; encourage softening (<i>Some people think Brazilians tend to be…</i>) and <i>tend to</i> / <i>can be</i> for generalizations.</li></ol>""")

    # Page 8 - Wrap-up
    pc = ["I can describe people's personality with adjectives and their opposites.", "I can describe people politely with <i>a bit, not very, can be, tend to</i>.",
          "I can tell a story about a feeling with nouns like <i>pride</i> and <i>embarrassment</i>."]
    pcr = "".join(f"<tr><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for s in pc)
    b.page(f"""{sec(8, "Wrap-up and homework", "4 min")}
{sub("A", "Can-do check", "1 min")}
<table class="ck" style="font-size:8.6pt"><tr><th>In English…</th><th style="width:16mm">Easy!</th><th style="width:16mm">Sometimes</th><th style="width:16mm">Not yet</th></tr>{pcr}</table>
{sub("B", "My language notes. Write three corrections from today's class.", "2 min")}
<div style="display:flex;gap:5mm;font-size:8.6pt"><div style="flex:1"><b>I said…</b>{lines(3)}</div><div style="flex:1"><b>Better:</b>{lines(3)}</div></div>
{sub("C", "Homework: writing (100–150 words)", "1 min")}
<p style="margin:.3mm 0">Describe a person you admire: a friend, a family member or a coworker. Read Danny's model first.</p>
<div class="box" style="font-size:8.6pt;line-height:1.4;margin:.5mm 0"><i>The person I admire most is my mom, Rita. She manages a café in Chicago, and she's usually at work before six a.m. She's generous and patient with her staff, and she never forgets a customer's name. To be fair, she can be a bit stubborn: she tends to do everything herself! She seems tough, but deep down she's very sensitive. When I left for Brazil, she cried at the airport. I felt so much pride when she said she was proud of me.</i></div>
<p class="small" style="margin:.3mm 0">Checklist: ☐ who the person is &nbsp;☐ four personality adjectives &nbsp;☐ softening (<i>a bit, not very, can be, tends to</i>) &nbsp;☐ one example or story &nbsp;☐ one feeling noun &nbsp;☐ 100–150 words</p>
{lines(7)}""",
    30, """<ol><li>B (error log): during the lesson, note 3–5 real mistakes. Here, the student writes what they said and the better version; guide them to self-correct first.</li>
<li>C: when you correct, focus on adverb position, softening and the false friends from page 5.</li></ol>""")

    b.extra("Audio script", f"""
{sub("02.1", "Danny calls his mom (natural and slow)")}
<p style="line-height:1.4;font-size:9pt">{"<br>".join(f"<b>{n}:</b> {t}" if n != "Narrator" else f"<i>{t}</i>" for n, t in S021)}</p>
{sub("02.2", "Repeat: word stress in word families")}
<p>{" · ".join(S022)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 02 - Character and feelings")
