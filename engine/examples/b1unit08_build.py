# Speak! Progress B1 - Unit 08 "Work words" (all English) - lean B1 format (rebuilt 2026-11-19)
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
setup(band="B1 · UNIT 08", audio_json="audio_b1-unit-08.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-08"]
S081 = [l.replace("thirty-five", "35").replace("thirty buildings", "30 buildings") for l in _r["08.1 Voice messages: Danny's new job"].split("\n")]
S082 = [x.split(": ", 1)[1] for x in _r["08.2 Repeat: phrasal verb stress"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'

    # 1 Warm-up
    cover = cover_html(T, "LEVEL B1 · UNIT 08", "Work words", "Types of work and workers · <b>phrasal verbs and word order</b>",
                       [("YOU CAN", "talk about different types of work, changes in your working life and work trends"),
                        ("LANGUAGE", "a freelancer · on maternity leave · laid off · She took him on. · I turned it down."),
                        ("PRONUNCIATION", "stress in phrasal verbs")])
    kw = [("sells their work or services to different companies", "a freelancer"), ("works somewhere to get experience, often without pay", "an intern"),
          ("works for a company for a short, fixed period", "a temp"), ("has their own business", "self-employed"),
          ("works without pay to help others", "a volunteer"), ("works at different times, for example nights", "a shift worker")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:22mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Warm-up: nine to five?", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["Do you work (or study) from nine to five? What hours do you prefer?", "How do you get to work? How long does it take?", "Do you know anyone who works at night or on weekends?"], "START TALKING")}</div></div>
{sub("A", "Key words. Types of workers. Write the words from the box next to the definitions.", "3 min")}
<div class="bank">a freelancer · an intern · self-employed · a shift worker · a temp · a volunteer</div>
<div style="font-size:8.6pt">{twocol(kwl, 3)}</div>
{talk(["Which of these have you been? Which would you like to be?", "What are the pros and cons of being a freelancer?"], "USE THE WORDS")}""",
    26, """<ol><li>Top box: <i>nine to five</i> = a traditional office job. Ask about commuting in the student's city.</li>
<li>A: <i>self-employed</i> is an adjective (<i>I'm self-employed</i>), the others are nouns. <i>Temp</i> = temporary worker.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Voice messages: Danny's new job · true or false · Talk about it", "Phrasal verbs and word order",
                      "Match the meanings · pronoun in the middle · Use it (oral)", "Functional language · stress in phrasal verbs (08.2) · career advice role-play",
                      "Danny's blog post · not working: fired, laid off… · word choice · writing"),
        "The Linguahouse lesson is vocabulary only. Our listening continues B1 Unit 07: Danny got the guide job at City Steps Tours. It's part-time (weekends), for three months, and he's a freelancer (paid per tour). There's a metro strike, so he walked to the office. Rita (his mom, City Coffee manager) replies: the barista Jen is on maternity leave and Rita has taken on a temp; Lucy got the volunteer position at the animal shelter; Danny's uncle Mike has retired after 35 years at the same company.",
        "Students say <i>a work</i> and <i>works</i> (work is uncountable; use <i>a job</i>), put pronouns after the particle (<i>turn down it</i>), use <i>demitted</i> for <i>fired</i> or <i>laid off</i>, and mix up <i>fired</i> (your fault) with <i>laid off</i> (the company's decision).",
        "Track 08.1 Voice messages: Danny's new job (natural and slow) · Track 08.2 Repeat: phrasal verb stress"))

    # 2 Listening
    gist = ["He didn't get the job.", "He got the job, but it isn't permanent.", "He got a full-time job."]
    tf = [("Danny will work from Monday to Friday.", "F (weekends only)"), ("Danny gets paid for each tour.", "T"),
          ("He took the metro to the office today.", "F (he walked; there's a strike)"), ("Rita thinks freelancing is perfect for life.", "F (fine for a gap year)"),
          ("Lucy gets paid at the animal shelter.", "F (she's a volunteer)"), ("Danny's uncle Mike has retired.", "T")]
    tfl = [f'<li value="{i+1}">{s} {A(a, "min-width:9mm")}</li>' for i, (s, a) in enumerate(tf)]
    b.page(f"""{sec(2, "Listening: Danny's new job", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{audiocard(["08.1 · NATURAL", "08.1 · SLOW"])}
{sub("A", "Listen to Danny's voice message. What's his news? Choose.", "2 min", "08.1")}
<p style="margin:.3mm 0;font-size:8.9pt">{ch(gist, gist[1])}</p></div>{img('B', 40, 27)}</div>
{sub("B", "Listen to both messages (Danny and his mom). True or false? Correct the false sentences.", "4 min")}
<div style="font-size:8.6pt">{twocol(tfl, 3)}</div>
{talk(["Rita says, &ldquo;Your generation will never do that.&rdquo; What does she mean? Do you agree?", "Is being a freelancer a good idea for Danny? Why or why not?", "Would you prefer a permanent job or freelance work? Why?"])}""",
    26, """<ol><li>A–B: 6 minutes. Play only Danny's message for A, then both for B. <i>On maternity leave</i> and <i>on strike</i> always use <i>on</i>.</li>
<li>Talk about it: 6 minutes. 1: young people won't stay 35 years at the same company. 2: flexible and fine for a gap year, but no paid vacation or sick leave.</li></ol>""")

    # 3 Grammar reference
    lean.grammar_in_class(b, grammar_ref.phrasal_verbs_word_order)

    # 4 Practice
    pv = [("I can work my way up.", "b"), ("Please work out a budget.", "a"), ("I've taken on a temp.", "c"), ("…to fill in for her.", "d")]
    mean = ["calculate or plan", "get a better position, step by step", "hire", "do someone's work while they're away"]
    pvl = "".join(f"<li>{s} {A(a, 'min-width:6mm')}</li>" for s, a in pv)
    ml = " &nbsp; ".join(f"<b>{chr(97+i)}</b> {m}" for i, m in enumerate(mean))
    rw = [("Rita took on a temp.", "Rita took him on."), ("Danny didn't turn down the offer.", "Danny didn't turn it down.")]
    rwl = "".join(f"<li>{a} → {A(r, 'min-width:38mm')}</li>" for a, r in rw)
    use = ["Have you ever turned down a job or an invitation? Why?", "Have you ever filled in for a coworker or a classmate?", "How do you work out your monthly budget?",
           "What would help you work your way up in your career?", "Your teacher asks: <i>Did you finish the report?</i> Answer with a pronoun: <i>Yes, I handed it in.</i>"]
    b.page(f"""{sec(4, "Practice: phrasal verbs at work", "10 min")}
{sub("A", "Phrasal verbs from the messages. Match them to the meanings a–d.", "2 min")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.6">{ml}</p>
<ol style="line-height:1.6;font-size:8.9pt;margin:0;column-count:2">{pvl}</ol>
{sub("B", "Word order. Rewrite with a pronoun (him, it).", "2 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0">{rwl}</ol>
<div class="box sand"><h4>RULE</h4><b>Separable</b> phrasal verbs (<i>take on, work out, lay off, turn down</i>): a noun can go before or after the particle, but a <b>pronoun goes in the middle</b>: <i>take him on</i>. <b>Inseparable</b> and three-part verbs keep the object after: <i>fill in for her</i>. See the <b>Grammar reference</b> on page 3.</div>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    24, """<ol><li>A–B: 4 minutes. Drill: <i>Did Rita take on a temp? — Yes, she took him on.</i></li>
<li>Use it: 6 minutes, all oral. Correct <i>turned down it</i> every time.</li></ol>""")

    # 5 Speaking
    b.page(f"""{sec(5, "Speaking: working life", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>compare options</th><th>give advice</th><th>talk about the future</th><th>opinions on trends</th></tr>
<tr><td><i>On the one hand… on the other hand… · The main advantage is…</i></td><td><i>If I were you, I'd… · Have you thought about…? · It might be worth…</i></td><td><i>In five years, I'd like to… · I'm hoping to… · I might…</i></td><td><i>I think it's a good thing because… · The problem is…</i></td></tr></table></div>
{audiocard(["08.2"])}
{sub("A", "Stress the particle. Listen and repeat: work it OUT · take ON · turn it DOWN.", "4 min", "08.2")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.55">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S082))}</p>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("B", "Role-play: career advice. Your teacher has a work problem. Ask questions and give advice. Then change roles: tell your teacher about a real or invented work problem.", "10 min")}
<p style="margin:.3mm 0;font-size:8.6pt">{R("Teacher's card: You were laid off last month. You have two offers: a permanent job in an office, 9 to 5, an hour from home, or freelance work from home with no fixed salary. You have a small child and you love flexibility, but you're worried about money.") if T else ""}</p></div>{img('D', 32, 24)}</div>
{talk(["Should companies care about their employees' well-being? How?", "What do you think about app-based work, like delivery and ride-sharing?"])}""",
    28, """<ol><li>B: let the student ask questions before giving advice. Talk about it: these are Linguahouse work trends; don't state statistics, ask for the student's experience.</li>
<li>Last 3 minutes: wrap-up (two corrections and <i>Can you talk about types of work?</i>).</li></ol>""")

    # H Homework
    pr = [(["job", "work"], "job"), (["a freelancer", "a permanent employee"], "a freelancer"), (["work out", "work up"], "work out"),
          (["fill in for", "fill for"], "fill in for"), (["turned it down", "turned down it"], "turned it down"), (["career", "occupation"], "career")]
    p = [ch(o, a) for o, a in pr]
    nw = [("Workers don't go to work because they want better pay.", "on strike"), ("The company wanted to cut costs, so they let you go.", "laid off"), ("You were often late, so you lost your job.", "fired")]
    nwl = "".join(f"<li>{s} {A(w, 'min-width:18mm')}</li>" for s, w in nw)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Danny writes a blog post. Choose the correct words.", "")}</div>{img('C', 28, 18)}</div>
<div class="box" style="line-height:1.8;font-size:8.8pt;margin:.5mm 0"><b>Gap Year Diaries: my first week as a freelancer</b><br>I've got my first real {p[0]} in Brazil! I'm {p[1]}, so I get paid for each tour. My mom told me to {p[2]} a budget, so I made a spreadsheet. On Sunday, Rafa was sick, so I had to {p[3]} him. Then a hotel offered me a full-time job at reception, but I {p[4]}. Who knows? Maybe tourism will become my {p[5]}.</div>
{sub("B", "Not working. Write fired, laid off or on strike.", "")}
<ol style="line-height:1.5;font-size:8.6pt;margin:0">{nwl}</ol>
{lean.watch_out([("I'm looking for a work.", "I'm looking for a job.", "<i>work</i> is uncountable; <i>a job</i> is countable."), ("I have a lot of works today.", "I have a lot of work today.", "no plural for <i>work</i>."), ("He was demitted last month.", "He was fired / laid off.", "<i>fired</i> = his fault; <i>laid off</i> = the company cut jobs.")])}
{lean.writing_task(sub, "Work news: write an email to a friend about a change in your working life (or the life of someone you know).", "Hi…! I have some news: I've… It isn't a permanent job – I'm…", ["type of work", "three phrasal verbs", "a pronoun in the middle", "100–150 words"], "I can talk about types of work and changes in my working life.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class (ask the student to explain each choice). When you correct the writing, check <i>job / work</i> and phrasal verb word order.</p>""")

    script = "".join(f"<p style='margin:.6mm 0'><b>{l.split(': ', 1)[0]}:</b> {l.split(': ', 1)[1]}</p>" for l in S081)
    b.extra("Audio script", f"""
{sub("08.1", "Voice messages: Danny's new job (natural and slow)")}
<div style="line-height:1.35;font-size:8.7pt">{script}</div>
{sub("08.2", "Repeat: phrasal verb stress")}
<p>{" · ".join(S082)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 08 - Work words")
