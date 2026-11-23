# Speak! Progress B1 - Review 4 (Units 31-39), all English - B1 review format (8 pages)
import sys, os, json
_h = os.path.dirname(os.path.abspath(__file__))
for _d in ("/home/claude/speak-audio/engine", os.path.join(_h, "..", "speak-audio", "engine"), os.path.join(_h, "..", "..", "speak-audio", "engine"), os.path.join(_h, "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
_se.SERIES = "Progress"
setup(band="B1 · REVIEW 4", audio_json="audio_b1-review-4.json", img_dir="img")

PHOTOS = [("A", "a paint roller", "Unit 31"), ("B", "a valley", "Unit 32"), ("C", "rush hour", "Unit 33"), ("D", "a traffic jam", "Unit 34"),
          ("E", "a predator", "Unit 35"), ("F", "an old town", "Unit 36"), ("G", "a flat tire", "Unit 37"), ("H", "a passport", "Unit 38")]
_r = json.load(open("roteiro.json"))["units"]["b1-review-4"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["R4.1 A birthday dinner"].split("\n")]
S42 = [x.split(": ", 1)[1].split(". ", 1)[1] for x in _r["R4.2 Dictation: weak forms"].split("\n")]
S43 = [tuple(x.split(": ", 1)) for x in _r["R4.3 Dialogues"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def lines(n):
        return '<div class="wline"></div>' * n

    # Page 1 - Warm-up
    cover = cover_html(T, "LEVEL B1 · REVIEW 4", "Review 4", "Units 31–39 · have something done · the + places · it is said · was supposed to · because of · suggestions · needs doing · I wish · will be + -ing",
                       [("YOU CAN", "check what you learned in Units 31–39 and plan what to practice next"),
                        ("LANGUAGE", "I had it fixed · the Pantanal · is said to be · I was about to… · as a result · How about going…? · It needs fixing · I wish I could… · I'll be working"),
                        ("PRONUNCIATION", "weak forms: to, be, could, about")])
    b.page(f"""{sec(1, "Warm-up: photo memory", "6 min")}
{sub("A", "One photo from each unit. Write the word. Then say one sentence about it with the language of that unit.", "6 min")}
<div class="bank">a flat tire · an old town · a paint roller · a passport · a predator · rush hour · a traffic jam · a valley</div>
{photo_grid(T, PHOTOS)}
<p class="small" style="margin-top:2mm"><b>Example:</b> a traffic jam → <i>I was supposed to arrive at six, but I got stuck in a traffic jam.</i></p>""",
    25, """<p>Photos A–H come from Units 31–38 (Unit 39 is in the listening). Push each unit's language: <i>have something done</i> (31), <i>the</i> with place names and superlatives (32), <i>it is said that / is said to</i> (33), <i>was going to / was supposed to / was about to</i> (34), cause and result (35), suggestions (36), <i>needs doing</i> (37), <i>I wish</i> (38).</p>""", cover=cover)

    b.extra("Review overview · 60 min", """
<table><tr><th>Stage</th><th>Time</th><th>Units</th><th>SB page</th></tr>
<tr><td>1 Warm-up: photo memory</td><td>6 min</td><td>31–38</td><td>1</td></tr>
<tr><td>2 Listening: a birthday dinner</td><td>10 min</td><td>31–39</td><td>2</td></tr>
<tr><td>3 Grammar 1: have something done, the, it is said, future in the past, cause and result</td><td>8 min</td><td>31–35</td><td>3</td></tr>
<tr><td>4 Grammar 2: correct Danny's email</td><td>8 min</td><td>36–39</td><td>4</td></tr>
<tr><td>5 Vocabulary and word choice</td><td>7 min</td><td>31–39</td><td>5</td></tr>
<tr><td>6 Pronunciation and social English</td><td>8 min</td><td>34–39</td><td>6</td></tr>
<tr><td>7 Speaking: long turn and role-play</td><td>9 min</td><td>31–39</td><td>7</td></tr>
<tr><td>8 Reflect and homework</td><td>4 min</td><td>31–39</td><td>8</td></tr></table>
<div class="box"><h4>HOW THIS GUIDE WORKS</h4>Every page looks like the Student Book page with the same number. Your notes are in the <b>yellow box</b>; <span class="red">answers in red</span> are not in the Student Book. This is a review: don't teach everything again. Let the student work, then focus on the mistakes that come back. The Grammar reference pages of Units 31–39 are useful here.</div>
<div class="box sand"><h4>THE STORY SO FAR</h4>Sunday evening: Danny's birthday get-together at Mrs. Lima's hostel, moved from Friday (Unit 39). Ana (Neural2-F) had a chocolate cake made at a bakery near the hospital. Bruno (Fenrir) arrives late: his plane from Porto Alegre was forty minutes late, then a traffic jam (34). Ana's kitchen is finished; Danny helped paint (31). The hostel's kitchen faucet is leaking again; Mrs. Lima (Vindemiatrix) is having it fixed on Tuesday (31, 37). Danny wishes his mom were there (38). He was going to go home in July but is thinking of staying until the end of the year. Plans: a trip to the Pantanal (Bruno saw a jaguar there as a kid, Unit 32) and the new restaurant on their street. Dialogues: Carol (Leda) at the auto shop in Orlando (37; Mechanic = Charon); Bruno and Danny plan a beach day. The only real-world fact is from Unit 32: Angel Falls is the highest waterfall in the world.</div>
<div class="box"><h4>THE TOP 5 MISTAKES TO WATCH</h4>1. <i>I painted my house</i> (when someone else did it) → <b>I had my house painted</b>; <i>the Brazil</i> → <b>Brazil</b>. 2. <i>The restaurant is said that is good</i> → <b>is said to be good</b>; <i>I was supposing to…</i> → <b>I was supposed to…</b>. 3. <i>because the accident</i> → <b>because of the accident</b>. 4. <i>How about go…?</i> → <b>going</b>; <i>I suggest to go</i> → <b>I suggest going / we go</b>; <i>It needs fix</i> → <b>fixing</b>. 5. <i>I wish I can…</i> → <b>could</b>; <i>I'll working</i> → <b>I'll be working</b>; <i>I'll be sending</i> (a promise) → <b>I'll send</b>.</div>
<div class="box"><h4>AUDIO</h4>Track R4.1 A birthday dinner (natural and slow) · Track R4.2 Dictation: weak forms (6-second pauses) · Track R4.3 Two dialogues (correct versions)</div>""")

    # Page 2 - Listening
    topics = [("Ana's cake", True), ("Bruno's flight", True), ("Ana's kitchen", True), ("a leaking faucet", True), ("Danny's mom", True),
              ("Danny's plans for the year", True), ("a trip to the Pantanal", True), ("Danny's new job", False), ("a new restaurant", True)]
    tl = " &nbsp; ".join(f"☐ {t}{(' ' + R('✓')) if ok else ''}" for t, ok in topics)
    tf = [("Ana made the cake herself.", "F: she had it made at a bakery."), ("Bruno's plane landed on time.", "F: it was forty minutes late."),
          ("Bruno took the subway.", "F: he was about to, but he stayed in the taxi."), ("The faucet will be fixed on Tuesday.", "T"),
          ("Danny is going home in July.", "F: he was going to, but he may stay till the end of the year."), ("Ana and Bruno are free next weekend.", "F: they'll both be working.")]
    tfl = [f'<li value="{i+1}">{s} <b>T / F</b> {R(a)}</li>' for i, (s, a) in enumerate(tf)]
    find = [("have something done (31)", "I had it made / We had new cabinets put in / I'm having it fixed"), ("the + a place name (32)", "the Pantanal"),
            ("is said to (33)", "the new restaurant is said to be wonderful"), ("was supposed to / was about to / was going to (34)", "My plane was supposed to land at six / I was about to get out / I was going to go home"),
            ("because of (35)", "Because of an accident on the highway"), ("a suggestion (36)", "Why don't you call her? / How about a trip…? / It's worth it / I suggest we all go"),
            ("needs + -ing (37)", "It needs fixing."), ("I wish (38)", "I wish my mom were here / I wish I could have her lasagna"),
            ("will be + -ing (39)", "She'll be waiting / I'll be working")]
    fl = "".join(f"<li>{x} {R(y)}</li>" for x, y in find)
    b.page(f"""{sec(2, "Listening: a birthday dinner", "10 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
<p style="margin:0">It's Sunday evening. Danny's friends arrive at the hostel for his birthday get-together.</p>
{audiocard(["R4.1 · NATURAL", "R4.1 · SLOW"])}</div><div style="width:40mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo('I')}" style="width:40mm;height:24mm;object-fit:cover;display:block"></div></div>
{sub("A", "Listen at natural speed. Which topics do they talk about? Check eight. One topic is extra.", "2 min", "R4.1")}
<p style="font-weight:600;font-size:8.8pt;line-height:1.6">{tl}</p>
{sub("B", "Listen again. True (T) or false (F)? Correct the false sentences.", "4 min")}
<div style="font-size:8.6pt">{twocol(tfl, 3)}</div>
{sub("C", "Find one example in the dialogue of each form. Use the audio script or listen again.", "4 min")}
<ol style="font-size:8.4pt;line-height:1.35;margin:0">{fl}</ol>""",
    20, """<p>A: the extra topic is <i>Danny's new job</i>. C: let the student read the script (last page of this guide) or play the slow version and pause. Ask: <i>How do you like to celebrate your birthday?</i></p>""")

    # Page 3 - Grammar 1
    hd = [("A plumber fixed our sink last week. (We / have)", "We had our sink fixed last week."), ("Someone is going to paint my apartment. (I / get)", "I'm going to get my apartment painted.")]
    hdl = "".join(f'<li><i>{d}</i> {A(i, "min-width:62mm")}</li>' for d, i in hd)
    th = [(["the Andes", "Andes"], "the Andes", "We flew over", "."), (["the highest", "the most high"], "the highest", "Angel Falls is", " waterfall in the world.")]
    thl = "".join(f"<li>{a} {ch(o, r_)}{e}</li>" for o, r_, a, e in th)
    sd = [("People say that the new restaurant is wonderful. (is said to)", "The new restaurant is said to be wonderful."), ("People think that long commutes make us unhappy. (It is thought)", "It is thought that long commutes make us unhappy.")]
    sdl = "".join(f'<li><i>{d}</i> {A(i, "min-width:62mm")}</li>' for d, i in sd)
    fp = [(["was supposed to", "was supposing to"], "was supposed to", "My plane", " land at six."), (["about to", "going"], "about to", "I was", " call a taxi when my phone rang.")]
    fpl = "".join(f"<li>{a} {ch(o, r_)}{e}</li>" for o, r_, a, e in fp)
    cr = [("There was an accident. The taxi took an hour. (because of)", "Because of an accident, the taxi took an hour."), ("Tourists fed the fish. The fish lost their fear. (as a result)", "Tourists fed the fish. As a result, the fish lost their fear.")]
    crl = "".join(f'<li><i>{d}</i> {A(i, "min-width:62mm")}</li>' for d, i in cr)
    b.page(f"""{sec(3, "Grammar 1: Units 31–35", "8 min")}
{sub("A", "Unit 31. Rewrite with have or get something done.", "2 min")}
<ol style="line-height:1.7;font-size:8.8pt;margin:0">{hdl}</ol>
{sub("B", "Unit 32. Choose.", "1 min")}
<ol style="line-height:1.7;font-size:8.8pt;margin:0">{thl}</ol>
{sub("C", "Unit 33. Rewrite with the words in brackets.", "2 min")}
<ol style="line-height:1.7;font-size:8.8pt;margin:0">{sdl}</ol>
{sub("D", "Unit 34. Choose.", "1 min")}
<ol style="line-height:1.7;font-size:8.8pt;margin:0">{fpl}</ol>
{sub("E", "Unit 35. Join the sentences with the words in brackets.", "2 min")}
<ol style="line-height:1.7;font-size:8.8pt;margin:0">{crl}</ol>
<div class="box sand"><h4>REMEMBER</h4><b>have / get</b> + thing + past participle (someone else does it) · <b>the</b> + rivers, mountain ranges, oceans; no <i>the</i> with most cities and countries · <b>is said to</b> + verb / <b>It is said that</b> + clause · <b>was supposed to / was going to / was about to</b> + verb · <b>because of</b> + noun; <b>because</b> + clause; <b>As a result,</b> + new sentence.</div>""",
    22, """<ol><li>A: ask who did the work. In A2 also accept <i>I'm going to have my apartment painted.</i></li>
<li>B: Angel Falls (Venezuela) is the highest waterfall in the world (Unit 32). D: <i>supposed</i> is an adjective here, always with <i>-ed</i>.</li></ol>""")

    # Page 4 - Grammar 2
    errs = [("are", "were"), ("can", "could"), ("to go", "going"), ("to visit", "visiting"), ("repair", "repairing"),
            ("try", "try"), ("will guiding", "'ll be guiding"), ("to call", "calling")]
    def e(i):
        w, c = errs[i]
        return f"<u>{w}</u>" + (f" {R('→ ' + c)}" if T and w != c else (f" {R('✓')}" if T else ""))
    b.page(f"""{sec(4, "Grammar 2: Units 36–39", "8 min")}
{sub("A", "Danny writes to his mom, Rita. Eight words are underlined. Seven are wrong. Correct them.", "6 min")}
<div class="box" style="line-height:1.95;font-size:9pt">Hi Mom!<br>Thanks for the birthday call. I wish you {e(0)} here with us! And I wish I {e(1)} have your lasagna. Ana brought a chocolate cake, and Bruno arrived late, as usual. Ana suggested {e(2)} to the Pantanal, and Bruno says it's worth {e(3)}. Also, my old bike needs {e(4)}, so Mrs. Lima suggested I {e(5)} the new bike shop on our street. Next month I {e(6)} tours every weekend, so how about {e(7)} me on Sunday evenings? Love, Danny</div>
{sub("B", "Units 36–39. Complete the sentences so they are true for you. Then tell your teacher.", "2 min")}
<ol style="line-height:1.35;font-size:8.9pt;margin:0"><li>I wish I could…<div class="wline"></div></li><li>This time next year, I'll be…<div class="wline"></div></li><li>Something in my home needs…<div class="wline"></div></li><li>How about… this weekend?<div class="wline"></div></li></ol>
<div class="box sand"><h4>REMEMBER</h4><b>How about / suggest / It's worth</b> + -ing; <b>suggest (that) someone</b> + base verb · <b>needs</b> + -ing = <b>needs to be</b> + past participle · <b>wish</b> + past (<i>were, had</i>) / <b>could</b> · <b>will be</b> + -ing = in progress at a future time.</div>""",
    22, """<ol><li>A: word 6 (<i>try</i>) is correct: <i>suggest (that) I try</i>. For 3, <i>suggested we go</i> is also correct.</li>
<li>B: correct with the student, then ask follow-up questions in the same structures.</li></ol>""")

    # Page 5 - Vocabulary
    vc = [("water escaping through a small hole", "a leak"), ("an area of very wet land, like the Pantanal", "a wetland"), ("a person who travels to work every day", "a commuter"),
          ("a place where people can cross the street", "a crosswalk"), ("an animal that kills and eats other animals", "a predator"), ("full of tourists (often negative)", "touristy"),
          ("they clean the rain off a car's front window", "windshield wipers"), ("sad because you are far from home", "homesick"), ("an informal meeting or small party with friends", "a get-together")]
    vcl = [f'<li value="{i+1}">{d} → {A(w, "min-width:22mm")}</li>' for i, (d, w) in enumerate(vc)]
    ff = [(["renovate", "reform"], "renovate", "We're going to", " the kitchen."), (["lost", "missed"], "missed", "I", " the bus."),
          (["spend", "take"], "spend", "I", " two hours in traffic every day."), (["touristy", "turistic"], "touristy", "The town is very", "."),
          (["flat", "empty"], "flat", "My tire is", "."), (["a compromise", "plans"], "plans", "I can't go. I have", ".")]
    ffl = "".join(f"<li>{a + ' ' if a else ''}{ch(o, r_)}{e2}</li>" for o, r_, a, e2 in ff)
    b.page(f"""{sec(5, "Vocabulary and word choice", "7 min")}
{sub("A", "Units 31–39. Write the word.", "3 min")}
<div class="bank">a commuter · a crosswalk · a get-together · homesick · a leak · a predator · touristy · a wetland · windshield wipers</div>
<div style="font-size:8.7pt">{twocol(vcl, 5)}</div>
{sub("B", "Watch out! Units 31–39. Choose the correct words.", "4 min")}
<ol style="line-height:1.75;font-size:8.9pt;margin:0;columns:2;column-gap:5mm">{ffl}</ol>
<div class="box sand"><h4>YOUR WORD BANK</h4>Choose five words from Units 31–39 that you want to use more. Write a personal sentence with each one in your notebook.</div>""",
    22, """<ol><li>A: after each word, ask a personal question: <i>Have you ever had a leak at home? Are you a commuter? Which places in your city are touristy?</i></li>
<li>B: these come from the WATCH OUT boxes of Units 31, 33, 34, 36, 37 and 39.</li></ol>""")

    # Page 6 - Pronunciation and social English
    d1 = [("Mechanic", "Good morning. What can I do for you?"), ("Carol", "Hi. My car needs <u>check</u>. The brakes are making a strange noise."),
          ("Mechanic", "OK, we'll take a look. Your tires need <u>changed</u>, too."), ("Carol", "Can I <u>have done it</u> today?"), ("Mechanic", "Sure. <u>It'll be ready</u> at four.")]
    d2 = [("Bruno", "How about <u>go</u> to the beach on Saturday?"), ("Danny", "I'd love to, but I'll <u>working</u>. I have two tours."),
          ("Bruno", "Then I suggest <u>us to go</u> on Sunday."), ("Danny", "Sunday works for me. But it's worth <u>leaving</u> early, because of the traffic.")]
    def dlg(ls):
        return "<br>".join(f"<b>{n}:</b> {t}" for n, t in ls)
    b.page(f"""{sec(6, "Pronunciation and social English", "8 min")}
{audiocard(["R4.2", "R4.3"])}
{sub("A", "Dictation. Listen and write the six sentences. Notice the weak forms: to /tə/, be /bi/, could /kəd/, about /əbaʊt/.", "4 min", "R4.2")}
<ol style="font-size:8.8pt;margin:0;line-height:1.3">{"".join(f"<li>{R(s) if T else '<div class=wline></div>'}</li>" for s in S42)}</ol>
{sub("B", "Each dialogue has mistakes (underlined; one in each dialogue is correct). Correct them. Then listen and check.", "4 min", "R4.3")}
<div class="two"><div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.5pt;line-height:1.45"><b>Dialogue 1</b><br>{dlg(d1)}</div>
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.5pt;line-height:1.45"><b>Dialogue 2</b><br>{dlg(d2)}</div></div>
<p class="small">{R("1: checking · to be changed (or changing) · have it done · It'll be ready ✓ — 2: going · I'll be working · we go · leaving ✓")}</p>""",
    28, """<ol><li>A: the track has a 6-second pause after each sentence; pause more if needed. In sentence 2, <i>supposed to</i> sounds like /səˈpoʊstə/.</li>
<li>B: then role-play the dialogues with the student; change roles and change the details (a different car problem, a different plan).</li></ol>""")

    # Page 7 - Speaking
    b.page(f"""{sec(7, "Speaking: long turn and role-play", "9 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE FROM UNITS 31–39</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>telling a story</th><th>services</th><th>suggesting</th><th>making plans</th></tr>
<tr><td><i>I was supposed to… · I was about to… when… · Because of…, … · As a result, …</i></td><td><i>I'm having… fixed. · It needs checking. · Can I have it done today?</i></td><td><i>How about…? · Why don't we…? · I suggest we… · It's worth…</i></td><td><i>I'll be working. · Can you make it on…? · Something has come up. · Are we still on for…?</i></td></tr></table></div>
{sub("A", "Long turn. Choose one card. Prepare for one minute, then talk for two minutes.", "5 min")}
<div style="display:flex;gap:2mm;font-size:8.5pt;margin:.5mm 0">
<div class="msg" style="max-width:none;flex:1;padding:1.5mm 2.5mm"><b>Card 1: A journey that went wrong</b><br>where you were going · what was supposed to happen · what happened, and why · what you learned</div>
<div class="msg" style="max-width:none;flex:1;padding:1.5mm 2.5mm"><b>Card 2: Living somewhere new</b><br>a place you'd like to live · what you would miss · what you wish were different where you live now · what people say about that place</div>
<div class="msg" style="max-width:none;flex:1;padding:1.5mm 2.5mm"><b>Card 3: Home and car</b><br>something you had done recently · something that needs fixing now · a repair that went wrong · DIY or a professional?</div></div>
{sub("B", "Role-play. Plan a weekend away with your teacher: suggest a place, find a day that works for both of you, and agree on the details. Then your teacher calls with a change of plans. Change roles.", "4 min")}
<p style="margin:.3mm 0;font-size:8.6pt">{R("Teacher's card: say no to the first suggestion (it's too touristy); you'll be working on Saturday morning. After you agree, call back: something has come up (your car needs fixing, you're having it done on Saturday). Suggest a new day. Push for suggestions with -ing, will be + -ing and needs doing.") if T else ""}</p>""",
    28, """<ol><li>A: let the student choose; note mistakes for the reflection on page 8. Fluency option (3-2-1): the same talk in 2 minutes, then in 1 minute.</li>
<li>B: keep it realistic and personal: real places and the student's real week.</li></ol>""")

    # Page 8 - Reflect
    ck = [("31", "I can talk about home repairs and things I have done."), ("32", "I can talk about geography with the right articles and superlatives."),
          ("33", "I can report what people say and think (It is said that…)."), ("34", "I can tell the story of a journey that went wrong."),
          ("35", "I can explain causes and results."), ("36", "I can suggest ideas and respond to suggestions."),
          ("37", "I can explain a car problem and what needs doing."), ("38", "I can talk about moving abroad and say what I wish were different."), ("39", "I can arrange, change and cancel plans.")]
    ckr = "".join(f"<tr><td><b>Unit {u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in ck)
    b.page(f"""{sec(8, "Reflect and homework", "4 min")}
{sub("A", "How are you doing? Check one box for each line.", "1 min")}
<table class="ck" style="font-size:8.4pt"><tr><th style="width:15mm"></th><th>In English…</th><th style="width:15mm">Easy!</th><th style="width:15mm">Sometimes</th><th style="width:15mm">Not yet</th></tr>{ckr}</table>
{sub("B", "My language notes. Look at your notes from Units 31–39. Which mistake do you still make? What are your two goals for Units 41–49?", "2 min")}
{lines(3)}
{sub("C", "Homework: writing (100–150 words)", "1 min")}
<p style="margin:.3mm 0"><b>A plan that changed.</b> Write about a plan (a trip, a party, a move) that didn't happen the way you expected. Use at least five of these: <i>have something done · was supposed to / was about to · because of / as a result · it is said that · How about…? / I suggest… · needs + -ing · I wish · will be + -ing</i>.</p>
{lines(6)}""",
    22, """<p>Compare this writing with the one from Review 3: is it longer, more accurate, more varied? Use the "Not yet" lines to plan extra practice before Unit 41.</p>""")

    def scr(lst):
        return "<br>".join(f"<b>{n}:</b> {t}" if n != "Narrator" else f"<i>{t}</i>" for n, t in lst)
    b.extra("Audio scripts", f"""
{sub("R4.1", "A birthday dinner (natural and slow)")}
<p style="line-height:1.3;font-size:8.3pt">{scr(SCRIPT)}</p>
{sub("R4.2", "Dictation: weak forms (6-second pauses)")}
<p style="font-size:8.6pt">{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S42))}</p>
{sub("R4.3", "Two dialogues (correct versions)")}
<p style="line-height:1.3;font-size:8.3pt">{scr(S43)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 40 - Review 4")
