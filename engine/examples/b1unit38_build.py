# Speak! Progress B1 - Unit 38 "Moving to a new country" (all English) - lean B1 format
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
setup(band="B1 · UNIT 38", audio_json="audio_b1-unit-38.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-38"]
S381 = [l.split(": ", 1)[1] for l in _r["38.1 Life as an expat"].split("\n")]
S382 = [x.split(": ", 1)[1] for x in _r["38.2 Repeat: I wish"].split("\n")]


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
    cover = cover_html(T, "LEVEL B1 · UNIT 38", "Moving to a new country", "Life as an expat · <b>I wish I spoke… · I wish I could… · If only…</b>",
                       [("YOU CAN", "talk about moving abroad, deal with documents, and say what you wish were different"),
                        ("LANGUAGE", "an expat · a visa · insurance · homesick · I wish I had… · I wish people wouldn't…"),
                        ("PRONUNCIATION", "I wish: stress and weak forms")])
    kw = [("someone living in a country that is not their own", "an expat"), ("a person with the rights of a country, often by birth", "a citizen"),
          ("a document that lets you enter or stay in a country", "a visa"), ("you pay for it, and a company pays if something goes wrong", "insurance"),
          ("the money a country uses", "currency"), ("sad because you are far from home", "homesick")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:21mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Warm-up: a new life abroad", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["Have you ever thought about moving to another country? Where?", "Do you know anyone who lives abroad? How is life for them?", "What do you think is the hardest part of moving abroad?"], "START TALKING")}</div></div>
{sub("A", "Key words. Write the words from the box next to the definitions.", "3 min")}
<div class="bank">a citizen · currency · an expat · homesick · insurance · a visa</div>
<div style="font-size:8.7pt">{twocol(kwl, 3)}</div>
{talk(["Have you ever needed a visa or travel insurance? For which country?", "Have you ever felt homesick? When? What helped?"], "USE THE WORDS")}""",
    26, """<ol><li>Start with the questions in the top box: 4 minutes.</li>
<li>A: quick check (3 minutes), then the two questions. Other words from the Linguahouse lesson: <i>an immigrant</i> (moves to live permanently), <i>a migrant</i> (moves, often to find work), <i>a refugee</i> (forced to leave because of war or danger), <i>a resident</i> (lives in a place).</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Danny's podcast: life as an expat · answer the questions · reasons for moving · Talk about it",
                      "I wish + past simple / could / would(n't); If only; wish vs hope", "Complete, choose · Use it (oral)",
                      "I wish (38.2) · role-play: getting a residence permit", "Danny's email to his mom · rewrite · word choice · writing"),
        """The Linguahouse lesson is vocabulary only (reasons for moving, things to consider, things you need, people in new countries) with a dialogue at an office where a man applies for a residence permit. We kept the vocabulary, the reasons for moving and the office dialogue (now the 1:1 role-play), and added a B1 grammar point that fits the topic: wishes about the present. In a Gap Year Diaries episode, Danny talks honestly about life as an expat in São Paulo: friendly people, great food, some things cheaper than back home (his opinion), a lot of paperwork (a tax number for things like opening a bank account; photocopies of his passport), homesickness, and people switching to English when they hear his accent. He gives three tips. In the homework, Danny writes to his mom. The unit gives no other real-world facts and no rules about visas, which change often.""",
        """<i>I wish I speak…</i> and <i>I wish I can…</i> (no step back), <i>I wish I would have…</i> and <i>I wish you have a great trip</i> (for <i>hope</i>); word choice: <i>I'm with homesick</i>, <i>do my documents</i>, <i>take out my passport</i> for <i>get a passport</i>. Pronunciation: <i>I wish</i> /aɪˈwɪʃ/ with the stress on the new information (<i>I wish I SPOKE better PORtuguese</i>).""",
        "Track 38.1 Life as an expat (natural and slow; Danny's podcast) · Track 38.2 Repeat: I wish"))

    # Page 2 - Listening
    qs = [("How long has Danny lived in São Paulo?", "several months"), ("What three good things does he mention?", "friendly people, amazing food, lower prices"),
          ("Why does he carry photocopies of his passport?", "Every office asks for one."), ("What does he want people to stop doing?", "switching to English"),
          ("What are his three tips?", "learn key phrases, get health insurance, give yourself time")]
    ql = "".join(f"<li>{q} {A(a, 'min-width:46mm')}</li>" for q, a in qs)
    rs = [("a lower cost of living", "M"), ("better job opportunities", "M"), ("discovering a new culture", "P"), ("being with a partner", "P"),
          ("escaping war", "S"), ("getting away from natural disasters", "S"), ("a better climate", "W"), ("a better healthcare system", "W")]
    rsl = "".join(f"<li style='list-style:none'>{A(c, 'min-width:6mm')} {s}</li>" for s, c in rs)
    b.page(f"""{sec(2, "Listening: life as an expat", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Listen to Danny's podcast, Gap Year Diaries. Answer the questions.", "4 min")}
<ol style="line-height:1.5;font-size:8.6pt;margin:0">{ql}</ol></div>{img('B', 36, 26)}</div>
{audiocard(["38.1 · NATURAL", "38.1 · SLOW"])}
{sub("B", "Why do people move to a new country? Write M (money and work), P (people and culture), S (safety) or W (weather and well-being).", "3 min")}
<ul style="line-height:1.5;font-size:8.7pt;margin:0;padding-left:2mm;columns:2">{rsl}</ul>
{talk(["Which reasons from B would make you move to another country? Which wouldn't?", "Do you agree with Danny's three tips? What tip would you add?", "What would you miss most about Brazil?"])}""",
    30, """<ol><li>A: play the natural version; play the slow one if needed. 6 minutes.</li>
<li>B: the categories come from the Linguahouse lesson. Some reasons can fit two groups; accept any answer the student can explain.</li>
<li>Talk about it: 4 minutes. Note Danny's sentences with <i>I wish</i> for page 3.</li></ol>""")

    # Page 3
    lean.grammar_in_class(b, grammar_ref.wish_present)

    # Page 4 - Practice
    fs = [("My family lives far away.", "I wish my family lived closer."), ("I can't have dinner with my mom on Sundays.", "I wish I could have dinner with my mom on Sundays."),
          ("I don't speak Portuguese very well.", "I wish I spoke better Portuguese."), ("People switch to English. It's annoying!", "I wish people wouldn't switch to English."),
          ("I don't have a Brazilian driver's license.", "I wish I had a Brazilian driver's license.")]
    fsl = "".join(f'<li><i>{d}</i><br>{A(i, "min-width:90mm")}</li>' for d, i in fs)
    use = ["Tell me three things you wish were different in your life right now.", "What do you wish you could do, but can't?",
           "What do you wish people in your city wouldn't do?", "Which language do you wish you spoke? Why?",
           "What do you hope will happen next year? (hope, not wish)"]
    b.page(f"""{sec(4, "Practice: I wish, If only", "10 min")}
{sub("A", "Danny's problems. Write his wishes.", "4 min")}
<ol style="line-height:1.6;font-size:8.9pt;margin:0">{fsl}</ol>
{sub("B", "Choose.", "2 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0"><li>I wish I {ch(["have", "had"], "had")} more free time.</li>
<li>I wish I {ch(["could", "can"], "could")} visit my grandmother more often.</li>
<li>I {ch(["wish", "hope"], "hope")} you have a great trip!</li></ol>
<div class="box sand"><h4>RULE</h4><b>wish + past simple</b> (a situation now) · <b>wish + could</b> (ability) · <b>wish + someone + would(n't)</b> (a complaint) · <b>hope</b> for good wishes about the future. See the <b>Grammar reference</b> on page 3.</div>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    24, """<ol><li>A–B: 6 minutes. In A1, also accept <i>I wish my family didn't live so far away.</i></li>
<li>Use it: 4 minutes, all oral. Follow up with <i>Why?</i> and <i>What can you do about it?</i></li></ol>""")

    # Page 5 - Speaking
    dc = ["your passport", "a photocopy of your passport", "two photos", "proof of address", "a document that shows you are employed", "health insurance", "the application form, signed and dated"]
    dl = "".join(f"<li>{x}</li>" for x in dc)
    card = f"""<div class="box" style="margin-top:1mm;font-size:8.3pt">{R("<b>Teacher's card (the clerk):</b> ask for each document. Problems: one document is missing at first; the date on the form is old (the student must initial the new date); the photos are the wrong size. The permit takes about three to four weeks, and the student must come back to collect it.")}</div>""" if T else ""
    b.page(f"""{sec(5, "Speaking: at the immigration office", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.3pt"><tr><th>starting</th><th>the clerk</th><th>problems</th><th>finishing</th></tr>
<tr><td><i>Good morning. I need to get… · Am I in the right place?</i></td><td><i>Can I see your…, please? · Do you also have…? · Please initial here.</i></td><td><i>I'm afraid… is missing. · Is that a problem? · Sorry about that, here it is.</i></td><td><i>How long do I have to wait? · Will it be sent to me? · Do you need anything else?</i></td></tr></table></div>
{audiocard(["38.2"])}
{sub("A", "Listen and repeat. Stress the new information: I wish I SPOKE better PORtuguese.", "4 min", "38.2")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S382))}</p>
{sub("B", "You have just moved to a new country and need a residence permit. Your teacher is the clerk. Show your documents, deal with the problems, and find out how long it takes. Then change roles.", "14 min")}
<ol style="line-height:1.4;font-size:8.8pt;margin:0;columns:2">{dl}</ol>{card}
{talk(["Which is the hardest when you arrive in a new country: finding a place to live, getting documents, making friends, understanding the transportation system, paying taxes or fitting in? Why?", "Would you like to live abroad one day? Where, and for how long?"], "TALK ABOUT IT")}""",
    32, """<ol><li>A: <i>I wish</i> is fast; stress the verb and the key noun.</li>
<li>B: use the teacher's card above. When you change roles, the student is the clerk and you forget something. Last 3 minutes: wrap-up (two corrections, and ask <i>Can you now deal with documents and talk about what you wish were different?</i>). The first Talk about it question is the Linguahouse ranking task.</li></ol>""")

    # Homework
    pc = [(["lived", "live"], "lived"), (["could", "can"], "could"), (["understood", "understand"], "understood"),
          (["wouldn't", "don't"], "wouldn't"), (["were", "is"], "were")]
    p = [ch(o, a) for o, a in pc]
    rw = [("I'm sorry I don't have a car. (I wish)", "I wish I had a car."),
          ("I can't speak Italian. (I wish … could)", "I wish I could speak Italian."),
          ("My neighbor always plays loud music. It's annoying. (I wish … wouldn't)", "I wish my neighbor wouldn't play loud music.")]
    rwl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Danny writes to his mom. Choose the correct words.", "")}</div>{img('C', 28, 18)}</div>
<div class="box" style="line-height:1.85;font-size:8.8pt;margin:.5mm 0"><b>Hi Mom!</b><br>Everything's great here, but I miss you. I wish you {p[0]} closer, and I wish I {p[1]} come home for your birthday. My Portuguese is much better, but I wish I {p[2]} people when they talk fast. And I wish the guys in my room at the hostel {p[3]} snore so loudly! Good news: I finally have my tax number, so I can open a bank account. I wish the paperwork {p[4]} easier, though! Love, Danny</div>
{sub("B", "Rewrite the sentences with the words in brackets.", "")}
<ol style="line-height:1.5;font-size:8.7pt;margin:0">{rwl}</ol>
{lean.watch_out([("I'm with homesick.", "I'm homesick. / I miss home.", "<i>homesick</i> is an adjective: <i>be homesick</i>."), ("I need to do my documents.", "I need to get my documents. / apply for my documents.", "<i>get</i> or <i>apply for</i> documents."), ("I need to take out my passport.", "I need to get a passport.", "<i>take out</i> = remove from a bag or a pocket.")])}
{lean.writing_task(sub, "Imagine you moved to another country a year ago. Write an email home: what you love, what's hard, and what you wish were different.", "Hi …! I can't believe I've been here for a year!", ["two good things", "two difficulties", "three wishes (past, could, wouldn't)", "two key words from this unit", "100–150 words"], "I can talk about moving abroad and say what I wish were different.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class. Read the writing at home and choose two mistakes to discuss in class.</p>""")

    script = "".join(f"<p style='margin:.5mm 0'>{l}</p>" for l in S381)
    b.extra("Audio script", f"""
{sub("38.1", "Life as an expat (natural and slow; Danny's podcast, Gap Year Diaries)")}
<div style="line-height:1.3;font-size:8.6pt">{script}</div>
{sub("38.2", "Repeat: I wish")}
<p>{" · ".join(S382)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 38 - Moving to a new country")
