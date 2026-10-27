# Speak! Essentials A1 - Unit 29 "Shopping for clothes" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
from speak_engine import *
setup(band="A1 · UNIT 29", audio_json="audio_a1-unit-29.json", img_dir="img")

PHOTOS = [("A", "coat", "coat"), ("B", "dress", "dress"), ("C", "jeans", "jeans"), ("D", "shirt", "shirt"),
          ("E", "shoes", "shoes"), ("F", "skirt", "skirt"), ("G", "socks", "socks"), ("H", "sweater", "sweater")]

_r = json.load(open("roteiro.json"))["units"]["a1-unit-29"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["29.1 Store"].split("\n")]
S292 = [x.split(": ", 1)[1] for x in _r["29.2 Repeat words"].split("\n")]
S293 = [x.split(": ", 1)[1] for x in _r["29.3 Repeat phrases"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LEVEL A1 · UNIT 29", "Shopping for clothes", "Clothes · <b>useful phrases in a store · how much / how many</b>",
                       [("YOU CAN", "ask for clothes, sizes, colors and prices, try things on and pay"),
                        ("LANGUAGE", "Do you have any sweaters? · Where can I try it on? · It doesn't fit."),
                        ("PRONUNCIATION", "clothes /kloʊðz/ · shirt ≠ skirt · sweater /ˈswetər/ · suits /suːts/")])
    b.page(f"""{sec(1, "Warm-up: clothes", "8 min")}
{sub("A", "Look at the photos. Write the word under each photo.", "3 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(w for _, w, _ in PHOTOS)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Talk about it.", "5 min")}
<ol><li>What are you wearing today?</li><li>Which three words are always plural? Why? {R("jeans, shoes, socks: they have two parts (two legs, two feet).")}</li><li>How many pairs of jeans do you have? And pairs of shoes?</li></ol>""",
    27, """<ol><li>A: drill <b>clothes</b> /kloʊðz/: one syllable, like <i>close</i> the door. Many Brazilians say "clo-thes" with two syllables.</li>
<li>B: we say <b>a pair of</b> jeans / shoes / socks, and they take a plural verb: <i>My jeans <b>are</b> new.</i></li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>8 items of clothing with photos · a pair of</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Lucy buys a sweater in a store in Chicago</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Store phrases: who says it? · how much / how many · it / they</td><td>3</td></tr>
<tr><td>4 Pronunciation lab</td><td>5 min</td><td>Clothes words · store phrases</td><td>4</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Choose the correct phrase · Ana buys sneakers in São Paulo</td><td>5</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Store role-play with an information gap · shoes and shopping</td><td>6</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>7</td></tr></table>
<div class="box"><h4>HOW THIS GUIDE WORKS</h4>Every page looks like the Student Book page with the same number. Your notes are in the <b>yellow box</b>.
<span class="red">Answers in red</span> are not in the Student Book. The <span class="time">5 min</span> chips show the time for each activity. Audio scripts are on the last page.</div>
<div class="box sand"><h4>THE STORY CONTINUES</h4>It's December in Chicago and it's very cold. Lucy (the weekend barista at City Coffee) needs a warm sweater for the City Coffee holiday party. In a store downtown, the small is too big, so she tries an extra small in red. It's on sale for $45 and she pays by credit card. In São Paulo, Ana buys sneakers for Leo and pays with Pix (page 5).</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>The false friend <i>prove</i>: <i>Can I prove it?</i> ✗ → <b>Can I try it on?</b> Sizes: <i>I'm small size</i> ✗ → <b>I'm a small / I usually wear a small.</b> Plural clothes: <i>The jeans is expensive</i> ✗ → <b>These jeans are expensive. How much are they?</b> And <i>in credit card</i> ✗ → <b>by credit card</b>.</div>
<div class="box"><h4>AUDIO</h4>Track 29.1 At the store (slow and natural) · Track 29.2 Clothes words · Track 29.3 Store phrases</div>""")

    # Page 2
    gist = [("What does Lucy want to buy?", "a sweater"), ("Why does she need it?", "for the City Coffee holiday party"),
            ("What size does she usually wear?", "a small"), ("What color does she choose?", "red"),
            ("How much is it?", "$45 (it's on sale)"), ("How does she pay?", "by credit card")]
    gl = [f'<li value="{i+1}">{q}<div class="wline">{R(a)}</div></li>' for i, (q, a) in enumerate(gist)]
    gaps = [("Clerk", "Good afternoon! Can I", "help", "you?"), ("Lucy", "Yes, please.", "Do you have", "any sweaters?"),
            ("Clerk", "Yes, we do.", "What size", "are you?"), ("Lucy", "I like the red one. Where can I", "try it on", "?"),
            ("Lucy", "It's really nice, but it doesn't", "fit", ". It's too big."), ("Clerk", "Oh, that looks great on you! Red really", "suits", "you."),
            ("Lucy", "Thanks! It's perfect.", "How much", "is it?"), ("Clerk", "How would you like to", "pay", ", in cash or by card?")]
    gpl = "".join(f"<p><b>{n}:</b> {a} {A(g, 'min-width:22mm')} {c}</p>" for n, a, g, c in gaps)
    b.page(f"""{sec(2, "Listening: at the store", "10 min")}
<p>It's December in Chicago, and it's very cold. Lucy is in a clothes store downtown. She needs something warm for a party.</p>
{audiocard(["29.1 · SLOW", "29.1 · NATURAL"])}
{sub("A", "Listen and answer the questions.", "4 min", "29.1 · SLOW")}
{twocol(gl, 4)}
{sub("B", "Listen again and complete the sentences.", "4 min", "29.1 · NATURAL")}
<div class="msg" style="max-width:none;padding:2mm 4mm;line-height:1.7">{gpl}</div>
{sub("C", "The small sweater doesn't fit. What's the problem?", "2 min")}
<div class="wline">{R("It's too big, so Lucy tries an extra small.")}</div>""",
    31, """<ol><li>A: <b>slow</b> version. Teach <b>try it on</b> (put on clothes in the store to see if they fit) and <b>changing rooms</b> (the small rooms where you do it).</li>
<li>B: <b>natural</b> version. <b>It fits</b> = the size is right. <b>It suits you</b> = it looks good on you (color, style). <b>On sale</b> = cheaper than usual.</li></ol>""")

    # Page 3
    phr = [("size", "What size are you?", "S", "I usually wear a small.", "C"),
           ("trying on", "Where can I try it on?", "C", "The changing rooms are over there.", "S"),
           ("opinion", "It looks good on you. / It suits you.", "S", "It doesn't fit. / I don't think I like it.", "C"),
           ("colors", "What colors does it come in?", "C", "It comes in blue, gray and red.", "S"),
           ("price", "How much is it? / How much does it cost?", "C", "It's $45. / It's on sale!", "S"),
           ("paying", "How would you like to pay?", "S", "By credit card. / In cash. / With Pix.", "C")]
    box = lambda x: f"<td style='width:9mm;text-align:center'><b>{R(x) if T else '☐'}</b></td>"
    pt = "".join(f"<tr><td class='small'><b>{t}</b></td><td>{q}</td>{box(a)}<td>{r}</td>{box(c)}</tr>" for t, q, a, r, c in phr)
    b.page(f"""{sec(3, "Language focus: in a clothes store", "10 min")}
{sub("A", "Who says it? Write S (sales clerk) or C (customer).", "4 min")}
<table style="table-layout:fixed;font-size:9pt"><tr><th style="width:20mm"></th><th>Question</th><th style="width:9mm">S/C</th><th>Answer</th><th style="width:9mm">S/C</th></tr>{pt}</table>
{sub("B", "How much or how many? Choose the correct word.", "3 min")}
<ol><li>How {ch(["much", "many"], "much")} is this coat? It's $120.</li>
<li>How {ch(["much", "many"], "many")} colors does it come in? Three.</li>
<li>How {ch(["much", "many"], "many")} pairs of jeans do you have?</li>
<li>How {ch(["much", "many"], "much")} money do you spend on clothes?</li></ol>
<div class="box sand"><h4>HOW MUCH / HOW MANY · IT / THEY</h4><b>How much</b> = a price, or things we can't count (money, time). <b>How many</b> + plural noun: How many <b>colors</b>? How many <b>pairs</b>?<br>
One item: <b>it</b>. This sweater: How much <b>is it</b>? Can I try <b>it</b> on? &nbsp;·&nbsp; Jeans, shoes, socks: <b>they</b>. These jeans: How much <b>are they</b>? Can I try <b>them</b> on?</div>""",
    26, """<ol><li>A: then drill the phrases as a mini dialogue: you are the clerk, the student is the customer; change roles. <b>suits</b> /suːts/.</li>
<li>B: countable and uncountable nouns come back in a later unit; here, just <i>much</i> for prices and money, <i>many</i> + plural.</li></ol>""")

    # Page 4
    b.page(f"""{sub("C", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>Can I prove it?</td><td><b>Can I try it on?</b></td><td><i>prove</i> = show something is true.</td></tr>
<tr><td>I'm small size.</td><td><b>I'm a small. / I wear a small.</b></td><td>Use <i>a</i> + small / medium / large.</td></tr>
<tr><td>Where I can try it on?</td><td><b>Where can I try it on?</b></td><td>Question order: <i>can</i> + I.</td></tr>
<tr><td>It's not fit.</td><td><b>It doesn't fit.</b></td><td><i>fit</i> is a verb: <i>doesn't</i>.</td></tr>
<tr><td>The jeans is expensive.</td><td><b>These jeans are expensive.</b></td><td>jeans = plural.</td></tr>
<tr><td>I'll pay in credit card.</td><td><b>I'll pay by credit card.</b></td><td><i>by</i> card, <i>in</i> cash.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "5 min")}
{audiocard(["29.2", "29.3"])}
{sub("A", "Clothes words. Listen and repeat.", "2 min", "29.2")}
<table style="table-layout:fixed;margin-top:0"><tr>{"".join(f"<td style='text-align:center'><b>{w}</b></td>" for w in S292)}</tr></table>
<div class="box" style="margin-top:1mm"><h4>LISTEN CAREFULLY</h4><b>clothes</b> /kloʊðz/ has one syllable. &nbsp;·&nbsp; <b>shirt</b> /ʃɜrt/ ≠ <b>skirt</b> /skɜrt/ &nbsp;·&nbsp; <b>sweater</b> /ˈswetər/ sounds like <i>wet</i>.</div>
{sub("B", "Store phrases. Listen and repeat.", "2 min", "29.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S293)}</div>""",
    24, """<ol><li>4A: contrast <b>shirt / skirt</b> and <b>shoes / socks</b>: you say one word, the student points at the photo on page 1.</li>
<li>4B: <i>try it on</i> sounds like one word: /traɪ ɪ tɑn/. Practice the phrases as a chain: question → answer.</li></ol>""")

    # Page 5
    cp = [(["I'm a large.", "I'm large size.", "It's a large."], "I'm a large.", "What size are you?"),
          (["Where I can try it on?", "Where can I try it on?", "Where do I can try it on?"], "Where can I try it on?", ""),
          (["It not fit.", "It doesn't fit.", "It don't fit."], "It doesn't fit.", "How is it?"),
          (["What colors does it come in?", "What colors it comes in?", "It comes in what colors?"], "What colors does it come in?", ""),
          (["How much is they?", "How many are they?", "How much are they?"], "How much are they?", "I love these boots!"),
          (["By credit card.", "In credit card.", "With credit card."], "By credit card.", "How would you like to pay?")]
    cpl = "".join(f"<li>{('<i>' + q + '</i> → ') if q else ''}{ch(o, a)}</li>" for o, a, q in cp)
    lines = [("Clerk", "Good morning! What are you looking for today?", 0), ("Ana", "Do you have any sneakers for my son?", 1),
             ("Clerk", "Yes, we do. What size does he wear?", 2), ("Ana", "He usually wears a thirty-eight.", 3),
             ("Clerk", "Here you are. They come in black and white.", 4), ("Ana", "Black, please. How much are they?", 5),
             ("Clerk", "They're on sale, only two hundred reais!", 6), ("Ana", "Great! I'll take them. Can I pay with Pix?", 7),
             ("Clerk", "Of course! Here's the QR code.", 8)]
    mix = [6, 1, 4, 7, 2, 5, 3]  # scrambled order of lines 1-7 in the SB
    mixl = "".join(f"<tr><td style='width:12mm;text-align:center'>{A(str(lines[k][2] + 1), 'min-width:8mm')}</td><td><b>{lines[k][0]}:</b> {lines[k][1]}</td></tr>" for k in mix)
    b.page(f"""{sec(5, "Practice", "8 min")}
{sub("A", "Choose the correct phrase.", "3 min")}
<ol>{cpl}</ol>
{sub("B", "Ana is in a store in São Paulo. Put the dialogue in order (2–8).", "5 min")}
<table style="table-layout:fixed;font-size:9.3pt"><tr><td style='width:12mm;text-align:center'><b>1</b></td><td><b>Clerk:</b> {lines[0][1]}</td></tr>{mixl}
<tr><td style='width:12mm;text-align:center'><b>9</b></td><td><b>Clerk:</b> {lines[8][1]}</td></tr></table>
<p class="small">Which words helped you find the order?</p>""",
    24, """<p>A: ask the student to say why the wrong options are wrong. B: Brazilian shoe sizes are different from US sizes, so a thirty-eight is a Brazilian size. <b>Pix</b> is the Brazilian instant payment system. When the order is correct, read the dialogue together: you are the clerk, then change roles.</p>""")

    # Page 6
    cat = [("winter coat", "S, M, L", "black, gray, green", "$89 (on sale)"), ("boots", "6 to 10", "brown, black", "$75"),
           ("jeans", "26 to 34", "blue, black", "$49"), ("dress", "S, M", "red, blue, white", "$60")]
    ct = "".join(f"<tr><td style='height:8mm'><b>{i}</b></td><td class='small'>{R(s)}</td><td class='small'>{R(c)}</td><td class='small'>{R(p)}</td></tr>" for i, s, c, p in cat)
    plan = [("1 Say hello and offer help.", "2 Say what you want."), ("3 Ask about size.", "4 Answer about size."),
            ("5 Show it. Say the colors.", "6 Choose a color. Ask where to try it on."), ("7 Say where the changing rooms are.", "8 It doesn't fit / you don't like it. Ask for another one."),
            ("9 Bring another one. Say it suits the customer.", "10 Ask the price."), ("11 Say the price. Ask about payment.", "12 Say how you want to pay.")]
    plt = "".join(f"<tr><td class='small'>{a}</td><td class='small'>{c}</td></tr>" for a, c in plan)
    b.page(f"""{sec(6, "Speaking", "12 min")}
{sub("A", "You are a customer in a store in Chicago. Choose two items. Ask your teacher (the sales clerk) and complete the table.", "7 min")}
<table style="table-layout:fixed;font-size:9pt;margin-bottom:1mm"><tr><th style="width:28mm">Item</th><th>Sizes</th><th>Colors</th><th>Price</th></tr>{ct}</table>
<table style="table-layout:fixed;margin-top:0"><tr><th>Sales clerk</th><th>Customer</th></tr>{plt}</table>
<p class="small">Now change roles. You are the sales clerk in a store in Brazil. Invent the sizes, colors and prices in reais.</p>
{sub("B", "Talk about shopping.", "5 min")}
<div class="bank">boots · flip-flops · heels · sandals · slippers · sneakers</div>
<ol><li>What shoes are you wearing now? When did you buy them? How much did they cost?</li>
<li>Which of the shoes in the box do you have at home?</li>
<li>Do you prefer shopping for clothes online or in a store? Why?</li></ol>""",
    28, """<ol><li>A: information gap: the answers in red are for you only. Follow the plan; the student completes the table. Then the student is the clerk and you are the customer: ask for a size that doesn't exist!</li>
<li>B: <b>flip-flops</b> are very Brazilian. <b>heels</b> = high-heeled shoes. <b>slippers</b> = shoes for the house.</li></ol>""")

    # Page 7
    pc = [("Unit 24", "I can say -ed correctly: played, worked, started."), ("Unit 25", "I can make past questions and negatives with did / didn't."),
          ("Unit 26", "I can use irregular past verbs: went, ate, saw, bought."), ("Unit 28", "I can ask questions in the present and past with who, whose, which…"),
          ("Unit 29", "I can buy clothes: ask about sizes, colors and prices, try things on and pay.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = ["sale", "size", "try", "changing", "fit", "suits", "much", "by"]
    def g(i): return f"({i+1}) {A(hw[i], 'min-width:18mm')}"
    msg = (f"Hi Mia! I went shopping yesterday. There was a big {g(0)} at a store downtown, so I bought a new coat. "
           f"I usually wear a medium, but the medium was the wrong {g(1)}. I wanted to {g(2)} on a small, but the {g(3)} rooms were full! "
           f"Finally, the small was perfect. It {g(4)} me, and the color really {g(5)} me. How {g(6)} was it? Only 150 reais! I paid {g(7)} card.")
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:15mm"></th><th>In English…</th><th style="width:20mm">Easy!</th><th style="width:20mm">Sometimes</th><th style="width:20mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Ana's message to Mia.</b> Complete with the words in the box.</p>
<div class="bank">by · changing · fit · much · sale · size · suits · try</div>
<div class="msg" style="max-width:none;line-height:2">{msg}</div>
<p style="margin-top:3mm"><b>2. At the store.</b> Write a dialogue (10 lines) between you and a sales clerk in a clothes store in your city. Use at least six phrases from page 3.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class: start with homework 2. Read the dialogue together (you are the clerk), then correct it. Check <i>try it on</i>, <i>it doesn't fit</i> and <i>by card</i>.</p>""")

    b.extra("Audio scripts", f"""
{sub("29.1", "At the store (slow and natural)")}
<p style="line-height:1.5">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("29.2", "Clothes words")}
<p>{" · ".join(S292)}</p>
{sub("29.3", "Store phrases")}
<p>{" ".join(S293)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essentials 29 - Shopping for clothes")
