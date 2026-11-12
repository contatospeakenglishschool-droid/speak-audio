# Speak! Progress B1 - Unit 08 "Work words" (all English) - B1 format (2026-11-09)
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Progress"
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
    def lines(n):
        return '<div class="wline"></div>' * n

    # Page 1 - Warm-up
    cover = cover_html(T, "LEVEL B1 · UNIT 08", "Work words", "Types of work and workers · <b>phrasal verbs and word order</b>",
                       [("YOU CAN", "talk about different types of work, changes in your working life and work trends"),
                        ("LANGUAGE", "a freelancer · on maternity leave · laid off · She took him on. · I turned it down."),
                        ("PRONUNCIATION", "stress in phrasal verbs")])
    kw = [("sells their work or services to different companies", "a freelancer"), ("works somewhere to get experience, often without pay", "an intern"),
          ("works for a company for a short, fixed period", "a temp"), ("works with no fixed end to the contract", "a permanent employee"),
          ("learns a skill on the job and earns a small amount of money", "an apprentice"), ("has their own business", "self-employed"),
          ("works without pay to help others", "a volunteer"), ("works at different times, for example nights", "a shift worker")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:22mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Warm-up: nine to five?", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 58, 38)}<div style="flex:1">
{sub("A", "Discuss with your teacher.", "3 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0"><li>Do you work (or study) from nine to five, Monday to Friday? What hours do you prefer?</li><li>How do you get to work? How long does it take?</li><li>Do you know anyone who works at night or on weekends?</li></ol></div></div>
{sub("B", "Key words. Types of workers. Write the words from the box next to the definitions.", "4 min")}
<div class="bank">an apprentice · a freelancer · an intern · a permanent employee · self-employed · a shift worker · a temp · a volunteer</div>
<div style="font-size:8.6pt">{twocol(kwl, 4)}</div>
{sub("C", "Which of these have you been? Which would you like to be?", "1 min")}""",
    25, """<ol><li>A: <i>nine to five</i> = a traditional office job. Ask about commuting in the student's city.</li>
<li>B: <i>self-employed</i> is an adjective (<i>I'm self-employed</i>), the others are nouns. <i>Temp</i> is short for <i>temporary worker</i>.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 60 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Discussion · key words: types of workers</td><td>1</td></tr>
<tr><td>2 Listening</td><td>12 min</td><td>Voice messages: Danny's new job and news from Rita</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>8 min</td><td>Work phrasal verbs · word order with pronouns</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Phrasal verbs and word order (study at home)</td><td>4</td></tr>
<tr><td>4 Vocabulary lab + pronunciation</td><td>8 min</td><td>Not working · job synonyms · phrasal verb stress</td><td>5</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Danny's blog: my first week as a freelancer · pronouns</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Functional language · long turn: my working life · career advice · work trends</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>4 min</td><td>Can-do · language notes · writing homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY</h4>The Linguahouse lesson is vocabulary only. Our original listening continues B1 Unit 07: Danny got the guide job at City Steps Tours. It's part-time (weekends), for three months, and he's a freelancer (paid per tour). There's a metro strike, so he walked to the office. Rita (his mom, City Coffee manager) replies: the barista Jen is on maternity leave and Rita has taken on a temp; Lucy got the volunteer position at the animal shelter (B1 Unit 07 writing model); Danny's uncle Mike has retired after 35 years at the same company. In the writing model, Danny writes to Tom.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students say <i>a work</i> and <i>works</i> (work is uncountable; use <i>a job</i>), put pronouns after the particle (<i>turn down it</i>), use <i>demitted</i> for <i>fired</i> or <i>laid off</i>, and mix up <i>fired</i> (your fault) with <i>laid off</i> (the company's decision).</div>
<div class="box"><h4>AUDIO</h4>Track 08.1 Voice messages: Danny's new job (natural and slow) · Track 08.2 Repeat: phrasal verb stress</div>""")

    # Page 2 - Listening
    gist = ["He didn't get the job.", "He got the job, but it isn't permanent.", "He got a full-time job."]
    tf = [("Danny will work from Monday to Friday.", "F (weekends only)"), ("Danny gets paid for each tour.", "T"), ("He can't get paid sick leave.", "T"),
          ("He took the metro to the office today.", "F (he walked; there's a strike)"), ("Rita thinks freelancing is perfect for life.", "F (fine for a gap year)"), ("Lucy gets paid at the animal shelter.", "F (she's a volunteer)")]
    tfl = [f'<li value="{i+1}">{s} {A(a, "min-width:9mm")}</li>' for i, (s, a) in enumerate(tf)]
    pp = [("Danny", "a freelancer"), ("Jen", "on maternity leave"), ("the new barista", "a temp"), ("Lucy", "a volunteer"), ("uncle Mike", "retired"), ("the metro workers", "on strike")]
    ppl = " &nbsp;·&nbsp; ".join(f"{p} {A(w, 'min-width:20mm')}" for p, w in pp)
    b.page(f"""{sec(2, "Listening: Danny's new job", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{audiocard(["08.1 · NATURAL", "08.1 · SLOW"])}
{sub("A", "Listen to Danny's voice message at natural speed. What's his news? Choose.", "2 min", "08.1")}
<p style="margin:.3mm 0;font-size:8.9pt">{ch(gist, gist[1])}</p></div>{img('B', 40, 27)}</div>
{sub("B", "Listen to both messages. True or false? Correct the false sentences.", "4 min")}
<div style="font-size:8.6pt">{twocol(tfl, 3)}</div>
{sub("C", "Who is it? Write the words from the box.", "2 min")}
<div class="bank">a freelancer · on maternity leave · on strike · retired · a temp · a volunteer</div>
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.9">{ppl}</p>
{sub("D", "Think about it. Discuss with your teacher.", "4 min")}
<ol style="line-height:1.4;font-size:8.8pt;margin:0"><li>Rita says, "Your generation will never do that." What does she mean? Do you agree? {R("Young people won't stay 35 years at the same company; they change jobs more often.") if T else ""}</li>
<li>Is being a freelancer a good idea for Danny? Why or why not? {R("Personal: flexible and fine for a gap year, but no paid vacation or sick leave.") if T else ""}</li></ol>
<div class="box sand" style="margin-top:1mm"><h4>NOTICE: USEFUL CHUNKS</h4><i>Big news… · It isn't even… · That means… · Anyway, … · If you don't work, you don't get paid. · Can you imagine?</i></div>""",
    25, """<ol><li>A: play only Danny's message for A, then both messages for B and C.</li>
<li>C: <i>on maternity / paternity / sick leave</i> and <i>on strike</i> always use <i>on</i>.</li></ol>""")

    # Page 3 - Language focus
    pv = [("I can work my way up", "b"), ("I need to get down to work.", "e"), ("Please work out a budget.", "a"), ("I've taken on a temp.", "c"), ("…to fill in for her.", "d")]
    mean = ["calculate or plan", "get a better position, step by step", "hire", "do someone's work while they're away", "start doing something seriously"]
    pvl = "".join(f"<li>{s} {A(a, 'min-width:6mm')}</li>" for s, a in pv)
    ml = " &nbsp; ".join(f"<b>{chr(97+i)}</b> {m}" for i, m in enumerate(mean))
    rw = [("Rita took on a temp.", "Rita took him on."), ("Please work out a budget.", "Please work it out."), ("The company laid off the workers.", "The company laid them off."), ("Danny didn't turn down the offer.", "Danny didn't turn it down.")]
    rwl = "".join(f"<li>{a} → {A(r, 'min-width:38mm')}</li>" for a, r in rw)
    b.page(f"""{sec(3, "Language focus: phrasal verbs at work", "8 min")}
{sub("A", "Phrasal verbs from the messages. Match them to the meanings a–e.", "3 min")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.6">{ml}</p>
<ol style="line-height:1.6;font-size:8.9pt;margin:0;column-count:2">{pvl}</ol>
{sub("B", "Word order. Rewrite the sentences with a pronoun (him, it, them).", "3 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0">{rwl}</ol>
{sub("C", "Correct or incorrect? Choose.", "2 min")}
<ol style="line-height:1.6;font-size:8.9pt;margin:0"><li>A temp is filling in for Jen. {ch(["correct", "incorrect"], "correct")}</li><li>They offered him the job, but he turned down it. {ch(["correct", "incorrect"], "incorrect")} {R("→ turned it down") if T else ""}</li><li>Let's get down to business. {ch(["correct", "incorrect"], "correct")}</li></ol>
<div class="box sand"><h4>RULE</h4><b>Separable</b> phrasal verbs (<i>take on, work out, lay off, turn down</i>): a noun can go before or after the particle, but a <b>pronoun goes in the middle</b>: <i>take him on, work it out</i>. <b>Inseparable</b> and three-part verbs keep the object after: <i>fill in for her, get down to work</i>. More on the next page: <b>Grammar reference</b>.</div>""",
    24, """<ol><li>A: elicit the meaning from context, then ask: <i>Have you ever turned down a job?</i></li>
<li>B: drill quickly: <i>Did Rita take on a temp? — Yes, she took him on.</i></li></ol>""")

    grammar_ref.phrasal_verbs_word_order(b)

    # Page 5 - Vocabulary lab
    nw = [("You're taking care of your newborn baby.", "on paternity / maternity leave"), ("Workers don't go to work because they want better pay.", "on strike"),
          ("You reached 65 and stopped working.", "retired"), ("The company wanted to cut costs, so they let you go.", "laid off"),
          ("You had an operation and you're recovering at home.", "on sick leave"), ("You were often late and made mistakes, so you lost your job.", "fired")]
    nwl = [f'<li value="{i+1}">{s} {A(w, "min-width:22mm")}</li>' for i, (s, w) in enumerate(nw)]
    sy = [("Ana chose medicine as a", "career", ", and she's been a doctor for years."), ("Teaching isn't just a job for him; it's a", "vocation", "."),
          ("She applied for the", "position", "of sales manager."), ("Please write your name and", "occupation", "on the form."), ("Law is a respected", "profession", "in Brazil.")]
    syl = [f'<li value="{i+1}">{a} {A(w, "min-width:18mm")}{e if e.startswith(",") or e == "." else " " + e}</li>' for i, (a, w, e) in enumerate(sy)]
    b.page(f"""{sec(4, "Vocabulary lab: in and out of work", "4 min")}
{sub("A", "Not working. Match the situations to the phrases in the box.", "2 min")}
<div class="bank">fired · laid off · on paternity / maternity leave · on sick leave · on strike · retired</div>
<div style="font-size:8.5pt">{twocol(nwl, 3)}</div>
{sub("B", "Job synonyms. Complete with career, occupation, position, profession or vocation.", "2 min")}
<div style="font-size:8.5pt">{twocol(syl, 3)}</div>
<div class="box sand"><h4>WATCH OUT: WORD CHOICE</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>I'm looking for a work.</td><td><b>I'm looking for a job.</b></td><td><i>work</i> is uncountable; <i>a job</i> is countable.</td></tr>
<tr><td>I have a lot of works today.</td><td><b>I have a lot of work today.</b></td><td>no plural for <i>work</i> (= tasks).</td></tr>
<tr><td>He was demitted last month.</td><td><b>He was fired / laid off last month.</b></td><td><i>fired</i> = his fault; <i>laid off</i> = the company cut jobs.</td></tr></table></div>
{sec(5, "Pronunciation lab: stress in phrasal verbs", "4 min")}
<p class="small" style="margin:.3mm 0">In phrasal verbs, the <b>particle</b> is usually stressed: <i>work it OUT · take ON · lay OFF · turn it DOWN</i>.</p>
{audiocard(["08.2"])}
{sub("A", "Listen and repeat. Then tell your teacher about a time you turned something down or filled in for someone.", "4 min", "08.2")}
<p style="margin:.3mm 0;font-size:8.8pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S082))}</p>""",
    24, """<ol><li>A: <i>fired</i> is informal (<i>sacked</i> in British English); <i>let go</i> is a softer way to say it.</li>
<li>B: <i>career</i> = your working life; <i>position</i> = a specific job in a company; <i>occupation</i> is formal (forms); <i>vocation</i> = a job you feel called to do.</li></ol>""")

    # Page 6 - Practice
    pr = [(["job", "work"], "job"), (["a freelancer", "a permanent employee"], "a freelancer"), (["vacation", "leave"], "leave"), (["work out", "work up"], "work out"),
          (["get down to", "get down"], "get down to"), (["took on", "laid off"], "took on"), (["fill in for", "fill for"], "fill in for"), (["turned it down", "turned down it"], "turned it down"), (["career", "occupation"], "career")]
    p = [ch(o, a) for o, a in pr]
    rw2 = [("Can you look after my dog this weekend?", "Can you look after it this weekend?"), ("I need to work out the cost of the trip.", "I need to work it out."),
           ("They took on three new guides.", "They took them on."), ("Kate turned down the offer from a big hotel.", "Kate turned it down.")]
    rw2l = "".join(f"<li>{a} → {A(r, 'min-width:36mm')}</li>" for a, r in rw2)
    b.page(f"""{sec(6, "Practice", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Danny writes a blog post. Choose the correct words.", "5 min")}</div>{img('C', 30, 20)}</div>
<div class="box" style="line-height:1.95;font-size:9pt"><b>Gap Year Diaries: my first week as a freelancer</b><br>I've got my first real {p[0]} in Brazil! I'm {p[1]}, so I get paid for each tour, and there's no paid sick {p[2]}. My mom told me to {p[3]} a budget, so on Monday I had to {p[4]} business with a spreadsheet. City Steps {p[5]} two new guides this month, me and a student called Rafa. On Sunday, Rafa was sick, so I had to {p[6]} him. Then a hotel offered me a full-time job at reception, but I {p[7]}. I want to see Brazil, not a hotel lobby! Who knows? Maybe tourism will become my {p[8]}.</div>
{sub("B", "Rewrite the sentences with a pronoun.", "3 min")}
<ol style="line-height:1.9;font-size:8.9pt;margin:0">{rw2l}</ol>""",
    22, """<ol><li>A: ask the student to explain each choice (uncountable <i>work</i>, three-part <i>fill in for</i>, pronoun position).</li>
<li>B: in 1, <i>look after</i> is inseparable, so the pronoun stays after the particle. Ask: <i>Why is this one different?</i></li></ol>""")

    # Page 7 - Speaking
    b.page(f"""{sec(7, "Speaking: working life", "12 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>compare options</th><th>give advice</th><th>talk about the future</th><th>opinions on trends</th></tr>
<tr><td><i>On the one hand… on the other hand… · The main advantage is…</i></td><td><i>If I were you, I'd… · Have you thought about…? · It might be worth…</i></td><td><i>In five years, I'd like to… · I'm hoping to… · I might…</i></td><td><i>I think it's a good thing because… · The problem is…</i></td></tr></table></div>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("A", "Long turn. Prepare for one minute, then talk for two minutes about your working life.", "5 min")}
<ul style="line-height:1.45;font-size:8.9pt;margin:0"><li>your type of work now (or your studies)</li><li>how your working life has changed</li><li>the best and worst types of work for you</li><li>where you'd like to be in five years</li></ul></div>{img('D', 32, 24)}</div>
{sub("B", "Role-play: career advice. Your teacher has a work problem. Ask questions and give advice. Then change roles.", "4 min")}
<p style="margin:.3mm 0;font-size:8.6pt">{R("Teacher's card: You were laid off last month. You have two offers: a permanent job in an office, 9 to 5, an hour from home, or freelance work from home with no fixed salary. You have a small child and you love flexibility, but you're worried about money.") if T else ""}</p>
{sub("C", "Talking point: work trends. Discuss with your teacher.", "3 min")}
<ol style="line-height:1.5;font-size:8.9pt;margin:0"><li>Should companies care about their employees' well-being? How?</li><li>Do people need to keep learning new skills to keep their jobs?</li><li>What do you think about app-based work, like delivery and ride-sharing?</li></ol>""",
    28, """<ol><li>A: don't interrupt; note mistakes for the error log (page 8), especially <i>a work / works</i> and phrasal verb word order. Fluency option (3-2-1): the same talk in 2 minutes, then in 1 minute.</li>
<li>C: these are the Linguahouse "work trends" (well-being, upskilling, the gig economy). Don't state statistics; ask for the student's experience.</li></ol>""")

    # Page 8 - Wrap-up
    pc = ["I can understand informal voice messages about work news.", "I can use work phrasal verbs with the correct word order.",
          "I can talk about types of work, changes in my working life and work trends."]
    pcr = "".join(f"<tr><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for s in pc)
    b.page(f"""{sec(8, "Wrap-up and homework", "4 min")}
{sub("A", "Can-do check", "1 min")}
<table class="ck" style="font-size:8.6pt"><tr><th>In English…</th><th style="width:16mm">Easy!</th><th style="width:16mm">Sometimes</th><th style="width:16mm">Not yet</th></tr>{pcr}</table>
{sub("B", "My language notes. Write three corrections from today's class.", "2 min")}
<div style="display:flex;gap:5mm;font-size:8.6pt"><div style="flex:1"><b>I said…</b>{lines(3)}</div><div style="flex:1"><b>Better:</b>{lines(3)}</div></div>
{sub("C", "Homework: writing (100–150 words)", "1 min")}
<p style="margin:.3mm 0"><b>Work news.</b> Write an email to a friend about a change in your working life (or the life of someone you know). Read Danny's email to Tom first.</p>
<div class="box" style="font-size:8.6pt;line-height:1.4;margin:.5mm 0"><i>Hi Tom,<br>How are things in Chicago? I have some news: I've found a job! I'm working as a tour guide in São Paulo. It isn't a permanent job – I'm a freelancer, so I get paid for each tour, and I only work on weekends. The first week was crazy. On Sunday, another guide was sick, so I had to fill in for him and do two tours in one day. My feet are still hurting! A hotel offered me a full-time job, but I turned it down, because I want to keep traveling. My boss says I can work my way up to senior guide if I do well. Not bad for someone who used to play video games all day, right? Write soon!<br>Danny</i></div>
<p class="small" style="margin:.3mm 0">Checklist: ☐ type of work (<i>part-time, freelance…</i>) &nbsp;☐ three phrasal verbs &nbsp;☐ one pronoun in the middle (<i>turned it down</i>) &nbsp;☐ how you feel about it &nbsp;☐ 100–150 words</p>
{lines(6)}""",
    30, """<ol><li>B (error log): during the lesson, note 3–5 real mistakes. Here, the student writes what they said and the better version; guide them to self-correct first.</li>
<li>C: check <i>job / work</i>, the phrasal verbs and informal email features (contractions, <i>Write soon!</i>).</li></ol>""")

    script = "".join(f"<p style='margin:.6mm 0'><b>{l.split(': ', 1)[0]}:</b> {l.split(': ', 1)[1]}</p>" for l in S081)
    b.extra("Audio script", f"""
{sub("08.1", "Voice messages: Danny's new job (natural and slow)")}
<div style="line-height:1.35;font-size:8.7pt">{script}</div>
{sub("08.2", "Repeat: phrasal verb stress")}
<p>{" · ".join(S082)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 08 - Work words")
