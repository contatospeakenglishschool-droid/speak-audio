# Speak! Bridge A2 - Review 5 (Units 41-49), all English - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
_se.SERIES = "Bridge"
setup(band="A2 · REVIEW 5", audio_json="audio_a2-review-5.json", img_dir="img")

PHOTOS = [("A", "curry", "Unit 41"), ("B", "a thermometer", "Unit 42"), ("C", "dice", "Unit 43"), ("D", "a game controller", "Unit 45"),
          ("E", "takeout", "Unit 46"), ("F", "a planet", "Unit 47"), ("G", "a farmers market", "Unit 48"), ("H", "Christ the Redeemer", "Unit 49")]

_r = json.load(open("roteiro.json"))["units"]["a2-review-5"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["R5.1 A dinner party"].split("\n")]
S52 = [x.split(": ", 1)[1] for x in _r["R5.2 Can or can't?"].split("\n")][1:]
S53 = [tuple(x.split(": ", 1)) for x in _r["R5.3 Dialogues"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LEVEL A2 · REVIEW 5", "Review 5", "Units 41–49 · quantifiers · advice and rules · purpose · passives · phrasal verbs · questions",
                       [("YOU CAN", "check what you learned in Units 41–49 and plan what to practice next"),
                        ("LANGUAGE", "plenty of · You should… · You don't have to… · to / for / by · It was built… · pick it up · Who was it designed by?"),
                        ("PRONUNCIATION", "can /kən/ or can't /kænt/")])
    b.page(f"""{sec(1, "Warm-up: photo memory", "5 min")}
{sub("A", "One photo from each unit. Write the word or phrase. Then say one sentence about it with the grammar of that unit.", "5 min")}
<div class="bank">Christ the Redeemer · curry · dice · a farmers market · a game controller · a planet · takeout · a thermometer</div>
{photo_grid(T, PHOTOS)}
<p class="small" style="margin-top:2mm"><b>Example:</b> Christ the Redeemer → <i>It was inaugurated in 1931.</i></p>""",
    25, """<p>Photos A–H come from Units 41–49 (Unit 44, life hacks, is practiced on page 4). Push each unit's grammar: quantifiers (41), advice and instructions (42), rules (43), present passive (45), phrasal verbs (46), questions (47), opinions (48), past passive (49).</p>""", cover=cover)

    b.extra("Review overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Units</th><th>SB page</th></tr>
<tr><td>1 Warm-up: photo memory</td><td>5 min</td><td>41–49</td><td>1</td></tr>
<tr><td>2 Listening: a dinner party</td><td>10 min</td><td>41–49</td><td>2</td></tr>
<tr><td>3 Grammar: quantifiers, advice, rules, purpose</td><td>9 min</td><td>41, 42, 43, 44</td><td>3</td></tr>
<tr><td>4 Grammar: passives, phrasal verbs, questions</td><td>9 min</td><td>45, 46, 47, 49</td><td>4</td></tr>
<tr><td>5 Vocabulary and an opinion paragraph</td><td>8 min</td><td>41–49</td><td>5</td></tr>
<tr><td>6 Pronunciation and social English</td><td>9 min</td><td>42, 43, 47, 49</td><td>6</td></tr>
<tr><td>7 Reflect and homework</td><td>5 min</td><td>41–49</td><td>7</td></tr></table>
<div class="box"><h4>HOW THIS GUIDE WORKS</h4>Every page looks like the Student Book page with the same number. Your notes are in the <b>yellow box</b>; <span class="red">answers in red</span> are not in the Student Book. This is a review: don't teach everything again. Let the student work, then focus on the mistakes that come back. The grammar reference pages (page 4) of Units 41–49 are useful here. This is the last unit of A2 Bridge.</div>
<div class="box sand"><h4>THE STORY SO FAR</h4>Saturday evening in Chicago: Tom (Neural2-D) and Lucy (Neural2-C) cook a curry (Unit 41) for Kate (Neural2-G) and Priya (Chirp3-HD-Kore). Priya has a headache and repeats the pharmacist's advice (Unit 42); they talk about Tom on Brain Battle (Unit 47), Ana's TOEIC essay (Unit 48), Paulo's webinar about Brazil (Unit 49) and Kate's blog (Unit 46); Tom suggests GHOST and Kate complains about his rules (Units 35, 43); Lucy gives a life hack (Unit 44); Kate made the ice cream (passives). Dialogues: Priya at the pharmacy (Charon) and Tom on the quiz show (Host: Studio-O). No new facts.</div>
<div class="box"><h4>THE TOP 5 MISTAKES TO WATCH</h4>1. <i>How many money / plenty rice</i> → <b>How much money / plenty of rice</b>. 2. <i>You must to take / You don't have to use your phone (rule)</i> → <b>You must take / You can't use your phone</b>. 3. <i>I study for get a job</i> → <b>to get a job</b>. 4. <i>It built in 1960 / heat up it</i> → <b>It was built / heat it up</b>. 5. <i>Where you are from? / Who did discover…?</i> → <b>Where are you from? / Who discovered…?</b></div>
<div class="box"><h4>AUDIO</h4>Track R5.1 A dinner party (slow and natural) · Track R5.2 Can or can't? · Track R5.3 Two dialogues</div>""")

    # Page 2
    topics = [("food and quantities", True), ("a headache", True), ("a TV quiz show", True), ("an essay", True), ("Brazil", True), ("a new job", False), ("a game", True), ("dessert", True)]
    tl = " &nbsp; ".join(f"☐ {t}{(' ' + R('✓')) if ok else ''}" for t, ok in topics)
    tf = [("There isn't enough rice for everyone.", "F: there's plenty."), ("The curry is very spicy.", "F: just a little chili."),
          ("The pharmacist told Priya to drink more water.", "T"), ("Tom got all the quiz questions right.", "F: five out of eight."),
          ("Priya learned that Brasília was built in less than four years.", "T"), ("The ice cream was bought at a store.", "F: it was made by Kate.")]
    tfl = [f'<li value="{i+1}">{s} <b>T / F</b> {R(a)}</li>' for i, (s, a) in enumerate(tf)]
    find = [("a quantifier (Unit 41)", "plenty for everyone / How much chili / a little / many chilies"), ("advice from the pharmacist (Unit 42)", "I should drink more water / I shouldn't look at my laptop"),
            ("something necessary (Unit 43)", "you have to take it easy / You have to tell us all the rules"), ("to + verb for a purpose (Unit 44)", "To make the ice cream easier to serve"),
            ("a phrasal verb (Unit 46)", "picked up some rice / take it easy / take it out"), ("an opinion phrase (Unit 48)", "In my opinion, she's ready"),
            ("a past passive (Unit 49)", "Brasília was built / Was the ice cream made… / It was made")]
    fl = "".join(f"<li>{x} {R(y)}</li>" for x, y in find)
    b.page(f"""{sec(2, "Listening: a dinner party", "10 min")}
<p>Tom and Lucy are having a dinner party for Kate and their roommate Priya.</p>
{audiocard(["R5.1 · SLOW", "R5.1 · NATURAL"])}
{sub("A", "Listen. What do they talk about? Check (✓) seven topics. One topic is extra.", "2 min", "R5.1 · SLOW")}
<p style="font-weight:600">{tl}</p>
{sub("B", "Listen again. True (T) or false (F)? Correct the false sentences.", "4 min", "R5.1 · NATURAL")}
{twocol(tfl, 4)}
{sub("C", "Find one example in the conversation of each form.", "4 min")}
<ol style="font-size:8.8pt;line-height:1.4">{fl}</ol>""",
    22, """<p>A: the extra topic is <i>a new job</i>. C: let the student read the script (TB last page) or play the natural version again and pause. Ask: <i>Have you ever had a dinner party? What did you cook?</i></p>""")

    # Page 3
    qn = [(["much", "many"], "much", "How", "money do you spend on food?"), (["a few", "a little"], "a little", "Just", "milk in my coffee, please."),
          (["plenty", "plenty of"], "plenty of", "Don't worry, there's", "rice."), (["too much", "too many"], "too many", "There are", "people in this room!")]
    qnl = [f'<li value="{i+1}">{a} {ch(o, r)} {e}</li>' for i, (o, r, a, e) in enumerate(qn)]
    ar = [(["should", "can't"], "can't", "You", "drive after you take this medicine. It's dangerous."), (["don't have to", "can't"], "don't have to", "You", "start with A. Any letter is OK."),
          (["must", "should"], "should", "You look tired. You", "go to bed early."), (["allowed", "supposed"], "allowed", "You're not", "to look at the other players' papers.")]
    arl = [f'<li value="{i+1}">{a} {ch(o, r)} {e}</li>' for i, (o, r, a, e) in enumerate(ar)]
    pm = [("I study English", "to get", "a better job. (get)"), ("", "For", "white sneakers, use toothpaste."), ("Keep your socks together", "by putting", "them in a mesh bag. (put)"),
          ("It works", "because", "the ice melts.")]
    pml = "".join(f"<li>{a}{' ' if a else ''}{A(w, 'min-width:18mm')} {e}</li>" for a, w, e in pm)
    b.page(f"""{sec(3, "Grammar: quantifiers, advice, rules, purpose", "9 min")}
<div class="two"><div>{sub("A", "Unit 41. Choose the correct option.", "2 min")}
<ol style="line-height:1.6;margin:0">{"".join(qnl)}</ol></div>
<div>{sub("B", "Units 42–43. Choose the correct option.", "3 min")}
<ol style="line-height:1.6;margin:0">{"".join(arl)}</ol></div></div>
{sub("C", "Unit 44. Complete with to, for, by or because. Use the verbs in brackets.", "3 min")}
<ol style="line-height:1.7">{pml}</ol>
<div class="box sand"><h4>REMEMBER</h4><b>much / a little</b> + uncountable · <b>many / a few</b> + plural · <b>plenty of</b> = enough and extra · <b>should</b> = advice · <b>must / have to</b> = necessary · <b>can't</b> = not allowed · <b>don't have to</b> = not necessary · <b>to</b> + verb, <b>for</b> + noun, <b>by</b> + verb-ing, <b>because</b> + subject + verb.</div>""",
    22, """<ol><li>B: insist on the difference between <i>can't</i> (not allowed) and <i>don't have to</i> (not necessary).</li>
<li>C: ask for a personal sentence: <i>Why are you learning English?</i> → <i>To…</i></li></ol>""")

    # Page 4
    pv = [(["is made", "was made"], "was made", "The ice cream", "this morning."), (["is spoken", "was spoken"], "is spoken", "Portuguese", "in Brazil."),
          (["were designed", "was designed"], "were designed", "Many buildings in Brasília", "by Niemeyer."), (["is tested", "tests"], "is tested", "Every game", "before it goes on sale.")]
    pvl = [f'<li value="{i+1}">{a} {ch(o, r)} {e}</li>' for i, (o, r, a, e) in enumerate(pv)]
    ph = [("Heat up it in the microwave.", "Heat it up"), ("Let's eat up tonight.", "eat out"), ("I'm cutting down sugar.", "cutting down on"), ("Cut up them, please.", "Cut them up")]
    phl = [f'<li value="{i+1}">{a} {A(c, "min-width:22mm")}</li>' for i, (a, c) in enumerate(ph)]
    qq = [("Where you are from?", "Where are you from?"), ("Who did discover the galaxies?", "Who discovered the galaxies?"), ("When was built the stadium?", "When was the stadium built?"),
          ("How many rings Saturn has?", "How many rings does Saturn have?")]
    qql = "".join(f"<li>{a} {A(c, 'min-width:46mm')}</li>" for a, c in qq)
    b.page(f"""{sec(4, "Grammar: passives, phrasal verbs, questions", "9 min")}
<div class="two"><div>{sub("A", "Units 45 and 49. Choose the correct passive.", "2 min")}
<ol style="line-height:1.6;margin:0">{"".join(pvl)}</ol></div>
<div>{sub("B", "Unit 46. Correct the phrasal verbs.", "2 min")}
<ol style="line-height:1.6;margin:0">{"".join(phl)}</ol></div></div>
{sub("C", "Unit 47. Correct the questions.", "3 min")}
<ol style="line-height:1.7">{qql}</ol>
{sub("D", "Unit 49. Ask your teacher two questions about a famous place: When was it…? Who was it… by?", "2 min")}
<div class="box sand"><h4>REMEMBER</h4><b>passive:</b> is / are (present) or was / were (past) + past participle · <b>phrasal verbs:</b> pronouns go in the middle (<i>heat it up</i>) · <b>questions:</b> do / does / did in simple forms, change the order in other tenses, no auxiliary in subject questions.</div>""",
    22, """<ol><li>A: ask: now or in the past? singular or plural? B: separable type 3 + pronoun.</li>
<li>C: these four question mistakes are the most common at A2; drill each correct question with the right intonation.</li></ol>""")

    # Page 5
    vc = [("a thing that is nice but not necessary, and expensive", "a luxury"), ("food you buy in a restaurant and eat at home", "takeout"),
          ("problems that some medicine can cause", "side effects"), ("a problem or mistake in a computer program", "a bug"),
          ("the people a product is for", "the target audience"), ("a person who competes on a TV quiz show", "a contestant"),
          ("how far food travels from the farm to you", "food miles"), ("a smart, easy solution to an everyday problem", "a life hack")]
    b.page(f"""{sec(5, "Vocabulary and an opinion paragraph", "8 min")}
{sub("A", "Units 41–49. Write the word or phrase.", "4 min")}
<div class="bank">a bug · a contestant · food miles · a life hack · a luxury · side effects · takeout · the target audience</div>
{twocol([f'<li value="{i+1}">{d} → {A(w, "min-width:22mm")}</li>' for i, (d, w) in enumerate(vc)], 5)}
{sub("B", "Unit 48. Put the sentences in order to make a short opinion paragraph (1–5).", "4 min")}
<ul style="line-height:1.6;padding-left:2mm;margin:0;list-style:none">
<li>{A("3", "min-width:6mm;text-align:center")} However, it can be expensive and difficult to find.</li>
<li>{A("1", "min-width:6mm;text-align:center")} Should we always eat organic food?</li>
<li>{A("5", "min-width:6mm;text-align:center")} In conclusion, we should buy it when we can, but we don't have to buy it every day.</li>
<li>{A("2", "min-width:6mm;text-align:center")} First of all, many people think it is better for the environment.</li>
<li>{A("4", "min-width:6mm;text-align:center")} For example, some organic fruit travels thousands of kilometers.</li></ul>""",
    22, """<ol><li>A: after each word, ask a personal question: <i>What's a luxury for you? Do you often order takeout?</i></li>
<li>B: point out the question in the introduction, the linking words and the advice in the conclusion.</li></ol>""")

    # Page 6
    cn = {"can": "1, 3, 5, 7, 9", "can't": "2, 4, 6, 8"}
    cnt = "".join(f"<td style='height:12mm;vertical-align:top'><b>{k}</b><br>{R(v)}</td>" for k, v in cn.items())
    d1 = [("Pharmacist", "Here are your pills. You <u>must to take</u> one pill three times a day."), ("Priya", "OK. Can I take them with food?"),
          ("Pharmacist", "Yes, it's a good idea <u>take</u> them with a meal. But you <u>don't have to</u> drive after you take them."),
          ("Priya", "How <u>many</u> do they cost?"), ("Pharmacist", "Your insurance covers them, so you <u>can't</u> pay anything.")]
    d2 = [("Host", "Next question. Where <u>the Maracanã stadium was</u> built?"), ("Tom", "It <u>built</u> in Rio de Janeiro."),
          ("Host", "Correct! And who <u>was</u> many buildings in Brasília designed by?"), ("Tom", "They were designed <u>for</u> Oscar Niemeyer."),
          ("Host", "Correct again! How many questions <u>you have answered</u> today?")]
    def dlg(lines):
        return "<br>".join(f"<b>{n}:</b> {t}" for n, t in lines)
    b.page(f"""{sec(6, "Pronunciation and social English", "9 min")}
{audiocard(["R5.2", "R5.3"])}
{sub("A", "Units 42–43. Listen to nine rules. Write each number in the correct column.", "3 min", "R5.2")}
<table style="table-layout:fixed;margin-top:0"><tr>{cnt}</tr></table>
{sub("B", "Units 41–49. Each dialogue has mistakes (underlined). Correct them. Then listen and check.", "4 min", "R5.3")}
<div class="two"><div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.8pt;line-height:1.5"><b>Dialogue 1</b><br>{dlg(d1)}</div>
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.8pt;line-height:1.5"><b>Dialogue 2</b><br>{dlg(d2)}</div></div>
<p class="small">{R("1: must take · a good idea to take · can't drive · How much · don't have to pay — 2: Where was the Maracanã stadium built? · It was built · who were · designed by · How many questions have you answered")}</p>
{sub("C", "Role-play the dialogues with your teacher. Then change roles.", "2 min")}""",
    32, """<ol><li>A: 3-second pause after each rule. <i>can</i> = /kən/ (short, weak); <i>can't</i> = /kænt/ (long, stressed; the t is often silent in American English).</li>
<li>B: Dialogue 1 mixes advice, instructions and quantifiers; Dialogue 2 mixes passives and questions.</li></ol>""")

    # Page 7
    ck = [("41", "I can talk about quantities with some, any, much, many, enough and plenty of."), ("42", "I can understand and give advice and instructions at a pharmacy."),
          ("43", "I can explain the rules of a game."), ("44", "I can explain how to solve a problem and why a solution works."),
          ("45", "I can describe a process with the present simple passive."), ("46", "I can use food phrasal verbs with the correct word order."),
          ("47", "I can ask correct questions in different tenses."), ("48", "I can plan and write a short opinion essay."), ("49", "I can talk about history with the past simple passive.")]
    ckr = "".join(f"<tr><td><b>Unit {u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in ck)
    b.page(f"""{sec(7, "Reflect and homework", "5 min")}
{sub("A", "How are you doing? Check one box for each line.", "2 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{ckr}</table>
{sub("B", "My goals for B1. What do you want to practice more? Write two things.", "2 min")}
<div class="wline"></div><div class="wline"></div>
{sub("C", "Homework", "1 min")}
<p><b>My A2 year (80–100 words).</b> Write about your English this year. Include:</p>
<ol><li>one thing you can do now that you couldn't do before (a passive or a question form);</li><li>some advice for a new A2 student (<i>You should… / You don't have to…</i>);</li>
<li>one phrasal verb and one quantifier;</li><li>your opinion: <i>In my opinion, … · For example, …</i></li></ol>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Congratulations: this is the end of A2 Bridge. Use the "Not yet" lines to plan the first review activities of B1 Progress. Keep this text as a writing sample to compare at the end of B1.</p>""")

    b.extra("Audio scripts", f"""
{sub("R5.1", "A dinner party (slow and natural)")}
<p style="line-height:1.32;font-size:8.6pt">{"<br>".join(f"<b>{n}:</b> {t}" if n != "Narrator" else f"<i>{t}</i>" for n, t in SCRIPT)}</p>
{sub("R5.2", "Can or can't? (3-second pause after each rule)")}
<p>{" · ".join(S52)}</p>
{sub("R5.3", "Two dialogues (correct versions)")}
<p style="line-height:1.32;font-size:8.6pt">{"<br>".join(f"<b>{n}:</b> {t}" if n != "Narrator" else f"<i>{t}</i>" for n, t in S53)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 50 - Review 5")
