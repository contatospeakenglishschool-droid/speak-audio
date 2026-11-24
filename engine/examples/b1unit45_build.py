# Speak! Progress B1 - Unit 45 "Common expressions 2" (all English) - lean B1 format
import sys, os, json
_h = os.path.dirname(os.path.abspath(__file__))
for _d in ("/home/claude/speak-audio/engine", os.path.join(_h, "..", "speak-audio", "engine"), os.path.join(_h, "..", "..", "speak-audio", "engine"),
           os.path.join(_h, "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Progress"
import lean
from lean import talk
setup(band="B1 · UNIT 45", audio_json="audio_b1-unit-45.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-45"]
S451 = [l.split(": ", 1) for l in _r["45.1 A day out with Carol"].split("\n")]
S452 = [x.split(": ", 1)[1] for x in _r["45.2 Repeat: question tags"].split("\n")]


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
    cover = cover_html(T, "LEVEL B1 · UNIT 45", "Common expressions 2", "Small talk · <b>Lucky you! · Calm down! · It's a long flight, isn't it?</b>",
                       [("YOU CAN", "react with common expressions and keep a conversation going with question tags"),
                        ("LANGUAGE", "Lucky you · Have fun · Well done · Calm down · It doesn't matter · isn't it? · don't you?"),
                        ("PRONUNCIATION", "question tags: falling ↘ or rising ↗")])
    kw = [("I've just won two tickets to the final!", "Lucky you!"), ("I'm off to the party. See you tomorrow!", "Have fun!"),
          ("My plane leaves in two hours.", "Have a good trip!"), ("I finally passed my driving test!", "Well done!"),
          ("I can't come to work today. I've got the flu.", "Get well soon!"), ("The concert was canceled because of the rain.", "What a shame."),
          ("I lost my job today! What am I going to do?", "Calm down."), ("Sorry, I spilled some water on the floor.", "It doesn't matter."),
          ("Can I borrow your car for six months?", "No way!"), ("Can I ask you something?", "Go ahead.")]
    kwl = "".join(f'<li>{s} {A(r, "min-width:26mm")}</li>' for s, r in kw)
    bank = sorted(r.rstrip("!.") for s, r in kw)
    b.page(f"""{sec(1, "Warm-up: what do you say?", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 50, 33)}<div style="flex:1">
{talk(["What do you say to a friend who is leaving on a trip? And to a friend who is sick?", "Do you find small talk easy or difficult? Why?", "Which expressions from Unit 42 do you remember?"], "START TALKING")}</div></div>
{sub("A", "Respond to each sentence with an expression from the box.", "4 min")}
<div class="bank" style="font-size:8.6pt">{" · ".join(bank)}</div>
<ol style="font-size:8.6pt;line-height:1.6;margin:0;columns:2;column-gap:6mm">{kwl}</ol>
{talk(["When did you last say <i>Well done</i> to someone? Why?", "What makes you say <i>No way!</i>?", "Who needs to hear <i>Calm down</i> in your family?"], "USE THE EXPRESSIONS")}""",
    30, """<ol><li>Top box: 3 minutes. Unit 42 had part 1 of these expressions.</li>
<li>A: the student says the answers out loud first, then writes. <i>No way!</i> can mean <i>Absolutely not</i> (item 9) or <i>I can't believe it!</i> (surprise). <i>It doesn't matter</i> answers an apology for something small. <i>Well done</i> is for an achievement that needed effort.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Danny shows Carol around downtown São Paulo · which expression and why? · complete the question tags · Talk about it",
                      "question tags: positive → negative tag, same auxiliary; I'm…, aren't I? · Let's…, shall we?; intonation; answering tags", "Add the tags · check facts about your teacher · Use it (oral)",
                      "question tags ↘ ↗ (45.2) · respond to the teacher's sentences · role-play: meet Carol at a party", "Carol's message to Ana · rewrite as tag questions · watch out · writing a dialogue"),
        """The Linguahouse lesson is part 2 of the social expressions (Calm down, Get well soon, Go ahead, Have a good trip, Have fun, It doesn't matter, Lucky you, No way, Well done, What a shame), with two sets of sentences to respond to. It has no listening text and no grammar, so we added a dialogue and a new B1 grammar point: question tags, the most natural way to make small talk and check information. Story: on Wednesday, his day off, Danny shows Carol (Ana's cousin, staying with Ana for two weeks, Unit 43) around downtown São Paulo; they have lunch at the municipal market (huge sandwiches). Ana asked Danny to look after Carol, who thinks Ana worries too much. Bruno has the flu and stayed in bed. Danny spills juice on Carol's old bag; Carol read the whole menu in Portuguese (six months with an app); she can't find her phone, but it's in her jacket. Ana takes Carol to the beach on Saturday; next week Marcos takes them to Paraty for two days; Carol flies back to Orlando next Friday. No real-world facts are given.""",
        """One fixed tag for every sentence (<i>…, no?</i>); the wrong auxiliary (<i>You went, don't you?</i>); a negative tag after a negative sentence; <i>am not I</i> for <i>aren't I</i>; answering <i>Yes</i> to agree with a negative sentence. <i>Have a good travel</i> for <i>Have a good trip</i>. Pronunciation: falling tags (sure) vs rising tags (real questions).""",
        "Track 45.1 A day out with Carol (natural and slow; Danny and Carol) · Track 45.2 Repeat: question tags"))

    # Page 2 - Listening
    rows = [("Bruno is in bed with the flu.", "Get well soon! / What a shame."), ("Danny spills juice on Carol's bag.", "It doesn't matter."),
            ("Danny wants to ask a question.", "Go ahead."), ("Carol learned Portuguese by herself in six months.", "No way! Well done!"),
            ("Carol can't find her phone.", "Calm down."), ("Carol is going to the beach and to Paraty.", "Lucky you! Have fun!"),
            ("Carol flies back next Friday.", "Have a good trip!")]
    rt = "".join(f'<tr><td>{s}</td><td>{A(e, "min-width:40mm")}</td></tr>' for s, e in rows)
    tg = [("You don't usually work on Wednesdays,", "do you?"), ("Ana asked me to look after you,", "didn't she?"),
          ("Bruno was supposed to come too,", "wasn't he?"), ("These sandwiches are huge,", "aren't they?"),
          ("You put it in your jacket,", "didn't you?"), ("It's a long flight,", "isn't it?")]
    tgl = "".join(f"<li>{s} {A(t, 'min-width:20mm')}</li>" for s, t in tg)
    b.page(f"""{sec(2, "Listening: a day out with Carol", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Danny shows Ana's cousin Carol around São Paulo on his day off. Listen. What do they say in each situation?", "5 min")}
<table style="font-size:8.5pt;margin:.5mm 0"><tr><th>situation</th><th>expression</th></tr>{rt}</table></div>{img('B', 32, 30)}</div>
{audiocard(["45.1 · NATURAL", "45.1 · SLOW"])}
{sub("B", "Listen again. Complete the end of each sentence.", "3 min")}
<ol style="line-height:1.5;font-size:8.6pt;margin:0;columns:2;column-gap:6mm">{tgl}</ol>
<p style="margin:.6mm 0;font-size:8.6pt"><b>Think about it:</b> Carol says "I'm a grown woman!" What does she mean? How does she feel about Ana? {A("Ana worries too much; Carol can look after herself, but she knows Ana cares.", "min-width:20mm")}</p>
{talk(["Have you ever shown a visitor around your city? Where did you go?", "Who in your family worries about you too much?", "What's the longest flight you've taken? Did you sleep?"])}""",
    30, """<ol><li>A: play the natural version; play the slow one if needed. Accept any expression that fits.</li>
<li>B: these short questions at the end are <i>question tags</i>, the grammar of page 3. Ask: <i>Is Danny really asking, or does he already know?</i> (He knows: the tags fall.)</li>
<li>Talk about it: 4 minutes.</li></ol>""")

    # Page 3
    lean.grammar_in_class(b, grammar_ref.question_tags)

    # Page 4 - Practice
    comp = [("You're a teacher,", "aren't you?"), ("She doesn't like seafood,", "does she?"), ("They went to Paraty last year,", "didn't they?"),
            ("You've met my cousin,", "haven't you?"), ("It won't rain tomorrow,", "will it?"), ("I'm late again,", "aren't I?"),
            ("Let's get a coffee,", "shall we?"), ("Your brother can drive,", "can't he?")]
    cl = "".join(f"<li>{s} {A(t, 'min-width:20mm')}</li>" for s, t in comp)
    gs = [("where your teacher lives", "You live in …, don't you?"), ("something your teacher likes", "You like …, don't you?"),
          ("something your teacher did last weekend", "You went to …, didn't you?")]
    gsl = "".join(f'<li>{d}<br>{R("Possible: " + i) if T else lines(1)}</li>' for d, i in gs)
    use = ["You were born in a big city, …?", "You can cook, …?", "You've never been to Japan, …?", "You don't like getting up early, …?", "You're going to travel this year, …?"]
    b.page(f"""{sec(4, "Practice: isn't it? don't you?", "10 min")}
{sub("A", "Add the question tags.", "3 min")}
<ol style="line-height:1.75;font-size:8.8pt;margin:0;columns:2;column-gap:6mm">{cl}</ol>
{sub("B", "What do you think you know about your teacher? Write sentences with tags. Then ask: is it true?", "4 min")}
<ol style="line-height:1.45;font-size:8.7pt;margin:0">{gsl}</ol>
{talk(use, "USE IT: FINISH THE QUESTIONS AND ASK YOUR TEACHER. ANSWER THE FACTS.")}""",
    30, """<ol><li>A: 3 minutes. Item 6: <i>aren't I</i>. Item 7: <i>Let's…, shall we?</i></li>
<li>B: the student asks with falling or rising intonation depending on how sure they are. Answer with the facts.</li>
<li>Use it: 3 minutes. Then you ask the same questions; the student answers <i>Yes, I do / No, I don't</i> by the facts (not to agree).</li></ol>""")

    # Page 5 - Speaking
    card1 = f"""<div class="box" style="margin-top:1mm;font-size:8.1pt">{R("<b>Teacher's card (B):</b> read one by one: I won the tennis match! (Well done!) · Is it OK if I open the window? (Go ahead.) · There's a huge spider on the table! (Calm down!) · My vacation starts today. (Lucky you! / Have fun!) · Sorry, I forgot your pen at home. (It doesn't matter.) · Can I call you tomorrow at 5 a.m.? (No way!) · I'm flying to Lisbon tonight. (Have a good trip!) · I can't come to the movies tonight. (What a shame.) · I'm in bed with a fever. (Get well soon!)")}</div>""" if T else ""
    card2 = f"""<div class="box" style="margin-top:1mm;font-size:8.1pt">{R("<b>Teacher's card (C):</b> you are Carol at Ana's party. You live in Orlando; you're staying with Ana for two weeks; you've been teaching yourself Portuguese for six months; you're going to the beach on Saturday and to Paraty next week; you fly back next Friday; you didn't sleep on the plane. Answer the student's tags with the facts and ask tags back (You work with Ana, don't you?).")}</div>""" if T else ""
    b.page(f"""{sec(5, "Speaking: small talk", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.2pt"><tr><th>starting small talk</th><th>checking</th><th>reacting</th><th>saying goodbye</th></tr>
<tr><td><i>Lovely day, isn't it? · Great party, isn't it? · You're a friend of Ana's, aren't you?</i></td><td><i>You live near here, don't you? · You've been here before, haven't you?</i></td><td><i>No way! · Lucky you! · Well done! · What a shame.</i></td><td><i>Have fun! · Have a good trip! · Get well soon! · See you!</i></td></tr></table></div>
{audiocard(["45.2"])}
{sub("A", "Listen and repeat. The tags fall ↘: the speaker is sure.", "3 min", "45.2")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S452))}</p>
{sub("B", "Cover page 1. Your teacher says some sentences. Respond quickly with an expression.", "5 min")}{card1}
{sub("C", "Role-play. You're at Ana's party and you meet Carol (your teacher). Check what you know about her with question tags and react. Then swap: you're a guest and your teacher checks facts about you.", "7 min")}{card2}
{talk(["Where do you make small talk: at work, in elevators, at the gym? What do you talk about?"], "TALK ABOUT IT")}""",
    30, """<ol><li>A: then say the same tags with a rising tune and ask the student to hear the difference (real question).</li>
<li>B is the Linguahouse practice, adapted for 1:1. C: the student uses at least four tags. Last 3 minutes: wrap-up (two corrections, and ask <i>Can you now make small talk with question tags?</i>).</li></ol>""")

    # Homework
    pc = [(["isn't he", "is he"], "isn't he"), (["Get well soon", "Have fun"], "Get well soon"), (["doesn't matter", "isn't matter"], "doesn't matter"),
          (["calm down", "be calm down"], "calm down"), (["aren't you", "don't you"], "aren't you"), (["shall we", "will we"], "shall we")]
    p = [ch(o, a) for o, a in pc]
    rw2 = [("I think you're from Recife. Am I right?", "You're from Recife, aren't you?"),
           ("I think she didn't call. Am I right?", "She didn't call, did she?"),
           ("I think you've seen this movie. Am I right?", "You've seen this movie, haven't you?")]
    rwl2 = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw2)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Carol writes to Ana from downtown São Paulo. Choose the correct words.", "")}</div>{img('C', 30, 19)}</div>
<div class="box" style="line-height:1.85;font-size:8.8pt;margin:.5mm 0"><b>Hi Ana!</b> Danny is a great guide, {p[0]}? We had lunch at the market: the sandwiches are enormous! Bruno couldn't come because he has the flu, so I sent him a message: "{p[1]}!" Danny spilled juice on my bag, but it {p[2]}: it's my old one. Then I couldn't find my phone, and Danny told me to {p[3]}. It was in my jacket! You're working late tonight, {p[4]}? Let's order pizza tomorrow, {p[5]}? Love, Carol</div>
{sub("B", "Rewrite the sentences with a question tag.", "")}
<ol style="line-height:1.5;font-size:8.7pt;margin:0">{rwl2}</ol>
{lean.watch_out([("You're Brazilian, no?", "You're Brazilian, aren't you?", "use a real tag: the same auxiliary + pronoun."), ("Have a good travel!", "Have a good trip!", "<i>travel</i> is a verb or an uncountable noun; one journey = <i>a trip</i>."), ("You don't eat meat, do you? — Yes. (= I don't)", "No, I don't.", "answer about the facts, not to agree.")])}
{lean.writing_task(sub, "Write a short dialogue: you meet a new colleague on their first day at work.", "A: You're the new designer, aren't you?", ["at least four question tags", "three expressions from page 1", "a positive and a negative sentence with tags", "a goodbye: Have fun! / See you!", "100–150 words"], "I can react with common expressions and keep a conversation going with question tags.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class. In A, <i>You're working late tonight, aren't you?</i>: the auxiliary is <i>are</i>. Ask the student to read the dialogue with you, with falling tags.</p>""")

    script = "".join(f"<p style='margin:.5mm 0'><b>{s}:</b> {t}</p>" for s, t in S451)
    b.extra("Audio script", f"""
{sub("45.1", "A day out with Carol (natural and slow; Danny and Carol)")}
<div style="line-height:1.3;font-size:8.4pt">{script}</div>
{sub("45.2", "Repeat: question tags")}
<p>{" · ".join(S452)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 45 - Common expressions 2")
