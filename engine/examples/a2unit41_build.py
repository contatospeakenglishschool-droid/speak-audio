# Speak! Bridge A2 - Unit 41 "Curry" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 41", audio_json="audio_a2-unit-41.json", img_dir="img")

PHOTOS = [("A", "chicken", "chicken"), ("B", "chickens", "chickens"), ("C", "red peppers", "red peppers"), ("D", "coconut milk", "coconut milk"),
          ("E", "spinach", "spinach"), ("F", "green beans", "green beans"), ("G", "yogurt", "yogurt"), ("H", "chilies", "chilies")]
_r = json.load(open("roteiro.json"))["units"]["a2-unit-41"]
S411 = [x.split(": ", 1) for x in _r["41.1 Too much chicken"].split("\n")]
S412 = [x.split(": ", 1)[1] for x in _r["41.2 Repeat: quantities"].split("\n")]
S413 = [x.split(". ", 1)[1] for x in [y.split(": ", 1)[1] for y in _r["41.3 How many syllables?"].split("\n")]]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 41", "Curry", "Shopping and cooking · <b>countable and uncountable nouns, quantifiers</b>",
                       [("YOU CAN", "talk about food and quantities: some, any, a few, a little, much, many, too much, enough, plenty of"),
                        ("LANGUAGE", "Did you get any chicken? · I got a few chilies. · We have too much chicken! · There's plenty of rice."),
                        ("PRONUNCIATION", "weak some and of · hidden syllables: VEG-ta-bles, CUP-board")])
    b.page(f"""{sec(1, "Warm-up: ingredients", "8 min")}
{sub("A", "Name the food in the photos.", "3 min")}
{photo_grid(T, PHOTOS)}
{sub("B", "Talk about it.", "5 min")}
<ol style="line-height:1.5;margin:0"><li>What could you cook with these ingredients? What other ingredients would you need?</li><li>Where in the world does this kind of food come from?</li>
<li>Do you like spicy food? Do Brazilian dishes use coconut milk or chilies? Which ones?</li></ol>""",
    27, """<ol><li>A: <i>chicken</i> (the meat, uncountable) vs <i>chickens</i> (the animals, countable). Coconut milk is made from the white part of the coconut. Drill <i>spinach</i> /ˈspɪnɪtʃ/, <i>yogurt</i> /ˈjoʊɡərt/.</li>
<li>B: curries are popular in many countries of South and Southeast Asia. Brazilian links: moqueca and bobó use coconut milk; many dishes from Bahia and the North use chilies.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Ingredients for a curry</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Tom and Lucy both did the grocery shopping</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Countable and uncountable nouns, quantifiers</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Quantifiers</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>4 min</td><td>Weak forms · how many syllables?</td><td>5</td></tr>
<tr><td>5 Practice</td><td>9 min</td><td>Choose the quantifier · a coffee or coffee?</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>What did you buy? Compare shopping lists</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Roommates Tom (Neural2-D) and Lucy (Neural2-C) both did the grocery shopping for the weekend, so now they have too much chicken and too many onions. They decide to make a big curry and invite Kate (Tom's sister) and Rita (Lucy's boss at City Coffee) for dinner. No new facts; US units: two pounds of onions (about 900 g).</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students make uncountable nouns plural or use <i>a/an</i> (<i>an advice, breads, informations</i>), say <i>many money</i> and <i>How many time?</i>, forget <i>of</i> in <i>plenty of</i>, and confuse <i>too much</i> (a problem) with <i>a lot of</i> (neutral).</div>
<div class="box"><h4>AUDIO</h4>Track 41.1 Too much chicken (slow and natural) · Track 41.2 Repeat: quantities · Track 41.3 How many syllables?</div>""")

    # Page 2
    who = [("chilies", "L, T"), ("green beans", "L"), ("red peppers", "L"), ("onions", "L, T"), ("spinach", "T"), ("chicken", "L, T"), ("coconut milk", "L"), ("yogurt", "T")]
    wl = [f'<li value="{i+1}">{w} {A(a, "min-width:12mm;text-align:center")}</li>' for i, (w, a) in enumerate(who)]
    dq = [("What's the problem?", "They both bought groceries, so they have too much food."), ("What are they going to do?", "make a big curry and invite Kate and Rita"),
          ("Which foods did they both buy?", "chilies, onions and chicken"), ("What food did they already have at home?", "yogurt, rice and cans of tomatoes"),
          ("What does Lucy mean: \"They won't go bad\"?", "Onions stay fresh for a long time.")]
    dql = "".join(f"<li>{q} {A(a, 'min-width:30mm')}</li>" for q, a in dq)
    b.page(f"""{sec(2, "Listening: too much chicken", "10 min")}
<div style="display:flex;gap:2.5mm;align-items:center"><p style="flex:1;margin:0">Lucy comes home with four bags of groceries for the weekend. But Tom has a surprise for her…</p>{img('J', 26, 18)}{img('I', 26, 18)}</div>
{audiocard(["41.1 · SLOW", "41.1 · NATURAL"])}
{sub("A", "Listen. Who bought what? Write L (Lucy), T (Tom) or both.", "4 min", "41.1 · SLOW")}
<div style="font-size:9pt">{twocol(wl, 5)}</div>
{sub("B", "Listen again and answer the questions.", "5 min", "41.1 · NATURAL")}
<ol style="margin:0;line-height:1.5;font-size:9pt">{dql}</ol>
{sub("C", "Has this ever happened in your home? What do you do with extra food?", "1 min")}""",
    22, """<ol><li>A–B: <i>cupboard</i> /ˈkʌbərd/ (silent p) = a kitchen cabinet with doors. <i>Go bad</i> = become unsafe to eat. <i>Two pounds</i> is about 900 g.</li>
<li>C: a good moment for <i>freezer</i>, <i>leftovers</i> and <i>invite people over</i>.</li></ol>""")

    # Page 3
    nouns = ["chilies", "chicken", "coconut milk", "green beans", "red peppers", "spinach", "yogurt"]
    cnt = {"chilies", "green beans", "red peppers"}
    nl = " · ".join(f"{n}{(' ' + R('C' if n in cnt else 'U')) if T else ''}" for n in nouns)
    b.page(f"""{sec(3, "Language focus: how much? how many?", "10 min")}
{sub("A", "Countable (C) nouns have a plural; uncountable (U) nouns don't. Which are which?", "2 min")}
<p style="margin:.5mm 0;font-weight:600">{nl}</p>
{sub("B", "Some and any. Read and choose.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">Did you get <b>any</b> chilies / chicken? · I got <b>some</b> chilies / chicken. · I didn't get <b>any</b> chilies / chicken.</div>
<p style="margin:.5mm 0;line-height:1.7">In questions, we use {ch(["some", "any"], "any")}. We use <i>some</i> in {ch(["positive", "negative"], "positive")} sentences and <i>any</i> in {ch(["positive", "negative"], "negative")} sentences.</p>
{sub("C", "A few, a little, much, many. Read and choose.", "3 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">I got <b>a few</b> chilies too. · We already have <b>a little</b> yogurt. · You said you didn't have <b>much</b> time. · Do you have <b>many</b> bags?</div>
<p style="margin:.5mm 0;line-height:1.7"><i>a few</i> and <i>many</i> go with {ch(["plural countable", "uncountable"], "plural countable")} nouns. <i>a little</i> and <i>much</i> go with {ch(["plural countable", "uncountable"], "uncountable")} nouns.</p>
{sub("D", "Too much, enough, plenty of. Read and choose.", "3 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">We have <b>too much</b> chicken. We have <b>too many</b> onions! · We have <b>enough</b> chicken for everyone, and there's <b>plenty of</b> rice.</div>
<p style="margin:.5mm 0;line-height:1.7">With <i>too much / too many</i>, we're {ch(["happy", "not happy"], "not happy")}. With <i>enough / plenty of</i>, we're {ch(["happy", "not happy"], "happy")}. {ch(["Enough", "Plenty of"], "Plenty of")} means we have some extra.</p>
<div class="box sand"><h4>RULE</h4><b>some</b> (+) · <b>any</b> (− and ?) · <b>a few / many</b> + plural · <b>a little / much</b> + uncountable · <b>a lot of</b> + both · <b>too much / too many</b> = a problem · <b>enough</b> = what we need · <b>plenty of</b> = enough and extra. More on the next page: <b>Grammar reference</b>.</div>""",
    25, """<ol><li>A: <i>chicken</i> is uncountable as food; <i>a chicken</i> is the animal (or a whole bird to cook).</li>
<li>Earlier units used <i>too</i> + adjective for a problem; <i>too much / too many</i> do the same with quantities. Point out the <i>of</i> in <i>plenty of</i>.</li></ol>""")

    grammar_ref.quantifiers(b)

    # Page 5
    syl = [("vegetables", "3: VEG-ta-bles"), ("chocolate", "2: CHOC-lit"), ("spinach", "2: SPIN-ach"), ("cupboard", "2: CUB-erd"), ("coconut", "3: CO-co-nut"), ("yogurt", "2: YO-gurt")]
    syl_t = "".join(f"<li>{w} {A(n, 'min-width:24mm')}</li>" for w, n in syl)
    syl_s = "".join(f"<li>{A(n, 'min-width:10mm')}</li>" for w, n in syl)
    b.page(f"""{sub("E", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>How many money do you have?</td><td><b>How much money do you have?</b></td><td>money is uncountable.</td></tr>
<tr><td>Can you give me an advice?</td><td><b>Can you give me some advice?</b></td><td>advice is uncountable.</td></tr>
<tr><td>I bought two breads.</td><td><b>I bought two loaves of bread.</b></td><td>use a unit.</td></tr>
<tr><td>We have plenty rice.</td><td><b>We have plenty of rice.</b></td><td>plenty of.</td></tr>
<tr><td>There are too much people.</td><td><b>There are too many people.</b></td><td>people is plural.</td></tr>
<tr><td>I love this city. It has too many parks!</td><td><b>It has a lot of parks!</b></td><td>too = a problem.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "4 min")}
{audiocard(["41.2", "41.3"])}
{sub("A", "Listen and repeat. some = /səm/, of = /əv/: short and weak.", "2 min", "41.2")}
{twocol([f'<li value="{i+1}">{s}</li>' for i, s in enumerate(S412)], 4)}
{sub("B", "Listen to six food words. How many syllables do you hear? Write the number.", "2 min", "41.3")}
<ol style="line-height:1.5;column-count:3;column-gap:5mm">{syl_t if T else syl_s}</ol>""",
    24, """<ol><li>A: link the words: <i>plenty‿of‿rice</i>, <i>a few‿chilies</i>. <i>Some</i> is stressed only when it contrasts.</li>
<li>B: script: vegetables, chocolate, spinach, cupboard, coconut, yogurt. Brazilians often say all the letters: <i>VE-GE-TA-BLES</i>, <i>CUP-BOARD</i>.</li></ol>""")

    # Page 6
    pr = [(["a little", "a few", "much"], "a few", "Can I borrow", "chilies? I want to make a curry."), (["any", "much", "many"], "much", "How", "milk do we have?"),
          (["a little", "a few", "plenty"], "a little", "I only want", "yogurt, please."), (["some", "enough of", "enough"], "enough", "I think we have", "pizza for six people."),
          (["too many", "plenty", "too much"], "too much", "Is it possible to eat", "ice cream?"), (["too much", "too many", "a little"], "too many", "There are", "people in this room."),
          (["many", "much", "too much"], "many", "There aren't", "tomatoes in this salad."), (["plenty", "plenty of", "many"], "plenty of", "There's", "time before the movie starts."),
          (["any", "some", "many"], "any", "We don't have", "spinach. Can you put it on the shopping list?")]
    prl = [f'<li value="{i+1}">{a} {ch(o, r)} {e}</li>' for i, (o, r, a, e) in enumerate(pr)]
    cu = [("I'll have", "a coffee", "please. (one cup, for me)"), ("Do you want some", "cake", "? (from the big cake, to share)"), ("Can I have", "an ice cream", "? (one cone)"),
          ("There's", "pie", "in the fridge if you're hungry. (some of a big pie)")]
    cul = "".join(f"<li>{a} {A(w, 'min-width:20mm')}{'' if e[0] in '?' else ' '}{e}</li>" for a, w, e in cu)
    b.page(f"""{sec(5, "Practice", "9 min")}
{sub("A", "Choose the best option. Be ready to explain your answer.", "5 min")}
<div style="font-size:9pt"><ol style="line-height:1.6;margin:0">{"".join(prl)}</ol></div>
{sub("B", "Word builder: a coffee or coffee? Some food words can be both. Complete with or without a/an.", "4 min")}
<div class="bank">a coffee / coffee · cake / a cake · an ice cream / ice cream · a pie / pie</div>
<ol style="line-height:1.6;font-size:9pt">{cul}</ol>
<p class="small" style="margin:.5mm 0">countable = one, for one person · uncountable = in general, or some of something big to share</p>""",
    25, """<ol><li>A: ask for the reason each time: countable or uncountable? question or negative? a problem?</li>
<li>B: from the Linguahouse extension (the drawing game is replaced by this exercise). In a café, Americans say <i>Can I get a coffee?</i></li></ol>""")

    # Page 7
    items = ["chicken", "chilies", "garlic", "green beans", "onions", "red peppers", "rice", "spinach", "tomatoes", "a dessert (your idea)"]
    tbought = ["chicken", "garlic", "onions", "rice", "tomatoes", "ice cream"]
    rows = "".join(f"<tr><td style='height:6mm'>{i+1}</td><td></td><td>{R(tbought[i]) if T else ''}</td></tr>" for i in range(6))
    b.page(f"""{sec(6, "Speaking: what did you buy?", "12 min")}
<div style="display:flex;gap:3mm;align-items:center"><p style="flex:1;margin:0">You and your teacher want to make a curry together. You made a shopping list, but you went shopping separately and each of you only remembered <b>six</b> things.</p>{img('I', 30, 20)}</div>
<div class="box" style="margin:1mm 0"><b>Shopping list:</b> {" · ".join(items)}</div>
{sub("A", "Choose six things you bought. Write them in your column. Don't show your teacher!", "2 min")}
<table style="margin:0;font-size:9pt"><tr><th style="width:8mm"></th><th>What I bought</th><th>What my teacher bought</th></tr>{rows}</table>
{sub("B", "Ask and answer. Write what your teacher bought.", "5 min")}
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:9pt"><b>You:</b> Did you buy any tomatoes? <b>Teacher:</b> Yes, I bought a few tomatoes. / No, I didn't buy any tomatoes. How about you? Did you get any rice?</div>
{sub("C", "Now talk about your shopping together.", "5 min")}
<ol style="margin:0;line-height:1.5"><li>What do we have too much or too many of? What do we have enough of? Plenty of?</li><li>Do we need to go back to the store? What for?</li><li>Is there anything that might go bad? What can we do with it?</li></ol>""",
    25, """<ol><li>A–B: the red list is your side; change it if you like. Answer with different quantifiers: <i>a few, some, plenty of, a lot of</i>.</li>
<li>C: insist on full sentences: <i>We have too much chicken because we both bought some.</i></li></ol>""")

    # Page 8
    pc = [("A2 Unit 37", "I can use -ing forms after verbs like enjoy and avoid, and as subjects."), ("A2 Unit 38", "I can use a/an, the and no article correctly."),
          ("A2 Unit 39", "I can put nouns together: a coffee cup, Leo's ideas, the end of the story."), ("A2 Unit 41", "I can talk about quantities with some, any, much, many, enough and plenty of.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    mh = [("If you want to make a cake, we need", "some eggs."), ("Can you tell me how many", "eggs you need?"), ("How much", "time do you spend cooking every week?"),
          ("I need a little", "milk for my coffee."), ("I'm sorry, we don't have", "any fresh fish today."), ("I've got a few", "carrots and onions."),
          ("If you have too many bananas,", "you can put a few in the freezer."), ("Yuck! There's too much", "garlic in this soup!")]
    ends = sorted(e for _, e in mh)
    lt = "abcdefgh"
    mhl = "".join(f"<li>{s} {A(lt[ends.index(e)], 'min-width:6mm;text-align:center')}</li>" for s, e in mh)
    el = "".join(f"<li>{e}</li>" for e in ends)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Match the sentence halves.</b></p>
<div style="display:flex;gap:4mm;font-size:8.8pt"><ol style="flex:1;line-height:1.5;margin:0">{mhl}</ol><ol type="a" style="flex:1;line-height:1.5;margin:0">{el}</ol></div>
<p style="margin-top:1.5mm"><b>2. My favorite dish (50–75 words).</b> Write about a dish you love to cook or eat. What ingredients do you need, and how much? Use at least four quantifiers.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class: the student reads the recipe aloud; ask <i>How much…? How many…? Do you need any…?</i> If there's time, cook it together in English on the next class.</p>""")

    b.extra("Audio script", f"""
{sub("41.1", "Too much chicken (slow and natural)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in S411)}</p>
{sub("41.2", "Repeat: quantities")}
<p>{" · ".join(S412)}</p>
{sub("41.3", "How many syllables? (3-second pause)")}
<p>{" · ".join(S413)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 41 - Curry")
