# Speak! Bridge A2 - Unit 35 "Out and about" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 35", audio_json="audio_a2-unit-35.json", img_dir="img")

PHOTOS = [("A", "towel", "towel"), ("B", "sunscreen", "sunscreen"), ("C", "backpack", "backpack"),
          ("D", "boots", "boots"), ("E", "sandwiches", "sandwiches"), ("F", "chips", "chips")]
_r = json.load(open("roteiro.json"))["units"]["a2-unit-35"]
S351 = [x.split(": ", 1) for x in _r["35.1 Planning a day out"].split("\n")]
S352 = [x.split(": ", 1)[1] for x in _r["35.2 Repeat: suggestions and offers"].split("\n")]
S353 = [x.split(". ", 1)[1] for x in [y.split(": ", 1)[1] for y in _r["35.3 Suggestion, offer or prediction?"].split("\n")]]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 35", "Out and about", "A day out · <b>suggestions, offers, plans and predictions</b>",
                       [("YOU CAN", "plan a day out with friends: make suggestions, offer to help and make predictions"),
                        ("LANGUAGE", "Let's leave early. · Why don't we take the train? · How about stopping for ice cream? · I'll bring the sunscreen."),
                        ("PRONUNCIATION", "friendly intonation in suggestions · I'll")])
    cats = [("beach", "towel, sunscreen, bathing suit"), ("picnic", "sandwiches, chips, fruit"), ("hiking", "backpack, boots, hat")]
    ct = "".join(f"<tr><td style='width:22mm'><b>{c}</b></td><td>{A(w, 'min-width:60mm')}</td></tr>" for c, w in cats)
    b.page(f"""{sec(1, "Warm-up: a day out", "8 min")}
{sub("A", "What do you need for a day out? Name the things in the photos.", "2 min")}
{photo_grid(T, PHOTOS)}
{sub("B", "Put the six words from A and these three words in the table: <b>fruit · hat · bathing suit</b>.", "3 min")}
<table style="margin:0;font-size:9pt">{ct}</table>
<p class="small" style="margin:.5mm 0">Can you add one more thing for each day out?</p>
{sub("C", "Talk about a day out that you enjoyed.", "3 min")}
<p style="margin:0">Where did you go? · Who did you go with? · What did you do? · What did you take with you?</p>""",
    25, """<ol><li>A <i>day out</i> = a trip for one day to relax somewhere away from home. The hat could also go with the beach; accept any logical answer.</li>
<li>US English: <i>chips</i> (British: <i>crisps</i>), <i>bathing suit</i> or <i>swimsuit</i>. Drill <i>sunscreen</i> and <i>backpack</i>.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Things for a day out at the beach, a picnic or a hike</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Tom, Lucy and Priya plan a day at Indiana Dunes</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Suggestions, offers, plans and predictions</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Making plans together</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>4 min</td><td>Friendly suggestions · suggestion, offer or prediction?</td><td>5</td></tr>
<tr><td>5 Practice</td><td>9 min</td><td>Add the missing word · match and respond · snacks in US English</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Plan a day out with your teacher</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Tom (Neural2-D), Lucy (Neural2-C) and their roommate Priya (Unit 26) plan a Saturday at Indiana Dunes National Park. Priya speaks for the first time in this unit: her voice is <b>en-US-Chirp3-HD-Kore</b> (keep it in future units). Tom buys the train tickets, Lucy plans the hike and brings sunscreen, Priya bakes bread for sandwiches (in Unit 26 she bakes her own bread), and they want to stop at Kate's bakery for her coffee ice cream (Review 3). Facts: Indiana Dunes on Lake Michigan became Indiana's first national park in 2019 (NBC Chicago, "Indiana Dunes Becomes State's 1st National Park"); the South Shore Line commuter train runs from downtown Chicago to Dune Park station, near the dunes, and tickets can be bought on its mobile app (South Shore Line / Wikipedia, "Dune Park station").</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students say <i>Let's to go</i>, <i>How about go…?</i> and <i>Why we don't…?</i>, write <i>Lets</i> without the apostrophe, and use the present simple for offers (<i>I bring the drinks!</i>) instead of <i>I'll</i>.</div>
<div class="box"><h4>AUDIO</h4>Track 35.1 Planning a day out (slow and natural) · Track 35.2 Repeat: suggestions and offers · Track 35.3 Suggestion, offer or prediction?</div>""")

    # Page 2
    resp = [("the train tickets", "T"), ("plan the hike on a map", "L"), ("sandwiches", "P"), ("drinks", "E"), ("fruit", "T"),
            ("chips", "T"), ("hats", "E"), ("sunscreen", "L"), ("towels and bathing suits", "E")]
    rl = [f'<li value="{i+1}">{s} {A(a, "min-width:9mm;text-align:center")}</li>' for i, (s, a) in enumerate(resp)]
    op = [("Tom,", ["are you going to get", "will you get"], "are you going to get", "the train tickets again?"),
          ("", ["I'll bake", "I'm baking"], "I'll bake", "some bread tonight."),
          ("", ["Why don't", "Do"], "Why don't", "we all bring our own drinks?"),
          ("The forecast says", ["it's going to be", "it'll being"], "it's going to be", "really hot."),
          ("", ["We're needing", "We'll need"], "We'll need", "hats."),
          ("And let's", ["bring", "to bring"], "bring", "towels and bathing suits."),
          ("How about", ["stop", "stopping"], "stopping", "at Kate's bakery?"),
          ("Why don't I", ["get", "getting"], "get", "some fruit and some chips?")]
    opl = [f'<li value="{i+1}">{(a + " ") if a else ""}{ch(o, r)} {e}</li>' for i, (a, o, r, e) in enumerate(op)]
    b.page(f"""{sec(2, "Listening: planning a day out", "10 min")}
<div style="display:flex;gap:2.5mm;align-items:center"><p style="flex:1;margin:0">Tom, Lucy and their roommate Priya are planning a day out at Indiana Dunes National Park, on Lake Michigan, about an hour from Chicago by train.</p>{img('G', 34, 22)}{img('H', 34, 22)}</div>
{audiocard(["35.1 · SLOW", "35.1 · NATURAL"])}
{sub("A", "Listen. Who is responsible for each thing? Write L (Lucy), T (Tom), P (Priya) or E (everyone).", "4 min", "35.1 · SLOW")}
<div style="font-size:9pt">{twocol(rl, 6)}</div>
{sub("B", "Listen again and choose the words you hear.", "5 min", "35.1 · NATURAL")}
<div style="font-size:8.8pt">{twocol(opl, 5)}</div>
{sub("C", "Would you enjoy this day out? Where can people go for a day out near your city?", "1 min")}""",
    29, """<ol><li>A: three-person conversations are hard: before listening, play the first lines and ask who is speaking (Lucy, Tom, Priya). Priya is new: she's the medical student from Unit 26.</li>
<li>B: let the student predict first. Indiana Dunes became Indiana's first national park in 2019; the South Shore Line train goes there from downtown Chicago.</li></ol>""")

    # Page 3
    b.page(f"""{sec(3, "Language focus: making plans together", "10 min")}
{sub("A", "Suggestions. Read and choose.", "4 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">1 <b>Why don't we</b> all bring our own drinks? · 2 <b>Let's</b> leave early so it's not too hot. · 3 <b>Let's</b> bring towels. · 4 <b>How about</b> stopping at Kate's bakery?</div>
<ol style="margin:.5mm 0;line-height:1.7"><li>The phrases in bold are {ch(["predictions", "suggestions"], "suggestions")}.</li>
<li>After <i>Why don't we</i> and <i>Let's</i>, we use {ch(["the base form", "verb-ing"], "the base form")}. After <i>How about</i>, we use {ch(["the base form", "verb-ing"], "verb-ing")}.</li>
<li>In <i>Let's</i>, the apostrophe comes {ch(["before", "after"], "before")} the letter s.</li></ol>
{sub("B", "Offers and plans. Read and choose.", "3 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">1 Tom, <b>are you going to get</b> the train tickets again? · Yes, I am. · 2 <b>I'll bake</b> some bread tonight and make sandwiches. · 3 <b>Why don't I get</b> some fruit?</div>
<ol style="margin:.5mm 0;line-height:1.7"><li>Tom decided to get the tickets {ch(["before the conversation", "during the conversation"], "before the conversation")}.</li>
<li>Priya decided to make sandwiches {ch(["before the conversation", "during the conversation"], "during the conversation")}. Sentences 2 and 3 are {ch(["offers", "predictions"], "offers")}.</li></ol>
{sub("C", "Predictions. Which is an opinion? Which is based on evidence?", "3 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">1 I checked the weather forecast, and it<b>'s going to be</b> really hot. · 2 We<b>'ll</b> all <b>need</b> hats.</div>
<p style="margin:.5mm 0">evidence: {A("1 (going to: the forecast)", "min-width:40mm")} &nbsp; opinion: {A("2 (will)", "min-width:16mm")}</p>
<div class="box sand"><h4>RULE</h4><b>suggestion</b> → Let's + base form · Why don't we + base form? · How about + verb-ing? &nbsp; <b>offer</b> (decided now) → I'll · Why don't I…? &nbsp; <b>plan</b> (decided before) → going to &nbsp; <b>prediction</b> → going to (evidence) · will (opinion). More on the next page: <b>Grammar reference</b>.</div>""",
    20, """<ol><li>A: <i>Let's</i> = <i>let us</i>. A light bulb is a good image for <i>I'll</i>: an idea that comes now.</li>
<li>Drill all the examples with friendly, rising intonation.</li></ol>""")

    grammar_ref.suggestions_offers(b)

    # Page 5
    sop = ["S", "O", "P", "S", "P", "O"]
    sopl = "".join(f"<li>{A(f, 'min-width:10mm;text-align:center')}</li>" for f in sop)
    b.page(f"""{sub("D", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>Let's to go to the beach.</td><td><b>Let's go to the beach.</b></td><td>Let's + base form.</td></tr>
<tr><td>How about go by bike?</td><td><b>How about going by bike?</b></td><td>How about + verb-ing.</td></tr>
<tr><td>Why we don't take the train?</td><td><b>Why don't we take the train?</b></td><td>question word order.</td></tr>
<tr><td>Lets bring towels.</td><td><b>Let's bring towels.</b></td><td>apostrophe.</td></tr>
<tr><td>Your bag is heavy. I help you!</td><td><b>I'll help you!</b></td><td>an offer = I'll.</td></tr>
<tr><td>Look at the sky! It will rain.</td><td><b>It's going to rain.</b></td><td>evidence.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "4 min")}
{audiocard(["35.2", "35.3"])}
{sub("A", "Listen and repeat. Sound friendly!", "2 min", "35.2")}
{twocol([f'<li value="{i+1}">{s}</li>' for i, s in enumerate(S352)], 4)}
{sub("B", "Listen to six sentences. Is each one a suggestion (S), an offer (O) or a prediction (P)? Write S, O or P.", "2 min", "35.3")}
<ol style="line-height:1.5;column-count:3;column-gap:5mm">{sopl}</ol>""",
    27, """<ol><li>A: suggestions sound friendly when the voice goes up on the main word: <i>How about STOPping at the bakery?</i> <i>I'll</i> /aɪl/ is short; students often don't hear it.</li>
<li>B: script: 1 How about going by bike? 2 I'll carry your bag. 3 Look at those clouds. It's going to rain. 4 Let's take the train. 5 I think you'll love the beach. 6 Why don't I make some sandwiches?</li></ol>""")

    # Page 6
    mw = [("How going by bike?", "How <u>about</u> going by bike?"), ("I going to wear my new hiking boots.", "I<u>'m</u> going to wear…"),
          ("Why don't take the bus?", "Why don't <u>we</u> take the bus?"), ("I know! I ask Dan if he wants to come.", "I<u>'ll</u> ask Dan…"),
          ("She's going bring a cake. She's making it now.", "She's going <u>to</u> bring…"), ("bring some chocolate too.", "<u>Let's</u> bring some chocolate too."),
          ("How about here for lunch?", "How about <u>stopping / eating</u> here…?"), ("Why don't I some money?", "Why don't I <u>bring</u> some money?"),
          ("Let's to the café we went to last time.", "Let's <u>go</u> to the café…"), ("lend you my sunglasses if you don't have any.", "<u>I'll</u> lend you my sunglasses…")]
    mwl = "".join(f"<li>{a}{(' ' + R('→ ' + c)) if T else ''}</li>" for a, c in mw)
    mt = [("What should we do about food?", "I'm going to make sandwiches for everyone."), ("I really need a coffee, but I didn't bring any money.", "I'll buy the drinks."),
          ("There aren't many trains on Sundays.", "Why don't I check the train times?"), ("I'm tired of shopping.", "How about going to the museum?"),
          ("This is such a beautiful place!", "Let's take a photo."), ("We have to cross the river, but there's no bridge.", "Oh no! Our feet are going to get wet!"),
          ("I'm so hot and tired.", "Why don't we get some ice cream?"), ("I'm carrying seven bags!", "I'll help you carry them.")]
    rs = sorted(r for _, r in mt)
    lt = "abcdefgh"
    mtl = "".join(f"<li>{s} {A(lt[rs.index(r)], 'min-width:7mm;text-align:center')}</li>" for s, r in mt)
    rsl = "".join(f"<li>{r}</li>" for r in rs)
    b.page(f"""{sec(5, "Practice", "9 min")}
{sub("A", "One word is missing in each sentence. Add it. Use contractions if you can.", "4 min")}
<ol style="line-height:1.5;font-size:9pt;column-count:2;column-gap:6mm">{mwl}</ol>
{sub("B", "Match 1–8 with the best responses a–h.", "4 min")}
<div style="display:flex;gap:4mm;font-size:8.8pt"><ol style="flex:1;line-height:1.5;margin:0">{mtl}</ol><ol type="a" style="flex:1;line-height:1.5;margin:0">{rsl}</ol></div>
{sub("C", "Word builder: snacks in American English", "1 min")}
<div style="display:flex;gap:3mm;align-items:center"><div class="box" style="flex:1;margin:0;font-size:8.8pt;line-height:1.5"><b>chips</b> = thin, crunchy slices of potato in a bag (British: <i>crisps</i>) · <b>French fries / fries</b> = hot, long pieces of potato (British: <i>chips</i>) · <b>tortilla chips</b> = triangles made from corn. Which do you like? What snacks are popular in Brazil?</div>{img('F', 26, 20)}</div>""",
    26, """<ol><li>A: the student works from memory first, then checks with the Language focus. Item 7: any logical -ing verb.</li>
<li>B: ask which responses are suggestions, offers, plans or predictions.</li>
<li>C: from the Linguahouse extension, adapted to US English. Popular US flavors include barbecue and sour cream and onion.</li></ol>""")

    # Page 7
    rows = [("transportation", "Let's take the train.", "I'll buy the tickets."),
            ("food and drink", "Why don't we have a picnic?", "I'll make sandwiches."),
            ("weather and clothes", "Let's bring jackets.", "It's going to be cold. (forecast)"),
            ("things to do", "How about renting bikes?", "We'll have a great time!"),
            ("people to invite", "Why don't we invite Ana?", "Why don't I text her?")]
    rt = "".join(f"<tr><td><b>{a}</b></td><td>{R(s) if T else ''}</td><td>{R(o) if T else ''}</td></tr>" for a, s, o in rows)
    b.page(f"""{sec(6, "Speaking: plan a day out", "12 min")}
<div style="display:flex;gap:3mm;align-items:center"><p style="flex:1;margin:0">You and your teacher are planning a day out together. Choose one: <b>a day at the beach · a day out shopping · a picnic and sports in the park · your idea</b>.</p>{img('C', 30, 20)}</div>
{sub("A", "Make notes in at least five spaces. Use suggestions, offers and predictions.", "3 min")}
<table style="margin:0;font-size:8.8pt"><tr><th style="width:32mm"></th><th>suggestions: let's · why don't we · how about</th><th>offers and predictions: I'll · why don't I · will · going to</th></tr>{rt}</table>
{sub("B", "Plan the day with your teacher. Use the language from the lesson. Your teacher sometimes says no!", "5 min")}
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:9pt;line-height:1.45"><b>Teacher:</b> So, we need to plan our day out on Saturday. We're going shopping, so let's drive. <b>You:</b> Good idea. I'll take my car and pick you up at your house. <b>Teacher:</b> Great! How about having lunch at the mall? <b>You:</b> Hmm, I'm not sure. It's going to be expensive. Why don't we…</div>
{sub("C", "Did you use all the forms? Write three good sentences from your conversation.", "3 min")}
<div class="wline"></div><div class="wline"></div><div class="wline"></div>
{sub("D", "Is this day out realistic? Would you really like to do it?", "1 min")}""",
    24, """<ol><li>A: the red examples in the table are your model; share one or two only if the student needs ideas.</li>
<li>B: say no to one or two suggestions (<i>I'm not sure… How about…?</i>) so the student has to offer an alternative. Then swap: the student starts. Correct afterwards, not during.</li></ol>""")

    # Page 8
    pc = [("A2 Unit 32", "I can talk about timetables and personal plans for the future."), ("A2 Unit 33", "I can make predictions and say how sure I am."),
          ("A2 Unit 34", "I can choose the right future form: going to, will or the present continuous."), ("A2 Unit 35", "I can make suggestions and offers when I plan a day out.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("How about to go to the zoo on Sunday?", "How about going…"), ("Let's meet at the station at nine.", "✓"),
          ("Why we don't invite Kate?", "Why don't we invite…"), ("That box looks heavy. I carry it for you.", "I'll carry it…"),
          ("The forecast says it's going to rain, so let's take umbrellas.", "✓"), ("Lets have a picnic in the park.", "Let's have…")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:36mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Correct the mistakes. If a sentence is correct, write ✓.</b></p>
<ol style="line-height:1.55;font-size:9pt">{hwl}</ol>
<p style="margin-top:1.5mm"><b>2. A message to a friend (50–75 words).</b> Write a message to a friend about a day out next weekend. Include two suggestions, one offer and one prediction.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class: the student reads the message aloud and you answer it as the friend, accepting one suggestion and refusing one: <i>Good idea! But I'm not sure about… How about…?</i></p>""")

    b.extra("Audio script", f"""
{sub("35.1", "Planning a day out (slow and natural)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in S351)}</p>
{sub("35.2", "Repeat: suggestions and offers")}
<p>{" · ".join(S352)}</p>
{sub("35.3", "Suggestion, offer or prediction? (3-second pause)")}
<p>{" · ".join(S353)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 35 - Out and about")
