# Speak! Bridge A2 - Review 2 (Units 11-19), all English - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
_se.SERIES = "Bridge"
setup(band="A2 · REVIEW 2", audio_json="audio_a2-review-2.json", img_dir="img")

PHOTOS = [("A", "blow up the balloons", "Unit 11"), ("B", "an iceberg", "Unit 13"), ("C", "wind turbines", "Unit 14"), ("D", "a veggie burger", "Unit 15"),
          ("E", "a thrift store", "Unit 16"), ("F", "answer the phone", "Unit 17"), ("G", "a movie theater", "Unit 18"), ("H", "get married", "Unit 19")]

_r = json.load(open("roteiro.json"))["units"]["a2-review-2"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["R2.1 Goodbye dinner"].split("\n")]
S22 = [x.split(": ", 1)[1] for x in _r["R2.2 Listen to the ed"].split("\n")][1:]
S23 = [tuple(x.split(": ", 1)) for x in _r["R2.3 Dialogues"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LEVEL A2 · REVIEW 2", "Review 2", "Units 11–19 · already, yet, still · conditionals · conjunctions · relative clauses · the past simple",
                       [("YOU CAN", "check what you learned in Units 11–19 and plan what to practice"),
                        ("LANGUAGE", "I still haven't… · If we…, we'll… · although · First… Then… · a designer who… · So do I. · When did she…?"),
                        ("PRONUNCIATION", "-ed endings /t/ /d/ /ɪd/ · phone phrases · So am I.")])
    b.page(f"""{sec(1, "Warm-up: photo memory", "5 min")}
{sub("A", "One photo from each unit. Write the word or phrase. Then say one sentence about it with the grammar of that unit.", "5 min")}
<div class="bank">answer the phone · blow up the balloons · get married · an iceberg · a movie theater · a thrift store · a veggie burger · wind turbines</div>
{photo_grid(T, PHOTOS)}
<p class="small" style="margin-top:2mm"><b>Example:</b> wind turbines → <i>Wind turbines are cheap to operate, although they can be noisy.</i></p>""",
    20, """<p>Photos A–H come from Units 11–19 in order (Unit 12, emails, has no photo here). Push each unit's grammar: <i>already / yet / still</i> (11), conditionals (13), conjunctions (14), <i>first, then, at last</i> (15), relative clauses (16), phone phrases (17), <i>so / neither</i> (18), past simple (19).</p>""", cover=cover)

    b.extra("Review overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Units</th><th>SB page</th></tr>
<tr><td>1 Warm-up: photo memory</td><td>5 min</td><td>11–19</td><td>1</td></tr>
<tr><td>2 Listening: a goodbye dinner for Paulo</td><td>10 min</td><td>11–19</td><td>2</td></tr>
<tr><td>3 Grammar: already / yet / still, conditionals, conjunctions</td><td>9 min</td><td>11, 13, 14</td><td>3</td></tr>
<tr><td>4 Grammar: sequencers, relative clauses, past simple</td><td>9 min</td><td>15, 16, 19</td><td>4</td></tr>
<tr><td>5 Vocabulary and emails</td><td>8 min</td><td>11–16, 18</td><td>5</td></tr>
<tr><td>6 Pronunciation and social English</td><td>9 min</td><td>17, 18, 19</td><td>6</td></tr>
<tr><td>7 Reflect and homework</td><td>5 min</td><td>11–19</td><td>7</td></tr></table>
<div class="box"><h4>HOW THIS GUIDE WORKS</h4>Every page looks like the Student Book page with the same number. Your notes are in the <b>yellow box</b>; <span class="red">answers in red</span> are not in the Student Book. This is a review: don't teach everything again. Let the student work, then focus on the mistakes that come back. The grammar reference pages (page 4) of Units 11–19 are useful here.</div>
<div class="box sand"><h4>THE STORY SO FAR</h4>Sunday evening in Chicago. Paulo came on the overnight train (Unit 17) and went to the movies with Tom (Unit 18). Now it's his last night, and Tom, Lucy and Kate have a goodbye dinner for him. Kate has brought a carrot cake (Unit 11), but the takeout from the new burger place still hasn't arrived (Unit 15). Paulo is wearing a Grace Kim jacket (Unit 16), is taking the train back because it's greener (Units 13–14), and gets a call from Carol, who's visiting him in New York (Units 12, 17). Lucy talks about the Grace Kelly podcast (Unit 19). No new facts: the story only uses what the students know from Units 11–19.</div>
<div class="box"><h4>THE TOP 5 MISTAKES TO WATCH</h4>1. <i>I didn't make the cake yet / I already have made it</i> → <b>I haven't made the cake yet / I've already made it</b>. 2. <i>If we will protect forests…</i> → <b>If we protect forests, …will…</b> 3. <i>a designer which / a place that you buy clothes</i> → <b>a designer who / a place where you buy clothes</b>. 4. <i>I'm tired. – Me too am I / So I am</i> → <b>So am I. / Me too.</b> 5. <i>Did she won? / When they got married?</i> → <b>Did she win? / When did they get married?</b></div>
<div class="box"><h4>AUDIO</h4>Track R2.1 A goodbye dinner (slow and natural) · Track R2.2 -ed endings · Track R2.3 Two dialogues</div>""")

    # Page 2
    topics = [("takeout food", True), ("a jacket", True), ("a train trip", True), ("a wedding cake", False), ("solar panels", True), ("a phone call", True), ("an American princess", True)]
    tl = " &nbsp; ".join(f"☐ {t}{(' ' + R('✓')) if ok else ''}" for t, ok in topics)
    tf = [("Kate still hasn't made the dessert.", "F: she's already put it in the fridge."), ("Tom ordered the food an hour ago.", "T"),
          ("At first, Tom loved the burger place.", "F: at first he didn't want to try it."), ("Paulo bought his jacket at Grace Kim's studio.", "T"),
          ("Paulo is flying back to New York.", "F: he's taking the train."), ("Kate knew about Grace Kelly.", "F: Tom knew; Kate didn't.")]
    tfl = [f'<li value="{i+1}">{s} <b>T / F</b> {R(a)}</li>' for i, (s, a) in enumerate(tf)]
    find = [("already, yet or still (Unit 11)", "have you brought the dessert yet? / I've already put it / the food still hasn't arrived"),
            ("a first conditional (Unit 13)", "If more people take the train, the air will be cleaner."),
            ("because or although (Unit 14)", "because trains produce less carbon dioxide / although they were expensive"),
            ("a sequencer (Unit 15)", "At first… then / First… Then… Finally / At last!"), ("a relative clause (Unit 16)", "the designer who makes jackets"),
            ("a phone phrase (Unit 17)", "Hang on a minute. / You're breaking up. / I'll call you back."),
            ("an agreeing reply (Unit 18)", "So am I! / Neither did I. / Me too!"), ("a past simple question (Unit 19)", "Who did she marry?")]
    fl = "".join(f"<li>{x} {R(y)}</li>" for x, y in find)
    b.page(f"""{sec(2, "Listening: a goodbye dinner for Paulo", "10 min")}
<p>It's Paulo's last night in Chicago. Tom, Lucy and Kate are having a goodbye dinner for him.</p>
{audiocard(["R2.1 · SLOW", "R2.1 · NATURAL"])}
{sub("A", "Listen. What do they talk about? Check (✓) six topics. One topic is extra.", "2 min", "R2.1 · SLOW")}
<p style="font-weight:600">{tl}</p>
{sub("B", "Listen again. True (T) or false (F)? Correct the false sentences.", "4 min", "R2.1 · NATURAL")}
{twocol(tfl, 3)}
{sub("C", "Find one example in the conversation of each form.", "4 min")}
<ol>{fl}</ol>""",
    22, """<p>A: the extra topic is <i>a wedding cake</i> (Unit 17). C: let the student read the script (TB last page) to find the forms, or play the natural version again and pause. Ask: <i>Do you prefer trains or planes? Why?</i></p>""")

    # Page 3
    ay = [("Have you sent the invitations", "yet", "?"), ("Kate has", "already", "made the cake."), ("I", "still", "haven't wrapped the presents!"),
          ("We haven't bought the balloons", "yet", "."), ("Tom has", "already", "tried every burger on the menu."), ("Lucy", "still", "hasn't called Kate back.")]
    ayl = [f'<li value="{i+1}">{a} {A(w, "min-width:16mm")}{"" if e in "?." else " "}{e}</li>' for i, (a, w, e) in enumerate(ay)]
    cd = [("If we", "protect", "forests, the trees", "will help", "us. (protect / help)"), ("When ice", "melts", ", sea levels", "rise", ". (melt / rise)"),
          ("If you", "ride", "a bike, you", "will produce", "less carbon dioxide. (ride / produce)"), ("Temperatures", "will keep", "rising if we", "don't change", ". (keep / not change)")]
    cdl = "".join(f"<li>{a} {A(v1, 'min-width:16mm')} {m} {A(v2, 'min-width:20mm')} {e}</li>" for a, v1, m, v2, e in cd)
    cj = [(["so", "because"], "so", "Solar panels are cheaper now,", "many people install them."), (["because", "although"], "although", "Wind turbines are cheap,", "they can be noisy."),
          (["but", "so"], "but", "Fossil fuels will run out,", "the sun's energy won't."), (["because", "so"], "because", "Heat pumps are reliable", "they rarely break down.")]
    cjl = [f'<li value="{i+1}">{a} {ch(o, r)} {c}</li>' for i, (o, r, a, c) in enumerate(cj)]
    b.page(f"""{sec(3, "Grammar: already / yet / still, conditionals, conjunctions", "9 min")}
{sub("A", "Unit 11. Complete with already, yet or still.", "3 min")}
{twocol(ayl, 3)}
{sub("B", "Unit 13. Complete the zero and first conditionals.", "3 min")}
<ol>{cdl}</ol>
{sub("C", "Unit 14. Choose the correct conjunction.", "3 min")}
{twocol(cjl, 2)}""",
    24, """<ol><li>A: <b>yet</b> at the end (questions, negatives); <b>already</b> before the main verb; <b>still</b> before <i>haven't</i>.</li>
<li>B: 2 is a zero conditional (always true): present + present. Never <i>will</i> after <i>if</i>. C: ask for one true sentence about energy in Brazil.</li></ol>""")

    # Page 4
    sq = [(["First", "At last"], "First", ", I tried the bean burger."), (["Then", "At first"], "Then", ", I tried the nut burger."),
          (["Finally", "First"], "Finally", ", I tried the fries."), (["At first", "Finally"], "At first", ", I didn't like it, but then I loved it."),
          (["At last", "Then"], "At last", "! The food is here. We waited an hour!")]
    sql = [f'<li value="{i+1}">{ch(o, r)}{c}</li>' for i, (o, r, c) in enumerate(sq)]
    rc = [("Grace is a designer", "who", "makes jackets out of old jeans."), ("A thrift store is a place", "where", "you can buy second-hand clothes."),
          ("Denim is a material", "that / which", "lasts for years."), ("Paulo is the photographer", "who", "took the photos for the article."),
          ("Union Station is the place", "where", "Paulo's train arrived.")]
    rcl = "".join(f"<li>{a} {A(w, 'min-width:18mm')} {c}</li>" for a, w, c in rc)
    ps = [("When", "was", "Grace Kelly born?", "In 1929, in Philadelphia."), ("Who", "did she marry", "?", "Prince Rainier of Monaco."),
          ("When", "did they get", "married?", "In April 1956."), ("", "Did she make", "more movies after that?", "No, she didn't.")]
    psl = "".join(f"<li>{a} {A(v, 'min-width:24mm')} {c} <span class='small'>—</span> <i>{ans}</i></li>" for a, v, c, ans in ps)
    b.page(f"""{sec(4, "Grammar: sequencers, relative clauses, past simple", "9 min")}
{sub("A", "Unit 15. Tom tells the story of his first takeout. Choose the correct word.", "2 min")}
{twocol(sql, 3)}
{sub("B", "Unit 16. Complete with who, which, that or where.", "3 min")}
<ol>{rcl}</ol>
{sub("C", "Unit 19. Complete the questions about Grace Kelly. Look at the answers.", "3 min")}
<ol>{psl}</ol>
<div class="box sand"><h4>REMEMBER</h4><b>who</b> = people · <b>which / that</b> = things · <b>where</b> = places. Past simple questions: <b>did + base form</b> (<i>Who did she marry?</i>), but <b>was / were</b> for <i>born</i>.</div>""",
    24, """<ol><li>A: <i>at first</i> = in the beginning (it changes later); <i>at last</i> = after a long wait. B: in 3, both <i>that</i> and <i>which</i> are correct.</li>
<li>C: watch for <i>When they got married?</i> and <i>Did she made…?</i>. Ask the student two questions about a famous person.</li></ol>""")

    # Page 5
    pt = [("blow up", "the balloons"), ("wrap", "the presents"), ("light", "the candles"), ("send", "the invitations")]
    ptl = " · ".join(f"<b>{v}</b> {A(n, 'min-width:20mm')}" for v, n in pt)
    em = [("the place where your new emails arrive", "inbox"), ("add a file or a photo to an email", "attach"), ("emails you don't want, often ads", "spam"), ("the short title of an email", "subject")]
    eml = "".join(f"<li>{d} → {A(w, 'min-width:16mm')}</li>" for d, w in em)
    cl = [("Oil, gas and coal are", "fossil fuels"), ("Solar and wind energy are", "renewable"), ("When ice melts, sea levels", "rise"), ("A good car doesn't break down. It's", "reliable")]
    cll = "".join(f"<li>{a} {A(w, 'min-width:18mm')}.</li>" for a, w in cl)
    fm = [("A movie that makes you laugh is a", "comedy"), ("A movie that's real, not a story, is a", "documentary"), ("A material that comes from sheep is", "wool"), ("Jeans are made of", "denim")]
    fml = "".join(f"<li>{a} {A(w, 'min-width:18mm')}.</li>" for a, w in fm)
    ep = [("Dear Ms. Clark,", "formal"), ("Hi Paulo!", "informal"), ("It's great to hear from you!", "informal"), ("I look forward to hearing from you.", "formal"),
          ("Love, Carol", "informal"), ("Best regards,", "formal")]
    ept = "".join(f"<td style='text-align:center'><b>{p}</b><br>{R(f)}</td>" for p, f in ep)
    b.page(f"""{sec(5, "Vocabulary and emails", "8 min")}
<div class="two"><div>{sub("A", "Unit 11. Complete the party jobs.", "1 min")}
<div class="bank">the balloons · the candles · the invitations · the presents</div><p style="line-height:2">{ptl}</p></div>
<div>{sub("B", "Unit 12. Email words.", "2 min")}
<div class="bank">attach · inbox · spam · subject</div><ol>{eml}</ol></div></div>
<div class="two"><div>{sub("C", "Units 13–14. Climate and energy.", "2 min")}
<div class="bank">fossil fuels · reliable · renewable · rise</div><ol>{cll}</ol></div>
<div>{sub("D", "Units 16 and 18. Movies and materials.", "1 min")}
<div class="bank">comedy · denim · documentary · wool</div><ol>{fml}</ol></div></div>
{sub("E", "Unit 12. Formal or informal? Write F or I.", "2 min")}
<table style="table-layout:fixed;margin-top:0"><tr>{ept}</tr></table>""",
    22, """<p>After each block, ask for a personal sentence: <i>What was the last party you planned? Do you get a lot of spam? What kind of movies do you like?</i> E: Brazilians often mix styles in one email (<i>Dear Ms. Clark… Kisses!</i>).</p>""")

    # Page 6
    d1 = [("Rita", "Hello, City Coffee. Rita <u>talking</u>. How can I help you?"), ("Kate", "Hello. Could I <u>talk with</u> Lucy, please?"),
          ("Rita", "Who's calling, please?"), ("Kate", "<u>I am</u> Kate Miller, from Sweet Kate Bakery."),
          ("Rita", "I'm afraid she isn't here today. Would you like to leave a message?"), ("Kate", "Yes, please. Can you ask her to call me <u>again</u>?"),
          ("Rita", "Of course. I'll make sure she gets the message.")]
    d2 = [("Lucy", "I'm really tired today."), ("Kate", "<u>So I am</u>. I didn't sleep well."), ("Lucy", "<u>Neither I did</u>. I don't like hot nights."),
          ("Kate", "<u>Me too</u>. But I love summer!"), ("Lucy", "<u>So I do</u>!")]
    def dlg(lines):
        return "<br>".join(f"<b>{n}:</b> {t}" for n, t in lines)
    ed = ["watched", "moved", "wanted", "finished", "decided", "played"]
    eda = {"/t/": "watched, finished", "/d/": "moved, played", "/ɪd/": "wanted, decided"}
    edt = "".join(f"<td style='height:14mm;vertical-align:top'><b>{k}</b><br>{R(v)}</td>" for k, v in eda.items())
    b.page(f"""{sec(6, "Pronunciation and social English", "9 min")}
{audiocard(["R2.2", "R2.3"])}
{sub("A", "Unit 19. Listen to the past simple verbs. Write each verb in the correct column.", "3 min", "R2.2")}
<div class="bank">decided · finished · moved · played · wanted · watched</div>
<table style="table-layout:fixed;margin-top:0"><tr>{edt}</tr></table>
{sub("B", "Units 17–18. Each dialogue has mistakes (underlined). Correct them. Then listen and check.", "4 min", "R2.3")}
<div class="two"><div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.8pt;line-height:1.5"><b>Dialogue 1</b><br>{dlg(d1)}</div>
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.8pt;line-height:1.5"><b>Dialogue 2</b><br>{dlg(d2)}</div></div>
<p class="small">{R("1: Rita speaking · Could I speak to Lucy · It's Kate Miller · call me back — 2: So am I. · Neither did I. · Me neither. · So do I!")}</p>
{sub("C", "Role-play the dialogues with your teacher. Then tell your teacher three things about you. Your teacher agrees or disagrees.", "2 min")}""",
    24, """<ol><li>A: 3-second pause after each verb. The rule: /ɪd/ only after t or d sounds. Avoid <i>watch-ed</i>.</li>
<li>B: on the phone, say <b>It's…</b> or <b>This is…</b>, never <i>I am…</i>. After <i>I don't…</i>, say <b>Me neither</b>.</li></ol>""")

    # Page 7
    ck = [("11", "I can say what's done and not done yet with already, yet and still."), ("12", "I can read and write a friendly email with the right phrases."),
          ("13", "I can explain causes and effects with zero and first conditionals."), ("14", "I can join ideas with and, but, so, because and although."),
          ("15", "I can describe a meal step by step and say how my opinion changed."), ("16", "I can define people, things and places with who, which, that and where."),
          ("17", "I can make and answer phone calls and leave a message."), ("18", "I can agree and disagree with so, neither, me too and me neither."),
          ("19", "I can tell the story of someone's life and ask about the past.")]
    ckr = "".join(f"<tr><td><b>Unit {u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in ck)
    b.page(f"""{sec(7, "Reflect and homework", "5 min")}
{sub("A", "How are you doing? Check one box for each line.", "2 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{ckr}</table>
{sub("B", "My goals. What do you want to practice more? Write two things.", "2 min")}
<div class="wline"></div><div class="wline"></div>
{sub("C", "Homework", "1 min")}
<p><b>An email to Paulo (80–100 words).</b> Paulo is back in New York and wants to hear your news. Write him a friendly email. Include:</p>
<ol><li>a good opening and closing (Unit 12);</li><li>something you've already done this month and something you haven't done yet (Unit 11);</li>
<li>a meal, a movie or a trip you had recently, step by step (Units 15, 18, 19);</li><li>one plan with if and one sentence with although (Units 13–14).</li></ol>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Look at the "Not yet" lines and plan two short review activities for the next classes. The homework uses grammar from all nine units: keep it next to the Review 1 sample. Next: Unit 21, Fables.</p>""")

    b.extra("Audio scripts", f"""
{sub("R2.1", "A goodbye dinner (slow and natural)")}
<p style="line-height:1.32;font-size:8.6pt">{"<br>".join(f"<b>{n}:</b> {t}" if n != "Narrator" else f"<i>{t}</i>" for n, t in SCRIPT)}</p>
{sub("R2.2", "-ed endings (3-second pause after each verb)")}
<p>{" · ".join(S22)}</p>
{sub("R2.3", "Two dialogues (correct versions)")}
<p style="line-height:1.32;font-size:8.6pt">{"<br>".join(f"<b>{n}:</b> {t}" if n != "Narrator" else f"<i>{t}</i>" for n, t in S23)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 20 - Review 2")
