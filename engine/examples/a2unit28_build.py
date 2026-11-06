# Speak! Bridge A2 - Unit 28 "Ice cream" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 28", audio_json="audio_a2-unit-28.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["a2-unit-28"]
S281 = [x.split(": ", 1) for x in _r["28.1 Our Favorite Foods podcast"].split("\n")]
S282 = [x.split(": ", 1)[1] for x in _r["28.2 Repeat: adverbs"].split("\n")]
S283 = [x.split(": ", 1)[1] for x in _r["28.3 Repeat: hidden syllables"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h, cap=""):
        c = f'<div class="small" style="text-align:center;padding:.4mm 0">{cap}</div>' if cap else ""
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block">{c}</div>'

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 28", "Ice cream", "Food and business · <b>adverbs and word order</b>",
                       [("YOU CAN", "talk about habits, plans and how you do things, with adverbs in the right place"),
                        ("LANGUAGE", "I usually get coffee. · I'm probably going to try it. · Do it carefully. · It's really good."),
                        ("PRONUNCIATION", "hidden syllables: choc(o)late · ev(e)ry")])
    cats = [("making ice cream", "recipe · ice cream maker"), ("flavors", "chocolate · vanilla"), ("where and when", "beach · sunny"), ("how we eat it", "cone · cup and spoon · scoop")]
    ct = "<tr>" + "".join(f"<th>{c}</th>" for c, _ in cats) + "</tr><tr>" + "".join(f'<td style="height:13mm;vertical-align:top">{R(w) if T else ""}</td>' for _, w in cats) + "</tr>"
    b.page(f"""{sec(1, "Warm-up: all about ice cream", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">{sub("A", "Put the words in the correct group.", "4 min")}
<div class="bank">beach · chocolate · cone · cup and spoon · ice cream maker · recipe · scoop · sunny · vanilla</div></div>{img('A', 36, 24)}</div>
<table style="margin:0;table-layout:fixed;text-align:center">{ct}</table>
<p class="small" style="margin:.8mm 0">Can you add more words to each group?</p>
{sub("B", "Talk about it.", "4 min")}
<ol style="line-height:1.55"><li>What's your favorite ice cream flavor? Do you prefer a cone or a cup?</li>
<li>Which flavors are popular in Brazil? Have you ever tried açaí, cupuaçu or tapioca ice cream?</li>
<li>Do you eat ice cream only in the summer, or all year?</li></ol>""",
    25, """<ol><li>A: an <i>ice cream maker</i> can be a machine or a person. Drill <i>chocolate</i> (two syllables: CHOC-lit) and <i>recipe</i> (three: RES-ih-pee).</li>
<li>B: in the US, July is National Ice Cream Month, proclaimed by President Reagan in 1984 (National Archives, <i>Prologue</i> blog, "NARA Screams for Ice Cream!", 2022).</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Ice cream vocabulary</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>A food podcast: an ice cream maker in Chicago</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Types of adverbs and their position</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Front, mid and end position · irregular adverbs</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>4 min</td><td>Adverbs in sentences · hidden syllables</td><td>5</td></tr>
<tr><td>5 Practice</td><td>9 min</td><td>Adding adverbs · Word builder: ordering ice cream</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Guess the adverb</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Kate is thinking of selling ice cream at Sweet Kate Bakery this summer, so she listens to a food podcast. The host (Studio-O) visits Rafael (Chirp3-HD-Charon), a Brazilian who left an office job in Boston and opened a small ice cream shop near the beach in Chicago. Rafael and his shop are invented. Fact: in 1984, President Ronald Reagan proclaimed July National Ice Cream Month (Proclamation 5219; National Archives, <i>Prologue</i> blog, July 2022). Today, National Ice Cream Day is celebrated on the third Sunday in July.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Portuguese word order is freer, so students put adverbs between the verb and the object (<i>I like very much ice cream</i> ✗, <i>I drink always coffee</i> ✗), say <i>good</i> instead of <i>well</i>, and put <i>probably</i> after <i>going to</i>. They also pronounce every letter in <i>chocolate</i> and <i>vegetable</i>.</div>
<div class="box"><h4>AUDIO</h4>Track 28.1 Our Favorite Foods podcast (slow and natural) · Track 28.2 Repeat: adverbs · Track 28.3 Repeat: hidden syllables</div>""")

    # Page 2
    tf = [("Rafael opened his ice cream shop five years ago.", "F: he started last year."), ("He made a lot of mistakes at first.", "T: but he ate them!"),
          ("He thinks you shouldn't look at other people's recipes.", "F: research them, then do it better."), ("Raspberry is his most popular flavor.", "F: strawberry sells out quickly."),
          ("People don't like new flavors.", "F: they usually want to try something new."), ("He sells a lot of ice cream all year.", "T: even in the winter.")]
    tfl = "".join(f'<li>{s} <b>T / F</b> {A(a, "min-width:40mm")}</li>' for s, a in tf)
    b.page(f"""{sec(2, "Listening: an ice cream podcast", "10 min")}
<div style="display:flex;gap:3mm;align-items:center"><p style="flex:1;margin:0">Kate wants to sell ice cream at Sweet Kate Bakery this summer, so she listens to a food podcast. The host visits Rafael, who has a small ice cream shop near the beach in Chicago.</p>{img('F', 34, 21)}</div>
{audiocard(["28.1 · SLOW", "28.1 · NATURAL"])}
{sub("A", "Listen and answer the questions.", "3 min", "28.1 · SLOW")}
<ol style="line-height:1.5"><li>Which words from the Warm-up do you hear? {A("recipe, flavor, beach, sunny, scoop", "min-width:50mm")}</li>
<li>Which new flavor is Rafael going to make next? {A("B: seaweed", "min-width:22mm")}</li></ol>
<div style="display:flex;gap:3mm;justify-content:center">{img('B', 34, 20, "A starfish")}{img('C', 34, 20, "B seaweed")}{img('D', 34, 20, "C seashell")}</div>
<ol start="3"><li>Do you think it's a good idea? Would you try it?</li></ol>
{sub("B", "Listen again. Are the sentences true (T) or false (F)?", "5 min", "28.1 · NATURAL")}
<ol style="line-height:1.55;font-size:9pt">{tfl}</ol>""",
    27, """<ol><li>A: before listening, ask the student to guess the new flavor from the photos. Rafael also mentions açaí, a good link to Brazil.</li>
<li>B: let the student correct the false sentences. Read the script together if there is time; it prepares the next page.</li></ol>""")

    # Page 3
    b.page(f"""{sec(3, "Language focus: adverbs", "10 min")}
{sub("A", "Time and place, manner. Read and choose.", "3 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5"><b>Today</b> I'm making strawberry ice cream. · I started making ice cream <b>last year</b>.<br>Research your recipe <b>carefully</b>. · People want to spend time <b>outside</b>.</div>
<ol style="line-height:1.7"><li><i>Today</i> and <i>last year</i> tell us {ch(["when", "how often", "how"], "when")}. They go at the {ch(["front or end", "middle"], "front or end")} of the sentence.</li>
<li><i>Carefully</i> and <i>outside</i> tell us {ch(["how and when", "how and where", "where and when"], "how and where")}. They go at the {ch(["front", "end"], "end")}.</li></ol>
{sub("B", "Mid position. Read and choose.", "3 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">I'm <b>probably</b> going to try a seaweed flavor. · People <b>usually</b> want to try something new. · It's <b>always</b> time for ice cream!</div>
<ol style="line-height:1.7"><li><i>Probably</i> tells us {ch(["how certain", "how often"], "how certain")}; <i>usually</i> and <i>always</i> tell us {ch(["how certain", "how often"], "how often")}.</li>
<li>These adverbs go {ch(["before", "after"], "before")} the main verb, but {ch(["before", "after"], "after")} the verb <b>be</b>.</li></ol>
{sub("C", "Adverbs with adjectives, and irregular adverbs. Read and answer.", "4 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">That's <b>really</b> interesting. · That's a <b>very</b> good question. · It wasn't <b>too</b> bad.<br>…before I learned how to do it <b>well</b>. · See if you can do it <b>better</b>.</div>
<ol style="line-height:1.7"><li><i>Really, very</i> and <i>too</i> give information about {ch(["a verb", "an adjective", "a noun"], "an adjective")}. They go before it.</li>
<li>Which adjective is related to <i>well</i>? {A("good", "min-width:16mm")} What form is <i>better</i>? {A("the comparative of well", "min-width:40mm")}</li></ol>
<div class="box sand"><h4>RULE</h4><b>front / end:</b> time · <b>end:</b> manner, place · <b>mid</b> (before the main verb, after <b>be</b>): frequency, certainty · <b>before an adjective:</b> degree. Don't put an adverb between a verb and its object. More on the next page: <b>Grammar reference</b>.</div>""",
    27, """<ol><li>Adverbs are complex, and there are exceptions; a different position can add emphasis. At A2, the rules on this page are enough.</li>
<li>Drill every example sentence. Ask: <i>Where's the main verb? Where's the adverb?</i></li></ol>""")

    grammar_ref.adverb_position(b)

    # Page 5
    syl = ["choc(o)late: 2", "ev(e)ry: 2", "veg(e)table: 3", "comf(or)table: 3", "recipe: 3 (no silent letters!)"]
    sl = "".join(f"<li>{w} {A(s, 'min-width:44mm')}</li>" for w, s in zip(S283, syl))
    b.page(f"""{sub("D", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>I like very much ice cream.</td><td><b>I like ice cream very much.</b></td><td>verb + object together.</td></tr>
<tr><td>I drink always coffee.</td><td><b>I always drink coffee.</b></td><td>frequency: before the main verb.</td></tr>
<tr><td>She always is happy.</td><td><b>She's always happy.</b></td><td>after be.</td></tr>
<tr><td>He cooks very good.</td><td><b>He cooks very well.</b></td><td>good → well.</td></tr>
<tr><td>I'm going to probably buy it.</td><td><b>I'm probably going to buy it.</b></td><td>certainty: mid position.</td></tr>
<tr><td>I went yesterday to the beach.</td><td><b>I went to the beach yesterday.</b></td><td>time: end (or front).</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "4 min")}
{audiocard(["28.2", "28.3"])}
{sub("A", "Listen and repeat. Notice where the adverbs are.", "2 min", "28.2")}
{twocol([f'<li value="{i+1}">{s}</li>' for i, s in enumerate(S282)], 4)}
{sub("B", "Hidden syllables. Listen and repeat. How many syllables do you hear? Cross out the silent letters.", "2 min", "28.3")}
<ol style="line-height:1.55">{sl}</ol>""",
    27, """<ol><li>A: in sentence 3, <i>always</i> comes after <i>'s</i> (be); in 1, <i>probably</i> comes before <i>going</i>.</li>
<li>B: Brazilians pronounce every written vowel (<i>cho-co-la-te</i>). Also <i>different</i>, <i>family</i>, <i>favorite</i> and <i>interesting</i> are often shorter in natural speech.</li></ol>""")

    # Page 6
    pr = [("I'll call you when I get home.", "definitely", "I'll definitely call you when I get home.", "certainty · mid"),
          ("I went to see my family.", "last week", "I went to see my family last week. / Last week I went…", "time · end or front"),
          ("She is late.", "never", "She is never late.", "frequency · after be"),
          ("She's going to buy a new car.", "probably", "She's probably going to buy a new car.", "certainty · mid"),
          ("I was watching a cool movie on TV.", "really", "I was watching a really cool movie on TV.", "degree · before the adjective"),
          ("When it started to rain, we went.", "inside", "When it started to rain, we went inside.", "place · end"),
          ("I have fallen asleep in front of the TV.", "often", "I have often fallen asleep in front of the TV.", "frequency · mid"),
          ("That soup is spicy!", "too", "That soup is too spicy!", "degree · before the adjective"),
          ("You play the guitar.", "well", "You play the guitar well.", "manner · end")]
    prl = "".join(f'<li>{s} <b>({a})</b><br>{A(r, "min-width:80mm")} <span class="small">{R(t) if T else ""}</span></li>' for s, a, r, t in pr)
    lines = [("Server", "Hi! What can I get you?"), ("Kate", f"Can I have two {A('scoops', 'min-width:16mm')} of chocolate, please?"),
             ("Server", f"Sure. In a {A('cone', 'min-width:14mm')} or a {A('cup', 'min-width:14mm')}?"),
             ("Kate", f"A cup, please. And can I have some chocolate {A('sprinkles', 'min-width:18mm')} on top?"),
             ("Server", f"Of course. Is that for here or {A('to go', 'min-width:14mm')}?"),
             ("Kate", f"For here. Oh, and can I {A('try', 'min-width:12mm')} the açaí flavor first?"),
             ("Server", f"Sure. Here's a {A('sample', 'min-width:16mm')}. It's really good!")]
    ol = "<br>".join(f"<b>{n}:</b> {t}" for n, t in lines)
    b.page(f"""{sec(5, "Practice", "9 min")}
{sub("A", "Add the adverb in the correct place. Sometimes two positions are possible.", "6 min")}
<p class="small" style="margin:0"><i>Example: I think we can move this piano if we do it. (slowly) → …if we do it slowly. (manner · end)</i></p>
<ol style="line-height:1.32;font-size:8.8pt">{prl}</ol>
{sub("B", "Word builder: ordering ice cream. Complete the conversation.", "3 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1"><div class="bank">cone · cup · sample · scoops · sprinkles · to go · try</div>
<p style="margin:.5mm 0;line-height:1.55;font-size:9pt">{ol}</p></div>{img('E', 32, 24)}</div>""",
    27, """<ol><li>A: ask the student to name the type of adverb and the position each time. Then drill the sentences.</li>
<li>B: in the US, ice cream shops often give a free <i>sample</i> on a small spoon. <i>For here or to go?</i> = eat in the shop or take it away.</li></ol>""")

    # Page 7
    prompts = ["something you <b>always</b> do on the weekend", "something you want to do <b>better</b> in the future", "something you need to do <b>carefully</b>",
               "something you're <b>definitely</b> going to eat in the next few days", "something you bought <b>last month</b>", "something you like to do <b>outside</b>",
               "someone you're <b>probably</b> going to see next week", "something that's <b>too</b> expensive for you at the moment", "something you <b>usually</b> do in the evening"]
    pl = "".join(f"<li>{p}</li>" for p in prompts)
    cellst = 'style="height:16mm;width:25%;vertical-align:top;border:1pt solid #9cc5cc;background:#fff;padding:1mm" class="small"'
    boxes = "</tr><tr>".join("".join(f'<td {cellst}><b>{r*4+c+1}</b> ' + ("<i>go for a walk</i>" if r == 0 and c == 0 else "") + "</td>" for c in range(4)) for r in range(2))
    b.page(f"""{sec(6, "Speaking: guess the adverb", "12 min")}
{sub("A", "Choose eight of these ideas. Write a key word or short phrase in each box, in any order. Don't write the adverb!", "4 min")}
<ol style="line-height:1.45;font-size:9pt;column-count:2;column-gap:5mm">{pl}</ol>
<table style="margin:1mm 0 0;table-layout:fixed;border-collapse:collapse"><tr>{boxes}</tr></table>
{sub("B", "Your teacher looks at your boxes and guesses. Then change roles.", "8 min")}
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:9pt;line-height:1.45"><b>A:</b> I think you <b>always</b> go for a walk on the weekend.<br><b>B:</b> No, try again.<br><b>A:</b> Going for a walk is something you like to do <b>outside</b>.<br><b>B:</b> Yes, that's right! I always feel much better when I spend time outside.</div>
{sub("C", "Tell your teacher about two of your answers. Give more details.", "2 min")}""",
    22, """<ol><li>A: the teacher fills in boxes too. Check the first box before the student continues.</li>
<li>B: insist on full sentences with the adverb in the correct position; correct word order immediately, then let the student repeat.</li></ol>""")

    # Page 8
    pc = [("A2 Unit 25", "I can talk about TV shows with -ed and -ing adjectives."), ("A2 Unit 26", "I can describe people's personalities with modifiers."),
          ("A2 Unit 27", "I can compare people and things with comparatives and superlatives."), ("A2 Unit 28", "I can use adverbs in the correct position.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("I usually get coffee on my way to work.", "I get usually coffee on my way to work.", "a"),
          ("I'm afraid too you're late for the party.", "I'm afraid you're too late for the party.", "b"),
          ("I'm probably going to get chocolate ice cream.", "I'm going to probably get chocolate ice cream.", "a"),
          ("It's not healthy to spend inside the weekend.", "It's not healthy to spend the weekend inside.", "b"),
          ("Last year I went to Florida on vacation.", "I went to Florida on vacation last year.", "both"),
          ("That's a very nice coat!", "That's very a nice coat!", "a"),
          ("They'll be definitely very happy.", "They'll definitely be very happy.", "b"),
          ("Today I'm going to work very hard.", "I'm going to work very hard today.", "both"),
          ("We can get to the station on time if you walk quickly.", "We can get to the station on time if you quickly walk.", "a"),
          ("We want always to try new flavors.", "We always want to try new flavors.", "b")]
    hwl = "".join(f'<li>a) {R("<u>" + a + "</u>") if T and k in ("a", "both") else a} &nbsp; b) {R("<u>" + bb + "</u>") if T and k in ("b", "both") else bb}</li>' for a, bb, k in hw)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Underline the correct sentence. In some pairs, both are correct.</b></p>
<ol style="line-height:1.5;font-size:8.8pt">{hwl}</ol>
<p style="margin-top:1.5mm"><b>2. My perfect dessert (50–75 words).</b> Write about a dessert or food you love. When do you usually eat it? Where? Can you make it well? Use at least five adverbs.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    27, """<p>Next class: the student reads the text aloud; check adverb positions together. Extension idea: invent a new ice cream flavor for Rafael's shop and describe it with adverbs (<i>It's really sweet, and people will definitely love it</i>).</p>""")

    b.extra("Audio script", f"""
{sub("28.1", "Our Favorite Foods podcast (slow and natural)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in S281)}</p>
{sub("28.2", "Repeat: adverbs")}
<p>{" · ".join(S282)}</p>
{sub("28.3", "Repeat: hidden syllables")}
<p>{" · ".join(S283)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 28 - Ice cream")
