# Speak! Progress B1 - Unit 21 "Clothes" (all English) - B1 format (2026-11-17)
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Progress"
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

    # Page 1 - Warm-up
    cover = cover_html(T, "LEVEL B1 · UNIT 21", "Clothes", "Packing for a trip · <b>the order of adjectives: a long black waterproof jacket</b>",
                       [("YOU CAN", "describe clothes in detail and decide what to wear and pack"),
                        ("LANGUAGE", "a headscarf · a bow tie · layers · put on · take off · try on · fit · fold · a brown leather belt"),
                        ("PRONUNCIATION", "tricky clothes words: clothes, suit, sweater, wear / where")])
    hw = ["a blouse", "a bow tie", "a cap", "a headscarf", "a jacket", "a top", "a scarf"]
    ft = ["boots", "pants", "a skirt", "sneakers", "shorts"]
    ac = [("earrings", "on the ears"), ("a bracelet", "on the wrist"), ("a handbag", "over the shoulder"), ("a belt", "around the waist"), ("a necklace", "around the neck")]
    acl = " &nbsp;·&nbsp; ".join(f"<b>{a}</b> {A(w, 'min-width:20mm')}" for a, w in ac)
    b.page(f"""{sec(1, "Warm-up: what are you wearing?", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 46, 31)}<div style="flex:1">
{sub("A", "Discuss with your teacher.", "2 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0"><li>Describe what you're wearing today.</li><li>Do you plan your clothes the night before?</li><li>Are you good at packing for a trip?</li></ol></div></div>
{sub("B", "Where do you wear them? Write the clothes in the correct column.", "4 min")}
<div class="bank">a blouse · boots · a bow tie · a cap · a headscarf · a jacket · pants · a scarf · shorts · a skirt · sneakers · a top</div>
<table style="font-size:8.6pt;margin:.5mm 0"><tr><th style="width:50%">from head to waist</th><th>from waist to feet</th></tr><tr><td>{R(', '.join(hw)) if T else lines(2)}</td><td>{R(', '.join(ft)) if T else lines(2)}</td></tr></table>
{sub("C", "Accessories. Where do you wear them? Write: around the neck, around the waist, on the ears, on the wrist, over the shoulder.", "2 min")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.9">{acl}</p>""",
    30, """<ol><li>B: ask for two more items in each column (<i>a hoodie, a vest / leggings, sandals</i>). <i>Pants</i> is American English (British: <i>trousers</i>).</li>
<li>C: also <i>a watch</i> (on the wrist), <i>a ring</i> (on a finger), <i>sunglasses</i>, <i>a backpack</i> (on your back).</li></ol>""", cover=cover)

    b.extra("Lesson overview · 60 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Discussion · types of clothes · accessories</td><td>1</td></tr>
<tr><td>2 Listening</td><td>12 min</td><td>Dialogue: Danny packs for Patagonia and Buenos Aires with Bruno</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>8 min</td><td>The order of adjectives</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>The order of adjectives (study at home)</td><td>4</td></tr>
<tr><td>4 Vocabulary lab + pronunciation</td><td>8 min</td><td>Clothing verbs · US/UK words · tricky clothes words</td><td>5</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Carol's email about a wedding outfit · describing clothes</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>What would you wear? · long turn · talking point</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>4 min</td><td>Can-do · language notes · writing homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY</h4>The Linguahouse lesson is a vocabulary lesson (types of clothes, formal clothes, US/UK words, materials, accessories, clothing verbs) with no listening and no grammar. We added a listening and a grammar point that fits the topic: the order of adjectives. Danny is packing for his trip south (mentioned in B1 Unit 19 and Review 2): two weeks in Patagonia, then Buenos Aires, with only one backpack. Bruno (Fenrir) helps and lends him his belt. Continuity: the sweater was bought second-hand (B1 18). No new real-world facts beyond general travel advice (layers, cold nights in the mountains). In the Practice, Carol (Orlando) asks Ana about an outfit for a wedding. The writing model is Danny's blog post about packing.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students put adjectives after the noun (<i>a jacket black</i>) or in the wrong order (<i>a leather brown belt</i>). False friends: <i>blouse</i> for a warm sweater, <i>a smoking</i> for a tuxedo, <i>a short</i> for shorts, <i>I dressed a jacket</i> for <i>I put on a jacket</i>. Pronunciation: <i>clothes</i> is one syllable /kloʊðz/.</div>
<div class="box"><h4>AUDIO</h4>Track 21.1 One backpack (natural and slow) · Track 21.2 Repeat: tricky clothes words</div>""")

    # Page 2 - Listening
    gist = ["to a wedding in Buenos Aires", "to Patagonia and Buenos Aires", "home to the US"]
    items = [("a long black waterproof jacket", True), ("a dark suit", False), ("an old green wool sweater", True), ("brown leather hiking boots", True), ("sandals", False),
             ("a light blue cotton shirt", True), ("dark jeans", True), ("a tie", False), ("Bruno's belt", True), ("a swimsuit", True), ("gloves", True)]
    il = " &nbsp; ".join(f"☐ {t}{(' ' + R('✓')) if ok else ''}" for t, ok in items)
    gp = [("my long ___ waterproof jacket", "black"), ("this ugly ___ green wool sweater", "old"), ("a pair of brown ___ hiking boots", "leather"),
          ("a ___ blue cotton shirt", "light"), ("a classic brown leather ___", "belt")]
    gpl = "".join(f"<li><i>{s.replace('___', A(a, 'min-width:14mm'))}</i></li>" for s, a in gp)
    b.page(f"""{sec(2, "Listening: one backpack", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{audiocard(["21.1 · NATURAL", "21.1 · SLOW"])}
{sub("A", "Danny is packing, and his roommate Bruno helps. Listen at natural speed. Where is Danny going?", "2 min", "21.1")}
<p style="margin:.3mm 0;font-size:8.9pt">{ch(gist, gist[1])}</p></div>{img('B', 40, 27)}</div>
{sub("B", "Listen again. What is Danny taking? Check eight items. Three are not mentioned.", "3 min")}
<p style="font-weight:600;font-size:8.7pt;line-height:1.6;margin:.3mm 0">{il}</p>
{sub("C", "Complete the descriptions from the dialogue.", "3 min")}
<ol style="line-height:1.7;font-size:8.8pt;margin:0;columns:2;column-gap:5mm">{gpl}</ol>
{sub("D", "Think about it. Discuss with your teacher.", "4 min")}
<ol style="line-height:1.4;font-size:8.7pt;margin:0"><li>Why does Danny want to wear his boots on the bus? {R("So they don't take up space in his backpack.") if T else ""}</li><li>Do you prefer to travel with one backpack or a big suitcase? Why?</li></ol>
<div class="box sand" style="margin-top:1mm"><h4>NOTICE: USEFUL CHUNKS</h4><i>No way. · That goes in, for sure. · take up space · Fair enough. · Here, try it on. · See? It fits. · Yes, sir!</i></div>""",
    27, """<ol><li>B: the items not mentioned are <i>a dark suit, sandals</i> and <i>a tie</i>. The boots and the belt are not in the bag: Danny will wear them.</li>
<li>C: ask the student what kind of information each adjective gives (color, age, material, purpose) before the Language focus.</li></ol>""")

    # Page 3 - Language focus
    oq = [("waterproof / long / black", "a long black waterproof jacket"), ("old / ugly / wool / green", "an ugly old green wool sweater"),
          ("cotton / light blue", "a light blue cotton shirt"), ("leather / classic / brown", "a classic brown leather belt")]
    oql = "".join(f"<li>a ({o}) {'jacket' if 'jacket' in r else 'sweater' if 'sweater' in r else 'shirt' if 'shirt' in r else 'belt'} → {A(r, 'min-width:50mm')}</li>" for o, r in oq)
    b.page(f"""{sec(3, "Language focus: the order of adjectives", "8 min")}
{sub("A", "Put the adjectives in the correct order. Then check in the audio script.", "3 min")}
<ol style="line-height:1.85;font-size:8.9pt;margin:0">{oql}</ol>
{sub("B", "Complete the rules. Choose.", "3 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0"><li>Adjectives go {ch(["before", "after"], "before")} the noun.</li>
<li>Opinion adjectives (<i>ugly, classic, beautiful</i>) come {ch(["first", "last"], "first")}.</li>
<li>Color comes {ch(["before", "after"], "before")} material: <i>brown leather</i>.</li>
<li>Purpose (<i>hiking, running</i>) goes {ch(["next to the noun", "at the start"], "next to the noun")}: <i>leather hiking boots</i>.</li>
<li>After <i>be</i>, we join adjectives with {ch(["and", "nothing"], "and")}: <i>The jacket is long and warm.</i></li></ol>
{sub("C", "Correct or incorrect? Choose.", "2 min")}
<ol style="line-height:1.6;font-size:8.9pt;margin:0"><li>She bought a dress red. {ch(["correct", "incorrect"], "incorrect")} {R("→ a red dress") if T else ""}</li><li>I love your new Italian shoes. {ch(["correct", "incorrect"], "correct")}</li><li>He wore a silk beautiful tie. {ch(["correct", "incorrect"], "incorrect")} {R("→ a beautiful silk tie") if T else ""}</li></ol>
<div class="box sand"><h4>RULE</h4>Order: <b>opinion → size → age → shape → color → origin → material → purpose → NOUN</b> (<i>a beautiful old Italian silk tie</i>). Use two or three adjectives, not more. No <i>and</i> before the noun; use <i>and</i> after <i>be</i>. More on the next page: <b>Grammar reference</b>.</div>""",
    27, """<ol><li>A: write the eight categories on the board and ask the student to place each adjective.</li>
<li>B: point out <i>light / dark</i> + color (<i>light blue</i>) and purpose nouns (<i>hiking boots, running shoes</i>).</li>
<li>C: personalize: <i>Describe your favorite piece of clothing with three adjectives.</i></li></ol>""")

    grammar_ref.adjective_order(b)

    # Page 5 - Vocabulary lab
    vv = ["got dressed", "put on", "took off", "hung up", "wear", "try on", "fit", "fold"]
    g = [A(v, "min-width:15mm") for v in vv]
    txt = (f"Ana got up at 6:30, had a shower and {g[0]}. It was sunny, so she {g[1]} a light jacket and walked to the hospital. When she got there, she {g[2]} her jacket and {g[3]} it behind the door. "
           f"Then she remembered: it was her mom's birthday! At lunch, she went to a store near the hospital. Ana and her mom are the same size and often {g[4]} the same clothes, so she decided to {g[5]} a sweater and a dress herself. "
           f"The sweater didn't {g[6]} her, but the dress was perfect. She asked the clerk to {g[7]} it neatly and wrap it.")
    uk = [("a sweater", "a jumper"), ("pantyhose", "tights"), ("a tuxedo", "a dinner jacket"), ("a swimsuit", "a swimming costume"), ("an undershirt", "a vest")]
    ukl = " &nbsp;·&nbsp; ".join(f"{a} = {A(u, 'min-width:22mm')}" for a, u in uk)
    b.page(f"""{sec(4, "Vocabulary lab: clothing verbs", "4 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Complete the text with the verbs in the box. Use the correct form.", "2 min")}
<div class="bank">fit · fold · get dressed · hang up · put on · take off · try on · wear</div></div>{img('C', 30, 20)}</div>
<div class="box" style="font-size:8.7pt;line-height:1.85;margin:.5mm 0">{txt}</div>
{sub("B", "American or British? Write the British word: a dinner jacket, a jumper, a swimming costume, tights, a vest.", "2 min")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.9">{ukl}</p>
<div class="box sand"><h4>WATCH OUT: FALSE FRIENDS AND WORD CHOICE</h4>
<table style="margin:0;font-size:8.2pt"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>I'm cold. I'll put on a blouse.</td><td><b>I'll put on a sweater.</b></td><td>a <i>blouse</i> is a light shirt for women.</td></tr>
<tr><td>He wore a smoking to the wedding.</td><td><b>He wore a tuxedo.</b></td><td><i>smoking</i> = using cigarettes.</td></tr>
<tr><td>I'm wearing a short.</td><td><b>I'm wearing shorts / a pair of shorts.</b></td><td><i>shorts, pants, jeans</i> are always plural.</td></tr>
<tr><td>I dressed a jacket.</td><td><b>I put on a jacket.</b></td><td><i>get dressed</i> = put on all your clothes; for one item, <i>put on</i>.</td></tr></table></div>
{sec(5, "Pronunciation lab: tricky clothes words", "4 min")}
<p class="small" style="margin:.3mm 0"><i>clothes</i> /kloʊðz/ (one syllable) · <i>sweater</i> /ˈswetər/ (like <i>sweat</i>) · <i>suit</i> /suːt/ · <i>shirt</i> /ʃɜrt/ vs <i>skirt</i> /skɜrt/ · <i>wool</i> /wʊl/ · <i>wear</i> and <i>where</i> sound the same.</p>
{audiocard(["21.2"])}
{sub("A", "Listen and repeat. Then describe what your teacher is wearing.", "4 min", "21.2")}
<p style="margin:.3mm 0;font-size:8.8pt;line-height:1.55">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S212))}</p>""",
    22, """<ol><li>A: <i>fit</i> = the right size; <i>suit</i> = looks good on you. <i>Hang up</i> is irregular: <i>hung up</i>.</li>
<li>B: in British English, a <i>vest</i> is an undershirt; in American English, a <i>vest</i> is worn over a shirt (British: <i>waistcoat</i>).</li></ol>""")

    # Page 6 - Practice
    pc = [(["beautiful long blue", "long beautiful blue"], "beautiful long blue"), (["fits", "suits"], "fits"), (["tried it on", "dressed it"], "tried it on"),
          (["black silk", "silk black"], "black silk"), (["comfortable old", "old comfortable"], "comfortable old"), (["take off", "take out"], "take off")]
    p = [ch(o, a) for o, a in pc]
    dd = [("jacket: denim / old / blue", "an old blue denim jacket"), ("shoes: running / white / new", "new white running shoes"), ("scarf: wool / lovely / red", "a lovely red wool scarf"),
          ("bag: leather / small / Italian", "a small Italian leather bag"), ("hat: straw / big / beach", "a big straw beach hat")]
    ddl = "".join(f'<li><i>{d}</i> {A(i, "min-width:48mm")}</li>' for d, i in dd)
    b.page(f"""{sec(6, "Practice", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Carol (Orlando) writes to her cousin Ana. Choose the correct words.", "4 min")}</div>{img('D', 30, 20)}</div>
<div class="box" style="line-height:1.95;font-size:9pt"><b>From: Carol · To: Ana</b><br>Hi Ana! I need your help. My friend Linda is getting married in Miami next month, and the invitation says "cocktail attire." I have a {p[0]} dress, but I'm not sure it still {p[1]} me. I {p[2]} last night, and it's a bit tight! Plan B is my {p[3]} top with a skirt. For shoes, I'll take high heels for the photos and a pair of {p[4]} sandals for later, because I always {p[5]} my shoes to dance. What would you wear? Send me photos of your wedding outfits! Love, Carol</div>
{sub("B", "Describe the clothes. Put the adjectives in order.", "4 min")}
<ol style="line-height:1.75;font-size:8.8pt;margin:0">{ddl}</ol>""",
    24, """<ol><li>A: <i>cocktail attire</i> = semi-formal: a short or knee-length dress, or a suit without a tie. <i>Attire</i> = clothes (formal word).</li>
<li>B: in 5, <i>beach</i> is the purpose, so it goes next to the noun.</li></ol>""")

    # Page 7 - Speaking
    sit = ["a job interview at an international company", "a wedding abroad", "a formal dinner", "a day at the beach", "a very cold day in New York", "a hiking trip in the mountains"]
    sitl = "".join(f"<li>{x}</li>" for x in sit)
    b.page(f"""{sec(7, "Speaking: what would you wear?", "12 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>choosing</th><th>describing</th><th>opinions</th><th>dress codes</th></tr>
<tr><td><i>I'd probably wear… · I definitely wouldn't wear…</i></td><td><i>a … made of … · It's a kind of… · It goes with…</i></td><td><i>It really suits you. · It's a bit too formal / casual.</i></td><td><i>formal · smart casual · casual · You're supposed to…</i></td></tr></table></div>
{sub("A", "What would you wear? Take turns. Describe your outfit with at least two adjectives in the right order, and say what you definitely wouldn't wear.", "5 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0;columns:2">{sitl}</ol>
{sub("B", "Long turn. Prepare for one minute, then talk for two minutes about a piece of clothing that is special to you.", "4 min")}
<ul style="line-height:1.45;font-size:8.9pt;margin:0"><li>what it looks like (use three adjectives)</li><li>where and when you got it</li><li>when you wear it and what you wear it with</li><li>why it's special</li></ul>
{sub("C", "Talking point. Discuss with your teacher.", "3 min")}
<ol style="line-height:1.5;font-size:8.9pt;margin:0"><li>Do the clothes people wear reflect their personality? How?</li><li>Is it important to be fashionable? Do people in different countries dress differently?</li></ol>""",
    30, """<ol><li>A: answer first to model: <i>For a wedding abroad, I'd probably wear a dark blue linen suit. I definitely wouldn't wear sneakers.</i> <i>Smart casual</i> = nice but not formal.</li>
<li>B: don't interrupt; note mistakes for the error log (page 8), especially adjective order and <i>blouse / sweater</i>.</li></ol>""")

    # Page 8 - Wrap-up
    cd = ["I can describe clothes with adjectives in the correct order.", "I can use clothing verbs (put on, take off, try on, fit…).", "I can say what I would wear in different situations."]
    cdr = "".join(f"<tr><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for s in cd)
    b.page(f"""{sec(8, "Wrap-up and homework", "4 min")}
{sub("A", "Can-do check", "1 min")}
<table class="ck" style="font-size:8.6pt"><tr><th>In English…</th><th style="width:16mm">Easy!</th><th style="width:16mm">Sometimes</th><th style="width:16mm">Not yet</th></tr>{cdr}</table>
{sub("B", "My language notes. Write three corrections from today's class.", "2 min")}
<div style="display:flex;gap:5mm;font-size:8.6pt"><div style="flex:1"><b>I said…</b>{lines(3)}</div><div style="flex:1"><b>Better:</b>{lines(3)}</div></div>
{sub("C", "Homework: writing (100–150 words)", "1 min")}
<p style="margin:.3mm 0"><b>A packing list blog post.</b> Choose a trip (real or imaginary). Write what you would pack and why. Read Danny's post first.</p>
<div class="box" style="font-size:8.6pt;line-height:1.4;margin:.5mm 0"><b>Gap Year Diaries · Patagonia in one backpack</b><br><i>Everything I'm taking fits in one backpack, so I had to choose carefully. The most important thing is my long black waterproof jacket, because the weather in the mountains can change fast. Under it, I'll wear layers: a T-shirt and my ugly old green wool sweater (my favorite!). My brown leather hiking boots don't fit in the bag, so I'll wear them on the bus. For Buenos Aires, I'm taking a light blue cotton shirt, dark jeans and a classic brown leather belt that my roommate lent me. I'm also packing a swimsuit, a hat and some gloves, because it can get cold at night. My tip: roll your T-shirts. They take up less space!</i></div>
<p class="small" style="margin:.3mm 0">Checklist: ☐ where you're going &nbsp;☐ five items with two or three adjectives &nbsp;☐ reasons (because…) &nbsp;☐ a tip &nbsp;☐ 100–150 words</p>
{lines(5)}""",
    30, """<ol><li>B (error log): during the lesson, note 3–5 real mistakes. Here, the student writes what they said and the better version; guide them to self-correct first.</li>
<li>C: check adjective order and plural clothes (<i>jeans, shorts, pants</i>).</li></ol>""")

    script = "".join(f"<p style='margin:.5mm 0'><b>{l.split(': ', 1)[0]}:</b> {l.split(': ', 1)[1]}</p>" for l in S211)
    b.extra("Audio script", f"""
{sub("21.1", "One backpack (natural and slow)")}
<div style="line-height:1.3;font-size:8.6pt">{script}</div>
{sub("21.2", "Repeat: tricky clothes words")}
<p>{" · ".join(S212)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 21 - Clothes")
