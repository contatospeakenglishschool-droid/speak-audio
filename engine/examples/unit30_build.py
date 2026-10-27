# Speak! Essentials A1 - Unit 30 "Do we have any onions?" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
from speak_engine import *
setup(band="A1 · UNIT 30", audio_json="audio_a1-unit-30.json", img_dir="img")

PHOTOS = [("A", "an apple", "apple"), ("B", "bread", "bread"), ("C", "cheese", "cheese"), ("D", "an egg", "egg"),
          ("E", "garlic", "garlic"), ("F", "lettuce", "lettuce"), ("G", "an onion", "onion"), ("H", "a potato", "potato")]

_r = json.load(open("roteiro.json"))["units"]["a1-unit-30"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["30.1 Kitchen"].split("\n")]
S302 = [x.split(": ", 1)[1] for x in _r["30.2 Repeat words"].split("\n")]
S303 = [x.split(": ", 1)[1] for x in _r["30.3 Repeat sentences"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LEVEL A1 · UNIT 30", "Do we have any onions?", "Food · <b>countable and uncountable nouns · some / any / a lot of</b>",
                       [("YOU CAN", "talk about the food in your kitchen and make a shopping list"),
                        ("LANGUAGE", "We have some beans. · We don't have any garlic. · Do we have any cheese?"),
                        ("PRONUNCIATION", "an apple /ənˈæpəl/ · some /səm/ · a lot of /əˈlɑtəv/")])
    b.page(f"""{sec(1, "Warm-up: food", "8 min")}
{sub("A", "Look at the photos. Write the word under each photo.", "3 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(w.replace(" ", "&nbsp;") for _, w, _ in PHOTOS)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Talk about it.", "5 min")}
<ol><li>Which words have <i>a</i> or <i>an</i>? Which words don't? Why? {R("We can count apples, eggs, onions and potatoes; we can't count bread, cheese and garlic. Lettuce can be both: some lettuce / a lettuce.")}</li>
<li>Which of these things did you buy the last time you went to the supermarket?</li><li>Do you make a shopping list?</li></ol>""",
    26, """<ol><li>A: drill the /e/ sound in <b>bread</b>, <b>egg</b> and <b>lettuce</b>. <b>lettuce</b> /ˈletɪs/: the second syllable is short.</li>
<li>B: don't explain the grammar yet; let the student notice that some words have <i>a/an</i> and some don't. <i>a lettuce</i> = one head of lettuce.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>8 food words with photos · a / an</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Ana and Marcos plan Sunday lunch and make a shopping list</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Countable and uncountable nouns · some / any · a lot of</td><td>3</td></tr>
<tr><td>4 Pronunciation lab</td><td>5 min</td><td>a / an / some + food · weak forms in sentences</td><td>4</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Kate's bakery kitchen · correct the mistakes</td><td>5</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Barbecue information gap · your kitchen</td><td>6</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework (packaging words)</td><td>7</td></tr></table>
<div class="box"><h4>HOW THIS GUIDE WORKS</h4>Every page looks like the Student Book page with the same number. Your notes are in the <b>yellow box</b>.
<span class="red">Answers in red</span> are not in the Student Book. The <span class="time">5 min</span> chips show the time for each activity. Audio scripts are on the last page.</div>
<div class="box sand"><h4>THE STORY CONTINUES</h4>It's Saturday morning in São Paulo. Ana's parents, Carlos and Rosa, are coming for lunch on Sunday. Rosa loves lasagna, but there isn't any pasta and Marcos thinks it's a lot of work. They check the kitchen, make a shopping list (garlic, tomatoes, lettuce, cheese, coffee) and decide on a real Brazilian Sunday lunch: chicken with rice and beans, a salad, and cheese bread with coffee. In Chicago, Kate checks her bakery kitchen before Christmas (page 5).</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Some nouns are countable in Portuguese but uncountable in English: <i>a bread, breads</i> ✗ → <b>some bread / a loaf of bread</b>; <i>informations, advices</i> ✗ → <b>information, advice</b>. Students also use <i>some</i> in negatives (<i>We don't have some cheese</i> ✗ → <b>any</b>) and forget <i>a</i> in <b>a lot of</b>.</div>
<div class="box"><h4>AUDIO</h4>Track 30.1 In the kitchen (slow and natural) · Track 30.2 Food words · Track 30.3 Sentences</div>""")

    # Page 2
    opts = [(["a lot of", "some", "any"], "any", "No, we don't have", "pasta."), (["a lot of", "any", "an"], "a lot of", "But we have", "rice and some beans."),
            (["any", "some", "a"], "some", "Yes, there's", "chicken in the freezer."), (["an", "some", "any"], "an", "We have", "onion, but we don't have any garlic."),
            (["any", "a", "some"], "some", "We need", "tomatoes and a lettuce for the salad."), (["some", "a", "any"], "any", "No, there isn't", "cheese, so let's buy some."),
            (["lots", "a lot of", "any"], "a lot of", "We drink", "coffee in this house.")]
    ol = "".join(f"<li>{a} {ch(o, r)} {c}</li>" for o, r, a, c in opts)
    shop = ["garlic", "tomatoes", "a lettuce", "cheese", "coffee"]
    b.page(f"""{sec(2, "Listening: Sunday lunch", "10 min")}
<p>It's Saturday morning in São Paulo. Ana's parents are coming for lunch tomorrow. Ana and Marcos are checking the kitchen before they go to the supermarket.</p>
{audiocard(["30.1 · SLOW", "30.1 · NATURAL"])}
{sub("A", "Listen. What are they going to cook for lunch tomorrow?", "2 min", "30.1 · SLOW")}
<p>a) lasagna &nbsp;&nbsp; b) chicken with rice and beans &nbsp;&nbsp; c) pizza &nbsp;&nbsp; {R("→ b)")}</p>
{sub("B", "Listen again and choose the words you hear.", "5 min", "30.1 · NATURAL")}
<ol>{ol}</ol>
{sub("C", "Write their shopping list. What do they need to buy?", "3 min")}
<div class="two"><div>{"".join(f'<div class="wline">{i+1}. {R(s)}</div>' for i, s in enumerate(shop[:3]))}</div><div>{"".join(f'<div class="wline">{i+4}. {R(s)}</div>' for i, s in enumerate(shop[3:]))}</div></div>""",
    26, """<ol><li>A: <b>slow</b> version. Then ask: <i>Why not lasagna?</i> (no pasta, and it's a lot of work).</li>
<li>B–C: <b>natural</b> version. Ask what a <i>real Brazilian Sunday lunch</i> is in the student's family. <b>freezer</b>: the very cold part of the fridge.</li></ol>""")

    # Page 3
    nouns = ["beans", "cheese", "coffee", "garlic", "meat", "oranges", "pasta", "rice", "tomatoes", "water"]
    cnt = ["beans", "oranges", "tomatoes"]
    b.page(f"""{sec(3, "Language focus: some, any, a lot of", "10 min")}
<div class="box" style="margin-top:0"><h4>COUNTABLE AND UNCOUNTABLE NOUNS</h4><b>Countable</b> nouns have a singular and a plural form: an onion → three onions, a potato → potatoes. Singular countable nouns need <b>a / an</b>.<br>
<b>Uncountable</b> nouns have no plural and no <i>a / an</i>: bread, cheese, rice, coffee. ✗ <i>a rice</i> ✗ <i>breads</i></div>
{sub("A", "Countable (C) or uncountable (U)? Write C or U.", "3 min")}
<div class="bank" style="background:#fff;font-weight:600">{" &nbsp; ".join(f"{n} {A('C' if n in cnt else 'U', 'min-width:8mm')}" for n in nouns)}</div>
{sub("B", "Read the sentences from the conversation. Then choose the correct option.", "4 min")}
<table style="table-layout:fixed;font-size:9.3pt"><tr><th style="width:30mm"></th><th>plural countable</th><th>uncountable</th></tr>
<tr><td><b>+</b></td><td>We have <b>some</b> beans.</td><td>There's <b>some</b> chicken in the freezer.</td></tr>
<tr><td><b>–</b></td><td>We don't have <b>any</b> eggs.</td><td>We don't have <b>any</b> pasta.</td></tr>
<tr><td><b>?</b></td><td>Do we have <b>any</b> onions?</td><td>Do we have <b>any</b> cheese?</td></tr></table>
<ol><li>We use <i>some</i> in {ch(["positive", "negative"], "positive")} sentences.</li>
<li>We use <i>any</i> in {ch(["positive", "negative"], "negative")} sentences and in questions.</li>
<li>We use <i>a lot of</i> with {ch(["only plural nouns", "plural and uncountable nouns"], "plural and uncountable nouns")}.</li></ol>
<div class="box sand"><h4>A LOT OF / LOTS OF</h4>For a big amount: We have <b>a lot of</b> rice. · We drink <b>lots of</b> coffee. · There are <b>a lot of</b> eggs.<br>Don't forget the <b>a</b> in <i>a lot of</i>, and no <b>a</b> in <i>lots of</i>.</div>""",
    26, """<ol><li>A: some words are countable in Portuguese but not in English: <i>pasta, bread, information</i>. Plural form = countable.</li>
<li>B: offers and requests often use <i>some</i> in questions (<i>Would you like some coffee?</i>), but keep the simple rule for now.</li></ol>""")

    # Page 4
    b.page(f"""{sub("C", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>I need a bread.</td><td><b>I need some bread.</b></td><td><i>bread</i> is uncountable.</td></tr>
<tr><td>We don't have some cheese.</td><td><b>We don't have any cheese.</b></td><td>Negative: <i>any</i>.</td></tr>
<tr><td>We have lot of apples.</td><td><b>We have a lot of apples.</b></td><td><i>a lot of</i> / <i>lots of</i>.</td></tr>
<tr><td>I need potato.</td><td><b>I need a potato.</b></td><td>Singular countable: <i>a / an</i>.</td></tr>
<tr><td>Do you have a onion?</td><td><b>Do you have an onion?</b></td><td><i>an</i> before a vowel sound.</td></tr>
<tr><td>Can you give me some informations?</td><td><b>Can you give me some information?</b></td><td><i>information</i> is uncountable.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "5 min")}
{audiocard(["30.2", "30.3"])}
{sub("A", "Food words. Listen and repeat.", "2 min", "30.2")}
<table style="table-layout:fixed;margin-top:0"><tr>{"".join(f"<td style='text-align:center'><b>{w}</b></td>" for w in S302)}</tr></table>
<div class="box" style="margin-top:1mm"><h4>LINKING</h4><b>an apple</b> sounds like one word: /ənˈæpəl/. Also <b>an_egg</b>, <b>an_onion</b>. In sentences, <b>some</b> is short and weak: /səm/.</div>
{sub("B", "Sentences. Listen and repeat.", "2 min", "30.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S303)}</div>
<div class="box" style="margin-top:1mm"><h4>A LOT OF</h4>In fast speech, <b>a lot of</b> sounds like <i>a-lot-uv</i> /əˈlɑtəv/: We drink a lot of coffee.</div>""",
    22, """<ol><li>4A: Brazilians often say <i>a apple</i> /ə ˈæpəl/: insist on <b>an</b> + linking.</li>
<li>4B: stress the food words, not <i>some</i> or <i>any</i>: We have some <b>BEANS</b>. We don't have any <b>GAR</b>lic.</li></ol>""")

    # Page 5
    gaps = ["any", "some", "a lot of", "any", "some", "an", "some", "any", "lots of", "any", "an", "some"]
    def g(i): return f"({i+1}) {A(gaps[i], 'min-width:16mm')}"
    dlg = [("Kate", f"It's Christmas next week, and we're very busy at the bakery. Let's check the kitchen. Do we have {g(0)} sugar?"),
           ("Tom", f"Yes, there's {g(1)} sugar here. And we have {g(2)} eggs: there are fifty!"),
           ("Kate", f"Great. What about butter? Do we have {g(3)}?"),
           ("Tom", f"There's {g(4)} butter, but not much. And there's only {g(5)} orange for the orange cake."),
           ("Kate", f"So we need {g(6)} oranges and butter. We don't need {g(7)} flour: there are {g(8)} bags."),
           ("Tom", f"Do we have {g(9)} chocolate? People love your chocolate cookies."),
           ("Kate", f"No, and there's only {g(10)} apple, so let's buy {g(11)} apples too.")]
    dl = "".join(f"<p><b>{n}:</b> {t}</p>" for n, t in dlg)
    corr = [("We have lot of apples.", "We have a lot of apples. / lots of apples"), ("Do we have any coffees?", "Do we have any coffee?"),
            ("I need potato.", "I need a potato. / some potatoes"), ("We have any tomatoes.", "We have some tomatoes."),
            ("We don't have some rice.", "We don't have any rice."), ("I want a cheese sandwich and a orange juice.", "…and an orange juice.")]
    cl = "".join(f'<li value="{i+1}">{w} {R("→ " + c)}</li>' for i, (w, c) in enumerate(corr))
    b.page(f"""{sec(5, "Practice", "8 min")}
{sub("A", "Kate and Tom are in the kitchen of Kate's bakery in Chicago. Complete with the words in the box.", "5 min")}
<div class="bank">a lot of · an (×2) · any (×4) · lots of · some (×4)</div>
<div class="msg" style="max-width:none;padding:2mm 4mm;line-height:1.95">{dl}</div>
{sub("B", "Correct the mistakes.", "3 min")}
{twocol([f'<li value="{i+1}">{w}<div class="wline">{R(c)}</div></li>' for i, (w, c) in enumerate(corr)], 4)}""",
    22, """<p>A: before checking, ask the student to say why: <i>any</i> in a question, <i>some</i> in a positive sentence, <i>an</i> + singular. B: some sentences have two correct answers.</p>""")

    # Page 6
    items = ["meat", "sausages", "bread", "onions", "tomatoes", "lettuce", "rice", "cheese", "juice", "ice cream"]
    teacher_k = ["sausages", "rice", "juice", "bread"]
    box3 = lambda h, body="": f"<div style='flex:1;border:1pt solid #c9dfe3;border-radius:2mm;padding:1.5mm 2.5mm;min-height:24mm'><b class='small' style='color:#0f4a5a'>{h}</b><div class='small'>{body}</div></div>"
    b.page(f"""{sec(6, "Speaking", "12 min")}
{sub("A", "A Sunday barbecue. You and your teacher are making a barbecue together. You need these ten things.", "7 min")}
<div class="bank">{" · ".join(items)}</div>
<ol><li>Choose four things that you have at home. Write them in <b>My kitchen</b>. Don't show your teacher.</li>
<li>Ask your teacher: <i>Do you have any…?</i> Write the answers in <b>My teacher's kitchen</b>.</li>
<li>Write the things you need to buy in <b>Shopping list</b>.</li></ol>
<div style="display:flex;gap:3mm;margin:1mm 0 2mm">{box3("My kitchen")}{box3("My teacher's kitchen", R(", ".join(teacher_k)))}{box3("Shopping list")}</div>
<div class="msg" style="max-width:none;padding:2mm 4mm;line-height:1.55"><b>You:</b> Do you have any sausages?<br><b>Teacher:</b> Yes, I have some sausages. Do you have any cheese?<br><b>You:</b> No, I don't have any cheese.</div>
{sub("B", "Talk about your kitchen.", "5 min")}
<ol><li>What food do you always have in your kitchen?</li><li>Is there anything you never have at home? Why?</li>
<li>What's in your fridge right now? Is there a lot of food or not much?</li><li>Who usually goes to the supermarket in your house?</li></ol>""",
    24, """<ol><li>A: your kitchen has the items in red; answer with full sentences: <i>Yes, I have some… / No, I don't have any…</i> Before you start, ask which items are countable (sausages, onions, tomatoes).</li>
<li>B: correct <i>a bread</i>, <i>some</i> in negatives and the missing <i>a</i> in <i>a lot of</i>.</li></ol>""")

    # Page 7
    pc = [("Unit 25", "I can make past questions and negatives with did / didn't."), ("Unit 26", "I can use irregular past verbs: went, ate, saw, bought."),
          ("Unit 28", "I can ask questions in the present and past with who, whose, which…"), ("Unit 29", "I can buy clothes: ask about sizes, colors and prices, try things on and pay."),
          ("Unit 30", "I can talk about food with some, any, a / an and a lot of.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    pk = [("bottle", "water"), ("can", "soda"), ("carton", "milk"), ("jar", "honey"), ("loaf", "bread"), ("packet", "pasta")]
    def p(i): return f"a {A(pk[i][0], 'min-width:15mm')} of {pk[i][1]}"
    msg = (f"Hi Marcos! I'm at the supermarket. I have everything for lunch, but I want to buy some things for breakfast too: "
           f"{p(4)}, {p(2)} and {p(3)} for Leo. I also want {p(0)} for the car, {p(5)} for dinner on Monday and {p(1)} for you. Do we need anything else? Ana")
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:15mm"></th><th>In English…</th><th style="width:20mm">Easy!</th><th style="width:20mm">Sometimes</th><th style="width:20mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<div class="box" style="margin-top:0"><h4>PACKAGING WORDS</h4>We can count uncountable food with packaging words: <b>a bottle of</b> water, <b>two jars of</b> honey, <b>a loaf of</b> bread.</div>
<p><b>1. Ana's message.</b> Complete with the words in the box.</p>
<div class="bank">bottle · can · carton · jar · loaf · packet</div>
<div class="msg" style="max-width:none;line-height:2">{msg}</div>
<p style="margin-top:3mm"><b>2. My kitchen.</b> Write 6 sentences about the food in your kitchen. Use <i>some</i>, <i>any</i>, <i>a / an</i> and <i>a lot of</i>.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class: start with homework 2. Ask questions about the student's kitchen: <i>Do you have any…? How many…?</i> Check the packaging words in exercise 1.</p>""")

    b.extra("Audio scripts", f"""
{sub("30.1", "In the kitchen (slow and natural)")}
<p style="line-height:1.5">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("30.2", "Food words")}
<p>{" · ".join(S302)}</p>
{sub("30.3", "Sentences")}
<p>{" ".join(S303)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essentials 30 - Do we have any onions")
