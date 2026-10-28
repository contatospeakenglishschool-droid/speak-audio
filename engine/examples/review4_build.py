# Speak! Essentials A1 - Review 4 (Units 28-35), all English - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
from speak_engine import *
setup(band="A1 · REVIEW 4", audio_json="audio_a1-review-4.json", img_dir="img")

PHOTOS = [("A", "a bank", "Unit 28"), ("B", "a sweater", "Unit 29"), ("C", "an onion", "Unit 30"), ("D", "strawberries", "Unit 31"),
          ("E", "see the dentist", "Unit 32"), ("F", "do housework", "Unit 33"), ("G", "eat out", "Unit 34"), ("H", "feed the animals", "Unit 35")]

_r = json.load(open("roteiro.json"))["units"]["a1-review-4"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["R4.1 Airport"].split("\n")]
S42 = [x.split(": ", 1)[1] for x in _r["R4.2 Write can or cant"].split("\n")][1:]
S43 = [tuple(x.split(": ", 1)) for x in _r["R4.3 Dialogues"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1: cover + photo memory
    cover = cover_html(T, "LEVEL A1 · REVIEW 4", "Review 4", "Units 28–35 · questions · quantity · the future · advice and rules",
                       [("YOU CAN", "check what you learned in Units 28–35 and plan what to practice"),
                        ("LANGUAGE", "Who painted it? · some / any · I'm meeting… · It'll… · You should… · You mustn't…"),
                        ("PRONUNCIATION", "can ≠ can't · won't ≠ want · should, could (silent l)")])
    b.page(f"""{sec(1, "Warm-up: photo memory", "5 min")}
{sub("A", "One photo from each unit. Write the word or phrase. Then say one sentence about it.", "5 min")}
<div class="bank">a bank · do housework · eat out · feed the animals · an onion · see the dentist · strawberries · a sweater</div>
{photo_grid(T, PHOTOS)}
<p class="small" style="margin-top:2mm"><b>Example:</b> strawberries → <i>How many strawberries are one serving? Seven!</i></p>""",
    20, """<p>Photos A–H come from Units 28–35 in order. Push the grammar of each unit: a question (28), shopping (29), <i>some / any</i> (30), <i>how much / how many</i> (31), a plan (32), a prediction (33), advice (34), a rule (35).</p>""", cover=cover)

    b.extra("Review overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Units</th><th>SB page</th></tr>
<tr><td>1 Warm-up: photo memory</td><td>5 min</td><td>28–35</td><td>1</td></tr>
<tr><td>2 Listening: Tom arrives in São Paulo</td><td>10 min</td><td>28–35</td><td>2</td></tr>
<tr><td>3 Grammar: questions and quantity</td><td>8 min</td><td>28, 30, 31</td><td>3</td></tr>
<tr><td>4 Grammar: the future, advice and rules</td><td>10 min</td><td>32–35</td><td>4</td></tr>
<tr><td>5 Vocabulary</td><td>8 min</td><td>29–35</td><td>5</td></tr>
<tr><td>6 Pronunciation and social English</td><td>9 min</td><td>29, 34, 35</td><td>6</td></tr>
<tr><td>7 Reflect and homework</td><td>5 min</td><td>28–35</td><td>7</td></tr></table>
<div class="box"><h4>HOW THIS GUIDE WORKS</h4>Every page looks like the Student Book page with the same number. Your notes are in the <b>yellow box</b>.
<span class="red">Answers in red</span> are not in the Student Book. Audio scripts are on the last page. This is a review: don't teach everything again. Let the student work, then focus on the mistakes that come back.</div>
<div class="box sand"><h4>THE STORY SO FAR</h4>December 28th. Tom arrives in São Paulo for New Year's (his plan in Unit 32). Ana meets him at the airport. Tom needs summer clothes (Unit 29), the family is making a big dinner (Units 30–31), Paulo is bringing Buddy the robot for Grandma Lourdes (Unit 33), they're going to the beach in Santos (Unit 32), Ana gives advice and rules (Units 34–35)… and Tom wants to save money (Unit 34).</div>
<div class="box"><h4>THE TOP 5 MISTAKES TO WATCH</h4>1. <i>Where you live? / Who did paint it?</i> → <b>Where do you live? / Who painted it?</b> 2. <i>a bread / We don't have some</i> → <b>some bread / any</b>. 3. <i>I go to the dentist tomorrow</i> → <b>I'm going to / I'm seeing</b>. 4. <i>will to / should to / must to</i> → no <i>to</i>. 5. <i>Can you borrow me…?</i> → <b>lend</b>.</div>
<div class="box"><h4>AUDIO</h4>Track R4.1 At the airport (slow and natural) · Track R4.2 can or can't? · Track R4.3 Two dialogues</div>""")

    # Page 2: listening
    topics = [("summer clothes", True), ("the New Year's dinner", True), ("Tom's job", False), ("Buddy the robot", True), ("the beach", True), ("money", True), ("the weather in Chicago", True), ("Marcos's car", True)]
    tl = " &nbsp; ".join(f"{'☒' if (T and ok) else '☐'} {t}" for t, ok in topics)
    tf = [("Tom took a taxi from the airport.", "F: Ana met him in Marcos's car."), ("It's very cold in Chicago now.", "T: minus ten degrees."),
          ("Tom has a lot of summer clothes.", "F: he only has sweaters and a coat."), ("They need some rice for the dinner.", "T: they don't have any rice."),
          ("About twenty people are coming to dinner.", "F: about twelve."), ("Ana thinks Buddy will play cards with Grandma.", "F: probably not."),
          ("They're going to the beach on New Year's Day.", "T"), ("Ana says Tom should take taxis everywhere.", "F: he could take the subway.")]
    tfl = "".join(f"<li>{s} <b>T / F</b> {R(a)}</li>" for s, a in tf)
    b.page(f"""{sec(2, "Listening: welcome back, Tom!", "10 min")}
<p>It's December 28th. Tom is at the airport in São Paulo for New Year's, and Ana is there to meet him.</p>
{audiocard(["R4.1 · SLOW", "R4.1 · NATURAL"])}
{sub("A", "Listen. What do they talk about? Check (✓) seven topics. One topic is extra.", "3 min", "R4.1 · SLOW")}
<div class="bank" style="background:#fff;line-height:1.7">{tl}</div>
{sub("B", "Listen again. True (T) or false (F)? Correct the false sentences.", "5 min", "R4.1 · NATURAL")}
<ol>{tfl}</ol>
{sub("C", "Find one example in the conversation of each form.", "2 min")}
<table style="table-layout:fixed"><tr><td>a question with Whose / How many</td><td>{R("Whose car is this? · How many people are coming?")}</td></tr><tr><td>a plan (present continuous)</td><td>{R("We're going to the supermarket / We're making a big dinner")}</td></tr>
<tr><td>a prediction (will)</td><td>{R("Will it play cards…? · I think Grandma will win.")}</td></tr><tr><td>advice or a rule</td><td>{R("you should use sunscreen · you must wear your seat belt · You could take the subway")}</td></tr></table>""",
    18, """<p>A: extra topic = <span class="red">Tom's job</span>. B: in 8 the student must notice <i>Don't take taxis</i> = an imperative. In Brazil, everybody in a car must wear a seat belt: a real rule.</p>""")

    # Page 3: questions + quantity
    xq = [("Who did wrote this book?", "did"), ("Where do you live?", "✓"), ("What does your friend he like to drink?", "he"), ("Whose the phone is this?", "the"),
          ("Who does usually cooks dinner?", "does"), ("When did you move to São Paulo?", "✓")]
    xql = [f'<li value="{i+1}">{q} {R("→ " + a)}</li>' for i, (q, a) in enumerate(xq)]
    qn = [("I need", "a", "lemon for the cake."), ("Do we have", "any", "cheese?"), ("There's", "some", "coffee in the pot."), ("We have lots", "of", "rice."),
          ("How", "many", "oranges do we need?"), ("How", "much", "juice is there?"), ("Do we have", "an", "onion?"), ("Can I have", "a little", "milk, please?")]
    qnl = [f'<li value="{i+1}">{a} {A(g, "min-width:16mm")} {c}</li>' for i, (a, g, c) in enumerate(qn)]
    b.page(f"""{sec(3, "Grammar: questions and quantity", "8 min")}
{sub("A", "Unit 28. Some questions have an extra word. Cross it out. Two questions are correct: check them (✓).", "3 min")}
{twocol(xql, 4)}
<p class="small">Which two questions are subject questions? {R("1 (Who wrote…?) and 5 (Who usually cooks…?)")}</p>
{sub("B", "Units 30–31. Complete with a word from the box.", "4 min")}
<div class="bank">a · a little · an · any · many · much · of · some</div>
{twocol(qnl, 5)}
<div class="box sand"><h4>QUICK CHECK</h4>Countable or uncountable? bread {A("U", "min-width:8mm")} · egg {A("C", "min-width:8mm")} · money {A("U", "min-width:8mm")} · strawberry {A("C", "min-width:8mm")} · garlic {A("U", "min-width:8mm")} · banana {A("C", "min-width:8mm")}</div>""",
    26, """<ol><li>A: ask the student to say each correct question aloud with the right intonation: yes/no ↗, wh- ↘ (Unit 28).</li>
<li>B: ask <i>why?</i> for each answer: countable or uncountable, positive, negative or question.</li></ol>""")

    # Page 4: future + advice/rules
    fu = [("I think robots", "will be", "more important in the future. (be)"), ("I", "'m meeting", "Kate on Friday at 7:30. (meet)"),
          ("I", "'m going to stay", "home and watch a movie tonight. (stay)"), ("Robots probably", "won't be", "good teachers. (not be)"),
          ("We", "aren't doing", "anything on Sunday, so let's have lunch. (not do)"), ("Tom", "is flying", "to São Paulo on Monday at 9 pm. (fly)")]
    ful = [f'<li value="{i+1}">{a} {A(g, "min-width:28mm")} {c}</li>' for i, (a, g, c) in enumerate(fu)]
    ar = [("It's a good idea to go to bed early.", "You ___ go to bed early.", "should"), ("It's OK to eat your lunch here.", "You ___ eat your lunch here.", "can"),
          ("My advice: wait 30 days before you buy something.", "___ you wait 30 days before you buy something?", "Could"), ("No dictionaries during the test!", "You ___ use a dictionary.", "mustn't / can't"),
          ("It's a bad idea to buy snacks every day.", "You ___ buy snacks every day.", "shouldn't"), ("No smoking.", "___ smoke here.", "Don't")]
    arl = "".join(f"<li>{a}<br>→ {b2.replace('___', A(w, 'min-width:20mm'))}</li>" for a, b2, w in ar)
    b.page(f"""{sec(4, "Grammar: the future, advice and rules", "10 min")}
{sub("A", "Units 32–33. Complete with the present continuous, be going to or will. Use contractions.", "5 min")}
{twocol(ful, 4)}
<div class="box" style="margin-top:1mm"><b>Present continuous</b> = an arrangement (time, other people) · <b>be going to</b> = my plan · <b>will</b> = a prediction</div>
{sub("B", "Units 34–35. Complete the second sentence so it means the same. Use one word.", "5 min")}
<ol style="line-height:1.5">{arl}</ol>""",
    22, """<ol><li>A: in 3 both <i>'m staying</i> and <i>'m going to stay</i> are possible; accept both if the student explains.</li>
<li>B: in 4 <i>mustn't</i> and <i>can't</i> are both correct. Ask: <i>Is it advice or a rule?</i></li></ol>""")

    # Page 5: vocabulary
    cu = ["bread", "egg", "garlic", "money", "onion", "rice", "strawberry", "sweater", "water", "shoe"]
    pv = [("Don't throw", "away", "your old phone."), ("Can you hold", "on", "for a minute?"), ("She gave", "up", "sugar last year."), ("Don't worry", "about", "the test."),
          ("We love eating", "out", "on Fridays."), ("Fill", "up", "your bottle at home."), ("I'm meeting my brother", "on", "Saturday."), ("The meeting is", "at", "eleven o'clock.")]
    pvl = [f'<li value="{i+1}">{a} {A(g, "min-width:13mm")} {c}</li>' for i, (a, g, c) in enumerate(pv)]
    co = [("Robots will do", "housework.", "b"), ("Please stay in", "your car.", "d"), ("I'm seeing", "the dentist on Tuesday.", "a"), ("You mustn't feed", "the animals.", "c")]
    colist = "".join(f"<li>{a} {A(x, 'min-width:8mm')}</li>" for a, _, x in co)
    cor = ["the dentist on Tuesday.", "housework.", "the animals.", "your car."]
    b.page(f"""{sec(5, "Vocabulary", "8 min")}
{sub("A", "Units 29–31. Countable (C) or uncountable (U)?", "2 min")}
<div class="bank" style="background:#fff;font-weight:600">{" &nbsp; ".join(f"{w} {A('C' if w in ('egg','onion','strawberry','sweater','shoe') else 'U', 'min-width:8mm')}" for w in cu)}</div>
{sub("B", "Units 32 and 34. Complete with at, on, up, out, away or about.", "3 min")}
{twocol(pvl, 5)}
{sub("C", "Units 32–35. Match the beginnings and the endings.", "2 min")}
<div class="two"><div><ol>{colist}</ol></div><div class="small">{"".join(f"<p>{'abcd'[i]}. {x}</p>" for i, x in enumerate(cor))}</div></div>
{sub("D", "Unit 29. In a clothes store. Who says it: the sales clerk (S) or the customer (C)?", "1 min")}
<p>What size are you? {A("S", "min-width:8mm")} · Can I try it on? {A("C", "min-width:8mm")} · It suits you! {A("S", "min-width:8mm")} · It doesn't fit. {A("C", "min-width:8mm")} · How would you like to pay? {A("S", "min-width:8mm")}</p>""",
    18, """<p>A: <i>money</i> and <i>rice</i> are uncountable in English. B: phrasal verbs from Unit 34 and time prepositions from Unit 32. D: then role-play a 30-second shopping dialogue.</p>""")

    # Page 6: pronunciation + social English
    cc = "".join(f"<tr><td>{i+1}</td><td style='text-align:center'>{'☒' if (T and 't' not in s.split()[1]) else '☐'}</td><td style='text-align:center'>{'☒' if (T and 't' in s.split()[1]) else '☐'}</td></tr>" for i, s in enumerate(S42))
    d1 = [("Tom", "Excuse me. Can I prove these shorts?", "Can I try on these shorts?"), ("Clerk", "Of course. What size are you?", ""), ("Tom", "I'm medium size.", "I'm a medium."),
          ("Tom", "Hmm… they're not fit. Do you have them in a large?", "they don't fit"), ("Tom", "Perfect. How much is they?", "How much are they?"), ("Tom", "Great! I'll pay in card.", "by card")]
    d2 = [("Mia", "Can you borrow me twenty reais? I'm worried with money again.", "lend me · worried about"), ("Ana", "Sure. But you should to make coffee at home!", "should make"),
          ("Mia", "I know. And my old phone is broken.", ""), ("Ana", "Don't throw away it. You can repair it!", "Don't throw it away.")]
    def dl(rows): return "".join(f"<div><b>{n}:</b> {t} {R('→ ' + c) if c else ''}</div>" for n, t, c in rows)
    b.page(f"""{sec(6, "Pronunciation and social English", "9 min")}
{audiocard(["R4.2", "R4.3"])}
{sub("A", "Unit 35. Listen to the rules. Check can or can't for each sentence.", "3 min", "R4.2")}
<table style="table-layout:fixed;margin-top:0;width:60%"><tr><th style="width:12mm"></th><th style="text-align:center">can</th><th style="text-align:center">can't</th></tr>{cc}</table>
{sub("B", "Units 29 and 34. Each dialogue has mistakes. Correct them. Then listen and check.", "4 min", "R4.3")}
<div class="two"><div class="msg" style="max-width:none;padding:2mm 3mm;line-height:1.55"><b style="color:{TEAL}">Dialogue 1: shopping</b>{dl(d1)}</div>
<div class="msg" style="max-width:none;padding:2mm 3mm;line-height:1.55"><b style="color:{TEAL}">Dialogue 2: money</b>{dl(d2)}</div></div>
{sub("C", "Role-play the dialogues with your teacher. Then change the details and make them true for you.", "2 min")}""",
    26, """<ol><li>A: <i>can</i> is short and weak /kən/, <i>can't</i> is long and strong /kænt/. The audio pauses after each sentence: the student checks while listening. Then the student reads the sentences and you say "can" or "can't".</li>
<li>B: 5 mistakes in dialogue 1 and 4 in dialogue 2. The audio has the correct versions.</li></ol>""")

    # Page 7: reflect
    cd = [("28", "I can ask questions in the present and past, with who, whose, which…"), ("29", "I can buy clothes: sizes, colors, prices, try on and pay."),
          ("30", "I can talk about food with some, any, a / an, a lot of."), ("31", "I can ask about quantity: how much, how many, a few, a little."),
          ("32", "I can talk about plans and arrangements."), ("33", "I can make predictions with will / won't."),
          ("34", "I can give advice with should, could and imperatives."), ("35", "I can explain rules with must, mustn't, can and can't.")]
    cdr = "".join(f"<tr><td><b>Unit {u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in cd)
    b.page(f"""{sec(7, "Reflect and homework", "5 min")}
{sub("A", "How are you doing? Check one box for each line.", "2 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{cdr}</table>
{sub("B", "My goals. What do you want to practice more? Write two things.", "2 min")}
<div class="wline"></div><div class="wline"></div>
{sub("C", "Homework", "1 min")}
<p><b>A message to Tom.</b> Tom is visiting your city next month. Write him a message (70–90 words). Include:</p>
<ol><li>two questions for Tom;</li><li>your plans for his first weekend (present continuous / going to);</li><li>a prediction about the weather or the trip (will);</li><li>two pieces of advice and one rule for visitors in your city.</li></ol>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Look at the "Not yet" lines and plan two short review activities for the next classes. The homework uses all the grammar of Units 28–35: correct it carefully and keep it as a writing sample.</p>""")

    b.extra("Audio scripts", f"""
{sub("R4.1", "At the airport (slow and natural)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("R4.2", "can or can't? (3-second pause after each sentence)")}
<p>{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S42))}</p>
{sub("R4.3", "Two dialogues (correct versions)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in S43)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essentials 36 - Review 4")
