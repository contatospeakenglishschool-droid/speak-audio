# Speak! Progress B1 - Unit 01 "Getting to know someone" (all English) - lean B1 format (rebuilt 2026-11-19)
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Progress"
import lean
from lean import talk
setup(band="B1 · UNIT 01", audio_json="audio_b1-unit-01.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-01"]
S011 = [x.split(": ", 1) for x in _r["01.1 Ana meets Danny"].split("\n")]
S012 = [x.split(": ", 1) for x in _r["01.2 Kate meets Yuki"].split("\n")]
S013 = [x.split(": ", 1)[1] for x in _r["01.3 Repeat: connected speech"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'
    def lines(n):
        return '<div class="wline"></div>' * n

    # 1 Warm-up
    cover = cover_html(T, "LEVEL B1 · UNIT 01", "Getting to know someone", "First conversations · <b>questions in different tenses, showing interest</b>",
                       [("YOU CAN", "start a conversation with someone new, ask the right questions and show interest"),
                        ("LANGUAGE", "Where do you come from? · Have you ever been…? · How long have you been learning…? · Do you? · Really?"),
                        ("PRONUNCIATION", "connected speech in questions: do you, have you, did you")])
    df = [("a person you know a little, but not well", "an acquaintance"), ("people you work with", "coworkers"),
          ("people in your family", "relatives"), ("a person you don't know at all", "a stranger"),
          ("people who share a home with you", "roommates"), ("a friend of two people", "a mutual friend")]
    dfl = [f'<li value="{i+1}">{d} {A(w, "min-width:24mm")}</li>' for i, (d, w) in enumerate(df)]
    b.page(f"""{sec(1, "Warm-up: meeting people", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('G', 52, 34)}<div style="flex:1">
{talk(["How do these people know each other? Guess.", "Where do you usually meet new people?", "What do you talk about with someone new? What topics do you avoid?"], "START TALKING")}</div></div>
{sub("A", "People you know. Write the words from the box next to the definitions.", "3 min")}
<div class="bank">an acquaintance · coworkers · a mutual friend · relatives · roommates · a stranger</div>
<div style="font-size:8.8pt">{twocol(dfl, 3)}</div>
{talk(["Tell me about a coworker or a relative you get along with.", "Do you have a mutual friend with someone in your class or at work?"], "USE THE WORDS")}""",
    26, """<ol><li>Start with the questions in the top box (4 minutes): accept any guess and ask follow-ups (<i>Why do you think so?</i>).</li>
<li>A: a <i>stranger</i> is a person you don't know; a <i>foreigner</i> is from another country. <i>Roommate</i> (US) = flatmate (UK). Welcome to B1! Use the questions to get to know the student, even if you know them well.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Ana meets Danny: topics · write the questions · Talk about it", "Getting to know someone: questions in different tenses",
                      "Which question for which situation? · reply questions · Use it (oral)", "Functional language · connected speech (01.3) · party role-play",
                      "Danny's message · conversation 2 (01.2) · word choice · writing"),
        "B1 Progress starts a new year of the story. Danny, Rita's son (A2 Unit 34), arrives in São Paulo for his gap year and meets Ana (Neural2-F) at a café; Danny is a new recurring voice: <b>en-US-Chirp3-HD-Puck</b>. They discover a mutual friend: Tom. In Chicago, Kate (Neural2-G) chats with Yuki, a Japanese tourist (one-off, Studio-O), at Sweet Kate Bakery (conversation 2 is homework). No new facts.",
        "Students say <i>How long are you learning English?</i>, use the present perfect with a past time (<i>I have been to Peru in 2024</i>) and confuse <i>actually / currently</i>, <i>pretend / intend</i> and <i>know / meet</i>. They rarely use reply questions, so conversations sound flat.",
        "Track 01.1 Ana meets Danny (natural and slow) · Track 01.2 Kate meets Yuki (homework) · Track 01.3 Repeat: connected speech"))

    # 2 Listening
    t1 = [("origin", True), ("hobbies", False), ("travel", True), ("work", True), ("family", False), ("studies", True)]
    t1l = " &nbsp; ".join(f"☐ {t}{(' ' + R('✓')) if ok else ''}" for t, ok in t1)
    q1 = [("Whereabouts in", "Chicago?"), ("", "Have you been to Brazil before?"), ("And what", "do you do?"), ("", "Do you enjoy your work?"),
          ("How long", "have you been learning?"), ("", "Do you travel much?"), ("", "Have you ever been to Peru?")]
    q1l = [f'<li value="{i+1}">{A(f"{a} {q}".strip(), "min-width:44mm")}</li>' for i, (a, q) in enumerate(q1)]
    b.page(f"""{sec(2, "Listening: first conversations", "12 min")}
<p style="margin:0 0 1mm">Danny, Rita's son, has just arrived in São Paulo for his gap year. He meets Ana at a café.</p>
{audiocard(["01.1 · NATURAL", "01.1 · SLOW"])}
{sub("A", "Listen at natural speed. Check (✓) the topics Ana and Danny talk about.", "2 min", "01.1 · NATURAL")}
<p style="font-weight:600;margin:.3mm 0">{t1l}</p>
{sub("B", "Listen again and write the questions. Use the slow version only if you need it.", "4 min", "01.1 · NATURAL")}
<div style="font-size:8.8pt">{twocol(q1l, 4)}</div>
{talk(["Why does Ana say &quot;It's a small world!&quot;? Has this ever happened to you?", "Which of the questions in B would you ask a new coworker? Which wouldn't you ask?", "Ask your teacher three of the questions. Then answer them yourself."])}""",
    26, """<ol><li>A–B: 6 minutes. Natural speed first; offer the slow version only if the student is lost. Pause after each question in B.</li>
<li>Talk about it: 6 minutes. In 1, Ana and Danny discover they both know Tom (a mutual friend). Push for follow-up questions in 3.</li></ol>""")

    # 3 Grammar reference (class)
    lean.grammar_in_class(b, grammar_ref.getting_to_know)

    # 4 Practice
    fn = [("general facts about a person", "Where do you come from? / What do you do?"), ("someone's experiences", "Have you ever been to Peru?"),
          ("something that started in the past and continues now", "How long have you been learning?"), ("a temporary situation now", "Where are you staying?"),
          ("a finished past event", "When did you get here?")]
    fnl = "".join(f"<li>{f} {A(e, 'min-width:56mm')}</li>" for f, e in fn)
    use = ["Ask your teacher about their job. Use the present simple.", "Ask about their travel experiences: <i>Have you ever…?</i>", "Ask about something they've been doing for a long time: <i>How long have you been…?</i>",
           "Ask about their last vacation: <i>When did you…?</i>", "Your teacher tells you three facts. Answer with a reply question: <i>Do you? Have you? Did you?</i>"]
    b.page(f"""{sec(4, "Practice: asking and showing interest", "10 min")}
{sub("A", "Look at Danny and Ana's questions on page 2. Write one question for each use.", "3 min")}
<ol style="line-height:1.55;font-size:9pt;margin:0">{fnl}</ol>
{sub("B", "Reply questions. Complete.", "1 min")}
<p style="margin:.5mm 0;line-height:1.7">"I work at a hospital." → "{A("Do you?", "min-width:14mm")}" · "I've been to Japan." → "{A("Have you?", "min-width:16mm")}" · "I went to Mexico." → "{A("Did you?", "min-width:14mm")}"</p>
<div class="box sand"><h4>RULE</h4><b>facts</b> → present simple · <b>experiences</b> → present perfect · <b>duration up to now</b> → present perfect continuous · <b>temporary</b> → present continuous · <b>finished past</b> → past simple. Show interest with <i>Really?</i>, echo questions, reply questions and follow-ups. See the <b>Grammar reference</b> on page 3.</div>
{talk(use, "USE IT: ASK OUT LOUD")}""",
    24, """<ol><li>A–B: 4 minutes. Some questions fit more than one use; accept reasonable answers. The auxiliary in the reply question matches the sentence.</li>
<li>Use it: 6 minutes, all oral. Answer with real information and invite follow-ups. Correct only the question form.</li></ol>""")

    # 5 Speaking
    card = ["Name: Sam(antha) Reed", "From: Denver, Colorado; now lives in Chicago", "Job: nurse (for 6 years)", "Experiences: has been to Brazil once (Rio, 2023)", "Now: learning Portuguese, staying with a friend", "Free time: rock climbing, cooking"]
    b.page(f"""{sec(5, "Speaking: meeting people", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>start</th><th>keep it going</th><th>find common ground</th><th>finish</th></tr>
<tr><td><i>Mind if I join you? · So, how do you know Kate? · Is this your first time here?</i></td><td><i>What about you? · Really? Whereabouts? · Oh, have you? When was that?</i></td><td><i>Me too! · So have I! · We have a lot in common.</i></td><td><i>It was great talking to you. · Let's keep in touch! · See you around.</i></td></tr></table></div>
{audiocard(["01.3"])}
{sub("A", "Listen and repeat. In fast questions, do you → /də jə/, have you → /həv jə/, did you → /dɪdʒə/.", "4 min", "01.3")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.55">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {s}" for i, s in enumerate(S013))}</p>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("B", "Role-play. You're at a party at a friend's house in Chicago. Your teacher is a guest you don't know. Start, keep the conversation going, find something in common and finish politely. Then change roles.", "11 min")}
<p class="small" style="margin:0">{R("Teacher's role card: " + " · ".join(card)) if T else "Use the functional language above, reply questions and questions in different tenses."}</p></div>{img('E', 32, 22)}</div>
{talk(["Who is an important person in your life? How did you meet?", "Do you find it easy to talk to strangers? Why?"])}""",
    30, """<ol><li>A: understanding reduced forms matters more than producing them. Exaggerate the rising tone in reply questions.</li>
<li>B: answer as the character in red, giving details that invite follow-ups (Denver? rock climbing?). Count the student's reply questions. Last 3 minutes: wrap-up (two corrections and <i>Can you start a conversation with someone new?</i>).</li></ol>""")

    # H Homework
    gp = [("arrive", "arrived"), ("stay", "'m staying"), ("meet", "met"), ("work", "works"), ("learn", "has been learning"), ("never / try", "have never tried")]
    g = [A(a, "min-width:22mm") + f" ({v})" for v, a in gp]
    q2 = ["Is this your first time in Chicago?", "How long are you here for?", "How long have you been learning it?"]
    q2l = "".join(f"<li>{A(q, 'min-width:52mm')}</li>" for q in q2)
    b.page(f"""{sec("H", "Homework", "at home")}
{sub("A", "Danny writes to his mom. Complete his message with the correct form of the verbs.", "")}
<div class="box" style="line-height:1.8;font-size:8.8pt;margin:.5mm 0">Hi Mom! I {g[0]} in São Paulo on Saturday, and this week I {g[1]} at a small hostel near Paulista Avenue. Yesterday I {g[2]} Ana at a café. She {g[3]} as a doctor, and she {g[4]} English for about ten years. Guess what? Her teacher is Tom, Lucy's roommate! I {g[5]} Brazilian food before, but now I love pão de queijo! Love, Danny</div>
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("B", "Listen to conversation 2: Kate talks to a tourist at her bakery in Chicago. Write three of Kate's questions.", "", "01.2")}
<ol style="line-height:1.5;font-size:8.7pt;margin:0">{q2l}</ol></div><div style="width:56mm">{audiocard(["01.2"])}</div></div>
{lean.watch_out([("Actually, I live in São Paulo. (= now)", "Currently / Right now, I live in São Paulo.", "<i>actually</i> = in fact."), ("I pretend to travel to Peru.", "I plan / intend to travel to Peru.", "<i>pretend</i> = act as if something is true."), ("I knew Ana yesterday.", "I met Ana yesterday.", "<i>meet</i> = see someone for the first time.")])}
{lean.writing_task(sub, "Write a message to a new language exchange partner: introduce yourself, say how long you've been learning English and ask three questions.", "Hi! My name is… and I'm from… I've been learning English for…", ["three tenses", "three questions", "100–150 words"], "I can start a conversation with someone new and show interest.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class (B: accept any three of Kate's questions from the script). Next class, answer the student's three questions as the language partner; they reply with reply questions.</p>""")

    b.extra("Audio script", f"""
{sub("01.1", "Ana meets Danny (natural and slow)")}
<p style="line-height:1.35;font-size:8.8pt">{"<br>".join(f"<b>{n}:</b> {t}" if n != "Narrator" else f"<i>{t}</i>" for n, t in S011)}</p>
{sub("01.2", "Kate meets Yuki (homework)")}
<p style="line-height:1.35;font-size:8.8pt">{"<br>".join(f"<b>{n}:</b> {t}" if n != "Narrator" else f"<i>{t}</i>" for n, t in S012)}</p>
{sub("01.3", "Repeat: connected speech")}
<p>{" · ".join(S013)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 01 - Getting to know someone")
