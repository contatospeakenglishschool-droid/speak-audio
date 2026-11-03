# Speak! Bridge A2 - Unit 15 "Burgers, fries, shakes" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 15", audio_json="audio_a2-unit-15.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["a2-unit-15"]
NAMES = {"Tom": "Tom", "Lucy": "Lucy"}
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["15.1 Takeout"].split("\n")]
S152 = [x.split(": ", 1)[1] for x in _r["15.2 Repeat words"].split("\n")]
S153 = [x.split(": ", 1)[1] for x in _r["15.3 Repeat sentences"].split("\n")]
PHOTOS = [("A", "veggie burger", "a veggie burger"), ("B", "shake", "a milkshake"), ("D", "sweet potato", "a sweet potato"), ("E", "oats", "oats"),
          ("F", "nuts", "nuts"), ("G", "green beans", "green beans"), ("H", "buns", "bread rolls"), ("I", "flour", "flour")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 15", "Burgers, fries, shakes", "Takeout food · <b>first, then, finally · at first, at last</b>",
                       [("YOU CAN", "describe a meal step by step and talk about changing your mind"),
                        ("LANGUAGE", "First, there's no meat. Then, there are no fries. · At first, I didn't like it, but then I loved it."),
                        ("PRONUNCIATION", "first /fɜːrst/ · third /θɜːrd/ · at LAST · TAKEout")])
    b.page(f"""{sec(1, "Warm-up: food words", "8 min")}
{sub("A", "Look at the photos. Write the words under the photos.", "4 min")}
<div class="bank">buns · flour · green beans · nuts · oats · shake · sweet potato · veggie burger</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Talk about it.", "4 min")}
<ol><li>Which of these things do you eat? Which do you never eat?</li><li>Can you make a meal with some of these things? What can you make?</li><li>Do you order takeout? What do you usually order?</li></ol>""",
    22, """<p>A: <b>veggies</b> is informal for vegetables; a <b>veggie burger</b> has no meat. <b>Buns</b> are the round bread for burgers. <b>Shake</b> = milkshake. B3: <b>takeout</b> (American) = restaurant food that you eat at home (British: takeaway).</p>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Food vocabulary</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Tom and Lucy read a strange takeout menu</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>First, second, then, finally · at first … but then · at last</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Sequencers · first / at first · finally / at last · then / than · made with / from / of</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>5 min</td><td>Ordinal sounds · pausing after sequencers</td><td>5</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Tom tells a friend · Word builder: takeout and delivery</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Role-play: our takeout experience</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework (50–75 words)</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Tom and Lucy (Chicago; voices Neural2-D and Neural2-C, as in Units 04, 07 and 11) look at the menu of a new burger place on their street. The restaurant is invented. Facts: North Carolina has been the top sweet potato producer in the U.S. since 1971 (USDA Economic Research Service, "Charts of Note"); cricket flour is sold as a food in the U.S. and is high in protein. Tom mentions an acai bowl in Miami: acai bowls, from Brazil, are popular in the U.S. In the U.S. it's customary to tip delivery drivers.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students confuse <i>first</i> (number 1 in a list) with <i>at first</i> (my feeling in the beginning), and <i>finally / lastly</i> (the last item) with <i>at last</i> (after a long wait). They also write <i>then</i> for <i>than</i> and say <i>history</i> for a personal story (<i>Let me tell you a history</i> ✗ → <b>a story</b>).</div>
<div class="box"><h4>AUDIO</h4>Track 15.1 Tom and Lucy order takeout (slow and natural) · Track 15.2 Sequencers · Track 15.3 Sentences with sequencers</div>""")

    # Page 2
    tf = [("Tom and Lucy have eaten at this burger place before.", "F: it's new."), ("The burgers are made from meat.", "F: no meat; bean and nut burgers."),
          ("You can only get buns with cricket flour.", "F: you can get normal buns too."), ("You can order fries.", "T: sweet potato fries."),
          ("Only Tom orders food.", "F: they both order."), ("The restaurant doesn't use plastic bags.", "T: recycled paper.")]
    tfl = [f'<li value="{i+1}">{s} <b>T / F</b> {R(a)}</li>' for i, (s, a) in enumerate(tf)]
    qs = [("How many things are strange about the menu?", "four: burgers, buns, fries, shake (five with the paper bags)"),
          ("How does Tom feel about the menu? Why?", "excited: the other places are all the same and he's bored"),
          ("How does Lucy feel at the beginning?", "she isn't sure"),
          ("What story does Tom tell about Miami?", "at first Lucy didn't want an acai bowl, but then she ate his"),
          ("What do they order?", "Lucy: bean burger, sweet potato fries · Tom: nut burger, chocolate shake")]
    qsl = "".join(f"<li>{q}<div class='wline'>{R(a)}</div></li>" for q, a in qs)
    b.page(f"""{sec(2, "Listening: a strange menu", "10 min")}
<p>Tom and Lucy are at home in Chicago. They don't feel like cooking, and a new burger place on their street has sent them a menu.</p>
{audiocard(["15.1 · SLOW", "15.1 · NATURAL"])}
{sub("A", "Listen. True (T) or false (F)? Correct the false sentences.", "4 min", "15.1 · SLOW")}
{twocol(tfl, 3)}
{sub("B", "Listen again and answer the questions.", "6 min", "15.1 · NATURAL")}
<ol>{qsl}</ol>""",
    22, """<p>Pre-teach <b>takeout</b> and <b>cricket</b> (a small jumping insect). B1: accept four or five. Ask: "Would you try cricket flour?" Fact: North Carolina grows more sweet potatoes than any other state (USDA).</p>""")

    # Page 3
    b.page(f"""{sec(3, "Language focus: putting ideas in order", "10 min")}
{sub("A", "Read Lucy's sentences. Then choose the correct options.", "4 min")}
<div class="bank" style="background:#fff"><b>First,</b> there's no meat in any of the burgers. · <b>Second,</b> the buns are made with cricket flour. · <b>Then,</b> there are no potato fries. · That's <b>the last</b> strange thing on the menu.</div>
<ol><li>We use these words for {ch(["contrasting ideas", "connecting ideas in a list"], "connecting ideas in a list")}.</li>
<li>We {ch(["can", "can't"], "can")} say <i>firstly, secondly, lastly</i> at the start of a sentence.</li>
<li>We {ch(["can", "can't"], "can")} use <i>first, second, last</i> before a noun: <i>the last thing</i>.</li>
<li>We can also use <i>next</i> instead of {ch(["then", "than"], "then")}.</li>
<li>These words help the listener {ch(["understand", "sound formal"], "understand")}. We also use them to tell a {ch(["history", "story"], "story")}.</li></ol>
{sub("B", "Read Tom's sentences. Then choose.", "4 min")}
<div class="bank" style="background:#fff"><b>At last,</b> something different! · <b>At first,</b> you didn't want to try it, <b>but then</b> you tasted mine and you ate the whole thing!</div>
<ol><li><i>At last</i> shows that Tom waited a {ch(["long", "short"], "long")} time for something new.</li>
<li>Lucy's first feelings about the acai bowl were {ch(["positive", "negative"], "negative")}.</li>
<li><i>But then</i> shows that Lucy {ch(["changed", "didn't change"], "changed")} her mind.</li>
<li>Her final feelings were {ch(["positive", "negative"], "positive")}.</li></ol>
<div class="box sand"><h4>RULE</h4><b>First</b> = number 1 in a list. <b>At first</b> = my feeling in the beginning (it changes later: <i>but then</i>). <b>At last</b> = after a long wait. More on the next page: <b>Grammar reference</b>.</div>""",
    24, """<ol><li>A: <i>then</i> (next) and <i>than</i> (comparisons) sound almost the same; write both on the board. <i>History</i> = the past of a country; <i>story</i> = what happened to someone.</li>
<li>B: we use <i>at first</i> and <i>but then</i> as a pair.</li></ol>""")

    grammar_ref.sequencers(b)

    # Page 5
    b.page(f"""{sub("C", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>At first, we ordered burgers. Then, fries.</td><td><b>First, we ordered burgers.</b></td><td>a list = first.</td></tr>
<tr><td>First, I didn't like it, but then I loved it.</td><td><b>At first, I didn't like it, …</b></td><td>a change of feeling.</td></tr>
<tr><td>The food arrived after an hour. Finally!</td><td><b>At last!</b></td><td>after a long wait.</td></tr>
<tr><td>The fries were better then the burger.</td><td><b>… better than the burger.</b></td><td>than = comparison.</td></tr>
<tr><td>Let me tell you a history.</td><td><b>Let me tell you a story.</b></td><td>history = the past.</td></tr>
<tr><td>The shake is made of oat milk.</td><td><b>… made with oat milk.</b></td><td>with = ingredient.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "5 min")}
{audiocard(["15.2", "15.3"])}
{sub("A", "Sequencers. Listen and repeat.", "2 min", "15.2")}
<table style="table-layout:fixed;margin-top:0"><tr>{"".join(f"<td style='text-align:center'><b>{w}</b></td>" for w in S152)}</tr></table>
<p class="small">{R("first and third: the same vowel /ɜːr/ as in bird · at LAST: stress on last")}</p>
{sub("B", "Sentences. Listen and repeat. Make a short pause after the sequencer.", "2 min", "15.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S153)}</div>
<div class="box" style="margin-top:1mm"><h4>TH SOUNDS</h4><b>third</b> /θ/: put your tongue between your teeth and blow (not <i>tird</i> or <i>fird</i>) · <b>then / than</b> /ð/: the same position, with voice.</div>""",
    24, """<ol><li>4A: many students say <i>firsty</i>; there is no vowel at the end of <i>first</i>.</li>
<li>4B: the voice goes up a little on the sequencer, then a pause.</li></ol>""")

    # Page 6
    tx = [(["First,", "At first,", "Firstly,"], "At first,"), (["Next,", "And next,", "But then,"], "But then,"), (['"No thanks."', '"Let\'s try it."', '"That\'s crazy."'], '"Let\'s try it."'),
          (["First,", "At first,", "At last,"], "First,"), (["Last,", "But then,", "At last,"], "At last,"), (["At second,", "Then,", "But then,"], "Then,"),
          (["secondly", "third", "thirdly"], "third"), (["last", "at last", "lastly"], "last")]
    o = [ch(x, a) for x, a in tx]
    wb = [("order", "online or by phone"), ("deliver", "the food to your home"), ("pick up", "the food at the restaurant"),
          ("pay", "a delivery fee"), ("leave", "a tip for the driver"), ("read", "the reviews")]
    wbl = [f'<li value="{i+1}">{A(v, "min-width:14mm")} {n}</li>' for i, (v, n) in enumerate(wb)]
    b.page(f"""{sec(5, "Practice", "8 min")}
{sub("A", "Tom is telling his friend Jake about the new burger place. Read the whole text first. Then choose the best words.", "5 min")}
<div class="msg" style="max-width:none;font-size:9pt;line-height:1.55">You know that new burger place on our street? Well, Lucy and I got takeout from there last night. The menu is really strange. There's no meat in the burgers! <sup>1</sup>{o[0]} I thought it was a mistake. <sup>2</sup>{o[1]} I read about it online, and they want to do something different, so I thought, <sup>3</sup>{o[2]} We ordered lots of things. <sup>4</sup>{o[3]} we got the burgers. They were OK, but a little dry. The buns had cricket flour in them! <sup>5</sup>{o[4]} a new use for insects! <sup>6</sup>{o[5]} we had sweet potato fries. They were really good! The <sup>7</sup>{o[6]} thing was an oat milk shake. That was definitely the best thing. Oh, and the <sup>8</sup>{o[7]} thing: they don't use any plastic.</div>
{sub("B", "Word builder: takeout and delivery. Complete with the verbs.", "3 min")}
<div class="bank">deliver · leave · order · pay · pick up · read</div>
{twocol(wbl, 3)}
<p class="small">What do you do before you order takeout? <i>First, I read the reviews. Then, …</i></p>""",
    22, """<ol><li>A: the student explains each answer with the rule. 7: <i>third</i> before a noun.</li>
<li>B: in the U.S. people usually <b>leave a tip</b> for the delivery driver, often in the app.</li></ol>""")

    # Page 7
    plan = [("Teacher", "Have you tried that new burger place?"), ("You", "Yes, I have."), ("Teacher", "What was your meal like?"),
            ("You", "Well, first, … Then, … Finally, …"), ("Teacher", "And what did you think?"), ("You", "At first, … but then … What did you order?"),
            ("Teacher", "(describes the meal and the delivery)"), ("You", "(react) Would you order from there again?")]
    pl = "".join(f"<tr><td style='width:18mm'><b>{w}</b></td><td>{s}</td></tr>" for w, s in plan)
    b.page(f"""{sec(6, "Speaking: our takeout experience", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">
<div style="flex:1">{sub("A", "You tried the new burger place too. Read about your meal and add one more detail about the staff.", "3 min")}
<div class="box" style="margin-top:1mm">Your meal: a <b>tofu burger</b>, <b>rice fries</b> and <b>nut milk ice cream</b>.<br>Your extra detail: the staff were… (friendly? slow? funny?)</div></div>
<div style="width:40mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo('B')}" style="width:40mm;height:28mm;object-fit:cover;display:block"></div></div>
{sub("B", "Have the conversation with your teacher. Follow the plan.", "6 min")}
<table style="table-layout:fixed;margin-top:1mm;font-size:9pt">{pl}</table>
<p class="small" style="margin:1mm 0">Now do it again and use <b>At last!</b> one time (a long wait for the food? the driver?).</p>
{sub("C", "Your turn.", "3 min")}
<ol><li>Tell your teacher about a food that you didn't like at first. Do you like it now?</li><li>What's the strangest thing you have ever eaten?</li></ol>""",
    26, """<ol><li>B: your meal: a bean burger, parsnip fries and an avocado chocolate dessert; the delivery was very slow (one hour). Note the student's errors and give feedback after the second round.</li>
<li>C: encourage <i>At first, … but then …</i></li></ol>""")

    # Page 8
    pc = [("A2 Unit 11", "I can check what's done and not done with already, yet and still."), ("A2 Unit 12", "I can write a friendly email with the right phrases."),
          ("A2 Unit 13", "I can explain causes and effects with zero and first conditionals."), ("A2 Unit 14", "I can join ideas with and, but, so, because and although."),
          ("A2 Unit 15", "I can put ideas in order and talk about changing my mind.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    conv = [("And the burgers?", "6"), ("It's unusual. First, the buns are made with cricket flour.", "3"), ("Oh dear. And the delivery?", "8"),
            ("Really? What's it like?", "2"), ("Very slow! When the food arrived, I said, \"At last!\"", "9"), ("Cricket flour? That sounds terrible!", "4"),
            ("Not great. First, they were dry. Then, they were really small.", "7"), ("I thought so too, at first. But then I tried it, and it was OK.", "5")]
    cvl = "".join(f"<li>{A(n, 'min-width:6mm')} {s}</li>" for s, n in conv)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Two friends talk about the burger place. Line 1 is: "I tried that new burger place last weekend." Number the other lines (2–9).</b></p>
<ol style="list-style:none;padding-left:2mm">{cvl}</ol>
<p style="margin-top:2mm"><b>2. A review (50–75 words).</b> Write a review of a restaurant or a takeout meal. Say what you ordered (<i>first, then, finally</i>) and what you thought (<i>at first … but then</i>). Would you go back?</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>1: other orders are possible if they make sense. Next class: the student reads the review aloud; underline the sequencers together.</p>""")

    b.extra("Audio scripts", f"""
{sub("15.1", "Tom and Lucy order takeout (slow and natural)")}
<p style="line-height:1.42">{"<br>".join(f"<b>{NAMES[n]}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("15.2", "Sequencers")}
<p>{" · ".join(S152)}</p>
{sub("15.3", "Sentences with sequencers")}
<p>{" ".join(S153)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 15 - Burgers, fries, shakes")
