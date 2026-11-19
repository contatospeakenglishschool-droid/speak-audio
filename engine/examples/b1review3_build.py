# Speak! Progress B1 - Review 3 (Units 21-29), all English - B1 review format (8 pages)
import sys, os, json
_h = os.path.dirname(os.path.abspath(__file__))
for _d in ("/home/claude/speak-audio/engine", os.path.join(_h, "..", "speak-audio", "engine"), os.path.join(_h, "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
_se.SERIES = "Progress"
setup(band="B1 · REVIEW 3", audio_json="audio_b1-review-3.json", img_dir="img")

PHOTOS = [("A", "hiking boots", "Unit 21"), ("B", "a zipper", "Unit 22"), ("C", "an ATM", "Unit 23"), ("D", "a canal", "Unit 24"),
          ("E", "a cathedral", "Unit 25"), ("F", "a desert", "Unit 26"), ("G", "a waterfall", "Unit 27"), ("H", "a luggage cart", "Unit 28")]
_r = json.load(open("roteiro.json"))["units"]["b1-review-3"]
SCRIPT = [tuple(x.replace("twenty-five", "25").split(": ", 1)) for x in _r["R3.1 Back from the south"].split("\n")]
S32 = [x.split(": ", 1)[1].split(". ", 1)[1] for x in _r["R3.2 Dictation: contractions and weak forms"].split("\n")]
S33 = [tuple(x.split(": ", 1)) for x in _r["R3.3 Dialogues"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def lines(n):
        return '<div class="wline"></div>' * n

    # Page 1 - Warm-up
    cover = cover_html(T, "LEVEL B1 · REVIEW 3", "Review 3", "Units 21–29 · adjective order · reported speech · unless · contrast · relative clauses · used to · extreme adjectives · polite requests · past tenses",
                       [("YOU CAN", "check what you learned in Units 21–29 and plan what to practice next"),
                        ("LANGUAGE", "an old green wool sweater · She told me… · in case · although · Tomás, who… · I got used to it · absolutely freezing · Would you mind…? · I'd never seen…"),
                        ("PRONUNCIATION", "contractions and weak forms: 'd, 's, such a")])
    b.page(f"""{sec(1, "Warm-up: photo memory", "6 min")}
{sub("A", "One photo from each unit. Write the word. Then say one sentence about it with the language of that unit.", "6 min")}
<div class="bank">an ATM · a canal · a cathedral · a desert · hiking boots · a luggage cart · a waterfall · a zipper</div>
{photo_grid(T, PHOTOS)}
<p class="small" style="margin-top:2mm"><b>Example:</b> a cathedral → <i>São Paulo Cathedral, which is Neo-Gothic, has a beautiful dome.</i></p>""",
    25, """<p>Photos A–H come from Units 21–28 (Unit 29 is in the listening). Push each unit's language: adjective order (21), reported speech (22), <i>unless / in case</i> (23), contrast linkers (24), non-defining relative clauses (25), <i>be / get used to</i> (26), extreme adjectives and <i>so / such</i> (27), polite requests (28).</p>""", cover=cover)

    b.extra("Review overview · 60 min", """
<table><tr><th>Stage</th><th>Time</th><th>Units</th><th>SB page</th></tr>
<tr><td>1 Warm-up: photo memory</td><td>6 min</td><td>21–28</td><td>1</td></tr>
<tr><td>2 Listening: back from the south</td><td>10 min</td><td>21–29</td><td>2</td></tr>
<tr><td>3 Grammar 1: adjective order, reported speech, unless, contrast, relative clauses</td><td>8 min</td><td>21–25</td><td>3</td></tr>
<tr><td>4 Grammar 2: correct Danny's email</td><td>8 min</td><td>26–29</td><td>4</td></tr>
<tr><td>5 Vocabulary and word choice</td><td>7 min</td><td>21–29</td><td>5</td></tr>
<tr><td>6 Pronunciation and social English</td><td>8 min</td><td>26–29</td><td>6</td></tr>
<tr><td>7 Speaking: long turn and role-play</td><td>9 min</td><td>21–29</td><td>7</td></tr>
<tr><td>8 Reflect and homework</td><td>4 min</td><td>21–29</td><td>8</td></tr></table>
<div class="box"><h4>HOW THIS GUIDE WORKS</h4>Every page looks like the Student Book page with the same number. Your notes are in the <b>yellow box</b>; <span class="red">answers in red</span> are not in the Student Book. This is a review: don't teach everything again. Let the student work, then focus on the mistakes that come back. The Grammar reference pages of Units 21–29 are useful here.</div>
<div class="box sand"><h4>THE STORY SO FAR</h4>Danny (Puck) is back at Mrs. Lima's hostel after his trip south: two weeks in Patagonia (Unit 21), the hermit Tomás (29) and three nights at a hotel in Buenos Aires (28). Over dinner with Ana (Neural2-F), Bruno (Fenrir) and Mrs. Lima (Vindemiatrix), he talks about Bruno's belt and his old sweater (21), the ATM problem (23), tourism (24) and the cold and wind (26–27). Ana passes on news from Carol (22, 27). December is summer in Patagonia; the strong wind there is well known. Dialogues: Carol (Leda) checks in at a hotel (Receptionist, Studio-O); Paulo (Neural2-I) tells Ana about Iceland (Unit 27). No new facts are stated.</div>
<div class="box"><h4>THE TOP 5 MISTAKES TO WATCH</h4>1. <i>a wool green old sweater</i> → <b>an old green wool sweater</b>; <i>She said me…</i> → <b>She told me / She said (that)…</b>. 2. <i>Unless you don't…</i> → <b>Unless you…</b>; <i>Despite it was cold</i> → <b>Although it was cold / Despite the cold</b>. 3. <i>Tomás, that lives…</i> → <b>Tomás, who lives…</b>. 4. <i>I'm used to wake up</i> → <b>waking up</b>; <i>very freezing</i> → <b>absolutely freezing</b>. 5. <i>Would you mind to help?</i> → <b>helping</b>; <i>I live here since…</i> → <b>I've lived here since…</b>.</div>
<div class="box"><h4>AUDIO</h4>Track R3.1 Back from the south (natural and slow) · Track R3.2 Dictation: contractions and weak forms (6-second pauses) · Track R3.3 Two dialogues (correct versions)</div>""")

    # Page 2 - Listening
    topics = [("Danny's boots", True), ("Bruno's belt", True), ("the wind in Patagonia", True), ("a hermit", True), ("the hotel in Buenos Aires", True),
              ("money and ATMs", True), ("Danny's new girlfriend", False), ("tourism in Buenos Aires", True), ("Carol's dress", True)]
    tl = " &nbsp; ".join(f"☐ {t}{(' ' + R('✓')) if ok else ''}" for t, ok in topics)
    tf = [("Danny took his boots off at the door.", "T (Mrs. Lima asked him to)"), ("It was hot at night in Patagonia.", "F: freezing at night."),
          ("Danny never got used to the wind.", "F: he got used to it after a few days."), ("Tomás had worked in an office.", "T"),
          ("Danny paid for something he didn't have at the hotel.", "F: they took it off the bill."), ("Buenos Aires was cheaper than Danny expected.", "F: more expensive.")]
    tfl = [f'<li value="{i+1}">{s} <b>T / F</b> {R(a)}</li>' for i, (s, a) in enumerate(tf)]
    find = [("adjective order (21)", "my ugly old green wool sweater"), ("reported speech (22)", "Paulo told me that the wind was… / He told me he would… / She told me she had found…"),
            ("in case / unless (23)", "in case my card didn't work / unless I had to"), ("a contrast linker (24)", "Although it was summer / However / On the other hand"),
            ("a relative clause with commas (25)", "Tomás, who has lived… / The hotel, which was near the center,"), ("get used to (26)", "I got used to it"),
            ("an extreme adjective / such (27)", "absolutely amazing · huge · freezing · filthy · such a bright blue that"), ("a polite request (28)", "Would you mind taking your boots off? / Could you pass me your plate?"),
            ("past perfect (29)", "I'd never been so happy / He'd worked in an office / than I'd expected")]
    fl = "".join(f"<li>{x} {R(y)}</li>" for x, y in find)
    b.page(f"""{sec(2, "Listening: back from the south", "10 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
<p style="margin:0">Danny is back at the hostel after his trip to Patagonia and Buenos Aires.</p>
{audiocard(["R3.1 · NATURAL", "R3.1 · SLOW"])}</div><div style="width:40mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo('I')}" style="width:40mm;height:24mm;object-fit:cover;display:block"></div></div>
{sub("A", "Listen at natural speed. Which topics do they talk about? Check eight. One topic is extra.", "2 min", "R3.1")}
<p style="font-weight:600;font-size:8.8pt;line-height:1.6">{tl}</p>
{sub("B", "Listen again. True (T) or false (F)? Correct the false sentences.", "4 min")}
<div style="font-size:8.6pt">{twocol(tfl, 3)}</div>
{sub("C", "Find one example in the dialogue of each form. Use the audio script or listen again.", "4 min")}
<ol style="font-size:8.4pt;line-height:1.35;margin:0">{fl}</ol>""",
    20, """<p>A: the extra topic is <i>Danny's new girlfriend</i>. C: let the student read the script (last page of this guide) or play the slow version and pause. Ask: <i>What was your best trip this year?</i></p>""")

    # Page 3 - Grammar 1
    ao = [("sweater / wool / old / green", "an old green wool sweater"), ("jacket / black / waterproof / long", "a long black waterproof jacket")]
    aol = "".join(f"<li><i>a / an + {w}</i> {A(r_, 'min-width:50mm')}</li>" for w, r_ in ao)
    rs = [("&ldquo;The zipper is broken.&rdquo; (Carol said)", "Carol said (that) the zipper was broken."), ("&ldquo;I'll send a new card.&rdquo; (The bank told Danny)", "The bank told Danny (that) they would send a new card.")]
    rsl = "".join(f'<li><i>{d}</i> {A(i, "min-width:60mm")}</li>' for d, i in rs)
    uc = [(["unless", "in case"], "in case", "Take an umbrella", "it rains."), (["Unless", "In case"], "Unless", "", "you book now, there won't be any rooms.")]
    ucl = "".join(f"<li>{a} {ch(o, r_)} {e}</li>" for o, r_, a, e in uc)
    cl = [("It was expensive. We loved it. (although)", "Although it was expensive, we loved it."), ("Tomás lives by a lake. He has no TV. (who, with commas)", "Tomás, who lives by a lake, has no TV.")]
    cll = "".join(f'<li><i>{d}</i> {A(i, "min-width:60mm")}</li>' for d, i in cl)
    b.page(f"""{sec(3, "Grammar 1: Units 21–25", "8 min")}
{sub("A", "Unit 21. Put the adjectives in the correct order.", "2 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0">{aol}</ol>
{sub("B", "Unit 22. Report the sentences.", "2 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0">{rsl}</ol>
{sub("C", "Unit 23. Choose.", "1 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0">{ucl}</ol>
{sub("D", "Units 24–25. Join the sentences with the word in brackets.", "3 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0">{cll}</ol>
<div class="box sand"><h4>REMEMBER</h4><b>opinion · size · age · color · material</b> + noun · <b>say</b> (no person) / <b>tell</b> + person; one tense back · <b>unless</b> = if… not; <b>in case</b> = to be ready if · <b>although</b> + clause; <b>despite</b> + noun / -ing; <b>However,</b> + new sentence · <b>who / which / where</b> + commas, never <i>that</i>.</div>""",
    22, """<ol><li>A: ask the student to say the order out loud: opinion, size, age, color, material.</li>
<li>B: accept <i>would</i> or <i>were going to</i> in 2. D: check the commas and the pause in speech.</li></ol>""")

    # Page 4 - Grammar 2
    errs = [("very amazing", "absolutely amazing"), ("walk", "walking"), ("get", "got"), ("lives", "has lived"), ("has worked", "had worked"),
            ("such a", "such a"), ("to keep", "keeping"), ("have arrived", "arrived")]
    def e(i):
        w, c = errs[i]
        return f"<u>{w}</u>" + (f" {R('→ ' + c)}" if T and w != c else (f" {R('✓')}" if T else ""))
    b.page(f"""{sec(4, "Grammar 2: Units 26–29", "8 min")}
{sub("A", "Danny writes to his mom, Rita. Eight phrases are underlined. Seven are wrong. Correct them.", "6 min")}
<div class="box" style="line-height:1.95;font-size:9pt">Hi Mom!<br>I'm back at the hostel. Patagonia was {e(0)}! The first days were hard: I wasn't used to {e(1)} in that wind, but I {e(2)} used to it after a few days. I met a hermit who {e(3)} there for 25 years. Before that, he {e(4)} in an office in Buenos Aires. It was {e(5)} long trip that I'm still tired. In Buenos Aires, I asked the receptionist, &ldquo;Would you mind {e(6)} my bags until six?&rdquo; I {e(7)} here yesterday, and Mrs. Lima made chicken soup! Love, Danny</div>
{sub("B", "Units 26–29. Complete the sentences so they are true for you. Then tell your teacher.", "2 min")}
<ol style="line-height:1.35;font-size:8.9pt;margin:0"><li>I'm not used to…<div class="wline"></div></li><li>The best place I've ever been to was absolutely…<div class="wline"></div></li><li>Would you mind…?<div class="wline"></div></li><li>Before I started English at Speak!, I had never…<div class="wline"></div></li></ol>
<div class="box sand"><h4>REMEMBER</h4><b>be / get used to</b> + noun / -ing; <b>used to</b> + verb = past habit · <b>absolutely</b> + extreme adjective (never <i>very</i>); <b>so</b> + adjective; <b>such (a)</b> + adjective + noun · <b>Would you mind</b> + -ing; <b>Do you mind if I</b> + present · finished time → <b>past simple</b>; up to now → <b>present perfect</b>; before another past action → <b>past perfect</b>.</div>""",
    22, """<ol><li>A: phrase 6 (<i>such a</i>) is correct. 8: <i>yesterday</i> = finished time, so past simple.</li>
<li>B: correct with the student, then ask follow-up questions in the same structures.</li></ol>""")

    # Page 5 - Vocabulary
    vc = [("it keeps the rain out", "waterproof"), ("money you get back for something you returned", "a refund"), ("to take money out of the bank", "withdraw"),
          ("a place that charges tourists too much", "a tourist trap"), ("pretty, like a postcard", "picturesque"), ("damage to the body from extreme cold", "frostbite"),
          ("very hungry", "starving"), ("given for free", "complimentary"), ("a person who lives alone, far from other people", "a hermit")]
    vcl = [f'<li value="{i+1}">{d} → {A(w, "min-width:20mm")}</li>' for i, (d, w) in enumerate(vc)]
    ff = [(["agency", "branch"], "branch", "I went to the bank", "."), (["I agree", "I'm agree"], "I agree", "", ". Tourism creates jobs."),
          (["I know Paris", "I've been to Paris"], "I've been to Paris", "", " twice."), (["It's making cold", "It's cold"], "It's cold", "", " today."),
          (["I want the bill", "Could I have the bill"], "Could I have the bill", "", ", please?"), (["sick of", "sick with"], "sick of", "I'm", " my landlord!")]
    ffl = "".join(f"<li>{a + ' ' if a else ''}{ch(o, r_)}{e2}</li>" for o, r_, a, e2 in ff)
    b.page(f"""{sec(5, "Vocabulary and word choice", "7 min")}
{sub("A", "Units 21–29. Write the word.", "3 min")}
<div class="bank">complimentary · frostbite · a hermit · picturesque · a refund · starving · a tourist trap · waterproof · withdraw</div>
<div style="font-size:8.7pt">{twocol(vcl, 5)}</div>
{sub("B", "Watch out! Units 23–29. Choose the correct words.", "4 min")}
<ol style="line-height:1.75;font-size:8.9pt;margin:0;columns:2;column-gap:5mm">{ffl}</ol>
<div class="box sand"><h4>YOUR WORD BANK</h4>Choose five words from Units 21–29 that you want to use more. Write a personal sentence with each one in your notebook.</div>""",
    22, """<ol><li>A: after each word, ask a personal question: <i>Have you ever asked for a refund? What's the most picturesque town you know?</i></li>
<li>B: these come from the WATCH OUT boxes of Units 23, 24, 25, 26, 28 and 29.</li></ol>""")

    # Page 6 - Pronunciation and social English
    d1 = [("Receptionist", "Good evening. How can I help you?"), ("Carol", "Hi. I have a <u>reserve</u> for two nights. Would you mind <u>to tell</u> me what time checkout is?"),
          ("Receptionist", "<u>Not at all</u>. It's at eleven. Here's your key card."), ("Carol", "Thanks. Do you mind if I <u>would leave</u> my bags here for an hour?"), ("Receptionist", "Of course not.")]
    d2 = [("Ana", "How was Iceland?"), ("Paulo", "<u>Very fantastic</u>! The waterfalls were huge."), ("Ana", "Was it cold?"),
          ("Paulo", "It was <u>freezing</u>. It was <u>such cold</u> that my camera stopped working."), ("Ana", "You must be exhausted."), ("Paulo", "I am. It was <u>a so long</u> trip!")]
    def dlg(ls):
        return "<br>".join(f"<b>{n}:</b> {t}" for n, t in ls)
    b.page(f"""{sec(6, "Pronunciation and social English", "8 min")}
{audiocard(["R3.2", "R3.3"])}
{sub("A", "Dictation. Listen and write the six sentences. Notice the contractions and weak forms ('d, 's, such a /sʌtʃə/, used to /ˈjuːstə/).", "4 min", "R3.2")}
<ol style="font-size:8.8pt;margin:0;line-height:1.3">{"".join(f"<li>{R(s) if T else '<div class=wline></div>'}</li>" for s in S32)}</ol>
{sub("B", "Each dialogue has mistakes (underlined; one in each dialogue is correct). Correct them. Then listen and check.", "4 min", "R3.3")}
<div class="two"><div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.5pt;line-height:1.45"><b>Dialogue 1</b><br>{dlg(d1)}</div>
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.5pt;line-height:1.45"><b>Dialogue 2</b><br>{dlg(d2)}</div></div>
<p class="small">{R("1: reservation · telling · Not at all ✓ · leave — 2: Absolutely fantastic · freezing ✓ · so cold · such a long")}</p>""",
    28, """<ol><li>A: the track has a 6-second pause after each sentence; pause more if needed. Check <i>'d</i> (had or would?) and <i>'s</i> (is or has?).</li>
<li>B: then role-play the dialogues with the student; change roles and change the details (a different hotel request, a different trip).</li></ol>""")

    # Page 7 - Speaking
    b.page(f"""{sec(7, "Speaking: long turn and role-play", "9 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE FROM UNITS 21–29</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>telling a story</th><th>opinions</th><th>giving a tour</th><th>at the hotel or store</th></tr>
<tr><td><i>I had never… · I got used to… · It was such a… that…</i></td><td><i>That may be true, but… · Although… · On the other hand…</i></td><td><i>Our next stop is… · It's the place where… · Don't miss…</i></td><td><i>Would you mind…? · I'd like a refund. · She told me…</i></td></tr></table></div>
{sub("A", "Long turn. Choose one card. Prepare for one minute, then talk for two minutes.", "5 min")}
<div style="display:flex;gap:2mm;font-size:8.5pt;margin:.5mm 0">
<div class="msg" style="max-width:none;flex:1;padding:1.5mm 2.5mm"><b>Card 1: A trip I'll never forget</b><br>where you went · what you packed · the most amazing / awful moment · what you had never done before</div>
<div class="msg" style="max-width:none;flex:1;padding:1.5mm 2.5mm"><b>Card 2: A big change</b><br>what your life was like before · what you had to get used to · what is still strange · how long it has been</div>
<div class="msg" style="max-width:none;flex:1;padding:1.5mm 2.5mm"><b>Card 3: Tourism in my city</b><br>two good things · two bad things · a place, which… · your opinion (although, however)</div></div>
{sub("B", "Role-play. Choose: a hotel front desk or returning something to a store. Your teacher is the receptionist or the clerk. Then change roles.", "4 min")}
<p style="margin:.3mm 0;font-size:8.6pt">{R("Teacher's card: hotel: check-in is at 3 p.m., the room is noisy, there's a wrong charge on the bill. Store: no receipt, but paid by card; the item is faulty; the store offers an exchange first. Push for polite requests, reported speech (The website said…) and unless / in case.") if T else ""}</p>""",
    28, """<ol><li>A: let the student choose; note mistakes for the reflection on page 8. Fluency option (3-2-1): the same talk in 2 minutes, then in 1 minute.</li>
<li>B: keep it realistic: these are situations students meet when they travel.</li></ol>""")

    # Page 8 - Reflect
    ck = [("21", "I can describe clothes with adjectives in the right order."), ("22", "I can return something and report what people said."),
          ("23", "I can solve a money problem (unless, in case)."), ("24", "I can discuss pros and cons and disagree politely."),
          ("25", "I can give a short tour with relative clauses."), ("26", "I can talk about getting used to new things."),
          ("27", "I can describe experiences with extreme adjectives."), ("28", "I can make polite requests at a hotel."), ("29", "I can tell a life story with the right past tenses.")]
    ckr = "".join(f"<tr><td><b>Unit {u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in ck)
    b.page(f"""{sec(8, "Reflect and homework", "4 min")}
{sub("A", "How are you doing? Check one box for each line.", "1 min")}
<table class="ck" style="font-size:8.4pt"><tr><th style="width:15mm"></th><th>In English…</th><th style="width:15mm">Easy!</th><th style="width:15mm">Sometimes</th><th style="width:15mm">Not yet</th></tr>{ckr}</table>
{sub("B", "My language notes. Look at your notes from Units 21–29. Which mistake do you still make? What are your two goals for Units 31–39?", "2 min")}
{lines(3)}
{sub("C", "Homework: writing (100–150 words)", "1 min")}
<p style="margin:.3mm 0"><b>A trip to remember.</b> Write about a trip: where you stayed, what happened and what you learned. Use at least five of these: <i>adjective order · reported speech · in case / unless · although / however · who / which with commas · get used to · absolutely / such a · past perfect</i>.</p>
{lines(6)}""",
    22, """<p>Compare this writing with the one from Review 2: is it longer, more accurate, more varied? Use the "Not yet" lines to plan extra practice before Unit 31.</p>""")

    def scr(lst):
        return "<br>".join(f"<b>{n}:</b> {t}" if n != "Narrator" else f"<i>{t}</i>" for n, t in lst)
    b.extra("Audio scripts", f"""
{sub("R3.1", "Back from the south (natural and slow)")}
<p style="line-height:1.3;font-size:8.3pt">{scr(SCRIPT)}</p>
{sub("R3.2", "Dictation: contractions and weak forms (6-second pauses)")}
<p style="font-size:8.6pt">{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S32))}</p>
{sub("R3.3", "Two dialogues (correct versions)")}
<p style="line-height:1.3;font-size:8.3pt">{scr(S33)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 30 - Review 3")
