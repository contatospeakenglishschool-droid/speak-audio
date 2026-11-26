# Speak! Progress B1 - Review 6 (Units 51-59), all English - B1 review format (8 pages)
import sys, os, json
_h = os.path.dirname(os.path.abspath(__file__))
for _d in ("/home/claude/speak-audio/engine", os.path.join(_h, "..", "speak-audio", "engine"), os.path.join(_h, "..", "..", "speak-audio", "engine"), os.path.join(_h, "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
_se.SERIES = "Progress"
setup(band="B1 · REVIEW 6", audio_json="audio_b1-review-6.json", img_dir="img")

PHOTOS = [("A", "a dog", "Unit 51"), ("B", "a toucan", "Unit 52"), ("C", "an hourglass", "Unit 53"), ("D", "a soccer ball", "Unit 54"),
          ("E", "a hammock", "Unit 55"), ("F", "an alarm clock", "Unit 56"), ("G", "a fire truck", "Unit 57"), ("H", "a bakery", "Unit 58")]
_r = json.load(open("roteiro.json"))["units"]["b1-review-6"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["R6.1 Sunday lunch at the hostel"].split("\n")]
S52 = [x.split(": ", 1)[1].split(". ", 1)[1] for x in _r["R6.2 Dictation: weak forms"].split("\n")]
S53 = [tuple(x.split(": ", 1)) for x in _r["R6.3 Dialogues"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def lines(n):
        return '<div class="wline"></div>' * n

    # Page 1 - Warm-up
    cover = cover_html(T, "LEVEL B1 · REVIEW 6", "Review 6", "Units 51–59 · <b>past modals · future perfect · reporting verbs · had been + -ing</b>",
                       [("YOU CAN", "check what you learned in Units 51–59 and plan what to practice next"),
                        ("LANGUAGE", "must have · heard them screaming · will have done · twice as… as · a cake made by… · there's been · denied doing · had been doing"),
                        ("PRONUNCIATION", "weak forms: must have, had been, will have, to, as")])
    b.page(f"""{sec(1, "Warm-up: photo memory", "6 min")}
{sub("A", "One photo from each unit. Write the word. Then say one sentence about it with the language of that unit.", "6 min")}
<div class="bank">an alarm clock · a bakery · a dog · a fire truck · a hammock · an hourglass · a soccer ball · a toucan</div>
{photo_grid(T, PHOTOS)}
<p class="small" style="margin-top:2mm"><b>Example:</b> a dog → <i>Pipoca's bowl was empty. He must have eaten all the food.</i></p>""",
    25, """<p>Photos A–H come from Units 51–58 (Unit 59 is in the listening). Push each unit's language: past modals, <i>must have / should have</i> (51); <i>see / hear someone doing</i> (52); the future perfect (53); <i>twice as… as, the more… the more</i> (54); participle clauses (55); uses of <i>get</i> (56); <i>there's been, there might be</i> (57); reporting verbs (58).</p>""", cover=cover)

    b.extra("Review overview · 60 min", """
<table><tr><th>Stage</th><th>Time</th><th>Units</th><th>SB page</th></tr>
<tr><td>1 Warm-up: photo memory</td><td>6 min</td><td>51–58</td><td>1</td></tr>
<tr><td>2 Listening: Sunday lunch at the hostel</td><td>10 min</td><td>51–59</td><td>2</td></tr>
<tr><td>3 Grammar 1: past modals, perception verbs, future perfect, comparisons, participle clauses</td><td>8 min</td><td>51–55</td><td>3</td></tr>
<tr><td>4 Grammar 2: correct Danny's email</td><td>8 min</td><td>56–59</td><td>4</td></tr>
<tr><td>5 Vocabulary and word choice</td><td>7 min</td><td>51–59</td><td>5</td></tr>
<tr><td>6 Pronunciation and social English</td><td>8 min</td><td>52–59</td><td>6</td></tr>
<tr><td>7 Speaking: long turn and role-play</td><td>9 min</td><td>51–59</td><td>7</td></tr>
<tr><td>8 Reflect and homework</td><td>4 min</td><td>51–59</td><td>8</td></tr></table>
<div class="box"><h4>HOW THIS GUIDE WORKS</h4>Every page looks like the Student Book page with the same number. Your notes are in the <b>yellow box</b>; <span class="red">answers in red</span> are not in the Student Book. This is a review: don't teach everything again. Let the student work, then focus on the mistakes that come back. The Grammar reference pages of Units 51–59 are useful here.</div>
<div class="box sand"><h4>THE STORY SO FAR</h4>Sunday lunch at Mrs. Lima's hostel (Mrs. Lima = Vindemiatrix). She serves a cake made by her cousin Dora, the founder of the Strange Games (55). Pipoca, the dog she adopted (51), smells the cheese bread; he is now twice as fast as Bruno (Fenrir) (54). Rafa (Umbriel) is still embarrassed about sharing the fake bakery rumor; Mr. Nunes admitted selling more bread that day than at Christmas (58). Danny (Puck) tells his mom about the monkeys and the jaguar in the Pantanal (52); Rafa had been planning to go, but his band had a gig (59). Danny now gets up at six for his 7 a.m. classes, and Ana calls him (56); by December he'll have taught more than two hundred classes (53). Carol's crazy week in Orlando (57). Movie night: the war film (59). Dialogues: Carol reports a break-in to the operator (Charon) (57); Ana and Danny after a late soccer game (54, 56). There are no real-world facts in this review.</div>
<div class="box"><h4>THE TOP 5 MISTAKES TO WATCH</h4>1. <i>He must ate</i> → <b>must have eaten</b>; <i>I heard the monkeys to scream</i> → <b>heard them scream / screaming</b>. 2. <i>By December I will teach 200</i> → <b>will have taught</b>; <i>two times more fast</i> → <b>twice as fast as</b>. 3. <i>a cake making by Dora</i> → <b>made</b>; <i>I slept late</i> (= went to bed late) → <b>stayed up late</b>. 4. <i>Has an accident</i> → <b>There's been an accident</b>; <i>She suggested me to check</i> → <b>suggested checking</b>. 5. <i>They were fighting for six years when…</i> → <b>had been fighting</b>.</div>
<div class="box"><h4>AUDIO</h4>Track R6.1 Sunday lunch at the hostel (natural and slow) · Track R6.2 Dictation: weak forms (6-second pauses) · Track R6.3 Two dialogues (correct versions)</div>""")

    # Page 2 - Listening
    topics = [("Dora's cake", True), ("Pipoca", True), ("the bakery rumor", True), ("the Pantanal", True), ("Rafa's band", True),
              ("Danny's 7 a.m. classes", True), ("Carol's week", True), ("a soccer game", False), ("a war film", True)]
    tl = " &nbsp; ".join(f"☐ {t}{(' ' + R('✓')) if ok else ''}" for t, ok in topics)
    tf = [("Pipoca is faster than Bruno now.", "T: twice as fast."), ("Rafa went to the Pantanal with Danny and Bruno.", "F: he'd been planning to go, but the band had a gig."),
          ("Danny gets up at seven now.", "F: he gets up at six."), ("Danny has already taught two hundred classes.", "F: about 150; he'll have taught 200+ by December."),
          ("Mr. Nunes sold a lot of bread on the day of the rumor.", "T"), ("Bruno loved the war film.", "F: it was too long for him; Danny loved it.")]
    tfl = [f'<li value="{i+1}">{s} <b>T / F</b> {R(a)}</li>' for i, (s, a) in enumerate(tf)]
    find = [("must / must have (51)", "It must be strange too! / He must have smelled the cheese bread."), ("hear / see + object + -ing (52)", "we'd heard the monkeys screaming… seen a jaguar walking"),
            ("the future perfect (53)", "By December, I'll have taught more than two hundred."), ("the more… / twice as… as (54)", "The more Bruno runs with him, the faster he gets. / twice as fast as me"),
            ("a participle clause (55)", "a cake made by my cousin Dora"), ("get (56)", "Pipoca, get down! / He's getting faster / I get up at six"),
            ("there + be (57)", "There was a fire next door… there was an accident"), ("a reporting verb (58)", "I've promised to check / Mr. Nunes admitted selling"),
            ("the past perfect continuous (59)", "I'd been planning to go with you")]
    fl = "".join(f"<li>{x} {R(y)}</li>" for x, y in find)
    b.page(f"""{sec(2, "Listening: Sunday lunch at the hostel", "10 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
<p style="margin:0">It's Sunday. Mrs. Lima invites Danny, Bruno and Rafa for lunch at the hostel. Pipoca is there too, of course.</p>
{audiocard(["R6.1 · NATURAL", "R6.1 · SLOW"])}</div><div style="width:40mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo('I')}" style="width:40mm;height:24mm;object-fit:cover;display:block"></div></div>
{sub("A", "Listen at natural speed. Which topics do they talk about? Check eight. One topic is extra.", "2 min", "R6.1")}
<p style="font-weight:600;font-size:8.8pt;line-height:1.6">{tl}</p>
{sub("B", "Listen again. True (T) or false (F)? Correct the false sentences.", "4 min")}
<div style="font-size:8.6pt">{twocol(tfl, 3)}</div>
{sub("C", "Find one example in the dialogue of each form. Use the audio script or listen again.", "4 min")}
<ol style="font-size:8.4pt;line-height:1.35;margin:0">{fl}</ol>""",
    20, """<p>A: the extra topic is <i>a soccer game</i> (they talk about running, not soccer). C: let the student read the script (last page of this guide) or play the slow version and pause. Ask: <i>What was the best Sunday lunch you ever had?</i></p>""")

    # Page 3 - Grammar 1
    def cho(items):
        return "".join(f"<li>{a} {ch(o, r_)}{e}</li>" for o, r_, a, e in items)
    pm = [(["should have", "must have"], "must have", "Pipoca's bowl is empty. He", " eaten everything."), (["should have", "must have"], "should have", "You missed the bus. You", " left earlier.")]
    pv = [(["to scream", "screaming"], "screaming", "At five a.m. we heard the monkeys", "."), (["walking", "walked"], "walking", "We saw a jaguar", " along the river.")]
    fp = [("By December, Danny", "will have taught", "(teach) two hundred classes."), ("By 2050, Mrs. Lima", "will have turned", "(turn) ninety.")]
    fpl = "".join(f'<li>{a} {A(v, "min-width:30mm")} {z}</li>' for a, v, z in fp)
    cm = [("Pipoca is fast. Bruno is half as fast. (twice)", "Pipoca is twice as fast as Bruno."), ("If you practice more, you get better. (The more…)", "The more you practice, the better you get.")]
    cml = "".join(f'<li><i>{d}</i> {A(i, "min-width:50mm")}</li>' for d, i in cm)
    pc = [(["making", "made"], "made", "We ate a cake", " by Dora."), (["holding", "held"], "holding", "The woman", " the umbrella is seventy.")]
    b.page(f"""{sec(3, "Grammar 1: Units 51–55", "8 min")}
{sub("A", "Unit 51. Choose.", "1 min")}
<ol style="line-height:1.7;font-size:8.8pt;margin:0">{cho(pm)}</ol>
{sub("B", "Unit 52. Choose.", "1 min")}
<ol style="line-height:1.7;font-size:8.8pt;margin:0">{cho(pv)}</ol>
{sub("C", "Unit 53. Complete with the future perfect.", "2 min")}
<ol style="line-height:1.7;font-size:8.8pt;margin:0">{fpl}</ol>
{sub("D", "Unit 54. Rewrite with the word in brackets.", "2 min")}
<ol style="line-height:1.7;font-size:8.8pt;margin:0">{cml}</ol>
{sub("E", "Unit 55. Choose.", "1 min")}
<ol style="line-height:1.7;font-size:8.8pt;margin:0">{cho(pc)}</ol>
<div class="box sand"><h4>REMEMBER</h4><b>must have / might have</b> + past participle = a guess about the past; <b>should have</b> = criticism or regret · <b>see / hear / watch</b> + object + base form (whole action) or <b>-ing</b> (in progress) · <b>will have</b> + past participle = finished before a future time · <b>twice as</b> + adjective + <b>as</b>; <b>the</b> + comparative…, <b>the</b> + comparative · <b>-ing</b> = active, <b>past participle</b> = passive.</div>""",
    22, """<ol><li>A–E: ask the student to explain each choice. In B, <i>heard the monkeys scream</i> is also correct (the whole action).</li>
<li>After each section, ask one personal question with the same form: <i>What will you have done by the end of the year?</i></li></ol>""")

    # Page 4 - Grammar 2
    errs = [("got up", "got up"), ("suggested me to put", "suggested putting / suggested that I put"), ("had", "there was"), ("Has been", "There have been"),
            ("apologized to share", "apologized for sharing"), ("promised checking", "promised to check"), ("were fighting", "had been fighting"), ("had been knowing", "had known")]
    def e(i):
        w, c = errs[i]
        return f"<u>{w}</u>" + (f" {R('→ ' + c)}" if T and w != c else (f" {R('✓')}" if T else ""))
    b.page(f"""{sec(4, "Grammar 2: Units 56–59", "8 min")}
{sub("A", "Danny writes to his mom. Eight words or phrases are underlined. Seven are wrong. Correct them.", "6 min")}
<div class="box" style="line-height:1.95;font-size:9pt">Hi Mom!<br>Good news: this week I {e(0)} at six every day! Ana {e(1)} my phone in the kitchen, and it works. On Friday, {e(2)} a fire alarm at the hostel, but it was only toast. {e(3)} a lot of rumors on the street this month, too. Rafa {e(4)} the fake bakery message, and he {e(5)} everything from now on. On Saturday we watched a war film. At the start, the two sides {e(6)} for six years. Bruno said he {e(7)} the ending since the first scene! Love, Danny</div>
{sub("B", "Units 56–59. Complete the sentences so they are true for you. Then tell your teacher.", "2 min")}
<ol style="line-height:1.35;font-size:8.9pt;margin:0"><li>I usually get… when…<div class="wline"></div></li><li>Recently there's been… in my city.<div class="wline"></div></li><li>My parents always warned me not to…<div class="wline"></div></li><li>When I started this course, I'd been… for…<div class="wline"></div></li></ol>
<div class="box sand"><h4>REMEMBER</h4><b>get up</b> = leave the bed; <b>get</b> + adjective = become · <b>there</b> + be in all tenses: <i>there was, there have been, there'll be</i> (not <i>had / has</i>) · <b>suggest</b> + -ing; <b>apologize for</b> + -ing; <b>promise to</b> + verb · <b>had been</b> + -ing = an activity up to a past moment; state verbs (<i>know</i>) use <b>had known</b>.</div>""",
    22, """<ol><li>A: word 1 (<i>got up</i>) is correct. For 4, <i>There's been a lot of rumors</i> is common in speech, but <i>There have been</i> is correct with a plural noun.</li>
<li>B: correct with the student, then ask follow-up questions in the same structures.</li></ol>""")

    # Page 5 - Vocabulary
    vw = [("tell someone your secrets or private feelings", "confide"), ("an animal that may disappear forever", "an endangered species"),
          ("the average number of children women have", "fertility rate"), ("the person who controls a game and makes sure players follow the rules", "a referee"),
          ("with no purpose or reason", "pointless"), ("sleep longer than you planned", "oversleep"), ("not able to escape from a place", "trapped"),
          ("a story passed from person to person that may not be true", "a rumor"), ("an agreement to stop fighting for a period of time", "a truce")]
    order = [4, 7, 0, 6, 1, 8, 3, 5, 2]
    vcl = [f'<li value="{k+1}">{vw[i][0]} → {A(vw[i][1], "min-width:24mm")}</li>' for k, i in enumerate(order)]
    ff = [(["create", "have"], "have", "I", " a dog and two cats."), (["Look at", "Look"], "Look at", "", " the monkey!"),
          (["less", "fewer"], "fewer", "Today people have", " children."), (["watched", "assisted"], "watched", "I", " the game on TV."),
          (["won", "beat"], "beat", "We", " the other team 3–1."), (["overslept", "lost the hour"], "overslept", "I", " this morning."),
          (["denounce", "report"], "report", "I want to", " a robbery."), (["is", "are"], "is", "Fake news", " dangerous.")]
    ffl = "".join(f"<li>{a + ' ' if a else ''}{ch(o, r_)}{e2}</li>" for o, r_, a, e2 in ff)
    b.page(f"""{sec(5, "Vocabulary and word choice", "7 min")}
{sub("A", "Units 51–59. Write the word or phrase.", "3 min")}
<div class="bank">confide · an endangered species · fertility rate · oversleep · pointless · a referee · a rumor · trapped · a truce</div>
<div style="font-size:8.7pt">{twocol(vcl, 5)}</div>
{sub("B", "Watch out! Units 51–59. Choose the correct words.", "4 min")}
<ol style="line-height:1.75;font-size:8.9pt;margin:0;columns:2;column-gap:5mm">{ffl}</ol>
<div class="box sand"><h4>YOUR WORD BANK</h4>Choose five words from Units 51–59 that you want to use more. Write a personal sentence with each one in your notebook.</div>""",
    22, """<ol><li>A: after each word, ask a personal question: <i>Who do you confide in? Have you ever overslept on an important day? Have you ever heard a rumor about yourself?</i></li>
<li>B: these come from the WATCH OUT boxes of Units 51–58.</li></ol>""")

    # Page 6 - Pronunciation and social English
    d1 = [("Operator", "Nine one one, what's your emergency?"), ("Carol", "I'd like to <u>denounce</u> a break-in. My neighbor's window is broken."),
          ("Operator", "<u>Is anyone hurt</u>?"), ("Carol", "I don't think so. But <u>might have someone</u> inside."), ("Operator", "OK, ma'am. Stay outside. <u>Will have an officer</u> there in ten minutes.")]
    d2 = [("Ana", "You look tired. Did you sleep well?"), ("Danny", "Not really. I <u>slept late</u> watching the game, and this morning I <u>lost the hour</u>."),
          ("Ana", "Who won?"), ("Danny", "We <u>won them</u> two to one! It was <u>twice as exciting as</u> last week.")]
    def dlg(ls):
        return "<br>".join(f"<b>{n}:</b> {t}" for n, t in ls)
    b.page(f"""{sec(6, "Pronunciation and social English", "8 min")}
{audiocard(["R6.2", "R6.3"])}
{sub("A", "Dictation. Listen and write the six sentences. Notice the weak forms: must have /ˈmʌstəv/, they'd been /ðeɪd bɪn/, I'll have /ˈaɪləv/, to /tə/, as /əz/.", "4 min", "R6.2")}
<ol style="font-size:8.8pt;margin:0;line-height:1.3">{"".join(f"<li>{R(s) if T else '<div class=wline></div>'}</li>" for s in S52)}</ol>
{sub("B", "Each dialogue has mistakes (underlined; one in each dialogue is correct). Correct them. Then listen and check.", "4 min", "R6.3")}
<div class="two"><div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.5pt;line-height:1.45"><b>Dialogue 1</b><br>{dlg(d1)}</div>
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.5pt;line-height:1.45"><b>Dialogue 2</b><br>{dlg(d2)}</div></div>
<p class="small">{R("1: report · Is anyone hurt ✓ · there might be someone · There'll be an officer — 2: stayed up late · overslept · beat them · twice as exciting as ✓")}</p>""",
    28, """<ol><li>A: the track has a 6-second pause after each sentence; pause more if needed. In sentence 4, <i>There's been</i> = <i>There has been</i>.</li>
<li>B: then role-play the dialogues with the student; change roles and change the details (a different emergency, a different game).</li></ol>""")

    # Page 7 - Speaking
    b.page(f"""{sec(7, "Speaking: long turn and role-play", "9 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE FROM UNITS 51–59</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>guessing and comparing</th><th>explaining</th><th>emergencies</th><th>news and stories</th></tr>
<tr><td><i>He must have… · She might have… · It's twice as… as… · The more…, the more…</i></td><td><i>The aim of the game is to… · You're (not) allowed to… · One tip is to…</i></td><td><i>I'd like to report… · There's been… · There might be someone…</i></td><td><i>Where did you see that? · I'm not sure that's true. · That's not true! · At the start, they'd been…</i></td></tr></table></div>
{sub("A", "Long turn. Choose one card. Prepare for one minute, then talk for two minutes.", "5 min")}
<div style="display:flex;gap:2mm;font-size:8.5pt;margin:.5mm 0">
<div class="msg" style="max-width:none;flex:1;padding:1.5mm 2.5mm"><b>Card 1: An animal you know</b><br>what it's like · a funny or strange thing it did · what it must have been thinking · what you saw or heard it doing</div>
<div class="msg" style="max-width:none;flex:1;padding:1.5mm 2.5mm"><b>Card 2: A game or event</b><br>where it was · what you saw and heard · how it compared with others (twice as…) · what you will have done by next year</div>
<div class="msg" style="max-width:none;flex:1;padding:1.5mm 2.5mm"><b>Card 3: A story you heard</b><br>a rumor, a news story or a film · what had been happening before · what people claimed, denied or admitted · was it true?</div></div>
{sub("B", "Role-play. Call the emergency services: your teacher is the operator. Choose a fire, a break-in or an accident. Then tell a friend what happened: The operator asked me… / told me not to… Change roles.", "4 min")}
<p style="margin:.3mm 0;font-size:8.6pt">{R("Teacher's card: ask what, where and is anyone hurt; give one instruction (Stay away from the smoke / Don't move anyone). Then be the friend: ask questions with reporting verbs (What did they advise you to do?). Next round, the student is the operator.") if T else ""}</p>""",
    28, """<ol><li>A: let the student choose; note mistakes for the reflection on page 8. Fluency option (3-2-1): the same talk in 2 minutes, then in 1 minute.</li>
<li>B: keep it realistic: the student's real street or city, with invented events.</li></ol>""")

    # Page 8 - Reflect
    ck = [("51", "I can talk about pets, guess what happened and say what someone should have done."), ("52", "I can describe animals and say what I saw, heard or felt on a trip."),
          ("53", "I can talk about population and say what will have happened by a future time."), ("54", "I can talk about sports and compare them in detail."),
          ("55", "I can describe unusual sports and explain the rules of a game."), ("56", "I can talk about sleep and give tips to get up more easily."),
          ("57", "I can make an emergency call and answer the operator's questions."), ("58", "I can talk about fake news and report what people said."),
          ("59", "I can talk about conflict, review a film and tell a story with had been + -ing.")]
    ckr = "".join(f"<tr><td><b>Unit {u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in ck)
    b.page(f"""{sec(8, "Reflect and homework", "4 min")}
{sub("A", "How are you doing? Check one box for each line.", "1 min")}
<table class="ck" style="font-size:8.4pt"><tr><th style="width:15mm"></th><th>In English…</th><th style="width:15mm">Easy!</th><th style="width:15mm">Sometimes</th><th style="width:15mm">Not yet</th></tr>{ckr}</table>
{sub("B", "My language notes. Look at your notes from Units 51–59. Which mistake do you still make? What are your two goals for Units 61–69?", "2 min")}
{lines(3)}
{sub("C", "Homework: writing (100–150 words)", "1 min")}
<p style="margin:.3mm 0"><b>A story people believed.</b> Write about a rumor, a surprising event or a film that people talked about. Use at least five of these: <i>must have / should have · heard / saw someone doing · will have · twice as… as · a participle clause · get · there's been · denied / admitted / warned · had been + -ing</i>.</p>
{lines(6)}""",
    22, """<p>Compare this writing with the one from Review 5: is it longer, more accurate, more varied? Use the "Not yet" lines to plan extra practice before Unit 61.</p>""")

    def scr(lst):
        return "<br>".join(f"<b>{n}:</b> {t}" if n != "Narrator" else f"<i>{t}</i>" for n, t in lst)
    b.extra("Audio scripts", f"""
{sub("R6.1", "Sunday lunch at the hostel (natural and slow)")}
<p style="line-height:1.3;font-size:8.3pt">{scr(SCRIPT)}</p>
{sub("R6.2", "Dictation: weak forms (6-second pauses)")}
<p style="font-size:8.6pt">{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S52))}</p>
{sub("R6.3", "Two dialogues (correct versions)")}
<p style="line-height:1.3;font-size:8.3pt">{scr(S53)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 60 - Review 6")
