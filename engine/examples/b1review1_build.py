# Speak! Progress B1 - Review 1 (Units 01-09), all English - B1 format (2026-11-12)
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
_se.SERIES = "Progress"
setup(band="B1 · REVIEW 1", audio_json="audio_b1-review-1.json", img_dir="img")

PHOTOS = [("A", "chess", "Unit 03"), ("B", "a wedding cake", "Unit 02"), ("C", "a hair salon", "Unit 04"), ("D", "a runner", "Unit 05"),
          ("E", "a hospital", "Unit 06"), ("F", "a résumé", "Unit 07"), ("G", "a metro station", "Unit 08"), ("H", "a wedding photo", "Unit 09")]
_r = json.load(open("roteiro.json"))["units"]["b1-review-1"]
def _fix(t):
    return t.replace("twelve-hour", "12-hour").replace("ten-K", "10K")
SCRIPT = [tuple(_fix(x).split(": ", 1)) for x in _r["R1.1 Gap Year Diaries: a special episode"].split("\n")]
S12 = [x.split(": ", 1)[1].split(". ", 1)[1] for x in _r["R1.2 Dictation: weak forms"].split("\n")]
S13 = [tuple(x.split(": ", 1)) for x in _r["R1.3 Dialogues"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def lines(n):
        return '<div class="wline"></div>' * n

    # Page 1 - Warm-up
    cover = cover_html(T, "LEVEL B1 · REVIEW 1", "Review 1", "Units 01–09 · questions · character and appearance · past and present · verb patterns · work · trends",
                       [("YOU CAN", "check what you learned in Units 01–09 and plan what to practice next"),
                        ("LANGUAGE", "How long have you been…? · He can be a bit… · She looks like… · I used to… · decided to / stopped -ing · don't have to · turned it down · more and more"),
                        ("PRONUNCIATION", "weak forms: to, been, used to")])
    b.page(f"""{sec(1, "Warm-up: photo memory", "6 min")}
{sub("A", "One photo from each unit. Write the word. Then say one sentence about it with the language of that unit.", "6 min")}
<div class="bank">chess · a hair salon · a hospital · a metro station · a résumé · a runner · a wedding cake · a wedding photo</div>
{photo_grid(T, PHOTOS)}
<p class="small" style="margin-top:2mm"><b>Example:</b> chess → <i>Mequinho became the first Brazilian grandmaster in 1972. People used to compare him to Fischer.</i></p>""",
    25, """<p>Photos A–H come from Units 02–09 (Unit 01 is in the listening). Push each unit's language: character and softening (02), past and present tenses, <i>used to</i> (03), <i>look / look like</i> (04), verb patterns (05), <i>have to / don't have to</i> (06), present perfect continuous (07), phrasal verbs (08), trends (09).</p>""", cover=cover)

    b.extra("Review overview · 60 min", """
<table><tr><th>Stage</th><th>Time</th><th>Units</th><th>SB page</th></tr>
<tr><td>1 Warm-up: photo memory</td><td>6 min</td><td>02–09</td><td>1</td></tr>
<tr><td>2 Listening: Gap Year Diaries, a special episode</td><td>10 min</td><td>01–09</td><td>2</td></tr>
<tr><td>3 Grammar 1: questions, describing people, past and present, verb patterns</td><td>8 min</td><td>01–05</td><td>3</td></tr>
<tr><td>4 Grammar 2: correct Danny's email</td><td>8 min</td><td>06–09</td><td>4</td></tr>
<tr><td>5 Vocabulary and word choice</td><td>7 min</td><td>01–09</td><td>5</td></tr>
<tr><td>6 Pronunciation and social English</td><td>8 min</td><td>01–09</td><td>6</td></tr>
<tr><td>7 Speaking: long turn and interview</td><td>9 min</td><td>01–09</td><td>7</td></tr>
<tr><td>8 Reflect and homework</td><td>4 min</td><td>01–09</td><td>8</td></tr></table>
<div class="box"><h4>HOW THIS GUIDE WORKS</h4>Every page looks like the Student Book page with the same number. Your notes are in the <b>yellow box</b>; <span class="red">answers in red</span> are not in the Student Book. This is a review: don't teach everything again. Let the student work, then focus on the mistakes that come back. The Grammar reference pages (page 4) of Units 01–09 are useful here.</div>
<div class="box sand"><h4>THE STORY SO FAR</h4>Danny (Puck) records a special episode of his podcast in the café where he met Ana (Neural2-F) in Unit 01; they share a mutual friend, Tom. Bruno (Fenrir) describes how Danny has changed (Units 02, 03); Danny's beard (Unit 04); Ana's 12-hour shifts in the emergency department (Unit 06); Carol's visit (Unit 04); the running group and the 10K in December (Unit 05); Danny's guide job: freelancer, filled in for a colleague, turned down a hotel job (Units 07, 08); Bruno's parents and online dating (Unit 09). New: Ana's grandparents met at a church party. Dialogues: Danny meets Carol (Leda) at the airport; Bruno and Danny talk about the job. No new real-world facts.</div>
<div class="box"><h4>THE TOP 5 MISTAKES TO WATCH</h4>1. <i>How long are you living here? / I live here since July</i> → <b>How long have you been living…? / I've been living here since July</b>. 2. <i>She's a bit friendly / She looks like tired</i> → <b>She's really friendly / She looks tired</b>. 3. <i>I use to play / I stopped to eat junk food (= quit)</i> → <b>I used to play / I stopped eating</b>. 4. <i>You mustn't wear a suit (= not necessary) / I turned down it</i> → <b>You don't have to… / I turned it down</b>. 5. <i>It has overtaken… in 2013 / less people</i> → <b>It overtook… in 2013 / fewer people</b>.</div>
<div class="box"><h4>AUDIO</h4>Track R1.1 Gap Year Diaries: a special episode (natural and slow) · Track R1.2 Dictation: weak forms (6-second pauses) · Track R1.3 Two dialogues (correct versions)</div>""")

    # Page 2 - Listening
    topics = [("how Danny and Ana met", True), ("how Danny has changed", True), ("Danny's beard", True), ("Ana's work", True), ("a visit from Carol", True),
              ("a running race", True), ("Danny's new job", True), ("a chess tournament", False), ("how people meet partners", True)]
    tl = " &nbsp; ".join(f"☐ {t}{(' ' + R('✓')) if ok else ''}" for t, ok in topics)
    tf = [("Danny and Ana met at the airport.", "F: at a café."), ("Bruno says Danny used to be a bit shy.", "T"), ("Danny still plays video games for hours every day.", "F: he hardly ever plays."),
          ("Ana has been working 12-hour shifts all month.", "T"), ("Danny wants to finish the 10K in less than an hour.", "T"), ("Danny accepted the hotel job.", "F: he turned it down.")]
    tfl = [f'<li value="{i+1}">{s} <b>T / F</b> {R(a)}</li>' for i, (s, a) in enumerate(tf)]
    find = [("a reply question or a question about someone's past (01)", "So, Bruno, how would you describe me…?"), ("tend to or can be (02)", "you tended to stay… / you can be quite messy"),
            ("used to (03)", "I used to play for hours"), ("look / look like (04)", "Danny looks different / He looks like a pirate"),
            ("a verb + -ing or to + infinitive (05)", "persuaded me to keep running / I've stopped eating / I hope to finish"),
            ("have to / don't have to (06)", "I don't have to work every day, but I have to know…"), ("present perfect continuous (07)", "He's been growing a beard / I've been working…"),
            ("a work phrasal verb (08)", "filled in for him / turned it down"), ("a trend (09)", "More and more people are using apps.")]
    fl = "".join(f"<li>{x} {R(y)}</li>" for x, y in find)
    b.page(f"""{sec(2, "Listening: Gap Year Diaries, a special episode", "10 min")}
<p>Danny records his podcast in a café with Ana and Bruno.</p>
{audiocard(["R1.1 · NATURAL", "R1.1 · SLOW"])}
{sub("A", "Listen at natural speed. Which topics do they talk about? Check eight. One topic is extra.", "2 min", "R1.1")}
<p style="font-weight:600;font-size:8.8pt;line-height:1.6">{tl}</p>
{sub("B", "Listen again. True (T) or false (F)? Correct the false sentences.", "4 min")}
<div style="font-size:8.6pt">{twocol(tfl, 3)}</div>
{sub("C", "Find one example in the podcast of each form. Use the audio script or listen again.", "4 min")}
<ol style="font-size:8.5pt;line-height:1.38;margin:0">{fl}</ol>""",
    22, """<p>A: the extra topic is <i>a chess tournament</i>. C: let the student read the script (last page of this guide) or play the slow version and pause. Ask: <i>How have you changed since you started B1?</i></p>""")

    # Page 3 - Grammar 1
    qq = [("How long are you learning English?", "How long have you been learning English?"), ("Where you come from?", "Where do you come from?"), ("Have you been to Peru in 2024?", "Did you go to Peru in 2024?")]
    qql = "".join(f"<li>{a} {A(c, 'min-width:48mm')}</li>" for a, c in qq)
    dp = [(["a bit impatient", "a bit friendly"], "a bit impatient", "She's", "in the morning."), (["can be", "is can"], "can be", "He", "moody."),
          (["looks", "looks like"], "looks", "You", "tired today."), (["has", "is with"], "has", "My brother", "a beard.")]
    dpl = "".join(f"<li>{a} {ch(o, r)} {e}</li>" for o, r, a, e in dp)
    vp = [("When I was a kid, I", "used to play", "(play) soccer every day."), ("Mequinho", "became", "(become) a grandmaster in 1972."),
          ("Valmir Nunes kept", "competing", "(compete) as he got older."), ("My friend encouraged me", "to start", "(start) running."),
          ("I've stopped", "eating", "(eat) junk food."), ("I hope", "to finish", "(finish) the race in an hour.")]
    vpl = "".join(f"<li>{a} {A(f, 'min-width:22mm')} {e}</li>" for a, f, e in vp)
    b.page(f"""{sec(3, "Grammar 1: Units 01–05", "8 min")}
{sub("A", "Unit 01. Correct the questions.", "2 min")}
<ol style="line-height:1.7;font-size:8.9pt;margin:0">{qql}</ol>
{sub("B", "Units 02 and 04. Choose the correct option.", "2 min")}
<ol style="line-height:1.7;font-size:8.9pt;margin:0;column-count:2">{dpl}</ol>
{sub("C", "Units 03 and 05. Complete with the correct form of the verb.", "4 min")}
<ol style="line-height:1.75;font-size:8.9pt;margin:0">{vpl}</ol>
<div class="box sand"><h4>REMEMBER</h4><b>questions:</b> auxiliary + subject + verb; present perfect continuous for duration · <b>a bit</b> + negative adjectives; <b>can be / tend to</b> for typical behavior · <b>look</b> + adjective, <b>look like</b> + noun; <b>have</b> + hair, beard · <b>used to</b> = past habits; past simple = finished events · <b>to</b> + infinitive after <i>hope, decide, manage</i>; <b>-ing</b> after <i>keep, stop, enjoy</i>; <b>object + to</b> after <i>encourage, persuade</i>.</div>""",
    22, """<ol><li>A: in 3, a finished time needs the past simple (Unit 01 and Unit 03).</li>
<li>C: ask for a personal sentence for each pattern: <i>What have you stopped doing? What do you hope to do this year?</i></li></ol>""")

    # Page 4 - Grammar 2: email correction
    errs = [("I'm working", "I've been working"), ("since three weeks", "for three weeks"), ("mustn't", "don't have to"), ("filled for", "filled in for"),
            ("turned down it", "turned it down"), ("has overtaken", "overtook"), ("less people", "fewer people"), ("are meeting", "are meeting")]
    def e(i):
        w, c = errs[i]
        return f"<u>{w}</u>" + (f" {R('→ ' + c)}" if T and w != c else (f" {R('✓')}" if T else ""))
    b.page(f"""{sec(4, "Grammar 2: Units 06–09", "8 min")}
{sub("A", "Danny writes to his mom. Eight phrases are underlined. Seven are wrong. Correct them.", "6 min")}
<div class="box" style="line-height:1.95;font-size:9pt">Hi Mom!<br>Good news: I love my new job. {e(0)} as a tour guide {e(1)} now. I'm a freelancer, so I {e(2)} work every day – only on weekends. Last Sunday, Rafa was sick, so I {e(3)} him and did two tours in one day. A hotel offered me a job at reception, but I {e(4)}. Bruno says I made the right decision. By the way, Bruno told me that online dating {e(5)} meeting through friends in 2013. Today, {e(6)} meet through friends, and more and more couples {e(7)} on apps. Crazy, right? Love, Danny</div>
{sub("B", "Units 06–09. Complete the sentences so they are true for you. Then tell your teacher.", "2 min")}
<ol style="line-height:1.35;font-size:8.9pt;margin:0"><li>In my job or studies, I don't have to…<div class="wline"></div></li><li>I've been… since…<div class="wline"></div></li><li>Once, I turned down… because…<div class="wline"></div></li><li>In my city, more and more people…<div class="wline"></div></li></ol>
<div class="box sand"><h4>REMEMBER</h4><b>don't have to</b> = not necessary; <b>mustn't</b> = not allowed · <b>have / has been + -ing</b> + <b>for</b> (a period) / <b>since</b> (a point) · separable phrasal verbs: <b>pronoun in the middle</b> (<i>turn it down</i>) · trends: past simple with a finished time; <b>fewer</b> + countable.</div>""",
    22, """<ol><li>A: phrase 8 (<i>are meeting</i>) is correct (a trend in progress). Note: <i>has overtaken</i> → <i>overtook</i> because of the finished year 2013.</li>
<li>B: correct with the student, then ask follow-up questions in the same tenses.</li></ol>""")

    # Page 5 - Vocabulary
    vc = [("a friend of both people", "a mutual friend"), ("friendly and confident with people", "outgoing"), ("a young person with an exceptional talent", "a prodigy"),
          ("small brown spots on the skin", "freckles"), ("the ability to keep going for a long time", "endurance"), ("making you feel useful and happy", "rewarding"),
          ("a person you can trust to do what they promise", "reliable"), ("a worker who sells their services to different companies", "a freelancer")]
    vcl = [f'<li value="{i+1}">{d} → {A(w, "min-width:22mm")}</li>' for i, (d, w) in enumerate(vc)]
    ff = [(["sympathetic", "nice"], "nice", "My new roommate is really", "– he always helps me."), (["assisted", "watched"], "watched", "I", "the São Silvestre race on TV."),
          (["I'm formed in", "I have a degree in"], "I have a degree in", "", "engineering."), (["chef", "boss"], "boss", "My", "is very strict about deadlines."),
          (["married with", "married"], "married", "She", "a doctor last year."), (["curriculum", "résumé"], "résumé", "I sent my", "and a cover letter.")]
    ffl = "".join(f"<li>{a}{' ' if a else ''}{ch(o, r)} {e2}</li>" for o, r, a, e2 in ff)
    b.page(f"""{sec(5, "Vocabulary and word choice", "7 min")}
{sub("A", "Units 01–08. Write the word or phrase.", "3 min")}
<div class="bank">endurance · a freelancer · freckles · a mutual friend · outgoing · a prodigy · reliable · rewarding</div>
<div style="font-size:8.7pt">{twocol(vcl, 4)}</div>
{sub("B", "Watch out! Units 02–09. Choose the correct word.", "4 min")}
<ol style="line-height:1.75;font-size:8.9pt;margin:0">{ffl}</ol>
<div class="box sand"><h4>YOUR WORD BANK</h4>Choose five words from Units 01–09 that you want to use more. Write a personal sentence with each one in your notebook.</div>""",
    22, """<ol><li>A: after each word, ask a personal question: <i>Who is the most reliable person you know? Is your job rewarding?</i></li>
<li>B: these false friends come from the WATCH OUT boxes of Units 02, 05, 06, 07 and 09.</li></ol>""")

    # Page 6 - Pronunciation and social English
    d1 = [("Carol", "Hi! You must be Danny. Ana told me what you <u>look like</u>."), ("Danny", "Hi Carol! Welcome to Brazil. How <u>is</u> your flight?"),
          ("Carol", "Long! I never sleep on planes. <u>Are you living</u> here for long?"), ("Danny", "For about three months. I've been <u>work</u> as a tour guide."),
          ("Carol", "Really? I'd love <u>doing</u> a tour."), ("Danny", "<u>Are you?</u> I'll take you on Saturday!")]
    d2 = [("Bruno", "You look tired. What <u>have you done</u>?"), ("Danny", "I've been studying the history of the city all morning. I <u>must to</u> give a tour tomorrow."),
          ("Bruno", "<u>Have you to</u> wear a uniform?"), ("Danny", "No, I don't have to. But I <u>don't have to</u> be late. Tourists hate waiting."),
          ("Bruno", "And the hotel job? Did you take it?"), ("Danny", "No, I <u>turned down it</u>. I want to keep <u>to travel</u>.")]
    def dlg(ls):
        return "<br>".join(f"<b>{n}:</b> {t}" for n, t in ls)
    b.page(f"""{sec(6, "Pronunciation and social English", "8 min")}
{audiocard(["R1.2", "R1.3"])}
{sub("A", "Dictation. Listen and write the six sentences. Notice the weak forms (to /tə/, been /bɪn/, used to /ˈjuːstə/).", "4 min", "R1.2")}
<ol style="font-size:8.8pt;margin:0;line-height:1.3">{"".join(f"<li>{R(s) if T else '<div class=wline></div>'}</li>" for s in S12)}</ol>
{sub("B", "Each dialogue has mistakes (underlined; one is correct). Correct them. Then listen and check.", "4 min", "R1.3")}
<div class="two"><div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.5pt;line-height:1.45"><b>Dialogue 1</b><br>{dlg(d1)}</div>
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.5pt;line-height:1.45"><b>Dialogue 2</b><br>{dlg(d2)}</div></div>
<p class="small">{R("1: look like ✓ · was · Have you been living · working · to do · Would you? — 2: have you been doing · have to · Do you have to · mustn't · turned it down · traveling")}</p>""",
    28, """<ol><li>A: the track has a 6-second pause after each sentence; pause more if needed. Check contractions (<i>He's been</i>) and weak forms.</li>
<li>B: then role-play the dialogues with the student; change roles. The reply question must match the auxiliary: <i>I'd love… — Would you?</i></li></ol>""")

    # Page 7 - Speaking
    b.page(f"""{sec(7, "Speaking: long turn and interview", "9 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE FROM UNITS 01–09</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>keep a conversation going</th><th>describe people</th><th>talk about change</th><th>give opinions</th></tr>
<tr><td><i>Really? · Do you? · How long have you…? · What was that like?</i></td><td><i>He can be a bit… · She looks like… · I'd say she's in her…</i></td><td><i>I used to… · These days… · More and more…</i></td><td><i>If you ask me… · I see your point, but… · On the whole…</i></td></tr></table></div>
{sub("A", "Long turn. Choose one card. Prepare for one minute, then talk for two minutes.", "5 min")}
<div style="display:flex;gap:2mm;font-size:8.5pt;margin:.5mm 0">
<div class="msg" style="max-width:none;flex:1;padding:1.5mm 2.5mm"><b>Card 1: A person who changed my life</b><br>what they look like · what they're like · how you met · how they changed your life</div>
<div class="msg" style="max-width:none;flex:1;padding:1.5mm 2.5mm"><b>Card 2: My working life</b><br>what you do (or study) · what you have to do · how long you've been doing it · what you'd like to do next</div>
<div class="msg" style="max-width:none;flex:1;padding:1.5mm 2.5mm"><b>Card 3: Then and now</b><br>what you used to do · what you've stopped doing · what you've started · how your city is changing</div></div>
{sub("B", "Interview. Your teacher interviews you for a job or a course you would like. Then change roles.", "4 min")}
<p style="margin:.3mm 0;font-size:8.6pt">{R("Teacher's questions: Tell me about yourself. How long have you been studying / working…? What did you use to do before? What are you good at? What's your greatest weakness? Do you have any questions? Give feedback on one strength and one thing to improve.") if T else ""}</p>""",
    28, """<ol><li>A: let the student choose; note mistakes for the reflection on page 8. Fluency option (3-2-1): the same talk in 2 minutes, then in 1 minute.</li>
<li>B: keep it realistic but friendly. Listen especially for questions, the present perfect continuous and verb patterns.</li></ol>""")

    # Page 8 - Reflect
    ck = [("01", "I can start and keep a conversation going with a new person."), ("02", "I can describe character and feelings politely."),
          ("03", "I can talk about the past and the present (used to, present perfect)."), ("04", "I can describe people's appearance in detail."),
          ("05", "I can use verbs + to + infinitive or -ing."), ("06", "I can describe a job (have to, don't have to, mustn't)."),
          ("07", "I can answer interview questions (present perfect continuous)."), ("08", "I can talk about types of work with phrasal verbs."), ("09", "I can describe trends and changes.")]
    ckr = "".join(f"<tr><td><b>Unit {u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in ck)
    b.page(f"""{sec(8, "Reflect and homework", "4 min")}
{sub("A", "How are you doing? Check one box for each line.", "1 min")}
<table class="ck" style="font-size:8.4pt"><tr><th style="width:15mm"></th><th>In English…</th><th style="width:15mm">Easy!</th><th style="width:15mm">Sometimes</th><th style="width:15mm">Not yet</th></tr>{ckr}</table>
{sub("B", "My language notes. Look at your notes from Units 01–09. Which mistake do you still make? What are your two goals for Units 11–19?", "2 min")}
{lines(3)}
{sub("C", "Homework: writing (100–150 words)", "1 min")}
<p style="margin:.3mm 0"><b>Then and now: me and my English.</b> Write about how your life and your English have changed. Use at least five of these: <i>used to · I've been… for / since · a verb + -ing · a verb + to · have to / don't have to · a phrasal verb · more and more</i>.</p>
{lines(6)}""",
    22, """<p>Use the "Not yet" lines to plan extra practice before Unit 11. Keep the writing as a sample to compare with Review 2.</p>""")

    def scr(lst):
        return "<br>".join(f"<b>{n}:</b> {t}" if n != "Narrator" else f"<i>{t}</i>" for n, t in lst)
    b.extra("Audio scripts", f"""
{sub("R1.1", "Gap Year Diaries: a special episode (natural and slow)")}
<p style="line-height:1.3;font-size:8.3pt">{scr(SCRIPT)}</p>
{sub("R1.2", "Dictation: weak forms (6-second pauses)")}
<p style="font-size:8.6pt">{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S12))}</p>
{sub("R1.3", "Two dialogues (correct versions)")}
<p style="line-height:1.3;font-size:8.3pt">{scr(S13)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 10 - Review 1")
