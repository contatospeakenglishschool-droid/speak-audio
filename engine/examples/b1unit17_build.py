# Speak! Progress B1 - Unit 17 "Cooking and eating" (all English) - B1 format (2026-11-09)
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Progress"
setup(band="B1 · UNIT 17", audio_json="audio_b1-unit-17.json", img_dir="img")


_r = json.load(open("roteiro.json"))["units"]["b1-unit-17"]
S171 = _r["17.1 Just like yours"].split("\n")
S172 = [x.split(": ", 1)[1] for x in _r["17.2 Repeat: linking in instructions"].split("\n")]


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
    cover = cover_html(T, "LEVEL B1 · UNIT 17", "Cooking and eating", "Recipes, kitchen words and taste · <b>time clauses: when, as soon as, until, while</b>",
                       [("YOU CAN", "follow and give step-by-step cooking instructions and describe how food tastes"),
                        ("LANGUAGE", "a frying pan · a saucepan · chop · stir · squeeze · bland · greasy · as soon as it boils · until it's golden"),
                        ("PRONUNCIATION", "linking in instructions: chop it up, turn it over")])
    ut = [("a flat pan with a long handle, for frying", "a frying pan"), ("a deep round pan with a lid, for boiling and sauces", "a saucepan"),
          ("a large round pan for stir-frying, from Chinese cooking", "a wok"), ("a big metal tray for cooking meat in the oven", "a roasting pan"),
          ("the hot box where you bake and roast food", "an oven"), ("the top part with burners where you put pans", "a stove"),
          ("a big spoon, also a unit of measure (tbsp)", "a tablespoon"), ("a tool with a blade for cutting", "a knife")]
    utl = [f'<li value="{i+1}">{d} {A(w, "min-width:22mm")}</li>' for i, (d, w) in enumerate(ut)]
    b.page(f"""{sec(1, "Warm-up: in the kitchen", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 35)}<div style="flex:1">
{sub("A", "Discuss with your teacher.", "3 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0"><li>Who does most of the cooking in your home?</li><li>Do you follow recipes exactly, or do you prefer to improvise?</li><li>What's the best thing you can cook?</li></ol></div></div>
{sub("B", "Kitchen words. Write the words from the box next to the definitions.", "4 min")}
<div class="bank">a frying pan · a knife · an oven · a roasting pan · a saucepan · a stove · a tablespoon · a wok</div>
<div style="font-size:8.6pt">{twocol(utl, 4)}</div>
{sub("C", "Which of these do you use every week? Which do you have but rarely use?", "1 min")}""",
    30, """<ol><li>A: <i>improvise</i> = cook without a recipe, using what you have.</li>
<li>B: <i>stove</i> is American English (British: <i>cooker</i> or <i>hob</i>). In recipes: <i>tbsp</i> = tablespoon, <i>tsp</i> = teaspoon. US recipes measure in <i>cups</i> and use °F (350°F ≈ 180°C).</li>
<li>C: also teach <i>a cutting board, a bowl, a wooden spoon, a blender</i> if the student needs them.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 60 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Discussion · kitchen words: pans, oven, stove</td><td>1</td></tr>
<tr><td>2 Listening</td><td>12 min</td><td>Phone call: Rita gives Danny her pancake recipe</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>8 min</td><td>Time clauses: when, as soon as, once, until, while, before</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Time clauses (study at home)</td><td>4</td></tr>
<tr><td>4 Vocabulary lab + pronunciation</td><td>8 min</td><td>Cooking verbs in a recipe · taste adjectives · linking</td><td>5</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Danny's message about the breakfast · joining instructions</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Give a recipe · long turn · talking point</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>4 min</td><td>Can-do · language notes · writing homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY</h4>The Linguahouse lesson is a vocabulary lesson (kitchen utensils, cooking verbs in two recipes, taste adjectives) with no listening and no grammar. We added a listening and a grammar point that fits recipes: time clauses. Following the school's choice for food units, the dishes are international. Danny wants to thank Mrs. Lima, who always cooks for the hostel, so he makes American pancakes for breakfast. He calls his mom, Rita (City Coffee, Chicago), for her recipe. The recipe uses US measures (cups, tablespoons). There are no factual claims in the unit beyond cooking instructions. In the Practice, Danny tells Rita how the breakfast went. The writing model is Tom's guacamole recipe.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students use <i>will</i> after <i>when / as soon as</i> (<i>when it will boil</i>), say <i>I love kitchen</i> (cooking), <i>my mother is a great cooker</i> (cook), <i>turn on the fire</i> (the stove), and <i>the meat is soft</i> (tender). They also confuse <i>sour</i> and <i>bitter</i>.</div>
<div class="box"><h4>AUDIO</h4>Track 17.1 Just like yours (natural and slow) · Track 17.2 Repeat: linking in instructions</div>""")

    # Page 2 - Listening
    gist = ["it's his mom's birthday", "to thank Mrs. Lima, who always cooks for the guests", "he wants to sell them at the hostel"]
    ing = [("flour", "2 cups"), ("sugar", "2 tablespoons"), ("baking powder", "2 teaspoons"), ("salt", "a pinch"), ("butter", "3 tablespoons"), ("eggs", "2"), ("milk", "almost 2 cups")]
    ingt = "".join(f"<tr><td>{n}</td><td>{A(q, 'min-width:24mm')}</td></tr>" for n, q in ing)
    st = [("Mix the flour, sugar, baking powder and salt.", "1"), ("Melt the butter.", "2"), ("Beat the eggs with the milk.", "3"), ("Add the butter to the eggs and milk.", "4"),
          ("Stir the wet and dry mixes together, but not too much.", "5"), ("Leave the batter for five minutes.", "6"), ("Pour a quarter cup of batter into the hot pan.", "7"), ("Flip the pancake when the bubbles pop.", "8")]
    order = [2, 5, 0, 7, 3, 6, 1, 4]
    stl = "".join(f'<li style="list-style:none">{A(st[k][1], "min-width:5mm")} {st[k][0]}</li>' for k in order)
    b.page(f"""{sec(2, "Listening: just like yours", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{audiocard(["17.1 · NATURAL", "17.1 · SLOW"])}
{sub("A", "Danny calls his mom, Rita, in Chicago. Listen at natural speed. Why is he making pancakes?", "2 min", "17.1")}
<p style="margin:.3mm 0;font-size:8.9pt">{ch(gist, gist[1])}</p></div>{img('B', 40, 27)}</div>
<div style="display:flex;gap:4mm;align-items:flex-start"><div style="width:58mm">
{sub("B", "Listen again. How much?", "3 min")}
<table style="font-size:8.6pt;margin:.5mm 0"><tr><th>ingredient</th><th>amount</th></tr>{ingt}</table></div><div style="flex:1">
{sub("C", "Number the steps in order (1–8).", "3 min")}
<ul style="font-size:8.5pt;line-height:1.5;margin:0;padding-left:0">{stl}</ul></div></div>
{sub("D", "Think about it. Discuss with your teacher.", "4 min")}
<ol style="line-height:1.4;font-size:8.7pt;margin:0"><li>Why does Rita say "A few lumps are fine"? {R("If you stir too much, the pancakes will be tough.") if T else ""}</li><li>Is there a dish that your family always makes "just like" someone else did?</li></ol>
<div class="box sand" style="margin-top:1mm"><h4>NOTICE: USEFUL CHUNKS</h4><i>What's the occasion? · Got it. · Not yet. · That's the secret! · Trust me. · Oh, and one more thing… · a pinch of salt</i></div>""",
    24, """<ol><li>B: <i>batter</i> = the liquid mix for pancakes and cakes; <i>flip</i> / <i>turn over</i> = turn upside down. A US cup is about 240 ml.</li>
<li>C: ask the student to retell the recipe from their numbered list, using the time words they heard (<i>while, when, as soon as, until</i>).</li></ol>""")

    # Page 3 - Language focus
    fs = [("___ it's cooling down, beat the eggs with the milk.", "While"), ("___ the butter isn't too hot, add it to the eggs.", "When"),
          ("Stop ___ everything is combined.", "as soon as"), ("___ it's hot, pour in a quarter cup of batter.", "Once"),
          ("Wait ___ you see small bubbles on top.", "until"), ("Leave the batter for five minutes ___ you start cooking.", "before")]
    fsl = "".join(f"<li><i>{s.replace('___', A(a, 'min-width:16mm'))}</i></li>" for s, a in fs)
    b.page(f"""{sec(3, "Language focus: time clauses", "8 min")}
{sub("A", "Complete Rita's instructions with the words from the box. Then listen again and check.", "2 min")}
<div class="bank">as soon as · before · once · until · when · while</div>
<ol style="line-height:1.8;font-size:8.9pt;margin:0">{fsl}</ol>
{sub("B", "Complete the rules. Choose.", "3 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0"><li><i>As soon as</i> and <i>once</i> mean {ch(["immediately after", "a long time after"], "immediately after")}.</li>
<li><i>Wait until you see bubbles</i>: you wait, and you stop waiting {ch(["when you see them", "before you see them"], "when you see them")}.</li>
<li><i>While</i> is for two actions {ch(["at the same time", "one after the other"], "at the same time")}.</li>
<li>After <i>when, as soon as, until</i>, for the future we use {ch(["will", "the present simple"], "the present simple")}: <i>Send me a photo when they're ready.</i></li></ol>
{sub("C", "Correct or incorrect? Choose.", "3 min")}
<ol style="line-height:1.6;font-size:8.9pt;margin:0"><li>As soon as the water will boil, add the pasta. {ch(["correct", "incorrect"], "incorrect")} {R("→ boils") if T else ""}</li><li>Cook the onions until they're soft. {ch(["correct", "incorrect"], "correct")}</li><li>I'll text you when I get home. {ch(["correct", "incorrect"], "correct")}</li><li>Don't open the oven until the cake doesn't rise. {ch(["correct", "incorrect"], "incorrect")} {R("→ until the cake rises") if T else ""}</li></ol>
<div class="box sand"><h4>RULE</h4><b>when</b> (at that time) · <b>as soon as / once</b> (immediately after) · <b>until</b> (up to that moment, then stop) · <b>while</b> (at the same time) · <b>before / after</b>. In instructions and for the future, use the <b>present</b> after these words, not <i>will</i>. More on the next page: <b>Grammar reference</b>.</div>""",
    27, """<ol><li>A: draw a simple timeline for <i>until</i> (an arrow that stops at a point) and for <i>while</i> (two parallel arrows).</li>
<li>B: point out the comma when the time clause comes first.</li>
<li>C: in 4, <i>until</i> already contains the idea of "not before"; no negative is needed.</li></ol>""")

    grammar_ref.time_clauses(b)

    # Page 5 - Vocabulary lab
    rv = ["Chop", "Heat up", "fry", "Add", "Stir", "boil", "Squeeze", "serve"]
    rec = ("<b>Spaghetti with tomato sauce</b><br>1 {0} the onion and the garlic into small pieces. 2 {1} two tablespoons of olive oil in a frying pan and {2} the onion and garlic for a few minutes. "
           "3 {3} a can of tomatoes, salt and pepper. 4 {4} with a wooden spoon and cook on low heat for 30 minutes. 5 In a saucepan, {5} the spaghetti. "
           "6 {6} a little lemon juice into the sauce. 7 Mix the pasta with the sauce and {7} it warm.").format(*[A(v, "min-width:13mm") for v in rv])
    ta = [("lemons, vinegar", "sour"), ("black coffee without sugar", "bitter"), ("hospital food, soup with no salt", "bland"), ("fries, fried chicken", "greasy"),
          ("a chocolate cake with cream", "rich"), ("chips, soy sauce", "salty"), ("chili peppers, curry", "spicy"), ("honey, candy", "sweet")]
    tal = [f'<li value="{i+1}">{f} {A(a, "min-width:13mm")}</li>' for i, (f, a) in enumerate(ta)]
    b.page(f"""{sec(4, "Vocabulary lab: cooking verbs and taste", "4 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Complete the recipe with the verbs from the box.", "2 min")}
<div class="bank">add · boil · chop · fry · heat up · serve · squeeze · stir</div></div>{img('C', 30, 20)}</div>
<div class="box" style="font-size:8.6pt;line-height:1.75;margin:.5mm 0">{rec}</div>
{sub("B", "How does it taste? Write an adjective from the box.", "2 min")}
<div class="bank">bitter · bland · greasy · rich · salty · sour · spicy · sweet</div>
<div style="font-size:8.5pt">{twocol(tal, 4)}</div>
<div class="box sand"><h4>WATCH OUT: FALSE FRIENDS AND WORD CHOICE</h4>
<table style="margin:0;font-size:8.2pt"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>I love kitchen.</td><td><b>I love cooking.</b></td><td>the <i>kitchen</i> is the room; the activity is <i>cooking</i>.</td></tr>
<tr><td>My mom is a great cooker.</td><td><b>My mom is a great cook.</b></td><td>a <i>cook</i> is a person; a <i>cooker</i> is a stove (UK).</td></tr>
<tr><td>Turn on the fire.</td><td><b>Turn on the stove / the burner.</b></td><td><i>fire</i> = flames that burn things.</td></tr>
<tr><td>The meat is very soft.</td><td><b>The meat is very tender.</b></td><td>for meat that is easy to cut and chew, say <i>tender</i>.</td></tr></table></div>
{sec(5, "Pronunciation lab: linking in instructions", "4 min")}
<p class="small" style="margin:.3mm 0">When a word ends in a consonant and the next word starts with a vowel, we join them: <i>chop_it_up</i> /tʃɑpɪˈtʌp/, <i>turn_it_over</i>. The stress goes on the particle: <i>chop it <b>UP</b>, turn it <b>O</b>ver</i>.</p>
{audiocard(["17.2"])}
{sub("A", "Listen and repeat. Then give your teacher three instructions for making a cup of coffee or tea.", "4 min", "17.2")}
<p style="margin:.3mm 0;font-size:8.8pt;line-height:1.55">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S172))}</p>""",
    23, """<ol><li>A: also <i>peel</i> (remove the skin) and <i>preheat</i> (heat the oven before cooking): <i>Preheat the oven to 350°F.</i></li>
<li>B: <i>sour</i> = acid, like lemon; <i>bitter</i> = strong and unpleasant, like black coffee or dark chocolate. Ask: <i>What food don't you eat because of its flavor? I find it too…</i></li></ol>""")

    # Page 6 - Practice
    gw = ["set", "burned", "raw", "fresh", "diet", "delicious"]
    g = [A(w, "min-width:15mm") for w in gw]
    jn = [("The water boils. Add the pasta. (as soon as)", "As soon as the water boils, add the pasta."), ("Bake the cake. It's golden. (until)", "Bake the cake until it's golden."),
          ("The rice is cooking. Make the salad. (while)", "While the rice is cooking, make the salad."), ("Wash your hands. Start cooking. (before)", "Wash your hands before you start cooking."),
          ("The oil is hot. Add the onions. (once)", "Once the oil is hot, add the onions.")]
    jnl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in jn)
    b.page(f"""{sec(6, "Practice", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Danny tells his mom about the breakfast. Complete his message with the words from the box. There are two extra words.", "4 min")}
<div class="bank">burned · delicious · diet · fresh · medium · raw · set · tender</div></div>{img('D', 30, 20)}</div>
<div class="box" style="line-height:1.95;font-size:9pt"><b>From: Danny · To: Mom</b><br>Mom, the breakfast was a success! I got up at six and {g[0]} the table for twenty people. The first pancake was a disaster, of course: I {g[1]} the outside, and the middle was still {g[2]}. I ate it before anyone saw it! The rest were perfect, though. Mrs. Lima bought {g[3]} strawberries at the market, and Bruno made scrambled eggs. One guest is on a {g[4]}, so she just had fruit and coffee. And Mrs. Lima said the pancakes were {g[5]} and asked for the recipe! Photo attached. Love, Danny</div>
{sub("B", "Join the instructions with the word in brackets.", "4 min")}
<ol style="line-height:1.55;font-size:8.8pt;margin:0">{jnl}</ol>""",
    24, """<ol><li>A: the extra words are <i>medium</i> and <i>tender</i> (both for meat). <i>Raw</i> = not cooked; <i>set the table</i> = put plates, glasses and forks on it.</li>
<li>B: accept the time clause in either position; check the comma when it comes first.</li></ol>""")

    # Page 7 - Speaking
    b.page(f"""{sec(7, "Speaking: how do you make it?", "12 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>giving steps</th><th>tips and warnings</th><th>checking</th><th>taste</th></tr>
<tr><td><i>First of all… · After that… · As soon as… · Leave it until…</i></td><td><i>Make sure you… · Be careful not to… · The secret is…</i></td><td><i>How long do I…? · What do I do after…? · Got it.</i></td><td><i>It tastes a bit… · I find it too… · It isn't … enough.</i></td></tr></table></div>
{sub("A", "Role-play: give a recipe. Choose a dish from any country that you can cook (or would like to learn). Explain it to your teacher step by step, with at least three time words. Your teacher asks questions. Then change roles.", "6 min")}
<div style="display:flex;gap:4mm;font-size:8.6pt"><div style="flex:1"><b>Dish:</b>{lines(1)}</div><div style="flex:2"><b>Ingredients:</b>{lines(1)}</div></div>
<p style="margin:.3mm 0;font-size:8.6pt">{R("Teacher's turn: explain a simple international dish (for example, an omelet, guacamole or a stir-fry). Use until, while and as soon as. Let the student ask checking questions.") if T else ""}</p>
{sub("B", "Long turn. Prepare for one minute, then talk for two minutes about an unusual dish you have tried, at home or abroad.", "4 min")}
<ul style="line-height:1.45;font-size:8.9pt;margin:0"><li>where you tried it and who you were with</li><li>what was in it and how it was cooked</li><li>how it tasted (sweet, spicy, bland, rich…)</li><li>would you eat it again?</li></ul>
{sub("C", "Talking point. Discuss with your teacher.", "2 min")}
<ol style="line-height:1.5;font-size:8.9pt;margin:0"><li>Should everyone learn to cook at school? Why or why not?</li><li>Video recipes or written recipes: which do you prefer, and why?</li></ol>""",
    30, """<ol><li>A: before the student starts, give one minute to plan. Ask checking questions (<i>How long do I fry it? What do I do after that?</i>) to push for time clauses.</li>
<li>B: don't interrupt; note mistakes for the error log (page 8), especially <i>will</i> after <i>when / as soon as</i>.</li></ol>""")

    # Page 8 - Wrap-up
    cd = ["I can follow a recipe given step by step.", "I can give instructions with when, as soon as, until and while.", "I can describe how food tastes."]
    cdr = "".join(f"<tr><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for s in cd)
    b.page(f"""{sec(8, "Wrap-up and homework", "4 min")}
{sub("A", "Can-do check", "1 min")}
<table class="ck" style="font-size:8.6pt"><tr><th>In English…</th><th style="width:16mm">Easy!</th><th style="width:16mm">Sometimes</th><th style="width:16mm">Not yet</th></tr>{cdr}</table>
{sub("B", "My language notes. Write three corrections from today's class.", "2 min")}
<div style="display:flex;gap:5mm;font-size:8.6pt"><div style="flex:1"><b>I said…</b>{lines(3)}</div><div style="flex:1"><b>Better:</b>{lines(3)}</div></div>
{sub("C", "Homework: writing (100–150 words)", "1 min")}
<p style="margin:.3mm 0"><b>A recipe for a blog.</b> Write a recipe for a dish you like. Give a short introduction, the ingredients and the steps. Read Tom's recipe first.</p>
<div class="box" style="font-size:8.6pt;line-height:1.4;margin:.5mm 0"><b>Tom's quick guacamole</b><br><i>My roommates always ask me to make this for movie night. It takes ten minutes, and you don't need a stove! <b>You need:</b> 2 ripe avocados, half a red onion, 1 lime, a handful of cilantro, salt. <b>Steps:</b> First, chop the onion and the cilantro into very small pieces. Cut the avocados in half and take out the seed. Mash the avocados with a fork until they're smooth, but leave a few pieces. Squeeze the lime juice in as soon as you finish, so the avocado stays green. Then add the onion, the cilantro and a pinch of salt, and stir. Taste it before you serve it: if it's bland, add more salt or lime. Serve it with tortilla chips while it's fresh!</i></div>
<p class="small" style="margin:.3mm 0">Checklist: ☐ a short introduction &nbsp;☐ the ingredients with amounts &nbsp;☐ steps with three time words (when, until, as soon as…) &nbsp;☐ a tip &nbsp;☐ 100–150 words</p>
{lines(5)}""",
    30, """<ol><li>B (error log): during the lesson, note 3–5 real mistakes. Here, the student writes what they said and the better version; guide them to self-correct first.</li>
<li>C: check the cooking verbs and the present after the time words. <i>Mash</i> = press food until it's soft.</li></ol>""")

    script = "".join(f"<p style='margin:.5mm 0'><b>{l.split(': ', 1)[0]}:</b> {l.split(': ', 1)[1]}</p>" for l in S171)
    b.extra("Audio script", f"""
{sub("17.1", "Just like yours (natural and slow)")}
<div style="line-height:1.3;font-size:8.6pt">{script}</div>
{sub("17.2", "Repeat: linking in instructions")}
<p>{" · ".join(S172)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 17 - Cooking and eating")
