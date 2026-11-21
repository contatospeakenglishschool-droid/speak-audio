# Speak! Progress B1 - Unit 34 "Road and transport" (all English) - lean B1 format
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
setup(band="B1 · UNIT 34", audio_json="audio_b1-unit-34.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-34"]
S341 = [l.split(": ", 1)[1] for l in _r["34.1 Bruno's journey from hell"].split("\n")]
S342 = [x.split(": ", 1)[1] for x in _r["34.2 Repeat: was going to, was supposed to"].split("\n")]


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
    cover = cover_html(T, "LEVEL B1 · UNIT 34", "Road and transport", "A journey from hell · <b>was going to / was supposed to / was about to</b>",
                       [("YOU CAN", "talk about roads and transport, and tell the story of a journey that went wrong"),
                        ("LANGUAGE", "a highway · a traffic jam · catch / miss / get off · I was supposed to… · I was about to…"),
                        ("PRONUNCIATION", "weak forms: was going to, was supposed to")])
    kw = [("a big, fast road between cities", "a highway"), ("a place where two or more roads meet", "an intersection"),
          ("a marked place where people can cross the street", "a crosswalk"), ("a long line of cars that can't move", "a traffic jam"),
          ("to stop working (a car, a bus or a machine)", "break down"), ("a person who is walking, not driving", "a pedestrian")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:21mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Warm-up: on the road", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["How do you usually get around: by car, bus, subway, bike or on foot?", "What's the worst thing about driving in your city?", "Look at the photo. How would you feel in this situation?"], "START TALKING")}</div></div>
{sub("A", "Key words. Write the words from the box next to the definitions.", "3 min")}
<div class="bank">break down · a crosswalk · a highway · an intersection · a pedestrian · a traffic jam</div>
<div style="font-size:8.7pt">{twocol(kwl, 3)}</div>
{talk(["Is there a dangerous intersection or crosswalk near your home? Why is it dangerous?", "Has a car or a bus you were in ever broken down? What happened?"], "USE THE WORDS")}""",
    26, """<ol><li>Start with the questions in the top box: 4 minutes.</li>
<li>A: quick check (3 minutes), then the two questions. Point out American English: <i>highway, crosswalk, intersection, gas, subway, truck</i>.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Bruno's voice message: a journey from hell · gist · put the events in order · Talk about it",
                      "was going to, was supposed to, was about to; would", "Complete, choose · Use it (oral)",
                      "Weak forms (34.2) · tell the story of a difficult journey", "Ana's email to Tom · rewrite · word choice · writing"),
        """The Linguahouse lesson is vocabulary only (types of road, road signs, US and UK terms, transport verbs, driving problems, people who use transport). We kept its vocabulary and its talking point (a difficult journey) and added a B1 grammar point that fits a travel story: the future in the past. Bruno (programmer) flies to Porto Alegre for his mom's birthday lunch (his parents live there, Unit 9): he gets up late, calls a ride, gets stuck behind a truck that has broken down, the car runs out of gas, he catches a taxi, misses the plane by five minutes and arrives at five; his dad picks him up. All events are fictional; the unit states no real-world facts. In the homework, Ana answers Tom's question from Unit 33 about her commute to the hospital.""",
        """<i>It was for me to arrive at noon</i> (word-for-word translation) for <i>I was supposed to arrive</i>, dropping the <i>-d</i> in <i>supposed</i>, <i>I lost the bus</i> for <i>I missed the bus</i>, and <i>enter in the car</i> for <i>get in the car</i>. Pronunciation: <i>going to</i> /gənə/ and <i>supposed to</i> /səˈpoʊstə/ are weak in fast speech.""",
        "Track 34.1 Bruno's journey from hell (natural and slow; voice message, Bruno) · Track 34.2 Repeat: was going to, was supposed to"))

    # Page 2 - Listening
    ev = [("The car ran out of gas.", "4"), ("He missed the plane.", "6"), ("He got up late.", "1"), ("His dad picked him up.", "8"),
          ("He caught a taxi.", "5"), ("He got stuck in a traffic jam.", "3"), ("He caught the next flight.", "7"), ("He called a ride.", "2")]
    evl = "".join(f"<li style='list-style:none'>{A(n, 'min-width:6mm')} {s}</li>" for s, n in ev)
    b.page(f"""{sec(2, "Listening: Bruno's journey from hell", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Bruno sends Danny a voice message. Listen and answer.", "3 min")}
<ol style="line-height:1.6;font-size:8.8pt;margin:0"><li>Why was Bruno going to Porto Alegre? {A("for his mom's birthday lunch", "min-width:40mm")}</li>
<li>Did he get there on time? {A("No. He arrived at five and missed the lunch.", "min-width:40mm")}</li></ol></div>{img('B', 40, 27)}</div>
{audiocard(["34.1 · NATURAL", "34.1 · SLOW"])}
{sub("B", "Listen again. Number the events in order (1–8).", "4 min")}
<ul style="line-height:1.55;font-size:8.8pt;margin:0;padding-left:2mm;columns:2">{evl}</ul>
<div class="box sand"><h4>NOTICE: TRANSPORT VERBS</h4><b>catch / miss / get on / get off</b> a bus, a train, a plane · <b>get in / get out of</b> a car, a taxi · <b>call a ride</b> · <b>run out of</b> gas · <b>get stuck</b> in traffic · <b>pick someone up</b> at the airport</div>
{talk(["Was calling a ride a mistake? What would you have done?", "Have you ever missed a plane, a bus or a train? What happened?", "What's the best way to get to the airport in your city?"])}""",
    30, """<ol><li>A: play the natural version once; B: play it again (slow version if needed). 7 minutes.</li>
<li>The notice box comes from the Linguahouse transport phrases. Ask the student to find three of these verbs in the story (<i>called a ride, got out of the car, caught a taxi, missed the plane</i>).</li>
<li>Talk about it: 5 minutes. Note any sentences about plans that changed for page 3.</li></ol>""")

    # Page 3
    lean.grammar_in_class(b, grammar_ref.future_in_past)

    # Page 4 - Practice
    fs = [("I ___ take the subway, but I got up late.", "was going to"), ("My flight ___ leave at eleven, but I got there at ten fifty.", "was supposed to"),
          ("The driver ___ call a friend when I got out of the car.", "was about to"), ("We ___ have lunch together at one, but I wasn't there.", "were supposed to"),
          ("I ___ give up when I saw a taxi at the intersection.", "was about to")]
    fsl = "".join(f'<li>{d.replace("___", A(a, "min-width:26mm"))}</li>' for d, a in fs)
    use = ["Tell me something you were going to do last weekend, but didn't. Why not?", "What were you supposed to do this week that you haven't done yet?",
           "Tell me about a time you were about to leave home when something happened.", "When you were a teenager, what did you think you would do as a job?",
           "Have you ever been to a place that was supposed to be great, but wasn't?"]
    b.page(f"""{sec(4, "Practice: was going to, was supposed to, was about to", "10 min")}
{sub("A", "Complete Bruno's sentences with was / were going to, was / were supposed to or was about to.", "4 min")}
<ol style="line-height:1.75;font-size:8.9pt;margin:0">{fsl}</ol>
{sub("B", "Choose.", "2 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0"><li>I was going to {ch(["call", "called"], "call")} you, but my phone died.</li>
<li>I thought the bus {ch(["will", "would"], "would")} be late.</li>
<li>The train was {ch(["suppose", "supposed"], "supposed")} to arrive at six.</li></ol>
<div class="box sand"><h4>RULE</h4><b>was going to</b> = a plan · <b>was supposed to</b> = an arrangement or a schedule · <b>was about to</b> = very soon · all + the base form of the verb · <b>would</b> after <i>thought, knew, hoped</i>. See the <b>Grammar reference</b> on page 3.</div>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    24, """<ol><li>A–B: 6 minutes. In A, other answers are possible if the student can explain them (1 <i>was supposed to</i> is possible if it was a fixed plan; 5 <i>was going to</i> is possible).</li>
<li>Use it: 4 minutes, all oral. Ask a follow-up question each time (<i>So what happened?</i>).</li></ol>""")

    # Page 5 - Speaking
    pr = ["miss the bus, the train or the plane", "get stuck in a traffic jam", "the car breaks down", "run out of gas", "get on the wrong train",
          "get off at the wrong stop", "a flat tire", "a bus or subway strike", "the road is closed for roadwork", "lost luggage"]
    pl = "".join(f"<li>{x}</li>" for x in pr)
    b.page(f"""{sec(5, "Speaking: a journey from hell", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.3pt"><tr><th>starting</th><th>sequencing</th><th>reacting (listener)</th><th>finishing</th></tr>
<tr><td><i>You won't believe what happened… · So, I was supposed to… · It all started when…</i></td><td><i>Then… · After that… · Just as I was about to… · By the time I got there…</i></td><td><i>No way! · Oh no! · What did you do? · That sounds like a nightmare!</i></td><td><i>In the end… · Luckily… · The good part is… · Anyway, …</i></td></tr></table></div>
{audiocard(["34.2"])}
{sub("A", "Listen and repeat. Say the forms quickly (the d in supposed is silent).", "4 min", "34.2")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S342))}</p>
{sub("B", "Tell the story of a difficult journey. Use a real journey, or invent one with four problems from the list. Say what was supposed to happen and what went wrong. Your teacher reacts and asks questions. Then listen to your teacher's story and react.", "14 min")}
<ol style="line-height:1.4;font-size:8.8pt;margin:0;columns:2">{pl}</ol>
{talk(["Is it better to drive or to use public transport in your city? Why?", "What would make the streets in your city safer for pedestrians and cyclists?"], "TALK ABOUT IT")}""",
    32, """<ol><li>A: <i>going to</i> /gənə/, <i>supposed to</i> /səˈpoʊstə/; the stress is on the main verb (<i>I was going to TAKE the bus</i>).</li>
<li>B: give the student 1 minute to plan, then 3–4 minutes to tell the story. React with the listener phrases and ask questions. Then tell your own story (real, or Bruno's from the point of view of the taxi driver) and let the student react. Last 3 minutes: wrap-up (two corrections, and ask <i>Can you now tell the story of a journey that went wrong?</i>).</li></ol>""")

    # Homework
    pc = [(["was supposed", "was suppose"], "was supposed"), (["was going to", "was about to"], "was going to"), (["caught", "lost"], "caught"),
          (["get off", "get out of"], "get off"), (["about to", "about"], "about to"), (["got in", "got on"], "got in"), (["would", "will"], "would")]
    p = [ch(o, a) for o, a in pc]
    rw = [("I planned to take the bus, but it didn't come. (was going to)", "I was going to take the bus, but it didn't come."),
          ("The train was scheduled to arrive at six, but it arrived at seven. (was supposed to)", "The train was supposed to arrive at six, but it arrived at seven."),
          ("I nearly left home, and then it started to rain. (was about to … when)", "I was about to leave home when it started to rain.")]
    rwl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Ana answers Tom's email about her commute. Choose the correct words.", "")}</div>{img('C', 28, 18)}</div>
<div class="box" style="line-height:1.85;font-size:8.8pt;margin:.5mm 0"><b>Hi Tom,</b><br>Cycling to school? Good for you! My commute is a different story. Last Monday I {p[0]} to start my shift at seven, so I left home at six. I {p[1]} drive, as usual, but Marcos had the car, so I {p[2]} the subway. At the third station, everybody had to {p[3]} the train because of a problem on the line. I was {p[4]} call the hospital when a colleague offered me a ride. We {p[5]} her car and got there at 7:05. Not bad! I thought I {p[6]} be much later. Ana</div>
{sub("B", "Rewrite the sentences with the words in brackets.", "")}
<ol style="line-height:1.5;font-size:8.7pt;margin:0">{rwl}</ol>
{lean.watch_out([("I lost the bus.", "I missed the bus.", "<i>miss</i> a bus, train or plane; <i>lose</i> = you can't find something."), ("We ran out of petrol on the motorway.", "We ran out of gas on the highway.", "American English: <i>gas, highway, subway, truck, parking lot</i>."), ("I entered in the taxi.", "I got in the taxi.", "<i>get in / out of</i> a car or taxi; <i>get on / off</i> a bus, train or plane.")])}
{lean.writing_task(sub, "Write an email to a friend about a difficult journey (real or invented). What was supposed to happen? What went wrong? How did it end?", "You won't believe what happened on my way to…", ["what was supposed to happen", "three problems", "was going to / was supposed to / was about to", "three transport verbs", "100–150 words"], "I can tell the story of a difficult journey and talk about plans that changed.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class. The writing task is the Linguahouse talking point. Read it at home and choose two mistakes to discuss in class.</p>""")

    script = "".join(f"<p style='margin:.5mm 0'>{l}</p>" for l in S341)
    b.extra("Audio script", f"""
{sub("34.1", "Bruno's journey from hell (natural and slow; voice message, Bruno)")}
<div style="line-height:1.3;font-size:8.6pt">{script}</div>
{sub("34.2", "Repeat: was going to, was supposed to")}
<p>{" · ".join(S342)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 34 - Road and transport")
