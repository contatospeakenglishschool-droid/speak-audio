# Speak! Bridge A2 - Unit 07 "Oh no!" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 07", audio_json="audio_a2-unit-07.json", img_dir="img")

PHOTOS = [("A", "break my arm", "arm in a cast"), ("B", "cut my finger", "bandaged finger"), ("C", "burn my hand", "hand and a hot iron"), ("D", "sprain my ankle", "ankle brace"),
          ("E", "break my leg", "leg in a cast"), ("F", "fall off my bike", "man on a bike"), ("G", "slip on the ice", "icy path"), ("H", "break a glass", "broken glass")]

_r = json.load(open("roteiro.json"))["units"]["a2-unit-07"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["07.1 Urgent care"].split("\n")]
S072 = [x.split(": ", 1)[1] for x in _r["07.2 Repeat sentences"].split("\n")]
S073 = [x.split(": ", 1)[1] for x in _r["07.3 Repeat participles"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 07", "Oh no!", "Accidents and injuries · <b>present perfect with just</b>",
                       [("YOU CAN", "talk about accidents that just happened and explain them to a doctor"),
                        ("LANGUAGE", "What's happened? · I've just slipped on the ice. · You haven't broken it."),
                        ("PRONUNCIATION", "I've · she's (= she has) · slipped /t/ · burned /d/")])
    b.page(f"""{sec(1, "Warm-up: accidents and injuries", "8 min")}
{sub("A", "Look at the photos. Write the phrases under the photos.", "3 min")}
<div class="bank">break a glass · break my arm · break my leg · burn my hand · cut my finger · fall off my bike · slip on the ice · sprain my ankle</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Answer the questions.", "5 min")}
<ol><li>Which phrases are accidents (what happened)? Which are injuries (what happened to your body)? {R("accidents: fall off my bike, slip on the ice, break a glass · injuries: the others")}</li>
<li>Have you had any of these accidents or injuries? Did you go to the hospital?</li></ol>""",
    22, """<ol><li>A: <b>sprain</b> rhymes with <i>train</i> /eɪ/. <i>Fall off</i> a bike / a horse; <i>slip on</i> the ice / a wet floor; <i>trip over</i> something.</li>
<li>B: accept the past simple (<i>I broke my arm in 2015</i>). Don't correct yet: the present perfect comes on page 3.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Accidents and injuries</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Three dialogues at an urgent care center in Chicago</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Present perfect: form · just · present result</td><td>3</td></tr>
<tr><td>4 Pronunciation lab</td><td>5 min</td><td>Contractions · past participles</td><td>4</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Have / has + past participle · Word builder: treatments</td><td>5</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Mime it! · doctor and patient role-play</td><td>6</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check · irregular verbs · homework (50–75 words)</td><td>7</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>A bad day in Chicago. At an urgent care center, the doctor (one-off voice, Studio-O) sees three patients: <b>Tom</b> slipped on the ice on his way to school and sprained his ankle; <b>Lucy</b> fell off her bike when a car door opened in front of her (she was wearing a helmet!) and broke her arm; and <b>Kate and Rita</b> had an accident in Kate's bakery: Kate burned her hand and Rita cut her finger. In the US, people go to <b>urgent care</b> for injuries that are not life-threatening and to the <b>ER</b> (emergency room) for emergencies; the emergency number is 911.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Portuguese uses a different structure for recent events, so students say <i>I just slip</i> ✗ or <i>I have just slipped yesterday</i> ✗. Teach <b>I've just slipped</b> (recent, no time) vs <b>I slipped an hour ago</b> (past simple + time). Watch participles: <i>He's cutted</i> ✗ → <b>cut</b>; <i>I haven't broke</i> ✗ → <b>broken</b>; <i>What have you did?</i> ✗ → <b>done</b>. Note: Americans often use the past simple with <i>just</i> (<i>I just slipped</i>); both are correct.</div>
<div class="box"><h4>AUDIO</h4>Track 07.1 Three dialogues (slow and natural) · Track 07.2 Sentences · Track 07.3 Past participles</div>""")

    # Page 2
    tf = [("Tom slipped on the ice.", "T"), ("Tom has broken his foot.", "F: he's sprained his ankle."), ("Lucy has had a car accident.", "F: she's fallen off her bike."),
          ("Lucy has broken her arm.", "T"), ("The accident happened in a kitchen.", "T: in the kitchen of Kate's bakery."), ("Only one person is hurt.", "F: two people (Kate and Rita).")]
    tfl = [f'<li value="{i+1}">{s} <b>T / F</b> {R(a)}</li>' for i, (s, a) in enumerate(tf)]
    cw = [(["recently", "just", "now"], "just", "I've", "slipped on the ice."), (["break", "breaking", "broken"], "broken", "Have I", "it?"),
          (["done", "did", "doing"], "done", "What have you", "to yourself?"), (["felt", "fallen", "falling"], "fallen", "I've just", "off my bike."),
          (["have", "had", "having"], "had", "We've", "a bit of an accident."), (["weren't", "aren't", "haven't been"], "haven't been", "You", "very lucky today.")]
    cwl = [f'<li value="{i+1}">{a} {ch(o, r)} {c}</li>' for i, (o, r, a, c) in enumerate(cw)]
    b.page(f"""{sec(2, "Listening: a bad day in Chicago", "10 min")}
<p>It's a cold winter day in Chicago. At an urgent care center, a doctor sees three patients you know.</p>
{audiocard(["07.1 · SLOW", "07.1 · NATURAL"])}
{sub("A", "Listen. True (T) or false (F)? Correct the false sentences.", "4 min", "07.1 · SLOW")}
{twocol(tfl, 4)}
{sub("B", "Listen again. Circle the word you hear.", "4 min", "07.1 · NATURAL")}
{twocol(cwl, 4)}
{sub("C", "Who was the luckiest? Who was the unluckiest? Why?", "2 min")}""",
    22, """<p>A: explain <b>urgent care</b> (a clinic for injuries that are not emergencies; the ER is for emergencies). Stop after each dialogue and ask <i>Who is it? What's happened?</i> B: the student guesses first. Lucy was lucky: she was wearing a helmet. If there's time, read one dialogue together from the script (TB last page).</p>""")

    # Page 3
    b.page(f"""{sec(3, "Language focus: present perfect with just", "10 min")}
{sub("A", "Read the sentences from the dialogues. Then choose the correct option.", "3 min")}
<div class="bank" style="background:#fff;font-weight:600">What's happened to you? · I've just slipped on the ice. · You've sprained your ankle. · You haven't broken your foot. · Have I broken it?</div>
<ol><li>These sentences talk about something that happened in {ch(["the past", "the future"], "the past")}, but the result is important {ch(["now", "tomorrow"], "now")}.</li>
<li>We make the present perfect with {ch(["do / does", "have / has", "was / were"], "have / has")} + the past participle.</li>
<li><i>Just</i> means a {ch(["short", "long"], "short")} time ago. It goes before the {ch(["main verb", "have / has"], "main verb")}.</li>
<li>When we say <b>when</b> it happened (<i>an hour ago</i>), we use the {ch(["present perfect", "past simple"], "past simple")}.</li></ol>
{sub("B", "Complete the table.", "4 min")}
<table style="table-layout:fixed;margin-top:0;font-size:9pt"><tr><th style="width:26mm"></th><th>I / you / we / they</th><th>he / she / it</th></tr>
<tr><td><b>positive</b></td><td>I{A("'ve", "min-width:9mm")} just cut my finger.</td><td>She{A("'s", "min-width:9mm")} burned her hand.</td></tr>
<tr><td><b>negative</b></td><td>You {A("haven't", "min-width:14mm")} broken it.</td><td>He {A("hasn't", "min-width:14mm")} hurt his head.</td></tr>
<tr><td><b>question</b></td><td>{A("Have", "min-width:11mm")} I broken it?</td><td>{A("Has", "min-width:11mm")} she cut her finger?</td></tr>
<tr><td><b>short answer</b></td><td>Yes, you have. / No, you {A("haven't", "min-width:14mm")}.</td><td>Yes, she {A("has", "min-width:10mm")}. / No, she hasn't.</td></tr>
<tr><td><b>wh- question</b></td><td colspan="2">What {A("have", "min-width:10mm")} you done? · What's happened? (= What <b>has</b> happened?)</td></tr></table>
{sub("C", "Past participles. Regular verbs end in -ed. Write the irregular ones.", "3 min")}
<table style="table-layout:fixed;margin-top:0;font-size:9pt"><tr>{"".join(f"<td style='text-align:center'>{v} → {A(p, 'min-width:12mm')}</td>" for v, p in (("break", "broken"), ("fall", "fallen"), ("cut", "cut"), ("hurt", "hurt"), ("do", "done"), ("be", "been")))}</tr></table>
<div class="box sand"><h4>RULE</h4>Present perfect = a past action + a result <b>now</b>: <i>I've just cut my finger</i> (it's bleeding now). With a finished time, use the past simple: <i>I cut my finger <b>this morning</b> / <b>an hour ago</b></i>.</div>""",
    24, """<ol><li>A: draw a timeline: past action → result now. <i>'s</i> can be <i>is</i> or <i>has</i>: <i>She's burned</i> = she <b>has</b> burned (followed by a participle).</li>
<li>C: <i>burn</i> → <i>burned</i> in American English (<i>burnt</i> is British). The full irregular verb list is on page 7.</li></ol>""")

    # Page 4
    b.page(f"""{sub("D", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>He's cutted his hand.</td><td><b>He's cut his hand.</b></td><td>cut – cut – cut.</td></tr>
<tr><td>I just have hit my head.</td><td><b>I've just hit my head.</b></td><td>just after have.</td></tr>
<tr><td>I haven't broke my leg.</td><td><b>I haven't broken my leg.</b></td><td>past participle.</td></tr>
<tr><td>Have sprained you your ankle?</td><td><b>Have you sprained your ankle?</b></td><td>have + subject + participle.</td></tr>
<tr><td>What have you did?</td><td><b>What have you done?</b></td><td>do – did – done.</td></tr>
<tr><td>I've broken my arm last year.</td><td><b>I broke my arm last year.</b></td><td>finished time = past simple.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "5 min")}
{audiocard(["07.2", "07.3"])}
{sub("A", "Contractions. Listen and repeat.", "2 min", "07.2")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S072)}</div>
{sub("B", "Past participles. Listen and repeat. Which -ed endings sound like /t/? Which sound like /d/?", "2 min", "07.3")}
<table style="table-layout:fixed;margin-top:0"><tr>{"".join(f"<td style='text-align:center'><b>{w}</b></td>" for w in S073)}</tr></table>
<p class="small">{R("/t/: slipped, tripped · /d/: burned, spilled · no -ed: broken, fallen, cut, hurt")}</p>
<div class="box" style="margin-top:1mm"><h4>SHORT AND LINKED</h4>Use contractions: <b>I've</b> /aɪv/, <b>she's</b>, <b>haven't</b>. Don't add a vowel to -ed: <i>slipped</i> = one syllable /slɪpt/, not "slip-ed".</div>""",
    24, """<ol><li>4A: Brazilians often drop the <i>'ve</i>: <i>I just cut</i>. Make them hear and say the /v/: <i>I've_just</i>.</li>
<li>4B: <i>hurt</i> /hɜrt/ vs <i>heart</i> /hɑrt/; <i>burned</i> /bɜrnd/.</li></ol>""")

    # Page 5
    gp = [("She", "'s broken", "the window. (break)"), ("Sorry about the smoke. We", "'ve burned", "the toast. (burn)"), ("Ouch! I", "'ve just cut", "my finger. (just / cut)"),
          ("", "Has he fallen", "off his bike? (he / fall)"), ("They're hungry because they", "haven't had", "lunch. (not have)"), ("Oh no! Someone", "has spilled", "coffee on my laptop! (spill)"),
          ("Ana", "has just finished", "a twelve-hour shift at the hospital. (just / finish)"), ("Don't worry. You", "haven't broken", "your foot. (not break)")]
    gpl = [f'<li value="{i+1}">{a} {A(v, "min-width:26mm")} {c}</li>' for i, (a, v, c) in enumerate(gp)]
    tr = [("a bandage", "a sprained ankle"), ("a Band-Aid", "a small cut"), ("a cast", "a broken arm or leg"), ("an ice pack", "a hit on the head, a sprain"),
          ("cream", "a small burn"), ("painkillers", "a headache or pain")]
    trl = "".join(f"<tr><td>{A(t, 'min-width:24mm')}</td><td>{u}</td></tr>" for t, u in tr)
    b.page(f"""{sec(5, "Practice", "8 min")}
{sub("A", "Complete with have / has + past participle. Use contractions when you can.", "4 min")}
{twocol(gpl, 5)}
{sub("B", "Word builder: treatments. Which treatment is best for each injury? Complete with the words.", "4 min")}
<div class="bank">a Band-Aid · a bandage · a cast · an ice pack · cream · painkillers</div>
<table style="table-layout:fixed;margin-top:0;font-size:9pt;width:80%"><tr><th>treatment</th><th>for…</th></tr>{trl}</table>
<p class="small">Which of these do you have at home? Where do you buy them in Brazil?</p>""",
    22, """<ol><li>A: point out <i>haven't had</i> (have twice: auxiliary + main verb) and <i>Has he fallen…?</i> (question order).</li>
<li>B: <b>Band-Aid</b> is a brand name used as a common word in the US (British: <i>plaster</i>). Accept reasonable alternatives.</li></ol>""")

    # Page 6
    acc = ["slip on a banana peel", "fall off a horse", "trip over a cat", "spill hot coffee", "fall in the shower", "break a glass"]
    inj = ["break your arm", "cut your knee", "hit your head", "sprain your wrist", "burn your hand", "hurt your back"]
    b.page(f"""{sec(6, "Speaking", "12 min")}
{sub("A", "Mime it! Choose an accident and an injury. Act them out without words. Your teacher guesses: “You've just… and you've…!” Then change roles.", "6 min")}
<table style="table-layout:fixed;margin-top:0"><tr><th>accidents</th><th>injuries</th></tr>
{"".join(f"<tr><td>{a}</td><td>{i}</td></tr>" for a, i in zip(acc, inj))}</table>
<div class="msg" style="max-width:none;padding:1.5mm 4mm"><b>Teacher:</b> You've just slipped on a banana peel… and you've hurt your back! <b>You:</b> Yes!</div>
{sub("B", "Role-play: at urgent care. You are the patient; your teacher is the doctor. Then change roles.", "6 min")}
<div class="two"><div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.8pt"><b>Patient</b><br>• Choose an accident from A.<br>• Explain what's happened and when.<br>• Ask: <i>Have I broken it? What should I do?</i></div>
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.8pt"><b>Doctor</b><br>• Start: <i>What's happened to you? / What have you done to yourself?</i><br>• Check: <i>Can I touch it? Does it hurt?</i><br>• Give a treatment from page 5.</div></div>""",
    26, """<ol><li>A: if mime is difficult online, the student can describe the scene in simple words: <i>I'm in the kitchen… Oops!</i></li>
<li>B: check the contrast: <i>I've just fallen</i> (no time) vs <i>It happened an hour ago</i> (past simple).</li></ol>""")

    # Page 7
    pc = [("A2 Unit 03", "I can describe a place with my senses and use state verbs correctly."), ("A2 Unit 04", "I can use adjectives and nouns with the right preposition."),
          ("A2 Unit 05", "I can ask about words in class and name parts of speech."), ("A2 Unit 06", "I can praise, compliment and congratulate people, and respond politely."),
          ("A2 Unit 07", "I can talk about accidents that just happened with the present perfect.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    iv = [("be", "was / were", "been"), ("break", "broke", "broken"), ("burn", "burned", "burned"), ("cut", "cut", "cut"), ("do", "did", "done"), ("fall", "fell", "fallen"),
          ("get", "got", "gotten"), ("go", "went", "gone"), ("have", "had", "had"), ("hit", "hit", "hit"), ("hurt", "hurt", "hurt"), ("make", "made", "made"),
          ("see", "saw", "seen"), ("take", "took", "taken")]
    half = (len(iv) + 1) // 2
    def ivt(rows):
        return "<table style='table-layout:fixed;margin-top:0;font-size:8.6pt'><tr><th>verb</th><th>past</th><th>participle</th></tr>" + "".join(
            f"<tr><td>{v}</td><td>{p}</td><td>{A(pp, 'min-width:14mm') if k % 3 == 1 else pp}</td></tr>" for k, (v, p, pp) in enumerate(rows)) + "</table>"
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Irregular verbs. Complete the missing participles and study the list.</b></p>
<div class="two"><div>{ivt(iv[:half])}</div><div>{ivt(iv[half:])}</div></div>
<p style="margin-top:1.5mm"><b>2. A message (50–75 words).</b> You've just had a small accident. Write a message to a friend: say what has happened (present perfect) and give the details: when, where, how (past simple).</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class: start with a quick verb quiz (you say the verb, the student says the past and the participle). Check the message: present perfect for the news, past simple for the details.</p>""")

    b.extra("Audio scripts", f"""
{sub("07.1", "Three dialogues at urgent care (slow and natural)")}
<p style="line-height:1.42">{"<br>".join(f"<b>{n}:</b> {t}" if n != "Narrator" else f"<i>{t}</i>" for n, t in SCRIPT)}</p>
{sub("07.2", "Sentences")}
<p>{" ".join(S072)}</p>
{sub("07.3", "Past participles")}
<p>{" · ".join(S073)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 07 - Oh no")
