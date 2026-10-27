# Speak! Essentials A1 - Unit 28 "Questions, questions" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
from speak_engine import *
setup(band="A1 · UNIT 28", audio_json="audio_a1-unit-28.json", img_dir="img")

PHOTOS = [("A", "bakery", "bakery"), ("B", "bank", "bank"), ("C", "hotel", "hotel"), ("D", "movie theater", "movie theater"),
          ("E", "museum", "museum"), ("F", "office", "office"), ("G", "pharmacy", "pharmacy"), ("H", "post office", "post office")]

_r = json.load(open("roteiro.json"))["units"]["a1-unit-28"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["28.1 Rio"].split("\n")]
S282 = [x.split(": ", 1)[1] for x in _r["28.2 Repeat question words"].split("\n")]
S283 = [x.split(": ", 1)[1] for x in _r["28.3 Repeat questions"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LEVEL A1 · UNIT 28", "Questions, questions", "Everyday places · <b>questions in the present and past</b>",
                       [("YOU CAN", "ask and answer questions at the bank, the hotel, the pharmacy and more"),
                        ("LANGUAGE", "Do you have…? · When did it start? · Who painted this picture?"),
                        ("PRONUNCIATION", "who /huː/ ≠ whose /huːz/ · yes/no questions ↗ · wh- questions ↘")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Warm-up: places in town", "8 min")}
{sub("A", "Look at the photos. Write the place under each photo.", "3 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Talk about it.", "5 min")}
<ol><li>Which of these places did you go to last month? What did you do there?</li><li>Which place do you go to every week?</li><li>What questions do people ask at a pharmacy?</li></ol>""",
    27, """<ol><li>A: <b>movie theater</b> is American English; people also say <i>the movies</i>. <b>post office</b>: the place where you send letters and packages.</li>
<li>B: question 1 reviews the past simple (Units 24–26). For question 3, accept any idea: this prepares the listening.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>8 places in town with photos</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Paulo's busy day in Rio: 8 questions in 8 places</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Yes/no, wh- and subject questions · present and past · question words</td><td>3</td></tr>
<tr><td>4 Pronunciation lab</td><td>5 min</td><td>Question words · who/whose · intonation ↗ ↘</td><td>4</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Question words · a Brazil quiz (word order)</td><td>5</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>"Where am I?" guessing game · what or which?</td><td>6</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>7</td></tr></table>
<div class="box"><h4>HOW THIS GUIDE WORKS</h4>Every page looks like the Student Book page with the same number. Your notes are in the <b>yellow box</b>.
<span class="red">Answers in red</span> are not in the Student Book. The <span class="time">5 min</span> chips show the time for each activity. Audio scripts are on the last page.</div>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Paulo, Ana's brother and a travel photographer, is in Rio de Janeiro for a photo job. On a busy Friday he asks questions everywhere: at the hotel, the bakery, the pharmacy, the bank (the ATM kept his card!), the post office, a client's office, the museum (Candido Portinari's painting <i>Coffee</i>, 1935) and the movie theater, where he arrives late. Homework: Paulo sends Ana a message full of questions.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>In Portuguese, a question can have the same words as a statement, so students forget the auxiliary: <i>Where you live?</i> ✗ → <b>Where do you live?</b> They also keep the statement order: <i>What time starts the movie?</i> ✗ → <b>What time does the movie start?</b> And they add <i>did</i> to subject questions: <i>Who did paint this?</i> ✗ → <b>Who painted this?</b> Finally, <i>Who is this bag?</i> ✗ → <b>Whose bag is this?</b></div>
<div class="box"><h4>AUDIO</h4>Track 28.1 Paulo's busy day (slow and natural) · Track 28.2 Question words · Track 28.3 Questions (intonation)</div>""")

    # Page 2
    rows = [("What time does breakfast start?", "hotel", "It starts at", "six thirty", "on the first floor."),
            ("Did you make this cheese bread today?", "bakery", "Yes, we did. We make it every morning at", "five o'clock", "."),
            ("Do you have something for a headache?", "pharmacy", "Yes, we do. Take one after", "lunch", "with some water."),
            ("Why did the machine keep my card?", "bank", "Because he typed the wrong", "password", "three times."),
            ("Which is faster, SEDEX or PAC?", "post office", "", "SEDEX", "is faster, but it's more expensive."),
            ("Who usually answers the phone here?", "office", "Bia usually answers it, but she's on", "vacation", "this week."),
            ("Who painted this picture?", "museum", "Candido Portinari painted it in", "1935", "."),
            ("When did the movie start?", "movie theater", "It started", "ten minutes", "ago.")]
    tr = "".join(f"<tr><td>{i+1}. {q}</td><td>{A(p, 'min-width:24mm')}</td><td class='small'>{a1} {A(g, 'min-width:16mm')} {a2}</td></tr>"
                 for i, (q, p, a1, g, a2) in enumerate(rows))
    b.page(f"""{sec(2, "Listening: Paulo's busy day", "10 min")}
<p>Paulo, Ana's brother, is a travel photographer. Today he's in Rio de Janeiro for a photo job, and he has a lot of questions!</p>
{audiocard(["28.1 · SLOW", "28.1 · NATURAL"])}
{sub("A", "Where is Paulo? Guess the place for each question. Then listen and check.", "4 min", "28.1 · SLOW")}
{sub("B", "Listen again and complete the answers.", "4 min", "28.1 · NATURAL")}
<table style="table-layout:fixed;font-size:8.8pt"><tr><th style="width:62mm">Paulo's question</th><th style="width:29mm">A. Place</th><th>B. Answer</th></tr>{tr}</table>
{sub("C", "Why didn't anybody answer the phone at the office this morning?", "2 min")}
<div class="wline">{R("Because Bia usually answers the phone, and she's on vacation this week.")}</div>""",
    32, """<ol><li>A: let the student guess first (use the photos on page 1), then play the <b>slow</b> version. <b>cheese bread</b>: the famous snack from Minas Gerais. <b>SEDEX</b> and <b>PAC</b> are two services of the Brazilian post office: SEDEX is the fast one.</li>
<li>B: <b>natural</b> version. <i>Coffee</i> (1935) by Candido Portinari is at the National Museum of Fine Arts in Rio. Ask: <i>Which place was a problem for Paulo?</i> (the bank, the movie theater)</li></ol>""")

    # Page 3
    words8 = [("what", "an activity or a thing"), ("which", "a choice"), ("who", "a person"), ("whose", "the owner"),
              ("where", "a place"), ("when", "a time"), ("why", "a reason"), ("how much", "a price")]
    qw = lambda xs: "".join(f"<tr><td><b>{w}</b></td><td>{A(m, 'min-width:38mm')}</td></tr>" for w, m in xs)
    b.page(f"""{sec(3, "Language focus: questions", "10 min")}
{sub("A", "Complete Paulo's questions with do, does or did. Then answer the questions below.", "4 min")}
<table style="table-layout:fixed"><tr><th style="width:30mm"></th><th>Present simple</th><th>Past simple</th></tr>
<tr><td><b>Yes/no</b></td><td>{A("Do")} you have something for a headache?</td><td>{A("Did")} you make this cheese bread today?</td></tr>
<tr><td><b>Wh- question</b></td><td>What time {A("does")} breakfast start?</td><td>When {A("did")} the movie start?</td></tr>
<tr><td><b>Subject question</b></td><td>Who usually answers the phone?</td><td>Who painted this picture?</td></tr></table>
<ol><li>After do, does and did, the verb is in the {ch(["base form", "past form"], "base form")}.</li>
<li>We use <i>does</i> with {ch(["he, she, it", "I, you, we, they"], "he, she, it")}.</li>
<li>In <i>Who painted this picture?</i>, <i>who</i> is the {ch(["subject", "object"], "subject")}: the person who did the action.</li>
<li>In subject questions, we {ch(["use", "don't use"], "don't use")} do, does or did.</li></ol>
{sub("B", "Question words. What information do they ask for? Use the box.", "4 min")}
<div class="bank">a choice · a person · a place · a price · a reason · a time · an activity or a thing · the owner</div>
<div class="two"><div><table style="margin:0">{qw(words8[:4])}</table></div><div><table style="margin:0">{qw(words8[4:])}</table></div></div>
<div class="box sand"><h4>QUESTION ORDER</h4>(question word) + <b>do / does / did</b> + subject + base form: Where <b>do</b> you live? · How much <b>does</b> it cost? · Why <b>did</b> the machine keep my card?<br>
<b>Subject questions</b>: Who / What + verb, no <i>do / does / did</i>: Who <b>lives</b> with you? · Who <b>painted</b> it?</div>""",
    27, """<ol><li>A: elicit the rule from the examples before you explain it. Drill the six questions with the right intonation (page 4).</li>
<li>B: <b>whose</b> asks about the owner: <i>Whose bag is this? It's mine.</i> Remind the student of Unit 11 (possessives).</li></ol>""")

    # Page 4
    b.page(f"""{sub("C", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>Where you live?</td><td><b>Where do you live?</b></td><td>Questions need <i>do / does / did</i>.</td></tr>
<tr><td>What time starts the movie?</td><td><b>What time does the movie start?</b></td><td>Auxiliary before the subject.</td></tr>
<tr><td>How much costs it?</td><td><b>How much does it cost?</b></td><td>Same order: <i>does</i> + it + cost.</td></tr>
<tr><td>Did you went to the bank?</td><td><b>Did you go to the bank?</b></td><td>After <i>did</i>: base form.</td></tr>
<tr><td>Who did paint this picture?</td><td><b>Who painted this picture?</b></td><td>Subject question: no <i>did</i>.</td></tr>
<tr><td>Who is this bag?</td><td><b>Whose bag is this?</b></td><td><i>whose</i> = the owner.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "5 min")}
{audiocard(["28.2", "28.3"])}
{sub("A", "Question words. Listen and repeat.", "2 min", "28.2")}
<table style="table-layout:fixed;margin-top:0"><tr>{"".join(f"<td style='text-align:center'><b>{w}</b></td>" for w in S282)}</tr></table>
<div class="box" style="margin-top:1mm"><h4>WHO OR WHOSE?</h4>In <b>who</b> /huː/ and <b>whose</b> /huːz/, <i>wh</i> sounds like <i>h</i>. <b>Whose</b> sounds the same as <b>who's</b> (= who is).</div>
{sub("B", "Questions. Listen and repeat. Does your voice go up ↗ or down ↘?", "2 min", "28.3")}
<table style="table-layout:fixed;margin-top:0">{"".join(f"<tr><td>{q}</td><td style='width:16mm;text-align:center'>{R('↗' if q.split()[0] in ('Do', 'Did') else '↘')}</td></tr>" for q in S283)}</table>""",
    25, """<ol><li>4A: the <i>w</i> in <i>who</i> and <i>whose</i> is silent. Contrast: <i>Who's that?</i> / <i>Whose phone is that?</i></li>
<li>4B: yes/no questions usually go up ↗, wh- questions usually go down ↘. The student marks the arrow while listening, then repeats.</li></ol>""")

    # Page 5
    md = [("When", "do you usually go to the beach?", "In January."), ("Where", "do your parents live?", "In Recife."),
          ("Who", "lives with you?", "My wife and my two dogs."), ("What", "did you do on Sunday?", "I watched a soccer game."),
          ("Why", "do you study English?", "Because I want a better job."), ("How much", "did your new phone cost?", "It cost two thousand reais."),
          ("Which", "do you prefer, coffee or tea?", "Coffee, always!"), ("Whose", "car is this?", "It's my brother's.")]
    mdl = [f'<li value="{i+1}">{A(w, "min-width:17mm")} {q} <span class="small">{a}</span></li>' for i, (w, q, a) in enumerate(md)]
    quiz = [("painted / who / Abaporu", "Who painted Abaporu?", "Tarsila do Amaral painted it in 1928."),
            ("Brasília / did / when / become the capital", "When did Brasília become the capital?", "It became the capital in 1960."),
            ("açaí / where / come from / does", "Where does açaí come from?", "It comes from the Amazon."),
            ("Dom Casmurro / who / wrote", "Who wrote Dom Casmurro?", "Machado de Assis wrote it."),
            ("is / which city / bigger / São Paulo or Rio", "Which city is bigger, São Paulo or Rio?", "São Paulo is bigger."),
            ("a bus ticket / does / how much / cost / in your city", "How much does a bus ticket cost in your city?", "(personal answer)")]
    ql = "".join(f'<li><i>{s}</i><div class="wline">{R(q + " → " + a)}</div></li>' for s, q, a in quiz)
    b.page(f"""{sec(5, "Practice", "8 min")}
{sub("A", "Complete the questions with a question word.", "3 min")}
<div class="bank">how much · what · when · where · which · who · whose · why</div>
{twocol(mdl, 5)}
<p class="small">Which question is a subject question? {R("3. Who lives with you?")}</p>
{sub("B", "A Brazil quiz. Put the words in order to make questions. Then answer them.", "5 min")}
<ol>{ql}</ol>""",
    22, """<p>A: check that the student can say <i>why</i> each word fits (a time, a place, a person…). B: the student writes the question, then answers it orally. Questions 1 and 4 are subject questions: no <i>did</i>. <i>Abaporu</i> (1928) is Tarsila do Amaral's most famous painting.</p>""")

    # Page 6
    types = ["Present simple, yes/no: Do you…?", "Present simple, wh-: What / Where / How much…?", "Past simple: Did you…? / When did…?", "Subject question: Who…?"]
    tt = "".join(f"<tr><td class='small' style='width:62mm;height:10mm'>{x}</td><td></td></tr>" for x in types)
    ww = [("What", "do you want for lunch today?"), ("Which", "do you want, tea or coffee?"), ("What", "kind of music do you like?"),
          ("Which", "size do you want: small, medium or large?"), ("What", "'s your favorite Brazilian food?"), ("Which", "do you prefer, soccer or volleyball?")]
    wwl = [f'<li value="{i+1}">{A(w, "min-width:15mm")}{q}</li>' for i, (w, q) in enumerate(ww)]
    b.page(f"""{sec(6, "Speaking", "12 min")}
{sub("A", "Where am I? Choose a secret place. Write four questions people ask there. Read them to your teacher. Your teacher guesses the place. Then change roles.", "7 min")}
<div class="bank">airport · gym · hair salon · hospital · restaurant · school · supermarket · train station</div>
<table style="table-layout:fixed"><tr><th style="width:62mm">Type of question</th><th>Your question</th></tr>{tt}</table>
<div class="msg" style="max-width:none;padding:2mm 4mm;line-height:1.55"><b>You:</b> Do you have this in a smaller size? Who usually opens the store?<br><b>Teacher:</b> Hmm… Are you at a clothes store?</div>
{sub("B", "What or which? Complete the questions. Then ask your teacher and answer.", "5 min")}
<div class="box" style="margin-top:0"><b>which</b> = a small number of choices (tea or coffee?) · <b>what</b> = many possible answers (What's your favorite food?)</div>
{twocol(wwl, 4)}""",
    30, f"""<ol><li>A: the student reads the questions in random order; guess the place and say why. Correct the question order. Your turn: you are at the airport (the student guesses): {R("Did you pack this bag? · Which gate does the flight to Recife leave from? · Who usually checks the passports? · What time does the flight board?")}</li>
<li>B: we can't contract <i>which</i>: <i>What's</i> ✓ / <i>Which's</i> ✗. Ask follow-up questions: <i>Why?</i></li></ol>""")

    # Page 7
    pc = [("Unit 23", "I can use was / were and say when I was born."), ("Unit 24", "I can say -ed correctly: played, worked, started."),
          ("Unit 25", "I can make past questions and negatives with did / didn't."), ("Unit 26", "I can use irregular past verbs: went, ate, saw, bought."),
          ("Unit 28", "I can ask questions in the present and past with who, whose, which…")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [(["How are you", "How you are"], "How are you"), (["Did Leo go", "Did Leo went"], "Did Leo go"),
          (["What time finishes Marcos", "What time does Marcos finish"], "What time does Marcos finish"),
          (["Who made", "Who did make"], "Who made"), (["Who's", "Whose"], "Whose"), (["Which", "Who"], "Which"),
          (["Where you want", "Where do you want"], "Where do you want"), (["Why did you call", "Why you called"], "Why did you call")]
    def h(i): return f"({i+1}) {ch(*hw[i])}"
    msg = (f"Hi Ana! Rio is great, but I had a crazy day. {h(0)}? {h(1)} to school today? {h(2)} work today? "
           f"{h(3)} the cake for Mom's birthday? It was delicious! And {h(4)} car is that in front of your house? "
           f"{h(5)} do you prefer for Sunday lunch, pizza or barbecue? {h(6)} to go? And {h(7)} me yesterday? Kisses, Paulo")
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:15mm"></th><th>In English…</th><th style="width:20mm">Easy!</th><th style="width:20mm">Sometimes</th><th style="width:20mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Paulo's message to Ana.</b> Choose the correct option.</p>
<div class="msg" style="max-width:none;line-height:1.85">{msg}</div>
<p style="margin-top:3mm"><b>2. My questions.</b> Write six questions for a new friend: two in the present, two in the past, one subject question and one with <i>whose</i> or <i>which</i>. Then write your own answers.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class: start with homework 2. The student asks you the six questions and you answer; then you ask them back. Check the auxiliary in every question.</p>""")

    b.extra("Audio scripts", f"""
{sub("28.1", "Paulo's busy day (slow and natural)")}
<p style="line-height:1.5">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("28.2", "Question words")}
<p>{" · ".join(S282)}</p>
{sub("28.3", "Questions")}
<p>{" ".join(S283)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essentials 28 - Questions, questions")
