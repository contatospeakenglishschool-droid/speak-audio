# Speak! Progress B1 - Review 5 (Units 41-49), all English - B1 review format (8 pages)
import sys, os, json
_h = os.path.dirname(os.path.abspath(__file__))
for _d in ("/home/claude/speak-audio/engine", os.path.join(_h, "..", "speak-audio", "engine"), os.path.join(_h, "..", "..", "speak-audio", "engine"), os.path.join(_h, "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
_se.SERIES = "Progress"
setup(band="B1 · REVIEW 5", audio_json="audio_b1-review-5.json", img_dir="img")

PHOTOS = [("A", "a check-up", "Unit 41"), ("B", "a sneeze", "Unit 42"), ("C", "a guest room", "Unit 43"), ("D", "a bookcase", "Unit 44"),
          ("E", "a sandwich", "Unit 45"), ("F", "a lamp", "Unit 46"), ("G", "a saxophone", "Unit 47"), ("H", "a cooking class", "Unit 48")]
_r = json.load(open("roteiro.json"))["units"]["b1-review-5"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["R5.1 A night of jazz"].split("\n")]
S52 = [x.split(": ", 1)[1].split(". ", 1)[1] for x in _r["R5.2 Dictation: weak forms"].split("\n")]
S53 = [tuple(x.split(": ", 1)) for x in _r["R5.3 Dialogues"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def lines(n):
        return '<div class="wline"></div>' * n

    # Page 1 - Warm-up
    cover = cover_html(T, "LEVEL B1 · REVIEW 5", "Review 5", "Units 41–49 · <b>social English · reported questions · the third conditional</b>",
                       [("YOU CAN", "check what you learned in Units 41–49 and plan what to practice next"),
                        ("LANGUAGE", "It's bound to… · What a…! · Help yourself · I managed to… · isn't it? · Neither of us… · If I'd known…"),
                        ("PRONUNCIATION", "weak forms: of, can, would've, to, for")])
    b.page(f"""{sec(1, "Warm-up: photo memory", "6 min")}
{sub("A", "One photo from each unit. Write the word. Then say one sentence about it with the language of that unit.", "6 min")}
<div class="bank">a bookcase · a check-up · a cooking class · a guest room · a lamp · a sandwich · a saxophone · a sneeze</div>
{photo_grid(T, PHOTOS)}
<p class="small" style="margin-top:2mm"><b>Example:</b> a sneeze → <i>When my colleague sneezed, I said "Bless you!"</i></p>""",
    25, """<p>Photos A–H come from Units 41–48 (Unit 49 is in the listening). Push each unit's language: probability, <i>It's bound to / There's a good chance</i> (41); reactions and exclamations (42); reflexives, <i>Make yourself at home</i> (43); <i>managed to / was able to</i> (44); question tags (45); apologies and promises (46); <i>both / either / neither</i> (47); reported questions and requests (48).</p>""", cover=cover)

    b.extra("Review overview · 60 min", """
<table><tr><th>Stage</th><th>Time</th><th>Units</th><th>SB page</th></tr>
<tr><td>1 Warm-up: photo memory</td><td>6 min</td><td>41–48</td><td>1</td></tr>
<tr><td>2 Listening: a night of jazz</td><td>10 min</td><td>41–49</td><td>2</td></tr>
<tr><td>3 Grammar 1: probability, exclamations, reflexives, ability, question tags</td><td>8 min</td><td>41–45</td><td>3</td></tr>
<tr><td>4 Grammar 2: correct Danny's email</td><td>8 min</td><td>46–49</td><td>4</td></tr>
<tr><td>5 Vocabulary and word choice</td><td>7 min</td><td>41–49</td><td>5</td></tr>
<tr><td>6 Pronunciation and social English</td><td>8 min</td><td>42–49</td><td>6</td></tr>
<tr><td>7 Speaking: long turn and role-play</td><td>9 min</td><td>41–49</td><td>7</td></tr>
<tr><td>8 Reflect and homework</td><td>4 min</td><td>41–49</td><td>8</td></tr></table>
<div class="box"><h4>HOW THIS GUIDE WORKS</h4>Every page looks like the Student Book page with the same number. Your notes are in the <b>yellow box</b>; <span class="red">answers in red</span> are not in the Student Book. This is a review: don't teach everything again. Let the student work, then focus on the mistakes that come back. The Grammar reference pages of Units 41–49 are useful here.</div>
<div class="box sand"><h4>THE STORY SO FAR</h4>Friday night: Rafa's jazz band plays again at the bar near the hostel (Unit 47). Danny (Puck) and Bruno (Fenrir) got the best table this time. Ana (Neural2-F) arrives late from a hospital shift and apologizes (46). Neither Danny nor Bruno can dance (47). Rafa speaks for the first time (voice en-US-Chirp3-HD-Umbriel): last year he was stuck in a rut; his brother asked him what he really wanted and told him to join a band (48, homework); if he hadn't called him, he wouldn't have joined the band (49). Grandma Lourdes loved Danny's podcast episode and asked if he would visit her again (49). Dialogues: Ana welcomes Carol (Leda) to her apartment (43, 44); Danny late on his first week at the language school, with the director (Studio-O) (42, 45, 46). There are no real-world facts in this review.</div>
<div class="box"><h4>THE TOP 5 MISTAKES TO WATCH</h4>1. <i>There's a big chance</i> → <b>a good chance</b>; <i>How beautiful day!</i> → <b>What a beautiful day!</b> 2. <i>I relaxed myself</i> → <b>I relaxed</b>; <i>Yesterday I could finish it</i> → <b>I managed to finish it</b>. 3. <i>You're Brazilian, no?</i> → <b>aren't you?</b>; <i>I apologize you</i> → <b>I apologize to you</b>. 4. <i>I don't like neither</i> → <b>either</b>; <i>He asked me what did I want</i> → <b>what I wanted</b>; <i>She said me to wait</i> → <b>told me to wait</b>. 5. <i>If I would have known</i> → <b>If I had known</b>; <i>would of</i> → <b>would have</b>.</div>
<div class="box"><h4>AUDIO</h4>Track R5.1 A night of jazz (natural and slow) · Track R5.2 Dictation: weak forms (6-second pauses) · Track R5.3 Two dialogues (correct versions)</div>""")

    # Page 2 - Listening
    topics = [("Ana's shift", True), ("the best table", True), ("dancing", True), ("Rafa's brother", True), ("how Rafa joined the band", True),
              ("Grandma Lourdes", True), ("Carol's flight", False), ("the next song", True), ("the fries", True)]
    tl = " &nbsp; ".join(f"☐ {t}{(' ' + R('✓')) if ok else ''}" for t, ok in topics)
    tf = [("Ana arrived before the first song.", "F: she missed the first songs; her shift ended late."), ("Last time, Danny and Bruno couldn't find a seat.", "T"),
          ("Bruno can dance, but Danny can't.", "F: neither of them can dance."), ("Rafa has played with the band for about a year.", "T"),
          ("Rafa's brother told him to find a new job.", "F: he told him to stop complaining and join a band."), ("Grandma Lourdes wants Danny to visit her again.", "T")]
    tfl = [f'<li value="{i+1}">{s} <b>T / F</b> {R(a)}</li>' for i, (s, a) in enumerate(tf)]
    find = [("be bound to / a slight chance (41)", "they're bound to play that samba song / There's a slight chance I'll dance"), ("an exclamation (42)", "What a great band! / How kind of her!"),
            ("a reflexive pronoun (43)", "help yourself / You're both enjoying yourselves"), ("managed to / couldn't (44)", "we managed to get the best table / we couldn't even find a seat"),
            ("a question tag (45)", "aren't you? / isn't it?"), ("an apology (46)", "Sorry I'm late. I apologize for missing the first songs."),
            ("neither of us (47)", "Neither of us can dance. Neither of us wants to try."), ("a reported question or request (48)", "he asked me what I really wanted / he told me to stop complaining / She asked me if you would visit her"),
            ("the third conditional (49)", "If I hadn't called him, I wouldn't have joined the band.")]
    fl = "".join(f"<li>{x} {R(y)}</li>" for x, y in find)
    b.page(f"""{sec(2, "Listening: a night of jazz", "10 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
<p style="margin:0">It's Friday night. Rafa's jazz band is playing again at the bar near the hostel. Danny and Bruno are there, and Ana joins them.</p>
{audiocard(["R5.1 · NATURAL", "R5.1 · SLOW"])}</div><div style="width:40mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo('I')}" style="width:40mm;height:24mm;object-fit:cover;display:block"></div></div>
{sub("A", "Listen at natural speed. Which topics do they talk about? Check eight. One topic is extra.", "2 min", "R5.1")}
<p style="font-weight:600;font-size:8.8pt;line-height:1.6">{tl}</p>
{sub("B", "Listen again. True (T) or false (F)? Correct the false sentences.", "4 min")}
<div style="font-size:8.6pt">{twocol(tfl, 3)}</div>
{sub("C", "Find one example in the dialogue of each form. Use the audio script or listen again.", "4 min")}
<ol style="font-size:8.4pt;line-height:1.35;margin:0">{fl}</ol>""",
    20, """<p>A: the extra topic is <i>Carol's flight</i>. C: let the student read the script (last page of this guide) or play the slow version and pause. Ask: <i>Do you like live music? When did you last go to a concert?</i></p>""")

    # Page 3 - Grammar 1
    pr = [(["good", "big"], "good", "There's a", " chance of rain tomorrow."), (["bound to", "probable to"], "bound to", "Look at the traffic! We're", " be late.")]
    prl = "".join(f"<li>{a} {ch(o, r_)}{e}</li>" for o, r_, a, e in pr)
    ex = [("The band is great. (What)", "What a great band!"), ("You are very kind. (How)", "How kind of you!")]
    exl = "".join(f'<li><i>{d}</i> {A(i, "min-width:50mm")}</li>' for d, i in ex)
    rf = [(["yourself", "you"], "yourself", "Come in and make", " at home."), (["each other", "themselves"], "each other", "Carol and Leo teach", " English and Portuguese."), (["relaxed", "relaxed myself"], "relaxed", "After work, I", " on the sofa.")]
    rfl = "".join(f"<li>{a} {ch(o, r_)}{e}</li>" for o, r_, a, e in rf)
    ab = [(["could", "managed to"], "managed to", "The bookcase was heavy, but we", " carry it up three floors."), (["able", "can"], "able", "I'm sorry, I won't be", " to come on Saturday.")]
    abl = "".join(f"<li>{a} {ch(o, r_)}{e}</li>" for o, r_, a, e in ab)
    qt = [("You're Carol,", "aren't you?"), ("It's a long flight,", "isn't it?"), ("You don't eat meat,", "do you?"), ("Let's go,", "shall we?")]
    qtl = "".join(f'<li>{s} {A(t, "min-width:18mm")}</li>' for s, t in qt)
    b.page(f"""{sec(3, "Grammar 1: Units 41–45", "8 min")}
{sub("A", "Unit 41. Choose.", "1 min")}
<ol style="line-height:1.7;font-size:8.8pt;margin:0">{prl}</ol>
{sub("B", "Unit 42. Rewrite as exclamations with the word in brackets.", "1 min")}
<ol style="line-height:1.7;font-size:8.8pt;margin:0">{exl}</ol>
{sub("C", "Unit 43. Choose.", "2 min")}
<ol style="line-height:1.7;font-size:8.8pt;margin:0">{rfl}</ol>
{sub("D", "Unit 44. Choose.", "1 min")}
<ol style="line-height:1.7;font-size:8.8pt;margin:0">{abl}</ol>
{sub("E", "Unit 45. Add the question tag.", "2 min")}
<ol style="line-height:1.7;font-size:8.8pt;margin:0;columns:2;column-gap:6mm">{qtl}</ol>
<div class="box sand"><h4>REMEMBER</h4><b>be bound to / be likely to</b> + verb; <b>a good / slight chance of</b> + -ing · <b>What a</b> + adjective + noun! · <b>How</b> + adjective! · <b>myself, yourself…</b> (the same person) vs <b>each other</b> (A → B, B → A); no reflexive with <i>relax, feel, worry</i> · one success in the past: <b>managed to / was able to</b>, not <i>could</i> · tags: same auxiliary + pronoun, positive → negative tag.</div>""",
    22, """<ol><li>A–D: ask the student to explain each choice. In C, <i>Carol and Leo teach each other</i> comes from Unit 43.</li>
<li>E: practice the intonation: falling when you are sure, rising when you really ask.</li></ol>""")

    # Page 4 - Grammar 2
    errs = [("not to call", "not calling"), ("both", "both"), ("for to be", "for being"), ("can't", "can"),
            ("did he want", "he wanted"), ("join", "to join"), ("didn't call", "hadn't called"), ("wouldn't join", "wouldn't have joined")]
    def e(i):
        w, c = errs[i]
        return f"<u>{w}</u>" + (f" {R('→ ' + c)}" if T and w != c else (f" {R('✓')}" if T else ""))
    b.page(f"""{sec(4, "Grammar 2: Units 46–49", "8 min")}
{sub("A", "Danny writes to his mom. Eight words or phrases are underlined. Seven are wrong. Correct them.", "6 min")}
<div class="box" style="line-height:1.95;font-size:9pt">Hi Mom!<br>I'm sorry for {e(0)} you last week. Rafa's band played again on Friday, and {e(1)} Bruno and I went. Ana came too, but she apologized {e(2)} late. Neither of us {e(3)} dance, so we just listened! Rafa told us that his brother once asked him what {e(4)}, and he told him {e(5)} a band. If he {e(6)} his brother, he {e(7)} the band. Funny, isn't it? Love, Danny</div>
{sub("B", "Units 46–49. Complete the sentences so they are true for you. Then tell your teacher.", "2 min")}
<ol style="line-height:1.35;font-size:8.9pt;margin:0"><li>Once I apologized to someone for…<div class="wline"></div></li><li>Both my… and I…<div class="wline"></div></li><li>A teacher once asked me if…<div class="wline"></div></li><li>If I hadn't…, I wouldn't have…<div class="wline"></div></li></ol>
<div class="box sand"><h4>REMEMBER</h4><b>sorry for / apologize for</b> + -ing (<i>not calling</i>) · <b>both … and</b>; <b>neither</b> + positive verb · reported questions: <b>asked (me) what / if</b> + subject + verb, no <i>did</i>; <b>told me (not) to</b> + verb · third conditional: <b>If</b> + had + past participle, <b>would have</b> + past participle.</div>""",
    22, """<ol><li>A: word 2 (<i>both</i>) is correct. For 1, <i>I'm sorry I didn't call you</i> is also correct.</li>
<li>B: correct with the student, then ask follow-up questions in the same structures.</li></ol>""")

    # Page 5 - Vocabulary
    vc = [("to pay for a meal in a restaurant", "settle"), ("a person who receives visitors in their home", "a host"), ("what you say when someone sneezes", "Bless you"),
          ("let somebody stay at your home for a short time", "put somebody up"), ("to say that a person is responsible for something bad", "blame"),
          ("what you say to someone who is sick", "Get well soon"), ("honest and clear about what you think and want", "upfront"),
          ("to sign a contract with a music company", "get a record deal"), ("how long a person is likely to live", "life expectancy")]
    vcl = [f'<li value="{i+1}">{d} → {A(w, "min-width:24mm")}</li>' for i, (d, w) in enumerate(vc)]
    ff = [(["good", "big"], "good", "There's a", " chance of rain."), (["Same for you", "Same to you"], "Same to you", "", "!"),
          (["borrow", "lend"], "lend", "Can you", " me twenty dollars?"), (["trip", "travel"], "trip", "Have a good", "!"),
          (["music", "song"], "song", "I listened to a beautiful", "."), (["discussed about", "discussed"], "discussed", "We", " the problem."),
          (["smoking", "to smoke"], "smoking", "He quit", " last year."), (["give you a ride", "give you a lift"], "give you a ride", "I can", " home.")]
    ffl = "".join(f"<li>{a + ' ' if a else ''}{ch(o, r_)}{e2}</li>" for o, r_, a, e2 in ff)
    b.page(f"""{sec(5, "Vocabulary and word choice", "7 min")}
{sub("A", "Units 41–49. Write the word or phrase.", "3 min")}
<div class="bank">blame · Bless you · get a record deal · Get well soon · a host · life expectancy · put somebody up · settle · upfront</div>
<div style="font-size:8.7pt">{twocol(vcl, 5)}</div>
{sub("B", "Watch out! Units 41–49. Choose the correct words.", "4 min")}
<ol style="line-height:1.75;font-size:8.9pt;margin:0;columns:2;column-gap:5mm">{ffl}</ol>
<div class="box sand"><h4>YOUR WORD BANK</h4>Choose five words from Units 41–49 that you want to use more. Write a personal sentence with each one in your notebook.</div>""",
    22, """<ol><li>A: after each word, ask a personal question: <i>Who usually settles the bill when you go out? Have you ever put somebody up? Are you an upfront person?</i></li>
<li>B: these come from the WATCH OUT boxes of Units 41, 42, 44, 45, 47, 48 and 49. <i>A lift</i> is British English.</li></ol>""")

    # Page 6 - Pronunciation and social English
    d1 = [("Ana", "Come in! Make <u>you</u> at home."), ("Carol", "Thank you. <u>How beautiful apartment</u>!"),
          ("Ana", "<u>Serve you</u> to some coffee. Can I <u>give you a hand</u> with your bag?"), ("Carol", "Thanks. I <u>could</u> carry it up the stairs, but it's really heavy!")]
    d2 = [("Director", "You're new here, <u>no</u>?"), ("Danny", "Yes, I started on Monday. <u>Excuse me for late</u>. The bus broke down."),
          ("Director", "Never mind. It's a cold morning, <u>isn't it</u>?"), ("Danny", "It is! And it <u>doesn't happen</u> again, I promise.")]
    def dlg(ls):
        return "<br>".join(f"<b>{n}:</b> {t}" for n, t in ls)
    b.page(f"""{sec(6, "Pronunciation and social English", "8 min")}
{audiocard(["R5.2", "R5.3"])}
{sub("A", "Dictation. Listen and write the six sentences. Notice the weak forms: of /əv/, can /kən/, would've /ˈwʊdəv/, to /tə/, for /fər/.", "4 min", "R5.2")}
<ol style="font-size:8.8pt;margin:0;line-height:1.3">{"".join(f"<li>{R(s) if T else '<div class=wline></div>'}</li>" for s in S52)}</ol>
{sub("B", "Each dialogue has mistakes (underlined; one in each dialogue is correct). Correct them. Then listen and check.", "4 min", "R5.3")}
<div class="two"><div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.5pt;line-height:1.45"><b>Dialogue 1</b><br>{dlg(d1)}</div>
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.5pt;line-height:1.45"><b>Dialogue 2</b><br>{dlg(d2)}</div></div>
<p class="small">{R("1: yourself · What a beautiful apartment · Help yourself · give you a hand ✓ · managed to — 2: aren't you · Sorry I'm late · isn't it ✓ · won't happen")}</p>""",
    28, """<ol><li>A: the track has a 6-second pause after each sentence; pause more if needed. In sentence 3, <i>would've</i> sounds like /ˈwʊdəv/ and <i>I'd</i> = <i>I had</i>.</li>
<li>B: then role-play the dialogues with the student; change roles and change the details (a different guest, a different excuse).</li></ol>""")

    # Page 7 - Speaking
    b.page(f"""{sec(7, "Speaking: long turn and role-play", "9 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE FROM UNITS 41–49</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>reacting</th><th>hosting and helping</th><th>apologizing</th><th>explaining</th></tr>
<tr><td><i>What a…! · How kind of you! · Lucky you! · What a shame. · …, isn't it?</i></td><td><i>Make yourself at home. · Help yourself. · Can I give you a hand? · I managed to…</i></td><td><i>I'm so sorry about… · I apologize for… · It won't happen again. · Don't worry about it.</i></td><td><i>One explanation is… · The main reason is… · If I hadn't…, I wouldn't have…</i></td></tr></table></div>
{sub("A", "Long turn. Choose one card. Prepare for one minute, then talk for two minutes.", "5 min")}
<div style="display:flex;gap:2mm;font-size:8.5pt;margin:.5mm 0">
<div class="msg" style="max-width:none;flex:1;padding:1.5mm 2.5mm"><b>Card 1: Someone who helped you</b><br>who it was · what the problem was · what they did · what would have happened if they hadn't helped</div>
<div class="msg" style="max-width:none;flex:1;padding:1.5mm 2.5mm"><b>Card 2: Music and people</b><br>music you and a friend both like · a concert you went to · something neither of you likes · a song that reminds you of someone</div>
<div class="msg" style="max-width:none;flex:1;padding:1.5mm 2.5mm"><b>Card 3: Good advice</b><br>a time you asked someone for advice · what they asked you · what they told you to do · what happened next</div></div>
{sub("B", "Role-play. Your teacher is staying at your home for the weekend. Welcome them, offer help and make small talk. Then something goes wrong: apologize and promise to fix it. Change roles.", "4 min")}
<p style="margin:.3mm 0;font-size:8.6pt">{R("Teacher's card: arrive late (the bus broke down) and apologize. Accept some offers and refuse one politely. Use question tags in small talk. Then 'break' something (a glass, a lamp); the student is the host and reacts; next round, the student is the guest who breaks it and apologizes.") if T else ""}</p>""",
    28, """<ol><li>A: let the student choose; note mistakes for the reflection on page 8. Fluency option (3-2-1): the same talk in 2 minutes, then in 1 minute.</li>
<li>B: keep it realistic and personal: the student's real home and real week.</li></ol>""")

    # Page 8 - Reflect
    ck = [("41", "I can plan a busy week and say how probable something is."), ("42", "I can use common social expressions and react to news."),
          ("43", "I can be a good host or guest."), ("44", "I can offer help and say what I could or managed to do."),
          ("45", "I can keep a conversation going with question tags."), ("46", "I can apologize, make an excuse and make a promise."),
          ("47", "I can compare my musical tastes with someone else's."), ("48", "I can give advice and report questions and requests."),
          ("49", "I can explain reasons and imagine a different past.")]
    ckr = "".join(f"<tr><td><b>Unit {u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in ck)
    b.page(f"""{sec(8, "Reflect and homework", "4 min")}
{sub("A", "How are you doing? Check one box for each line.", "1 min")}
<table class="ck" style="font-size:8.4pt"><tr><th style="width:15mm"></th><th>In English…</th><th style="width:15mm">Easy!</th><th style="width:15mm">Sometimes</th><th style="width:15mm">Not yet</th></tr>{ckr}</table>
{sub("B", "My language notes. Look at your notes from Units 41–49. Which mistake do you still make? What are your two goals for Units 51–59?", "2 min")}
{lines(3)}
{sub("C", "Homework: writing (100–150 words)", "1 min")}
<p style="margin:.3mm 0"><b>A night to remember.</b> Write about a party, a concert or a visit that you remember well. Use at least five of these: <i>be bound to / a good chance · What a…! · yourself / each other · managed to · a question tag · I apologize for… · both / neither · asked me if / told me to · If I hadn't…, I wouldn't have…</i>.</p>
{lines(6)}""",
    22, """<p>Compare this writing with the one from Review 4: is it longer, more accurate, more varied? Use the "Not yet" lines to plan extra practice before Unit 51.</p>""")

    def scr(lst):
        return "<br>".join(f"<b>{n}:</b> {t}" if n != "Narrator" else f"<i>{t}</i>" for n, t in lst)
    b.extra("Audio scripts", f"""
{sub("R5.1", "A night of jazz (natural and slow)")}
<p style="line-height:1.3;font-size:8.3pt">{scr(SCRIPT)}</p>
{sub("R5.2", "Dictation: weak forms (6-second pauses)")}
<p style="font-size:8.6pt">{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S52))}</p>
{sub("R5.3", "Two dialogues (correct versions)")}
<p style="line-height:1.3;font-size:8.3pt">{scr(S53)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 50 - Review 5")
