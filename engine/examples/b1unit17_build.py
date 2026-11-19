# Speak! Progress B1 - Unit 17 "Cooking and eating" (all English) - lean B1 format (rebuilt 2026-11-19)
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

    # 1 Warm-up
    cover = cover_html(T, "LEVEL B1 · UNIT 17", "Cooking and eating", "Recipes, kitchen words and taste · <b>time clauses: when, as soon as, until, while</b>",
                       [("YOU CAN", "follow and give step-by-step cooking instructions and describe how food tastes"),
                        ("LANGUAGE", "a frying pan · a saucepan · chop · stir · squeeze · bland · greasy · as soon as it boils · until it's golden"),
                        ("PRONUNCIATION", "linking in instructions: chop it up, turn it over")])
    ut = [("a flat pan with a long handle, for frying", "a frying pan"), ("a deep round pan with a lid, for boiling and sauces", "a saucepan"),
          ("a large round pan for stir-frying", "a wok"), ("the hot box where you bake and roast food", "an oven"),
          ("the top part with burners where you put pans", "a stove"), ("a big spoon, also a unit of measure (tbsp)", "a tablespoon")]
    utl = [f'<li value="{i+1}">{d} {A(w, "min-width:22mm")}</li>' for i, (d, w) in enumerate(ut)]
    b.page(f"""{sec(1, "Warm-up: in the kitchen", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["Who does most of the cooking in your home?", "Do you follow recipes exactly, or do you prefer to improvise?", "What's the best thing you can cook?"], "START TALKING")}</div></div>
{sub("A", "Kitchen words. Write the words from the box next to the definitions.", "3 min")}
<div class="bank">an oven · a frying pan · a saucepan · a stove · a tablespoon · a wok</div>
<div style="font-size:8.6pt">{twocol(utl, 3)}</div>
{talk(["Which of these do you use every week? Which do you have but rarely use?", "What do you usually cook in a frying pan? And in the oven?"], "USE THE WORDS")}""",
    26, """<ol><li>Top box: <i>improvise</i> = cook without a recipe, using what you have.</li>
<li>A: <i>stove</i> is American English (British: <i>cooker</i> or <i>hob</i>). US recipes measure in <i>cups</i> and use °F (350 °F ≈ 180 °C).</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Phone call: Rita gives Danny her pancake recipe · amounts · Talk about it", "Time clauses: when, as soon as, once, until, while, before",
                      "Complete Rita's instructions · choose · Use it (oral)", "Functional language · linking (17.2) · give a recipe",
                      "Danny's message about the breakfast · taste adjectives · word choice · writing"),
        "The Linguahouse lesson is a vocabulary lesson (kitchen utensils, cooking verbs in two recipes, taste adjectives) with no listening and no grammar. We added a listening and a grammar point that fits recipes: time clauses. Following the school's choice for food units, the dishes are international. Danny wants to thank Mrs. Lima, who always cooks for the hostel, so he makes American pancakes for breakfast. He calls his mom, Rita (City Coffee, Chicago), for her recipe. The recipe uses US measures (cups, tablespoons). There are no factual claims in the unit beyond cooking instructions. In the homework, Danny tells Rita how the breakfast went.", 'Students use <i>will</i> after <i>when / as soon as</i> (<i>when it will boil</i>), say <i>I love kitchen</i> (cooking), <i>my mother is a great cooker</i> (cook), <i>turn on the fire</i> (the stove), and <i>the meat is soft</i> (tender). They also confuse <i>sour</i> and <i>bitter</i>.',
        "Track 17.1 Just like yours (natural and slow) · Track 17.2 Repeat: linking in instructions"))

    # 2 Listening
    gist = ["it's his mom's birthday", "to thank Mrs. Lima, who always cooks for the guests", "he wants to sell them at the hostel"]
    ing = [("flour", "2 cups"), ("sugar", "2 tablespoons"), ("baking powder", "2 teaspoons"), ("salt", "a pinch"), ("butter", "3 tablespoons"), ("eggs", "2"), ("milk", "almost 2 cups")]
    ingt = "".join(f"<tr><td>{n}</td><td>{A(q, 'min-width:24mm')}</td></tr>" for n, q in ing)
    b.page(f"""{sec(2, "Listening: just like yours", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{audiocard(["17.1 · NATURAL", "17.1 · SLOW"])}
{sub("A", "Danny calls his mom, Rita, in Chicago. Listen. Why is he making pancakes?", "2 min", "17.1")}
<p style="margin:.3mm 0;font-size:8.9pt">{ch(gist, gist[1])}</p></div>{img('B', 40, 27)}</div>
{sub("B", "Listen again. How much?", "4 min")}
<table style="font-size:8.6pt;margin:.5mm 0;width:70mm"><tr><th>ingredient</th><th>amount</th></tr>{ingt}</table>
{talk(["Why does Rita say &ldquo;A few lumps are fine&rdquo;?", "Is there a dish your family always makes &ldquo;just like&rdquo; someone else did?", "What's the first thing you learned to cook?"])}""",
    26, """<ol><li>A–B: 6 minutes. <i>Batter</i> = the liquid mix for pancakes and cakes; <i>flip</i> / <i>turn over</i> = turn upside down. A US cup is about 240 ml.</li>
<li>Talk about it: 6 minutes. 1: if you stir too much, the pancakes will be tough.</li></ol>""")

    # 3 Grammar reference
    lean.grammar_in_class(b, grammar_ref.time_clauses)

    # 4 Practice
    fs = [("___ it's cooling down, beat the eggs with the milk.", "While"), ("Stop ___ everything is combined.", "as soon as"),
          ("Wait ___ you see small bubbles on top.", "until"), ("Leave the batter for five minutes ___ you start cooking.", "before")]
    fsl = "".join(f"<li><i>{s.replace('___', A(a, 'min-width:16mm'))}</i></li>" for s, a in fs)
    use = ["How do you make coffee or tea? Use <i>when, as soon as, until</i>.", "What do you do as soon as you get home?", "What will you do when this class ends?",
           "Tell me something you do while you're cooking or commuting.", "Explain how to boil an egg, step by step."]
    b.page(f"""{sec(4, "Practice: time clauses", "10 min")}
{sub("A", "Complete Rita's instructions with as soon as, before, until or while.", "2 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0">{fsl}</ol>
{sub("B", "Choose.", "2 min")}
<p style="margin:.3mm 0;font-size:8.9pt;line-height:1.7">As soon as the water {ch(["boils", "will boil"], "boils")}, add the pasta. &nbsp;·&nbsp; Don't open the oven until the cake {ch(["rises", "doesn't rise"], "rises")}.</p>
<div class="box sand"><h4>RULE</h4><b>when</b> (at that time) · <b>as soon as / once</b> (immediately after) · <b>until</b> (up to that moment, then stop) · <b>while</b> (at the same time) · <b>before / after</b>. In instructions and for the future, use the <b>present</b> after these words, not <i>will</i>. See the <b>Grammar reference</b> on page 3.</div>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    24, """<ol><li>A–B: 4 minutes. Draw a timeline for <i>until</i> (an arrow that stops) and <i>while</i> (two parallel arrows). <i>Until</i> already means "not before": no negative.</li>
<li>Use it: 6 minutes, all oral. Correct <i>will</i> after <i>when / as soon as</i> every time.</li></ol>""")

    # 5 Speaking
    b.page(f"""{sec(5, "Speaking: how do you make it?", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>giving steps</th><th>tips and warnings</th><th>checking</th><th>taste</th></tr>
<tr><td><i>First of all… · After that… · As soon as… · Leave it until…</i></td><td><i>Make sure you… · Be careful not to… · The secret is…</i></td><td><i>How long do I…? · What do I do after…? · Got it.</i></td><td><i>It tastes a bit… · I find it too… · It isn't … enough.</i></td></tr></table></div>
{audiocard(["17.2"])}
{sub("A", "Linking. Listen and repeat: chop_it_up · turn_it_over. The particle is stressed.", "4 min", "17.2")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.55">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S172))}</p>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("B", "Give a recipe. Choose a dish from any country that you can cook (or would like to learn). Explain it step by step, with at least three time words. Your teacher asks questions. Then change roles.", "10 min")}
<p style="margin:.3mm 0;font-size:8.6pt">{R("Teacher's turn: explain a simple international dish (an omelet, guacamole or a stir-fry). Use until, while and as soon as. Let the student ask checking questions.") if T else ""}</p></div>{img('D', 32, 24)}</div>
{talk(["Tell me about an unusual dish you've tried, at home or abroad. How did it taste?", "Should everyone learn to cook at school? Why?"])}""",
    28, """<ol><li>B: give one minute to plan. Ask checking questions (<i>How long do I fry it? What do I do after that?</i>) to push for time clauses.</li>
<li>Last 3 minutes: wrap-up (two corrections and <i>Can you give instructions with time clauses?</i>).</li></ol>""")

    # H Homework
    gw = ["set", "burned", "raw", "fresh", "diet", "delicious"]
    g = [A(w, "min-width:15mm") for w in gw]
    ta = [("lemons, vinegar", "sour"), ("black coffee without sugar", "bitter"), ("fries, fried chicken", "greasy")]
    tal = " &nbsp;·&nbsp; ".join(f"{f} {A(a, 'min-width:13mm')}" for f, a in ta)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Danny tells his mom about the breakfast. Complete with burned, delicious, diet, fresh, raw, set.", "")}</div>{img('C', 28, 18)}</div>
<div class="box" style="line-height:1.8;font-size:8.8pt;margin:.5mm 0">Mom, the breakfast was a success! I got up at six and {g[0]} the table for twenty people. The first pancake was a disaster, of course: I {g[1]} the outside, and the middle was still {g[2]}. Mrs. Lima bought {g[3]} strawberries at the market. One guest is on a {g[4]}, so she just had fruit. And Mrs. Lima said the pancakes were {g[5]}! Love, Danny</div>
{sub("B", "How does it taste? Write bitter, greasy or sour.", "")}
<p style="margin:.3mm 0;line-height:1.9;font-size:8.6pt">{tal}</p>
{lean.watch_out([("I love kitchen.", "I love cooking.", "the <i>kitchen</i> is the room."), ("My mom is a great cooker.", "My mom is a great cook.", "a <i>cooker</i> is a stove (UK)."), ("Turn on the fire.", "Turn on the stove / the burner.", "<i>fire</i> = flames that burn things.")])}
{lean.writing_task(sub, "A recipe for a blog: write a recipe for a dish you like, with a short introduction, the ingredients and the steps.", "My friends always ask me to make this… You need:… First,… As soon as…", ["ingredients with amounts", "three time words", "a tip", "100–150 words"], "I can give instructions with time clauses and describe how food tastes.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class. <i>Sour</i> = acid, like lemon; <i>bitter</i> = strong and unpleasant, like black coffee. When you correct the writing, check the present after time words.</p>""")

    script = "".join(f"<p style='margin:.5mm 0'><b>{l.split(': ', 1)[0]}:</b> {l.split(': ', 1)[1]}</p>" for l in S171)
    b.extra("Audio script", f"""
{sub("17.1", "Just like yours (natural and slow)")}
<div style="line-height:1.3;font-size:8.6pt">{script}</div>
{sub("17.2", "Repeat: linking in instructions")}
<p>{" · ".join(S172)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 17 - Cooking and eating")
