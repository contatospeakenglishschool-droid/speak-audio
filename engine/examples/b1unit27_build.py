# Speak! Progress B1 - Unit 27 "Extreme adjectives" (all English) - lean B1 format
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
setup(band="B1 · UNIT 27", audio_json="audio_b1-unit-27.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-27"]
S271 = _r["27.1 A voice message from Iceland"].split(": ", 1)[1].replace("thirty-eight degrees", "38 °C (100 °F)")
S272 = [x.split(": ", 1)[1] for x in _r["27.2 Repeat: extreme adjectives"].split("\n")]


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
    cover = cover_html(T, "LEVEL B1 · UNIT 27", "Extreme adjectives", "Paulo in Iceland · <b>absolutely freezing, so… that, such… that</b>",
                       [("YOU CAN", "describe places and experiences in a vivid way and react with strong feelings"),
                        ("LANGUAGE", "exhausted · starving · packed · huge · tiny · It's absolutely freezing! · It was such a long day!"),
                        ("PRONUNCIATION", "stress on extreme adjectives")])
    kw = [("very tired", "exhausted"), ("very hungry", "starving"), ("very crowded", "packed"), ("very cold", "freezing"),
          ("very hot", "boiling"), ("very dirty", "filthy")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:20mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Warm-up: very, very tired", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["Look at the photo. How would you feel on this train?", "When was the last time you were really tired? Why?", "What's the most crowded place you go to every week?"], "START TALKING")}</div></div>
{sub("A", "Key words. Each word means &ldquo;very&rdquo; + an ordinary adjective. Write the extreme adjectives from the box.", "3 min")}
<div class="bank">boiling · exhausted · filthy · freezing · packed · starving</div>
<div style="font-size:8.7pt">{twocol(kwl, 3)}</div>
{talk(["When do you feel starving or exhausted? Tell me about a typical day.", "Describe a place that is always packed, boiling or freezing."], "USE THE WORDS")}""",
    26, """<ol><li>Start with the questions in the top box: this is speaking time, not a test. 4 minutes.</li>
<li>A: quick check (3 minutes). Point out: extreme adjective = <i>very</i> + ordinary adjective, so we don't say <i>very exhausted</i>. Then the two questions with the new words.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Voice message: Paulo in Iceland · why is he there? · complete the adjectives · Talk about it",
                      "ordinary and extreme adjectives, very / absolutely / really, so… that, such… that", "Complete, choose · Use it (oral)",
                      "Stress on extreme adjectives (27.2) · best and worst: tell your stories", "Carol's email · upgrade · word choice · writing"),
        """The Linguahouse lesson is vocabulary only (extreme adjectives, an email from Tokyo). We added the grammar of intensifiers and <i>so / such… that</i>. In B1 Unit 19, Paulo (Ana's brother, travel photographer) bought a down jacket in New York for a photo trip to Iceland; now he is there and sends Ana a voice message. In the homework, Carol (Ana's cousin, Orlando) writes about her friend Linda's wedding in Miami (B1 Units 21–22). Verified facts: around the winter solstice, Reykjavík has about 4 hours of daylight; the sun rises at about 11:20 and sets at about 3:30 p.m. (timeanddate.com; AccuWeather). The Blue Lagoon's water is usually 37–39 °C, about 38 °C on average (bluelagoon.com). Paulo's other details (the wind, the hotel, the hot dog) are his personal experience.""",
        """<i>very + extreme adjective</i> (<i>very exhausted, very delicious</i>), <i>absolutely + ordinary adjective</i>, <i>a so long day</i> for <i>such a long day</i>, and <i>I'm with hunger / I'm with cold</i> for <i>I'm hungry / I'm cold</i>. Brazilians also overuse <i>very</i>; extreme adjectives make speech more natural.""",
        "Track 27.1 A voice message from Iceland (natural and slow) · Track 27.2 Repeat: extreme adjectives"))

    # Page 2 - Listening
    gist = ["on vacation with friends", "to take photos for work", "to visit a friend who lives there"]
    det = [("Paulo is absolutely ___ after the day.", "exhausted"), ("The light is absolutely ___.", "fantastic"), ("The waterfalls were ___.", "huge"),
           ("The Blue Lagoon was ___ with tourists.", "packed"), ("Now he's ___: he hasn't eaten since breakfast.", "starving"),
           ("His hotel room is ___, but it's very clean.", "tiny"), ("The hostel he stayed in last year was ___.", "filthy")]
    dl = "".join(f"<li>{s.replace('___', A(a, 'min-width:17mm'))}</li>" for s, a in det)
    b.page(f"""{sec(2, "Listening: a voice message from Iceland", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{audiocard(["27.1 · NATURAL", "27.1 · SLOW"])}
{sub("A", "Paulo, Ana's brother, sends her a voice message from Iceland. Listen. Why is he there?", "2 min", "27.1")}
<p style="margin:.3mm 0;font-size:8.9pt">{ch(gist, gist[1])}</p></div>{img('B', 40, 27)}</div>
{sub("B", "Listen again. Complete the sentences with the extreme adjectives Paulo uses.", "4 min")}
<ol style="line-height:1.6;font-size:8.8pt;margin:0;columns:2">{dl}</ol>
{talk(["Would you like to visit Iceland in winter, with only four hours of daylight? Why?", "Paulo says the water &ldquo;feels amazing&rdquo; when the air is below zero. Have you ever felt something like that?", "Is it better to travel in the high season or the low season?"])}""",
    32, """<ol><li>A–B: 6 minutes. Paulo is a travel photographer (he bought the jacket in New York in Unit 19). The daylight and Blue Lagoon facts are real (see the story box). Ask: <i>Was the water really boiling?</i> (No, it's an exaggeration: about 38 °C.)</li>
<li>Talk about it: 7 minutes. Encourage extreme adjectives in the answers and note the student's <i>very</i> + adjective for page 3.</li></ol>""")

    # Page 3
    lean.grammar_in_class(b, grammar_ref.extreme_adjectives)

    # Page 4 - Practice
    fs = [("I'm ___ exhausted.", "absolutely"), ("It's ___ cold here.", "very"), ("The light is ___ fantastic.", "absolutely"),
          ("It was ___ a long drive that I almost fell asleep.", "such"), ("The wind was ___ strong that I couldn't hold the camera.", "so")]
    fsl = "".join(f"<li><i>{s.replace('___', A(a, 'min-width:18mm'))}</i></li>" for s, a in fs)
    use = ["Describe the weather today with an extreme adjective.", "Talk about the best meal you've ever had: <i>It was absolutely…</i>", "Talk about a terrible trip: <i>It was so… that…</i>",
           "Describe your home: <i>My kitchen is tiny / huge…</i>", "Talk about a great day: <i>It was such a… day that…</i>"]
    b.page(f"""{sec(4, "Practice: absolutely, so, such", "10 min")}
{sub("A", "Complete the sentences from Paulo's message with absolutely, very, so or such.", "3 min")}
<div class="bank">absolutely · so · such · very</div>
<ol style="line-height:1.85;font-size:8.9pt;margin:0">{fsl}</ol>
{sub("B", "Choose.", "2 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0"><li>The hotel was {ch(["very", "absolutely"], "absolutely")} filthy.</li>
<li>I was {ch(["very", "absolutely"], "very")} hungry, so I ate two hot dogs.</li>
<li>It was {ch(["so", "such"], "such")} a beautiful view!</li></ol>
<div class="box sand"><h4>RULE</h4><b>very, extremely, a bit</b> + ordinary adjectives · <b>absolutely, completely, totally</b> + extreme adjectives · <b>really</b> + both · <b>so</b> + adjective · <b>such (a)</b> + adjective + noun. See the <b>Grammar reference</b> on page 3.</div>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    24, """<ol><li>A–B: 4 minutes. Ask why each answer is right (ordinary or extreme adjective?).</li>
<li>Use it: 6 minutes, all oral. Ask follow-up questions and react with emotion (<i>No way! That sounds awful!</i>) to model page 5.</li></ol>""")

    # Page 5 - Speaking
    cards = ["the best trip you've ever had", "the worst hotel or hostel you've stayed in", "the most delicious meal you've ever eaten", "the most crowded place you've been to",
             "the hottest or coldest day you remember", "a day when you were absolutely exhausted", "a time when you were furious", "the best concert, game or show you've seen"]
    cl = "".join(f"<li>{c}</li>" for c in cards)
    b.page(f"""{sec(5, "Speaking: best and worst", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.3pt"><tr><th>describing</th><th>adding a result</th><th>reacting</th><th>asking for more</th></tr>
<tr><td><i>It was absolutely… · It was such a… · I was completely…</i></td><td><i>It was so… that… · It was such a… that…</i></td><td><i>No way! · That sounds awful / amazing! · You must have been exhausted! · Lucky you!</i></td><td><i>What happened next? · And then? · What was the best part?</i></td></tr></table></div>
{audiocard(["27.2"])}
{sub("A", "Listen and repeat. Stress the extreme adjective and say it with feeling. Which sentence has an ordinary adjective?", "4 min", "27.2")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S272))}</p>
{sub("B", "Choose three topics. Tell your teacher about each one for 1–2 minutes. Use extreme adjectives and so / such… that. Your teacher reacts and asks for more. Then ask your teacher about one topic.", "14 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0;columns:2">{cl}</ol>
{talk(["Do people in your country exaggerate when they tell stories? Is it a good thing?", "Is it rude to say a meal is &ldquo;awful&rdquo; to the cook? What would you say?"], "TALK ABOUT IT")}""",
    30, """<ol><li>A: sentence 4 (<i>It's really cold</i>) has an ordinary adjective. Model the stress: <i>It's ABsolutely FREEzing!</i></li>
<li>B: 12 minutes. React with the phrases in the box and ask follow-up questions. Note every <i>very</i> + extreme adjective. When the student asks you, tell a short, lively story. Last 3 minutes: wrap-up (two corrections, and ask <i>Can you now describe an experience in a vivid way?</i>).</li></ol>""")

    # Homework
    pc = [(["absolutely", "very"], "absolutely"), (["very", "absolutely"], "very"), (["so", "such"], "such"), (["so", "such"], "so"), (["starving", "hungry"], "starving")]
    p = [ch(o, a) for o, a in pc]
    rw = [("The room was very small. (extreme adjective)", "The room was absolutely tiny."), ("The beach was very crowded. (extreme adjective)", "The beach was absolutely packed."),
          ("It was a very long flight. I watched four movies. (such… that)", "It was such a long flight that I watched four movies.")]
    rwl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Carol, Ana's cousin, writes to her about her friend Linda's wedding in Miami. Choose the correct words.", "")}</div>{img('C', 28, 18)}</div>
<div class="box" style="line-height:1.85;font-size:8.8pt;margin:.5mm 0"><b>Hi Ana,</b><br>Linda's wedding was {p[0]} wonderful! I found a dress in the end, and it was {p[1]} comfortable. The ceremony was on the beach, and it was {p[2]} a hot day that everyone was fanning themselves with the program. The party was {p[3]} good that we danced until two in the morning. Dinner was very late, so we were all {p[4]} by then, but the food was delicious. I'm completely exhausted today! Love, Carol</div>
{sub("B", "Rewrite the sentences. Follow the instructions in brackets.", "")}
<ol style="line-height:1.5;font-size:8.7pt;margin:0">{rwl}</ol>
{lean.watch_out([("I'm with hunger.", "I'm hungry / starving.", "feelings like hungry, cold, sleepy are adjectives with <i>be</i>."), ("The food was very delicious.", "The food was absolutely / really delicious.", "<i>delicious</i> is already extreme."), ("It was a so nice day.", "It was such a nice day. / The day was so nice.", "<i>such a</i> + adjective + noun.")])}
{lean.writing_task(sub, "A friend wants to visit your city or country. Write an email: which places are fantastic, which are awful or packed, and the best and worst time of year to come.", "You're going to love it here! The beaches are absolutely…", ["four extreme adjectives", "absolutely / really", "so… that or such… that", "the best and worst time to come", "100–150 words"], "I can describe places and experiences in a vivid way.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class. The writing task is the Linguahouse homework. Read it at home and choose two mistakes to discuss in class.</p>""")

    b.extra("Audio script", f"""
{sub("27.1", "A voice message from Iceland (natural and slow)")}
<p style="line-height:1.35;font-size:8.8pt"><b>Paulo:</b> {S271}</p>
{sub("27.2", "Repeat: extreme adjectives")}
<p>{" · ".join(S272)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 27 - Extreme adjectives")
