# Speak! Bridge A2 - Review 4 (Units 31-39), all English - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
_se.SERIES = "Bridge"
setup(band="A2 · REVIEW 4", audio_json="audio_a2-review-4.json", img_dir="img")

PHOTOS = [("A", "cooking", "Unit 31"), ("B", "the northern lights", "Unit 32"), ("C", "a self-driving car", "Unit 33"), ("D", "a riding lesson", "Unit 34"),
          ("E", "hiking boots", "Unit 35"), ("F", "yoga", "Unit 37"), ("G", "a riverboat", "Unit 38"), ("H", "chocolate milk", "Unit 39")]

_r = json.load(open("roteiro.json"))["units"]["a2-review-4"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["R4.1 Ana's online class"].split("\n")]
S42 = [x.split(": ", 1)[1] for x in _r["R4.2 Sounds: s, z or iz?"].split("\n")][1:]
S43 = [tuple(x.split(": ", 1)) for x in _r["R4.3 Dialogues"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LEVEL A2 · REVIEW 4", "Review 4", "Units 31–39 · the future · suggestions · emails · -ing forms · articles · nouns",
                       [("YOU CAN", "check what you learned in Units 31–39 and plan what to practice"),
                        ("LANGUAGE", "I'm meeting… · It's going to… · I think you'll… · Let's… · I enjoy running. · the oldest · Marcos's laptop"),
                        ("PRONUNCIATION", "-s and 's: /s/, /z/ or /ɪz/")])
    b.page(f"""{sec(1, "Warm-up: photo memory", "5 min")}
{sub("A", "One photo from each unit. Write the word or phrase. Then say one sentence about it with the grammar of that unit.", "5 min")}
<div class="bank">chocolate milk · cooking · hiking boots · the northern lights · a riding lesson · a riverboat · a self-driving car · yoga</div>
{photo_grid(T, PHOTOS)}
<p class="small" style="margin-top:2mm"><b>Example:</b> cooking → <i>In this photo, a man and a woman are cooking in a kitchen.</i></p>""",
    25, """<p>Photos A–H come from Units 31–39 in order (Unit 36, work emails, is on page 5). Push each unit's grammar: describing a photo (31), plans and timetables (32), predictions (33), going to / will / present continuous (34), suggestions (35), gerunds (37), articles (38), noun + noun (39).</p>""", cover=cover)

    b.extra("Review overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Units</th><th>SB page</th></tr>
<tr><td>1 Warm-up: photo memory</td><td>5 min</td><td>31–39</td><td>1</td></tr>
<tr><td>2 Listening: Ana's online class</td><td>10 min</td><td>31–39</td><td>2</td></tr>
<tr><td>3 Grammar: the future, predictions, suggestions</td><td>9 min</td><td>32, 33, 34, 35</td><td>3</td></tr>
<tr><td>4 Grammar: -ing forms, articles, noun phrases</td><td>9 min</td><td>37, 38, 39</td><td>4</td></tr>
<tr><td>5 Vocabulary and a work email</td><td>8 min</td><td>31–39</td><td>5</td></tr>
<tr><td>6 Pronunciation and social English</td><td>9 min</td><td>35–39</td><td>6</td></tr>
<tr><td>7 Reflect and homework</td><td>5 min</td><td>31–39</td><td>7</td></tr></table>
<div class="box"><h4>HOW THIS GUIDE WORKS</h4>Every page looks like the Student Book page with the same number. Your notes are in the <b>yellow box</b>; <span class="red">answers in red</span> are not in the Student Book. This is a review: don't teach everything again. Let the student work, then focus on the mistakes that come back. The grammar reference pages (page 4) of Units 31–39 are useful here.</div>
<div class="box sand"><h4>THE STORY SO FAR</h4>Monday evening: Ana (Neural2-F) has her online class with Tom (Neural2-D). She describes Paulo's photo from the Alaska trip with Carol and Maya (Unit 32), says she's taking the TOEIC test (Units 31 and 34), and they plan an extra class (Unit 35) that she'll confirm by email (Unit 36). Tom tells her about Lucy's gap year (Unit 34), Priya's podcast (Unit 37) and Paulo's article on Hannibal (Unit 38); Ana mentions her favorite family photo with Marcos's coffee cup (Unit 39). Dialogues: Priya (Chirp3-HD-Kore) and Tom plan a beach day (Unit 35); Maya (Studio-O) and Paulo (Neural2-I) talk about Linda's visit (Unit 36). No new facts.</div>
<div class="box"><h4>THE TOP 5 MISTAKES TO WATCH</h4>1. <i>I will meet Tom tomorrow at six</i> (arranged) → <b>I'm meeting Tom</b>. 2. <i>Let's to go / How about go?</i> → <b>Let's go / How about going?</b> 3. <i>I enjoy to run / Thanks for help me</i> → <b>I enjoy running / Thanks for helping me</b>. 4. <i>The life is short / She is doctor</i> → <b>Life is short / She's a doctor</b>. 5. <i>the laptop of Marcos</i> → <b>Marcos's laptop</b>.</div>
<div class="box"><h4>AUDIO</h4>Track R4.1 Ana's online class (slow and natural) · Track R4.2 Sounds: s, z or iz? · Track R4.3 Two dialogues</div>""")

    # Page 2
    topics = [("a photo from Alaska", True), ("an English test", True), ("an extra class", True), ("a new job", False), ("a gap year", True), ("a podcast", True), ("a travel article", True), ("a family photo", True)]
    tl = " &nbsp; ".join(f"☐ {t}{(' ' + R('✓')) if ok else ''}" for t, ok in topics)
    tf = [("In Paulo's photo, the northern lights are behind a mountain.", "F: they're above them, next to a lake."), ("Ana's test is on a Saturday morning.", "T: at nine o'clock"),
          ("Ana is sure she won't be nervous.", "F: she might be a little nervous."), ("Tom suggests an extra class on Friday.", "F: on Thursday"),
          ("Lucy is starting at the animal shelter next week.", "T"), ("Ana is thinking about starting a running group.", "T: at the hospital")]
    tfl = [f'<li value="{i+1}">{s} <b>T / F</b> {R(a)}</li>' for i, (s, a) in enumerate(tf)]
    find = [("describing a photo: there are + place (Unit 31)", "Above them, there are green northern lights."), ("an arrangement with the present continuous (Unit 32)", "I'm taking the TOEIC test next month. / She's starting… next week."),
            ("a timetable with the present simple (Unit 32)", "The test starts at nine o'clock."), ("a prediction with will or might (Unit 33)", "I'm sure you'll do really well. / I might be a little nervous."),
            ("a plan with going to (Unit 34)", "I'm going to practice every day."), ("a suggestion and an offer (Unit 35)", "Why don't we…? / How about planning…? / Let's do it! / I'll send you an email."),
            ("a gerund (Unit 37)", "she enjoys running / I love listening / thinking about starting / changing"), ("the with a river (Unit 38)", "the Mississippi / the river"),
            ("'s for a person (Unit 39)", "Paulo's article / my father's birthday / Marcos's coffee cup")]
    fl = "".join(f"<li>{x} {R(y)}</li>" for x, y in find)
    b.page(f"""{sec(2, "Listening: Ana's online class", "10 min")}
<p>It's Monday evening in São Paulo. Ana is having her online English class with Tom, and they catch up on the news.</p>
{audiocard(["R4.1 · SLOW", "R4.1 · NATURAL"])}
{sub("A", "Listen. What do they talk about? Check (✓) seven topics. One topic is extra.", "2 min", "R4.1 · SLOW")}
<p style="font-weight:600">{tl}</p>
{sub("B", "Listen again. True (T) or false (F)? Correct the false sentences.", "4 min", "R4.1 · NATURAL")}
{twocol(tfl, 4)}
{sub("C", "Find one example in the conversation of each form.", "4 min")}
<ol style="font-size:8.8pt;line-height:1.35">{fl}</ol>""",
    22, """<p>A: the extra topic is <i>a new job</i>. C: let the student read the script (TB last page) or play the natural version again and pause. Finish with the task Tom gives Ana: the student describes the photo on page 1 (A) for about a minute.</p>""")

    # Page 3
    ff = [(["I'm meeting", "I'll meet"], "I'm meeting", "", "Tom at six tomorrow. It's in my calendar."), (["leaves", "is leaving"], "leaves", "Hurry! The train", "at 8:15."),
          (["It's going to", "It will"], "It's going to", "Look at those clouds!", "rain."), (["I'm going to", "I'll"], "I'll", "The phone's ringing.", "get it!"),
          (["are you going to", "will you"], "are you going to", "What", "do in your gap year? Have you decided?"), (["you'll love", "you're loving"], "you'll love", "I think", "Alaska.")]
    ffl = [f'<li value="{i+1}">{(a + " ") if a else ""}{ch(o, r)} {e}</li>' for i, (o, r, a, e) in enumerate(ff)]
    pr = [("It will definitely rain tomorrow. (100% sure)", "✓"), ("I might to go to the party.", "I might go"), ("She probably will be late.", "She'll probably be late."), ("He won't definitely come.", "He definitely won't come.")]
    prl = "".join(f"<li>{a} {A(c, 'min-width:36mm')}</li>" for a, c in pr)
    sg = [("Let's", "go", "to the beach on Sunday. (go)"), ("How about", "taking", "the train? (take)"), ("Why don't we", "bring", "our own drinks? (bring)"), ("You look tired. I", "'ll carry", "your bag. (carry, an offer)")]
    sgl = "".join(f"<li>{a} {A(v, 'min-width:18mm')}{'' if e[0] == ' ' else ' '}{e}</li>" for a, v, e in sg)
    b.page(f"""{sec(3, "Grammar: the future, predictions, suggestions", "9 min")}
{sub("A", "Units 32 and 34. Choose the correct future form.", "3 min")}
<div style="font-size:9pt">{twocol(ffl, 4)}</div>
{sub("B", "Unit 33. Correct the mistakes. If a sentence is correct, write ✓.", "3 min")}
<ol style="line-height:1.6">{prl}</ol>
{sub("C", "Unit 35. Complete the suggestions and the offer.", "3 min")}
<ol style="line-height:1.7">{sgl}</ol>
<div class="box sand"><h4>REMEMBER</h4><b>arrangement</b> → present continuous · <b>timetable</b> → present simple · <b>plan</b> or <b>evidence</b> → going to · <b>opinion</b>, <b>offer</b>, decision now → will · <b>might</b> + base form · <b>probably / definitely</b> after <i>will</i>, before <i>won't</i> · <b>Let's / Why don't we</b> + base form · <b>How about</b> + verb-ing.</div>""",
    22, """<ol><li>A: ask for the reason each time: <i>Is it arranged? Is it a timetable? Do you have evidence? Did you decide now?</i></li>
<li>B: 1 is correct. C: ask the student to answer each suggestion: <i>Good idea! / I'm not sure. How about…?</i></li></ol>""")

    # Page 4
    gd = [(["Swimming", "To swim"], "Swimming", "", "is good for your heart."), (["going", "to go"], "going", "I always avoid", "to the gym."),
          (["helping", "help"], "helping", "Thanks for", "me!"), (["seeing", "see"], "seeing", "I'm looking forward to", "you.")]
    gdl = [f'<li value="{i+1}">{(a + " ") if a else ""}{ch(o, r)} {e}</li>' for i, (o, r, a, e) in enumerate(gd)]
    ar = [(["The life", "Life"], "Life", "", "is short."), (["a", "—"], "a", "My sister is", "nurse."), (["the", "—"], "the", "Hannibal is on", "Mississippi."), (["the", "—"], "—", "I live in", "Brazil.")]
    arl = [f'<li value="{i+1}">{(a + " ") if a else ""}{ch(o, r)} {e}</li>' for i, (o, r, a, e) in enumerate(ar)]
    np_ = [("the laptop of Marcos", "Marcos's laptop"), ("the door of the kitchen", "the kitchen door"), ("the house's roof", "the roof of the house"), ("a shoes store", "a shoe store")]
    npl = "".join(f"<li>{a} → {A(c, 'min-width:34mm')}</li>" for a, c in np_)
    b.page(f"""{sec(4, "Grammar: -ing forms, articles, noun phrases", "9 min")}
<div class="two"><div>{sub("A", "Unit 37. Choose the correct form.", "2 min")}
<ol style="line-height:1.6;margin:0">{"".join(gdl)}</ol></div>
<div>{sub("B", "Unit 38. Choose the correct article (— = no article).", "2 min")}
<ol style="line-height:1.6;margin:0">{"".join(arl)}</ol></div></div>
{sub("C", "Unit 39. Write the phrases in a better way.", "3 min")}
<ol style="line-height:1.7;column-count:2;column-gap:6mm">{npl}</ol>
{sub("D", "Units 37–39. Complete with your own ideas. Then tell your teacher.", "2 min")}
<ol style="line-height:1.9"><li>I really enjoy ______________________ on weekends.</li><li>The best place in my city is ______________________.</li><li>My favorite thing in my kitchen is ______________________.</li></ol>
<div class="box sand"><h4>REMEMBER</h4><b>gerund</b> as subject, after prepositions and after <i>enjoy, avoid, miss, keep, look forward to</i> · <b>a/an</b> = one of many, jobs · <b>the</b> = we know which, rivers, superlatives · <b>no article</b> = in general, names, most countries · <b>noun + noun</b> for everyday things · <b>'s</b> for people · <b>of</b> for things.</div>""",
    22, """<ol><li>A–C: insist on the rule each time. In D, listen for gerunds (<i>enjoy cooking</i>), articles (<i>the best place</i>) and noun + noun (<i>my coffee machine</i>).</li>
<li>If articles are still difficult, do a quick extra round: describe the room you're in with a/an and the.</li></ol>""")

    # Page 5
    vc = [("a written test of English that many companies ask for", "the TOEIC"), ("colored lights in the night sky near the North Pole", "the northern lights"),
          ("a car that drives without a person in control", "a self-driving car"), ("a year off before or during college", "a gap year"),
          ("the line where you write what an email is about", "the subject line"), ("the general feeling of being healthy and happy", "well-being"),
          ("an enjoyable trip on a boat", "a cruise"), ("a frame for a photo on the wall", "a picture frame")]
    em = [("Kind regards, Ana", "6"), ("Hi Paulo,", "1"), ("Please let me know if Thursday works for you.", "4"), ("Thanks for your email.", "2"),
          ("I'm writing to suggest an extra class before my test.", "3"), ("I look forward to hearing from you.", "5")]
    eml = "".join(f"<li style='list-style:none'>{A(n, 'min-width:6mm;text-align:center')} {t}</li>" for t, n in em)
    b.page(f"""{sec(5, "Vocabulary and a work email", "8 min")}
{sub("A", "Units 31–39. Write the word or phrase.", "4 min")}
<div class="bank">a cruise · a gap year · the northern lights · a picture frame · a self-driving car · the subject line · the TOEIC · well-being</div>
{twocol([f'<li value="{i+1}">{d} → {A(w, "min-width:22mm")}</li>' for i, (d, w) in enumerate(vc)], 5)}
{sub("B", "Unit 36. Ana writes to Tom. Put the six parts of her email in order (1–6).", "4 min")}
<ul style="line-height:1.6;padding-left:2mm;margin:0">{eml.replace('Hi Paulo,', 'Hi Tom,')}</ul>
<p class="small" style="margin:.5mm 0">Which part is the greeting? the opening? the reason for writing? the call to action? the closing? the signing?</p>""",
    28, """<ol><li>A: after each word, ask a personal question: <i>Would you like to see the northern lights? Have you ever been on a cruise?</i></li>
<li>B: Hi Tom, (greeting) · Thanks for your email. (opening) · I'm writing to suggest… (reason) · Please let me know… (call to action) · I look forward to hearing from you. (closing) · Kind regards, Ana (signing).</li></ol>""")

    # Page 6
    snd = {"/s/": "Rita's, starts, cups", "/z/": "plans, Paulo's, enjoys", "/ɪz/": "boxes, finishes, the boss's"}
    stt = "".join(f"<td style='height:14mm;vertical-align:top'><b>{k}</b><br>{R(v)}</td>" for k, v in snd.items())
    d1 = [("Priya", "The forecast says <u>it will be</u> sunny on Sunday. <u>Let's to go</u> to the beach!"), ("Tom", "Good idea. <u>Why we don't take</u> our bikes?"),
          ("Priya", "OK. And how about <u>have</u> lunch at the beach?"), ("Tom", "Sure. <u>I make</u> some sandwiches."), ("Priya", "Great! I think <u>we're having</u> a lovely day.")]
    d2 = [("Maya", "Did you email Linda Brooks about the parking?"), ("Paulo", "Yes. I wrote, \"<u>Dear Ms. Linda</u>, <u>I write to inform about</u> the parking.\""),
          ("Maya", "Great. Did you <u>finish to check</u> the train times?"), ("Paulo", "Yes. And I'm really looking forward to <u>meet</u> her."), ("Maya", "Me too. Thanks for <u>help</u> me with the meeting.")]
    def dlg(lines):
        return "<br>".join(f"<b>{n}:</b> {t}" for n, t in lines)
    b.page(f"""{sec(6, "Pronunciation and social English", "9 min")}
{audiocard(["R4.2", "R4.3"])}
{sub("A", "Units 37 and 39. Listen to the words. Write each word in the correct column.", "3 min", "R4.2")}
<div class="bank">boxes · cups · enjoys · finishes · Paulo's · plans · Rita's · starts · the boss's</div>
<table style="table-layout:fixed;margin-top:0"><tr>{stt}</tr></table>
{sub("B", "Units 34–37. Each dialogue has mistakes (underlined). Correct them. Then listen and check.", "4 min", "R4.3")}
<div class="two"><div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.8pt;line-height:1.5"><b>Dialogue 1</b><br>{dlg(d1)}</div>
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.8pt;line-height:1.5"><b>Dialogue 2</b><br>{dlg(d2)}</div></div>
<p class="small">{R("1: it's going to be · Let's go · Why don't we take · how about having · I'll make · we'll have — 2: Dear Ms. Brooks · I'm writing to let you know about · finish checking · meeting · helping")}</p>
{sub("C", "Role-play the dialogues with your teacher. Then plan a real weekend together with suggestions and offers.", "2 min")}""",
    34, """<ol><li>A: 3-second pause after each word. The rule is the same for plurals, third person -s and possessive 's: /ɪz/ after /s, z, ʃ, tʃ, dʒ/; /s/ after /p, t, k, f/; /z/ after other sounds.</li>
<li>B: Dialogue 1: <i>it will be sunny</i> isn't wrong, but with a forecast (evidence) <i>going to</i> is more natural (Unit 34).</li></ol>""")

    # Page 7
    ck = [("31", "I can describe a photo for about a minute."), ("32", "I can talk about timetables and personal plans for the future."),
          ("33", "I can make predictions and say how sure I am."), ("34", "I can choose the right future form: going to, will or the present continuous."),
          ("35", "I can make suggestions and offers when I plan a day out."), ("36", "I can write a clear, polite work email."),
          ("37", "I can use -ing forms after verbs like enjoy and avoid, and as subjects."), ("38", "I can use a/an, the and no article correctly."),
          ("39", "I can put nouns together: a coffee cup, Leo's ideas, the end of the story.")]
    ckr = "".join(f"<tr><td><b>Unit {u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in ck)
    b.page(f"""{sec(7, "Reflect and homework", "5 min")}
{sub("A", "How are you doing? Check one box for each line.", "2 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{ckr}</table>
{sub("B", "My goals. What do you want to practice more? Write two things.", "2 min")}
<div class="wline"></div><div class="wline"></div>
{sub("C", "Homework", "1 min")}
<p><b>An email to a friend: "Plans for next weekend" (80–100 words).</b> Use the six parts of an email (Unit 36). Include:</p>
<ol><li>one arrangement and one plan (<i>I'm meeting… / I'm going to…</i>) (Units 32, 34);</li><li>one prediction (<i>I think it'll… / It might…</i>) (Unit 33);</li>
<li>two suggestions (<i>Let's… / How about…?</i>) (Unit 35);</li><li>one gerund and one noun + noun phrase (<i>I enjoy hiking. / the bus stop</i>) (Units 37, 39).</li></ol>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Look at the "Not yet" lines and plan two short review activities for the next classes. Next: Unit 41 (Curry). A2 Bridge ends with Review 5 (Unit 49).</p>""")

    b.extra("Audio scripts", f"""
{sub("R4.1", "Ana's online class (slow and natural)")}
<p style="line-height:1.32;font-size:8.6pt">{"<br>".join(f"<b>{n}:</b> {t}" if n != "Narrator" else f"<i>{t}</i>" for n, t in SCRIPT)}</p>
{sub("R4.2", "Sounds: s, z or iz? (3-second pause after each word)")}
<p>{" · ".join(S42)}</p>
{sub("R4.3", "Two dialogues (correct versions)")}
<p style="line-height:1.32;font-size:8.6pt">{"<br>".join(f"<b>{n}:</b> {t}" if n != "Narrator" else f"<i>{t}</i>" for n, t in S43)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 40 - Review 4")
