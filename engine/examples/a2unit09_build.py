# Speak! Bridge A2 - Unit 09 "Old friends" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 09", audio_json="audio_a2-unit-09.json", img_dir="img")

PHOTOS = [("A", "graduate from college", "graduation"), ("B", "start a new job", "handshake"), ("C", "get married", "wedding rings"), ("D", "have a baby", "baby feet"),
          ("E", "buy a car", "new car"), ("F", "move to a new house", "moving boxes"), ("G", "open a store", "ribbon cutting"), ("H", "get a dog", "puppy")]

_r = json.load(open("roteiro.json"))["units"]["a2-unit-09"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["09.1 Messages"].split("\n")]
S092 = [x.split(": ", 1)[1] for x in _r["09.2 Repeat phrases"].split("\n")]
S093 = [x.split(": ", 1)[1] for x in _r["09.3 Repeat sentences"].split("\n")]
YEARS = {"twenty ten": "2010", "twenty twelve": "2012", "twenty fifteen": "2015", "twenty eighteen": "2018", "twenty twenty": "2020"}


def num(t):
    for w, d in YEARS.items():
        t = t.replace(w, d)
    return t


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 09", "Old friends", "Life events · <b>present perfect with for and since</b>",
                       [("YOU CAN", "catch up with an old friend and say how long things have been true"),
                        ("LANGUAGE", "I haven't seen you for ages! · I've lived there since 2015. · How long have you known her?"),
                        ("PRONUNCIATION", "for /fər/ · How long have you…? · I've known /aɪv noʊn/")])
    b.page(f"""{sec(1, "Warm-up: life events", "8 min")}
{sub("A", "Look at the photos. Write the life events under the photos.", "3 min")}
<div class="bank">buy a car · get a dog · get married · graduate from college · have a baby · move to a new house · open a store · start a new job</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Answer the questions.", "5 min")}
<ol><li>Which events do people usually do first? Put four of them in order. Is it the same in Brazil?</li>
<li>Draw a quick timeline of your life with three events: one past, one present, one future. Tell your teacher.</li></ol>""",
    22, """<ol><li>A: <b>graduate from</b> college (not <i>form</i>); <b>get married</b> (not <i>marry with</i>); <b>have a baby</b>.</li>
<li>B: accept any order; in many families today people buy a car or get a dog before they get married!</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Life events</td><td>1</td></tr>
<tr><td>2 Reading</td><td>10 min</td><td>Messages on a classmates website: Tom finds an old friend (with audio)</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Present perfect for unfinished situations · for and since · How long…?</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>For and since · the three uses of the present perfect</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>5 min</td><td>Weak for · questions with How long</td><td>5</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Rewrite with for / since · Word builder: life stages</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>The class reunion · How long have you…?</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework (50–75 words)</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>On a classmates website, <b>Tom</b> finds Megan (invented; one-off female voice, Studio-O), a friend from Lakeside College (invented), class of 2010. She moved to Seattle in 2015 and is a nurse at a children's hospital; Tom has taught at a Chicago high school since 2012 and online since 2020 (one of his students is Ana). Tom has a cat, Pancake; Megan has a dog, Biscuit. They plan to meet at Sweet Kate in March. The "for" numbers count from 2026.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Portuguese uses the present for situations that continue, so students say <i>I live here since 2015</i> ✗ → <b>I've lived here since 2015</b>; <i>I know her for ten years</i> ✗ → <b>I've known her for ten years</b>; <i>How long do you live here?</i> ✗ → <b>How long have you lived here?</b> They also mix <i>for / since</i>: <i>since ten years</i> ✗ → <b>for ten years</b>.</div>
<div class="box"><h4>AUDIO</h4>Track 09.1 The messages (slow and natural) · Track 09.2 For and since · Track 09.3 Sentences</div>""")

    # Page 2: reading (chat)
    def bubble(n, t):
        right = n == "Tom"
        bg = "#e7f1f3" if right else "#f4efe6"
        return (f"<div style='display:flex;justify-content:{'flex-end' if right else 'flex-start'};margin:.6mm 0'><div style='max-width:92%;background:{bg};border-radius:2mm;padding:.8mm 2mm;font-size:8pt;line-height:1.3;break-inside:avoid'>"
                f"<b style='color:#0f4a5a;font-size:7.5pt'>{n}</b><br>{num(t)}</div></div>")
    chat = "".join(bubble(n, t) for n, t in SCRIPT)
    words = [("Seattle", "M"), ("nurse", "M"), ("high school", "T"), ("cat", "T"), ("dog", "M"), ("online", "T"), ("married", "M"), ("Brazil", "T")]
    wl = " &nbsp; ".join(f"<b>{w}</b> {R('(' + ('Megan' if k == 'M' else 'Tom') + ')')}" for w, k in words)
    yrs = [("2010", "They graduated from college."), ("2012", "Tom started teaching at a high school."), ("2015", "Megan moved to Seattle."),
           ("2018", "Megan got married."), ("2020", "Tom started teaching online.")]
    yl = "".join(f"<li><b>{y}</b> {A(a, 'min-width:40mm')}</li>" for y, a in yrs)
    b.page(f"""{sec(2, "Reading: old friends", "10 min")}
<p>Tom finds an old friend on <i>ClassFinder</i>, a website for old classmates. Read and listen.</p>
{audiocard(["09.1 · SLOW", "09.1 · NATURAL"])}
<div style="border:1pt solid #c9dfe3;border-radius:2mm;padding:1mm 2mm;column-count:2;column-gap:4mm">{chat}</div>
<div class="two" style="margin-top:1mm"><div>{sub("A", "Who do these words relate to: Tom or Megan?", "3 min", "09.1 · SLOW")}
<p style="line-height:1.6">{wl}</p>
{sub("C", "Have you found an old friend online? Who?", "2 min")}</div>
<div>{sub("B", "What happened in these years?", "5 min")}
<ol style="padding-left:0;list-style:none">{yl}</ol></div></div>""",
    20, """<p>B: answers in the past simple. Then ask: <i>Does Megan still live in Seattle?</i> (yes): the key to page 3. Joke: pancakes and biscuits are breakfast foods.</p>""")

    # Page 3
    fs = ["2010", "six months", "9 o'clock", "March", "two days", "Tuesday", "ages", "I was a child", "eleven years", "college"]
    fsa = {"2010": "since", "six months": "for", "9 o'clock": "since", "March": "since", "two days": "for", "Tuesday": "since", "ages": "for", "I was a child": "since", "eleven years": "for", "college": "since"}
    fst = "".join(f"<td style='text-align:center'>{x}<br>{R(fsa[x])}</td>" for x in fs)
    b.page(f"""{sec(3, "Language focus: for and since", "10 min")}
{sub("A", "Read the sentences from the messages. Then choose the correct option.", "4 min")}
<div class="bank" style="background:#fff;font-weight:600">In 2015 I moved to Seattle. I've lived there for eleven years now. · I started teaching in 2012, and I've worked there since then. · We've been married for eight years.</div>
<ol><li>Megan {ch(["lives", "doesn't live"], "lives")} in Seattle now. Tom {ch(["works", "doesn't work"], "works")} at the high school now.</li>
<li><i>I moved / I started</i> (past simple) = a {ch(["finished", "unfinished"], "finished")} action in the past.</li>
<li><i>I've lived / I've worked</i> (present perfect) = a situation that started in the past and is {ch(["finished", "still true now"], "still true now")}.</li>
<li><b>for</b> + {ch(["a length of time", "the start"], "a length of time")} · <b>since</b> + {ch(["a length of time", "the start"], "the start")}</li></ol>
{sub("B", "Quick check: for or since?", "3 min")}
<table style="table-layout:fixed;margin-top:0;font-size:8.8pt"><tr>{fst}</tr></table>
{sub("C", "Make the question. Then answer about Megan and Tom.", "3 min")}
<ol><li>How long / Megan / live / in Seattle? {R("How long has Megan lived in Seattle? — For eleven years. / Since 2015.")}<div class="wline"></div></li>
<li>How long / Tom / have / Pancake? {R("How long has Tom had Pancake? — For five years.")}<div class="wline"></div></li></ol>
<div class="box sand"><h4>RULE</h4>Started in the past + true now → <b>present perfect</b> (not the present!): <i>I've lived here since 2015</i>, not <s>I live here since 2015</s>. Ask with <b>How long have you…?</b> More on page 4.</div>""",
    24, """<ol><li>A: draw a timeline: a point (past simple) vs a bar that continues to now (present perfect).</li>
<li>B: practice converting: <i>since 2015 → for eleven years</i> (from 2026).</li></ol>""")

    # Grammar reference (before Common mistakes)
    grammar_ref.present_perfect_for_since(b)

    # Page 4
    b.page(f"""{sub("D", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>I live here since 2015.</td><td><b>I've lived here since 2015.</b></td><td>still true = present perfect.</td></tr>
<tr><td>I know her for ten years.</td><td><b>I've known her for ten years.</b></td><td>still true = present perfect.</td></tr>
<tr><td>How long do you work there?</td><td><b>How long have you worked there?</b></td><td>How long + have you.</td></tr>
<tr><td>We're married since 2018.</td><td><b>We've been married since 2018.</b></td><td>be → have been.</td></tr>
<tr><td>She's been a nurse since ten years.</td><td><b>She's been a nurse for ten years.</b></td><td>length = for.</td></tr>
<tr><td>I haven't seen you since ages!</td><td><b>I haven't seen you for ages!</b></td><td>ages = a length.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "5 min")}
{audiocard(["09.2", "09.3"])}
{sub("A", "For and since. Listen and repeat. For is short: /fər/.", "2 min", "09.2")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(num(x) for x in S092)}</div>
{sub("B", "Sentences. Listen and repeat.", "2 min", "09.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S093)}</div>
<div class="box" style="margin-top:1mm"><h4>SAY IT NATURALLY</h4><b>How long have you</b> = /haʊ lɔŋ əv jə/: <i>have</i> is very short. Years: <i>2015</i> = <b>twenty fifteen</b>; <i>2010</i> = <b>twenty ten</b>. <i>I've known</i> = /aɪv noʊn/: the <i>k</i> is silent.</div>""",
    24, """<ol><li>4A: Brazilians often stress <i>for</i>. It's weak: <i>for <b>A</b>ges, for e<b>LE</b>ven years</i>.</li>
<li>4B: <i>I haven't seen you for ages!</i> is a very common, friendly greeting.</li></ol>""")

    # Page 5
    rw = [("Megan met her husband ten years ago.", "know", "Megan has known her husband for ten years."), ("Tom became a teacher in 2012.", "be", "Tom has been a teacher since 2012."),
          ("Megan bought her car three years ago.", "have", "Megan has had her car for three years."), ("Tom's last contact with Megan was in 2010.", "not see", "Tom hasn't seen Megan since 2010."),
          ("Kate opened Sweet Kate many years ago.", "have", "Kate has had Sweet Kate for many years."), ("Ana started English classes with Tom two years ago.", "study", "Ana has studied with Tom for two years.")]
    rwl = [f'<li value="{i+1}">{s} <span class="small">({v})</span><div class="wline">{R(a)}</div></li>' for i, (s, v, a) in enumerate(rw)]
    ls = [("be", "born"), ("grow", "up"), ("go to", "school"), ("graduate from", "college"), ("get", "a job"), ("get", "married"), ("have", "children"), ("retire", "")]
    lsl = " → ".join(f"<b>{v}</b> {A(n, 'min-width:12mm') if n else ''}" for v, n in ls)
    b.page(f"""{sec(5, "Practice", "8 min")}
{sub("A", "Write new sentences with the present perfect and for or since.", "5 min")}
{twocol(rwl, 4)}
{sub("B", "Word builder: life stages. Complete the words.", "3 min")}
<div class="bank">born · children · college · a job · married · school · up</div>
<p style="line-height:2">{lsl}</p>
<p class="small">Tell your teacher about someone in your family using four life stages: <i>My grandmother was born in 1950. She has been retired since…</i></p>""",
    22, """<ol><li>A: accept <i>has worked / has taught</i> for 6. Point out <i>has had</i> (have twice) and the negative with <i>since</i>.</li>
<li>B: from the bonus lesson <i>Life stages</i> (Vocabulary to Go). <i>be born</i> is passive: <i>I was born in…</i> (not <i>I born</i>).</li></ol>""")

    # Page 6
    rows = ["subject you studied", "where you live now (since when?)", "your job (since when?)", "married / single / partner?", "children or pets?", "something new you've bought", "a hobby you've had for a long time"]
    rt = "".join(f"<tr><td>{r}</td><td></td><td></td></tr>" for r in rows)
    b.page(f"""{sec(6, "Speaking", "12 min")}
{sub("A", "The class reunion. Imagine you graduated from college in 2015. Invent your life since then. Make notes. Then meet your old classmate (your teacher).", "8 min")}
<table style="table-layout:fixed;margin-top:0;font-size:9pt"><tr><th style="width:52mm"></th><th>about you</th><th>about your classmate</th></tr>{rt}</table>
<div class="msg" style="max-width:none;padding:1.5mm 4mm;line-height:1.5"><b>Teacher:</b> Hi! I haven't seen you for ages! What are you doing these days? <b>You:</b> Well, after college I moved to Recife. I've lived there for eight years. I've worked at a big hospital since 2019… And you? How long have you…?</div>
{sub("B", "Real life: how long?", "4 min")}
<ol><li>How long have you lived in your home?</li><li>How long have you known your best friend?</li><li>How long have you had your phone?</li><li>How long have you studied English?</li></ol>""",
    26, """<ol><li>A: play the classmate with an invented life too. Then compare: <i>What's the same about our lives?</i></li>
<li>B: correct every <i>I live here since…</i> immediately; ask for both answers: <i>for… / since…</i></li></ol>""")

    # Page 7
    pc = [("A2 Unit 05", "I can ask about words in class and name parts of speech."), ("A2 Unit 06", "I can praise, compliment and congratulate people, and respond politely."),
          ("A2 Unit 07", "I can talk about accidents that just happened with the present perfect."), ("A2 Unit 08", "I can ask about life experiences and give details with the past simple."),
          ("A2 Unit 09", "I can say how long things have been true with for and since.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    cm = [("I haven't seen you since ages.", "I haven't seen you for ages."), ("He knows his girlfriend since June.", "He's known his girlfriend since June."),
          ("We've lived here for six months.", "✓"), ("I had this coat for ten years, and I still love it.", "I've had this coat for ten years…"),
          ("My parents been married for 30 years.", "My parents have been married for 30 years."), ("She's been a nurse for 2020.", "She's been a nurse since 2020.")]
    cml = "".join(f"<li>{s} {R(a)}</li>" for s, a in cm)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Correct the mistakes. One sentence is correct.</b></p>
<ol>{cml}</ol>
<p style="margin-top:2mm"><b>2. Reply to an old friend (50–75 words).</b> An old classmate writes: <i>“Hi! I haven't seen you for ages! What are you doing these days?”</i> Answer with at least three sentences with <b>for</b> or <b>since</b>.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class: the student reads the reply aloud and you ask follow-up questions: <i>How long have you…? When did you…?</i> Then start the Review (Unit 10).</p>""")


    b.extra("Audio scripts", f"""
{sub("09.1", "The messages (slow and natural)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{n}:</b> {num(t)}" for n, t in SCRIPT)}</p>
{sub("09.2", "For and since")}
<p>{" · ".join(num(x) for x in S092)}</p>
{sub("09.3", "Sentences")}
<p>{" ".join(S093)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 09 - Old friends")
