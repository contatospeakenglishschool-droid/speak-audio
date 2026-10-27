# Speak! Essentials A1 - Unit 31 "Eat the rainbow" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
from speak_engine import *
setup(band="A1 · UNIT 31", audio_json="audio_a1-unit-31.json", img_dir="img")

PHOTOS = [("A", "bananas", "bananas"), ("B", "broccoli", "broccoli"), ("C", "carrots", "carrots"), ("D", "corn", "corn"),
          ("E", "eggplant", "eggplant"), ("F", "grapes", "grapes"), ("G", "peas", "peas"), ("H", "strawberries", "strawberries")]

_r = json.load(open("roteiro.json"))["units"]["a1-unit-31"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["31.1 Doctor"].split("\n")]
S312 = [x.split(": ", 1)[1] for x in _r["31.2 Repeat words"].split("\n")]
S313 = [x.split(": ", 1)[1] for x in _r["31.3 Repeat sentences"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LEVEL A1 · UNIT 31", "Eat the rainbow", "Healthy food · <b>how much / how many · a few / a little · not much / not many</b>",
                       [("YOU CAN", "talk about how much fruit and vegetables you eat"),
                        ("LANGUAGE", "How many strawberries? · I don't eat much fruit. · a few carrots · a little broccoli"),
                        ("PRONUNCIATION", "BROccoli · baNAnas · STRAWberries · a glass of /əv/")])
    b.page(f"""{sec(1, "Warm-up: a rainbow of food", "8 min")}
{sub("A", "Look at the photos. Write the word under each photo.", "3 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(w for _, w, _ in PHOTOS)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Talk about it.", "5 min")}
<ol><li>What color is each food: red, orange, yellow, green or purple? {R("red: strawberries · orange: carrots · yellow: bananas, corn · green: broccoli, peas · purple: eggplant, grapes")}</li>
<li>Which two words are uncountable? {R("broccoli, corn")}</li><li>Which ones do you eat? How often?</li></ol>""",
    26, """<ol><li>A: <b>eggplant</b> is American English. <b>corn</b> = the vegetable; in a can it's often called <i>sweetcorn</i>.</li>
<li>B: review Unit 30: countable nouns have a plural form (carrots, grapes, peas); <i>broccoli</i> and <i>corn</i> don't.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>8 fruits and vegetables by color · countable / uncountable</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Ana answers listeners' questions on a health radio show</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>How much / how many · not much / not many · a few / a little · a glass of</td><td>3</td></tr>
<tr><td>4 Pronunciation lab</td><td>5 min</td><td>Word stress in food words · weak <i>of</i></td><td>4</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Match the halves · complete with much, many, a few, a little</td><td>5</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Food diary memory game · did they eat the rainbow?</td><td>6</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>7</td></tr></table>
<div class="box"><h4>HOW THIS GUIDE WORKS</h4>Every page looks like the Student Book page with the same number. Your notes are in the <b>yellow box</b>.
<span class="red">Answers in red</span> are not in the Student Book. The <span class="time">5 min</span> chips show the time for each activity. Audio scripts are on the last page.</div>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Ana, the doctor from São Paulo, is a guest on the radio show <i>Healthy Life</i>. She answers questions from listeners in Recife, Curitiba, Belo Horizonte and Salvador: how many servings a day, how many strawberries, how much corn, can I eat only fruit, is juice healthy? On page 6, Mia (the night nurse) and Paulo (the photographer) keep food diaries: did they eat the rainbow?</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4><i>Fruit</i> is usually uncountable in English: <i>I eat many fruits</i> ✗ → <b>I eat a lot of fruit</b>. <i>Much</i> in positive sentences sounds strange: <i>I eat much vegetables</i> ✗ → <b>a lot of vegetables</b>. And <i>a few</i> / <i>a little</i> get mixed: <i>a few milk</i> ✗ → <b>a little milk</b>.</div>
<div class="box"><h4>AUDIO</h4>Track 31.1 Ask the doctor (slow and natural) · Track 31.2 Food words · Track 31.3 Sentences<br><span class="small">Facts in the show: the WHO recommends at least 400 g of fruit and vegetables a day (about five servings); the UK NHS counts 7 strawberries, 3 heaped spoons of corn or peas, or one glass of juice (maximum one a day) as one serving.</span></div>""")

    # Page 2
    qs = [("How many servings of fruit and vegetables do I need every day?", "1"), ("Are frozen vegetables healthy?", "X"),
          ("How much corn is one serving?", "3"), ("Is juice healthy?", "5"), ("How many strawberries are one serving?", "2"),
          ("I don't really like vegetables. Can I eat only fruit?", "4")]
    ql = "".join(f"<tr><td style='width:12mm;text-align:center'>{A(n, 'min-width:8mm')}</td><td>{q}</td></tr>" for q, n in qs)
    nums = [("five", "servings of fruit and vegetables a day (at least)"), ("seven", "strawberries are one serving"),
            ("three", "big spoons of corn or peas are one serving"), ("two", "glasses of juice still count as one serving")]
    nl = "".join(f"<li><b>{n}</b> <div class='wline'>{R(a)}</div></li>" for n, a in nums)
    b.page(f"""{sec(2, "Listening: Ask the doctor", "10 min")}
<p>Ana is a guest on the radio show <i>Healthy Life</i>. Listeners from all over Brazil send her questions about fruit and vegetables.</p>
{audiocard(["31.1 · SLOW", "31.1 · NATURAL"])}
{sub("A", "Listen. Number the questions 1–5 in the order you hear them. One question is extra: write X.", "3 min", "31.1 · SLOW")}
<table style="table-layout:fixed;font-size:9.3pt">{ql}</table>
{sub("B", "Why are these numbers important? Listen again and write.", "5 min", "31.1 · NATURAL")}
<ol>{nl}</ol>
{sub("C", "What does Ana say about juice? Do you agree?", "2 min")}
<div class="wline">{R("One small glass is one serving, but juice has a lot of sugar: eat the fruit!")}</div>""",
    31, """<ol><li>A: <b>a serving</b> = the amount of one food on your plate in one meal. <b>to eat the rainbow</b> = to eat food of many colors.</li>
<li>B: the numbers are from the WHO and the UK NHS (see the audio box on the overview page). Ask: <i>Do you eat five servings a day?</i></li></ol>""")

    # Page 3
    b.page(f"""{sec(3, "Language focus: quantity", "10 min")}
{sub("A", "Read the sentences from the radio show. Then choose the correct word.", "4 min")}
<div class="bank" style="background:#fff;font-weight:600">How <u>many</u> strawberries are one serving? · How <u>much</u> corn is one serving? · Pedro doesn't eat <u>many</u> vegetables. · Don't drink too <u>much</u> juice. · Try <u>a few</u> carrots or <u>a little</u> broccoli.</div>
<ol><li>We use <i>how many</i> and <i>not many</i> with {ch(["countable", "uncountable"], "countable")} nouns.</li>
<li>We use <i>how much</i> and <i>not much</i> with {ch(["countable", "uncountable"], "uncountable")} nouns.</li>
<li><i>a few</i> and <i>a little</i> mean {ch(["a big quantity", "a small quantity"], "a small quantity")}.</li>
<li>We use <i>a few</i> with {ch(["countable", "uncountable"], "countable")} nouns and <i>a little</i> with {ch(["countable", "uncountable"], "uncountable")} nouns.</li></ol>
<table style="table-layout:fixed;font-size:9.3pt"><tr><th style="width:34mm"></th><th>countable (carrots, grapes)</th><th>uncountable (corn, juice, fruit)</th></tr>
<tr><td><b>?</b></td><td>How <b>many</b> carrots do you eat?</td><td>How <b>much</b> juice do you drink?</td></tr>
<tr><td><b>–</b> (a small quantity)</td><td>I don't eat <b>many</b> carrots.</td><td>I don't drink <b>much</b> juice.</td></tr>
<tr><td><b>+</b> small quantity</td><td>I eat <b>a few</b> grapes.</td><td>I drink <b>a little</b> juice.</td></tr>
<tr><td><b>+</b> big quantity</td><td>I eat <b>a lot of</b> grapes.</td><td>I drink <b>a lot of</b> juice.</td></tr></table>
{sub("B", "Containers and measures. Match.", "3 min")}
<div class="two"><div><ol><li>a glass of {A("juice", "min-width:16mm")}</li><li>a bowl of {A("soup", "min-width:16mm")}</li><li>a cup of {A("coffee", "min-width:16mm")}</li></ol></div>
<div><ol><li value="4">a slice of {A("pizza", "min-width:16mm")}</li><li value="5">a spoon of {A("sugar", "min-width:16mm")}</li><li value="6">a piece of {A("cake", "min-width:16mm")}</li></ol></div></div>
<div class="bank" style="margin-top:1mm">cake · coffee · juice · pizza · soup · sugar</div>
<div class="box sand"><h4>REMEMBER</h4>We don't usually use <i>much</i> in positive sentences: <i>I eat much fruit</i> ✗ → I eat <b>a lot of</b> fruit. With uncountable nouns, use a container to count: <b>two glasses of</b> juice, <b>three spoons of</b> corn.</div>""",
    26, """<ol><li>A: <i>not many / not much</i> = a small quantity, not zero. Drill the table with real questions: <i>How much water do you drink?</i></li>
<li>B: accept other logical answers (a cup of tea, a glass of water).</li></ol>""")

    # Page 4
    b.page(f"""{sub("C", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>I eat many fruits.</td><td><b>I eat a lot of fruit.</b></td><td><i>fruit</i> is usually uncountable.</td></tr>
<tr><td>How many sugar do you want?</td><td><b>How much sugar do you want?</b></td><td><i>sugar</i> is uncountable.</td></tr>
<tr><td>How much apples do you eat?</td><td><b>How many apples do you eat?</b></td><td><i>apples</i> is countable.</td></tr>
<tr><td>I eat much vegetables.</td><td><b>I eat a lot of vegetables.</b></td><td>Positive: <i>a lot of</i>.</td></tr>
<tr><td>Can I have a few milk?</td><td><b>Can I have a little milk?</b></td><td>Uncountable: <i>a little</i>.</td></tr>
<tr><td>A little of juice, please.</td><td><b>A little juice, please.</b></td><td>No <i>of</i> after <i>a little</i>.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "5 min")}
{audiocard(["31.2", "31.3"])}
{sub("A", "Food words. Listen and repeat. Underline the stressed syllable.", "2 min", "31.2")}
<table style="table-layout:fixed;margin-top:0"><tr>{"".join(f"<td style='text-align:center'><b>{w}</b></td>" for w in S312)}</tr></table>
<p class="small">{R("BA-na-nas · BRO-cco-li · CAR-rots · corn · EGG-plant · grapes · peas · STRAW-ber-ries")}</p>
{sub("B", "Sentences. Listen and repeat.", "2 min", "31.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S313)}</div>
<div class="box" style="margin-top:1mm"><h4>WEAK OF</h4>In <b>a glass of</b>, <b>a cup of</b>, <b>a lot of</b>, <i>of</i> is short: /əv/. It sounds like <i>a-glass-uv</i>.</div>""",
    22, """<ol><li>4A: Brazilians often stress <i>baNAnas</i> correctly but say <i>broCOli</i> (as in Portuguese): it's <b>BRO</b>ccoli.</li>
<li>4B: <i>a few</i> /ə fjuː/ and <i>a little</i> /ə ˈlɪtəl/: the <i>t</i> sounds soft, like a quick <i>d</i>.</li></ol>""")

    # Page 5
    halves = [("Seven strawberries", "are one serving of fruit."), ("I don't drink much", "coffee. Just one cup a day."),
              ("Would you like a little", "milk in your tea?"), ("Can I have a few", "grapes, please?"),
              ("How many bananas", "do you eat every week?"), ("We need two glasses", "of juice for breakfast.")]
    order = [3, 0, 5, 1, 4, 2]  # right column shown in this order
    lt = "".join(f'<li value="{i+1}">{a} {A("abcdef"[order.index(i)], "min-width:8mm")}</li>' for i, (a, _) in enumerate(halves))
    rt = "".join(f'<p>{"abcdef"[j]}. {halves[k][1]}</p>' for j, k in enumerate(order))
    gaps = [("I don't eat", "much", "rice at night."), ("How", "many", "eggs do you need for the cake?"), ("There are only", "a few", "carrots in the fridge."),
            ("Put", "a little", "salt in the soup. Not too much!"), ("She doesn't eat", "many", "sweets."), ("How", "much", "water do you drink every day?"),
            ("I'd like", "a few", "strawberries with my yogurt."), ("We don't have", "much", "time. Let's go!")]
    gl = [f'<li value="{i+1}">{a} {A(g, "min-width:17mm")} {c}</li>' for i, (a, g, c) in enumerate(gaps)]
    b.page(f"""{sec(5, "Practice", "8 min")}
{sub("A", "Match the sentence halves.", "3 min")}
<div class="two"><div><ol>{lt}</ol></div><div>{rt}</div></div>
{sub("B", "Complete with much, many, a few or a little.", "5 min")}
{twocol(gl, 5)}
<p class="small">Now answer questions 2 and 6 about you.</p>""",
    22, """<p>A: ask the student to explain each match: countable or uncountable? B: check that the student knows if each noun is countable before choosing. Then ask more personal questions: <i>How much rice do you eat? How many cups of coffee do you drink?</i></p>""")

    # Page 6
    mia = ["twelve cups of coffee", "a few cookies", "one banana", "a little lettuce", "two glasses of orange juice"]
    paulo = ["twenty strawberries", "three tomatoes", "a lot of watermelon", "two red apples", "four glasses of tomato juice"]
    b.page(f"""{sec(6, "Speaking", "12 min")}
{sub("A", "Memory game. Look at Mia's food diary for one minute. Then close your book. Your teacher asks questions. Answer from memory.", "4 min")}
<div style="display:flex;gap:4mm;align-items:stretch">
<div class="msg" style="flex:1;max-width:none;padding:2mm 4mm"><b>Mia's food diary (two days)</b><br>{"<br>".join("· " + x for x in mia)}</div>
<div class="msg" style="flex:1;max-width:none;padding:2mm 4mm"><b>Paulo's food diary (two days)</b><br>{"<br>".join("· " + R(x) for x in paulo) if T else "Your teacher has Paulo's diary. Ask questions and take notes:<br><br>"}</div></div>
<div class="bank" style="margin-top:2mm">How much…? · How many…? · a lot of · a few / a little · not much / not many</div>
<div class="msg" style="max-width:none;padding:2mm 4mm;line-height:1.55"><b>Teacher:</b> How much coffee did Mia drink?<br><b>You:</b> She drank a lot of coffee: twelve cups!</div>
{sub("B", "Now ask your teacher about Paulo's food diary. Then answer.", "4 min")}
<ol><li>Did Mia and Paulo eat five servings a day? {R("Mia: no, not many vegetables. Paulo: yes.")}</li>
<li>Did they eat the rainbow? {R("No! Mia ate very little fruit and vegetables; all Paulo's food was red.")}</li></ol>
{sub("C", "And you?", "4 min")}
<ol><li>What fruit and vegetables did you eat yesterday? How much? How many?</li><li>Did you eat the rainbow yesterday? Which colors were missing?</li><li>Do you drink a lot of juice or soda?</li></ol>""",
    22, """<ol><li>A: give the student one minute; then ask five questions with <i>How much / How many…?</i> B: you have Paulo's diary (in red); answer the student's questions from memory too.</li>
<li>Mia works at night and drinks a lot of coffee: a good moment to ask about the student's habits.</li></ol>""")

    # Page 7
    pc = [("Unit 26", "I can use irregular past verbs: went, ate, saw, bought."), ("Unit 28", "I can ask questions in the present and past with who, whose, which…"),
          ("Unit 29", "I can buy clothes: ask about sizes, colors and prices, try things on and pay."), ("Unit 30", "I can talk about food with some, any, a / an and a lot of."),
          ("Unit 31", "I can ask and talk about quantity: how much, how many, a few, a little.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [(["much", "lots of", "a lots of"], "lots of", "We bought", "mangoes at the market."), (["a few", "a little", "many"], "a little", "Can I have", "sugar in my coffee?"),
          (["much", "many", "a few"], "much", "I don't drink", "milk. I don't like it."), (["How many", "How much", "How"], "How many", "", "tomatoes do we need for the salad?"),
          (["a glass of", "a bowl of", "a little of"], "a glass of", "Would you like", "water?"), (["much", "many", "a little"], "many", "They didn't eat", "vegetables when they were children.")]
    hl = "".join(f"<li>{a} {ch(o, r)} {c}</li>" for o, r, a, c in hw)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:15mm"></th><th>In English…</th><th style="width:20mm">Easy!</th><th style="width:20mm">Sometimes</th><th style="width:20mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Choose the correct option.</b></p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. My food diary.</b> Write what you ate and drank yesterday (6 sentences). Use <i>a lot of, a few, a little, not much, not many</i> and containers (a glass of…). Did you eat the rainbow?</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class: start with homework 2. Ask <i>How much…? How many…?</i> about the student's diary and decide together: did they eat the rainbow?</p>""")

    b.extra("Audio scripts", f"""
{sub("31.1", "Ask the doctor (slow and natural)")}
<p style="line-height:1.5">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("31.2", "Food words")}
<p>{" · ".join(S312)}</p>
{sub("31.3", "Sentences")}
<p>{" ".join(S313)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essentials 31 - Eat the rainbow")
