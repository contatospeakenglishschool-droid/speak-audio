# Speak! Progress B1 - Unit 01 "Getting to know someone" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Progress"
setup(band="B1 · UNIT 01", audio_json="audio_b1-unit-01.json", img_dir="img")

PHOTOS = [("A", "close friends", "close friends"), ("B", "coworkers", "coworkers"), ("C", "acquaintances", "acquaintances"), ("D", "classmates", "classmates"),
          ("E", "roommates", "roommates"), ("F", "a stranger", "a stranger"), ("G", "a mutual friend", "a mutual friend"), ("H", "relatives", "relatives")]
_r = json.load(open("roteiro.json"))["units"]["b1-unit-01"]
S011 = [x.split(": ", 1) for x in _r["01.1 Ana meets Danny"].split("\n")]
S012 = [x.split(": ", 1) for x in _r["01.2 Kate meets Yuki"].split("\n")]
S013 = [x.split(". ", 1)[1] for x in [y.split(": ", 1)[1] for y in _r["01.3 Reply questions"].split("\n")]]
S014 = [x.split(": ", 1)[1] for x in _r["01.4 Repeat: showing interest"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'

    # Page 1
    cover = cover_html(T, "LEVEL B1 · UNIT 01", "Getting to know someone", "First conversations · <b>questions in different tenses, showing interest</b>",
                       [("YOU CAN", "start a conversation with someone new, ask the right questions and show interest"),
                        ("LANGUAGE", "Where do you come from? · Have you ever been…? · How long have you been learning…? · Do you? · Really?"),
                        ("PRONUNCIATION", "rising intonation in echo and reply questions")])
    sf = [("I don't know him that well. He's just an", "acquaintance", "."), ("My", "roommate", "never does any cleaning. It's very annoying."),
          ("My grandfather came from Italy, and I have a lot of", "relatives", "there."), ("I can talk to her about any problem. We're", "close friends", "."),
          ("One of my", "coworkers", "was sick, so my manager gave me extra work."), ("\"How do you two know each other?\" \"We met through a", "mutual friend", ".\""),
          ("He forgot his book, so he borrowed one from a", "classmate", "."), ("I've never seen him before. He's a complete", "stranger", ".")]
    sfl = "".join(f"<li>{a} {A(w, 'min-width:20mm')}{'' if e[0] in '.' else ' '}{e}</li>" for a, w, e in sf)
    b.page(f"""{sec(1, "Warm-up: people you know", "8 min")}
{sub("A", "Who are these people? Name the photos with the words in the box.", "2 min")}
<div class="bank">acquaintances · classmates · close friends · coworkers · a mutual friend · relatives · roommates · a stranger</div>
<div style="display:flex;gap:1.5mm;justify-content:space-between">{"".join(f'<div style="width:21mm;text-align:center;font-size:7.4pt"><div style="position:relative">{img(l, 21, 16)}<b style="position:absolute;top:.5mm;left:1mm;background:#176074;color:#fff;border-radius:1mm;padding:0 1mm;font-size:7pt">{l}</b></div>{A(w, "min-width:18mm")}</div>' for l, w, _ in PHOTOS)}</div>
{sub("B", "Complete with words from A (singular or plural). Then tell your teacher about three people you know.", "4 min")}
<ol style="line-height:1.5;font-size:8.8pt;margin:0;column-count:2;column-gap:5mm">{sfl}</ol>""",
    27, """<ol><li>A stranger is a person you don't know; a <i>foreigner</i> is a person from another country (a common confusion). A <i>mutual friend</i> is a friend of two people. <i>Roommate</i> (US) = flatmate (UK).</li>
<li>B: welcome to B1! Use the personal part as a getting-to-know-you activity even if you know the student well.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>People you know: acquaintance, coworker, relative…</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Two first conversations: Ana and Danny; Kate and Yuki</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Questions in different tenses · showing interest</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Getting to know someone</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>4 min</td><td>Showing interest · reply questions</td><td>5</td></tr>
<tr><td>5 Practice</td><td>9 min</td><td>Make the questions · which tense?</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Role-play: meet someone at a party</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES (B1)</h4>B1 Progress starts a new year of the story. Danny, Rita's son (A2 Unit 34), arrives in São Paulo for his gap year and meets Ana (Neural2-F) at a café; Danny is a new recurring voice: <b>en-US-Chirp3-HD-Puck</b> (keep it in future units). They discover a mutual friend: Tom. In Chicago, Kate (Neural2-G) chats with Yuki, a Japanese tourist (one-off, Studio-O), at Sweet Kate Bakery. No new facts.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students say <i>How long are you learning English?</i>, use the present perfect with a past time (<i>I have been to Peru in 2024</i>), forget <i>do</i> in questions, and confuse <i>stranger</i> and <i>foreigner</i>. They rarely use reply questions (<i>Do you? Have you?</i>), so conversations sound flat.</div>
<div class="box"><h4>AUDIO</h4>Track 01.1 Ana meets Danny (slow and natural) · Track 01.2 Kate meets Yuki · Track 01.3 Reply questions · Track 01.4 Repeat: showing interest</div>""")

    # Page 2
    t1 = [("origin", True), ("hobbies", False), ("travel", True), ("work", True), ("family", False), ("studies", True)]
    t1l = " &nbsp; ".join(f"☐ {t}{(' ' + R('✓')) if ok else ''}" for t, ok in t1)
    q1 = [("Whereabouts in", "Chicago?"), ("", "Have you been to Brazil before?"), ("And what", "do you do?"), ("", "Do you enjoy your work?"),
          ("How long", "have you been learning?"), ("", "Do you travel much?"), ("", "Have you ever been to Peru?")]
    q1l = [f'<li value="{i+1}">{A(f"{a} {q}".strip(), "min-width:44mm")}</li>' for i, (a, q) in enumerate(q1)]
    t2 = [("hobbies", True), ("the weather", False), ("current visit", True), ("languages", True), ("politics", False), ("family", False)]
    t2l = " &nbsp; ".join(f"☐ {t}{(' ' + R('✓')) if ok else ''}" for t, ok in t2)
    q2 = ["Is this your first time in Chicago?", "When did you get here?", "How long are you here for?", "Where are you staying?", "How long have you been learning it?", "What do you do in your free time?", "Do you do any sports?"]
    q2l = [f'<li value="{i+1}">{A(q, "min-width:44mm")}</li>' for i, q in enumerate(q2)]
    b.page(f"""{sec(2, "Listening: first conversations", "10 min")}
<div style="display:flex;gap:2.5mm;align-items:center"><p style="flex:1;margin:0"><b>Conversation 1:</b> Danny, Rita's son, has just arrived in São Paulo for his gap year. He meets Ana at a café. <b>Conversation 2:</b> Kate talks to a tourist at her bakery in Chicago.</p>{img('I', 26, 18)}{img('J', 26, 18)}</div>
{audiocard(["01.1 · SLOW", "01.1 · NATURAL", "01.2"])}
{sub("A", "Conversation 1. Check (✓) the topics Ana and Danny talk about. Then listen again and write the questions.", "5 min", "01.1 · NATURAL")}
<p style="font-weight:600;margin:.3mm 0">{t1l}</p>
<div style="font-size:8.8pt">{twocol(q1l, 5)}</div>
{sub("B", "Conversation 2. Check (✓) the topics. Then listen again and write the questions.", "5 min", "01.2")}
<p style="font-weight:600;margin:.3mm 0">{t2l}</p>
<div style="font-size:8.8pt">{twocol(q2l, 5)}</div>""",
    27, """<ol><li>A: play the slow version first for the topics, then the natural version for the questions; pause after each question. <i>Whereabouts?</i> = where exactly?</li>
<li>Danny and Ana discover a mutual friend (Tom). The student can write the questions in the gaps while listening, then check with the script.</li></ol>""")

    # Page 3
    fn = [("general facts about a person", "Where do you come from? / What do you do? / Do you travel much? / Do you do any sports?"),
          ("someone's experiences", "Have you been to Brazil before? / Have you ever been to Peru?"),
          ("something that started in the past and continues now", "How long have you been learning?"),
          ("a temporary situation now", "How long are you here for? / Where are you staying?"), ("a finished past event", "When did you get here?")]
    fnl = "".join(f"<li>{f} {A(e, 'min-width:60mm')}</li>" for f, e in fn)
    b.page(f"""{sec(3, "Language focus: asking and showing interest", "10 min")}
{sub("A", "Look at all the questions on page 2. Which questions ask about…", "5 min")}
<ol style="line-height:1.5;font-size:9pt;margin:0">{fnl}</ol>
{sub("B", "Showing interest. Which techniques do the speakers use? Check (✓).", "3 min")}
<ul style="line-height:1.6;margin:0;list-style:none;padding-left:1mm">
<li>☐ expressions: <i>Really? That's a shame! It's a small world!</i> {R('✓') if T else ''}</li>
<li>☐ echo: repeating a word: <i>A doctor? An English test? On Monday?</i> {R('✓') if T else ''}</li>
<li>☐ follow-up questions: <i>Whereabouts? Do you enjoy your work? Are you any good?</i> {R('✓') if T else ''}</li></ul>
{sub("C", "Reply questions. Complete.", "2 min")}
<p style="margin:.5mm 0;line-height:1.7">"I work at a hospital." → "{A("Do you?", "min-width:14mm")}" · "I've been to Japan." → "{A("Have you?", "min-width:16mm")}" · "I went to Mexico." → "{A("Did you?", "min-width:14mm")}"</p>
<div class="box sand"><h4>RULE</h4><b>facts</b> → present simple · <b>experiences</b> → present perfect (<i>Have you ever…?</i>) · <b>duration up to now</b> → present perfect continuous (<i>How long have you been…?</i>) · <b>temporary</b> → present continuous · <b>finished past</b> → past simple. Show interest with expressions, echo questions, reply questions and follow-ups. More on the next page: <b>Grammar reference</b>.</div>""",
    20, """<ol><li>A: some questions fit more than one category; accept reasonable answers if the student explains them.</li>
<li>C: the auxiliary in the reply question matches the sentence: <i>do / have / did / can / is</i>.</li></ol>""")

    grammar_ref.getting_to_know(b)

    # Page 5
    rq = ["Do you?", "Have you?", "Are you?", "Did you?", "Can you?", "Does she?"]
    rql = "".join(f"<li>{A(x, 'min-width:18mm')}</li>" for x in rq)
    b.page(f"""{sub("D", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>How long are you learning English?</td><td><b>How long have you been learning English?</b></td><td>duration up to now.</td></tr>
<tr><td>I have been to Peru in 2024.</td><td><b>I went to Peru in 2024.</b></td><td>past time: past simple.</td></tr>
<tr><td>Did you ever go to Italy?</td><td><b>Have you ever been to Italy?</b></td><td>experience.</td></tr>
<tr><td>Where you come from?</td><td><b>Where do you come from?</b></td><td>do in questions.</td></tr>
<tr><td>He's a foreigner. I don't know him.</td><td><b>He's a stranger.</b></td><td>stranger = unknown person.</td></tr>
<tr><td>I've been to Japan. – Yes.</td><td><b>– Oh, have you? When?</b></td><td>show interest.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "4 min")}
{audiocard(["01.4", "01.3"])}
{sub("A", "Listen and repeat. Your voice goes up ↗ to show interest.", "2 min", "01.4")}
{twocol([f'<li value="{i+1}">{s}</li>' for i, s in enumerate(S014)], 4)}
{sub("B", "Listen to six sentences. In the pause, say a reply question. Then write it.", "2 min", "01.3")}
<ol style="line-height:1.5;column-count:3;column-gap:5mm">{rql}</ol>""",
    30, """<ol><li>A: a flat voice sounds bored; a rising voice sounds interested. Exaggerate at first.</li>
<li>B: script: 1 I work at a hospital. 2 I've been to Japan twice. 3 I'm learning Portuguese. 4 I went to Mexico last year. 5 I can play the guitar. 6 My mom manages a café. Add a follow-up: <i>Do you? Which one?</i></li></ol>""")

    # Page 6
    mq = [("you / where / from / come / do", "Where do you come from?"), ("for a living / what / do / you / do", "What do you do for a living?"),
          ("you / ever / been / have / to Peru", "Have you ever been to Peru?"), ("learning / how long / you / have / English / been", "How long have you been learning English?"),
          ("staying / you / where / are", "Where are you staying?"), ("did / when / arrive / you", "When did you arrive?"),
          ("your / first time / is / in Brazil / this", "Is this your first time in Brazil?"), ("free time / what / do / you / in your / do", "What do you do in your free time?")]
    mql = "".join(f"<li>{w}<br>{A(q, 'min-width:70mm')}</li>" for w, q in mq)
    tc = [(["Do you live", "Are you living"], "Do you live", "in São Paulo? (always)"), (["How long have you worked", "How long do you work"], "How long have you worked", "here?"),
          (["Have you been", "Did you go"], "Did you go", "to the beach last weekend?"), (["are you staying", "do you stay"], "are you staying", "this week?")]
    tcl = "".join(f"<li>{'Where ' if i == 3 else ''}{ch(o, r)} {e}</li>" for i, (o, r, e) in enumerate(tc))
    b.page(f"""{sec(5, "Practice", "9 min")}
{sub("A", "Put the words in order to make questions.", "5 min")}
<ol style="line-height:1.4;font-size:8.8pt;margin:0;column-count:2;column-gap:5mm">{mql}</ol>
{sub("B", "Which tense? Choose the correct option.", "4 min")}
<ol style="line-height:1.7;font-size:9pt;margin:0">{tcl}</ol>
<p class="small" style="margin:.5mm 0">Now ask your teacher three questions from A. Show interest in the answers!</p>""",
    22, """<ol><li>B: in 2, <i>How long have you been working here?</i> is also correct.</li>
<li>Answer the student's questions with interesting details so they can practice reply questions and follow-ups.</li></ol>""")

    # Page 7
    card = ["Name: Sam(antha) Reed", "From: Denver, Colorado; now lives in Chicago", "Job: nurse (for 6 years)", "Experiences: has been to Brazil once (Rio, 2023)", "Now: learning Portuguese, staying with a friend", "Free time: rock climbing, cooking"]
    b.page(f"""{sec(6, "Speaking: meet someone new", "12 min")}
<div style="display:flex;gap:3mm;align-items:center"><p style="flex:1;margin:0">You're at a party at a friend's house in Chicago. Your teacher is a guest you don't know. Start a conversation, ask questions in different tenses, and show interest.</p>{img('G', 30, 20)}</div>
{sub("A", "Prepare. Write one question for each topic.", "3 min")}
<table style="margin:0;font-size:8.8pt"><tr><th style="width:32mm">topic</th><th>my question</th></tr>
<tr><td>origin</td><td></td></tr><tr><td>work or studies</td><td></td></tr><tr><td>an experience (ever)</td><td></td></tr><tr><td>duration (how long…?)</td><td></td></tr><tr><td>free time</td><td></td></tr><tr><td>a mutual friend?</td><td></td></tr></table>
{sub("B", "Role-play. Use reply questions and follow-ups. Try to find something you have in common.", "6 min")}
<p class="small" style="margin:0">{R("Teacher's role card: " + " · ".join(card)) if T else "Remember: Really? · Do you? · Have you? · Whereabouts? · That sounds interesting!"}</p>
{sub("C", "Change roles: now you're the guest. Be yourself, or invent a new identity!", "3 min")}""",
    26, """<ol><li>B: answer as the character in red, giving details that invite follow-ups (Denver? rock climbing?). Count the student's reply questions.</li>
<li>C: let the student invent an identity; ask them questions in all five tenses.</li></ol>""")

    # Page 8
    pc = [("B1 Unit 01", "I can ask questions in different tenses to get to know someone."), ("B1 Unit 01", "I can show interest with echo questions, reply questions and follow-ups."),
          ("B1 Unit 01", "I can talk about people I know: coworkers, acquaintances, relatives…")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("How long are you living in your city?", "How long have you been living / have you lived…?"), ("Did you ever eat sushi?", "Have you ever eaten sushi?"),
          ("I have been to Rio last year.", "I went to Rio last year."), ("What you do in your free time?", "What do you do…?"),
          ("Is this your first time in Chicago?", "✓"), ("He's my coworker. We work together.", "✓")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:44mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Correct the mistakes. If a sentence is correct, write ✓.</b></p>
<ol style="line-height:1.55;font-size:9pt">{hwl}</ol>
<p style="margin-top:1.5mm"><b>2. Hello from me (50–75 words).</b> Write a message to a new language exchange partner. Introduce yourself (where you're from, your job, how long you've been learning English, an experience) and ask them three questions.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class: answer the student's three questions as the language partner, and the student replies with reply questions. Progress check: from Unit 05, this table reviews the last four units, as in A2.</p>""")

    b.extra("Audio script", f"""
{sub("01.1", "Ana meets Danny (slow and natural)")}
<p style="line-height:1.35;font-size:8.8pt">{"<br>".join(f"<b>{n}:</b> {t}" if n != "Narrator" else f"<i>{t}</i>" for n, t in S011)}</p>
{sub("01.2", "Kate meets Yuki")}
<p style="line-height:1.35;font-size:8.8pt">{"<br>".join(f"<b>{n}:</b> {t}" if n != "Narrator" else f"<i>{t}</i>" for n, t in S012)}</p>
{sub("01.3", "Reply questions (3-second pause)")}
<p>{" · ".join(S013)}</p>
{sub("01.4", "Repeat: showing interest")}
<p>{" · ".join(S014)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 01 - Getting to know someone")
