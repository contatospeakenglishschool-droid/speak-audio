# Speak! Essentials A1 - Unit 26 "Weekends" (all English) - built with the shared engine
import sys, json
sys.path.insert(0, "/home/claude/speak-audio/engine")
from speak_engine import *
setup(band="A1 · UNIT 26", audio_json="audio_a1-unit-26.json", img_dir="img")

PHOTOS = [("A", "buy new clothes", "shopping"), ("B", "eat pizza", "pizza"), ("C", "get up late", "get up late"), ("D", "go dancing", "dancing"),
          ("E", "go to a restaurant", "restaurant"), ("F", "meet friends", "friends"), ("G", "read a book", "book"), ("H", "watch a movie", "movie")]

_r = json.load(open("roteiro.json"))["units"]["a1-unit-26"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["26.1 Monday"].split("\n")]
S262 = [x.split(": ", 1)[1] for x in _r["26.2 Repeat verbs"].split("\n")]
S263 = [x.split(": ", 1)[1] for x in _r["26.3 Repeat sentences"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LEVEL A1 · UNIT 26", "Weekends", "Free time · <b>past simple: irregular verbs</b>",
                       [("YOU CAN", "talk about your weekend and ask about someone else's"),
                        ("LANGUAGE", "I went to a pizzeria. · We ate a lot. · Did you have a good time?"),
                        ("PRONUNCIATION", "go → went · see → saw · read /red/ · felt ≠ fell")])
    words = ["buy new clothes", "eat pizza", "get up late", "go dancing", "go to a restaurant", "meet friends", "read a book", "watch a movie"]
    b.page(f"""{sec(1, "Warm-up: weekend activities", "8 min")}
{sub("A", "Look, listen and repeat. Then write the activity under the photo.", "3 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Talk about it.", "5 min")}
<ol><li>Which three activities do you enjoy most on the weekend?</li><li>What other things do people do on the weekend in Brazil?</li><li>Do you prefer a quiet weekend or a busy weekend?</li></ol>""",
    20, """<ol><li>A: <b>get up late</b> = get out of bed late. <b>go dancing</b> = go to a club or a party to dance.</li>
<li>B: ideas: <i>go to the beach, have a barbecue, watch soccer, visit family</i>.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>8 weekend activities with photos</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Monday morning: Ana and Mia talk about their weekends</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Past simple of 14 common irregular verbs · questions and negatives</td><td>3</td></tr>
<tr><td>4 Pronunciation lab</td><td>5 min</td><td>Base form → past · read /red/ · feel/felt × fall/fell</td><td>4</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Lucy's terrible weekend</td><td>5</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Great, terrible or crazy weekend? · your real weekend</td><td>6</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>7</td></tr></table>
<div class="box"><h4>HOW THIS GUIDE WORKS</h4>Every page looks like the Student Book page with the same number. Your notes are in the <b>yellow box</b>.
<span class="red">Answers in red</span> are not in the Student Book. The <span class="time">5 min</span> chips show the time for each activity. Audio scripts are on the last page.</div>
<div class="box sand"><h4>THE STORY CONTINUES</h4>It's Monday morning at the hospital in São Paulo. Ana and her colleague Mia (the night nurse) have a coffee before work. Mia bought new shoes, saw a Brazilian comedy and went home early. Ana went to a pizzeria with Marcos and Leo, ate too much and got up at noon. In Chicago, Lucy had a terrible weekend (page 5). Homework: Paulo's crazy weekend… or was it a dream?</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Adding -ed to irregular verbs: <i>I goed / buyed / eated</i> ✗ → <b>went / bought / ate</b>. Using the past after <i>did</i>: <i>Did you went?</i> ✗ → <b>Did you go?</b> <i>I didn't saw</i> ✗ → <b>I didn't see</b>. And <i>read</i> in the past sounds like <i>red</i>.</div>
<div class="box"><h4>AUDIO</h4>Track 26.1 Monday morning (slow and natural) · Track 26.2 Irregular verbs · Track 26.3 Sentences</div>""")

    # Page 2
    who = [("bought new shoes", "Mia"), ("ate pizza", "Ana"), ("got up late", "Ana"), ("went out on Saturday night", "both"), ("read a book", "Mia"), ("saw a movie", "Mia")]
    wr = "".join(f"<tr><td>{i+1}. {a}</td><td style='text-align:center'>{'☒' if T and w == 'Mia' else '☐'}</td><td style='text-align:center'>{'☒' if T and w == 'Ana' else '☐'}</td><td style='text-align:center'>{'☒' if T and w == 'both' else '☐'}</td></tr>" for i, (a, w) in enumerate(who))
    det = [(["R$ 170", "R$ 270"], "R$ 170", "Mia's new shoes cost"), (["Brazilian", "American"], "Brazilian", "Mia and her friends saw a"),
           (["an Uber", "the bus"], "an Uber", "Mia took"), (["Marcos", "Ana"], "Marcos", "After the pizzeria,"),
           (["11", "12"], "12", "On Sunday, Ana got up at about"), (["tea", "coffee"], "coffee", "Ana felt better after she drank some")]
    dl = [f'<li value="{i+1}">{s} {ch(o, r)}{" comedy." if i == 1 else (" home." if i == 2 else (" drove home." if i == 3 else (" o’clock." if i == 4 else ".")))}</li>' for i, (o, r, s) in enumerate(det)]
    b.page(f"""{sec(2, "Listening: Monday morning", "10 min")}
<p>It's Monday morning at the hospital in São Paulo. Ana and her colleague Mia are having coffee before work. They're talking about the weekend.</p>
{audiocard(["26.1 · SLOW", "26.1 · NATURAL"])}
{sub("A", "Listen. Who did each thing: Mia, Ana or both?", "4 min", "26.1 · SLOW")}
<table class="ck" style="table-layout:fixed"><tr><th></th><th style="width:22mm">Mia</th><th style="width:22mm">Ana</th><th style="width:22mm">both</th></tr>{wr}</table>
{sub("B", "Listen again and choose the correct option.", "4 min", "26.1 · NATURAL")}
{twocol(dl, 4)}
{sub("C", "Why didn't Mia go dancing with her friends?", "2 min")}
<div class="wline">{R("Because she was really tired.")}</div>""",
    22, """<ol><li>A: <b>slow</b> version. Item 4: Mia went to the movies and Ana went to a pizzeria. <b>reais</b> /reˈaɪs/.</li>
<li>B: <b>natural</b> version. Then ask: <i>Which weekend was better, Mia's or Ana's?</i></li></ol>""")

    # Page 3
    verbs = [("buy", "bought", True), ("cost", "cost", True), ("do", "did", True), ("drink", "drank", False), ("drive", "drove", False),
             ("eat", "ate", False), ("feel", "felt", False), ("get up", "got up", False), ("go", "went", False), ("have", "had", False),
             ("meet", "met", True), ("read", "read /red/", False), ("see", "saw", False), ("take", "took", False)]
    def vrow(v, p, given):
        return f"<tr><td>{v}</td><td>{('<b>' + p + '</b>') if given else A(p, 'min-width:24mm')}</td></tr>"
    h = len(verbs) // 2
    t1 = "".join(vrow(*x) for x in verbs[:h]); t2 = "".join(vrow(*x) for x in verbs[h:])
    th = "<tr><th>Base form</th><th>Past simple</th></tr>"
    b.page(f"""{sec(3, "Language focus: irregular verbs", "10 min")}
{sub("A", "Read the sentences from the conversation.", "1 min")}
<div class="bank" style="background:#fff;font-weight:600">On Saturday I <u>bought</u> these new shoes. · They <u>cost</u> a hundred and seventy reais. · I <u>met</u> my friends at the movie theater.</div>
<div class="box" style="margin-top:0"><h4>IRREGULAR VERBS</h4>Regular verbs add <b>-ed</b> (work → work<b>ed</b>). Many common verbs are <b>irregular</b>: they have a special past form, and you need to learn it. buy → <b>bought</b>, meet → <b>met</b>.</div>
{sub("B", "Complete the table. Use the audio script or your memory.", "4 min")}
<div class="two"><div><table style="margin:0">{th}{t1}</table></div><div><table style="margin:0">{th}{t2}</table></div></div>
{sub("C", "Answer the questions.", "2 min")}
<ol><li>Which two verbs have the same spelling in the base form and the past? {R("cost, read")}</li>
<li>Which verb changes the most? {R("go → went")}</li></ol>
<div class="box sand"><h4>QUESTIONS AND NEGATIVES</h4>Same as regular verbs: <b>did / didn't + base form</b>.<br>
What movie <b>did</b> you <b>see</b>? · <b>Did</b> you <b>have</b> a good time? · I <b>didn't go</b> with them. · No, I <b>didn't drive</b>.</div>""",
    25, """<ol><li>B: test the student: you say the base form, the student says the past, then change roles.</li>
<li>C: <i>read</i> has the same spelling but a different sound: /riːd/ → /red/. Remind the student of Unit 25: after <i>did</i>, no past form.</li></ol>""")

    # Page 4
    pairs = [x.split(", ") for x in S262]
    pt = "".join(f"<td style='text-align:center'>{a}<br><b>{p}</b></td>" for a, p in pairs[:6])
    pt2 = "".join(f"<td style='text-align:center'>{a}<br><b>{p}</b></td>" for a, p in pairs[6:])
    b.page(f"""{sub("D", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>I goed to a pizzeria.</td><td><b>I went to a pizzeria.</b></td><td>Irregular: no <i>-ed</i>.</td></tr>
<tr><td>She buyed new shoes.</td><td><b>She bought new shoes.</b></td><td>buy → bought.</td></tr>
<tr><td>Did you went out?</td><td><b>Did you go out?</b></td><td>After <i>did</i>: base form.</td></tr>
<tr><td>I didn't saw the movie.</td><td><b>I didn't see the movie.</b></td><td>After <i>didn't</i>: base form.</td></tr>
<tr><td>I readed a book. /riːd/</td><td><b>I read a book. /red/</b></td><td>Same spelling, new sound.</td></tr>
<tr><td>I felt from my bike.</td><td><b>I fell off my bike.</b></td><td>fall → <i>fell</i>; feel → <i>felt</i>.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "5 min")}
{audiocard(["26.2", "26.3"])}
{sub("A", "Irregular verbs. Listen and repeat.", "2 min", "26.2")}
<table style="table-layout:fixed;margin-top:0;font-size:9pt"><tr>{pt}</tr><tr>{pt2}</tr></table>
{sub("B", "Sentences. Listen and repeat.", "2 min", "26.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S263)}</div>
<div class="box" style="margin-top:1mm"><h4>FEEL OR FALL?</h4><b>feel → felt</b>: I felt tired. I felt great. &nbsp;·&nbsp; <b>fall → fell</b>: He fell off his bike. She fell down the stairs.</div>""",
    26, """<ol><li>4A: <b>bought</b> /bɔt/: the <i>gh</i> is silent. <b>ate</b> /eɪt/ sounds like <i>eight</i>. <b>read</b> /red/ sounds like the color.</li>
<li>Fast drill: you say the base form, the student says the past, without looking.</li></ol>""")

    # Page 5
    gaps = ["went", "bought", "cost", "got", "saw", "took", "saw", "got", "drank", "felt", "drove", "had", "ate"]
    def g(i): return f"({i+1}) {A(gaps[i], 'min-width:18mm')}"
    story = (f"Lucy {g(0)} shopping on Saturday. She {g(1)} a new coat. It {g(2)} two hundred dollars! But when she {g(3)} home, "
             f"she {g(4)} that the zipper was broken. So she {g(5)} the coat back to the store. On Saturday night, Lucy {g(6)} a scary movie on TV, "
             f"and she didn't sleep well. On Sunday she {g(7)} up late, and then she {g(8)} too much coffee. She {g(9)} terrible. "
             f"Then she {g(10)} to the next town. She {g(11)} a lunch date with her boyfriend, but he was late, so she {g(12)} alone.")
    qs = [("go shopping on Saturday?", "Yes, she did."), ("What / buy?", "She bought a new coat."), ("watch a funny movie?", "No, she didn't. She saw a scary movie."), ("Why / eat alone?", "Because her boyfriend was late.")]
    ql = "".join(f'<li>{("Did Lucy " + q) if "/" not in q else (q.split(" / ")[0] + " did Lucy " + q.split(" / ")[1])} {R("→ " + a)}</li>' for q, a in qs)
    b.page(f"""{sec(5, "Practice", "8 min")}
{sub("A", "Lucy had a terrible weekend in Chicago. Complete with the past simple of the verbs.", "6 min")}
<div class="bank">buy · cost · drink · drive · eat · feel · get (×2) · go · have · see (×2) · take</div>
<div class="msg" style="max-width:none;line-height:2.05;padding:2mm 4mm">{story}</div>
{sub("B", "Ask your teacher about Lucy's weekend. Your teacher answers.", "2 min")}
<ol style="line-height:1.7">{ql}</ol>
<p class="small">What was the worst thing about Lucy's weekend?</p>""",
    18, """<p>A: Lucy is the weekend barista at City Coffee, so <i>she drank too much coffee</i> is a joke! <b>zipper</b>: show one on a jacket. B: the student makes the questions with <b>did + base form</b>; you answer.</p>""")

    # Page 6
    rows = [("go", "I went to the beach with my friends.", "", ""), ("eat", "", "", "I ate twenty doughnuts."), ("see", "", "", "I saw a pink horse."),
            ("buy", "", "", ""), ("feel", "", "", ""), ("get up", "", "", ""), ("meet", "", "", ""), ("take", "", "", "")]
    rt = "".join(f"<tr><td><b>{v}</b></td><td class='small'>{a}</td><td class='small'>{t}</td><td class='small'>{c}</td></tr>" for v, a, t, c in rows)
    b.page(f"""{sec(6, "Speaking", "12 min")}
{sub("A", "Great, terrible or crazy? Write 5 sentences in the table. Use the past simple. Then read one sentence. Your teacher guesses what kind of weekend you had and asks a question.", "7 min")}
<table style="table-layout:fixed"><tr><th style="width:18mm">verb</th><th>a great weekend</th><th>a terrible weekend</th><th>a crazy weekend</th></tr>{rt}</table>
<div class="msg" style="max-width:none;padding:2mm 4mm;line-height:1.55"><b>You:</b> I ate twenty doughnuts.<br><b>Teacher:</b> Really? I think you had a crazy weekend. Did you feel sick?<br><b>You:</b> Yes, I did! I felt very sick. Next one: I went to the beach with my friends.<br><b>Teacher:</b> You had a great weekend!</div>
{sub("B", "Your real weekend. Answer your teacher's questions.", "5 min")}
<ol><li>What did you do on Saturday? Did you go out?</li><li>What did you eat? Did you go to a restaurant?</li><li>What time did you get up on Sunday? How did you feel?</li><li>Did you see a movie or read a book? Was it good?</li></ol>""",
    25, """<ol><li>A: the student doesn't show you the table. Guess, react (<i>Really? No way!</i>) and ask one question with <i>did</i>. Then you read some sentences too.</li>
<li>B: ask follow-up questions. Correct <i>goed / buyed</i> and <i>Did you went</i>.</li></ol>""")

    # Page 7
    pc = [("Unit 22", "I can talk about transportation and my plans."), ("Unit 23", "I can use was / were and say when I was born."),
          ("Unit 24", "I can say -ed correctly: played, worked, started."), ("Unit 25", "I can make past questions and negatives with did / didn't."),
          ("Unit 26", "I can use irregular past verbs: went, ate, saw, bought.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [(["drove", "drave", "droves"], "drove"), (["mit", "met", "meeted"], "met"), (["sew", "seed", "saw"], "saw"), (["want", "goed", "went"], "went"),
          (["doed", "did", "had"], "did"), (["felt", "feel", "fell"], "felt"), (["haved", "had", "has"], "had"), (["ated", "eated", "ate"], "ate"), (["toke", "tooked", "took"], "took")]
    def h(i): return f"({i+1}) {ch(*hw[i])}"
    msg = (f"Paulo had a crazy weekend. He {h(0)} to the beach in a pink car. At the beach, he {h(1)} a famous singer, and they {h(2)} a dinosaur! "
           f"Then they {h(3)} to the gym together and {h(4)} some yoga. After the class, they {h(5)} great, so they {h(6)} an ice cream on the beach. "
           f"In fact, Paulo {h(7)} two ice creams. Then he {h(8)} a taxi home. The next morning, he said: \"What a crazy weekend! Or was it a dream?\"")
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:15mm"></th><th>In English…</th><th style="width:20mm">Easy!</th><th style="width:20mm">Sometimes</th><th style="width:20mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Paulo's crazy weekend.</b> Choose the correct verb.</p>
<div class="msg" style="max-width:none;line-height:1.85">{msg}</div>
<p style="margin-top:3mm"><b>2. My weekend.</b> Write about your last weekend (6 sentences). Use at least five irregular verbs from this unit.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class is <b>Review 3</b> (Units 19–26). Check the homework first: the student reads the weekend text and you ask two questions with <i>did</i>.</p>""")

    b.extra("Audio scripts", f"""
{sub("26.1", "Monday morning (slow and natural)")}
<p style="line-height:1.5">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("26.2", "Irregular verbs")}
<p>{" · ".join(S262)}</p>
{sub("26.3", "Sentences")}
<p>{" ".join(S263)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essentials 26 - Weekends")
