# Speak! Progress B1 - Unit 01 "Getting to know someone" (all English) - B1 format (2026-11-09)
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

PHOTOS = [("G", "friends at a café", "friends at a café")]
_r = json.load(open("roteiro.json"))["units"]["b1-unit-01"]
S011 = [x.split(": ", 1) for x in _r["01.1 Ana meets Danny"].split("\n")]
S012 = [x.split(": ", 1) for x in _r["01.2 Kate meets Yuki"].split("\n")]
S013 = [x.split(": ", 1)[1] for x in _r["01.3 Repeat: connected speech"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'
    def lines(n):
        return '<div class="wline"></div>' * n

    # Page 1 - Warm-up
    cover = cover_html(T, "LEVEL B1 · UNIT 01", "Getting to know someone", "First conversations · <b>questions in different tenses, showing interest</b>",
                       [("YOU CAN", "start a conversation with someone new, ask the right questions and show interest"),
                        ("LANGUAGE", "Where do you come from? · Have you ever been…? · How long have you been learning…? · Do you? · Really?"),
                        ("PRONUNCIATION", "connected speech in questions: do you, have you, did you")])
    df = [("a person you know a little, but not well", "an acquaintance"), ("people you work with", "coworkers"),
          ("people in your family", "relatives"), ("a person you don't know at all", "a stranger"),
          ("people who share a home with you", "roommates"), ("a friend of two people", "a mutual friend"),
          ("people in the same class", "classmates"), ("friends you trust and can tell anything", "close friends")]
    dfl = [f'<li value="{i+1}">{d} {A(w, "min-width:24mm")}</li>' for i, (d, w) in enumerate(df)]
    b.page(f"""{sec(1, "Warm-up: meeting people", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('G', 58, 38)}<div style="flex:1">
{sub("A", "Look at the photo and discuss.", "3 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0"><li>How do these people know each other? Guess.</li><li>Where do you usually meet new people?</li><li>What do you talk about with someone new? What topics do you avoid?</li></ol></div></div>
{sub("B", "People you know. Write the words from the box next to the definitions.", "3 min")}
<div class="bank">acquaintance · classmates · close friends · coworkers · mutual friend · relatives · roommates · stranger</div>
<div style="font-size:8.8pt">{twocol(dfl, 4)}</div>
{sub("C", "Tell your teacher about three people from B in your life.", "2 min")}""",
    25, """<ol><li>A: a discussion lead-in; accept any guess and ask follow-ups (<i>Why do you think so?</i>).</li>
<li>B: a <i>stranger</i> is a person you don't know; a <i>foreigner</i> is from another country. <i>Roommate</i> (US) = flatmate (UK). C: welcome to B1! Use it as a getting-to-know-you task even if you know the student well.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 60 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Discussion · people you know (definitions)</td><td>1</td></tr>
<tr><td>2 Listening</td><td>12 min</td><td>Two first conversations: gist, detail, inference, useful chunks</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>8 min</td><td>Questions in different tenses · showing interest</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Getting to know someone (study at home)</td><td>4</td></tr>
<tr><td>4 Vocabulary lab + pronunciation</td><td>8 min</td><td>Relationship collocations · false friends · connected speech</td><td>5</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Danny's message: tenses in context · make the questions</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Functional language · long turn · party role-play</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>4 min</td><td>Can-do · language notes · writing homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE B1 FORMAT</h4>Natural-speed audio first (the slow version is support only) · an inference question in every listening · a Vocabulary lab (collocations, word building, false friends) · practice in connected texts · a long turn with planning time · written homework of 100–150 words with a model and a checklist. Use the <b>error log</b> (page 8) during the whole lesson.</div>
<div class="box sand"><h4>THE STORY CONTINUES (B1)</h4>B1 Progress starts a new year of the story. Danny, Rita's son (A2 Unit 34), arrives in São Paulo for his gap year and meets Ana (Neural2-F) at a café; Danny is a new recurring voice: <b>en-US-Chirp3-HD-Puck</b>. They discover a mutual friend: Tom. In Chicago, Kate (Neural2-G) chats with Yuki, a Japanese tourist (one-off, Studio-O), at Sweet Kate Bakery. No new facts.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students say <i>How long are you learning English?</i>, use the present perfect with a past time (<i>I have been to Peru in 2024</i>) and confuse <i>actually / currently</i>, <i>pretend / intend</i>, <i>know / meet</i> and <i>stranger / foreigner</i>. They rarely use reply questions, so conversations sound flat.</div>
<div class="box"><h4>AUDIO</h4>Track 01.1 Ana meets Danny (natural and slow) · Track 01.2 Kate meets Yuki · Track 01.3 Repeat: connected speech</div>""")

    # Page 2 - Listening
    t1 = [("origin", True), ("hobbies", False), ("travel", True), ("work", True), ("family", False), ("studies", True)]
    t1l = " &nbsp; ".join(f"☐ {t}{(' ' + R('✓')) if ok else ''}" for t, ok in t1)
    q1 = [("Whereabouts in", "Chicago?"), ("", "Have you been to Brazil before?"), ("And what", "do you do?"), ("", "Do you enjoy your work?"),
          ("How long", "have you been learning?"), ("", "Do you travel much?"), ("", "Have you ever been to Peru?")]
    q1l = [f'<li value="{i+1}">{A(f"{a} {q}".strip(), "min-width:44mm")}</li>' for i, (a, q) in enumerate(q1)]
    q2 = ["Is this your first time in Chicago?", "When did you get here?", "How long are you here for?", "Where are you staying?", "How long have you been learning it?", "Do you do any sports?"]
    q2l = [f'<li value="{i+1}">{A(q, "min-width:44mm")}</li>' for i, q in enumerate(q2)]
    b.page(f"""{sec(2, "Listening: first conversations", "12 min")}
<p style="margin:0 0 1mm"><b>Conversation 1:</b> Danny, Rita's son, has just arrived in São Paulo for his gap year. He meets Ana at a café. <b>Conversation 2:</b> Kate talks to a tourist at her bakery in Chicago.</p>
{audiocard(["01.1 · NATURAL", "01.1 · SLOW", "01.2"])}
{sub("A", "Listen to conversation 1 at natural speed. Check (✓) the topics Ana and Danny talk about.", "2 min", "01.1 · NATURAL")}
<p style="font-weight:600;margin:.3mm 0">{t1l}</p>
{sub("B", "Listen again and write the questions. Use the slow version only if you need it.", "4 min", "01.1 · NATURAL")}
<div style="font-size:8.8pt">{twocol(q1l, 4)}</div>
{sub("C", "Conversation 2. Write Kate's questions.", "3 min", "01.2")}
<div style="font-size:8.8pt">{twocol(q2l, 3)}</div>
{sub("D", "Think about it. Discuss with your teacher.", "3 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0"><li>Why does Ana say "It's a small world!"? {R("They discover that they both know Tom (a mutual friend).") if T else ""}</li>
<li>Who asks more questions in conversation 2, Kate or Yuki? Why, do you think? {R("Kate. Yuki gives short answers (maybe she's shy or tired), so Kate keeps the conversation going.") if T else ""}</li></ol>
<div class="box sand" style="margin-top:1.2mm"><h4>NOTICE: USEFUL CHUNKS</h4><i>Whereabouts in Chicago? · It's a small world! · That's a shame! · Not yet. · Are you any good? · Yes, I have, actually.</i></div>""",
    24, """<ol><li>B1 routine: natural speed first; offer the slow version only if the student is lost. Pause after each question in B.</li>
<li>D: inference questions have no single answer: accept any answer the student can support with something from the audio.</li></ol>""")

    # Page 3 - Language focus
    fn = [("general facts about a person", "Where do you come from? / What do you do? / Do you travel much? / Do you do any sports?"),
          ("someone's experiences", "Have you been to Brazil before? / Have you ever been to Peru?"),
          ("something that started in the past and continues now", "How long have you been learning?"),
          ("a temporary situation now", "How long are you here for? / Where are you staying?"), ("a finished past event", "When did you get here?")]
    fnl = "".join(f"<li>{f} {A(e, 'min-width:60mm')}</li>" for f, e in fn)
    b.page(f"""{sec(3, "Language focus: asking and showing interest", "8 min")}
{sub("A", "Look at all the questions on page 2. Which questions ask about…", "4 min")}
<ol style="line-height:1.5;font-size:9pt;margin:0">{fnl}</ol>
{sub("B", "Showing interest. Which techniques do the speakers use? Check (✓).", "2 min")}
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

    # Page 5 - Vocabulary lab + common mistakes + pronunciation
    col = [("It's easy to", "make", "friends at college."), ("At a party, a funny question can", "break", "the ice."),
           ("We", "have", "a lot in common: we both love jazz."), ("Let's", "keep", "in touch! Send me a message."),
           ("I", "get", "along well with my coworkers."), ("We moved to different cities and", "lost", "touch."),
           ("Danny wants to", "get", "to know São Paulo."), ("Americans often make small", "talk", "about the weather.")]
    coll = [f'<li value="{i+1}">{a} {A(w, "min-width:12mm")} {e}</li>' for i, (a, w, e) in enumerate(col)]
    b.page(f"""{sec(4, "Vocabulary lab: relationships", "4 min")}
{sub("A", "Complete the collocations with the words in the box.", "4 min")}
<div class="bank">break · get · get · have · keep · lost · make · talk</div>
<div style="font-size:8.8pt">{twocol(coll, 4)}</div>
<div class="box sand"><h4>WATCH OUT: FALSE FRIENDS AND WORD CHOICE</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>Actually, I live in São Paulo. (= now)</td><td><b>Currently / Right now, I live in São Paulo.</b></td><td><i>actually</i> = in fact.</td></tr>
<tr><td>I pretend to travel to Peru.</td><td><b>I plan / intend to travel to Peru.</b></td><td><i>pretend</i> = act as if something is true.</td></tr>
<tr><td>I knew Ana yesterday.</td><td><b>I met Ana yesterday.</b></td><td><i>meet</i> = see someone for the first time.</td></tr>
<tr><td>He's a foreigner. I don't know him.</td><td><b>He's a stranger.</b></td><td><i>stranger</i> = a person you don't know.</td></tr>
<tr><td>It's easy to do friends here.</td><td><b>It's easy to make friends here.</b></td><td>collocation: <i>make friends</i>.</td></tr></table></div>
{sec(5, "Pronunciation lab: connected speech", "4 min")}
<p class="small" style="margin:.3mm 0">In fast questions, small words join and get weak: <b>do you</b> → /də jə/ · <b>have you</b> → /həv jə/ · <b>did you</b> → /dɪdʒə/. In reply questions, your voice goes up ↗: <i>Oh, have you?</i></p>
{audiocard(["01.3"])}
{sub("A", "Listen and repeat. Then ask your teacher three of the questions, fast and natural.", "4 min", "01.3")}
{twocol([f'<li value="{i+1}">{s}</li>' for i, s in enumerate(S013)], 4)}""",
    28, """<ol><li>Vocabulary lab: ask a personal question with each collocation: <i>Who do you get along with at work? Have you lost touch with anyone?</i> <i>College</i> (US) = university.</li>
<li>Pronunciation: don't force the student to reduce; understanding reduced forms matters more than producing them. Exaggerate the rising tone in 8.</li></ol>""")

    # Page 6 - Practice (connected text)
    gp = [("arrive", "arrived"), ("stay", "'m staying"), ("meet", "met"), ("work", "works"), ("learn", "has been learning"), ("be", "has been"), ("never / try", "have never tried")]
    g = [A(a, "min-width:24mm") + f" ({v})" for v, a in gp]
    qa = [("On Saturday.", "When did you arrive?"), ("At a hostel near Paulista Avenue.", "Where are you staying?"), ("She's a doctor.", "What does Ana do?"),
          ("For about ten years.", "How long has she been learning English?"), ("Yes, she has. Two years ago.", "Has she ever been to Peru?"), ("Yes, I love it!", "Do you like Brazilian food?")]
    qal = "".join(f"<li>{A(q, 'min-width:62mm')} <i>– {a}</i></li>" for a, q in qa)
    b.page(f"""{sec(6, "Practice", "8 min")}
{sub("A", "Danny writes to his mom. Complete his message with the correct form of the verbs.", "4 min")}
<div class="box" style="line-height:1.85;font-size:9pt">Hi Mom! I {g[0]} in São Paulo on Saturday, and this week I {g[1]} at a small hostel near Paulista Avenue. Yesterday I {g[2]} Ana at a café. She's really nice! She {g[3]} as a doctor, and she {g[4]} English for about ten years. Guess what? Her teacher is Tom, Lucy's roommate! It's a small world. She {g[5]} to Peru, so she gave me some tips. I {g[6]} Brazilian food before, but now I love pão de queijo! Love, Danny</div>
{sub("B", "Rita calls Danny. Write her questions for Danny's answers.", "4 min")}
<ol style="line-height:1.6;font-size:9pt;margin:0">{qal}</ol>""",
    22, """<ol><li>A: in 2 the present continuous shows a temporary situation (<i>this week</i>); in 5 <i>has learned</i> is possible, but the continuous is more natural for an activity that continues.</li>
<li>B: accept other correct questions (6: <i>Have you tried Brazilian food? Do you like pão de queijo?</i>). Then role-play the call: the teacher is Rita.</li></ol>""")

    # Page 7 - Speaking
    card = ["Name: Sam(antha) Reed", "From: Denver, Colorado; now lives in Chicago", "Job: nurse (for 6 years)", "Experiences: has been to Brazil once (Rio, 2023)", "Now: learning Portuguese, staying with a friend", "Free time: rock climbing, cooking"]
    b.page(f"""{sec(7, "Speaking: meeting people", "12 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>start</th><th>keep it going</th><th>find common ground</th><th>finish</th></tr>
<tr><td><i>Mind if I join you? · So, how do you know Kate? · Is this your first time here?</i></td><td><i>What about you? · Really? Whereabouts? · Oh, have you? When was that?</i></td><td><i>Me too! · So have I! · We have a lot in common.</i></td><td><i>It was great talking to you. · Let's keep in touch! · See you around.</i></td></tr></table></div>
{sub("A", "Long turn. Prepare for one minute, then talk for two minutes about a person who is important in your life.", "5 min")}
<ul style="line-height:1.45;font-size:8.9pt;margin:0"><li>who the person is and how you met</li><li>how long you've known them (<i>for / since</i>)</li><li>what you have in common and how you get along</li><li>something you've done together, and when you last saw them</li></ul>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("B", "Role-play. You're at a party at a friend's house in Chicago. Your teacher is a guest you don't know. Start, keep the conversation going, find something in common and finish politely.", "5 min")}
<p class="small" style="margin:0">{R("Teacher's role card: " + " · ".join(card)) if T else "Use the functional language above, reply questions and questions in different tenses."}</p></div>{img('E', 32, 22)}</div>
{sub("C", "Change roles: now you're the guest. Be yourself, or invent a new identity!", "2 min")}""",
    28, """<ol><li>A: time the student; don't interrupt. Write mistakes in the error log (page 8). Fluency option (3-2-1): the student tells the same story again in 2 minutes, then in 1 minute; it gets faster and more fluent each time.</li>
<li>B: answer as the character in red, giving details that invite follow-ups (Denver? rock climbing?). Count the student's reply questions.</li></ol>""")

    # Page 8 - Wrap-up
    pc = ["I can ask questions in different tenses to get to know someone.", "I can show interest with echo questions, reply questions and follow-ups.",
          "I can talk about the people in my life: coworkers, acquaintances, relatives…"]
    pcr = "".join(f"<tr><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for s in pc)
    b.page(f"""{sec(8, "Wrap-up and homework", "4 min")}
{sub("A", "Can-do check", "1 min")}
<table class="ck" style="font-size:8.6pt"><tr><th>In English…</th><th style="width:16mm">Easy!</th><th style="width:16mm">Sometimes</th><th style="width:16mm">Not yet</th></tr>{pcr}</table>
{sub("B", "My language notes. Write three corrections from today's class.", "2 min")}
<div style="display:flex;gap:5mm;font-size:8.6pt"><div style="flex:1"><b>I said…</b>{lines(3)}</div><div style="flex:1"><b>Better:</b>{lines(3)}</div></div>
{sub("C", "Homework: writing (100–150 words)", "1 min")}
<p style="margin:.3mm 0">Write a message to a new language exchange partner. Read Yuki's model first.</p>
<div class="box" style="font-size:8.6pt;line-height:1.4;margin:.5mm 0"><i>Hi Marina! My name is Yuki and I'm from Tokyo. I work as a graphic designer, and I've been learning English for about ten years. I've just come back from Chicago. It was my first time in the US, and I loved the food! In my free time, I do aikido. Have you ever tried a martial art? Where do you live in Brazil? How long have you been learning Japanese? Write soon! Yuki</i></div>
<p class="small" style="margin:.3mm 0">Checklist: ☐ say hello and introduce yourself &nbsp;☐ use the present simple, the present perfect and the past simple &nbsp;☐ say how long you've been learning English &nbsp;☐ ask three questions &nbsp;☐ 100–150 words</p>
{lines(7)}""",
    30, """<ol><li>B (error log): during the lesson, note 3–5 real mistakes. Here, the student writes what they said and the better version; you guide them to self-correct first.</li>
<li>C: next class, answer the student's three questions as the language partner; the student replies with reply questions and follow-ups. Correct with a focus on tenses.</li></ol>""")

    b.extra("Audio script", f"""
{sub("01.1", "Ana meets Danny (natural and slow)")}
<p style="line-height:1.35;font-size:8.8pt">{"<br>".join(f"<b>{n}:</b> {t}" if n != "Narrator" else f"<i>{t}</i>" for n, t in S011)}</p>
{sub("01.2", "Kate meets Yuki")}
<p style="line-height:1.35;font-size:8.8pt">{"<br>".join(f"<b>{n}:</b> {t}" if n != "Narrator" else f"<i>{t}</i>" for n, t in S012)}</p>
{sub("01.3", "Repeat: connected speech")}
<p>{" · ".join(S013)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 01 - Getting to know someone")
