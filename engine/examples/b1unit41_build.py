# Speak! Progress B1 - Unit 41 "Making plans" (all English) - lean B1 format
import sys, os, json
_h = os.path.dirname(os.path.abspath(__file__))
for _d in ("/home/claude/speak-audio/engine", os.path.join(_h, "..", "speak-audio", "engine"), os.path.join(_h, "..", "..", "speak-audio", "engine"),
           os.path.join(_h, "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Progress"
import lean
from lean import talk
setup(band="B1 · UNIT 41", audio_json="audio_b1-unit-41.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-41"]
S411 = [l.split(": ", 1) for l in _r["41.1 Gap Year Diaries: planning ahead"].split("\n")]
S412 = [x.split(": ", 1)[1] for x in _r["41.2 Repeat: bound to, likely to"].split("\n")]


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
    cover = cover_html(T, "LEVEL B1 · UNIT 41", "Planning ahead", "Planning your week · <b>It's bound to rain · There's a good chance…</b>",
                       [("YOU CAN", "plan a busy week and say how probable something is"),
                        ("LANGUAGE", "go for a check-up · settle the bill · be bound to · be likely to · tend to · a good chance"),
                        ("PRONUNCIATION", "weak <i>to</i> /tə/: bound to, likely to")])
    kw = [("to have a medical examination to check your health", "go for", "a check-up"),
          ("to pay for a meal in a restaurant", "settle", "the bill"),
          ("to meet someone you might start a romantic relationship with", "go on", "a date"),
          ("to be present at a meeting where someone asks you questions for a job", "attend", "an interview"),
          ("to add new information to the document with your work history", "update", "your resume"),
          ("to enter a hospital as a patient and stay there", "be admitted", "to the hospital")]
    kwl = [f'<li value="{i+1}">{A(v, "min-width:20mm")} <b>{n}</b> <span style="color:#6b7377">= {d}</span></li>' for i, (d, v, n) in enumerate(kw)]
    b.page(f"""{sec(1, "Warm-up: a busy week", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["Do you plan your week, or do you take it day by day?", "Which day of the week is the best for you? Which is the worst? Why?", "Is there anything you always do on the same day?"], "START TALKING")}</div></div>
{sub("A", "Key phrases. Complete the phrases with the verbs from the box.", "3 min")}
<div class="bank">attend · be admitted · go for · go on · settle · update</div>
<ol style="font-size:8.7pt;line-height:1.75;margin:0">{"".join(kwl)}</ol>
{talk(["When did you last go for a check-up? Was it easy to get an appointment?", "When you eat out with friends, who usually settles the bill?", "How often do you update your resume or your LinkedIn profile?"], "USE THE PHRASES")}""",
    26, """<ol><li>Start with the questions in the top box: 3 minutes.</li>
<li>A: 4 minutes with the questions. The Linguahouse lesson uses <i>refresh your resume</i>; in American English <b>update your resume</b> is much more common, so we use it. <i>settle the bill</i> = pay; in everyday speech also <i>pay the check</i> / <i>split the check</i>.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Gap Year Diaries: Ana helps Danny plan his week · complete Danny's planner · why? · Talk about it",
                      "expressing probability: be bound / certain to, be likely / unlikely to, tend to, might / could, expressions with chance", "Choose, complete, rewrite with chance · Use it (oral)",
                      "bound to, likely to (41.2) · predictions: how sure are you? · plan the teacher's week", "Danny's message · rewrite with chance · watch out · writing"),
        """The Linguahouse lesson has key phrases for a busy week (go for a check-up, settle the bill, go on a date, attend an interview, refresh a resume, be admitted to the hospital), a newspaper article from 2007 with statistics about the best day of the week for each activity, and a grammar section on expressing probability. We did not use the old statistics: instead, the input is an episode of Danny's podcast, Gap Year Diaries, where Ana helps him plan a crazy week with her own opinions and experience as a doctor. Basic predictions (will, might, be likely to) were studied in A2, so the grammar page goes further: the probability scale with be bound to, be certain to, tend to and expressions with chance. Story: Danny is thinking of staying in São Paulo until the end of the year (Review 4), so he has a job interview at a language school. Ana's advice: check-up on Wednesday morning (clinics are bound to be packed on Mondays), the interview on Thursday at four, not Monday at nine; update his resume on Tuesday (Bruno will be at work); Bruno has a first date on Wednesday; no driving to the beach on Friday (traffic, and Ana sees accidents in the ER), so Danny and Rafa leave on Saturday morning; weekly shopping on Sunday before ten. Ana will call the clinic herself. No real-world facts or statistics are given.""",
        """<i>It's probable that he comes</i> (a literal translation from Portuguese); <i>a big chance</i> for <i>a good chance</i>; <i>a chance to win</i> vs. <i>a chance of winning</i>; a verb after <i>to</i> in the wrong form (<i>bound to won</i>). Pronunciation: <i>to</i> is weak /tə/ in <i>bound to, likely to, tend to</i>; <i>tend to</i> often sounds like /ˈtentə/.""",
        "Track 41.1 Gap Year Diaries: planning ahead (natural and slow; Danny and Ana) · Track 41.2 Repeat: bound to, likely to"))

    # Page 2 - Listening
    week = [("Monday", "", "—"), ("Tuesday", "", "update resume"), ("Wednesday", "morning", "check-up"), ("Wednesday", "evening", "Bruno's date"),
            ("Thursday", "4 p.m.", "job interview"), ("Friday", "", "— (no driving!)"), ("Saturday", "morning", "beach trip with Rafa"), ("Sunday", "before 10 a.m.", "weekly shopping")]
    wk = "".join(f'<tr><td><b>{d}</b> <span style="color:#6b7377">{t}</span></td><td>{A(e, "min-width:44mm")}</td></tr>' for d, t, e in week)
    qs = [("Why shouldn't Danny go for a check-up on Monday?", "Clinics are bound to be packed: people get sick on the weekend."),
          ("Why is Thursday better for the interview?", "Interviewers are likely to be tired on Monday; people tend to be more relaxed later in the week; more time to prepare."),
          ("Why is Wednesday a smart day for a first date?", "Good chance of meeting again on the weekend; an excuse to leave early if it goes badly."),
          ("Why does Ana say no to Friday for the beach?", "The traffic is certain to be terrible; she sees accidents in the ER on Friday nights.")]
    ql = "".join(f"<li>{q} {A(a, 'min-width:50mm')}</li>" for q, a in qs)
    b.page(f"""{sec(2, "Listening: Gap Year Diaries", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Listen to Danny's podcast. Ana helps him plan his week. Write the plans in Danny's planner.", "4 min")}
<div class="bank" style="font-size:8.6pt">beach trip with Rafa · Bruno's date · check-up · job interview · update resume · weekly shopping</div>
<table style="font-size:8.6pt;margin:.5mm 0">{wk}</table></div>{img('B', 36, 30)}</div>
{audiocard(["41.1 · NATURAL", "41.1 · SLOW"])}
{sub("B", "Listen again. Why does Ana choose each day?", "4 min")}
<ol style="line-height:1.5;font-size:8.6pt;margin:0">{ql}</ol>
<p style="margin:.6mm 0;font-size:8.6pt"><b>Think about it:</b> Ana's advice comes from her experience, not from statistics. Which tip do you agree with? Which one is different in your city? {A("open answer", "min-width:20mm")}</p>
{talk(["Which day of the week is your clinic, bank or supermarket bound to be busy?", "Is Friday traffic bad where you live? When do you avoid driving?", "Would you choose Monday or Thursday for a job interview? Why?"])}""",
    30, """<ol><li>A: play the natural version; play the slow one if needed. 6 minutes. Monday and Friday stay empty: that's the point of Ana's advice.</li>
<li>B: accept short answers. Ask the student to repeat Ana's exact words with <i>bound to, likely to, tend to, certain to, a good chance</i>: they come back on page 3.</li>
<li>Talk about it: 4 minutes. Danny's podcast <i>Gap Year Diaries</i> appeared in earlier units.</li></ol>""")

    # Page 3
    lean.grammar_in_class(b, grammar_ref.probability_chance)

    # Page 4 - Practice
    comp = [("Don't go out with wet hair in this cold. You", "might get", "a cold."),
            ("He hasn't studied at all. He", "is unlikely to pass", "the exam."),
            ("Look at those black clouds! It", "is bound to rain", "this afternoon."),
            ("In my family, the women", "tend to live", "longer than the men."),
            ("She's practiced for weeks. She", "should be", "ready for the test."),
            ("The museum is closed for repairs until March. It", "is certain not to open", "this weekend.")]
    cl = "".join(f"<li>{a} {A(m, 'min-width:30mm')} {z}</li>" for a, m, z in comp)
    rw = [("You're unlikely to win the race. (little chance)", "There's little chance (that) you'll win the race. / You have little chance of winning the race."),
          ("Bruno is likely to see Paula again. (good chance)", "There's a good chance (that) Bruno will see Paula again."),
          ("Could you possibly lend me fifty reais? (any chance)", "Is there any chance you could lend me fifty reais?")]
    rwl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw)
    use = ["Name something that is bound to happen this week.", "What do people in your city tend to do on Sunday?",
           "Is it likely to rain this weekend where you live?", "Is there a good chance you'll travel this year? Where?",
           "Ask me a very polite favor: Is there any chance you could…?"]
    b.page(f"""{sec(4, "Practice: how sure are you?", "10 min")}
{sub("A", "Complete with the words from the box. Use the verbs in brackets in the right form.", "4 min")}
<div class="bank" style="font-size:8.6pt">be bound to (rain) · be certain not to (open) · be unlikely to (pass) · might (get) · should (be) · tend to (live)</div>
<ol style="line-height:1.75;font-size:8.8pt;margin:0">{cl}</ol>
{sub("B", "Rewrite the sentences with the expression with chance in brackets.", "3 min")}
<ol style="line-height:1.45;font-size:8.7pt;margin:0">{rwl}</ol>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    24, """<ol><li>A: 4 minutes. Item 5: <i>should</i> + base form = we expect it. Item 6: in speech we'd say <i>There's no chance it'll open.</i></li>
<li>B: accept both <i>there's a … chance (that)</i> + clause and <i>have a … chance of</i> + -ing.</li>
<li>Use it: 3 minutes, all oral. Push the student to use a different structure in each answer.</li></ol>""")

    # Page 5 - Speaking
    card = f"""<div class="box" style="margin-top:1mm;font-size:8.3pt">{R("<b>Teacher's card (B):</b> after each prediction, ask <i>How sure are you? Why?</i> and push for a different structure. <b>(C)</b> Your week: a dentist appointment, a work meeting, dinner with an old friend (who settles the bill?), a car to take to the mechanic, a birthday present to buy. The student is Ana: they choose the day for each one and say why, with probability language.")}</div>""" if T else ""
    tp = ["your career or studies", "technology in ten years", "the traffic in your city next year", "the next World Cup", "the environment", "your next vacation"]
    b.page(f"""{sec(5, "Speaking: predictions and plans", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.3pt"><tr><th>very sure</th><th>quite sure</th><th>not sure</th><th>reacting</th></tr>
<tr><td><i>It's bound to… · There's no doubt that… · It's certain to…</i></td><td><i>It's likely to… · There's a good chance that… · It should…</i></td><td><i>It might… · There's a slight chance that… · I doubt it'll…</i></td><td><i>How sure are you? · Really? Why do you think so? · I wouldn't bet on it!</i></td></tr></table></div>
{audiocard(["41.2"])}
{sub("A", "Listen and repeat. Say to fast and weak: bound to /ˈbaʊnd tə/.", "4 min", "41.2")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S412))}</p>
{sub("B", "Choose three topics. What is likely or unlikely to happen? How sure are you? Give a reason.", "7 min")}
<div class="bank" style="font-size:8.6pt;background:#fff">{" · ".join(sorted(tp, key=lambda x: x.replace("the ", "")))}</div>
{sub("C", "Be Ana! Your teacher has a busy week. Listen to the plans and choose the best day for each one. Say why.", "7 min")}
<div style="display:flex;gap:3mm;font-size:8.6pt;margin:.5mm 0"><div style="flex:1">Day 1: {lines(1)}</div><div style="flex:1">Day 2: {lines(1)}</div><div style="flex:1">Day 3: {lines(1)}</div></div>{card}
{talk(["Are you an optimist or a pessimist about the future?"], "TALK ABOUT IT")}""",
    32, """<ol><li>A: the stress is on <i>bound, likely, chance, tend</i>; <i>to</i> is short.</li>
<li>B: this is the Linguahouse speaking task, adapted for 1:1 (we left out national elections). C replaces the Linguahouse planner task: the student gives advice like Ana. Last 3 minutes: wrap-up (two corrections, and ask <i>Can you now plan a week and say how probable something is?</i>).</li></ol>""")

    # Homework
    pc = [(["went for", "went to"], "went for"), (["is bound to", "is bound"], "is bound to"), (["tend to be", "tend being"], "tend to be"),
          (["good", "big"], "good"), (["of getting", "to getting"], "of getting"), (["settle", "settled"], "settle")]
    p = [ch(o, a) for o, a in pc]
    rw2 = [("The interview is likely to go well. (good chance)", "There's a good chance (that) the interview will go well."),
           ("I'm sure the supermarket will be empty early on Sunday. (bound to)", "The supermarket is bound to be empty early on Sunday."),
           ("Danny probably won't skip the check-up. (unlikely to)", "Danny is unlikely to skip the check-up.")]
    rwl2 = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw2)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Danny writes to Ana on Wednesday night. Choose the correct words.", "")}</div>{img('C', 30, 19)}</div>
<div class="box" style="line-height:1.85;font-size:8.8pt;margin:.5mm 0"><b>Hi Ana!</b> Good news: I {p[0]} my check-up this morning, and the clinic was quiet, just like you said. Everything's fine! My interview {p[1]} be difficult, but I updated my resume yesterday, and the school's teachers {p[2]} young and friendly, so I'm not too nervous. Bruno says there's a {p[3]} chance he'll see his date again on Saturday. And you were right: I have a good chance {p[4]} the job if I stay calm. Let's have dinner on Friday. I'll {p[5]} the bill this time! Danny</div>
{sub("B", "Rewrite the sentences with the words in brackets.", "")}
<ol style="line-height:1.5;font-size:8.7pt;margin:0">{rwl2}</ol>
{lean.watch_out([("It's probable that he comes tomorrow.", "He's likely to come tomorrow. / He'll probably come tomorrow.", "<i>It's probable that</i> is formal and rare in speech."), ("There's a big chance of rain.", "There's a good chance of rain.", "with <i>chance</i>: <i>good, fair, slight, little, no</i>."), ("You have a good chance to win.", "You have a good chance of winning.", "<i>chance of</i> + -ing.")])}
{lean.writing_task(sub, "Write a message to a friend with advice for a busy week. Choose a day for each plan and explain why.", "Hi …! I've got some advice for your crazy week.", ["at least four plans and four days", "be bound to · be likely / unlikely to · tend to", "one expression with chance", "two key phrases from page 1", "100–150 words"], "I can plan a week and say how probable something is.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class. In A, the job interview is on Thursday, so Danny talks about it in the future. Read the writing at home and choose two mistakes to discuss in class.</p>""")

    script = "".join(f"<p style='margin:.5mm 0'>{'<i>' + t + '</i>' if s == 'Narrator' else '<b>' + s + ':</b> ' + t}</p>" for s, t in S411)
    b.extra("Audio script", f"""
{sub("41.1", "Gap Year Diaries: planning ahead (natural and slow; Danny and Ana)")}
<div style="line-height:1.3;font-size:8.4pt">{script}</div>
{sub("41.2", "Repeat: bound to, likely to")}
<p>{" · ".join(S412)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 41 - Planning ahead")
