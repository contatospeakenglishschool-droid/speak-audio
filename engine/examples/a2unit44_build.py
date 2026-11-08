# Speak! Bridge A2 - Unit 44 "Life hacks" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 44", audio_json="audio_a2-unit-44.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["a2-unit-44"]
S441 = [x.split(": ", 1) for x in _r["44.1 The Life Hacks podcast"].split("\n")]
S442 = [x.split(": ", 1)[1] for x in _r["44.2 Repeat: purpose and method"].split("\n")]
S443 = [x.split(". ", 1)[1] for x in [y.split(": ", 1)[1] for y in _r["44.3 To, for or by?"].split("\n")]]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 44", "Life hacks", "Smart solutions · <b>to, in order to, for, by, because</b>",
                       [("YOU CAN", "explain how to solve everyday problems and why a solution works"),
                        ("LANGUAGE", "To stop buttons from falling off, use nail polish. · For white sneakers, use toothpaste. · Do it by putting… · It works because…"),
                        ("PRONUNCIATION", "weak to /tə/ and for /fər/ · to, for or by?")])
    pr = [("My shoes are too tight.", "", "uncomfortable because they're too small"), ("I lost a button.", "A", ""), ("My shoes smell bad.", "", ""),
          ("My clothes have wrinkles.", "", ""), ("My sneakers look dirty.", "B", ""), ("My sneakers always get wet in the rain.", "C", ""),
          ("My zipper is stuck.", "D", ""), ("I lost a sock in the washing machine.", "E", "")]
    prl = "".join(f"<li>{p} {A(l if l else '–', 'min-width:8mm;text-align:center')}</li>" for p, l, _ in pr)
    b.page(f"""{sec(1, "Warm-up: clothes problems", "8 min")}
<div style="display:flex;gap:2mm;margin-bottom:1mm">{"".join(f'<div style="position:relative">{img(l, 32, 22)}<b style="position:absolute;top:1mm;left:1.5mm;background:#176074;color:#fff;border-radius:1mm;padding:0 1.2mm;font-size:8pt">{l}</b></div>' for l in "ABCDE")}</div>
{sub("A", "Which problems do the photos show? Write A–E. Three problems don't have a photo.", "3 min")}
<ol style="line-height:1.55;font-size:9pt;column-count:2;column-gap:6mm;margin:0">{prl}</ol>
{sub("B", "Talk about it.", "5 min")}
<ol style="line-height:1.5;margin:0"><li>Which three problems are the most annoying? Have you had any of them?</li><li>Can you suggest a solution to any of these problems?</li>
<li>A <b>life hack</b> is a smart, easy solution to an everyday problem. Do you know any good life hacks?</li></ol>""",
    22, """<ol><li>A: <i>tight</i> = too small, uncomfortable; <i>stuck</i> = it can't move; <i>wrinkles</i> = lines in clothes (you remove them with an iron). Sneakers (British: trainers).</li>
<li>B: accept any ideas; the podcast gives some solutions.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Problems with clothes and shoes</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>The Life Hacks podcast answers listeners' questions</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>to, in order to, for, by, because</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Explaining how and why</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>4 min</td><td>Weak to and for · to, for or by?</td><td>5</td></tr>
<tr><td>5 Practice</td><td>9 min</td><td>Home hacks: add the missing word</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Solve each other's problems with life hacks</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>The Life Hacks podcast (Host: Studio-O; co-host Rafael: Chirp3-HD-Charon, the Brazilian from the ice cream podcast in Unit 28) answers listeners' questions, and the listeners are our characters: Kate loses socks, Tom loses buttons, Lucy's backpack zipper is stuck, Priya hates ironing, Ana's shoes smell, Paulo gets wet feet in New York, and Carol's new shoes are tight. The hacks are popular household tips, not scientific facts: the ice cube tip is presented as "people say this works".</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students use <i>for</i> + verb for purpose (<i>I study for get a job</i>), forget <i>-ing</i> after <i>by</i> (<i>by use</i>), and say <i>for to</i>. They also confuse <i>because</i> and <i>because of</i>.</div>
<div class="box"><h4>AUDIO</h4>Track 44.1 The Life Hacks podcast (slow and natural) · Track 44.2 Repeat: purpose and method · Track 44.3 To, for or by?</div>""")

    # Page 2
    hk = [("Kate: lost socks", "a mesh bag"), ("Tom: falling buttons", "clear nail polish"), ("Lucy: a stuck zipper", "a candle or a pencil"), ("Priya: wrinkles", "ice cubes in the dryer"),
          ("Ana: smelly shoes", "dry tea bags"), ("Paulo: wet sneakers", "melted beeswax"), ("white sneakers", "toothpaste and an old toothbrush"), ("Carol: tight shoes", "wet newspaper")]
    hkl = [f'<li value="{i+1}">{p} → {A(s, "min-width:30mm")}</li>' for i, (p, s) in enumerate(hk)]
    op = [("Keep your socks together", ["by", "with"], "by", "putting them in a mesh bag."), ("Tom,", ["to stopping", "to stop"], "to stop", "buttons from falling off, use nail polish."),
          ("Lucy,", ["in order to", "in order that"], "in order to", "get a stuck zipper moving, rub it with a candle."), ("", ["About", "For"], "For", "fewer wrinkles, some people put ice cubes in the dryer."),
          ("People say this works", ["so", "because"], "because", "the ice melts and turns into steam."), ("Rub your sneakers with beeswax", ["you", "to"], "to", "make them more waterproof."),
          ("For super white", ["sneakers", "clean"], "sneakers", ", use toothpaste."), ("You can make tight shoes more comfortable by", ["put", "putting"], "putting", "wet newspaper inside.")]
    opl = [f'<li value="{i+1}">{(a + " ") if a else ""}{ch(o, r)}{"" if e[0] == "," else " "}{e}</li>' for i, (a, o, r, e) in enumerate(op)]
    b.page(f"""{sec(2, "Listening: the Life Hacks podcast", "10 min")}
<div style="display:flex;gap:2.5mm;align-items:center"><p style="flex:1;margin:0">On the Life Hacks podcast, the host and Rafael answer listeners' questions about clothes and shoes. Do you recognize the listeners?</p>{img('F', 26, 18)}</div>
{audiocard(["44.1 · SLOW", "44.1 · NATURAL"])}
{sub("A", "Listen. What solution do they give for each problem?", "4 min", "44.1 · SLOW")}
<div class="bank">a candle or a pencil · clear nail polish · dry tea bags · ice cubes in the dryer · melted beeswax · a mesh bag · toothpaste and an old toothbrush · wet newspaper</div>
<div style="font-size:8.8pt">{twocol(hkl, 5)}</div>
{sub("B", "Listen again and choose the correct option.", "5 min", "44.1 · NATURAL")}
<div style="font-size:8.8pt">{twocol(opl, 5)}</div>
{sub("C", "Which hack is the best? Which would you try?", "1 min")}""",
    27, """<ol><li>A: the listeners are all story characters; ask who each one is (Kate is Tom's sister, Carol is Paulo's cousin…). A <i>mesh bag</i> = a bag made of net.</li>
<li>These are popular household tips: some work better than others. The podcast says "people say" for the ice cube tip.</li></ol>""")

    # Page 3
    b.page(f"""{sec(3, "Language focus: explaining how and why", "10 min")}
{sub("A", "To and in order to. Read and choose.", "4 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">1 <b>To stop</b> buttons from falling off, paint the threads with nail polish. · 2 Rub your sneakers with beeswax <b>to make</b> them waterproof. · 3 <b>In order to get</b> a stuck zipper moving, rub it with a candle.</div>
<ol style="margin:.5mm 0;line-height:1.7"><li><i>To / in order to</i> + base form explains {ch(["how to get a result", "the result we want"], "the result we want")}.</li>
<li>The other part of the sentence explains {ch(["how to get it", "the result"], "how to get it")}.</li>
<li>When the <i>how</i> part comes first (sentence 2), we {ch(["need", "don't need"], "don't need")} a comma.</li>
<li>{ch(["To", "In order to"], "In order to")} is more formal.</li></ol>
{sub("B", "For and by. Read and choose.", "3 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">1 Keep your socks together <b>by putting</b> them in a mesh bag. · 2 <b>For super white sneakers</b>, use toothpaste. · 3 Make tight shoes more comfortable <b>by putting</b> wet newspaper inside.</div>
<ol style="margin:.5mm 0;line-height:1.7"><li>We use {ch(["by", "for"], "by")} + verb-ing to explain how. We use {ch(["by", "for"], "for")} + noun to say the result we want.</li></ol>
{sub("C", "Because. Read and choose.", "3 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">People say this works <b>because</b> the ice melts and turns into steam.</div>
<p style="margin:.5mm 0"><i>Because</i> introduces {ch(["the result we want", "the reason"], "the reason")}. It's followed by {ch(["a noun", "subject + verb"], "subject + verb")}.</p>
<div class="box sand"><h4>RULE</h4><b>result:</b> to / in order to + base form · for + noun &nbsp; <b>how:</b> by + verb-ing &nbsp; <b>why:</b> because + subject + verb. Never <i>for</i> + verb: <i>I came here to learn</i> ✗ <i>for learn</i>. More on the next page: <b>Grammar reference</b>.</div>""",
    20, """<ol><li>In Portuguese, one word often covers both purpose and benefit, which is why students say <i>for learn</i>.</li>
<li>Drill the examples; then ask personal questions: <i>Why are you learning English? To…</i></li></ol>""")

    grammar_ref.purpose_method(b)

    # Page 5
    tfb = ["to", "For", "by", "to", "by", "For"]
    tfbl = "".join(f"<li>{A(x, 'min-width:10mm;text-align:center')}</li>" for x in tfb)
    b.page(f"""{sub("D", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>I study English for get a better job.</td><td><b>I study English to get a better job.</b></td><td>purpose: to + verb.</td></tr>
<tr><td>Clean it by use a toothbrush.</td><td><b>Clean it by using a toothbrush.</b></td><td>by + verb-ing.</td></tr>
<tr><td>For to fix a zipper, use a pencil.</td><td><b>To fix a zipper, use a pencil.</b></td><td>no for to.</td></tr>
<tr><td>I went to the store for buy tea.</td><td><b>I went to the store to buy tea.</b></td><td>purpose: to + verb.</td></tr>
<tr><td>It works because of the ice melts.</td><td><b>It works because the ice melts.</b></td><td>because + subject + verb.</td></tr>
<tr><td>For have white sneakers, …</td><td><b>For white sneakers, …</b></td><td>for + noun.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "4 min")}
{audiocard(["44.2", "44.3"])}
{sub("A", "Listen and repeat. to = /tə/, for = /fər/: short and weak.", "2 min", "44.2")}
{twocol([f'<li value="{i+1}">{s}</li>' for i, s in enumerate(S442)], 3)}
{sub("B", "Listen to six home hacks. Do you hear to, for or by? Write it.", "2 min", "44.3")}
<ol style="line-height:1.5;column-count:3;column-gap:5mm">{tfbl}</ol>""",
    29, """<ol><li>A: <i>to</i> and <i>for</i> are weak in the middle of a sentence; <i>by</i> keeps its full vowel /baɪ/.</li>
<li>B: script: 1 Use vinegar to clean the shower head. 2 For a clean mirror, use old newspaper. 3 Find lost earrings by using a stocking. 4 I went to the store to buy some tea. 5 Save time by choosing your clothes the night before. 6 For a fresh fridge, use baking soda.</li></ol>""")

    # Page 6
    mw = [("Stop a pot from boiling over, put a wooden spoon across the top.", "<u>To</u> stop a pot from boiling over, …"),
          ("Find lost earrings covering the end of your vacuum cleaner with a stocking.", "Find lost earrings <u>by</u> covering…"),
          ("A clean shower head, tie a bag of vinegar and water around it overnight.", "<u>For</u> a clean shower head, …"),
          ("Order to get your mirrors really clean, use old newspaper.", "<u>In</u> order to get…"),
          ("Keep brown sugar soft putting a slice of bread in the bag.", "…soft <u>by</u> putting…"),
          ("Put an open box of baking soda in your fridge make it smell fresh.", "…in your fridge <u>to</u> make it smell fresh."),
          ("A clean microwave, heat a bowl of water and lemon in it for three minutes.", "<u>For</u> a clean microwave, …"),
          ("Lemon is good for cleaning it cuts grease.", "…for cleaning <u>because</u> it cuts grease.")]
    mwl = "".join(f"<li>{a}{(' ' + R('→ ' + c)) if T else ''}</li>" for a, c in mw)
    b.page(f"""{sec(5, "Practice", "9 min")}
<p style="margin:0 0 1mm">Next week, the Life Hacks podcast is about home hacks. Here are the host's notes.</p>
{sub("A", "One word is missing in each sentence: to, in, for, by or because. Add it in the correct place.", "6 min")}
<div class="box" style="margin-top:1mm;font-size:8.8pt"><b>Example:</b> In to remove gum from a carpet, use a bag of ice. → In <b>order</b> to remove gum from a carpet, use a bag of ice.</div>
<ol style="line-height:1.55;font-size:9pt;margin:0">{mwl}</ol>
{sub("B", "Which hack is new for you? Which would you try first? Do you know a good home hack?", "3 min")}""",
    20, """<ol><li>A: work alone first, then check. Ask the student to read each corrected sentence aloud with weak <i>to</i> and <i>for</i>.</li>
<li>These are common household tips; replace any that don't work in your experience.</li></ol>""")

    # Page 7
    sw = [("a paper clip. / tray, / In order / the SIM card / to open / use", "In order to open the SIM card tray, use a paper clip."),
          ("airplane mode. / by / charge faster / Make / putting it in / your phone", "Make your phone charge faster by putting it in airplane mode."),
          ("a clean keyboard, / between the keys. / For / a sticky note / to clean / use", "For a clean keyboard, use a sticky note to clean between the keys."),
          ("an old toilet paper roll. / by / each one inside / Organize / putting / your cables", "Organize your cables by putting each one inside an old toilet paper roll."),
          ("close to your face. / isn't too / make sure / protect your eyes, / the screen / To", "To protect your eyes, make sure the screen isn't too close to your face.")]
    swl = "".join(f"<li>{w}<br>{A(s, 'min-width:90mm')}</li>" for w, s in sw)
    tprob = ["My computer keyboard is so dirty. I eat at my desk.", "I use a computer all day, and I'm worried about my eyes.", "I have so many cables and chargers!", "I lost the tool that opens the SIM card tray.", "My phone charges really slowly."]
    myprob = ["I often feel too tired to do my work.", "I find it difficult to focus.", "I get stressed when my work isn't perfect.", "People keep asking me for help, and I have too much to do.", "Surprises at work make me late with my other tasks."]
    thacks = ["Keep your energy high by taking regular breaks.", "Stay focused by turning off email notifications.", "For good mental health, focus on \"good enough\", not \"perfect\".", "To avoid too much work, learn to say no politely.", "In order to deal with surprises, leave extra time in your plans."]
    b.page(f"""{sec(6, "Speaking: life hacks for you and me", "12 min")}
{sub("A", "Your teacher has problems with phones and computers. Put the words in order to make life hacks for your teacher.", "4 min")}
<ol style="line-height:1.4;font-size:8.6pt;margin:0">{swl}</ol>
{sub("B", "Listen to your teacher's problems. Choose the right hack and give your advice.", "3 min")}
<p class="small" style="margin:0">{R("Teacher's problems (in a different order): " + " · ".join(tprob)) if T else ""}</p>
{sub("C", "Now you have problems with work or studies. Read them to your teacher and listen to the hacks.", "4 min")}
<ol style="line-height:1.45;font-size:9pt;margin:0;column-count:2;column-gap:5mm">{"".join(f"<li>{p}</li>" for p in myprob)}</ol>
<p class="small" style="margin:.5mm 0">{R("Teacher's hacks: " + " · ".join(thacks)) if T else ""}</p>
{sub("D", "Which hack is the most useful for you? Do you have a better one?", "1 min")}""",
    24, """<ol><li>A–B: read the problems in a different order so the student has to listen. The airplane mode tip makes charging a little faster; it doesn't do miracles.</li>
<li>C: give the hacks in red from memory, using <i>to, for, by</i>; ask the student to repeat the one they like best.</li></ol>""")

    # Page 8
    pc = [("A2 Unit 41", "I can talk about quantities with some, any, much, many, enough and plenty of."), ("A2 Unit 42", "I can understand and give advice and instructions at a pharmacy."),
          ("A2 Unit 43", "I can explain the rules of a game."), ("A2 Unit 44", "I can explain how to solve a problem and why a solution works.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hm = [("To drink more water,", "keep a bottle on your desk."), ("Fall asleep faster by", "putting your phone in another room."), ("For a quick workout at work,", "take the stairs instead of the elevator."),
          ("Remember people's names by", "repeating the name in the conversation."), ("In order to save time in the morning,", "choose your clothes the night before."),
          ("Have walking meetings at work", "because sitting too much is bad for you.")]
    he = sorted(e for _, e in hm)
    hml = "".join(f"<li>{s} {A('abcdef'[he.index(e)], 'min-width:6mm;text-align:center')}</li>" for s, e in hm)
    hel = "".join(f"<li>{e}</li>" for e in he)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Healthy life hacks. Match the halves.</b></p>
<div style="display:flex;gap:4mm;font-size:8.8pt"><ol style="flex:1;line-height:1.5;margin:0">{hml}</ol><ol type="a" style="flex:1;line-height:1.5;margin:0">{hel}</ol></div>
<p style="margin-top:1.5mm"><b>2. My best life hacks (50–75 words).</b> Write three life hacks you use at home, at work or in your studies. Use <i>to</i>, <i>for</i>, <i>by</i> and <i>because</i>.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class: the student presents the hacks like a podcast host; you ask <i>Why does it work? How do you do it?</i></p>""")

    b.extra("Audio script", f"""
{sub("44.1", "The Life Hacks podcast (slow and natural)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in S441)}</p>
{sub("44.2", "Repeat: purpose and method")}
<p>{" · ".join(S442)}</p>
{sub("44.3", "To, for or by? (3-second pause)")}
<p>{" · ".join(S443)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 44 - Life hacks")
