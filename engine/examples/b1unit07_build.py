# Speak! Progress B1 - Unit 07 "Attending a job interview" (all English) - lean B1 format (rebuilt 2026-11-19)
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

    # 1 Warm-up
    cover = cover_html(T, "LEVEL B1 · UNIT 07", "Attending a job interview", "Interviews and applications · <b>present perfect continuous · for / since</b>",
                       [("YOU CAN", "understand a job interview, answer typical interview questions and write a job application"),
                        ("LANGUAGE", "How long have you been working…? · I've been taking classes since… · for three months"),
                        ("PRONUNCIATION", "weak <i>been</i> /bɪn/")])
    tr = [("Julia is always at her desk before everyone else.", "punctual"), ("Leo wants to run his own company one day.", "ambitious"),
          ("Betty keeps spelling clients' names wrong.", "careless"), ("Carlos always supports his coworkers.", "a team player"),
          ("You can always count on Rosa. She does what she promises.", "reliable"), ("Sam is happy to change his plans or his schedule.", "flexible")]
    trl = [f'<li value="{i+1}">{s} {A(t, "min-width:22mm")}</li>' for i, (s, t) in enumerate(tr)]
    b.page(f"""{sec(1, "Warm-up: the right person for the job", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["Have you ever had a job interview? How did it go?", "How do you feel before an interview or an important exam?", "What's the most difficult question in an interview?"], "START TALKING")}</div></div>
{sub("A", "Key words. Match the people to the qualities in the box.", "3 min")}
<div class="bank">ambitious · careless · flexible · punctual · reliable · a team player</div>
<div style="font-size:8.5pt">{twocol(trl, 3)}</div>
{talk(["Which two qualities from A describe you? Give an example.", "Which quality is the most important in your job or studies? Why?"], "USE THE WORDS")}""",
    26, """<ol><li>Top box: if the student has never had an interview, ask about exams or a first day at work.</li>
<li>A: <i>careless</i> is the only negative quality. <i>Reliable</i> and <i>a team player</i> are very common in job ads.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Danny's job interview: which questions · details · Talk about it", "Present perfect continuous · for / since",
                      "Complete from the interview · for or since · Use it (oral)", "Functional language · weak been (07.2) · interview role-play",
                      "Article: five things never to say · How long questions · word choice · writing"),
        "Linguahouse uses an interview for a sales job. We wrote an original interview: Danny applies to be a guide at <b>City Steps Tours</b> (a fictional walking-tour company in São Paulo). The manager, Carla, is a one-off voice (Studio-O). Danny has been in São Paulo for about three months, has been taking Portuguese classes, worked at a supermarket in Chicago last year (B1 Unit 03), has been helping Mrs. Lima at the hostel, and runs with Bruno's group in Ibirapuera Park (B1 Unit 05). The Linguahouse article \"Never say these things in a job interview\" is rewritten for the homework.",
        "Students use the present tense for duration (<i>I live here for three months</i>, <i>I'm working here since 2022</i>), confuse <i>for</i> and <i>since</i>, say <i>I have experience of two years</i>, <i>apply to a job</i>, and call a résumé a <i>curriculum</i>.",
        "Track 07.1 Danny's job interview (natural and slow) · Track 07.2 Repeat: weak been"))

    # 2 Listening
    qs = [("Tell me a little about yourself.", True), ("Why are you leaving your job?", False), ("How long have you been living in São Paulo?", True),
          ("Do you have any experience working with the public?", True), ("What are your salary requirements?", False), ("Why do you want to work for us?", True),
          ("Where do you see yourself in five years?", False), ("What would you say is your greatest weakness?", True)]
    qsl = [f'<li value="{i+1}">☐ {q} {R("✓") if (T and ok) else ""}</li>' for i, (q, ok) in enumerate(qs)]
    mc = [("How long has Danny been living in São Paulo?", ["about two months", "about three months", "about a year"], "about three months"),
          ("What has he been doing at the hostel?", ["cleaning the rooms", "showing guests around", "working at reception"], "showing guests around"),
          ("What is his greatest weakness?", ["He's shy.", "He's not very organized.", "He's always late."], "He's not very organized."),
          ("What happens next?", ["He starts tomorrow.", "They'll call him by Friday.", "He has a second interview."], "They'll call him by Friday.")]
    mcl = "".join(f"<li>{q}<br>{ch(o, a)}</li>" for q, o, a in mc)
    b.page(f"""{sec(2, "Listening: Danny's job interview", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{audiocard(["07.1 · NATURAL", "07.1 · SLOW"])}
{sub("A", "Danny has an interview for a job as a tour guide. Listen. Tick the questions Carla asks.", "3 min", "07.1")}</div>{img('B', 40, 27)}</div>
<div style="font-size:8.5pt">{twocol(qsl, 4)}</div>
{sub("B", "Listen again and choose.", "3 min")}
<ol style="line-height:1.4;font-size:8.6pt;margin:0;column-count:2;column-gap:5mm">{mcl}</ol>
{talk(["Danny makes two small mistakes in the interview. What are they?", "Would you give Danny the job? Why or why not?", "Which question in A is the hardest for you to answer?"])}""",
    26, """<ol><li>A–B: 6 minutes. Five questions are asked; the other three are typical interview questions for the role-play.</li>
<li>Talk about it: 6 minutes. 1: he says he really needs the money, and he almost says he has no questions. He corrects himself (<i>I mean…</i>), a useful strategy.</li></ol>""")

    # 3 Grammar reference
    lean.grammar_in_class(b, grammar_ref.present_perfect_continuous)

    # 4 Practice
    ex = [("How long", "have you been living", "(you / live) in São Paulo?"), ("I", "'ve been taking", "(take) classes since I arrived."),
          ("For the last two months, I", "'ve been helping", "(help) the owner of my hostel.")]
    exl = "".join(f"<li>{a} {A(f, 'min-width:30mm')} {e}</li>" for a, f, e in ex)
    fs = [("three months", "for"), ("I arrived", "since"), ("2023", "since"), ("ages", "for"), ("last Monday", "since"), ("a long time", "for")]
    fsl = " &nbsp;·&nbsp; ".join(f"{A(a, 'min-width:9mm')} {t}" for t, a in fs)
    use = ["How long have you been studying English?", "How long have you been living in your home?", "How long have you been working or studying where you are now?",
           "How long have you known your best friend? (known, not been knowing)", "Ask your teacher three questions with <i>How long have you been…?</i>"]
    b.page(f"""{sec(4, "Practice: how long have you been…?", "10 min")}
{sub("A", "Complete the sentences from the interview.", "2 min")}
<ol style="line-height:1.7;font-size:8.9pt;margin:0">{exl}</ol>
{sub("B", "For or since? Write.", "2 min")}
<p style="margin:.3mm 0;font-size:8.8pt;line-height:1.9">{fsl}</p>
<div class="box sand"><h4>RULE</h4><b>have / has + been + -ing</b> → an activity that started in the past and continues now · <b>for</b> + a period · <b>since</b> + a point in time · present perfect simple with state verbs (<i>I've known her…</i>) · past simple for finished time. See the <b>Grammar reference</b> on page 3.</div>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    24, """<ol><li>A–B: 4 minutes. Draw a timeline: the activity starts in the past and continues to now.</li>
<li>Use it: 6 minutes, all oral. Brazilians often use the present for duration; correct <i>I live here for…</i> every time.</li></ol>""")

    # 5 Speaking
    b.page(f"""{sec(5, "Speaking: the interview", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>strengths</th><th>weaknesses</th><th>buy time</th><th>ask questions</th></tr>
<tr><td><i>I'm good at… · I've been working with… for… · I'm used to…</i></td><td><i>I tend to… · I'm working on it. · I've been trying to…</i></td><td><i>That's a good question. · Let me think. · Well, to be honest…</i></td><td><i>What would a typical day be like? · When would I start? · What's the next step?</i></td></tr></table></div>
{audiocard(["07.2"])}
{sub("A", "Weak been. Listen and repeat: I've_been_working /bɪn/.", "4 min", "07.2")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.55">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S072))}</p>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("B", "Role-play. Choose a job you would like. Your teacher interviews you. Start with &ldquo;Tell me about yourself.&rdquo; Then change roles: you are the interviewer.", "10 min")}
<p style="margin:.3mm 0;font-size:8.6pt">{R("Teacher's questions: Tell me about yourself. How long have you been working / studying…? Why do you want this job? What's your greatest weakness? How do you deal with pressure? Do you have any questions for me? At the end, say if you'd give the student the job and why.") if T else ""}</p></div>{img('D', 32, 24)}</div>
{talk(["Is it OK to lie a little in a job interview? Why or why not?", "What's the best advice you've ever had about work?"])}""",
    28, """<ol><li>A: <i>been</i> is weak /bɪn/ and <i>have</i> is contracted. B: make the interview realistic (formal, a little challenging), then give feedback on content and language.</li>
<li>Talk about it: last 3 minutes: wrap-up (two corrections and <i>Can you answer interview questions?</i>).</li></ol>""")

    # H Homework
    adv = [("How much will I earn?", "1"), ("I'm really nervous.", "2"), ("My weakness is that I work too hard.", "3"), ("My current boss is horrible.", "4"), ("No, I don't have any questions.", "5")]
    advl = " &nbsp; ".join(f"<b>{chr(97+i)}</b> \"{s}\" {A(n, 'min-width:5mm')}" for i, (s, n) in enumerate(adv))
    paras = ["Don't ask about money too early. The interviewer may think that you are only interested in the salary.",
             "Employers want confident people. Even if you are feeling stressed, try not to show it.",
             "Interviewers have heard this answer a thousand times. Talk about a real weakness and what you have been doing to improve.",
             "Never criticize a former employer. It makes you sound negative.",
             "This makes you look unprepared. Always prepare two or three questions about the job."]
    art = " ".join(f'<b style="color:#176074">{i+1}</b> {p}' for i, p in enumerate(paras))
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Read the article. Match the things you should never say (a–e) to paragraphs 1–5.", "")}</div>{img('C', 28, 18)}</div>
<div class="box" style="font-size:8.5pt;line-height:1.45;margin:.5mm 0"><b>Five things you should never say in a job interview</b><br>{art}</div>
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.8">{advl}</p>
{sub("B", "Correct the sentences.", "")}
<p style="margin:.3mm 0;line-height:1.8;font-size:8.7pt">I live in this city since 2019. → {A("I've been living / I've lived in this city since 2019.", "min-width:60mm")}<br>I've been knowing Ana for months. → {A("I've known Ana for months.", "min-width:60mm")}</p>
{lean.watch_out([("I sent my curriculum.", "I sent my résumé.", "American English: <i>résumé</i>; British English: <i>CV</i>."), ("I'm applying to the job.", "I'm applying for the job.", "<i>apply for</i> a job; <i>apply to</i> a company."), ("I have experience of two years.", "I have two years of experience.", "number + years + <i>of experience</i>.")])}
{lean.writing_task(sub, "A job application: write an email to apply for a job or a volunteer position.", "Dear…, I am writing to apply for the position of… I have been working as… for…", ["have been + -ing", "for / since", "three qualities", "100–150 words"], "I can answer interview questions and write a job application.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class. A formal email doesn't use contractions. Check <i>for / since</i> and the layout (greeting, reason for writing, experience, availability, ending).</p>""")

    script = "".join(f"<p style='margin:.5mm 0'><b>{('Carla' if l.split(': ', 1)[0] == 'Interviewer' else l.split(': ', 1)[0])}:</b> {l.split(': ', 1)[1]}</p>" for l in S071)
    b.extra("Audio script", f"""
{sub("07.1", "Danny's job interview (natural and slow)")}
<div style="line-height:1.33;font-size:8.5pt">{script}</div>
{sub("07.2", "Repeat: weak been")}
<p>{" · ".join(S072)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 07 - Attending a job interview")
