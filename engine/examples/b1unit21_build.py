# Speak! Progress B1 - Unit 21 "Clothes" (all English) - lean B1 format (rebuilt 2026-11-19)
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
setup(band="B1 · UNIT 21", audio_json="audio_b1-unit-21.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-21"]
S211 = [l.replace("twenty reais", "R$20") for l in _r["21.1 One backpack"].split("\n")]
S212 = [x.split(": ", 1)[1] for x in _r["21.2 Repeat: tricky clothes words"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'
    def lines(n):
        return '<div class="wline"></div>' * n

    # 1 Warm-up
    cover = cover_html(T, "LEVEL B1 · UNIT 21", "Clothes", "Packing for a trip · <b>the order of adjectives: a long black waterproof jacket</b>",
                       [("YOU CAN", "describe clothes in detail and decide what to wear and pack"),
                        ("LANGUAGE", "a headscarf · a bow tie · layers · put on · take off · try on · fit · fold · a brown leather belt"),
                        ("PRONUNCIATION", "tricky clothes words: clothes, suit, sweater, wear / where")])
    hw = ["a blouse", "a cap", "a jacket", "a scarf"]
    ft = ["boots", "pants", "a skirt", "sneakers"]
    b.page(f"""{sec(1, "Warm-up: what are you wearing?", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["Describe what you're wearing today.", "Do you plan your clothes the night before?", "Are you good at packing for a trip?"], "START TALKING")}</div></div>
{sub("A", "Where do you wear them? Write the clothes in the correct column.", "3 min")}
<div class="bank">a blouse · boots · a cap · a jacket · pants · a scarf · a skirt · sneakers</div>
<table style="font-size:8.6pt;margin:.5mm 0"><tr><th style="width:50%">from head to waist</th><th>from waist to feet</th></tr><tr><td>{R(', '.join(hw)) if T else lines(2)}</td><td>{R(', '.join(ft)) if T else lines(2)}</td></tr></table>
{talk(["Which accessories do you wear every day (a watch, a belt, earrings, a bracelet)?", "What's your favorite piece of clothing? Why?"], "USE THE WORDS")}""",
    26, """<ol><li>Top box: 4 minutes. <i>Pants</i> is American English (British: <i>trousers</i>).</li>
<li>A: ask for two more items in each column (<i>a hoodie, a vest / leggings, sandals</i>).</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Dialogue: Danny packs for Patagonia with Bruno · what he takes · Talk about it", "The order of adjectives",
                      "Put the adjectives in order · choose the rule · Use it (oral)", "Functional language · tricky clothes words (21.2) · What would you wear?",
                      "Carol's email about a wedding outfit · clothing verbs · word choice · writing"),
        'The Linguahouse lesson is a vocabulary lesson (types of clothes, formal clothes, US/UK words, materials, accessories, clothing verbs) with no listening and no grammar. We added a listening and a grammar point that fits the topic: the order of adjectives. Danny is packing for his trip south (mentioned in B1 Unit 19 and Review 2): two weeks in Patagonia, then Buenos Aires, with only one backpack. Bruno (Fenrir) helps and lends him his belt. Continuity: the sweater was bought second-hand (B1 18). No new real-world facts beyond general travel advice (layers, cold nights in the mountains). In the homework, Carol (Orlando) asks Ana about an outfit for a wedding.', 'Students put adjectives after the noun (<i>a jacket black</i>) or in the wrong order (<i>a leather brown belt</i>). False friends: <i>blouse</i> for a warm sweater, <i>a smoking</i> for a tuxedo, <i>a short</i> for shorts, <i>I dressed a jacket</i> for <i>I put on a jacket</i>. Pronunciation: <i>clothes</i> is one syllable /kloʊðz/.',
        "Track 21.1 One backpack (natural and slow) · Track 21.2 Repeat: tricky clothes words"))

    # 2 Listening
    gist = ["to a wedding in Buenos Aires", "to Patagonia and Buenos Aires", "home to the US"]
    items = [("a long black waterproof jacket", True), ("a dark suit", False), ("an old green wool sweater", True), ("brown leather hiking boots", True), ("sandals", False),
             ("a light blue cotton shirt", True), ("dark jeans", True), ("a tie", False), ("Bruno's belt", True), ("a swimsuit", True), ("gloves", True)]
    il = " &nbsp; ".join(f"☐ {t}{(' ' + R('✓')) if ok else ''}" for t, ok in items)
    b.page(f"""{sec(2, "Listening: one backpack", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{audiocard(["21.1 · NATURAL", "21.1 · SLOW"])}
{sub("A", "Danny is packing, and his roommate Bruno helps. Listen. Where is Danny going?", "2 min", "21.1")}
<p style="margin:.3mm 0;font-size:8.9pt">{ch(gist, gist[1])}</p></div>{img('B', 40, 27)}</div>
{sub("B", "Listen again. What is Danny taking? Check eight items. Three are not mentioned.", "4 min")}
<p style="font-weight:600;font-size:8.7pt;line-height:1.6;margin:.3mm 0">{il}</p>
{talk(["Why does Danny want to wear his boots on the bus?", "Do you prefer to travel with one backpack or a big suitcase? Why?", "What's the one thing you always pack?"])}""",
    26, """<ol><li>A–B: 6 minutes. Not mentioned: <i>a dark suit, sandals, a tie</i>. The boots and the belt are not in the bag: Danny will wear them.</li>
<li>Talk about it: 6 minutes. 1: so they don't take up space in his backpack.</li></ol>""")

    # 3 Grammar reference
    lean.grammar_in_class(b, grammar_ref.adjective_order)

    # 4 Practice
    oq = [("waterproof / long / black", "jacket", "a long black waterproof jacket"), ("old / ugly / wool / green", "sweater", "an ugly old green wool sweater"),
          ("cotton / light blue", "shirt", "a light blue cotton shirt"), ("leather / classic / brown", "belt", "a classic brown leather belt")]
    oql = "".join(f"<li>a ({o}) {n} → {A(r, 'min-width:50mm')}</li>" for o, n, r in oq)
    use = ["Describe what your teacher is wearing with two or three adjectives.", "Describe your favorite bag or backpack.", "Describe the shoes you wear most.",
           "What would you wear to a job interview at an international company?", "What would you definitely not wear to a wedding abroad?"]
    b.page(f"""{sec(4, "Practice: the order of adjectives", "10 min")}
{sub("A", "Put the adjectives in the correct order.", "3 min")}
<ol style="line-height:1.85;font-size:8.9pt;margin:0">{oql}</ol>
{sub("B", "Choose.", "1 min")}
<p style="margin:.3mm 0;font-size:8.9pt;line-height:1.7">She bought {ch(["a red dress", "a dress red"], "a red dress")}. &nbsp;·&nbsp; He wore {ch(["a beautiful silk tie", "a silk beautiful tie"], "a beautiful silk tie")}.</p>
<div class="box sand"><h4>RULE</h4>Order: <b>opinion → size → age → shape → color → origin → material → purpose → NOUN</b>. Use two or three adjectives, not more. No <i>and</i> before the noun; use <i>and</i> after <i>be</i>. See the <b>Grammar reference</b> on page 3.</div>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    24, """<ol><li>A–B: 4 minutes. Write the eight categories on the board and place each adjective.</li>
<li>Use it: 6 minutes, all oral. <i>Smart casual</i> = nice but not formal.</li></ol>""")

    # 5 Speaking
    sit = ["a job interview at an international company", "a wedding abroad", "a formal dinner", "a day at the beach", "a very cold day in New York", "a hiking trip in the mountains"]
    sitl = "".join(f"<li>{x}</li>" for x in sit)
    b.page(f"""{sec(5, "Speaking: what would you wear?", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>choosing</th><th>describing</th><th>opinions</th><th>dress codes</th></tr>
<tr><td><i>I'd probably wear… · I definitely wouldn't wear…</i></td><td><i>a … made of … · It's a kind of… · It goes with…</i></td><td><i>It really suits you. · It's a bit too formal / casual.</i></td><td><i>formal · smart casual · casual · You're supposed to…</i></td></tr></table></div>
{audiocard(["21.2"])}
{sub("A", "Tricky words. Listen and repeat: clothes (one syllable) · suit /suːt/ · wear and where sound the same.", "4 min", "21.2")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.55">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S212))}</p>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("B", "What would you wear? Take turns. Describe your outfit with adjectives in the right order, and say what you definitely wouldn't wear.", "10 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0;columns:2">{sitl}</ol></div>{img('D', 28, 28)}</div>
{talk(["Do the clothes people wear reflect their personality? How?", "Is it important to be fashionable? Do people in different countries dress differently?"])}""",
    28, """<ol><li>B: answer first to model: <i>For a wedding abroad, I'd probably wear a dark blue linen suit. I definitely wouldn't wear sneakers.</i></li>
<li>Last 3 minutes: wrap-up (two corrections and <i>Can you describe clothes in detail?</i>).</li></ol>""")

    # H Homework
    pc = [(["beautiful long blue", "long beautiful blue"], "beautiful long blue"), (["fits", "suits"], "fits"), (["tried it on", "dressed it"], "tried it on"),
          (["black silk", "silk black"], "black silk"), (["take off", "take out"], "take off")]
    p = [ch(o, a) for o, a in pc]
    dd = [("jacket: denim / old / blue", "an old blue denim jacket"), ("shoes: running / white / new", "new white running shoes"), ("bag: leather / small / Italian", "a small Italian leather bag")]
    ddl = "".join(f'<li><i>{d}</i> {A(i, "min-width:44mm")}</li>' for d, i in dd)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Carol (Orlando) writes to her cousin Ana. Choose the correct words.", "")}</div>{img('C', 28, 18)}</div>
<div class="box" style="line-height:1.8;font-size:8.8pt;margin:.5mm 0"><b>From: Carol · To: Ana</b><br>Hi Ana! My friend Linda is getting married in Miami next month, and the invitation says "cocktail attire." I have a {p[0]} dress, but I'm not sure it still {p[1]} me. I {p[2]} last night, and it's a bit tight! Plan B is my {p[3]} top with a skirt. And I always {p[4]} my shoes to dance! Love, Carol</div>
{sub("B", "Describe the clothes. Put the adjectives in order.", "")}
<ol style="line-height:1.6;font-size:8.6pt;margin:0">{ddl}</ol>
{lean.watch_out([("I'm cold. I'll put on a blouse.", "I'll put on a sweater.", "a <i>blouse</i> is a light shirt for women."), ("He wore a smoking to the wedding.", "He wore a tuxedo.", "<i>smoking</i> = using cigarettes."), ("I'm wearing a short.", "I'm wearing shorts.", "<i>shorts, pants, jeans</i> are always plural.")])}
{lean.writing_task(sub, "A packing list blog post: choose a trip (real or imaginary) and write what you would pack and why.", "Everything I'm taking fits in one… The most important thing is my…", ["five items with adjectives", "reasons (because…)", "a tip", "100–150 words"], "I can describe clothes in detail and decide what to wear and pack.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class. <i>Cocktail attire</i> = semi-formal. When you correct the writing, check adjective order and plural clothes (<i>jeans, shorts, pants</i>).</p>""")

    script = "".join(f"<p style='margin:.5mm 0'><b>{l.split(': ', 1)[0]}:</b> {l.split(': ', 1)[1]}</p>" for l in S211)
    b.extra("Audio script", f"""
{sub("21.1", "One backpack (natural and slow)")}
<div style="line-height:1.3;font-size:8.6pt">{script}</div>
{sub("21.2", "Repeat: tricky clothes words")}
<p>{" · ".join(S212)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 21 - Clothes")
