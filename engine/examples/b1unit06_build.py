# Speak! Progress B1 - Unit 06 "Describing jobs" (all English) - B1 format (2026-11-09)
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Progress"
setup(band="B1 · UNIT 06", audio_json="audio_b1-unit-06.json", img_dir="img")



_r = json.load(open("roteiro.json"))["units"]["b1-unit-06"]
S061 = [x.replace("twelve-hour", "12-hour") for x in _r["06.1 Gap Year Diaries: what do you do?"].split("\n")]
JOBS = [("accountant", "acCOUNtant"), ("architect", "ARchitect"), ("electrician", "elecTRIcian"), ("programmer", "PROgrammer"),
        ("photographer", "phoTOgrapher"), ("engineer", "engiNEER"), ("receptionist", "reCEPtionist"), ("manager", "MAnager")]


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
    cover = cover_html(T, "LEVEL B1 · UNIT 06", "Describing jobs", "What do you do? · <b>job phrases · have to, must, don't have to, mustn't</b>",
                       [("YOU CAN", "describe a job: responsibilities, skills and qualifications, and what it's like"),
                        ("LANGUAGE", "I work as a… · I'm responsible for -ing · It's my job to… · You have to… · You don't have to…"),
                        ("PRONUNCIATION", "word stress in job words")])
    kw = [("boring because it is long and always the same", "tedious"), ("very busy, with a lot to do", "hectic"),
          ("making you feel happy because it is useful or important", "rewarding"), ("very tiring", "exhausting"),
          ("a period of work, for example from 7 p.m. to 7 a.m.", "a shift"), ("the money you get every month for your work", "a salary"),
          ("a university course that you complete", "a degree"), ("the time when a piece of work must be finished", "a deadline")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:20mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Warm-up: the world of work", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 58, 38)}<div style="flex:1">
{sub("A", "Discuss with your teacher.", "3 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0"><li>What do you do, or what would you like to do?</li><li>What did you want to be when you were a child?</li><li>Which jobs are the most respected in Brazil? Which are the best paid?</li></ol></div></div>
{sub("B", "Key words. Write the words from the box next to the definitions.", "3 min")}
<div class="bank">a deadline · a degree · exhausting · hectic · rewarding · a salary · a shift · tedious</div>
<div style="font-size:8.8pt">{twocol(kwl, 4)}</div>
{sub("C", "Describe your job or your studies to your teacher. Use three words from B.", "2 min")}""",
    25, """<ol><li>A: if the student doesn't work, they can talk about their studies, a past job, or a family member's job (see the Linguahouse note: some students prefer not to talk about their own work).</li>
<li>B: <i>salary</i> is usually monthly or yearly; <i>wage</i> is usually paid by the hour or week. <i>Rewarding</i> is a very useful positive word for difficult jobs.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 60 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Discussion · key words: tedious, hectic, rewarding, shift…</td><td>1</td></tr>
<tr><td>2 Listening</td><td>12 min</td><td>Podcast: Danny interviews Ana (doctor) and Bruno (programmer)</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>8 min</td><td>Job phrases · have to, don't have to, mustn't</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Talking about work (study at home)</td><td>4</td></tr>
<tr><td>4 Vocabulary lab + pronunciation</td><td>8 min</td><td>Opposites · would make a good… · work collocations · word stress</td><td>5</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Kate's job ad · a job I know well</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Functional language · long turn: a job · guess the job · talking point</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>4 min</td><td>Can-do · language notes · writing homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY</h4>The Linguahouse lesson is vocabulary only, with a reading about a zookeeper. We built an original listening: Danny records an episode of his podcast <i>Gap Year Diaries</i>. Ana works in the emergency department of a big hospital in São Paulo (12-hour shifts, B1 Unit 04). Bruno is a programmer: he works from home for a software company in Porto Alegre, builds and tests apps for banks, learned online, and lives in the hostel because working alone is isolating. New voice for Bruno: <b>en-US-Chirp3-HD-Fenrir</b> (keep it). In the Practice, Kate (Sweet Kate Bakery, Chicago) writes a job ad for an assistant baker.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students drop the article (<i>I work as doctor</i>), use the infinitive after <i>responsible for</i>, confuse <i>don't have to</i> (not necessary) with <i>mustn't</i> (not allowed), and use false friends: <i>I'm formed in…</i> (= I have a degree in…), <i>professor</i> for a school teacher, and <i>chef</i> for a boss.</div>
<div class="box"><h4>AUDIO</h4>Track 06.1 Gap Year Diaries: what do you do? (natural and slow) · Track 06.2 Repeat: word stress in jobs</div>""")

    # Page 2 - Listening
    ws = [("I don't have to wear a suit.", "B"), ("Some nights I don't have time to eat.", "A"), ("I learned online.", "B"),
          ("It isn't as well-paid as people think.", "A"), ("I spend all day in front of a screen.", "B"), ("You can really change people's lives.", "A")]
    wsl = [f'<li value="{i+1}">{s} {A(w, "min-width:7mm")}</li>' for i, (s, w) in enumerate(ws)]
    rows = [("Job", "a doctor in an emergency department", "a programmer, working from home"),
            ("Responsibilities", "treating urgent patients; deciding who sees a doctor first; explaining things to families", "building and testing apps for banks; finding and fixing problems in the code"),
            ("Qualifications and skills", "a medical degree + years of training; quick decisions; staying calm", "no degree needed; good at solving problems; patient"),
            ("Good things", "rewarding; you can change people's lives", "well-paid; no suit, no traffic; can live anywhere"),
            ("Bad things", "hectic; 12-hour shifts; exhausting; not very well-paid", "a bit isolating; all day in front of a screen")]
    tbl = "".join(f"<tr><td style='width:24mm'><b>{r}</b></td><td>{R(a) if T else ''}</td><td>{R(c) if T else ''}</td></tr>" for r, a, c in rows)
    b.page(f"""{sec(2, "Listening: what do you do?", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{audiocard(["06.1 · NATURAL", "06.1 · SLOW"])}
{sub("A", "Listen at natural speed. Who says it? Write A (Ana) or B (Bruno).", "3 min", "06.1")}
<div style="font-size:8.5pt">{twocol(wsl, 3)}</div></div>{img('B', 40, 34)}</div>
{sub("B", "Listen again and complete the notes. Use the slow version if you need it.", "5 min")}
<table style="font-size:8.3pt;margin-top:.5mm"><tr><th></th><th>Ana</th><th>Bruno</th></tr>{tbl if T else "".join(f"<tr><td style='width:24mm;height:7mm'><b>{r}</b></td><td></td><td></td></tr>" for r, a, c in rows)}</table>
{sub("C", "Think about it. Discuss with your teacher.", "4 min")}
<ol style="line-height:1.4;font-size:8.8pt;margin:0"><li>Why does Bruno say, "That's why I live in a hostel!"? {R("Working from home is isolating; in a hostel he can meet and talk to people.") if T else ""}</li>
<li>Whose job would you prefer, Ana's or Bruno's? Why? {R("Personal.") if T else ""}</li></ol>
<div class="box sand" style="margin-top:1mm"><h4>NOTICE: USEFUL CHUNKS</h4><i>a job like that · You never know what's coming through the door. · It isn't as well-paid as people think. · Not really. · That's why… · I can't imagine doing anything else.</i></div>""",
    25, """<ol><li>A: play the natural version once. The slow version is support for B, not the first listening.</li>
<li>B: accept short notes in any order. The emergency department is often called the ER in the US.</li></ol>""")

    # Page 3 - Language focus
    ph = [("I work", "as", "a doctor."), ("I'm responsible for", "treating", "(treat) patients."), ("It's also my job", "to decide", "(decide) which patients…"),
          ("You need to be good at", "making", "(make) quick decisions."), ("It can", "get", "really hectic."), ("I work", "for", "a software company."), ("…but I work", "from", "home.")]
    phl = "".join(f"<li>{a} {A(f, 'min-width:16mm')} {e}</li>" for a, f, e in ph)
    ob = [(["has to", "doesn't have to"], "has to", "Ana", "work 12-hour shifts."), (["doesn't have to", "mustn't"], "doesn't have to", "Bruno", "wear a suit."),
          (["mustn't", "don't have to"], "mustn't", "In the ER, you", "panic."), (["has to", "doesn't need to"], "doesn't need to", "Bruno", "have a degree."),
          (["have to", "mustn't"], "have to", "Programmers", "be patient.")]
    obl = "".join(f"<li>{s} {ch(o, a)} {e}</li>" for o, a, s, e in ob)
    b.page(f"""{sec(3, "Language focus: talking about work", "8 min")}
{sub("A", "Complete the phrases from the podcast.", "3 min")}
<ol style="line-height:1.7;font-size:8.9pt;margin:0;column-count:2">{phl}</ol>
{sub("B", "Choose the correct option.", "3 min")}
<ol style="line-height:1.7;font-size:8.9pt;margin:0">{obl}</ol>
{sub("C", "Different meaning. Match.", "2 min")}
<p style="margin:.3mm 0;font-size:8.9pt;line-height:1.7"><b>1</b> You don't have to come to the meeting. {A("b", "min-width:6mm")} &nbsp; <b>2</b> You mustn't come to the meeting. {A("a", "min-width:6mm")} &nbsp;&nbsp; <b>a</b> It's not allowed. &nbsp; <b>b</b> It isn't necessary, but you can.</p>
<div class="box sand"><h4>RULE</h4><b>work as a / an</b> + job · <b>responsible for, good at</b> + -ing · <b>It's my job to</b> + infinitive · <b>It can get / I find it</b> + adjective · <b>have to / need to</b> = necessary · <b>don't have to / don't need to</b> = not necessary · <b>mustn't</b> = not allowed · past: <b>had to</b>. We use impersonal <b>you</b> to describe any job. More on the next page: <b>Grammar reference</b>.</div>""",
    24, """<ol><li>A: point out the forms: preposition + -ing (<i>for treating, at making</i>) and <i>my job to</i> + infinitive (Unit 05 verb patterns).</li>
<li>C: this is the key difference. Give a personal example: <i>I don't have to work on Sundays, but sometimes I do.</i></li></ol>""")

    grammar_ref.talking_about_work(b)

    # Page 5 - Vocabulary lab
    op = [("tedious", "exciting"), ("stressful", "relaxing"), ("well-paid", "badly paid"), ("challenging", "a piece of cake"), ("hectic", "quiet"), ("dangerous", "safe")]
    opl = " &nbsp;·&nbsp; ".join(f"{a} ↔ {A(o, 'min-width:16mm')}" for a, o in op)
    pp = [("Carla is very good with numbers, but she's shy and prefers to work alone.", "an accountant"), ("Pedro loves working with wood and is very good with his hands.", "a carpenter"),
          ("Beatriz is fascinated by buildings, creative and good at math.", "an architect"), ("Thiago is brave, fit and likes helping people in danger.", "a firefighter"),
          ("Julia is outgoing and confident, and she loves talking to strangers.", "a sales representative")]
    ppl = "".join(f"<li>{s} → She'd / He'd make a good {A(j, 'min-width:26mm')}</li>" for s, j in pp)
    co = [("Doctors often", "work", "long hours."), ("She", "earns", "a good salary."), ("We have to", "meet", "a deadline by Friday."),
          ("He worked hard and", "got", "promoted to manager."), ("I can", "work", "from home twice a week."), ("I'm tired. I need to", "take", "some time off.")]
    col = " &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {a} {A(v, 'min-width:12mm')} {e}" for i, (a, v, e) in enumerate(co))
    jl = " &nbsp; ".join(f"<b>{i+1}</b> {R(s) if T else w}" for i, (w, s) in enumerate(JOBS))
    b.page(f"""{sec(4, "Vocabulary lab: describing jobs", "4 min")}
{sub("A", "Opposites. Write the opposite from the box.", "1 min")}
<div class="bank">badly paid · exciting · a piece of cake · quiet · relaxing · safe</div>
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.8">{opl}</p>
{sub("B", "Who would make a good…? Choose from the box.", "1 min")}
<div class="bank">an accountant · an architect · a carpenter · a firefighter · a sales representative</div>
<ol style="line-height:1.55;font-size:8.6pt;margin:0">{ppl}</ol>
{sub("C", "Work collocations. Complete with earn, get, meet, take or work.", "2 min")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.8">{col}</p>
<div class="box sand"><h4>WATCH OUT: FALSE FRIENDS</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>I'm formed in law.</td><td><b>I have a degree in law.</b></td><td><i>formed</i> = given a shape.</td></tr>
<tr><td>my son's professor (at school)</td><td><b>my son's teacher</b></td><td><i>professor</i> = at a university.</td></tr>
<tr><td>My chef is very strict.</td><td><b>My boss is very strict.</b></td><td><i>chef</i> = a restaurant cook.</td></tr></table></div>
{sec(5, "Pronunciation lab: word stress in jobs", "4 min")}
{audiocard(["06.2"])}
{sub("A", "Listen and underline the stressed syllable. Then listen again and repeat.", "4 min", "06.2")}
<p style="margin:.3mm 0;font-size:9pt;line-height:1.7">{jl}</p>""",
    24, """<ol><li>B: model the structure <i>She'd make a good…</i> (= she has the right qualities). Ask: <i>What would you make a good…?</i></li>
<li>Pronunciation: <i>-ician</i> and <i>-tionist</i> words stress the syllable before the ending; <i>engineer</i> stresses the end. Brazilians often say <i>ar-CHI-tect</i>.</li></ol>""")

    # Page 6 - Practice
    pr = [(["baking", "bake"], "baking"), (["to keep", "keeping"], "to keep"), (["have to", "don't have to"], "have to"), (["don't have to", "mustn't"], "don't have to"),
          (["mustn't", "don't have to"], "mustn't"), (["working", "work"], "working"), (["get", "stay"], "get"), (["as", "like"], "as")]
    p = [ch(o, a) for o, a in pr]
    mb = ["He / She works as…", "He / She is responsible for…", "He / She has to…", "He / She doesn't have to…", "He / She finds the job…"]
    b.page(f"""{sec(6, "Practice", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Kate writes a job ad for her bakery. Choose the correct words.", "5 min")}</div>{img('C', 30, 20)}</div>
<div class="box" style="line-height:1.95;font-size:9pt"><b>Sweet Kate Bakery, Chicago, is looking for an assistant baker!</b><br>You'll be responsible for {p[0]} bread, cookies and cakes, and it's also your job {p[1]} the kitchen clean. You {p[2]} start at 5 a.m., so you need to love mornings! You {p[3]} have experience – we'll train you – but you {p[4]} be late, because our first customers arrive at 6:30. You need to be good at {p[5]} in a small team. The work can {p[6]} hectic on weekends and before holidays, but it's fun and rewarding. Have you ever wanted to work {p[7]} a baker? Come and talk to Kate!</div>
{sub("B", "Think of a person you know well. Write about his or her job. Then tell your teacher.", "3 min")}
<ol style="line-height:1.35;font-size:8.9pt;margin:0">{"".join(f"<li>{t}<div class='wline'></div></li>" for t in mb)}</ol>""",
    22, """<ol><li>A: ask the student why each answer is right (preposition + -ing, <i>my job to</i> + infinitive, necessary or not allowed).</li>
<li>B: ask follow-up questions: <i>Does he enjoy it? Would you like to do that job?</i></li></ol>""")

    # Page 7 - Speaking
    b.page(f"""{sec(7, "Speaking: jobs", "12 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>ask about a job</th><th>pros and cons</th><th>react</th><th>imagine</th></tr>
<tr><td><i>What do you do? · What does that involve? · Do you have to…?</i></td><td><i>The best thing about it is… · The downside is… · On the whole, …</i></td><td><i>That sounds rewarding! · I bet that's hard. · Really? I had no idea.</i></td><td><i>I'd love to work as… · I'd never want to be a… · I'd make a good…</i></td></tr></table></div>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("A", "Long turn. Prepare for one minute, then talk for two minutes about your job, your dream job or the job of someone you know.", "5 min")}
<ul style="line-height:1.45;font-size:8.9pt;margin:0"><li>what the job is and where</li><li>the main responsibilities</li><li>the skills and qualifications you need</li><li>what it's like: the good and bad things</li></ul></div>{img('D', 32, 24)}</div>
{sub("B", "Guess the job. Your teacher is thinking of a job. Ask up to ten yes / no questions. Then change roles.", "4 min")}
<p style="margin:.3mm 0;font-size:8.6pt"><i>Do you have to wear a uniform? · Is it well-paid? · Do you work with people? · Can it be dangerous? · Do you need a degree?</i></p>
<p style="margin:.3mm 0;font-size:8.6pt">{R("Teacher's cards: a zookeeper · a flight attendant · a private detective · a firefighter. Answer only yes or no; give a hint after five questions.") if T else ""}</p>
{sub("C", "Talking point. Discuss with your teacher.", "3 min")}
<ol style="line-height:1.5;font-size:8.9pt;margin:0"><li>Which jobs are very important but badly paid in Brazil? Why?</li><li>Would you prefer a well-paid, stressful job or a badly paid, relaxing one?</li></ol>""",
    28, """<ol><li>A: don't interrupt; note mistakes for the error log (page 8), especially articles, <i>responsible for</i> + -ing and <i>have to</i>. Fluency option (3-2-1): the same talk in 2 minutes, then in 1 minute.</li>
<li>B: encourage questions with <i>have to</i>, <i>need</i> and the adjectives from page 5.</li></ol>""")

    # Page 8 - Wrap-up
    pc = ["I can understand people describing their jobs in a podcast.", "I can use job phrases and <i>have to, don't have to, mustn't</i> correctly.",
          "I can describe a job: responsibilities, skills and what it's like."]
    pcr = "".join(f"<tr><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for s in pc)
    b.page(f"""{sec(8, "Wrap-up and homework", "4 min")}
{sub("A", "Can-do check", "1 min")}
<table class="ck" style="font-size:8.6pt"><tr><th>In English…</th><th style="width:16mm">Easy!</th><th style="width:16mm">Sometimes</th><th style="width:16mm">Not yet</th></tr>{pcr}</table>
{sub("B", "My language notes. Write three corrections from today's class.", "2 min")}
<div style="display:flex;gap:5mm;font-size:8.6pt"><div style="flex:1"><b>I said…</b>{lines(3)}</div><div style="flex:1"><b>Better:</b>{lines(3)}</div></div>
{sub("C", "Homework: writing (100–150 words)", "1 min")}
<p style="margin:.3mm 0"><b>My job.</b> Write a profile of your job (or a job you know well) for a careers website. Read Kate's profile first.</p>
<div class="box" style="font-size:8.6pt;line-height:1.4;margin:.5mm 0"><i>I work as a baker, and I run my own business, Sweet Kate Bakery, in Chicago. I'm responsible for planning the menu, baking cakes and managing a small team. It's also my job to order ingredients and to answer customers' emails. You don't need a degree for this job, but you have to be creative, and you need to be good at getting up early – I start at 5 a.m. every day! The work can get really hectic before holidays, and it's quite exhausting. It isn't very well-paid at first, either. But I find it incredibly rewarding when people come back and say they loved my cakes. On the whole, I can't imagine doing anything else.</i></div>
<p class="small" style="margin:.3mm 0">Checklist: ☐ <i>I work as a / for…</i> &nbsp;☐ <i>responsible for</i> + -ing &nbsp;☐ <i>my job to</i> + infinitive &nbsp;☐ <i>have to / don't have to</i> &nbsp;☐ good and bad things &nbsp;☐ 100–150 words</p>
{lines(7)}""",
    30, """<ol><li>B (error log): during the lesson, note 3–5 real mistakes. Here, the student writes what they said and the better version; guide them to self-correct first.</li>
<li>C: when you correct, check articles (<i>as a</i>), -ing after prepositions and the difference between <i>don't have to</i> and <i>mustn't</i>.</li></ol>""")

    script = "".join(f"<p style='margin:.5mm 0'><b>{l.split(': ', 1)[0]}:</b> {l.split(': ', 1)[1]}</p>" for l in S061)
    b.extra("Audio script", f"""
{sub("06.1", "Gap Year Diaries: what do you do? (natural and slow)")}
<div style="line-height:1.33;font-size:8.6pt">{script}</div>
{sub("06.2", "Repeat: word stress in jobs")}
<p>{" · ".join(x.split(": ", 1)[1] for x in _r["06.2 Repeat: word stress in jobs"].split(chr(10)))}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 06 - Describing jobs")
