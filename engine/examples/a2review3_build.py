# Speak! Bridge A2 - Review 3 (Units 21-29), all English - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
_se.SERIES = "Bridge"
setup(band="A2 · REVIEW 3", audio_json="audio_a2-review-3.json", img_dir="img")

PHOTOS = [("A", "a tortoise", "Unit 21"), ("B", "an animal shelter", "Unit 22"), ("C", "a trophy", "Unit 23"), ("D", "a remote control", "Unit 25"),
          ("E", "drums", "Unit 26"), ("F", "black coffee", "Unit 27"), ("G", "an ice cream cone", "Unit 28"), ("H", "an overhead bin", "Unit 29")]

_r = json.load(open("roteiro.json"))["units"]["a2-review-3"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["R3.1 A goodbye dinner for Ana"].split("\n")]
S32 = [x.split(": ", 1)[1] for x in _r["R3.2 Word stress"].split("\n")][1:]
S33 = [tuple(x.split(": ", 1)) for x in _r["R3.3 Dialogues"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LEVEL A2 · REVIEW 3", "Review 3", "Units 21–29 · stories in the past · used to · if I… · adjectives · comparing · adverbs",
                       [("YOU CAN", "check what you learned in Units 21–29 and plan what to practice"),
                        ("LANGUAGE", "While I was… · I used to… · If I lived…, I'd… · bored / boring · a bit, too · much bigger · probably"),
                        ("PRONUNCIATION", "word stress: ANxious · poLITE · GENerous · disHONest")])
    b.page(f"""{sec(1, "Warm-up: photo memory", "5 min")}
{sub("A", "One photo from each unit. Write the word or phrase. Then say one sentence about it with the grammar of that unit.", "5 min")}
<div class="bank">an animal shelter · black coffee · drums · an ice cream cone · an overhead bin · a remote control · a tortoise · a trophy</div>
{photo_grid(T, PHOTOS)}
<p class="small" style="margin-top:2mm"><b>Example:</b> a tortoise → <i>While the hare was sleeping, the tortoise was walking to the finish line.</i></p>""",
    20, """<p>Photos A–H come from Units 21–29 in order (Unit 24, story writing, has no photo here). Push each unit's grammar: past continuous (21), <i>used to</i> (22), second conditional (23), -ed / -ing adjectives (25), modifiers (26), comparatives (27), adverbs (28), airport requests (29).</p>""", cover=cover)

    b.extra("Review overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Units</th><th>SB page</th></tr>
<tr><td>1 Warm-up: photo memory</td><td>5 min</td><td>21–29</td><td>1</td></tr>
<tr><td>2 Listening: a goodbye dinner for Ana</td><td>10 min</td><td>21–29</td><td>2</td></tr>
<tr><td>3 Grammar: past continuous, used to, second conditional</td><td>9 min</td><td>21, 22, 23</td><td>3</td></tr>
<tr><td>4 Grammar: adjectives, modifiers, comparatives, adverbs</td><td>9 min</td><td>25–28</td><td>4</td></tr>
<tr><td>5 Vocabulary and story writing</td><td>8 min</td><td>22–29</td><td>5</td></tr>
<tr><td>6 Pronunciation and social English</td><td>9 min</td><td>25–29</td><td>6</td></tr>
<tr><td>7 Reflect and homework</td><td>5 min</td><td>21–29</td><td>7</td></tr></table>
<div class="box"><h4>HOW THIS GUIDE WORKS</h4>Every page looks like the Student Book page with the same number. Your notes are in the <b>yellow box</b>; <span class="red">answers in red</span> are not in the Student Book. This is a review: don't teach everything again. Let the student work, then focus on the mistakes that come back. The grammar reference pages (page 4) of Units 21–29 are useful here.</div>
<div class="box sand"><h4>THE STORY SO FAR</h4>Saturday evening in Chicago. Ana, Tom's online student from Brazil, is flying home tomorrow (Unit 29), so Tom, Lucy and Kate have a goodbye dinner for her at Tom and Lucy's apartment. Kate brings Pepper, the dog she adopted (Unit 22), who steals the chicken. Ana remembers her childhood dog Mel (Unit 24), talks about the Cubs game (Unit 23) and Chicago pizza (Unit 27), and tries Kate's new coffee ice cream (Units 27–28). Tom describes Priya, the new roommate (Unit 26), and Ana almost gives away the ending of <i>Kingdom of Fire</i> (Unit 25). No new facts: the story only uses what the students know from Units 21–29.</div>
<div class="box"><h4>THE TOP 5 MISTAKES TO WATCH</h4>1. <i>While I walked, I was seeing a dog</i> → <b>While I was walking, I saw a dog</b>. 2. <i>I use to play / I used to living</i> → <b>I used to play</b>. 3. <i>If I would have money, I will travel</i> → <b>If I had money, I'd travel</b>. 4. <i>I'm boring / too beautiful / more better</i> → <b>I'm bored / really beautiful / much better</b>. 5. <i>I like very much pizza / I drink always coffee</i> → <b>I like pizza very much / I always drink coffee</b>.</div>
<div class="box"><h4>AUDIO</h4>Track R3.1 A goodbye dinner for Ana (slow and natural) · Track R3.2 Word stress · Track R3.3 Two dialogues</div>""")

    # Page 2
    topics = [("a dog", True), ("a baseball game", True), ("pizza", True), ("a birthday cake", False), ("ice cream", True), ("a new roommate", True), ("a TV show", True), ("a flight", True)]
    tl = " &nbsp; ".join(f"☐ {t}{(' ' + R('✓')) if ok else ''}" for t, ok in topics)
    tf = [("Ana used to be scared of dogs.", "T"), ("Pepper ate the dessert.", "F: she stole the chicken."),
          ("Ana thinks deep-dish pizza is the best.", "F: Brazilian pizza is the best."), ("Kate's ice cream is made with black coffee.", "T"),
          ("Priya spends a lot of time at the library.", "T: she's always there."), ("Tom has already seen Kingdom of Fire.", "F: he hasn't seen it yet.")]
    tfl = [f'<li value="{i+1}">{s} <b>T / F</b> {R(a)}</li>' for i, (s, a) in enumerate(tf)]
    find = [("past continuous + past simple (Unit 21)", "While we were talking, she was stealing our dinner! / When the princess said…, I screamed."),
            ("used to (Unit 22)", "I used to be scared of dogs. / Pepper used to be really shy."),
            ("a second conditional (Unit 23)", "If I lived here, I'd go to every game!"),
            ("direct speech (Unit 24)", "When the princess said, \"I'm your sister!\", I screamed!"),
            ("an -ed adjective (Unit 25)", "scared / shocked"), ("a modifier (Unit 26)", "so cute / really shy / a little too busy"),
            ("a comparative or superlative (Unit 27)", "much bigger / a lot heavier / a bit stronger / the best"),
            ("an adverb of certainty or manner (Unit 28)", "definitely / probably / carefully")]
    fl = "".join(f"<li>{x} {R(y)}</li>" for x, y in find)
    b.page(f"""{sec(2, "Listening: a goodbye dinner for Ana", "10 min")}
<p>It's Ana's last night in Chicago. Tom, Lucy and Kate are having a goodbye dinner for her.</p>
{audiocard(["R3.1 · SLOW", "R3.1 · NATURAL"])}
{sub("A", "Listen. What do they talk about? Check (✓) seven topics. One topic is extra.", "2 min", "R3.1 · SLOW")}
<p style="font-weight:600">{tl}</p>
{sub("B", "Listen again. True (T) or false (F)? Correct the false sentences.", "4 min", "R3.1 · NATURAL")}
{twocol(tfl, 4)}
{sub("C", "Find one example in the conversation of each form.", "4 min")}
<ol style="font-size:9pt">{fl}</ol>""",
    22, """<p>A: the extra topic is <i>a birthday cake</i>. C: let the student read the script (TB last page) or play the natural version again and pause. Ask: <i>What would you show a visitor in your city?</i></p>""")

    # Page 3
    pc = [("While the hare", "was sleeping", ", the tortoise", "passed", "him. (sleep / pass)"),
          ("I", "was walking", "down the street when I", "saw", "a strange dog. (walk / see)"),
          ("What", "were you doing", "when the phone", "rang", "? (you / do / ring)"),
          ("Pepper", "was stealing", "the chicken while we", "were talking", ". (steal / talk)")]
    pcl = "".join(f"<li>{a} {A(v1, 'min-width:20mm')}{'' if m[0] in ',' else ' '}{m} {A(v2, 'min-width:16mm')}{'' if e[0] in '.?' else ' '}{e}</li>" for a, v1, m, v2, e in pc)
    ut = [("When I was a child, I", "used to be", "scared of dogs. (be)"), ("Pepper", "didn't use to", "like other dogs. (not like)"),
          ("", "Did you use to", "have a pet? (you / have)"), ("Kate", "used to work", "in an office before the bakery. (work)")]
    utl = "".join(f"<li>{a} {A(v, 'min-width:22mm')} {e}</li>" for a, v, e in ut)
    sc = [("If I", "lived", "in Chicago, I", "would go", "to every Cubs game. (live / go)"),
          ("If the Cubs", "won", "more often, Tom", "would be", "happier. (win / be)"),
          ("What", "would you do", "if you", "found", "a dog in the street? (you / do / find)"),
          ("I", "wouldn't buy", "a pet if I", "didn't have", "time for it. (not buy / not have)")]
    scl = "".join(f"<li>{a} {A(v1, 'min-width:18mm')} {m} {A(v2, 'min-width:18mm')} {e}</li>" for a, v1, m, v2, e in sc)
    b.page(f"""{sec(3, "Grammar: past continuous, used to, second conditional", "9 min")}
{sub("A", "Unit 21. Complete with the past continuous or the past simple.", "3 min")}
<ol style="line-height:1.7">{pcl}</ol>
{sub("B", "Unit 22. Complete with the correct form of used to.", "3 min")}
<ol style="line-height:1.7">{utl}</ol>
{sub("C", "Unit 23. Complete the second conditionals.", "3 min")}
<ol style="line-height:1.7">{scl}</ol>
<div class="box sand"><h4>REMEMBER</h4><b>was / were + -ing</b> = the longer action; <b>past simple</b> = the short action that interrupts it. <b>used to + base form</b> (negative and questions: <b>use to</b>). Second conditional: <b>if + past</b>, <b>would + base form</b>: never <i>would</i> after <i>if</i>.</div>""",
    22, """<ol><li>A: draw a timeline: the long action is a line, the interruption is a cross. B: <i>didn't use to</i>, <i>Did you use to…?</i> (no -d).</li>
<li>C: ask a personal follow-up: <i>If you lived in the US, which city would you choose?</i></li></ol>""")

    # Page 4
    ei = [(["bored", "boring"], "bored", "I'm", "! Let's go out."), (["interested", "interesting"], "interested", "Are you", "in history?"),
          (["shocked", "shocking"], "shocking", "The ending of the show was really", "."), (["scared", "scary"], "scary", "That was a", "movie!")]
    eil = [f'<li value="{i+1}">{a} {ch(o, r)}{e if e[0] in "!." else " " + e}</li>' for i, (o, r, a, e) in enumerate(ei)]
    md = [(["a bit", "too"], "too", "He's", "shy to share an apartment. It's a problem."), (["really", "a little"], "really", "Priya is", "smart."),
          (["a bit", "really"], "a bit", "Sam is", "miserable. He never smiles."), (["seems", "seems like"], "seems like", "She", "a nice person.")]
    mdl = [f'<li value="{i+1}">{a} {ch(o, r)} {e}</li>' for i, (o, r, a, e) in enumerate(md)]
    cs = [("Black coffee is", "much stronger", "than a latte. (strong, big difference)"), ("I'm", "a bit more patient", "than my brother. (patient, small difference)"),
          ("Brazilian pizza is", "the best", "pizza in the world! (good)"), ("Pepper is", "the friendliest", "dog in the park. (friendly)")]
    csl = "".join(f"<li>{a} {A(w, 'min-width:28mm')} {e}</li>" for a, w, e in cs)
    ad = [("I drink always coffee in the morning.", "I always drink coffee in the morning."), ("She's going to probably sell ice cream.", "She's probably going to sell ice cream."),
          ("I like very much Chicago.", "I like Chicago very much."), ("He cooks very good.", "He cooks very well.")]
    adl = "".join(f"<li>{x}<br>{A(y, 'min-width:80mm')}</li>" for x, y in ad)
    b.page(f"""{sec(4, "Grammar: adjectives, modifiers, comparatives, adverbs", "9 min")}
<div class="two"><div>{sub("A", "Unit 25. Choose the correct adjective.", "2 min")}
<ol style="line-height:1.6;margin:0">{"".join(eil)}</ol></div>
<div>{sub("B", "Unit 26. Choose the correct option.", "2 min")}
<ol style="line-height:1.6;margin:0">{"".join(mdl)}</ol></div></div>
{sub("C", "Unit 27. Complete with a comparative or superlative. Add a modifier if you need to.", "3 min")}
<ol style="line-height:1.7">{csl}</ol>
{sub("D", "Unit 28. Each sentence has a mistake with an adverb. Write it correctly.", "2 min")}
<ol style="line-height:1.4;font-size:9pt">{adl}</ol>
<div class="box sand"><h4>REMEMBER</h4><b>-ed</b> = feelings, <b>-ing</b> = the cause · <b>too</b> = a problem · <b>much / a lot</b> = big difference · frequency adverbs <b>before</b> the main verb, never between a verb and its object.</div>""",
    22, """<ol><li>A–B: insist on the reason: <i>Who feels bored? Is it a problem?</i> C: in 2, <i>a little / slightly more patient</i> are also correct.</li>
<li>D: these are the most common Brazilian word-order mistakes. Ask the student to say each correct sentence twice, quickly.</li></ol>""")

    # Page 5
    vc = [("an animal that lives in your home", "a pet"), ("a place where homeless animals wait for a new owner", "a shelter"),
          ("the people who support a team", "fans"), ("a TV show where people compete for money", "a game show"),
          ("a person who shares your apartment", "a roommate"), ("happy to give your time or money to others", "generous"),
          ("the number of balls of ice cream", "scoops"), ("the seat next to the walkway on a plane", "an aisle seat")]
    b.page(f"""{sec(5, "Vocabulary and story writing", "8 min")}
{sub("A", "Units 22–29. Write the word or phrase.", "4 min")}
<div class="bank">an aisle seat · fans · a game show · generous · a pet · a roommate · scoops · a shelter</div>
{twocol([f'<li value="{i+1}">{d} → {A(w, "min-width:22mm")}</li>' for i, (d, w) in enumerate(vc)], 5)}
{sub("B", "Unit 24. Correct the punctuation in this direct speech. Add quotation marks, commas, capital letters and question marks.", "4 min")}
<div class="msg" style="max-width:none;padding:2mm 3mm;font-size:9.4pt;line-height:1.6">ana looked at pepper and said you're so cute<br>where did you find her she asked<br>at the animal shelter kate answered</div>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>
<p class="small" style="margin:0">{R('Ana looked at Pepper and said, "You\'re so cute!" / "Where did you find her?" she asked. / "At the animal shelter," Kate answered.')}</p>""",
    22, """<ol><li>A: after each word, ask a personal question: <i>Have you ever had a pet? Are you a generous person?</i></li>
<li>B: American English puts the comma and the period <b>inside</b> the quotation marks: <i>"At the animal shelter," Kate answered.</i></li></ol>""")

    # Page 6
    stress = {"Oo": "anxious, chocolate", "oO": "polite, relaxed", "Ooo": "comfortable, generous, interesting", "oOo": "dishonest, excited"}
    stt = "".join(f"<td style='height:14mm;vertical-align:top'><b>{k}</b><br>{R(v)}</td>" for k, v in stress.items())
    d1 = [("Agent", "Good afternoon. Where <u>you are flying</u> today?"), ("Ana", "To São Paulo."), ("Agent", "May I see your passport, please?"),
          ("Ana", "<u>Here is.</u>"), ("Agent", "Thank you. Place your bag on the scale, please."), ("Ana", "<u>Give me</u> a window seat, please."),
          ("Agent", "Sure. Here's your boarding pass. Your gate is M12."), ("Ana", "<u>What?</u> Which gate?"), ("Agent", "M12. Have a good flight!")]
    d2 = [("Lucy", "Did you watch Fix My House last night?"), ("Kate", "Yes! I was really <u>interesting</u> in the new kitchen."),
          ("Lucy", "Me too. But the show was a bit <u>bored</u> this week."), ("Kate", "I know. I <u>watch always</u> it, but last week's show was <u>more better</u>."),
          ("Lucy", "Yes! It was <u>the more good</u> show of the year.")]
    def dlg(lines):
        return "<br>".join(f"<b>{n}:</b> {t}" for n, t in lines)
    b.page(f"""{sec(6, "Pronunciation and social English", "9 min")}
{audiocard(["R3.2", "R3.3"])}
{sub("A", "Units 26–28. Listen to the words. Write each word in the correct stress column. O = stressed syllable.", "3 min", "R3.2")}
<div class="bank">anxious · chocolate · comfortable · dishonest · excited · generous · interesting · polite · relaxed</div>
<table style="table-layout:fixed;margin-top:0"><tr>{stt}</tr></table>
{sub("B", "Units 25–29. Each dialogue has mistakes (underlined). Correct them. Then listen and check.", "4 min", "R3.3")}
<div class="two"><div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.8pt;line-height:1.5"><b>Dialogue 1</b><br>{dlg(d1)}</div>
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.8pt;line-height:1.5"><b>Dialogue 2</b><br>{dlg(d2)}</div></div>
<p class="small">{R("1: Where are you flying to · Here you are. · Could I have · Sorry, which gate? — 2: interested in · boring · always watch it · much better · the best")}</p>
{sub("C", "Role-play the dialogues with your teacher. Then change roles: your teacher is the passenger and you are the agent.", "2 min")}""",
    30, """<ol><li>A: 3-second pause after each word. <i>Chocolate</i> and <i>comfortable</i> have hidden syllables (Unit 28): CHOC-lit, COMF-tuh-bul.</li>
<li>B: Dialogue 1 also practices intonation: rising for <i>May I see…?</i> and <i>Could I have…?</i>, falling for <i>Where…?</i> and <i>Which gate?</i></li></ol>""")

    # Page 7
    ck = [("21", "I can tell a story in the past with the past continuous and the past simple."), ("22", "I can talk about past habits and states with used to."),
          ("23", "I can imagine a different situation with the second conditional."), ("24", "I can plan and write a short story with direct speech."),
          ("25", "I can talk about TV shows with -ed and -ing adjectives."), ("26", "I can describe people's personalities with modifiers."),
          ("27", "I can compare people and things with comparatives and superlatives."), ("28", "I can use adverbs in the correct position."),
          ("29", "I can check in, go through security and understand announcements on a plane.")]
    ckr = "".join(f"<tr><td><b>Unit {u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in ck)
    b.page(f"""{sec(7, "Reflect and homework", "5 min")}
{sub("A", "How are you doing? Check one box for each line.", "2 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{ckr}</table>
{sub("B", "My goals. What do you want to practice more? Write two things.", "2 min")}
<div class="wline"></div><div class="wline"></div>
{sub("C", "Homework", "1 min")}
<p><b>A story: "The day I met a special animal" (80–100 words).</b> It can be true or invented. Include:</p>
<ol><li>the past continuous and the past simple (<i>I was walking… when I saw…</i>) (Unit 21);</li><li>something you used to do or believe (Unit 22);</li>
<li>one line of direct speech with correct punctuation (Unit 24);</li><li>two adjectives with a modifier and one comparative (Units 25–27).</li></ol>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Look at the "Not yet" lines and plan two short review activities for the next classes. The homework uses grammar from all nine units: keep it next to the Review 2 email. Next: Unit 31.</p>""")

    b.extra("Audio scripts", f"""
{sub("R3.1", "A goodbye dinner for Ana (slow and natural)")}
<p style="line-height:1.32;font-size:8.6pt">{"<br>".join(f"<b>{n}:</b> {t}" if n != "Narrator" else f"<i>{t}</i>" for n, t in SCRIPT)}</p>
{sub("R3.2", "Word stress (3-second pause after each word)")}
<p>{" · ".join(S32)}</p>
{sub("R3.3", "Two dialogues (correct versions)")}
<p style="line-height:1.32;font-size:8.6pt">{"<br>".join(f"<b>{n}:</b> {t}" if n != "Narrator" else f"<i>{t}</i>" for n, t in S33)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 30 - Review 3")
