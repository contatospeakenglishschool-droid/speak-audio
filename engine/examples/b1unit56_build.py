# Speak! Progress B1 - Unit 56 "Wide awake" (all English) - lean B1 format
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
setup(band="B1 · UNIT 56", audio_json="audio_b1-unit-56.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-56"]
S561 = [l.split(": ", 1) for l in _r["56.1 Gap Year Diaries: I'm not a morning person"].split("\n")]
S562 = [x.split(": ", 1)[1] for x in _r["56.2 Repeat: phrases with get"].split("\n")]




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
    cover = cover_html(T, "LEVEL B1 · UNIT 56", "Wide awake", "Sleep and mornings · <b>get up · get ready · get to sleep</b>",
                       [("YOU CAN", "talk about sleep and morning routines, and give tips to get up more easily"),
                        ("LANGUAGE", "a morning person · energized · hydrate · avoid · comforter · get + adjective / past participle / to"),
                        ("PRONUNCIATION", "flap t in American English: get up /ɡeɾ ʌp/, get out")])
    words = ["avoid", "a blind", "a comforter", "energized", "hydrate", "metabolism", "a morning person", "stimulate"]
    defs = {"avoid": "to keep away from something", "a blind": "a window cover that you pull down",
            "a comforter": "a thick, warm cover for a bed", "energized": "full of energy",
            "hydrate": "to give water to your body", "metabolism": "the processes in the body that turn food into energy",
            "a morning person": "someone who gets up early and has a lot of energy in the morning", "stimulate": "to make something more active"}
    order = [4, 7, 0, 6, 1, 3, 5, 2]
    kwl = "".join(f'<li>{A(words[i], "min-width:28mm")} <span style="color:#6b7377">= {defs[words[i]]}</span></li>' for i in order)
    b.page(f"""{sec(1, "Warm-up: are you a morning person?", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["Is getting up in the morning difficult for you?", "What time do you get up on weekdays? And on weekends?", "Do you use the snooze button?"], "START TALKING")}</div></div>
{sub("A", "Key words. Write the words from the box next to their meanings.", "3 min")}
<div class="bank">{" · ".join(words)}</div>
<ol style="font-size:8.6pt;line-height:1.7;margin:0">{kwl}</ol>
{talk(["Are you a morning person or a night owl?", "What do you avoid before bed?", "What makes you feel energized in the morning?"], "USE THE WORDS")}""",
    30, """<ol><li>Top box: 3 minutes. Teach <i>snooze button</i> (the button that gives you a few more minutes of sleep) and <i>night owl</i> (the opposite of a morning person).</li>
<li>A: 4 minutes with the questions. <i>Comforter</i> is American English; British English says <i>duvet</i>.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Gap Year Diaries: Ana gives Danny tips to get up for his 7 a.m. classes · order the tips · questions · Talk about it",
                      "the many uses of get: + noun, + adjective, + past participle, + place, + object + adjective / to-infinitive; get phrases", "Choose the meaning · rewrite with get · Use it (oral)",
                      "phrases with get (56.2) · sleep expressions · role-play: help Carol sleep · long turn: your mornings", "Carol's message to Ana · rewrite · watch out · writing: tips for a good morning"),
        """The Linguahouse lesson is a newspaper article with tips from a real sleep therapist and her book, including numbers about caffeine. We did not use the article: we cannot check those facts, and we avoid real people. Instead, Danny records a Gap Year Diaries episode with Ana (a doctor). Story: the language school gave Danny the 7 a.m. classes, and getting up is a nightmare. Ana gets up at 5:30 for the morning shift, with no snooze button. Her tips: plan the night before (clothes and bag ready); leave the phone out of the bedroom (get a real alarm clock); let some light in (curtains a little open); avoid coffee in the late afternoon and evening; drink a glass of water and have breakfast; have something to look forward to (for Danny: Mrs. Lima's cheese bread). Danny promises to get up at six; Ana will call him at one minute past six. The tips are presented as Ana's advice, not as scientific facts. We kept the Linguahouse key words, the phrases with get and the talking points, and added a grammar page on the uses of get.""",
        """<i>wake up</i> vs <i>get up</i>; <i>got in home</i> (→ <i>got home</i>); <i>He got that I buy</i> (→ <i>got me to buy</i>). Vocabulary: <i>I slept late</i> for <i>I went to bed late</i> (→ <i>I stayed up late</i>); <i>I lost the hour</i> (→ <i>I overslept</i>). Pronunciation: the American flap t in <i>get up</i>, <i>get out</i>.""",
        "Track 56.1 Gap Year Diaries: I'm not a morning person (natural and slow; Danny and Ana) · Track 56.2 Repeat: phrases with get"))

    # Page 2 - Listening
    tips = [("Avoid coffee in the late afternoon and evening.", "4"), ("Have something to look forward to.", "6"), ("Plan the night before.", "1"),
            ("Drink water and have breakfast.", "5"), ("Let some light in.", "3"), ("Leave your phone out of the bedroom.", "2")]
    tl = "".join(f'<li style="list-style:none">{A(n, "min-width:6mm")} {t}</li>' for t, n in tips)
    qs = [("Why is getting up a problem for Danny now?", "The language school gave him the 7 a.m. classes."),
          ("What does Danny usually spend twenty minutes doing?", "Looking for his keys."),
          ("Why can't Danny leave his phone out of the bedroom?", "It's his alarm clock (Ana: get a real one)."),
          ("What gets Danny up in the morning?", "Mrs. Lima's cheese bread at breakfast.")]
    ql = "".join(f"<li>{q} {A(a, 'min-width:44mm')}</li>" for q, a in qs)
    b.page(f"""{sec(2, "Listening: I'm not a morning person", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Listen to Danny and Ana. Number Ana's tips 1–6 in the order she gives them.", "4 min")}
<ul style="font-size:8.6pt;line-height:1.6;margin:0;padding-left:0">{tl}</ul></div>{img('B', 38, 28)}</div>
{audiocard(["56.1 · NATURAL", "56.1 · SLOW"])}
{sub("B", "Listen again and answer.", "4 min")}
<ol style="line-height:1.5;font-size:8.6pt;margin:0">{ql}</ol>
<p style="margin:.6mm 0;font-size:8.6pt"><b>Think about it:</b> Ana says she'll call "at one minute past six". Why? {A("she's joking, but she wants to check that Danny really got up at six", "min-width:20mm")}</p>
<div class="box sand" style="margin:.8mm 0;font-size:8.3pt"><h4>NOTICE: PHRASES WITH GET</h4>get up · get out of bed · get going · get to sleep · get off to a good start · get ready · What gets you up?</div>
{talk(["Which of Ana's tips do you already follow?", "Which tip would be the hardest for you?", "What gets you out of bed in the morning?"])}""",
    35, """<ol><li>A: play the natural version; play the slow one if needed.</li>
<li>B: ask the student to find every <i>get</i> and say what it means: <i>get up, get out of bed, get your clothes ready, get going, gets too excited, get to sleep, get a real alarm clock, get off to a good start, gets you up</i>. They come back on page 3.</li>
<li>Talk about it: 4 minutes. Ana's tips are advice, not medical facts: the student can agree or disagree.</li></ol>""")

    # Page 3
    lean.grammar_in_class(b, grammar_ref.get_uses)

    # Page 4 - Practice
    pc = [("I woke up at six, but I didn't", ["get up", "wake up"], "get up", "until seven."), ("It's", ["getting", "getting to"], "getting", "cold. Close the window."),
          ("What time did you get", ["home", "to home"], "home", "last night?"), ("They got", ["married", "marry"], "married", "in a small church."),
          ("Ana got Danny", ["to buy", "buy"], "to buy", "an alarm clock."), ("I can't get", ["to sleep", "sleep"], "to sleep", "after a coffee."),
          ("Get your bag", ["ready", "readily"], "ready", "the night before."), ("I'm getting", ["more and more tired", "more tired and tired"], "more and more tired", "every day.")]
    cl = "".join(f"<li>{a} {ch(o, r)} {z}</li>" for a, o, r, z in pc)
    rw = [("I received a strange message last night. (get)", "I got a strange message last night."),
          ("We arrived at the hostel at midnight. (get)", "We got to the hostel at midnight."),
          ("The weather became warmer in the afternoon. (get)", "The weather got warmer in the afternoon.")]
    rwl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw)
    use = ["What time did you get home yesterday? What did you do after you got home?", "How long does it take you to get ready in the morning?",
           "What do you do when you can't get to sleep?", "Is your city getting better or worse? How?",
           "Who got you to start learning English?"]
    b.page(f"""{sec(4, "Practice: get up, get ready, get going", "10 min")}
{sub("A", "Choose the correct words.", "3 min")}
<ol style="line-height:1.7;font-size:8.6pt;margin:0;columns:2;column-gap:6mm">{cl}</ol>
{sub("B", "Rewrite the sentences with get.", "4 min")}
<ol style="line-height:1.45;font-size:8.7pt;margin:0">{rwl}</ol>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    30, """<ol><li>A: 3 minutes. After each item, ask the meaning: <i>become, arrive, receive, persuade…</i></li>
<li>B: point out that <i>get</i> is less formal than <i>receive, arrive, become</i>: perfect for conversation, not for a formal email.</li>
<li>Use it: 3 minutes, all oral. Count the uses of <i>get</i> in the student's answers.</li></ol>""")

    # Page 5 - Speaking
    phr = [("get up", "to rise after sleeping"), ("get out of bed", "to leave the place you sleep"), ("get off to a good start", "to begin something well"),
           ("get going", "to start going somewhere"), ("get a good night's sleep", "to sleep well"), ("get back to something", "to continue something you started earlier")]
    card = f"""<div class="box" style="margin-top:1mm;font-size:8.2pt">{R("<b>Teacher's card (C):</b> you are Carol, Ana's cousin in Orlando. You can't sleep: you watch TV in bed until midnight, you drink coffee after dinner, your phone is on the pillow, and you get up at different times every day. You feel tired at work. Ask for advice and react: <i>That's a good idea. / I could never do that! / I'll try it.</i>")}</div>""" if T else ""
    b.page(f"""{sec(5, "Speaking: sleep tips", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE: TALKING ABOUT SLEEP</h4>
<table style="margin:0;font-size:8.2pt"><tr><th>good nights</th><th>bad nights</th><th>mornings</th><th>advice</th></tr>
<tr><td><i>I slept like a log. · I got a good night's sleep.</i></td><td><i>I tossed and turned. · I couldn't get to sleep. · I stayed up late.</i></td><td><i>I overslept. · I hit snooze three times. · I'm a night owl.</i></td><td><i>Have you tried…? · Why don't you…? · It might help to…</i></td></tr></table></div>
{audiocard(["56.2"])}
{sub("A", "Listen and repeat. In American English, the t in get up sounds like a soft d.", "2 min", "56.2")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S562))}</p>
{sub("B", "Phrases with get. Read the meanings, then make a true sentence about you with each phrase. Say them out loud.", "4 min")}
<ol style="font-size:8.5pt;line-height:1.5;margin:0;columns:2;column-gap:6mm">{"".join(f"<li><b>{p}</b> = {d}</li>" for p, d in phr)}</ol>
{sub("C", "Role-play. Your teacher is Carol, Ana's cousin. She can't sleep. Ask about her routine and give her advice.", "5 min")}{card}
{sub("D", "Discuss. Do you use your phone or watch TV just before bed? What do you do when you can't sleep? Describe your perfect morning.", "4 min")}""",
    30, """<ol><li>B comes from the Linguahouse phrases with get. C: Carol couldn't sleep in Unit 13 too (phone in bed, coffee): the student is now the expert. Push for <i>Have you tried…? / Why don't you…?</i></li>
<li>D comes from the Linguahouse talking point. Last 3 minutes: wrap-up (two corrections, and ask <i>Can you now talk about sleep and give tips?</i>).</li></ol>""")

    # Homework
    pc2 = [(["get to sleep", "get sleep"], "get to sleep"), (["got", "got to"], "got"), (["get", "go"], "get"),
           (["getting", "get to"], "getting"), (["got me to", "got that I"], "got me to"), (["got up", "woke"], "got up")]
    p = [ch(o, a) for o, a in pc2]
    rw2 = [("I arrived home very late. (get)", "I got home very late."), ("It's becoming very cold. (get)", "It's getting very cold."),
           ("My sister persuaded me to stop drinking coffee at night. (get … to)", "My sister got me to stop drinking coffee at night.")]
    rwl2 = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw2)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Carol writes to Ana after a week of trying her tips. Choose the correct words.", "")}</div>{img('C', 30, 19)}</div>
<div class="box" style="line-height:1.85;font-size:8.8pt;margin:.5mm 0"><b>Hi Ana!</b> Your tips are working! I used to watch TV in bed and couldn't {p[0]} until two a.m. This week I {p[1]} a real alarm clock and left my phone in the kitchen. Now I {p[2]} ready the night before, and I'm {p[3]} more energized every day. My neighbor even {p[4]} walk with her before work. Yesterday I {p[5]} at six-thirty, without the snooze button! Danny should try this too. Love, Carol</div>
{sub("B", "Rewrite the sentences with get.", "")}
<ol style="line-height:1.5;font-size:8.7pt;margin:0">{rwl2}</ol>
{lean.watch_out([("I slept late last night.", "I went to bed late / I stayed up late last night.", "<i>sleep late</i> = stay in bed late in the morning."), ("I lost the hour this morning.", "I overslept this morning.", "<i>oversleep</i> = sleep longer than you planned."), ("I got up at six, but I stayed in bed until seven.", "I woke up at six, but I didn't get up until seven.", "<i>wake up</i> = open your eyes; <i>get up</i> = leave the bed.")])}
{lean.writing_task(sub, "Write a post for Danny's podcast page: your tips for a good morning.", "My secret for a good morning is…", ["your morning routine", "three tips (and why they work for you)", "something you'd like to change", "at least four phrases with get", "100–150 words"], "I can talk about sleep and morning routines, and give tips to get up more easily.")}""",
    25, """<p>Check A and B in 3 minutes at the start of the next class. In A, <i>got me to walk</i> = persuaded me to walk. Read the writing at home and choose two mistakes to discuss in class.</p>""")

    script = "".join(f"<p style='margin:.5mm 0'><b>{s}:</b> {t}</p>" for s, t in S561)
    b.extra("Audio script", f"""
{sub("56.1", "Gap Year Diaries: I'm not a morning person (natural and slow; Danny and Ana)")}
<div style="line-height:1.3;font-size:8.3pt">{script}</div>
{sub("56.2", "Repeat: phrases with get")}
<p>{" · ".join(S562)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 56 - Wide awake")
