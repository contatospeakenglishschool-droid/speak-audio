# Speak! Progress B1 - Unit 16 "Comfort food" (all English) - lean B1 format (rebuilt 2026-11-19)
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

    # 1 Warm-up
    cover = cover_html(T, "LEVEL B1 · UNIT 16", "Comfort food", "Food, feelings and memories · <b>talking about amounts: most of, half of, one in five</b>",
                       [("YOU CAN", "understand an article about research, talk about your comfort food and report survey results"),
                        ("LANGUAGE", "a recipe · flavor · time-consuming · stick to · most of us · a third of · the majority of"),
                        ("PRONUNCIATION", "numbers, fractions and amounts in connected speech")])
    kw = [("a set of instructions for preparing a dish", "a recipe"), ("the taste of food or drink in your mouth", "flavor"),
          ("taking a lot of time", "time-consuming"), ("to keep doing the same thing and not change", "stick to"),
          ("to say that someone is responsible for something bad", "blame"), ("to agree that something is true, even if you don't want to", "admit")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:20mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Warm-up: food and feelings", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["How often do you cook? Why?", "What do you like to eat when you're tired, sad or stressed?", "Is there a dish that reminds you of your childhood?"], "START TALKING")}</div></div>
{sub("A", "Key words. Write the words from the box next to the definitions.", "3 min")}
<div class="bank">admit · blame · flavor · a recipe · stick to · time-consuming</div>
<div style="font-size:8.8pt">{twocol(kwl, 3)}</div>
{talk(["Do you stick to the same recipes, or do you experiment?", "What's a time-consuming dish you love? Who makes it?"], "USE THE WORDS")}""",
    26, """<ol><li>Top box: <i>comfort food</i> = food that makes you feel better, often simple, warm and connected with home and family.</li>
<li>A: <i>flavor</i> is American spelling (British: <i>flavour</i>). <i>Stick to</i> + noun; <i>blame someone for something</i>.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Article: why comfort food makes us feel better (real research) · true or false · Talk about it", "Talking about amounts and statistics",
                      "Complete from the article · choose the rule · Use it (oral)", "Functional language · numbers and amounts (16.2) · comfort food interview",
                      "Danny's hostel poll · cooking methods · word choice · writing", "Reading"),
        "The Linguahouse lesson uses a 2007 newspaper article about British cooking habits. The data is old, so we wrote an original article on real research about comfort food, read by the Host (track 16.1). Verified facts: in 2011, Jordan Troisi and Shira Gabriel (University at Buffalo) published two experiments in <i>Psychological Science</i>: eating chicken noodle soup made people who saw it as comfort food think of relationship words; writing about a comfort food after writing about a fight with a close person reduced loneliness, but only for people with secure relationships. In 2015, Ong, IJzerman and Leung (<i>Frontiers in Psychology</i>) repeated the second experiment with US adults online, Dutch students (Tilburg University) and Singaporean students (Singapore Management University); the effect was not confirmed overall and seemed to hold only in the American sample. In their pilot study, 37 of 146 Singaporean students (25%) named chicken noodle soup as a comfort food; the typical comfort food was chocolate for Dutch students and noodles for Singaporean students. In the homework, Danny reports a poll he did with the guests at Mrs. Lima's hostel (fictional numbers).", "Students say <i>the most of people</i>, <i>the half of the class</i>, <i>most of people</i> and <i>None of them didn't like it</i>. In vocabulary, they confuse <i>recipe</i> and <i>receipt</i>, say <i>do dinner</i> (make dinner) and <i>I pretend to cook more</i> (I intend / plan to).",
        "Track 16.1 Good for the soul (natural and slow) · Track 16.2 Repeat: numbers and amounts"))

    # 2 Reading
    bf = [("Comfort food is usually something new and exotic.", "F"), ("The 2011 study was done in the United States.", "T"),
          ("Comfort food made everybody in the study feel less lonely.", "F (only people with secure relationships)"), ("The 2015 study found the same effect in all three groups.", "F (only in the US)")]
    bfl = [f'<li value="{i+1}">{s} {A(a, "min-width:9mm")}</li>' for i, (s, a) in enumerate(bf)]
    art = "".join(f'<p style="margin:0 0 .8mm"><b style="color:#176074">{i+1}</b> {p}</p>' for i, p in enumerate(PARAS))
    b.page(f"""{sec(2, "Reading: good for the soul?", "12 min")}
{sub("A", "Before you read. True or false? Guess. Then read the article and check.", "4 min")}
<div style="font-size:8.4pt">{twocol(bfl, 2)}</div>
<div class="box" style="margin:.5mm 0 0;font-size:7.9pt;line-height:1.32;column-count:2;column-gap:4mm"><b style="font-size:9.5pt">Good for the soul?</b><br>{art}</div>
<div style="display:flex;gap:3mm;align-items:center;margin-top:1mm"><div style="flex:1">{audiocard(["16.1 · NATURAL", "16.1 · SLOW"])}</div>{img('B', 36, 20)}</div>
{talk(["Why do you think chicken noodle soup didn't work for the students in Singapore?", "&ldquo;Comfort food is personal.&rdquo; Do you agree? What memories come with your comfort food?", "What's a comfort food from another country that you love?"])}""",
    26, """<ol><li>A: 6 minutes. Let the student guess first. They can read and listen (16.1). The article is based on real research (see the story box).</li>
<li>Talk about it: 6 minutes. 1: it wasn't their comfort food; comfort food depends on culture and personal memories. Science can change: a famous result was not confirmed in other countries.</li></ol>""")

    # 3 Grammar reference
    lean.grammar_in_class(b, grammar_ref.quantity_expressions)

    # 4 Practice
    fs = [("___ us reach for the same kind of food.", "Most of"), ("___ the participants ate chicken noodle soup.", "Some of"),
          ("Then ___ them wrote about eating a comfort food.", "half of"), ("Only about ___ the Singaporean students said yes.", "a quarter of")]
    fsl = "".join(f"<li><i>{s.replace('___', A(a, 'min-width:16mm'))}</i></li>" for s, a in fs)
    use = ["How many of your friends cook every day? Use <i>most of, half of, a few of, none of</i>.", "What do most people in your city eat for breakfast?", "Think of your family: how many of them like spicy food?",
           "Say a number (<i>8 out of 24</i>); your teacher answers with <i>a third of…</i> Then change roles.", "What do the majority of people in Brazil do on Sundays?"]
    b.page(f"""{sec(4, "Practice: talking about amounts", "10 min")}
{sub("A", "Complete the sentences from the article.", "2 min")}
<ol style="line-height:1.85;font-size:8.9pt;margin:0">{fsl}</ol>
{sub("B", "Choose.", "2 min")}
<p style="margin:.3mm 0;font-size:8.9pt;line-height:1.7">{ch(["The most of", "Most of"], "Most of")} my friends cook. &nbsp;·&nbsp; {ch(["Half", "The half"], "Half")} of the class was late. &nbsp;·&nbsp; None of them {ch(["liked", "didn't like"], "liked")} it.</p>
<div class="box sand"><h4>RULE</h4>In general: <b>most / some / all + noun</b> (<i>Most people…</i>). A specific group: <b>most of / some of / half of / none of + the / my / us / them</b>. Numbers: <b>a quarter of, a third of, one in five, the majority of</b>. Never <i>the most of</i> or <i>the half of</i>. See the <b>Grammar reference</b> on page 3.</div>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    24, """<ol><li>A–B: 4 minutes. Ask why there is <i>of</i> in every sentence in A (a specific group).</li>
<li>Use it: 6 minutes, all oral. <i>The majority of</i> is more formal, typical of reports and the news.</li></ol>""")

    # 5 Speaking
    iq = ["What's your comfort food? Who used to make it?", "When do you eat it: when you're sad, tired, sick or happy?", "Can you cook it? Is the recipe time-consuming?",
          "Do you stick to the same recipes, or do you like to experiment?", "Imagine you're explaining your comfort food to a friend from another country: what's it made with, and how is it cooked?"]
    iql = "".join(f"<li>{x}</li>" for x in iq)
    b.page(f"""{sec(5, "Speaking: just like Grandma's", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>memories</th><th>describing a dish</th><th>habits</th><th>reporting</th></tr>
<tr><td><i>It reminds me of… · My grandma used to make… · Whenever I…</i></td><td><i>It's made with… · It's a kind of… · It has a strong / mild flavor.</i></td><td><i>I tend to… · I always stick to… · I can't resist…</i></td><td><i>Most of my friends… · About half of… · None of us…</i></td></tr></table></div>
{audiocard(["16.2"])}
{sub("A", "Numbers and amounts. Listen and repeat: most of /ˈmoʊstəv/ · half of /ˈhæfəv/ · about a THIRD of us COOK.", "4 min", "16.2")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.55">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S162))}</p>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("B", "Comfort food interview. Ask your teacher the questions. Then answer them yourself.", "10 min")}
<ol style="line-height:1.4;font-size:8.8pt;margin:0">{iql}</ol></div>{img('D', 28, 28)}</div>
{talk(["How important is traditional food and cooking in your country? Is fast food becoming more popular?", "Think about your family and friends. How many of them cook every day?"])}""",
    28, """<ol><li>B: answer first to model language from the box. Question 5 is useful when students travel: they need to explain dishes that have no English name.</li>
<li>Last 3 minutes: wrap-up (two corrections and <i>Can you talk about amounts and your comfort food?</i>).</li></ol>""")

    # H Homework
    pc = [(["Most", "The most"], "Most"), (["Half", "The half"], "Half"), (["A quarter of", "A quarter"], "A quarter of"), (["guest", "guests"], "guests"), (["None", "No one"], "None")]
    p = [ch(o, a) for o, a in pc]
    cm = [("pasta, eggs, potatoes", "boil"), ("bread, cakes, cookies", "bake"), ("vegetables and noodles, quickly in a wok", "stir-fry")]
    cml = "".join(f"<li>{f} {A(m, 'min-width:16mm')}</li>" for f, m in cm)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Danny asked the 20 guests at Mrs. Lima's hostel about comfort food. Choose the correct words.", "")}</div>{img('C', 28, 18)}</div>
<div class="box" style="line-height:1.8;font-size:8.8pt;margin:.5mm 0"><b>Gap Year Diaries · Our hostel poll</b><br>{p[0]} of them answered in seconds! {p[1]} of the guests chose something sweet, usually chocolate or ice cream. {p[2]} them chose soup, and one in five {p[3]} said pasta. Only one person said salad: Bruno, of course. {p[4]} of the others understood that answer! And three guests chose Mrs. Lima's chicken soup.</div>
{sub("B", "How do we usually cook these foods? Write bake, boil or stir-fry.", "")}
<ol style="line-height:1.5;font-size:8.6pt;margin:0">{cml}</ol>
{lean.watch_out([("Can you send me the receipt of the cake?", "Can you send me the recipe for the cake?", "a <i>receipt</i> is the paper you get when you pay."), ("I'll do dinner tonight.", "I'll make / cook dinner tonight.", "we <i>make</i> or <i>cook</i> a meal."), ("I pretend to cook more this year.", "I plan / intend to cook more this year.", "<i>pretend</i> = act as if something is true.")])}
{lean.writing_task(sub, "My comfort food: write about your comfort food, who made it for you, and why it makes you feel better.", "My comfort food is… My grandmother used to make it… Most of my friends prefer…", ["what it is and how it's made", "a memory", "two amount expressions", "100–150 words"], "I can talk about amounts and describe my comfort food.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class (10 guests chose something sweet, 5 soup, 4 pasta). When you correct the writing, check <i>most of</i> / <i>most</i> and the key words.</p>""")

    b.extra("Audio script", f"""
{sub("16.1", "Good for the soul (natural and slow)")}
<p style="margin:.5mm 0"><b>{_L[0]}</b></p>
<div style="line-height:1.3;font-size:8.6pt">{"".join(f"<p style='margin:.5mm 0'>{x}</p>" for x in PARAS)}</div>
{sub("16.2", "Repeat: numbers and amounts")}
<p>{" · ".join(S162)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 16 - Comfort food")
