# Speak! Progress B1 - Unit 15 "Food and drink" (all English) - lean B1 format (rebuilt 2026-11-19)
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
setup(band="B1 · UNIT 15", audio_json="audio_b1-unit-15.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-15"]
S151 = _r["15.1 Food around the world"].split("\n")
S152 = [x.split(": ", 1)[1] for x in _r["15.2 Repeat: tricky food words"].split("\n")]
STORY = 'The Linguahouse lesson is a vocabulary lesson (fruit and vegetables, meat, fish and seafood, herbs and spices, drinks and containers, US/UK food words) with no grammar. We kept the vocabulary, added a listening and a grammar point that fits the topic: preferences. Following the school\'s choice for food units, the focus is international food that students will see when they travel. In Danny\'s podcast <i>Gap Year Diaries</i> (B1 Unit 06), he interviews Paulo, Ana\'s brother and a travel photographer. Verified facts: <i>chapulines</i> are grasshoppers eaten as a snack in Oaxaca, Mexico, usually toasted and seasoned with garlic, lime and salt, sometimes with chili (Wikipedia, "Chapulines"; Food First, "Chapulines, Oaxaca\'s Edible Insects"). In American English, the fresh leaves of coriander are called <i>cilantro</i>; British English uses <i>coriander</i> (Merriam-Webster Learner\'s Dictionary; Collins). Kate (Sweet Kate Bakery, Chicago) writes about her customers in the homework.'


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'

    # 1 Warm-up
    cover = cover_html(T, "LEVEL B1 · UNIT 15", "Food and drink", "Food vocabulary for travelers · <b>preferences: prefer… to, would rather, would prefer</b>",
                       [("YOU CAN", "name food and drink you see on menus abroad and say what you prefer"),
                        ("LANGUAGE", "pork · veal · poultry · seafood · herbs and spices · a mug of tea · aubergine / eggplant · I'd rather…"),
                        ("PRONUNCIATION", "tricky food words: vegetable, salmon, recipe, dessert")])
    groups = [("fruit", "cherry, lime"), ("vegetables", "cabbage, celery"), ("meat and poultry", "pork, turkey"), ("fish and seafood", "lobster, trout"), ("herbs and spices", "rosemary, turmeric")]
    gt = "".join(f"<tr><td style='width:34mm'><b>{g}</b></td><td>{R(w) if T else ''}</td></tr>" for g, w in groups)
    b.page(f"""{sec(1, "Warm-up: what's on the menu?", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["Do you like visiting food markets when you travel? Why?", "What's the most unusual food you've ever tried?", "Is it easy for you to read a menu in English? What's difficult?"], "START TALKING")}</div></div>
{sub("A", "Put the words into the correct group.", "3 min")}
<div class="bank">cabbage · celery · cherry · lime · lobster · pork · rosemary · trout · turkey · turmeric</div>
<table style="font-size:8.6pt;margin:.5mm 0">{gt}</table>
{talk(["Add one more word to each group.", "Which of these foods do you eat often? Which have you never tried?"], "USE THE WORDS")}""",
    26, """<ol><li>Top box (4 minutes): note food words the student needs.</li>
<li>A: <i>poultry</i> = birds we eat (chicken, turkey, duck). More words: <i>grapes, carrot, lamb, salmon, basil, paprika</i>.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Podcast: Paulo talks about food around the world · US/UK words · Talk about it", "Preferences: prefer… to, would prefer to, would rather (than)",
                      "Complete Paulo's sentences · choose the rule · Use it (oral)", "Functional language · tricky food words (15.2) · Would you rather…?",
                      "Kate's blog: what customers prefer · meat and animals · word choice · writing"),
        STORY,
        "Students say <i>I prefer coffee than tea</i> (<i>to</i>), <i>I'd rather to stay</i> (no <i>to</i>), <i>legumes</i> for vegetables, <i>I don't eat pig</i> (pork), and <i>take a coffee</i> (have a coffee). Pronunciation: <i>vegetable</i> in four syllables, the <i>l</i> in <i>salmon</i>, and <i>recipe</i> in two syllables.",
        "Track 15.1 Food around the world (natural and slow) · Track 15.2 Repeat: tricky food words"))

    # 2 Listening
    gist = ["landscapes", "food", "people"]
    us = [("fries", "chips"), ("potato chips", "crisps"), ("eggplant", "aubergine"), ("zucchini", "courgette"), ("shrimp", "prawns"), ("cilantro", "coriander")]
    ust = "".join(f"<tr><td>{a}</td><td>{A(u, 'min-width:28mm')}</td></tr>" for a, u in us)
    b.page(f"""{sec(2, "Listening: food around the world", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{audiocard(["15.1 · NATURAL", "15.1 · SLOW"])}
{sub("A", "Danny interviews Paulo, Ana's brother, on his podcast. Listen. What does Paulo photograph the most?", "2 min", "15.1")}
<p style="margin:.3mm 0;font-size:8.9pt">{ch(gist, "food")}</p></div>{img('B', 40, 27)}</div>
{sub("B", "Listen again. Complete the British English words.", "4 min")}
<table style="font-size:8.6pt;margin:.5mm 0;width:80mm"><tr><th>American English</th><th>British English</th></tr>{ust}</table>
{talk(["Paulo says you learn more about a country at a fruit stall than in a guidebook. Do you agree?", "&ldquo;I'd rather eat where the locals eat.&rdquo; How do you find good local food when you travel?", "What's the strangest thing you've ever eaten?"])}""",
    26, """<ol><li>A–B: 6 minutes. This book uses American English; students should recognize the British words, especially on menus in the UK, Ireland and Australia.</li>
<li>Talk about it: 6 minutes. Elicit preference structures: <i>He prefers markets to museums.</i></li></ol>""")

    # 3 Grammar reference
    lean.grammar_in_class(b, grammar_ref.preferences)

    # 4 Practice
    fs = [("I prefer markets ___ museums.", "to"), ("I'd ___ have a steak, to be honest.", "rather"), ("I'd prefer ___ keep walking.", "to"), ("Would you ___ try something new or order something safe?", "rather")]
    fsl = "".join(f"<li><i>{s.replace('___', A(a, 'min-width:14mm'))}</i></li>" for s, a in fs)
    use = ["Coffee or tea? Answer with <i>I prefer… to…</i>", "Tonight: pizza or sushi? Answer with <i>I'd rather… than…</i>", "Beach or mountains for your next vacation? Answer with <i>I'd prefer to…</i>",
           "Tell me something you'd rather not eat.", "Ask your teacher three questions with <i>Would you rather…?</i>"]
    b.page(f"""{sec(4, "Practice: talking about preferences", "10 min")}
{sub("A", "Complete Paulo's and Danny's sentences from the podcast.", "2 min")}
<ol style="line-height:1.85;font-size:8.9pt;margin:0">{fsl}</ol>
{sub("B", "Choose.", "2 min")}
<p style="margin:.3mm 0;font-size:8.9pt;line-height:1.7">I prefer tea {ch(["to", "than"], "to")} coffee. &nbsp;·&nbsp; She'd rather {ch(["sit", "to sit"], "sit")} outside. &nbsp;·&nbsp; I'd rather {ch(["not", "don't"], "not")} try it.</p>
<div class="box sand"><h4>RULE</h4><b>prefer A to B</b> = in general · <b>would prefer + to + verb</b> and <b>would rather + verb</b> (no <i>to</i>) = now, in a specific situation · <b>would rather A than B</b> · negatives: <b>I'd prefer not to… / I'd rather not…</b> See the <b>Grammar reference</b> on page 3.</div>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    24, """<ol><li>A–B: 4 minutes. Two columns on the board: <i>prefer + to</i> / <i>rather + base form</i>.</li>
<li>Use it: 6 minutes, all oral. Push for a reason after each answer.</li></ol>""")

    # 5 Speaking
    wr = ["eat street food or eat in a fancy restaurant?", "try grasshoppers or octopus?", "cook dinner for friends or take them out?",
          "give up coffee or give up chocolate?", "eat spicy food every day or eat no salt at all?", "have breakfast in a café or in bed?"]
    wrl = "".join(f"<li>Would you rather {x}</li>" for x in wr)
    b.page(f"""{sec(5, "Speaking: would you rather…?", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>asking</th><th>in general</th><th>this time</th><th>giving reasons</th></tr>
<tr><td><i>Which do you prefer…? · Would you rather…? · Would you prefer…?</i></td><td><i>I prefer… to… · I'm not a big fan of… · I can't stand…</i></td><td><i>I'd rather… than… · I'd prefer to… · I'd rather not…</i></td><td><i>The thing is… · That's because… · To be honest…</i></td></tr></table></div>
{audiocard(["15.2"])}
{sub("A", "Tricky food words. Listen and repeat: vegetable (3 syllables) · salmon (silent l) · recipe · dessert.", "4 min", "15.2")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.55">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S152))}</p>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("B", "Would you rather…? Take turns. Ask your teacher, listen, then answer yourself. Always give a reason.", "10 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0;columns:2">{wrl}</ol></div>{img('D', 28, 28)}</div>
{talk(["Describe the food of a country you've visited or would love to visit.", "Do you believe &ldquo;we are what we eat&rdquo;?"])}""",
    28, """<ol><li>A: <i>herbs</i> has a silent h in American English. B: answer first to model a full answer with a reason. Push for <i>than</i> in the second part.</li>
<li>Last 3 minutes: wrap-up (two corrections and <i>Can you talk about your preferences?</i>).</li></ol>""")

    # H Homework
    pc = [(["prefer", "would rather"], "prefer"), (["to", "than"], "to"), (["try", "to try"], "try"), (["than", "to"], "than"), (["not", "don't"], "not")]
    p = [ch(o, a) for o, a in pc]
    ma = [("pork", "a pig"), ("beef", "a cow"), ("veal", "a calf")]
    mal = " &nbsp;·&nbsp; ".join(f"<b>{m}</b> {A(a, 'min-width:16mm')}" for m, a in ma)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Kate writes about her customers on her blog. Choose the correct words.", "")}</div>{img('C', 28, 18)}</div>
<div class="box" style="line-height:1.8;font-size:8.8pt;margin:.5mm 0"><b>Sweet Kate's blog · What do my customers prefer?</b><br>Most people {p[0]} sweet food in the morning. They prefer cinnamon rolls {p[1]} sandwiches, and that's good news for me. On weekends, many customers would rather {p[2]} something new {p[3]} order the same thing again. One man said, "I'd rather {p[4]} talk about my diet, thank you!"</div>
{sub("B", "Which animal does the meat come from?", "")}
<p style="margin:.3mm 0;line-height:1.9;font-size:8.6pt">{mal}</p>
{lean.watch_out([("I eat a lot of legumes.", "I eat a lot of vegetables.", "<i>legumes</i> = beans, lentils and peas only."), ("I don't eat pig.", "I don't eat pork.", "<i>pork, beef, veal</i> are the meat."), ("Let's take a coffee.", "Let's have / get a coffee.", "we <i>have</i> food and drinks.")])}
{lean.writing_task(sub, "A travel blog post: How I eat when I travel. Write about your food habits and preferences abroad.", "When I travel, I prefer… to… I'd rather eat where… I always try…", ["prefer… to", "I'd rather", "one food you loved", "100–150 words"], "I can name food on menus abroad and say what I prefer.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class (lamb is the young animal and the meat). When you correct the writing, check <i>prefer… to</i> and <i>rather</i> + base form.</p>""")

    script = "".join(f"<p style='margin:.5mm 0'><b>{l.split(': ', 1)[0]}:</b> {l.split(': ', 1)[1]}</p>" for l in S151)
    b.extra("Audio script", f"""
{sub("15.1", "Food around the world (natural and slow)")}
<div style="line-height:1.3;font-size:8.6pt">{script}</div>
{sub("15.2", "Repeat: tricky food words")}
<p>{" · ".join(S152)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 15 - Food and drink")
