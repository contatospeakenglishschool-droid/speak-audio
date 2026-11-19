# Speak! Progress B1 - Unit 06 "Describing jobs" (all English) - lean B1 format (rebuilt 2026-11-19)
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
setup(band="B1 · UNIT 06", audio_json="audio_b1-unit-06.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-06"]
S061 = [x.replace("twelve-hour", "12-hour") for x in _r["06.1 Gap Year Diaries: what do you do?"].split("\n")]
S062 = [x.split(": ", 1)[1] for x in _r["06.2 Repeat: word stress in jobs"].split("\n")]
JOBS = [("accountant", "acCOUNtant"), ("architect", "ARchitect"), ("electrician", "elecTRIcian"), ("programmer", "PROgrammer"),
        ("photographer", "phoTOgrapher"), ("engineer", "engiNEER"), ("receptionist", "reCEPtionist"), ("manager", "MAnager")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'

    # 1 Warm-up
    cover = cover_html(T, "LEVEL B1 · UNIT 06", "Describing jobs", "What do you do? · <b>job phrases · have to, must, don't have to, mustn't</b>",
                       [("YOU CAN", "describe a job: responsibilities, skills and qualifications, and what it's like"),
                        ("LANGUAGE", "I work as a… · I'm responsible for -ing · It's my job to… · You have to… · You don't have to…"),
                        ("PRONUNCIATION", "word stress in job words")])
    kw = [("boring because it is long and always the same", "tedious"), ("very busy, with a lot to do", "hectic"),
          ("making you feel happy because it is useful or important", "rewarding"), ("a period of work, for example from 7 p.m. to 7 a.m.", "a shift"),
          ("the money you get every month for your work", "a salary"), ("the time when a piece of work must be finished", "a deadline")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:20mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Warm-up: the world of work", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["What do you do, or what would you like to do?", "What did you want to be when you were a child?", "Which jobs are the most respected in Brazil? Which are the best paid?"], "START TALKING")}</div></div>
{sub("A", "Key words. Write the words from the box next to the definitions.", "3 min")}
<div class="bank">a deadline · hectic · rewarding · a salary · a shift · tedious</div>
<div style="font-size:8.8pt">{twocol(kwl, 3)}</div>
{talk(["Describe your job or your studies with three words from A.", "Which job do you think is the most rewarding? And the most tedious?"], "USE THE WORDS")}""",
    26, """<ol><li>Top box: if the student doesn't work, they can talk about their studies, a past job or a family member's job.</li>
<li>A: <i>salary</i> is usually monthly or yearly; <i>wage</i> is paid by the hour or week. <i>Rewarding</i> is a very useful positive word for difficult jobs.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Podcast: Ana and Bruno describe their jobs · who says it · notes · Talk about it", "Talking about work: job phrases, have to, don't have to, mustn't",
                      "Complete the phrases · have to or mustn't · Use it (oral)", "Functional language · word stress (06.2) · guess the job",
                      "Kate's job ad · work collocations · word choice · writing"),
        "The Linguahouse lesson is vocabulary only, with a reading about a zookeeper. Our listening: Danny records an episode of his podcast <i>Gap Year Diaries</i>. Ana works in the emergency department of a big hospital in São Paulo (12-hour shifts, B1 Unit 04). Bruno is a programmer: he works from home for a software company in Porto Alegre, builds and tests apps for banks, learned online, and lives in the hostel because working alone is isolating. Bruno's voice: <b>en-US-Chirp3-HD-Fenrir</b>. In the homework, Kate (Sweet Kate Bakery, Chicago) writes a job ad for an assistant baker.",
        "Students drop the article (<i>I work as doctor</i>), use the infinitive after <i>responsible for</i>, confuse <i>don't have to</i> (not necessary) with <i>mustn't</i> (not allowed), and use false friends: <i>I'm formed in…</i>, <i>professor</i> for a school teacher, and <i>chef</i> for a boss.",
        "Track 06.1 Gap Year Diaries: what do you do? (natural and slow) · Track 06.2 Repeat: word stress in jobs"))

    # 2 Listening
    ws = [("I don't have to wear a suit.", "B"), ("Some nights I don't have time to eat.", "A"), ("I learned online.", "B"),
          ("It isn't as well-paid as people think.", "A"), ("I spend all day in front of a screen.", "B"), ("You can really change people's lives.", "A")]
    wsl = [f'<li value="{i+1}">{s} {A(w, "min-width:7mm")}</li>' for i, (s, w) in enumerate(ws)]
    rows = [("Job", "a doctor in an emergency department", "a programmer, working from home"),
            ("Good things", "rewarding; you can change people's lives", "well-paid; no suit, no traffic"),
            ("Bad things", "hectic; 12-hour shifts; exhausting", "a bit isolating; all day at a screen")]
    tbl = "".join(f"<tr><td style='width:22mm;height:7mm'><b>{r}</b></td><td>{R(a) if T else ''}</td><td>{R(c) if T else ''}</td></tr>" for r, a, c in rows)
    b.page(f"""{sec(2, "Listening: what do you do?", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{audiocard(["06.1 · NATURAL", "06.1 · SLOW"])}
{sub("A", "Danny interviews Ana and Bruno on his podcast. Listen. Who says it? Write A (Ana) or B (Bruno).", "3 min", "06.1")}
<div style="font-size:8.5pt">{twocol(wsl, 3)}</div></div>{img('B', 40, 34)}</div>
{sub("B", "Listen again and complete the notes.", "3 min")}
<table style="font-size:8.3pt;margin-top:.5mm"><tr><th></th><th>Ana</th><th>Bruno</th></tr>{tbl}</table>
{talk(["Why does Bruno say, &ldquo;That's why I live in a hostel!&rdquo;?", "Whose job would you prefer, Ana's or Bruno's? Why?", "Would you like to work from home every day? Why?"])}""",
    26, """<ol><li>A–B: 6 minutes. Accept short notes in any order. The emergency department is often called the ER in the US.</li>
<li>Talk about it: 6 minutes. 1: working from home is isolating; in a hostel he can meet people.</li></ol>""")

    # 3 Grammar reference
    lean.grammar_in_class(b, grammar_ref.talking_about_work)

    # 4 Practice
    ph = [("I work", "as", "a doctor."), ("I'm responsible for", "treating", "(treat) patients."), ("It's also my job", "to decide", "(decide) which patients…"),
          ("You need to be good at", "making", "(make) quick decisions.")]
    phl = "".join(f"<li>{a} {A(f, 'min-width:16mm')} {e}</li>" for a, f, e in ph)
    ob = [(["doesn't have to", "mustn't"], "doesn't have to", "Bruno", "wear a suit."), (["mustn't", "don't have to"], "mustn't", "In the ER, you", "panic."),
          (["has to", "doesn't need to"], "doesn't need to", "Bruno", "have a degree.")]
    obl = "".join(f"<li>{s} {ch(o, a)} {e}</li>" for o, a, s, e in ob)
    use = ["What do you do? What are you responsible for?", "What do you have to do every day at work or school?", "What don't you have to do? (a uniform, weekends…)",
           "What mustn't people do in your workplace or school?", "What did you have to do in your first job?"]
    b.page(f"""{sec(4, "Practice: talking about work", "10 min")}
{sub("A", "Complete the phrases from the podcast.", "2 min")}
<ol style="line-height:1.7;font-size:8.9pt;margin:0;column-count:2">{phl}</ol>
{sub("B", "Choose the correct option.", "2 min")}
<ol style="line-height:1.7;font-size:8.9pt;margin:0">{obl}</ol>
<div class="box sand"><h4>RULE</h4><b>work as a / an</b> + job · <b>responsible for, good at</b> + -ing · <b>It's my job to</b> + infinitive · <b>have to / need to</b> = necessary · <b>don't have to</b> = not necessary · <b>mustn't</b> = not allowed · past: <b>had to</b>. See the <b>Grammar reference</b> on page 3.</div>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    24, """<ol><li>A–B: 4 minutes. Preposition + -ing (<i>for treating, at making</i>); <i>don't have to</i> = not necessary, but you can.</li>
<li>Use it: 6 minutes, all oral. If the student doesn't work, use studies or a family member's job.</li></ol>""")

    # 5 Speaking
    jl = " &nbsp; ".join(f"<b>{i+1}</b> {R(s) if T else w}" for i, (w, s) in enumerate(JOBS))
    b.page(f"""{sec(5, "Speaking: jobs", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>ask about a job</th><th>pros and cons</th><th>react</th><th>imagine</th></tr>
<tr><td><i>What do you do? · What does that involve? · Do you have to…?</i></td><td><i>The best thing about it is… · The downside is… · On the whole, …</i></td><td><i>That sounds rewarding! · I bet that's hard. · Really? I had no idea.</i></td><td><i>I'd love to work as… · I'd never want to be a… · I'd make a good…</i></td></tr></table></div>
{audiocard(["06.2"])}
{sub("A", "Word stress. Listen, underline the stressed syllable and repeat.", "4 min", "06.2")}
<p style="margin:.3mm 0;font-size:9pt;line-height:1.7">{jl}</p>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("B", "Guess the job. Your teacher is thinking of a job. Ask up to ten yes / no questions. Then change roles: choose a job and answer.", "10 min")}
<p style="margin:.3mm 0;font-size:8.6pt"><i>Do you have to wear a uniform? · Is it well-paid? · Do you work with people? · Can it be dangerous? · Do you need a degree?</i></p>
<p style="margin:.3mm 0;font-size:8.6pt">{R("Teacher's cards: a zookeeper · a flight attendant · a private detective · a firefighter. Answer only yes or no; give a hint after five questions.") if T else ""}</p></div>{img('D', 32, 24)}</div>
{talk(["Which jobs are very important but badly paid in Brazil? Why?", "Would you prefer a well-paid, stressful job or a badly paid, relaxing one?"])}""",
    28, """<ol><li>A: <i>-ician</i> and <i>-tionist</i> words stress the syllable before the ending; <i>engineer</i> stresses the end. Brazilians often say <i>ar-CHI-tect</i>.</li>
<li>B: encourage questions with <i>have to</i> and <i>need</i>. Last 3 minutes: wrap-up (two corrections and <i>Can you describe a job?</i>).</li></ol>""")

    # H Homework
    pr = [(["baking", "bake"], "baking"), (["to keep", "keeping"], "to keep"), (["have to", "don't have to"], "have to"), (["don't have to", "mustn't"], "don't have to"),
          (["mustn't", "don't have to"], "mustn't"), (["as", "like"], "as")]
    p = [ch(o, a) for o, a in pr]
    co = [("She", "earns", "a good salary."), ("We have to", "meet", "a deadline by Friday."), ("I'm tired. I need to", "take", "some time off.")]
    col = " &nbsp;·&nbsp; ".join(f"{a} {A(v, 'min-width:12mm')} {e}" for a, v, e in co)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Kate writes a job ad for her bakery. Choose the correct words.", "")}</div>{img('C', 28, 18)}</div>
<div class="box" style="line-height:1.8;font-size:8.8pt;margin:.5mm 0"><b>Sweet Kate Bakery, Chicago, is looking for an assistant baker!</b><br>You'll be responsible for {p[0]} bread, cookies and cakes, and it's also your job {p[1]} the kitchen clean. You {p[2]} start at 5 a.m., so you need to love mornings! You {p[3]} have experience – we'll train you – but you {p[4]} be late, because our first customers arrive at 6:30. Have you ever wanted to work {p[5]} a baker? Come and talk to Kate!</div>
{sub("B", "Complete with earn, meet or take.", "")}
<p style="margin:.3mm 0;line-height:1.9;font-size:8.6pt">{col}</p>
{lean.watch_out([("I'm formed in law.", "I have a degree in law.", "<i>formed</i> = given a shape."), ("my son's professor (at school)", "my son's teacher", "<i>professor</i> = at a university."), ("My chef is very strict.", "My boss is very strict.", "<i>chef</i> = a restaurant cook.")])}
{lean.writing_task(sub, "My job: write a profile of your job (or a job you know well) for a careers website.", "I work as a… I'm responsible for… It's also my job to…", ["responsible for + -ing", "have to / don't have to", "good and bad things", "100–150 words"], "I can describe a job: responsibilities, skills and what it's like.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class (ask why each answer is right). When you correct the writing, check articles (<i>as a</i>), -ing after prepositions and <i>don't have to</i> vs <i>mustn't</i>.</p>""")

    script = "".join(f"<p style='margin:.5mm 0'><b>{l.split(': ', 1)[0]}:</b> {l.split(': ', 1)[1]}</p>" for l in S061)
    b.extra("Audio script", f"""
{sub("06.1", "Gap Year Diaries: what do you do? (natural and slow)")}
<div style="line-height:1.33;font-size:8.6pt">{script}</div>
{sub("06.2", "Repeat: word stress in jobs")}
<p>{" · ".join(S062)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 06 - Describing jobs")
