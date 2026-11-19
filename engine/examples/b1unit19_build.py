# Speak! Progress B1 - Unit 19 "At the clothes shop" (all English) - lean B1 format (rebuilt 2026-11-19)
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
    def _fill(s, a):
        for x in a.split(" / "):
            s = s.replace("___", A(x, "min-width:12mm"), 1)
        return s

    # 1 Warm-up
    cover = cover_html(T, "LEVEL B1 · UNIT 19", "At the clothes shop", "Shopping for clothes abroad · <b>too, enough, one / ones</b>",
                       [("YOU CAN", "ask for sizes and colors, try things on, decide, pay and ask about returns"),
                        ("LANGUAGE", "a bargain · on sale · out of stock · a refund · Do you have it in a medium? · It's too tight · a bigger one"),
                        ("PRONUNCIATION", "-teen or -ty? thirteen, thirty")])
    sw = [("This jacket was on ___ when I bought it. It usually costs twice as much.", "sale"), ("These pants are too long. I'll take them to a ___.", "tailor"),
          ("I only paid $10 for this sweater. It was a real ___!", "bargain"), ("They give you a 10% ___ if you buy three items.", "discount"),
          ("He didn't like the shirt, so I took it back and asked for a ___.", "refund"), ("The book was out of ___. The clerk said to come back on Friday.", "stock")]
    swl = "".join(f"<li>{s.replace('___', A(a, 'min-width:16mm'))}</li>" for s, a in sw)
    b.page(f"""{sec(1, "Warm-up: going shopping", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["Where do you usually buy clothes: in stores or online? Why?", "Have you ever bought clothes in another country? Was it easy?", "Do you enjoy shopping, or do you just buy what you need?"], "START TALKING")}</div></div>
{sub("A", "In the store. Complete the sentences with the words from the box.", "3 min")}
<div class="bank">bargain · discount · refund · sale · stock · tailor</div>
<ol style="line-height:1.5;font-size:8.6pt;margin:0;columns:2;column-gap:5mm">{swl}</ol>
{talk(["Tell me about the best bargain you've ever found.", "Have you ever asked for a refund? What happened?"], "USE THE WORDS")}""",
    26, """<ol><li>Top box: 4 minutes.</li>
<li>A: <i>on sale</i> = cheaper than usual (US); <i>for sale</i> = available to buy. <i>Out of stock</i> = the store doesn't have it now.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Dialogue: Paulo buys a winter jacket in New York · complete · Talk about it", "too, enough, one / ones",
                      "Complete from the dialogue · choose the rule · Use it (oral)", "Functional language · -teen or -ty? (19.2) · clothes store role-plays",
                      "Paulo's message to Ana · US/UK store words · word choice · writing"),
        "The Linguahouse listening is a short, generic dialogue in a clothes store. Our original dialogue happens abroad, as the school's choice for practical units: Paulo, Ana's brother and a travel photographer (B1 Unit 15), is in a store in New York. He needs a warm jacket for a photo trip to Iceland, asks for another color and size, tries it on, decides, pays and asks about returns. The store is fictional. Verified fact: in the United States, the price on the tag usually doesn't include sales tax; the tax is added at the register, and the rate depends on the state and city. Many other countries, Brazil included, show prices with taxes included. In the homework, Paulo writes to his sister Ana.", "Students say <i>Can I prove it?</i> (try it on), <i>It's in promotion</i> (on sale), <i>tennis</i> for sneakers, <i>It stays well on you</i> (it looks good on you / it suits you), <i>enough big</i>, <i>too much expensive</i> and <i>a bigger</i> without <i>one</i>. Pronunciation: <i>thirTEEN</i> vs <i>THIRty</i>, a real problem with prices.",
        "Track 19.1 A warm jacket (natural and slow) · Track 19.2 Repeat: teen or ty"))

    # 2 Listening
    gist = ["a jacket", "a jacket and gloves", "nothing"]
    gp = [("Do you have it ___ black?", "in"), ("I'm afraid we've ___ the black ones.", "sold out of"), ("Do you have it in a ___?", "medium"),
          ("The ___ are over there, on the left.", "fitting rooms"), ("It's ___ off, so it's $189, plus ___.", "30% / tax"), ("I'll ___ the gloves. But I'll ___ the jacket.", "leave / take")]
    gpl = "".join(f"<li>{_fill(s, a)}</li>" for s, a in gp)
    b.page(f"""{sec(2, "Listening: a warm jacket", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{audiocard(["19.1 · NATURAL", "19.1 · SLOW"])}
{sub("A", "Paulo, Ana's brother, is shopping in New York. Listen. What does he buy?", "2 min", "19.1")}
<p style="margin:.3mm 0;font-size:8.9pt">{ch(gist, gist[0])}</p></div>{img('B', 40, 27)}</div>
{sub("B", "Listen again and complete.", "4 min")}
<ol style="line-height:1.6;font-size:8.6pt;margin:0;columns:2;column-gap:5mm">{gpl}</ol>
{talk(["Why does Paulo say &ldquo;I always forget&rdquo; about the tax?", "What do you always check before you buy clothes: the size, the material, the price, the return policy?", "Online or in the store: which is better for clothes? Why?"])}""",
    26, """<ol><li>A–B: 6 minutes. In 5 and 6, there are two gaps. US clothing sizes: <i>small, medium, large</i>, or numbers.</li>
<li>Talk about it: 6 minutes. 1: in Brazil the price on the tag includes taxes; in many US stores 5–9% is added at the register.</li></ol>""")

    # 3 Grammar reference
    lean.grammar_in_class(b, grammar_ref.too_enough_one)

    # 4 Practice
    fs = [("My coat isn't warm ___.", "enough"), ("It's a bit ___ tight around the shoulders.", "too"), ("Do you have a bigger ___?", "one"), ("We've sold out of the black ___.", "ones")]
    fsl = "".join(f"<li><i>{s.replace('___', A(a, 'min-width:14mm'))}</i></li>" for s, a in fs)
    use = ["Describe something you own that's too big, too small or not … enough.", "Is your city warm enough in winter? Is it too hot in summer?", "Do you have enough time to study English? Why?",
           "Your teacher shows two things: <i>Which one do you prefer? Why not the other one?</i>", "Is anything in your city too expensive for you to buy? What?"]
    b.page(f"""{sec(4, "Practice: too, enough, one / ones", "10 min")}
{sub("A", "Complete the sentences from the dialogue with too, enough, one or ones.", "2 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0;columns:2;column-gap:5mm">{fsl}</ol>
{sub("B", "Choose.", "2 min")}
<p style="margin:.3mm 0;font-size:8.9pt;line-height:1.7">These shoes aren't {ch(["enough comfortable", "comfortable enough"], "comfortable enough")}. &nbsp;·&nbsp; It's {ch(["too much expensive", "much too expensive"], "much too expensive")}. &nbsp;·&nbsp; Can I see the white {ch(["one", "—"], "one")}?</p>
<div class="box sand"><h4>RULE</h4><b>too</b> + adjective = a problem · adjective + <b>enough</b> = OK · <b>not</b> + adjective + <b>enough</b> = a problem · <b>enough</b> + noun. Use <b>one</b> (singular) and <b>ones</b> (plural) so you don't repeat the noun. See the <b>Grammar reference</b> on page 3.</div>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    24, """<ol><li>A–B: 4 minutes. Draw a scale: <i>not big enough · big enough · too big</i>. <i>Very</i> is not a problem; <i>too</i> is.</li>
<li>Use it: 6 minutes, all oral. Correct <i>enough big</i> and <i>a bigger</i> (without <i>one</i>).</li></ol>""")

    # 5 Speaking
    b.page(f"""{sec(5, "Speaking: can I try it on?", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>asking for an item</th><th>trying on</th><th>deciding</th><th>paying and returns</th></tr>
<tr><td><i>Do you have this in black / in a medium / in a size 10? · Do you have a bigger one?</i></td><td><i>Can I try it on? · Where are the fitting rooms? · It's a bit too tight.</i></td><td><i>I'll take it. · I think I'll leave it. · It doesn't really suit me.</i></td><td><i>Can I pay by card? · What's your return policy? · Can I get a refund?</i></td></tr></table></div>
{audiocard(["19.2"])}
{sub("A", "-teen or -ty? Listen and repeat: thirTEEN / THIRty. Then your teacher says five prices: write them.", "4 min", "19.2")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.55">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S192))}</p>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("B", "Role-plays. Take turns as the sales clerk and the customer in a clothes store abroad.", "10 min")}
<ol style="line-height:1.4;font-size:8.7pt;margin:0"><li><b>Customer:</b> you want a sweater, a shirt and pants. You like a blue sweater, but you'd prefer it in black.</li>
<li><b>Customer:</b> you like a jacket and a pair of shoes. Ask for another color and your size. Try them on and decide.</li>
<li><b>Clerk:</b> try to sell a leather jacket. Talk about the material, the price and the sale.</li></ol>
<p style="margin:.3mm 0;font-size:8.5pt">{R("Teacher's card: 1 the black sweaters are sold out; only the pants are in the customer's size. 2 the shoes are a bit too small and there isn't a bigger one; the jacket fits. 3 as the customer: it's too expensive, so leave it politely.") if T else ""}</p></div>{img('D', 28, 28)}</div>
{talk(["Tell me about a shopping experience you remember, at home or abroad.", "Should prices always include taxes? Why?"])}""",
    28, """<ol><li>A: dictate prices like <i>$13.50, $30, $15.99, $50</i>. B: push for <i>too / enough / one</i> in every role-play.</li>
<li>Last 3 minutes: wrap-up (two corrections and <i>Can you shop for clothes in English?</i>).</li></ol>""")

    # H Homework
    pc = [(["enough warm", "warm enough"], "warm enough"), (["too", "very"], "too"), (["one", "ones"], "one"), (["enough money", "money enough"], "enough money"), (["too much", "too many"], "too many")]
    p = [ch(o, a) for o, a in pc]
    uk = [("pants", "trousers"), ("sneakers", "trainers"), ("a fitting room", "a changing room")]
    ukl = " &nbsp;·&nbsp; ".join(f"{a} = {A(u, 'min-width:20mm')}" for a, u in uk)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Paulo writes to his sister Ana. Choose the correct words.", "")}</div>{img('C', 28, 18)}</div>
<div class="box" style="line-height:1.8;font-size:8.8pt;margin:.5mm 0"><b>From: Paulo · To: Ana</b><br>Hi sis! I finally bought a jacket for Iceland. My old coat wasn't {p[0]}. The first jacket I tried was {p[1]} tight, so the clerk brought me a bigger {p[2]}. It was on sale, but I still didn't have {p[3]} for the boots. New York is crazy before the holidays: there are {p[4]} people in every store! Love, Paulo</div>
{sub("B", "American or British? Write the British word.", "")}
<p style="margin:.3mm 0;line-height:1.9;font-size:8.6pt">{ukl}</p>
{lean.watch_out([("Can I prove it?", "Can I try it on?", "we <i>try on</i> clothes."), ("These jeans are in promotion.", "These jeans are on sale.", "a <i>promotion</i> is a better job or a campaign."), ("That jacket stays well on you.", "That jacket looks good on you / suits you.", "<i>fit</i> = the right size.")])}
{lean.writing_task(sub, "An online product review: write a review of a piece of clothing you bought.", "I bought this… for… It's warm enough for… The medium was too…, so I took a bigger one.", ["the size and how it fits", "too / enough / one", "one good and one bad point", "100–150 words"], "I can shop for clothes and use too, enough and one.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class. In British English, <i>pants</i> means underwear! When you correct the writing, check <i>too / enough</i> word order and <i>fit</i> vs <i>suit</i>.</p>""")

    script = "".join(f"<p style='margin:.5mm 0'><b>{l.split(': ', 1)[0]}:</b> {l.split(': ', 1)[1]}</p>" for l in S191)
    b.extra("Audio script", f"""
{sub("19.1", "A warm jacket (natural and slow)")}
<div style="line-height:1.3;font-size:8.6pt">{script}</div>
{sub("19.2", "Repeat: teen or ty")}
<p>{" · ".join(S192)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 19 - At the clothes shop")
