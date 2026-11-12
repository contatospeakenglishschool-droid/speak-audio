# Speak! Progress B1 - Unit 07 "Attending a job interview" (all English) - B1 format (2026-11-09)
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Progress"
setup(band="B1 · UNIT 07", audio_json="audio_b1-unit-07.json", img_dir="img")



_r = json.load(open("roteiro.json"))["units"]["b1-unit-07"]
S071 = _r["07.1 Danny's job interview"].split("\n")
S072 = [x.split(": ", 1)[1] for x in _r["07.2 Repeat: weak been"].split("\n")]


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
    cover = cover_html(T, "LEVEL B1 · UNIT 07", "Attending a job interview", "Interviews and applications · <b>present perfect continuous · for / since</b>",
                       [("YOU CAN", "understand a job interview, answer typical interview questions and write a job application"),
                        ("LANGUAGE", "How long have you been working…? · I've been taking classes since… · for three months"),
                        ("PRONUNCIATION", "weak <i>been</i> /bɪn/")])
    tr = [("Mike doesn't mind stress. In fact, it helps him work better.", "able to work under pressure"), ("Julia is always at her desk before everyone else.", "punctual"),
          ("Leo wants to run his own company one day.", "ambitious"), ("Dave double-checks everything and rarely makes mistakes.", "careful"),
          ("Betty keeps spelling clients' names wrong in her emails.", "careless"), ("Carlos always supports his coworkers and listens to their ideas.", "a team player"),
          ("You can always count on Rosa. She does what she promises.", "reliable"), ("Sam is happy to change his plans or his schedule.", "flexible")]
    trl = [f'<li value="{i+1}">{s} {A(t, "min-width:22mm")}</li>' for i, (s, t) in enumerate(tr)]
    b.page(f"""{sec(1, "Warm-up: the right person for the job", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 58, 38)}<div style="flex:1">
{sub("A", "Discuss with your teacher.", "3 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0"><li>Have you ever had a job interview? How did it go?</li><li>How do you feel before an interview or an important exam?</li><li>What's the most difficult question in an interview?</li></ol></div></div>
{sub("B", "Key words. Match the people to the qualities in the box.", "4 min")}
<div class="bank">able to work under pressure · ambitious · careful · careless · flexible · punctual · reliable · a team player</div>
<div style="font-size:8.5pt">{twocol(trl, 4)}</div>
{sub("C", "Which three qualities from B describe you? Which one is important for your job?", "1 min")}""",
    25, """<ol><li>A: if the student has never had an interview, ask about exams or a first day at work.</li>
<li>B: <i>careless</i> is the only negative quality. <i>Reliable</i> (you can trust them) and <i>a team player</i> are very common in job ads.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 60 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Discussion · key words: qualities for a job</td><td>1</td></tr>
<tr><td>2 Listening</td><td>12 min</td><td>Danny's job interview at City Steps Tours</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>8 min</td><td>Present perfect continuous · for / since</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>The present perfect continuous (study at home)</td><td>4</td></tr>
<tr><td>4 Vocabulary lab + pronunciation</td><td>8 min</td><td>Applying for a job · opposite qualities · weak <i>been</i></td><td>5</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Article: things you should never say · how long…?</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Functional language · long turn: tell me about yourself · interview role-play</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>4 min</td><td>Can-do · language notes · writing homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY</h4>Linguahouse uses an interview with a woman called Kate Willis for a sales job. We wrote an original interview: Danny applies to be a guide at <b>City Steps Tours</b> (a fictional walking-tour company in São Paulo). The manager, Carla, is a one-off voice (Studio-O). Danny has been in São Paulo for about three months, has been taking Portuguese classes, worked at a supermarket in Chicago last year (B1 Unit 03), has been helping Mrs. Lima at the hostel, and runs with Bruno's group in Ibirapuera Park (B1 Unit 05). The Linguahouse article "Never say these things in a job interview" is rewritten as the Practice text. In the writing model, Lucy (Chicago, biology student) applies to volunteer at an animal shelter.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students use the present tense for duration (<i>I live here for three months</i>, <i>I'm working here since 2022</i>), confuse <i>for</i> and <i>since</i>, say <i>I have experience of two years</i>, <i>apply to a job</i>, and call a résumé a <i>curriculum</i>.</div>
<div class="box"><h4>AUDIO</h4>Track 07.1 Danny's job interview (natural and slow) · Track 07.2 Repeat: weak been</div>""")

    # Page 2 - Listening
    qs = [("Tell me a little about yourself.", True), ("Why are you leaving your job?", False), ("How long have you been living in São Paulo?", True),
          ("Do you have any experience working with the public?", True), ("What are your salary requirements?", False), ("Why do you want to work for us?", True),
          ("Where do you see yourself in five years?", False), ("What would you say is your greatest weakness?", True)]
    qsl = [f'<li value="{i+1}">☐ {q} {R("✓") if (T and ok) else ""}</li>' for i, (q, ok) in enumerate(qs)]
    mc = [("How long has Danny been living in São Paulo?", ["about two months", "about three months", "about a year"], "about three months"),
          ("Since when has he been taking Portuguese classes?", ["since he arrived", "since last year", "since last month"], "since he arrived"),
          ("What has he been doing at the hostel?", ["cleaning the rooms", "showing guests around", "working at reception"], "showing guests around"),
          ("Why are long walking tours not a problem for him?", ["He's been running.", "He used to be a guide.", "He has a car."], "He's been running."),
          ("What is his greatest weakness?", ["He's shy.", "He's not very organized.", "He's always late."], "He's not very organized."),
          ("What happens next?", ["He starts tomorrow.", "They'll call him by Friday.", "He has a second interview."], "They'll call him by Friday.")]
    mcl = "".join(f"<li>{q}<br>{ch(o, a)}</li>" for q, o, a in mc)
    b.page(f"""{sec(2, "Listening: Danny's job interview", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{audiocard(["07.1 · NATURAL", "07.1 · SLOW"])}
{sub("A", "Listen at natural speed. Tick the questions Carla asks.", "3 min", "07.1")}</div>{img('B', 40, 27)}</div>
<div style="font-size:8.5pt">{twocol(qsl, 4)}</div>
{sub("B", "Listen again and choose the correct answer. Use the slow version if you need it.", "5 min")}
<ol style="line-height:1.4;font-size:8.6pt;margin:0;column-count:2;column-gap:5mm">{mcl}</ol>
{sub("C", "Think about it. Discuss with your teacher.", "4 min")}
<ol style="line-height:1.4;font-size:8.8pt;margin:0"><li>Danny makes two small mistakes in the interview. What are they? {R("He says he really needs the money, and he almost says he has no questions.") if T else ""}</li>
<li>Would you give Danny the job? Why or why not? {R("Personal.") if T else ""}</li></ol>
<div class="box sand" style="margin-top:1mm"><h4>NOTICE: USEFUL CHUNKS</h4><i>Thanks for inviting me. · I'm used to dealing with customers. · Not at all. · I'm in good shape. · I mean… · Thank you so much for your time.</i></div>""",
    25, """<ol><li>A: play the natural version once. Five questions are asked; the other three are typical interview questions for the role-play on page 7.</li>
<li>C: Danny corrects himself (<i>I mean…</i>), which is a useful strategy. <i>Rain or shine</i> = in any weather.</li></ol>""")

    # Page 3 - Language focus
    ex = [("How long", "have you been living", "(you / live) in São Paulo?"), ("I", "'ve been taking", "(take) classes since I arrived."),
          ("For the last two months, I", "'ve been helping", "(help) the owner of my hostel."), ("I", "'ve been using", "(use) a planner app on my phone.")]
    exl = "".join(f"<li>{a} {A(f, 'min-width:30mm')} {e}</li>" for a, f, e in ex)
    fs = [("three months", "for"), ("I arrived", "since"), ("2023", "since"), ("ages", "for"), ("last Monday", "since"), ("a long time", "for"), ("I was a child", "since"), ("two weeks", "for")]
    fsl = " &nbsp;·&nbsp; ".join(f"{A(a, 'min-width:9mm')} {t}" for t, a in fs)
    cs = [(["I've been writing", "I've written"], "I've written", "ten emails this morning."), (["I've been knowing", "I've known"], "I've known", "Bruno since August."),
          (["You look tired. Have you been working", "Have you worked"], "You look tired. Have you been working", "all day?"), (["I worked", "I've been working"], "I worked", "at a supermarket last year.")]
    csl = "".join(f"<li>{ch(o, a)} {e}</li>" for o, a, e in cs)
    b.page(f"""{sec(3, "Language focus: how long have you been…?", "8 min")}
{sub("A", "Complete the sentences from the interview.", "3 min")}
<ol style="line-height:1.7;font-size:8.9pt;margin:0">{exl}</ol>
{sub("B", "For or since? Write.", "2 min")}
<p style="margin:.3mm 0;font-size:8.8pt;line-height:1.9">{fsl}</p>
{sub("C", "Choose the correct option.", "3 min")}
<ol style="line-height:1.7;font-size:8.9pt;margin:0">{csl}</ol>
<div class="box sand"><h4>RULE</h4><b>have / has + been + -ing</b> → an activity that started in the past and continues now: <i>I've been living here for three months.</i> · <b>for</b> + a period · <b>since</b> + a point in time · use the <b>present perfect simple</b> for results and numbers (<i>ten emails</i>) and with state verbs (<i>know, like, have</i>) · use the <b>past simple</b> for finished time (<i>last year</i>). More on the next page: <b>Grammar reference</b>.</div>""",
    24, """<ol><li>A: draw a timeline: the activity starts in the past and the line continues to now.</li>
<li>C: Brazilians often use the present for duration. Ask real questions: <i>How long have you been studying English? How long have you known your best friend?</i></li></ol>""")

    grammar_ref.present_perfect_continuous(b)

    # Page 5 - Vocabulary lab
    st = [("see a job ad and", "apply for", "the job"), ("send your", "résumé", "and a cover letter"), ("be", "invited", "to an interview"),
          ("have a second", "interview", "with the director"), ("get a job", "offer", ""), ("accept the offer and", "start", "the new job")]
    stl = " → ".join(f"{a} {A(w, 'min-width:15mm')} {e}".strip() for a, w, e in st)
    op = [("reliable", "unreliable"), ("organized", "disorganized"), ("patient", "impatient"), ("responsible", "irresponsible"), ("flexible", "inflexible"), ("honest", "dishonest")]
    opl = " &nbsp;·&nbsp; ".join(f"{a} ↔ {A(o, 'min-width:18mm')}" for a, o in op)
    b.page(f"""{sec(4, "Vocabulary lab: getting a job", "4 min")}
{sub("A", "The steps to a new job. Complete with the words in the box.", "2 min")}
<div class="bank">apply for · interview · invited · offer · résumé · start</div>
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.9">{stl}</p>
{sub("B", "Word building. Write the opposite with un-, dis-, im- or ir-.", "2 min")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.9">{opl}</p>
<div class="box sand"><h4>WATCH OUT: WORD CHOICE</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>I sent my curriculum.</td><td><b>I sent my résumé.</b></td><td>American English: <i>résumé</i> (or <i>resume</i>); British English: <i>CV</i>.</td></tr>
<tr><td>I'm applying to the job.</td><td><b>I'm applying for the job.</b></td><td><i>apply for</i> a job; <i>apply to</i> a company or university.</td></tr>
<tr><td>I have experience of two years.</td><td><b>I have two years of experience.</b></td><td>number + years + <i>of experience</i>.</td></tr>
<tr><td>I'm working here since 2022.</td><td><b>I've been working here since 2022.</b></td><td>use the present perfect with <i>since / for</i>.</td></tr></table></div>
{sec(5, "Pronunciation lab: weak been", "4 min")}
<p class="small" style="margin:.3mm 0">In the present perfect continuous, <i>been</i> is weak: /bɪn/, not /biːn/, and <i>have</i> is usually contracted: <i>I've_been_working · She's_been_studying</i>.</p>
{audiocard(["07.2"])}
{sub("A", "Listen and repeat. Then ask your teacher three questions with How long have you been…?", "4 min", "07.2")}
<p style="margin:.3mm 0;font-size:8.8pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S072))}</p>""",
    24, """<ol><li>A: a <i>cover letter</i> is the letter or email you send with your résumé. In American English, people say <i>résumé</i>; <i>CV</i> is used for academic jobs.</li>
<li>B: <i>im-</i> before p (<i>impatient</i>), <i>ir-</i> before r (<i>irresponsible</i>).</li></ol>""")

    # Page 6 - Practice
    adv = [("How much will I earn?", "1"), ("I'm really nervous.", "2"), ("My weakness is that I work too hard.", "3"), ("My current boss is horrible.", "4"), ("No, I don't have any questions.", "5")]
    advl = " &nbsp; ".join(f"<b>{chr(97+i)}</b> \"{s}\" {A(n, 'min-width:5mm')}" for i, (s, n) in enumerate(adv))
    paras = ["Don't ask about money too early. The interviewer may think that you are only interested in the salary. Wait until the end, or until they mention it.",
             "Employers want confident people. Even if you are feeling stressed, try not to show it. Take a deep breath and smile.",
             "Interviewers have heard this answer a thousand times. Talk about a real weakness that isn't very important for the job, and explain what you have been doing to improve.",
             "Never criticize a former employer. It makes you sound negative, and the interviewer will wonder what you will say about them one day.",
             "This makes you look unprepared or not interested. Always prepare two or three questions about the job or the company."]
    art = "".join(f'<p style="margin:0 0 .8mm"><b style="color:#176074">{i+1}</b> {p}</p>' for i, p in enumerate(paras))
    hl = [("you / study English?", "How long have you been studying English?"), ("you / live in your home?", "How long have you been living in your home?"),
          ("you / work or study at your current place?", "How long have you been working / studying there?"), ("you / know your best friend?", "How long have you known your best friend?")]
    hll = "".join(f"<li>How long ({q}) {A(a, 'min-width:50mm') if T else '<div class=wline></div>'}</li>" for q, a in hl)
    b.page(f"""{sec(6, "Practice", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Read the article. Match the things you should never say (a–e) to paragraphs 1–5.", "4 min")}</div>{img('C', 30, 20)}</div>
<div class="box" style="font-size:8.6pt;line-height:1.4"><b style="font-size:9.3pt">Five things you should never say in a job interview</b><br>{art}</div>
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.8">{advl}</p>
{sub("B", "Write the questions. Then ask your teacher and answer them yourself.", "4 min")}
<ol style="line-height:1.5;font-size:8.8pt;margin:0">{hll}</ol>""",
    22, """<ol><li>A: then ask: <i>Do you agree with the advice? Is it ever OK to ask about money?</i></li>
<li>B: question 4 uses <i>known</i>, not <i>been knowing</i> (state verb).</li></ol>""")

    # Page 7 - Speaking
    b.page(f"""{sec(7, "Speaking: the interview", "12 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>strengths</th><th>weaknesses</th><th>buy time</th><th>ask questions</th></tr>
<tr><td><i>I'm good at… · I've been working with… for… · I'm used to…</i></td><td><i>I tend to… · I'm working on it. · I've been trying to…</i></td><td><i>That's a good question. · Let me think. · Well, to be honest…</i></td><td><i>What would a typical day be like? · When would I start? · What's the next step?</i></td></tr></table></div>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("A", "Long turn. Prepare for one minute, then answer the classic question \"Tell me about yourself\" for two minutes.", "5 min")}
<ul style="line-height:1.45;font-size:8.9pt;margin:0"><li>who you are and what you do</li><li>what you have been doing recently</li><li>your experience and strengths</li><li>your goals for the future</li></ul></div>{img('D', 32, 24)}</div>
{sub("B", "Role-play. Choose a job you would like. Your teacher interviews you. Then change roles: you are the interviewer.", "5 min")}
<p style="margin:.3mm 0;font-size:8.6pt">{R("Teacher's questions: How long have you been working / studying…? Why do you want this job? What can you offer us? What's your greatest weakness? How do you deal with pressure? Do you have any questions for me? At the end, say if you would give the student the job and why.") if T else ""}</p>
{sub("C", "Talking point. Discuss with your teacher.", "2 min")}
<ol style="line-height:1.5;font-size:8.9pt;margin:0"><li>Is it OK to lie a little in a job interview? Why or why not?</li></ol>""",
    28, """<ol><li>A: don't interrupt; note mistakes for the error log (page 8), especially duration (<i>I live here for…</i>). Fluency option (3-2-1): the same talk in 2 minutes, then in 1 minute.</li>
<li>B: make the interview realistic (formal, a little challenging). Then give feedback on content and language.</li></ol>""")

    # Page 8 - Wrap-up
    pc = ["I can understand a job interview (questions, details, impressions).", "I can use the present perfect continuous with <i>for</i> and <i>since</i>.",
          "I can answer typical interview questions and talk about myself."]
    pcr = "".join(f"<tr><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for s in pc)
    b.page(f"""{sec(8, "Wrap-up and homework", "4 min")}
{sub("A", "Can-do check", "1 min")}
<table class="ck" style="font-size:8.6pt"><tr><th>In English…</th><th style="width:16mm">Easy!</th><th style="width:16mm">Sometimes</th><th style="width:16mm">Not yet</th></tr>{pcr}</table>
{sub("B", "My language notes. Write three corrections from today's class.", "2 min")}
<div style="display:flex;gap:5mm;font-size:8.6pt"><div style="flex:1"><b>I said…</b>{lines(3)}</div><div style="flex:1"><b>Better:</b>{lines(3)}</div></div>
{sub("C", "Homework: writing (100–150 words)", "1 min")}
<p style="margin:.3mm 0"><b>A job application.</b> Write an email to apply for a job or a volunteer position. Read Lucy's email first.</p>
<div class="box" style="font-size:8.6pt;line-height:1.4;margin:.5mm 0"><i>Dear Ms. Parker,<br>I am writing to apply for the volunteer position at Lakeside Animal Shelter, which I saw on your website. I am a biology student at a college in Chicago, and I have been working as a weekend barista for two years, so I am used to working under pressure and dealing with the public. I have loved animals since I was a child, and I am planning to become a vet. I have been helping a neighbor with her dogs for the last six months, and I am reliable, patient and a good team player. I am available on Saturday and Sunday mornings. I have attached my résumé, and I would be happy to come in for an interview.<br>Best regards,<br>Lucy Miller</i></div>
<p class="small" style="margin:.3mm 0">Checklist: ☐ the job and where you saw it &nbsp;☐ two sentences with <i>have been + -ing</i> &nbsp;☐ <i>for / since</i> &nbsp;☐ three qualities &nbsp;☐ a polite ending &nbsp;☐ 100–150 words</p>
{lines(6)}""",
    30, """<ol><li>B (error log): during the lesson, note 3–5 real mistakes. Here, the student writes what they said and the better version; guide them to self-correct first.</li>
<li>C: a formal email doesn't use contractions. Check <i>for / since</i> and the layout (greeting, reason for writing, experience, availability, ending).</li></ol>""")

    script = "".join(f"<p style='margin:.5mm 0'><b>{('Carla' if l.split(': ', 1)[0] == 'Interviewer' else l.split(': ', 1)[0])}:</b> {l.split(': ', 1)[1]}</p>" for l in S071)
    b.extra("Audio script", f"""
{sub("07.1", "Danny's job interview (natural and slow)")}
<div style="line-height:1.33;font-size:8.5pt">{script}</div>
{sub("07.2", "Repeat: weak been")}
<p>{" · ".join(S072)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 07 - Attending a job interview")
