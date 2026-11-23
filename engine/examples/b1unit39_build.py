# Speak! Progress B1 - Unit 39 "Making plans" (all English) - lean B1 format
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
setup(band="B1 · UNIT 39", audio_json="audio_b1-unit-39.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-39"]
S391 = [l.split(": ", 1) for l in _r["39.1 Two phone calls"].split("\n")]
S392 = [x.split(": ", 1)[1] for x in _r["39.2 Repeat: I'll be working"].split("\n")]


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
    cover = cover_html(T, "LEVEL B1 · UNIT 39", "Making plans", "Arranging, changing and canceling plans · <b>I'll be working · Will you be using…?</b>",
                       [("YOU CAN", "arrange to meet, say why you're not free, and change or cancel a plan"),
                        ("LANGUAGE", "an appointment · a get-together · Something has come up · put off · call off · will be + -ing"),
                        ("PRONUNCIATION", "I'll be working: contractions and weak forms")])
    kw = [("a formal arrangement to meet someone at a fixed time and place", "an appointment"), ("a planned romantic meeting between two people", "a date"),
          ("an informal meeting or small party with friends", "a get-together"), ("a medical examination to see if you are healthy", "a check-up"),
          ("a meeting where someone asks you questions for a job or a course", "an interview"), ("an arrangement to keep a table or a room for you", "a reservation")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:23mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Warm-up: busy week?", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["What are your plans for next week?", "Do you use a calendar app or a paper planner?", "How do you feel when someone cancels at the last minute?"], "START TALKING")}</div></div>
{sub("A", "Key words. Write the words from the box next to the definitions.", "3 min")}
<div class="bank">an appointment · a check-up · a date · a get-together · an interview · a reservation</div>
<div style="font-size:8.7pt">{twocol(kwl, 3)}</div>
{talk(["When was your last check-up? Do you have any appointments this month?", "For your birthday, do you prefer a big party or a small get-together?"], "USE THE WORDS")}""",
    26, """<ol><li>Start with the questions in the top box: 4 minutes.</li>
<li>A: quick check (3 minutes), then the two questions. The Linguahouse lesson also has <i>a dinner engagement</i> (very formal; rare in everyday American English), so we replaced it with <i>a reservation</i>.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Two phone calls: Danny and Ana arrange, then change a plan · questions · phrases for changing plans · Talk about it",
                      "the future continuous (will be + -ing); compare present continuous and will; state verbs", "Complete, choose · Use it (oral)",
                      "I'll be working (39.2) · role-play: arrange, then change a meeting", "Danny's group message · rewrite · word choice · writing"),
        """The Linguahouse lesson has two phone calls between two friends (arranging a movie, then canceling), expressions for making arrangements, phrasal vocabulary and the present continuous for plans. The present continuous for arrangements was already studied in this course, so we kept the functional language and the phrasal vocabulary and added a new B1 point: the future continuous, which people often use to say why they aren't free. Story: Danny's birthday is on Thursday (he was born on March 3). He calls Ana to invite her to a small get-together at the hostel. Saturday isn't good for her (she'll be working a twelve-hour shift), so they agree on Friday at eight. Bruno is going to Porto Alegre on Saturday morning. Mrs. Lima lets them use the kitchen. In the second call, Ana cancels: a colleague is sick and she'll be covering her night shift. They put it off till Sunday at 7:30 (Bruno's plane lands at six), and Ana will bring a cake. Homework: Danny's group message about the new plan. No real-world facts are given.""",
        """Overuse of <i>will be + -ing</i> for promises (<i>I'll be sending you…</i>); <i>I'm having an appointment</i> (state <i>have</i>); the false friend <i>compromise</i> for <i>plans</i>; <i>in Friday</i> for <i>on Friday</i>. Pronunciation: <i>I'll be</i> /aɪl bi/ is fast and weak; the main verb carries the stress (<i>I'll be WORKing</i>).""",
        "Track 39.1 Two phone calls (natural and slow; Danny and Ana) · Track 39.2 Repeat: I'll be working"))

    # Page 2 - Listening
    qs = [("Why can't Ana come on Saturday?", "She'll be working a twelve-hour shift."), ("When and where do they first arrange to meet?", "Friday at eight, at the hostel"),
          ("Why does Ana call back?", "A colleague is sick; she'll be covering her night shift."), ("Why can't they meet earlier on Sunday?", "Bruno's plane lands at six."),
          ("What's the final plan? What will Ana bring?", "Sunday, 7:30, at the hostel; a cake")]
    ql = "".join(f"<li>{q} {A(a, 'min-width:46mm')}</li>" for q, a in qs)
    ph = [("Something has come up.", "f"), ("I'm tied up all weekend.", "a"), ("Can we put it off till Sunday?", "c"), ("Can we move it up to Tuesday?", "d"),
          ("I have to call off the meeting.", "b"), ("Are we still on for Sunday?", "e")]
    df = ["a. busy, not available", "b. cancel", "c. change to a later time", "d. change to an earlier time", "e. Is the plan the same?", "f. Something happened that I didn't expect."]
    phl = "".join(f"<li>{s} {A(c, 'min-width:6mm')}</li>" for s, c in ph)
    b.page(f"""{sec(2, "Listening: a change of plans", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Listen to two phone calls between Danny and Ana. Answer the questions.", "4 min")}
<ol style="line-height:1.5;font-size:8.6pt;margin:0">{ql}</ol></div>{img('B', 34, 26)}</div>
{audiocard(["39.1 · NATURAL", "39.1 · SLOW"])}
<p style="margin:.6mm 0;font-size:8.6pt"><b>Think about it:</b> How does Danny feel when Ana cancels? How do you know? {A("disappointed, but he understands: <i>Oh no, that's a pity.</i> Then he's happy to change the day.", "min-width:40mm")}</p>
{sub("B", "Phrases for changing plans. Match the phrases (1–6) with the meanings (a–f).", "3 min")}
<div style="display:flex;gap:4mm;font-size:8.6pt"><ol style="line-height:1.5;margin:0;flex:1.2">{phl}</ol>
<div style="line-height:1.5;flex:1">{"<br>".join(df)}</div></div>
{talk(["Do you usually make plans weeks ahead or at the last minute?", "When was the last time something came up and you had to cancel? What did you say?", "Is it OK to cancel by text message? When isn't it OK?"])}""",
    30, """<ol><li>A: play the natural version; play the slow one if needed. 6 minutes. Danny's birthday is on Thursday; the get-together was on Friday and moved to Sunday.</li>
<li>B: the phrases come from the Linguahouse lesson. Also teach <i>meet up</i> (meet in order to do something together) and <i>pick up</i> (collect: <i>I'll pick up a cake</i>).</li>
<li>Talk about it: 4 minutes. Note Ana's sentences with <i>I'll be…ing</i> for page 3.</li></ol>""")

    # Page 3
    lean.grammar_in_class(b, grammar_ref.future_continuous)

    # Page 4 - Practice
    sat = [("9 a.m. – 1 p.m.", "lead a walking tour", "At ten, Danny will be leading a walking tour."),
           ("1 – 2 p.m.", "have lunch with Rafa", "At half past one, he'll be having lunch with Rafa."),
           ("2 – 4 p.m.", "study Portuguese", "At three, he'll be studying Portuguese."),
           ("4 – 7 p.m.", "cook for the get-together", "At five, he'll be cooking for the get-together."),
           ("7 – 8 p.m.", "wait for his friends", "At half past seven, he'll be waiting for his friends.")]
    satl = "".join(f'<tr><td style="white-space:nowrap">{t}</td><td>{a}</td><td>{A(s, "min-width:70mm")}</td></tr>' for t, a, s in sat)
    use = ["What will you be doing at this time tomorrow?", "What will you be doing next Saturday at 8 p.m.?",
           "Where do you think you'll be living in five years?", "Ask me a polite question about my plans: Will you be…?",
           "Name a day next week that isn't good for you. Why not?"]
    b.page(f"""{sec(4, "Practice: will be + -ing", "10 min")}
{sub("A", "Danny's plan for a busy Saturday. Write what he'll be doing at each time.", "4 min")}
<table style="font-size:8.6pt;margin:.5mm 0"><tr><th>time</th><th>plan</th><th>sentence</th></tr>{satl}</table>
{sub("B", "Choose.", "2 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0"><li>Friday isn't good for me. I {ch(["have", "'m having"], "have")} a dentist appointment.</li>
<li>Don't call me at nine. I {ch(["'ll watch", "'ll be watching"], "'ll be watching")} the game.</li>
<li>Sure, no problem. I {ch(["'ll send", "'ll be sending"], "'ll send")} you the address right now.</li></ol>
<div class="box sand"><h4>RULE</h4><b>will be + -ing</b> = in progress at a future time · <b>will</b> = a promise or a quick decision · state verbs (<i>have</i> = possess, <i>know</i>) are not continuous. See the <b>Grammar reference</b> on page 3.</div>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    24, """<ol><li>A–B: 6 minutes. In A, accept any time inside each slot.</li>
<li>Use it: 4 minutes, all oral. For question 4, the student asks you, for example <i>Will you be using your computer tonight?</i></li></ol>""")

    # Page 5 - Speaking
    card = f"""<div class="box" style="margin-top:1mm;font-size:8.3pt">{R("<b>Teacher's card:</b> Monday you'll be working late; Wednesday you're tied up all day; Thursday at 6 you'll be picking up a friend at the airport. Don't make it easy: say no to the first two suggestions. After you agree, call back: something has come up. Ask to put it off one day, or to move it up. End with: <i>So, are we still on for…?</i>")}</div>""" if T else ""
    b.page(f"""{sec(5, "Speaking: arrange it, then change it", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.3pt"><tr><th>suggesting</th><th>saying no</th><th>saying yes</th><th>changing plans</th></tr>
<tr><td><i>Shall we say Thursday? · How about eight? · Can you make it on Friday?</i></td><td><i>I'm afraid Friday isn't good for me. · I'm tied up. · I'll be working.</i></td><td><i>Friday sounds fine. · That works for me. · See you then!</i></td><td><i>Something has come up. · Can we put it off till…? · Can we do Sunday instead? · Are we still on for…?</i></td></tr></table></div>
{audiocard(["39.2"])}
{sub("A", "Listen and repeat. Say I'll be fast and weak, and stress the main verb: I'll be WORKing.", "4 min", "39.2")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S392))}</p>
{sub("B", "Your teacher wants to meet you for coffee next week. First, write three times when you're busy. Then find a time that works for both of you. Later, your teacher calls with a change of plans. Then change roles: invite your teacher to something, and you cancel.", "14 min")}
<div style="display:flex;gap:3mm;font-size:8.6pt;margin:.5mm 0"><div style="flex:1">Busy 1: {lines(1)}</div><div style="flex:1">Busy 2: {lines(1)}</div><div style="flex:1">Busy 3: {lines(1)}</div></div>{card}
{talk(["Are you a good planner, or do you prefer to be spontaneous?", "What's a good reason to cancel a plan? What's a bad one?"], "TALK ABOUT IT")}""",
    32, """<ol><li>A: <i>I'll be</i> sounds like /aɪl bi/; don't stress <i>be</i>.</li>
<li>B: use the teacher's card above. When the student invites you, accept, then cancel with a reason in the future continuous. Last 3 minutes: wrap-up (two corrections, and ask <i>Can you now arrange, change and cancel plans?</i>). This is the Linguahouse role-play, adapted for 1:1.</li></ol>""")

    # Homework
    pc = [(["will be working", "will working"], "will be working"), (["will be flying", "will fly be"], "will be flying"),
          (["has", "is having"], "has"), (["'ll be cooking", "'m cook"], "'ll be cooking"), (["on", "in"], "on")]
    p = [ch(o, a) for o, a in pc]
    rw = [("At ten tomorrow I'm at the gym, so I can't answer the phone. (will be + work out)", "At ten tomorrow I'll be working out at the gym."),
          ("Do you need the car tonight? (polite: Will you be…?)", "Will you be using the car tonight?"),
          ("We changed the meeting to a later day. (put off)", "We put off the meeting. / We put the meeting off.")]
    rwl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Danny writes to his friends. Choose the correct words.", "")}</div>{img('C', 28, 18)}</div>
<div class="box" style="line-height:1.85;font-size:8.8pt;margin:.5mm 0"><b>Hi everyone!</b> Change of plans: we've put off my birthday get-together till Sunday. Ana {p[0]} a night shift on Friday, and on Sunday afternoon Bruno {p[1]} back from Porto Alegre. So let's say 7:30. Mrs. Lima {p[2]} a big kitchen, and I {p[3]} all afternoon, so come hungry! Ana is bringing a cake. Are we still {p[4]} for Sunday? Danny</div>
{sub("B", "Rewrite the sentences with the words in brackets.", "")}
<ol style="line-height:1.5;font-size:8.7pt;margin:0">{rwl}</ol>
{lean.watch_out([("I can't go. I have a compromise.", "I can't go. I have plans. / I have something else on.", "a <i>compromise</i> is an agreement where both sides give something up."), ("I'll be sending you the report. (a promise)", "I'll send you the report.", "for a promise, use <i>will</i>."), ("Can you make it in Friday?", "Can you make it on Friday?", "<i>on</i> + day.")])}
{lean.writing_task(sub, "Write a message to a friend. Cancel a plan, explain why, suggest a new day and time, and check the details.", "Hi …! I'm really sorry, but something has come up.", ["an apology and a reason", "two sentences with will be + -ing", "a new day, time and place", "two phrases from page 5", "100–150 words"], "I can arrange, change and cancel plans.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class. Read the writing at home and choose two mistakes to discuss in class.</p>""")

    script = "".join(f"<p style='margin:.5mm 0'>{'<i>' + t + '</i>' if s == 'Narrator' else '<b>' + s + ':</b> ' + t}</p>" for s, t in S391)
    b.extra("Audio script", f"""
{sub("39.1", "Two phone calls (natural and slow; Danny and Ana)")}
<div style="line-height:1.3;font-size:8.4pt">{script}</div>
{sub("39.2", "Repeat: I'll be working")}
<p>{" · ".join(S392)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 39 - Making plans")
