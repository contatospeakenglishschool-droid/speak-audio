# Speak! Progress B1 - Review 2 (Units 11-19), all English - B1 format (2026-11-17)
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
_se.SERIES = "Progress"
setup(band="B1 · REVIEW 2", audio_json="audio_b1-review-2.json", img_dir="img")

PHOTOS = [("A", "a window view", "Unit 12"), ("B", "medicine", "Unit 13"), ("C", "a waiter", "Unit 14"), ("D", "spices", "Unit 15"),
          ("E", "chicken noodle soup", "Unit 16"), ("F", "pancakes", "Unit 17"), ("G", "a clothes rack", "Unit 18"), ("H", "a down jacket", "Unit 19")]
_r = json.load(open("roteiro.json"))["units"]["b1-review-2"]
SCRIPT = [tuple(x.replace("nineteen nineties", "1990s").split(": ", 1)) for x in _r["R2.1 Thanksgiving at the hostel"].split("\n")]
S22 = [x.split(": ", 1)[1].split(". ", 1)[1] for x in _r["R2.2 Dictation: contractions and weak forms"].split("\n")]
S23 = [tuple(x.split(": ", 1)) for x in _r["R2.3 Dialogues"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def lines(n):
        return '<div class="wline"></div>' * n

    # Page 1 - Warm-up
    cover = cover_html(T, "LEVEL B1 · REVIEW 2", "Review 2", "Units 11–19 · past perfect · deduction · advice · indirect questions · preferences · amounts · time clauses · passive · too / enough",
                       [("YOU CAN", "check what you learned in Units 11–19 and plan what to practice next"),
                        ("LANGUAGE", "He had just moved · It must be… · You'd better… · Could you tell me…? · I'd rather… · most of us · as soon as · it was made · too tight / warm enough"),
                        ("PRONUNCIATION", "contractions and weak forms: 'd, must, been")])
    b.page(f"""{sec(1, "Warm-up: photo memory", "6 min")}
{sub("A", "One photo from each unit. Write the word. Then say one sentence about it with the language of that unit.", "6 min")}
<div class="bank">chicken noodle soup · a clothes rack · a down jacket · medicine · pancakes · spices · a waiter · a window view</div>
{photo_grid(T, PHOTOS)}
<p class="small" style="margin-top:2mm"><b>Example:</b> a window view → <i>The woman at the window must be bored. She might be waiting for someone.</i></p>""",
    25, """<p>Photos A–H come from Units 12–19 (Unit 11 is in the listening). Push each unit's language: deduction (12), advice (13), indirect questions (14), preferences (15), amounts (16), time clauses (17), the passive (18), <i>too / enough / one</i> (19).</p>""", cover=cover)

    b.extra("Review overview · 60 min", """
<table><tr><th>Stage</th><th>Time</th><th>Units</th><th>SB page</th></tr>
<tr><td>1 Warm-up: photo memory</td><td>6 min</td><td>12–19</td><td>1</td></tr>
<tr><td>2 Listening: Thanksgiving at the hostel</td><td>10 min</td><td>11–19</td><td>2</td></tr>
<tr><td>3 Grammar 1: past perfect, deduction, advice, indirect questions, preferences</td><td>8 min</td><td>11–15</td><td>3</td></tr>
<tr><td>4 Grammar 2: correct Danny's email</td><td>8 min</td><td>16–19</td><td>4</td></tr>
<tr><td>5 Vocabulary and word choice</td><td>7 min</td><td>11–19</td><td>5</td></tr>
<tr><td>6 Pronunciation and social English</td><td>8 min</td><td>13–19</td><td>6</td></tr>
<tr><td>7 Speaking: long turn and role-play</td><td>9 min</td><td>11–19</td><td>7</td></tr>
<tr><td>8 Reflect and homework</td><td>4 min</td><td>11–19</td><td>8</td></tr></table>
<div class="box"><h4>HOW THIS GUIDE WORKS</h4>Every page looks like the Student Book page with the same number. Your notes are in the <b>yellow box</b>; <span class="red">answers in red</span> are not in the Student Book. This is a review: don't teach everything again. Let the student work, then focus on the mistakes that come back. The Grammar reference pages of Units 11–19 are useful here.</div>
<div class="box sand"><h4>THE STORY SO FAR</h4>Danny (Puck) cooks a Thanksgiving dinner at Mrs. Lima's hostel for Ana (Neural2-F), Bruno (Fenrir) and Mrs. Lima (Vindemiatrix). The dinner brings back the story of Units 11–19: Mrs. Lima's love story (11), the neighbor at the window (12), Bruno's ankle and the doctor's advice (13), Danny's nut allergy (14), Mrs. Lima prefers cooking (15), comfort food (16), Rita's instructions by phone (17), Danny's second-hand clothes (18) and the coat from Paulo (19). Verified fact: in the United States, Thanksgiving is on the fourth Thursday of November, by a 1941 law that took effect in 1942 (US National Archives). Dialogues: Ana orders at a restaurant (Waiter, Charon); Paulo (Neural2-I) buys boots (Clerk, Studio-O).</div>
<div class="box"><h4>THE TOP 5 MISTAKES TO WATCH</h4>1. <i>When I arrived, the bus left</i> (= it had already gone) → <b>the bus had left</b>; <i>It mustn't be her</i> → <b>It can't be her</b>. 2. <i>You better rest / You should to rest</i> → <b>You'd better rest / You should rest</b>. 3. <i>Could you tell me where is it?</i> → <b>where it is</b>; <i>I prefer tea than coffee / I'd rather to stay</i> → <b>to coffee / I'd rather stay</b>. 4. <i>The most of people / as soon as it will boil</i> → <b>Most people / as soon as it boils</b>. 5. <i>It can recycled / It's enough big</i> → <b>It can be recycled / It's big enough</b>.</div>
<div class="box"><h4>AUDIO</h4>Track R2.1 Thanksgiving at the hostel (natural and slow) · Track R2.2 Dictation: contractions and weak forms (6-second pauses) · Track R2.3 Two dialogues (correct versions)</div>""")

    # Page 2 - Listening
    topics = [("Danny's cooking", True), ("the neighbor at the window", True), ("Bruno's ankle", True), ("Danny's clothes", True), ("Paulo's coat", True),
              ("how Mrs. Lima met her husband", True), ("Danny's new job", False), ("comfort food", True), ("Thanksgiving in the US", True)]
    tl = " &nbsp; ".join(f"☐ {t}{(' ' + R('✓')) if ok else ''}" for t, ok in topics)
    tf = [("Danny had cooked a turkey many times before.", "F: he'd never cooked one."), ("Mrs. Lima thinks the person at the window is her neighbor.", "F: it can't be her; she's away."),
          ("Bruno has been running again since Monday.", "T"), ("Danny's sweater is new.", "F: it was bought second-hand."),
          ("Paulo's coat is too big for Danny.", "T (a bit too big)"), ("Thanksgiving is on the last Monday of November.", "F: the fourth Thursday.")]
    tfl = [f'<li value="{i+1}">{s} <b>T / F</b> {R(a)}</li>' for i, (s, a) in enumerate(tf)]
    find = [("past perfect (11)", "I'd never cooked one / He had just arrived / I had never seen"), ("must / might / can't (12)", "It must be… / It can't be her / It might be…"),
            ("advice (13)", "you'd better sit down / I should rest"), ("an indirect question (14)", "Could you tell me what's in the stuffing?"),
            ("a preference (15)", "I'd rather run than sit at home / I prefer cooking to running"), ("an amount (16)", "most of the people at this table"),
            ("a time clause (17)", "until it's golden / As soon as you finish"), ("a passive (18)", "it was bought / It was made / was sent by Paulo"),
            ("too / enough / one (19)", "a bit too big / warm enough / a new one")]
    fl = "".join(f"<li>{x} {R(y)}</li>" for x, y in find)
    b.page(f"""{sec(2, "Listening: Thanksgiving at the hostel", "10 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
<p style="margin:0">Danny cooks a Thanksgiving dinner for Ana, Bruno and Mrs. Lima.</p>
{audiocard(["R2.1 · NATURAL", "R2.1 · SLOW"])}</div><div style="width:40mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo('I')}" style="width:40mm;height:24mm;object-fit:cover;display:block"></div></div>
{sub("A", "Listen at natural speed. Which topics do they talk about? Check eight. One topic is extra.", "2 min", "R2.1")}
<p style="font-weight:600;font-size:8.8pt;line-height:1.6">{tl}</p>
{sub("B", "Listen again. True (T) or false (F)? Correct the false sentences.", "4 min")}
<div style="font-size:8.6pt">{twocol(tfl, 3)}</div>
{sub("C", "Find one example in the dialogue of each form. Use the audio script or listen again.", "4 min")}
<ol style="font-size:8.5pt;line-height:1.38;margin:0">{fl}</ol>""",
    20, """<p>A: the extra topic is <i>Danny's new job</i>. C: let the student read the script (last page of this guide) or play the slow version and pause. Ask: <i>What are you thankful for this year?</i></p>""")

    # Page 3 - Grammar 1
    pp = [("When I got to the station, the train", "had left", "(leave)."), ("She was nervous because she", "had never flown", "(never / fly) before.")]
    ppl = "".join(f"<li>{a} {A(f, 'min-width:22mm')} {e}</li>" for a, f, e in pp)
    dd = [(["must", "can't"], "can't", "That", "be Tom. He's in Chicago this week."), (["must", "mustn't"], "must", "The lights are off. They", "be out.")]
    ddl = "".join(f"<li>{a} {ch(o, r)} {e}</li>" for o, r, a, e in dd)
    rw = [("Rest. (strong advice: had better)", "You'd better rest."), ("Where is the restroom? (Could you tell me…)", "Could you tell me where the restroom is?"),
          ("Does the soup have nuts? (Do you know…)", "Do you know if the soup has nuts?"), ("I like tea more than coffee. (prefer)", "I prefer tea to coffee."),
          ("Tonight I want to stay home, not go out. (would rather … than)", "Tonight I'd rather stay home than go out.")]
    rwl = "".join(f'<li><i>{d}</i> {A(i, "min-width:56mm")}</li>' for d, i in rw)
    b.page(f"""{sec(3, "Grammar 1: Units 11–15", "8 min")}
{sub("A", "Unit 11. Complete with the past perfect.", "2 min")}
<ol style="line-height:1.75;font-size:8.9pt;margin:0">{ppl}</ol>
{sub("B", "Unit 12. Choose must or can't.", "1 min")}
<ol style="line-height:1.75;font-size:8.9pt;margin:0">{ddl}</ol>
{sub("C", "Units 13–15. Rewrite the sentences with the words in brackets.", "5 min")}
<ol style="line-height:1.85;font-size:8.9pt;margin:0">{rwl}</ol>
<div class="box sand"><h4>REMEMBER</h4><b>past perfect</b> = had + participle, the earlier past action · <b>must</b> = sure yes; <b>can't</b> = sure no; <b>might</b> = possible · <b>should / ought to</b> = advice; <b>had better</b> = strong advice, no <i>to</i> · indirect questions: <b>normal word order</b>, no <i>do / does</i>, <b>if</b> for yes/no · <b>prefer A to B</b>; <b>would rather</b> + verb (no <i>to</i>) + <b>than</b>.</div>""",
    22, """<ol><li>A: ask the student to draw a timeline for each sentence: which action happened first?</li>
<li>C: accept <i>Could you tell me if…</i> in 3; check word order carefully in 2 and 3.</li></ol>""")

    # Page 4 - Grammar 2
    errs = [("The most of", "Most of"), ("as soon as it will be", "as soon as it was"), ("until it was", "until it was"), ("None of them didn't leave", "None of them left"),
            ("was maked", "was made"), ("is being repair", "is being repaired"), ("enough warm", "warm enough"), ("a bigger", "a bigger one")]
    def e(i):
        w, c = errs[i]
        return f"<u>{w}</u>" + (f" {R('→ ' + c)}" if T and w != c else (f" {R('✓')}" if T else ""))
    b.page(f"""{sec(4, "Grammar 2: Units 16–19", "8 min")}
{sub("A", "Danny writes to his mom after the dinner. Eight phrases are underlined. Seven are wrong. Correct them.", "6 min")}
<div class="box" style="line-height:1.95;font-size:9pt">Hi Mom!<br>Thanksgiving was a success! {e(0)} the guests at the hostel came, about fifteen people. I followed your instructions: I put the turkey on the table {e(1)} ready, and I didn't take it out of the oven {e(2)} golden. {e(3)} any food on their plates! My sweater {e(4)} in the 1990s, and my old jeans {e(5)} by a tailor this week. Oh, and Paulo sent me a coat. It's {e(6)} for my trip south, but it's a bit too big. Maybe I'll exchange it for {e(7)}. Love, Danny</div>
{sub("B", "Units 16–19. Complete the sentences so they are true for you. Then tell your teacher.", "2 min")}
<ol style="line-height:1.35;font-size:8.9pt;margin:0"><li>Most of my friends…<div class="wline"></div></li><li>As soon as I get home today, I…<div class="wline"></div></li><li>My favorite piece of clothing was made / bought…<div class="wline"></div></li><li>My city is too… / isn't … enough.<div class="wline"></div></li></ol>
<div class="box sand"><h4>REMEMBER</h4><b>most people</b> (in general) / <b>most of the…</b> (a group); never <i>the most of</i>; <b>none of</b> + positive verb · after <b>when, as soon as, until</b>: present for the future, no <i>will</i> · passive = <b>be + participle</b> in every tense · <b>too</b> + adjective; adjective + <b>enough</b>; <b>one / ones</b> to avoid repeating a noun.</div>""",
    22, """<ol><li>A: phrase 3 (<i>until it was</i>) is correct. In 2, the past is fine (<i>as soon as it was ready</i>), but never <i>will</i> after <i>as soon as</i>.</li>
<li>B: correct with the student, then ask follow-up questions in the same structures.</li></ol>""")

    # Page 5 - Vocabulary
    vc = [("when someone asks their partner to marry them", "a proposal"), ("too interested in other people's lives", "nosy"), ("to blow air out of your nose suddenly", "sneeze"),
          ("extra money you leave for the server", "a tip"), ("birds we eat, like chicken and turkey", "poultry"), ("taking a lot of time", "time-consuming"),
          ("food with very little flavor", "bland"), ("a place where garbage is buried", "a landfill"), ("something you buy for a very good price", "a bargain")]
    vcl = [f'<li value="{i+1}">{d} → {A(w, "min-width:20mm")}</li>' for i, (d, w) in enumerate(vc)]
    ff = [(["married with", "married to"], "married to", "She's", "a doctor."), (["view", "vision"], "view", "I have a great", "from my window."),
          (["remedy", "medicine"], "medicine", "Did you take your", "?"), (["account", "check"], "check", "Could we have the", ", please?"),
          (["recipe", "receipt"], "recipe", "Can you send me the", "for this cake?"), (["try it on", "prove it"], "try it on", "Can I", "?")]
    ffl = "".join(f"<li>{a} {ch(o, r)}{e2 if e2[0] in '?,.' else ' ' + e2}</li>" for o, r, a, e2 in ff)
    b.page(f"""{sec(5, "Vocabulary and word choice", "7 min")}
{sub("A", "Units 11–19. Write the word.", "3 min")}
<div class="bank">a bargain · bland · a landfill · nosy · poultry · a proposal · sneeze · a tip · time-consuming</div>
<div style="font-size:8.7pt">{twocol(vcl, 5)}</div>
{sub("B", "Watch out! Units 11–19. Choose the correct word.", "4 min")}
<ol style="line-height:1.75;font-size:8.9pt;margin:0;columns:2;column-gap:5mm">{ffl}</ol>
<div class="box sand"><h4>YOUR WORD BANK</h4>Choose five words from Units 11–19 that you want to use more. Write a personal sentence with each one in your notebook.</div>""",
    22, """<ol><li>A: after each word, ask a personal question: <i>Is anyone in your building nosy? What's the best bargain you've found?</i></li>
<li>B: these false friends come from the WATCH OUT boxes of Units 11, 12, 13, 14, 16 and 19.</li></ol>""")

    # Page 6 - Pronunciation and social English
    d1 = [("Waiter", "Good evening. Are you ready to order?"), ("Ana", "Yes. Could you tell me what <u>is today's special</u>?"), ("Waiter", "It's grilled salmon with rice and a side salad."),
          ("Ana", "I'd rather <u>to have</u> something lighter. I'll have the tomato soup, please."), ("Waiter", "Of course. Anything to drink?"),
          ("Ana", "Just water, please. And could we have the <u>account</u> when you have a moment?")]
    d2 = [("Clerk", "Can I help you find anything?"), ("Paulo", "Do you have these boots <u>with</u> a size ten?"), ("Clerk", "I'm afraid we've sold out of the brown <u>ones</u>. We have black ones."),
          ("Paulo", "Can I <u>prove</u> them?"), ("Clerk", "Sure. How are they?"), ("Paulo", "They're a bit <u>very</u> tight. Do you have a <u>bigger</u>? No? Then I think I'll leave them.")]
    def dlg(ls):
        return "<br>".join(f"<b>{n}:</b> {t}" for n, t in ls)
    b.page(f"""{sec(6, "Pronunciation and social English", "8 min")}
{audiocard(["R2.2", "R2.3"])}
{sub("A", "Dictation. Listen and write the six sentences. Notice the contractions and weak forms ('d, must /məs/, been /bɪn/, could you /kʊdʒə/).", "4 min", "R2.2")}
<ol style="font-size:8.8pt;margin:0;line-height:1.3">{"".join(f"<li>{R(s) if T else '<div class=wline></div>'}</li>" for s in S22)}</ol>
{sub("B", "Each dialogue has mistakes (underlined; one is correct). Correct them. Then listen and check.", "4 min", "R2.3")}
<div class="two"><div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.5pt;line-height:1.45"><b>Dialogue 1</b><br>{dlg(d1)}</div>
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.5pt;line-height:1.45"><b>Dialogue 2</b><br>{dlg(d2)}</div></div>
<p class="small">{R("1: today's special is · have · check — 2: in · ones ✓ · try them on · too · bigger one")}</p>""",
    28, """<ol><li>A: the track has a 6-second pause after each sentence; pause more if needed. Check <i>'d</i> (had or would?) and <i>been</i>.</li>
<li>B: then role-play the dialogues with the student; change roles and change the details (a different dish, a different size).</li></ol>""")

    # Page 7 - Speaking
    b.page(f"""{sec(7, "Speaking: long turn and role-play", "9 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE FROM UNITS 11–19</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>telling a story</th><th>advising</th><th>ordering and shopping</th><th>food and preferences</th></tr>
<tr><td><i>By the time… · I had never… · It turned out that…</i></td><td><i>You should… · If I were you, I'd… · You'd better…</i></td><td><i>Could you tell me…? · Do you have it in…? · I'll take it.</i></td><td><i>I'd rather… · It reminds me of… · It's a bit too…</i></td></tr></table></div>
{sub("A", "Long turn. Choose one card. Prepare for one minute, then talk for two minutes.", "5 min")}
<div style="display:flex;gap:2mm;font-size:8.5pt;margin:.5mm 0">
<div class="msg" style="max-width:none;flex:1;padding:1.5mm 2.5mm"><b>Card 1: A love story I know</b><br>who the people are · how they met · what had happened before · how it ended (or continues)</div>
<div class="msg" style="max-width:none;flex:1;padding:1.5mm 2.5mm"><b>Card 2: A meal I'll never forget</b><br>where and when · what you ate and how it was cooked · how it tasted · who paid</div>
<div class="msg" style="max-width:none;flex:1;padding:1.5mm 2.5mm"><b>Card 3: Me and my clothes</b><br>where you buy clothes · something that was made or bought far away · too / not … enough · what should be done about fast fashion</div></div>
{sub("B", "Role-play abroad. Choose: a restaurant or a clothes store. Your teacher is the server or the clerk. Then change roles.", "4 min")}
<p style="margin:.3mm 0;font-size:8.6pt">{R("Teacher's card: restaurant: the special has nuts, the student's first choice is sold out, the service charge is not included. Store: the color is sold out, the size is too small, there's a 20% discount today. Push for indirect questions, too / enough and one.") if T else ""}</p>""",
    28, """<ol><li>A: let the student choose; note mistakes for the reflection on page 8. Fluency option (3-2-1): the same talk in 2 minutes, then in 1 minute.</li>
<li>B: keep it realistic: these are the situations students meet when they travel.</li></ol>""")

    # Page 8 - Reflect
    ck = [("11", "I can tell a story with the past perfect."), ("12", "I can make deductions (must, might, can't)."),
          ("13", "I can describe symptoms and give advice."), ("14", "I can order in a restaurant with indirect questions."),
          ("15", "I can talk about food and my preferences."), ("16", "I can talk about amounts and survey results."),
          ("17", "I can give and follow instructions with time clauses."), ("18", "I can use the passive in different tenses."), ("19", "I can shop for clothes (too, enough, one).")]
    ckr = "".join(f"<tr><td><b>Unit {u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in ck)
    b.page(f"""{sec(8, "Reflect and homework", "4 min")}
{sub("A", "How are you doing? Check one box for each line.", "1 min")}
<table class="ck" style="font-size:8.4pt"><tr><th style="width:15mm"></th><th>In English…</th><th style="width:15mm">Easy!</th><th style="width:15mm">Sometimes</th><th style="width:15mm">Not yet</th></tr>{ckr}</table>
{sub("B", "My language notes. Look at your notes from Units 11–19. Which mistake do you still make? What are your two goals for Units 21–29?", "2 min")}
{lines(3)}
{sub("C", "Homework: writing (100–150 words)", "1 min")}
<p style="margin:.3mm 0"><b>A special meal.</b> Write about a special meal: a celebration, a trip or a family dinner. Use at least five of these: <i>past perfect · must / might · I'd rather · most of · as soon as / until · a passive · too / enough</i>.</p>
{lines(6)}""",
    22, """<p>Compare this writing with the one from Review 1: is it longer, more accurate, more varied? Use the "Not yet" lines to plan extra practice before Unit 21.</p>""")

    def scr(lst):
        return "<br>".join(f"<b>{n}:</b> {t}" if n != "Narrator" else f"<i>{t}</i>" for n, t in lst)
    b.extra("Audio scripts", f"""
{sub("R2.1", "Thanksgiving at the hostel (natural and slow)")}
<p style="line-height:1.3;font-size:8.3pt">{scr(SCRIPT)}</p>
{sub("R2.2", "Dictation: contractions and weak forms (6-second pauses)")}
<p style="font-size:8.6pt">{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S22))}</p>
{sub("R2.3", "Two dialogues (correct versions)")}
<p style="line-height:1.3;font-size:8.3pt">{scr(S23)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 20 - Review 2")
