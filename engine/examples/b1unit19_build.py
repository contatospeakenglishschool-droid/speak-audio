# Speak! Progress B1 - Unit 19 "At the clothes shop" (all English) - B1 format (2026-11-09)
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Progress"
setup(band="B1 · UNIT 19", audio_json="audio_b1-unit-19.json", img_dir="img")


_r = json.load(open("roteiro.json"))["units"]["b1-unit-19"]
S191 = [l.replace("thirty percent", "30%").replace("one eighty-nine", "$189").replace("thirty days", "30 days") for l in _r["19.1 A warm jacket"].split("\n")]
S192 = [x.split(": ", 1)[1] for x in _r["19.2 Repeat: teen or ty"].split("\n")]


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
    cover = cover_html(T, "LEVEL B1 · UNIT 19", "At the clothes shop", "Shopping for clothes abroad · <b>too, enough, one / ones</b>",
                       [("YOU CAN", "ask for sizes and colors, try things on, decide, pay and ask about returns"),
                        ("LANGUAGE", "a bargain · on sale · out of stock · a refund · Do you have it in a medium? · It's too tight · a bigger one"),
                        ("PRONUNCIATION", "-teen or -ty? thirteen, thirty")])
    sw = [("This jacket was on ___ when I bought it. It usually costs twice as much.", "sale"), ("___ clothes by famous brands are usually very expensive.", "Designer"),
          ("We sell all kinds of ___: boots, high heels and sneakers.", "footwear"), ("You can find suits, ties and shirts in the ___ section.", "menswear"),
          ("In a ___ store, you can find a wide range of different products.", "department"), ("These pants are too long. I'll take them to a ___.", "tailor"),
          ("I only paid $10 for this sweater. It was a real ___!", "bargain"), ("They give you a 10% ___ if you buy three items.", "discount"),
          ("He didn't like the shirt, so I took it back and asked for a ___.", "refund"), ("The book was out of ___. The clerk said to come back on Friday.", "stock")]
    swl = "".join(f"<li>{s.replace('___', A(a, 'min-width:16mm'))}</li>" for s, a in sw)
    b.page(f"""{sec(1, "Warm-up: going shopping", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 46, 30)}<div style="flex:1">
{sub("A", "Discuss with your teacher.", "2 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0"><li>Where do you usually buy clothes: in stores or online? Why?</li><li>Have you ever bought clothes in another country? Was it easy?</li></ol></div></div>
{sub("B", "In the store. Complete the sentences with the words from the box.", "5 min")}
<div class="bank">bargain · department · designer · discount · footwear · menswear · refund · sale · stock · tailor</div>
<ol style="line-height:1.5;font-size:8.6pt;margin:0;columns:2;column-gap:5mm">{swl}</ol>
{sub("C", "Tell your teacher about the best bargain you've ever found.", "1 min")}""",
    30, """<ol><li>B: <i>on sale</i> = cheaper than usual (US); <i>for sale</i> = available to buy. <i>Out of stock</i> = the store doesn't have it now. A <i>refund</i> = your money back.</li>
<li>C: model it: <i>I found a leather jacket at a second-hand store for $20. It was a real bargain!</i></li></ol>""", cover=cover)

    b.extra("Lesson overview · 60 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Discussion · store words: sale, bargain, refund, out of stock</td><td>1</td></tr>
<tr><td>2 Listening</td><td>12 min</td><td>Dialogue: Paulo buys a winter jacket in New York</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>8 min</td><td>too, enough, one / ones</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>too, enough, one / ones (study at home)</td><td>4</td></tr>
<tr><td>4 Vocabulary lab + pronunciation</td><td>8 min</td><td>US/UK store words · materials · -teen or -ty?</td><td>5</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Paulo's message to Ana · rewriting with too / enough</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Role-plays in a clothes store · long turn · talking point</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>4 min</td><td>Can-do · language notes · writing homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY</h4>The Linguahouse listening is a short, generic dialogue in a clothes store. Our original dialogue happens abroad, as the school's choice for practical units: Paulo, Ana's brother and a travel photographer (B1 Unit 15), is in a store in New York. He needs a warm jacket for a photo trip to Iceland, asks for another color and size, tries it on, decides, pays and asks about returns. The store is fictional. Verified fact: in the United States, the price on the tag usually doesn't include sales tax; the tax is added at the register, and the rate depends on the state and city. Many other countries, Brazil included, show prices with taxes included. In the Practice, Paulo writes to his sister Ana. The writing model is Paulo's online review of the jacket.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students say <i>Can I prove it?</i> (try it on), <i>It's in promotion</i> (on sale), <i>tennis</i> for sneakers, <i>It stays well on you</i> (it looks good on you / it suits you), <i>enough big</i>, <i>too much expensive</i> and <i>a bigger</i> without <i>one</i>. Pronunciation: <i>thirTEEN</i> vs <i>THIRty</i>, a real problem with prices.</div>
<div class="box"><h4>AUDIO</h4>Track 19.1 A warm jacket (natural and slow) · Track 19.2 Repeat: teen or ty</div>""")

    # Page 2 - Listening
    gist = ["a jacket", "a jacket and gloves", "nothing"]
    gp = [("Do you have it ___ black?", "in"), ("I'm afraid we've ___ the black ones.", "sold out of"), ("Do you have it in a ___?", "medium"),
          ("The ___ are over there, on the left.", "fitting rooms"), ("It's ___ off, so it's $189, plus ___.", "30% / tax"), ("I'll ___ the gloves. But I'll ___ the jacket.", "leave / take"),
          ("Are you paying by ___ or card?", "cash"), ("You need to keep the ___.", "receipt")]
    def _fill(s, a):
        for x in a.split(" / "):
            s = s.replace("___", A(x, "min-width:12mm"), 1)
        return s
    gpl = "".join(f"<li>{_fill(s, a)}</li>" for s, a in gp)
    tf = [("Paulo's coat isn't warm enough for Iceland.", "T"), ("The medium is perfect.", "F (too tight; he takes a large)"),
          ("In the US, tax is usually included in the price on the tag.", "F (added at the register)"), ("Paulo can return the jacket without the receipt.", "F (he needs the receipt)")]
    tfl = [f'<li value="{i+1}">{s} {A(a, "min-width:9mm")}</li>' for i, (s, a) in enumerate(tf)]
    b.page(f"""{sec(2, "Listening: a warm jacket", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{audiocard(["19.1 · NATURAL", "19.1 · SLOW"])}
{sub("A", "Paulo, Ana's brother, is shopping in New York. Listen at natural speed. What does he buy?", "2 min", "19.1")}
<p style="margin:.3mm 0;font-size:8.9pt">{ch(gist, gist[0])}</p></div>{img('B', 40, 27)}</div>
{sub("B", "Listen again and complete.", "4 min")}
<ol style="line-height:1.6;font-size:8.6pt;margin:0;columns:2;column-gap:5mm">{gpl}</ol>
{sub("C", "True or false? Correct the false sentences.", "3 min")}
<div style="font-size:8.6pt">{twocol(tfl, 2)}</div>
{sub("D", "Think about it. Discuss with your teacher.", "3 min")}
<ol style="line-height:1.4;font-size:8.7pt;margin:0"><li>Why does Paulo say "I always forget"? {R("In Brazil, the price on the tag already includes taxes.") if T else ""}</li><li>What do you always check before you buy clothes: the size, the material, the price, the return policy?</li></ol>
<div class="box sand" style="margin-top:1mm"><h4>NOTICE: USEFUL CHUNKS</h4><i>Can I help you find anything? · You've come to the right place. · Here you go. · It's a great deal. · to go with it · Great choice. · It's freezing outside!</i></div>""",
    22, """<ol><li>B: in 5 and 6, there are two gaps in one line. Clothing sizes in the US: <i>small, medium, large</i>, or numbers (women: 2, 4, 6…; men's pants: waist and length in inches).</li>
<li>C: tell the student to add 5–9% to prices in many US stores; it depends on the state and city.</li></ol>""")

    # Page 3 - Language focus
    fs = [("My coat isn't warm ___.", "enough"), ("It's a bit ___ tight around the shoulders.", "too"), ("Do you have a bigger ___?", "one"),
          ("We've sold out of the black ___.", "ones"), ("It's long ___ too.", "enough"), ("These wool ___ are on sale too.", "ones")]
    fsl = "".join(f"<li><i>{s.replace('___', A(a, 'min-width:14mm'))}</i></li>" for s, a in fs)
    b.page(f"""{sec(3, "Language focus: too, enough, one / ones", "8 min")}
{sub("A", "Complete the sentences from the dialogue with too, enough, one or ones.", "2 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0;columns:2;column-gap:5mm">{fsl}</ol>
{sub("B", "Complete the rules. Choose.", "3 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0"><li><i>It's too tight</i> means it's {ch(["more than I want", "perfect"], "more than I want")}.</li>
<li><i>Enough</i> goes {ch(["before", "after"], "after")} an adjective: <i>long enough</i>.</li>
<li><i>Enough</i> goes {ch(["before", "after"], "before")} a noun: <i>enough money</i>.</li>
<li>We use <i>one / ones</i> {ch(["so we don't repeat a noun", "for uncountable nouns"], "so we don't repeat a noun")}: <i>a bigger one = a bigger jacket</i>.</li>
<li><i>It's very expensive</i> means {ch(["I won't buy it", "it costs a lot, but I might buy it"], "it costs a lot, but I might buy it")}; <i>It's too expensive</i> means I won't buy it.</li></ol>
{sub("C", "Correct or incorrect? Choose.", "3 min")}
<ol style="line-height:1.6;font-size:8.9pt;margin:0"><li>These shoes aren't enough comfortable. {ch(["correct", "incorrect"], "incorrect")} {R("→ comfortable enough") if T else ""}</li><li>It's much too expensive for me. {ch(["correct", "incorrect"], "correct")}</li><li>I don't like the blue shirt. Can I see the white? {ch(["correct", "incorrect"], "incorrect")} {R("→ the white one") if T else ""}</li><li>We don't have enough time to try everything on. {ch(["correct", "incorrect"], "correct")}</li></ol>
<div class="box sand"><h4>RULE</h4><b>too</b> + adjective = a problem (<i>too tight</i>) · adjective + <b>enough</b> = OK (<i>big enough</i>) · <b>not</b> + adjective + <b>enough</b> = a problem (<i>not warm enough</i>) · <b>enough</b> + noun (<i>enough money</i>). Use <b>one</b> (singular) and <b>ones</b> (plural) so you don't repeat the noun. More on the next page: <b>Grammar reference</b>.</div>""",
    26, """<ol><li>A: draw a scale: <i>not big enough · big enough · too big</i>.</li>
<li>B: in 5, point out that <i>very</i> is not a problem; <i>too</i> is. Brazilians often use <i>very</i> where English needs <i>too</i>.</li></ol>""")

    grammar_ref.too_enough_one(b)

    # Page 5 - Vocabulary lab
    uk = [("the register", "the till"), ("a store", "a shop"), ("pants", "trousers"), ("sneakers", "trainers"), ("a sales clerk", "a shop assistant"), ("a fitting room", "a changing room")]
    ukl = "".join(f"<tr><td>{a}</td><td>{A(u, 'min-width:24mm')}</td></tr>" for a, u in uk)
    mt = [("leather", "shoes, jackets"), ("cotton", "T-shirts"), ("silk", "ties"), ("wool / cashmere", "sweaters"), ("denim", "jeans")]
    mtl = "".join(f"<li><b>{m}</b> {A(c, 'min-width:22mm')}</li>" for m, c in mt)
    b.page(f"""{sec(4, "Vocabulary lab: store words and materials", "4 min")}
<div style="display:flex;gap:4mm;align-items:flex-start"><div style="width:72mm">
{sub("A", "American or British? Write the British word.", "2 min")}
<div class="bank" style="font-size:8.2pt">a changing room · a shop · a shop assistant · the till · trainers · trousers</div>
<table style="font-size:8.5pt;margin:.5mm 0"><tr><th>American</th><th>British</th></tr>{ukl}</table></div><div style="flex:1">
{sub("B", "What are these materials usually used for?", "2 min")}
<div class="bank" style="font-size:8.2pt">jeans · shoes, jackets · sweaters · T-shirts · ties</div>
<ul style="line-height:1.6;font-size:8.6pt;margin:0;padding-left:4mm">{mtl}</ul>
<div style="margin-top:1mm">{img('C', 34, 18)}</div></div></div>
<div class="box sand"><h4>WATCH OUT: FALSE FRIENDS AND WORD CHOICE</h4>
<table style="margin:0;font-size:8.2pt"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>Can I prove it?</td><td><b>Can I try it on?</b></td><td>we <i>try on</i> clothes; <i>prove</i> = show that something is true.</td></tr>
<tr><td>These jeans are in promotion.</td><td><b>These jeans are on sale.</b></td><td>a <i>promotion</i> is a better job or a marketing campaign.</td></tr>
<tr><td>I need new tennis.</td><td><b>I need new sneakers.</b></td><td><i>tennis</i> is the sport.</td></tr>
<tr><td>That jacket stays well on you.</td><td><b>That jacket looks good on you / suits you.</b></td><td>for clothes, use <i>look good on</i> or <i>suit</i>; <i>fit</i> = the right size.</td></tr></table></div>
{sec(5, "Pronunciation lab: -teen or -ty?", "4 min")}
<p class="small" style="margin:.3mm 0">Numbers ending in <i>-teen</i> are stressed at the end and have a clear /t/: <i>thir<b>TEEN</b></i>. Numbers ending in <i>-ty</i> are stressed at the start, and in American English the <i>t</i> sounds like a quick /d/: <i><b>THIR</b>ty</i> /ˈθɜrdi/.</p>
{audiocard(["19.2"])}
{sub("A", "Listen and repeat. Then your teacher says five prices. Write them down. Were you right?", "4 min", "19.2")}
<p style="margin:.3mm 0;font-size:8.8pt;line-height:1.55">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S192))}</p>""",
    23, """<ol><li>A: in British English, <i>pants</i> means underwear, so <i>pants</i> in London can be embarrassing! <i>Sneakers</i> is US; <i>trainers</i> is UK.</li>
<li>Dictate prices like <i>$13.50, $30, $15.99, $50</i>. Materials work as adjectives: <i>a cotton T-shirt</i>.</li></ol>""")

    # Page 6 - Practice
    pc = [(["enough warm", "warm enough"], "warm enough"), (["ones", "one"], "ones"), (["too", "very"], "too"), (["one", "ones"], "one"),
          (["enough money", "money enough"], "enough money"), (["too much", "too many"], "too many"), (["one", "ones"], "one")]
    p = [ch(o, a) for o, a in pc]
    rw = [("The pants are short. (long enough)", "The pants aren't long enough."), ("The sweater is very big. I can't wear it. (too)", "The sweater is too big."),
          ("I can't buy this. I only have $50. (enough money)", "I don't have enough money to buy this."), ("This store is very expensive for students. (too … for … to)", "This store is too expensive for students to shop in."),
          ("I don't like these sneakers. Show me the red sneakers. (ones)", "Show me the red ones.")]
    rwl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw)
    b.page(f"""{sec(6, "Practice", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Paulo writes to his sister Ana. Choose the correct words.", "4 min")}</div>{img('D', 30, 20)}</div>
<div class="box" style="line-height:1.95;font-size:9pt"><b>From: Paulo · To: Ana</b><br>Hi sis! Good news: I finally bought a jacket for Iceland. My old coat wasn't {p[0]}, and the boots I have are old too, so I need new {p[1]}. The first jacket I tried was {p[2]} tight, so the clerk brought me a bigger {p[3]}. It was on sale, but I still didn't have {p[4]} for the boots, so I'll buy them next week. New York is crazy before the holidays: there are {p[5]} people in every store! Hey, Danny told me he only buys second-hand clothes now. Maybe I'll give him my old coat. He needs a warm {p[6]} for his trip south! Love, Paulo</div>
{sub("B", "Rewrite the sentences with the words in brackets.", "4 min")}
<ol style="line-height:1.55;font-size:8.8pt;margin:0">{rwl}</ol>""",
    24, """<ol><li>A: in the last gap, <i>one</i> = a coat. Danny is going to travel south in Brazil and South America (his gap year), where winters can be cold.</li>
<li>B: accept other correct answers, e.g. <i>The sweater is much too big.</i></li></ol>""")

    # Page 7 - Speaking
    b.page(f"""{sec(7, "Speaking: can I try it on?", "12 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>asking for an item</th><th>trying on</th><th>deciding</th><th>paying and returns</th></tr>
<tr><td><i>Do you have this in black / in a medium / in a size 10? · Do you have a bigger one?</i></td><td><i>Can I try it on? · Where are the fitting rooms? · It's a bit too tight.</i></td><td><i>I'll take it. · I think I'll leave it. · It doesn't really suit me.</i></td><td><i>Can I pay by card? · What's your return policy? · Can I get a refund?</i></td></tr></table></div>
{sub("A", "Role-plays. Take turns as the sales clerk and the customer. You are in a clothes store abroad.", "7 min")}
<ol style="line-height:1.45;font-size:8.8pt;margin:0"><li><b>Customer:</b> you want a sweater, a shirt and a pair of pants. You like a blue sweater, but you'd prefer it in black.</li>
<li><b>Customer:</b> you like a jacket and a pair of shoes. Ask for another color and your size. Try them on and decide.</li>
<li><b>Clerk:</b> try to sell a leather jacket to your customer. Talk about the material, the price and the sale.</li></ol>
<p style="margin:.3mm 0;font-size:8.6pt">{R("Teacher's card: 1 the black sweaters are sold out; only the pants are in the customer's size. 2 the shoes are a bit too small and there isn't a bigger one; the jacket fits. 3 you're the customer: the jacket is too expensive, so say you'll leave it, politely.") if T else ""}</p>
{sub("B", "Long turn. Prepare for one minute, then talk for two minutes about a shopping experience you remember.", "3 min")}
<ul style="line-height:1.45;font-size:8.9pt;margin:0"><li>where you were (at home or abroad) and what you wanted</li><li>problems with sizes, colors or prices</li><li>what you bought, or why you left it</li></ul>
{sub("C", "Talking point. Discuss with your teacher.", "2 min")}
<ol style="line-height:1.5;font-size:8.9pt;margin:0"><li>Online or in the store: which is better for buying clothes? Why?</li><li>Should prices always include taxes? Why?</li></ol>""",
    30, """<ol><li>A: play the clerk first in role-play 1 and follow the teacher's card. Push for <i>too / enough / one</i> in every role-play.</li>
<li>B: don't interrupt; note mistakes for the error log (page 8), especially <i>prove it</i> and <i>enough big</i>.</li></ol>""")

    # Page 8 - Wrap-up
    cd = ["I can ask for sizes and colors and try things on in a store.", "I can use too, enough and one / ones.", "I can pay and ask about returns."]
    cdr = "".join(f"<tr><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for s in cd)
    b.page(f"""{sec(8, "Wrap-up and homework", "4 min")}
{sub("A", "Can-do check", "1 min")}
<table class="ck" style="font-size:8.6pt"><tr><th>In English…</th><th style="width:16mm">Easy!</th><th style="width:16mm">Sometimes</th><th style="width:16mm">Not yet</th></tr>{cdr}</table>
{sub("B", "My language notes. Write three corrections from today's class.", "2 min")}
<div style="display:flex;gap:5mm;font-size:8.6pt"><div style="flex:1"><b>I said…</b>{lines(3)}</div><div style="flex:1"><b>Better:</b>{lines(3)}</div></div>
{sub("C", "Homework: writing (100–150 words)", "1 min")}
<p style="margin:.3mm 0"><b>An online product review.</b> Write a review of a piece of clothing you bought. Read Paulo's review first.</p>
<div class="box" style="font-size:8.6pt;line-height:1.4;margin:.5mm 0"><b>★★★★☆ Warm, light and great for travel</b><br><i>I bought this down jacket for a photo trip to Iceland, and I'm very happy with it. It's warm enough for temperatures below zero, but it's light enough to carry in a backpack. It's also waterproof, which is important when you're outside all day. One tip: the sizes are small. The medium was too tight around the shoulders, so I took a large, and it fits perfectly. I wanted the black one, but it was sold out, so I got the navy one. The price wasn't cheap, but it was on sale, so it was a good deal. Why four stars and not five? The pockets aren't big enough for my camera batteries and gloves. Still, I'd buy it again.</i></div>
<p class="small" style="margin:.3mm 0">Checklist: ☐ what you bought and why &nbsp;☐ the size and how it fits &nbsp;☐ too / enough / one &nbsp;☐ one good point and one bad point &nbsp;☐ 100–150 words</p>
{lines(5)}""",
    30, """<ol><li>B (error log): during the lesson, note 3–5 real mistakes. Here, the student writes what they said and the better version; guide them to self-correct first.</li>
<li>C: check <i>too / enough</i> word order and <i>fit</i> (size) vs <i>suit</i> (style, color).</li></ol>""")

    script = "".join(f"<p style='margin:.5mm 0'><b>{l.split(': ', 1)[0]}:</b> {l.split(': ', 1)[1]}</p>" for l in S191)
    b.extra("Audio script", f"""
{sub("19.1", "A warm jacket (natural and slow)")}
<div style="line-height:1.3;font-size:8.6pt">{script}</div>
{sub("19.2", "Repeat: teen or ty")}
<p>{" · ".join(S192)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 19 - At the clothes shop")
