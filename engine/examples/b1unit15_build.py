# Speak! Progress B1 - Unit 15 "Food and drink" (all English) - B1 format (2026-11-09)
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Progress"
setup(band="B1 · UNIT 15", audio_json="audio_b1-unit-15.json", img_dir="img")


_r = json.load(open("roteiro.json"))["units"]["b1-unit-15"]
S151 = _r["15.1 Food around the world"].split("\n")
S152 = [x.split(": ", 1)[1] for x in _r["15.2 Repeat: tricky food words"].split("\n")]


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
    cover = cover_html(T, "LEVEL B1 · UNIT 15", "Food and drink", "Food vocabulary for travelers · <b>preferences: prefer… to, would rather, would prefer</b>",
                       [("YOU CAN", "name food and drink you see on menus abroad and say what you prefer"),
                        ("LANGUAGE", "pork · veal · poultry · seafood · herbs and spices · a mug of tea · aubergine / eggplant · I'd rather…"),
                        ("PRONUNCIATION", "tricky food words: vegetable, salmon, recipe, dessert")])
    groups = [("fruit", "cherry, lime, watermelon"), ("vegetables", "beet, cabbage, cauliflower, celery"), ("meat and poultry", "pork, turkey, veal"),
              ("fish and seafood", "lobster, mussels, trout"), ("herbs and spices", "garlic, rosemary, turmeric")]
    gt = "".join(f"<tr><td style='width:34mm'><b>{g}</b></td><td>{R(w) if T else ''}</td></tr>" for g, w in groups)
    b.page(f"""{sec(1, "Warm-up: what's on the menu?", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 35)}<div style="flex:1">
{sub("A", "Discuss with your teacher.", "3 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0"><li>Do you like visiting food markets when you travel? Why or why not?</li><li>What's the most unusual food you've ever tried?</li><li>Is it easy for you to read a menu in English? What's difficult?</li></ol></div></div>
{sub("B", "Put the words into the correct group. Then add one more word to each group.", "4 min")}
<div class="bank">beet · cabbage · cauliflower · celery · cherry · garlic · lime · lobster · mussels · pork · rosemary · trout · turkey · turmeric · veal · watermelon</div>
<table style="font-size:8.6pt;margin:.5mm 0">{gt}</table>
{sub("C", "Which of these foods do you eat often? Which have you never tried?", "1 min")}""",
    30, """<ol><li>A: let the student talk; note food words they need for the Vocabulary lab.</li>
<li>B: <i>beet</i> is American English (British: <i>beetroot</i>). Garlic is a vegetable but is used like a spice; accept it in either group. <i>Poultry</i> = birds we eat (chicken, turkey, duck). Ask for one more word per group: <i>grapes, peach / carrot, cucumber / lamb, duck / salmon, crab / basil, paprika</i>.</li>
<li>C: personalize; the Speaking on page 7 builds on this.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 60 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Discussion · food groups: fruit, vegetables, meat, seafood, herbs and spices</td><td>1</td></tr>
<tr><td>2 Listening</td><td>12 min</td><td>Podcast: Danny interviews Paulo, a travel photographer, about food around the world</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>8 min</td><td>Preferences: prefer… to, would prefer to, would rather (than)</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Talking about preferences (study at home)</td><td>4</td></tr>
<tr><td>4 Vocabulary lab + pronunciation</td><td>8 min</td><td>Meat and animals · drinks and containers · tricky food words</td><td>5</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Kate's blog: what customers prefer · odd one out</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Would you rather…? · long turn · talking point</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>4 min</td><td>Can-do · language notes · writing homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY</h4>The Linguahouse lesson is a vocabulary lesson (fruit and vegetables, meat, fish and seafood, herbs and spices, drinks and containers, US/UK food words) with no grammar. We kept the vocabulary, added a listening and a grammar point that fits the topic: preferences. Following the school's choice for food units, the focus is international food that students will see when they travel. In Danny's podcast <i>Gap Year Diaries</i> (B1 Unit 06), he interviews Paulo, Ana's brother and a travel photographer. Verified facts: <i>chapulines</i> are grasshoppers eaten as a snack in Oaxaca, Mexico, usually toasted and seasoned with garlic, lime and salt, sometimes with chili (Wikipedia, "Chapulines"; Food First, "Chapulines, Oaxaca's Edible Insects"). In American English, the fresh leaves of coriander are called <i>cilantro</i>; British English uses <i>coriander</i> (Merriam-Webster Learner's Dictionary; Collins). Kate (Sweet Kate Bakery, Chicago) writes about her customers in the Practice.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students say <i>I prefer coffee than tea</i> (<i>to</i>), <i>I'd rather to stay</i> (no <i>to</i>), <i>legumes</i> for vegetables, <i>I don't eat pig</i> (pork), and <i>take a coffee</i> (have a coffee). Pronunciation: <i>vegetable</i> in four syllables, the <i>l</i> in <i>salmon</i>, and <i>recipe</i> in two syllables.</div>
<div class="box"><h4>AUDIO</h4>Track 15.1 Food around the world (natural and slow) · Track 15.2 Repeat: tricky food words</div>""")

    # Page 2 - Listening
    gist = ["landscapes", "food", "people"]
    us = [("fries", "chips"), ("potato chips", "crisps"), ("eggplant", "aubergine"), ("zucchini", "courgette"), ("shrimp", "prawns"), ("cookies", "biscuits"), ("cilantro", "coriander")]
    ust = "".join(f"<tr><td>{a}</td><td>{A(u, 'min-width:28mm')}</td></tr>" for a, u in us)
    tf = [("Paulo prefers museums to markets.", "F (markets to museums)"), ("Chapulines are grasshoppers.", "T"),
          ("Paulo likes restaurants with menus in many languages.", "F (he'd rather eat where the locals eat)"), ("Veal comes from a calf.", "T"),
          ("In London, Paulo would rather have coffee.", "F (a mug of tea)")]
    tfl = [f'<li value="{i+1}">{s} {A(a, "min-width:9mm")}</li>' for i, (s, a) in enumerate(tf)]
    b.page(f"""{sec(2, "Listening: food around the world", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{audiocard(["15.1 · NATURAL", "15.1 · SLOW"])}
{sub("A", "Danny interviews Paulo, Ana's brother, on his podcast. Listen at natural speed. What does Paulo photograph the most?", "2 min", "15.1")}
<p style="margin:.3mm 0;font-size:8.9pt">{ch(gist, "food")}</p></div>{img('B', 40, 27)}</div>
<div style="display:flex;gap:4mm;align-items:flex-start"><div style="width:72mm">
{sub("B", "Listen again. Complete the British English words.", "3 min")}
<table style="font-size:8.6pt;margin:.5mm 0"><tr><th>American English</th><th>British English</th></tr>{ust}</table></div><div style="flex:1">
{sub("C", "True or false? Correct the false sentences.", "3 min")}
<ol style="font-size:8.6pt;line-height:1.5;margin:0;padding-left:4mm">{"".join(tfl)}</ol></div></div>
{sub("D", "Think about it. Discuss with your teacher.", "4 min")}
<ol style="line-height:1.4;font-size:8.8pt;margin:0"><li>Paulo says you learn more about a country at a fruit stall than in a guidebook. Do you agree?</li><li>"I'd rather eat where the locals eat." How do you find good local food when you travel?</li></ol>
<div class="box sand" style="margin-top:1mm"><h4>NOTICE: USEFUL CHUNKS</h4><i>Thanks for having me. · to be honest · Not bad at all! · I have one simple rule… · by the way · It's like a different language!</i></div>""",
    28, """<ol><li>B: this book uses American English; students should recognize the British words, especially on menus in the UK, Ireland and Australia. Students who say <i>chips</i> for fries are not wrong: it is British English.</li>
<li>C: elicit the preference structures in the corrections: <i>He prefers markets to museums. He'd rather eat where the locals eat.</i></li></ol>""")

    # Page 3 - Language focus
    fs = [("I prefer markets ___ museums.", "to"), ("I'd ___ have a steak, to be honest.", "rather"), ("I'd prefer ___ keep walking.", "to"),
          ("Would you ___ try something new or order something safe?", "rather"), ("I'd rather eat where the locals ___.", "eat")]
    fsl = "".join(f"<li><i>{s.replace('___', A(a, 'min-width:14mm'))}</i></li>" for s, a in fs)
    b.page(f"""{sec(3, "Language focus: talking about preferences", "8 min")}
{sub("A", "Complete Paulo's and Danny's sentences from the podcast. Then listen again and check.", "2 min")}
<ol style="line-height:1.85;font-size:8.9pt;margin:0">{fsl}</ol>
{sub("B", "Complete the rules. Choose.", "3 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0"><li><i>I prefer markets to museums</i> is about {ch(["what I like in general", "one specific situation"], "what I like in general")}.</li>
<li>After <i>prefer A</i>, we use {ch(["to", "than"], "to")} before <i>B</i>.</li>
<li>After <i>would rather</i>, we use the verb {ch(["with to", "without to"], "without to")}: <i>I'd rather have…</i></li>
<li>After <i>would prefer</i>, we use the verb {ch(["with to", "without to"], "with to")}: <i>I'd prefer to keep walking.</i></li>
<li>The negative of <i>I'd rather</i> is {ch(["I'd rather not", "I'd rather don't"], "I'd rather not")}.</li></ol>
{sub("C", "Correct or incorrect? Choose.", "3 min")}
<ol style="line-height:1.6;font-size:8.9pt;margin:0"><li>I prefer tea than coffee. {ch(["correct", "incorrect"], "incorrect")} {R("→ tea to coffee") if T else ""}</li><li>I'd rather cook at home than eat out tonight. {ch(["correct", "incorrect"], "correct")}</li><li>I'd prefer not to eat octopus. {ch(["correct", "incorrect"], "correct")}</li><li>She'd rather to sit outside. {ch(["correct", "incorrect"], "incorrect")} {R("→ She'd rather sit outside.") if T else ""}</li></ol>
<div class="box sand"><h4>RULE</h4><b>prefer A to B</b> = in general (<i>I prefer fish to meat</i>). <b>would prefer + to + verb</b> and <b>would rather + verb</b> (no <i>to</i>) = now, in a specific situation (<i>Tonight I'd rather stay in</i>). Compare two actions with <b>would rather A than B</b>. Negatives: <b>I'd prefer not to… / I'd rather not…</b> More on the next page: <b>Grammar reference</b>.</div>""",
    27, """<ol><li>A: write two columns on the board: <i>prefer + to</i> / <i>rather + base form</i>, and put each example in its column.</li>
<li>B: <i>'d</i> = <i>would</i>. With <i>prefer</i> + two verbs in general, use -ing: <i>I prefer cooking to eating out.</i></li>
<li>C: quick drill: give two options (<i>beach / mountains</i>); the student answers with <i>prefer… to</i>, then <i>this weekend, I'd rather…</i>.</li></ol>""")

    grammar_ref.preferences(b)

    # Page 5 - Vocabulary lab
    ma = [("pork", "a pig"), ("beef", "a cow"), ("veal", "a calf (a young cow)"), ("lamb", "a young sheep"), ("poultry", "birds, e.g. chickens and turkeys")]
    mal = "".join(f"<li><b>{m}</b> {A(a, 'min-width:40mm')}</li>" for m, a in ma)
    dk = [("tea", "a mug"), ("beer (in a pub)", "a pint glass"), ("wine", "a wine glass"), ("tequila", "a shot glass"), ("espresso", "a cup")]
    dkl = "".join(f"<li>{d} {A(c, 'min-width:22mm')}</li>" for d, c in dk)
    b.page(f"""{sec(4, "Vocabulary lab: meat and drinks", "4 min")}
<div style="display:flex;gap:4mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Which animal does the meat come from?", "2 min")}
<div class="bank" style="font-size:8.3pt">a calf (a young cow) · a cow · a pig · a young sheep · birds, e.g. chickens and turkeys</div>
<ol style="line-height:1.6;font-size:8.6pt;margin:0">{mal}</ol></div><div style="width:68mm">
{sub("B", "Which container? Choose from the box.", "2 min")}
<div style="display:flex;gap:2mm;align-items:flex-start"><div style="flex:1"><div class="bank" style="font-size:8.3pt">a cup · a mug · a pint glass · a shot glass · a wine glass</div>
<ol style="line-height:1.6;font-size:8.6pt;margin:0">{dkl}</ol></div>{img('D', 22, 22)}</div></div></div>
<div class="box sand"><h4>WATCH OUT: FALSE FRIENDS AND WORD CHOICE</h4>
<table style="margin:0;font-size:8.3pt"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>I eat a lot of legumes.</td><td><b>I eat a lot of vegetables.</b></td><td><i>legumes</i> = beans, lentils and peas only.</td></tr>
<tr><td>I don't eat pig.</td><td><b>I don't eat pork.</b></td><td>for the meat, use <i>pork, beef, veal</i>; <i>pig, cow, calf</i> are the animals.</td></tr>
<tr><td>Let's take a coffee.</td><td><b>Let's have / get a coffee.</b></td><td>we <i>have</i> food and drinks; <i>take</i> is for medicine.</td></tr>
<tr><td>The mass is ready.</td><td><b>The pasta / The dough is ready.</b></td><td><i>pasta</i> = spaghetti, etc.; <i>dough</i> = for bread and pizza.</td></tr></table></div>
{sec(5, "Pronunciation lab: tricky food words", "4 min")}
<p class="small" style="margin:.3mm 0">Some food words have silent letters or fewer syllables than you think: <i>vegetable</i> /ˈvedʒtəbəl/ (3 syllables), <i>chocolate</i> /ˈtʃɑklət/ (2), <i>salmon</i> /ˈsæmən/ (silent <i>l</i>), <i>recipe</i> /ˈresəpi/, <i>herbs</i> /ɜrbz/ (silent <i>h</i> in American English), <i>dessert</i> /dɪˈzɜrt/ (not <i>desert</i>).</p>
{audiocard(["15.2"])}
{sub("A", "Listen and repeat. Then tell your teacher which three words are the most difficult for you, and use them in a sentence.", "4 min", "15.2")}
<p style="margin:.3mm 0;font-size:8.8pt;line-height:1.55">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S152))}</p>""",
    25, """<ol><li>A: <i>chicken, turkey, duck</i> have the same name for the animal and the meat; <i>lamb</i> is both the young animal and the meat. Other drinking containers: <i>a can, a bottle, a jug</i>.</li>
<li>Pronunciation: also <i>lettuce</i> /ˈletɪs/, <i>steak</i> rhymes with <i>make</i>, <i>oregano</i> /əˈreɡənoʊ/ in American English.</li></ol>""")

    # Page 6 - Practice
    pc = [(["prefer", "would rather"], "prefer"), (["to", "than"], "to"), (["try", "to try"], "try"), (["than", "to"], "than"),
          (["to eat", "eat"], "to eat"), (["not", "don't"], "not"), (["having", "have"], "having")]
    p = [ch(o, a) for o, a in pc]
    oo = [("cherry · raspberry · celery · strawberry", "celery", "the others are fruit"), ("pork · veal · octopus · beef", "octopus", "the others are meat"),
          ("oregano · peas · rosemary · basil", "peas", "the others are herbs"), ("cod · salmon · trout · lamb", "lamb", "the others are fish"),
          ("crab · lettuce · lobster · mussels", "lettuce", "the others are seafood"), ("chicken · turkey · duck · pork", "pork", "the others are poultry")]
    ool = "".join(f"<li>{w} {A(x + ' – ' + why, 'min-width:44mm')}</li>" for w, x, why in oo)
    b.page(f"""{sec(6, "Practice", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Kate (Sweet Kate Bakery, Chicago) writes about her customers on her blog. Choose the correct words.", "4 min")}</div>{img('C', 30, 20)}</div>
<div class="box" style="line-height:1.95;font-size:9pt"><b>Sweet Kate's blog · What do my customers prefer?</b><br>Last month I asked my customers about their food habits. Here's what I learned! Most people {p[0]} sweet food in the morning. They prefer cinnamon rolls {p[1]} sandwiches, and that's good news for me. On weekends, many customers would rather {p[2]} something new {p[3]} order the same thing again, so I'm baking a new cake every Saturday. A lot of young customers told me they'd prefer {p[4]} less sugar. One man said, "I'd rather {p[5]} talk about my diet, thank you!" And my favorite answer? A woman who said she prefers {p[6]} breakfast here to cooking at home. Me too!</div>
{sub("B", "Odd one out. Cross out the word that doesn't belong. Say what the others have in common.", "4 min")}
<ol style="line-height:1.5;font-size:8.8pt;margin:0">{ool}</ol>""",
    26, """<ol><li>A: after correction, ask: <i>Which sentences are about habits in general, and which are about a specific situation?</i></li>
<li>B: in 6, <i>pork</i> is meat, but not poultry (birds). Ask the student to make a new line for you to solve.</li></ol>""")

    # Page 7 - Speaking
    wr = ["eat street food or eat in a fancy restaurant?", "try grasshoppers or octopus?", "cook dinner for friends or take them out?",
          "give up coffee or give up chocolate?", "eat spicy food every day or eat no salt at all?", "have breakfast in a café or in bed?"]
    wrl = "".join(f"<li>Would you rather {x}</li>" for x in wr)
    b.page(f"""{sec(7, "Speaking: would you rather…?", "12 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>asking</th><th>in general</th><th>this time</th><th>giving reasons</th></tr>
<tr><td><i>Which do you prefer…? · Would you rather…? · Would you prefer…?</i></td><td><i>I prefer… to… · I'm not a big fan of… · I can't stand…</i></td><td><i>I'd rather… than… · I'd prefer to… · I'd rather not…</i></td><td><i>The thing is… · That's because… · To be honest…</i></td></tr></table></div>
{sub("A", "Would you rather…? Take turns. Ask your teacher a question, listen to the answer, then answer it yourself. Always give a reason.", "5 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0;columns:2">{wrl}</ol>
{sub("B", "Long turn. Prepare for one minute, then talk for two minutes about the food of a country you've visited or would love to visit.", "5 min")}
<ul style="line-height:1.45;font-size:8.9pt;margin:0"><li>what people eat and drink there (meat, seafood, herbs and spices…)</li><li>a dish you tried or would like to try</li><li>something you would rather not eat there, and why</li><li>how it compares with food at home</li></ul>
{sub("C", "Talking point. Discuss with your teacher.", "2 min")}
<ol style="line-height:1.5;font-size:8.9pt;margin:0"><li>Do you believe "we are what we eat"?</li><li>What food or drink do you avoid? Why?</li></ol>""",
    30, """<ol><li>A: answer first to model a full answer with a reason (<i>I'd rather eat street food, because…</i>). Push for <i>than</i> in the second part.</li>
<li>B: don't interrupt; note mistakes for the error log (page 8), especially <i>prefer… than</i> and <i>rather to</i>. If the student hasn't traveled, they choose a country they'd like to visit.</li></ol>""")

    # Page 8 - Wrap-up
    cd = ["I can name food and drink I see on menus abroad.", "I can talk about my preferences (prefer… to, I'd rather…).",
          "I can understand some differences between American and British food words."]
    cdr = "".join(f"<tr><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for s in cd)
    b.page(f"""{sec(8, "Wrap-up and homework", "4 min")}
{sub("A", "Can-do check", "1 min")}
<table class="ck" style="font-size:8.6pt"><tr><th>In English…</th><th style="width:16mm">Easy!</th><th style="width:16mm">Sometimes</th><th style="width:16mm">Not yet</th></tr>{cdr}</table>
{sub("B", "My language notes. Write three corrections from today's class.", "2 min")}
<div style="display:flex;gap:5mm;font-size:8.6pt"><div style="flex:1"><b>I said…</b>{lines(3)}</div><div style="flex:1"><b>Better:</b>{lines(3)}</div></div>
{sub("C", "Homework: writing (100–150 words)", "1 min")}
<p style="margin:.3mm 0"><b>A travel blog post: How I eat when I travel.</b> Write about your food habits and preferences when you travel. Read Paulo's post first.</p>
<div class="box" style="font-size:8.6pt;line-height:1.4;margin:.5mm 0"><b>Paulo's travel blog · My three food rules</b><br><i>People always ask me how I choose where to eat abroad. Here are my rules. First, I prefer markets to restaurants. At a market, I can try a little of everything, and it's much cheaper. Second, I'd rather eat where the locals eat. If the menu has photos and five languages, I keep walking. Third, I always try one new thing, even if it looks strange. I'm not a big fan of seafood, but I tried mussels in Lisbon and loved them. There are a few things I'd rather not eat again, but that's part of the fun! Oh, and I always carry a little box of spices, because hotel food can be very boring. What about you?</i></div>
<p class="small" style="margin:.3mm 0">Checklist: ☐ two or three food habits &nbsp;☐ <i>prefer… to</i> and <i>I'd rather…</i> &nbsp;☐ one food you loved and one you'd rather not eat again &nbsp;☐ a question for your readers &nbsp;☐ 100–150 words</p>
{lines(5)}""",
    30, """<ol><li>B (error log): during the lesson, note 3–5 real mistakes. Here, the student writes what they said and the better version; guide them to self-correct first.</li>
<li>C: check the preference structures and food vocabulary (<i>seafood, herbs, spices, poultry</i>).</li></ol>""")

    script = "".join(f"<p style='margin:.5mm 0'><b>{l.split(': ', 1)[0]}:</b> {l.split(': ', 1)[1]}</p>" for l in S151)
    b.extra("Audio script", f"""
{sub("15.1", "Food around the world (natural and slow)")}
<div style="line-height:1.3;font-size:8.6pt">{script}</div>
{sub("15.2", "Repeat: tricky food words")}
<p>{" · ".join(S152)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 15 - Food and drink")
