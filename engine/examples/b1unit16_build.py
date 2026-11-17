# Speak! Progress B1 - Unit 16 "Comfort food" (all English) - B1 format (2026-11-09)
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Progress"
setup(band="B1 · UNIT 16", audio_json="audio_b1-unit-16.json", img_dir="img")


_r = json.load(open("roteiro.json"))["units"]["b1-unit-16"]
_L = [l.split(": ", 1)[1] for l in _r["16.1 Good for the soul"].split("\n")]
PARAS = _L[1:]
S162 = [x.split(": ", 1)[1] for x in _r["16.2 Repeat: numbers and amounts"].split("\n")]
NUM = {"two thousand eleven": "2011", "two thousand fifteen": "2015"}
for k, v in NUM.items():
    PARAS = [p.replace(k, v) for p in PARAS]


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
    cover = cover_html(T, "LEVEL B1 · UNIT 16", "Comfort food", "Food, feelings and memories · <b>talking about amounts: most of, half of, one in five</b>",
                       [("YOU CAN", "understand an article about research, talk about your comfort food and report survey results"),
                        ("LANGUAGE", "a recipe · flavor · time-consuming · stick to · most of us · a third of · the majority of"),
                        ("PRONUNCIATION", "numbers, fractions and amounts in connected speech")])
    kw = [("a set of instructions for preparing a dish", "a recipe"), ("the taste of food or drink in your mouth", "flavor"),
          ("taking a lot of time", "time-consuming"), ("a choice or variety of different things", "a range"),
          ("to keep doing the same thing and not change", "stick to"), ("to speak too proudly about yourself", "boast"),
          ("to say that someone is responsible for something bad", "blame"), ("to agree that something is true, even if you don't want to", "admit")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:20mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Warm-up: food and feelings", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 35)}<div style="flex:1">
{sub("A", "Discuss with your teacher.", "3 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0"><li>How often do you cook? Why?</li><li>What do you like to eat when you're tired, sad or stressed?</li><li>Is there a dish that reminds you of your childhood?</li></ol></div></div>
{sub("B", "Key words. Write the words from the box next to the definitions.", "4 min")}
<div class="bank">admit · blame · boast · flavor · a range · a recipe · stick to · time-consuming</div>
<div style="font-size:8.6pt">{twocol(kwl, 4)}</div>
{sub("C", "Use three of the key words to talk about your cooking. Example: I tend to stick to the same five recipes.", "1 min")}""",
    30, """<ol><li>A: <i>comfort food</i> = food that makes you feel better, often simple, warm and connected with home and family.</li>
<li>B: <i>flavor</i> is the American spelling (British: <i>flavour</i>). <i>Stick to</i> + noun: <i>stick to the same meals</i>. <i>Blame someone for something</i>; <i>admit (that)…</i>.</li>
<li>C: help with natural sentences: <i>I admit I'm not a great cook. Cooking every day is too time-consuming for me.</i></li></ol>""", cover=cover)

    b.extra("Lesson overview · 60 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Discussion · key words</td><td>1</td></tr>
<tr><td>2 Reading</td><td>12 min</td><td>Article: why does comfort food make us feel better? (real research)</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>8 min</td><td>Quantity expressions: most of, half of, a quarter of, one in five, none of</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Talking about amounts and statistics (study at home)</td><td>4</td></tr>
<tr><td>4 Vocabulary lab + pronunciation</td><td>8 min</td><td>Cooking methods · cooking collocations · numbers and amounts</td><td>5</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Danny's hostel poll · reporting numbers</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Comfort food interview · long turn · talking point</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>4 min</td><td>Can-do · language notes · writing homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY</h4>The Linguahouse lesson uses a 2007 newspaper article about British cooking habits. The data is old, so we wrote an original article on real research about comfort food, read by the Host (track 16.1). Verified facts: in 2011, Jordan Troisi and Shira Gabriel (University at Buffalo) published two experiments in <i>Psychological Science</i>: eating chicken noodle soup made people who saw it as comfort food think of relationship words; writing about a comfort food after writing about a fight with a close person reduced loneliness, but only for people with secure relationships. In 2015, Ong, IJzerman and Leung (<i>Frontiers in Psychology</i>) repeated the second experiment with US adults online, Dutch students (Tilburg University) and Singaporean students (Singapore Management University); the effect was not confirmed overall and seemed to hold only in the American sample. In their pilot study, 37 of 146 Singaporean students (25%) named chicken noodle soup as a comfort food; the typical comfort food was chocolate for Dutch students and noodles for Singaporean students. In the Practice, Danny reports a poll he did with the guests at Mrs. Lima's hostel (fictional numbers). The writing model is Ana's text about Grandma Lourdes's chicken soup.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students say <i>the most of people</i>, <i>the half of the class</i>, <i>most of people</i> and <i>None of them didn't like it</i>. In vocabulary, they confuse <i>recipe</i> and <i>receipt</i>, say <i>do dinner</i> (make dinner) and <i>I pretend to cook more</i> (I intend / plan to).</div>
<div class="box"><h4>AUDIO</h4>Track 16.1 Good for the soul (natural and slow) · Track 16.2 Repeat: numbers and amounts</div>""")

    # Page 2 - Reading
    bf = [("Comfort food is usually something new and exotic.", "F"), ("The 2011 study was done in the United States.", "T"),
          ("Comfort food made everybody in the study feel less lonely.", "F (only people with secure relationships)"), ("The 2015 study found the same effect in all three groups.", "F (only in the US)")]
    bfl = [f'<li value="{i+1}">{s} {A(a, "min-width:9mm")}</li>' for i, (s, a) in enumerate(bf)]
    qs = [("Who were Troisi and Gabriel?", "psychologists at the University at Buffalo"), ("What did some participants eat in the first experiment?", "chicken noodle soup"),
          ("What did all participants write about first in the second experiment?", "a fight with someone close"), ("Where were the participants of the 2015 study from?", "the US, the Netherlands, Singapore"),
          ("What was the most common comfort food for Dutch students?", "chocolate")]
    qsl = [f'<li value="{i+1}">{q} {A(a, "min-width:20mm")}</li>' for i, (q, a) in enumerate(qs)]
    art = "".join(f'<p style="margin:0 0 .8mm"><b style="color:#176074">{i+1}</b> {p}</p>' for i, p in enumerate(PARAS))
    b.page(f"""{sec(2, "Reading: good for the soul?", "12 min")}
{sub("A", "Before you read. True or false? Guess. Then read the article and check.", "3 min")}
<div style="font-size:8.5pt">{twocol(bfl, 2)}</div>
<div class="box" style="margin:.5mm 0 0;font-size:8pt;line-height:1.33;column-count:2;column-gap:4mm"><b style="font-size:9.5pt">Good for the soul?</b><br>{art}</div>
<div style="display:flex;gap:3mm;align-items:center;margin-top:1mm"><div style="flex:1">{audiocard(["16.1 · NATURAL", "16.1 · SLOW"])}</div>{img('B', 36, 20)}</div>
{sub("B", "Read again and answer the questions.", "4 min")}
<div style="font-size:8.5pt">{twocol(qsl, 3)}</div>
{sub("C", "Think about it. Discuss with your teacher.", "4 min")}
<ol style="line-height:1.4;font-size:8.7pt;margin:0"><li>Why do you think chicken noodle soup didn't work for the students in Singapore? {R("It wasn't their comfort food; comfort food depends on culture and personal memories.") if T else ""}</li>
<li>"Comfort food is personal." Do you agree? What memories come with your comfort food?</li></ol>
<div class="box sand" style="margin-top:1mm"><h4>NOTICE: USEFUL CHUNKS</h4><i>reach for · just like Grandma's · decided to find out · remind us of · close to them · afterward · Does this work everywhere? · One reason might be…</i></div>""",
    25, """<ol><li>A: let the student guess first; the reading then has a purpose. They can read and listen (16.1) at the same time.</li>
<li>The article is based on real research (see the story box). Point out that science can change: a famous result was not confirmed in other countries.</li></ol>""")

    # Page 3 - Language focus
    fs = [("___ us reach for the same kind of food.", "Most of"), ("___ the participants ate chicken noodle soup.", "Some of"),
          ("___ the participants first wrote about a fight.", "All of"), ("Then ___ them wrote about eating a comfort food.", "half of"),
          ("Only about ___ the Singaporean students said yes.", "a quarter of")]
    fsl = "".join(f"<li><i>{s.replace('___', A(a, 'min-width:16mm'))}</i></li>" for s, a in fs)
    b.page(f"""{sec(3, "Language focus: talking about amounts", "8 min")}
{sub("A", "Complete the sentences from the article. Then check in the text.", "2 min")}
<ol style="line-height:1.85;font-size:8.9pt;margin:0">{fsl}</ol>
{sub("B", "Complete the rules. Choose.", "3 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0"><li><i>Most people like chocolate</i> is about {ch(["people in general", "a specific group"], "people in general")}.</li>
<li>Before <i>the, my, us, them</i>, we use {ch(["of", "no word"], "of")}: <i>most of the guests, half of them</i>.</li>
<li>We say {ch(["the most of people", "most people"], "most people")} and {ch(["the half of the class", "half of the class"], "half of the class")}.</li>
<li>After <i>half of / most of</i>, the verb agrees with {ch(["the noun", "half / most"], "the noun")}: <i>Half of the students are…</i></li>
<li><i>None of</i> takes a {ch(["positive", "negative"], "positive")} verb: <i>None of them liked it.</i></li></ol>
{sub("C", "Correct or incorrect? Choose.", "3 min")}
<ol style="line-height:1.6;font-size:8.9pt;margin:0"><li>The most of my friends cook at home. {ch(["correct", "incorrect"], "incorrect")} {R("→ Most of my friends") if T else ""}</li><li>One in five people never cook. {ch(["correct", "incorrect"], "correct")}</li><li>None of the guests didn't want dessert. {ch(["correct", "incorrect"], "incorrect")} {R("→ None of the guests wanted dessert.") if T else ""}</li><li>About two-thirds of the class eat out on Fridays. {ch(["correct", "incorrect"], "correct")}</li></ol>
<div class="box sand"><h4>RULE</h4>In general: <b>most / some / all / no + noun</b> (<i>Most people…</i>). A specific group: <b>most of / some of / all of / none of / half of + the / my / us / them</b>. Numbers: <b>a quarter of, a third of, two-thirds of, one in five, the majority of, 60 percent of</b>. Never <i>the most of</i> or <i>the half of</i>. More on the next page: <b>Grammar reference</b>.</div>""",
    27, """<ol><li>A: ask why there is <i>of</i> in every sentence (a specific group: <i>us, the participants, them</i>).</li>
<li>B: contrast <i>Most people cook</i> (in general) with <i>Most of my friends cook</i> (a group I know).</li>
<li>C: <i>the majority of</i> is more formal, typical of reports and the news.</li></ol>""")

    grammar_ref.quantity_expressions(b)

    # Page 5 - Vocabulary lab
    cm = [("pasta, eggs, potatoes", "boil"), ("bread, cakes, cookies", "bake"), ("a whole chicken, potatoes in the oven", "roast"),
          ("steak, fish, corn on a barbecue", "grill"), ("vegetables and noodles, quickly in a wok", "stir-fry"), ("broccoli or dumplings over hot water", "steam")]
    cml = [f'<li value="{i+1}">{f} {A(m, "min-width:16mm")}</li>' for i, (f, m) in enumerate(cm)]
    co = [(["stick to", "stick with the"], "stick to", "I always", " the same recipes."), (["give", "make"], "give", "Add lime to", " the dish a twist."),
          (["wide", "large"], "wide", "The menu offers a", " range of dishes."), (["cook", "do"], "cook", "Let's", " dinner together tonight.")]
    cos = " &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {p} {ch(o, a)}{e}" for i, (o, a, p, e) in enumerate(co))
    b.page(f"""{sec(4, "Vocabulary lab: cooking", "4 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "How do we usually cook these foods? Write a verb from the box.", "2 min")}
<div class="bank">bake · boil · grill · roast · steam · stir-fry</div></div>{img('D', 30, 20)}</div>
<div style="font-size:8.5pt">{twocol(cml, 3)}</div>
{sub("B", "Choose the correct word.", "2 min")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.7">{cos}</p>
<div class="box sand"><h4>WATCH OUT: FALSE FRIENDS AND WORD CHOICE</h4>
<table style="margin:0;font-size:8.3pt"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>Can you send me the receipt of the cake?</td><td><b>Can you send me the recipe for the cake?</b></td><td>a <i>recipe</i> tells you how to cook; a <i>receipt</i> is the paper you get when you pay.</td></tr>
<tr><td>I'll do dinner tonight.</td><td><b>I'll make / cook dinner tonight.</b></td><td>we <i>make</i> or <i>cook</i> a meal.</td></tr>
<tr><td>I pretend to cook more this year.</td><td><b>I plan / intend to cook more this year.</b></td><td><i>pretend</i> = act as if something is true when it isn't.</td></tr>
<tr><td>It's a delicious food.</td><td><b>It's delicious. / It's a delicious dish.</b></td><td><i>food</i> is usually uncountable; use <i>a dish</i> or <i>a meal</i>.</td></tr></table></div>
{sec(5, "Pronunciation lab: numbers and amounts", "4 min")}
<p class="small" style="margin:.3mm 0">In amounts, <i>of</i> is weak and joins the word before: <i>most of</i> /ˈmoʊstəv/, <i>half of</i> /ˈhæfəv/, <i>a third of</i> /əˈθɜrdəv/. The stress is on the number and the noun: <i>about a <b>THIRD</b> of us <b>COOK</b></i>.</p>
{audiocard(["16.2"])}
{sub("A", "Listen and repeat. Then say three true sentences about your family or friends with these expressions.", "4 min", "16.2")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.55">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S162))}</p>""",
    25, """<ol><li>A: some foods can be cooked in different ways (<i>boil / roast potatoes</i>); accept logical answers. <i>Fry</i> = in hot oil; <i>stir-fry</i> = fry quickly while stirring.</li>
<li>B: <i>give a dish a twist</i> = change it a little, for example with a new ingredient.</li></ol>""")

    # Page 6 - Practice
    pc = [(["Most", "The most"], "Most"), (["Half", "The half"], "Half"), (["A quarter of", "A quarter"], "A quarter of"), (["guest", "guests"], "guests"),
          (["None", "No one"], "None"), (["them", "they"], "them"), (["is", "are"], "is")]
    p = [ch(o, a) for o, a in pc]
    rn = [("12 out of 24 students eat breakfast.", "Half of the students eat breakfast."), ("8 out of 24 students cook every day.", "A third of the students cook every day."),
          ("18 out of 24 students like spicy food.", "Three-quarters of the students like spicy food."), ("0 out of 24 students eat fish.", "None of the students eat fish."),
          ("20% of people never cook.", "One in five people never cook.")]
    rnl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rn)
    b.page(f"""{sec(6, "Practice", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Danny asked the 20 guests at Mrs. Lima's hostel about comfort food. Read his post and choose the correct words.", "4 min")}</div>{img('C', 30, 20)}</div>
<div class="box" style="line-height:1.95;font-size:9pt"><b>Gap Year Diaries · Our hostel poll</b><br>This week I asked the twenty guests at our hostel one question: what's your comfort food? {p[0]} of them answered in seconds! {p[1]} of the guests chose something sweet, usually chocolate or ice cream. {p[2]} them chose soup, and one in five {p[3]} said pasta. Only one person said salad: Bruno, of course. {p[4]} of the others understood that answer! The best part? Almost all of {p[5]} named a dish that someone in their family used to make. And three guests chose Mrs. Lima's chicken soup. Half of the pot {p[6]} already gone, so come early tonight!</div>
{sub("B", "Report the numbers. Use half of, a third of, three-quarters of, none of or one in five.", "4 min")}
<ol style="line-height:1.55;font-size:8.8pt;margin:0">{rnl}</ol>""",
    24, """<ol><li>A: in the last gap, <i>half of the pot</i> takes a singular verb because <i>pot</i> is singular. Ask: <i>How many guests chose something sweet? (10) Soup? (5) Pasta? (4)</i></li>
<li>B: accept <i>50 percent of, the majority of</i> where correct. Check that there is no <i>the</i> before <i>half</i>.</li></ol>""")

    # Page 7 - Speaking
    iq = ["What's your comfort food? Who used to make it?", "When do you eat it: when you're sad, tired, sick or happy?", "Can you cook it? Is the recipe time-consuming?",
          "Do you stick to the same recipes, or do you like to experiment?", "What's a comfort food from another country that you love?"]
    iql = "".join(f"<li>{x}</li>" for x in iq)
    b.page(f"""{sec(7, "Speaking: just like Grandma's", "12 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>memories</th><th>describing a dish</th><th>habits</th><th>reporting</th></tr>
<tr><td><i>It reminds me of… · My grandma used to make… · Whenever I…</i></td><td><i>It's made with… · It's a kind of… · It has a strong / mild flavor.</i></td><td><i>I tend to… · I always stick to… · I can't resist…</i></td><td><i>Most of my friends… · About half of… · None of us…</i></td></tr></table></div>
{sub("A", "Comfort food interview. Ask your teacher the questions. Then answer them yourself.", "4 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0">{iql}</ol>
{sub("B", "Long turn. Prepare for one minute, then talk for two minutes. Imagine you are explaining your comfort food to a friend from another country.", "5 min")}
<ul style="line-height:1.45;font-size:8.9pt;margin:0"><li>what it is and what it's made with</li><li>how it's cooked (boiled, baked, fried…)</li><li>who made it for you and when</li><li>why it makes you feel better</li></ul>
{sub("C", "Talking point. Discuss with your teacher.", "3 min")}
<ol style="line-height:1.5;font-size:8.9pt;margin:0"><li>How important is traditional food and cooking in your country? Is fast food becoming more popular? Why?</li><li>Think about your family and friends. How many of them cook every day? Use <i>most of, half of, a few of, none of</i>.</li></ol>""",
    30, """<ol><li>A: answer first to model language from the box (<i>It reminds me of…, My grandma used to make…</i>).</li>
<li>B: this is useful when students travel or meet foreigners: they need to explain dishes that have no English name. Don't interrupt; note mistakes for the error log (page 8), especially <i>the most of</i> and <i>receipt</i>.</li></ol>""")

    # Page 8 - Wrap-up
    cd = ["I can understand an article about research on food and feelings.", "I can talk about amounts (most of, half of, one in five…).",
          "I can describe my comfort food and the memories that come with it."]
    cdr = "".join(f"<tr><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for s in cd)
    b.page(f"""{sec(8, "Wrap-up and homework", "4 min")}
{sub("A", "Can-do check", "1 min")}
<table class="ck" style="font-size:8.6pt"><tr><th>In English…</th><th style="width:16mm">Easy!</th><th style="width:16mm">Sometimes</th><th style="width:16mm">Not yet</th></tr>{cdr}</table>
{sub("B", "My language notes. Write three corrections from today's class.", "2 min")}
<div style="display:flex;gap:5mm;font-size:8.6pt"><div style="flex:1"><b>I said…</b>{lines(3)}</div><div style="flex:1"><b>Better:</b>{lines(3)}</div></div>
{sub("C", "Homework: writing (100–150 words)", "1 min")}
<p style="margin:.3mm 0"><b>My comfort food.</b> Write about your comfort food: what it is, who made it for you, and why it makes you feel better. Read Ana's text first.</p>
<div class="box" style="font-size:8.6pt;line-height:1.4;margin:.5mm 0"><b>Ana · Grandma's chicken soup</b><br><i>My comfort food is my grandmother's chicken soup. Grandma Lourdes made it every Sunday when I was a child, with chicken, rice, carrots and a lot of parsley. Whenever I was sick, she brought me a big bowl in bed. Now I work twelve-hour shifts at the hospital, and when I get home late and tired, I don't want anything fancy. I want that soup. The recipe is simple, and it isn't time-consuming: it takes about forty minutes. Most of my friends prefer chocolate or pizza on a bad day, and my husband says I always stick to the same three dishes. He's right! Once I tried to give the soup a twist with ginger, but my son said Grandma's version was better. I have to admit he was right.</i></div>
<p class="small" style="margin:.3mm 0">Checklist: ☐ what it is and how it's made &nbsp;☐ a memory &nbsp;☐ when you eat it now &nbsp;☐ two key words from this unit &nbsp;☐ 100–150 words</p>
{lines(5)}""",
    30, """<ol><li>B (error log): during the lesson, note 3–5 real mistakes. Here, the student writes what they said and the better version; guide them to self-correct first.</li>
<li>C: check the key words (<i>recipe, flavor, stick to, time-consuming, admit</i>) and <i>used to / would</i> for childhood memories.</li></ol>""")

    b.extra("Audio script", f"""
{sub("16.1", "Good for the soul (natural and slow)")}
<p style="margin:.5mm 0"><b>{_L[0]}</b></p>
<div style="line-height:1.3;font-size:8.6pt">{"".join(f"<p style='margin:.5mm 0'>{x}</p>" for x in PARAS)}</div>
{sub("16.2", "Repeat: numbers and amounts")}
<p>{" · ".join(S162)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 16 - Comfort food")
