# Speak! Bridge A2 - Unit 47 "Question time" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 47", audio_json="audio_a2-unit-47.json", img_dir="img")

PHOTOS = [("A", "a comet", "comet"), ("B", "a galaxy", "galaxy"), ("C", "the universe", "universe"), ("D", "a planet", "planet")]
_r = json.load(open("roteiro.json"))["units"]["a2-unit-47"]
S471 = [x.split(": ", 1) for x in _r["47.1 Brain Battle"].split("\n")]
S472 = [x.split(": ", 1)[1] for x in _r["47.2 Repeat: questions"].split("\n")]
S473 = [x.split(". ", 1)[1] for x in [y.split(": ", 1)[1] for y in _r["47.3 Up or down?"].split("\n")]]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 47", "Question time", "Quiz show · <b>questions in different tenses</b>",
                       [("YOU CAN", "ask correct questions in many tenses and handle difficult questions in a quiz"),
                        ("LANGUAGE", "How many rings does Saturn have? · Who discovered…? · Where have they sent…? · What would they weigh?"),
                        ("PRONUNCIATION", "question intonation: up or down?")])
    mm = [("explore", "visit a place to see what is there"), ("discover", "find something that no one has seen before"),
          ("a mission", "an important job in another place, sometimes done by machines controlled from far away"), ("approach", "get close to something")]
    ms = sorted(mm, key=lambda x: x[1])
    ml = "".join(f"<li>{d} {A(w, 'min-width:16mm')}</li>" for w, d in ms)
    b.page(f"""{sec(1, "Warm-up: space", "8 min")}
{sub("A", "Name the photos. Then put them in order from the smallest to the largest.", "3 min")}
<div style="display:flex;gap:2mm;margin-bottom:1mm">{"".join(f'<div style="position:relative">{img(l, 40, 26)}<b style="position:absolute;top:1mm;left:1.5mm;background:#176074;color:#fff;border-radius:1mm;padding:0 1.2mm;font-size:8pt">{l}</b></div>' for l in "ABCD")}</div>
<div class="bank">comet · galaxy · planet · universe</div>
<p style="margin:.5mm 0">A {A("comet", "min-width:14mm")} B {A("galaxy", "min-width:14mm")} C {A("universe", "min-width:14mm")} D {A("planet", "min-width:14mm")} &nbsp; smallest → largest: {A("comet, planet, galaxy, universe", "min-width:50mm")}</p>
{sub("B", "Write the words next to the meanings: approach · discover · explore · a mission", "3 min")}
<ol style="line-height:1.5;font-size:9pt;margin:0">{ml}</ol>
{sub("C", "Are you interested in space? Would you like to visit another planet? Why or why not?", "2 min")}""",
    22, """<ol><li>A: a comet is much smaller than a planet; a galaxy contains billions of stars; the universe contains everything.</li>
<li>B: unmanned missions are controlled from Earth (robots, rovers, drones).</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Space vocabulary</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Tom answers space questions on a TV quiz show</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Questions: simple forms, multi-word forms, subject questions, intonation</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Making questions</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>4 min</td><td>Questions · up or down?</td><td>5</td></tr>
<tr><td>5 Practice</td><td>9 min</td><td>Animal quiz: write the questions · difficult questions</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Quiz time: write and ask multiple-choice questions</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Tom (Neural2-D) is a contestant on Brain Battle, an invented TV quiz show (Host: Studio-O). His special subject is space, and he gets five of eight questions right. Facts (NASA and NASA/JHU APL): Saturn has seven main rings (A–G); the Earth travels around the sun at about 18.5 miles per second; Edwin Hubble showed that the universe contains many galaxies; on the Moon you weigh about one sixth of your weight on Earth (120 lb → 20 lb); Halley's Comet returns about every 75 years and next in 2061; China (Tianwen-1) and the USA (Perseverance) both sent rovers to Mars in 2021; NASA's Dragonfly mission to Saturn's moon Titan is planned to launch in July 2028 (it was delayed from 2026/2027).</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students make questions with statement order and intonation (<i>Where you live?</i>), forget <i>do/does/did</i>, add <i>did</i> to subject questions (<i>Who did discover…?</i>), and write <i>Did you used to…?</i></div>
<div class="box"><h4>AUDIO</h4>Track 47.1 Brain Battle (slow and natural) · Track 47.2 Repeat: questions · Track 47.3 Up or down?</div>""")

    # Page 2
    qs = [("Saturn's main rings", "seven", "✓"), ("the Earth's speed", "18.5 miles per second", "✓"), ("galaxies", "Edwin Hubble", "✗ (Halley)"), ("weight on the Moon", "20 pounds", "✓"),
          ("what people used to say about the Moon", "cheese", "✗ (butter)"), ("Halley's Comet", "2061", "✗ (2051)"), ("robots on", "Mars", "✓"), ("Dragonfly", "Titan", "✓")]
    ql = [f'<li value="{i+1}">{t}: {A(a, "min-width:24mm")} Tom: {A(r, "min-width:14mm")}</li>' for i, (t, a, r) in enumerate(qs)]
    op = [("How many rings does Saturn", ["has", "have"], "have", "?"), ("How fast is the Earth", ["moving", "moved"], "moving", "?"), ("Who", ["did discover", "discovered"], "discovered", "that there are many galaxies?"),
          ("If a person went to the Moon, what", ["would", "do"], "would", "they weigh?"), ("What", ["did people use", "used people"], "did people use", "to say about the Moon?"),
          ("In what year will the comet", ["to approach", "approach"], "approach", "the Earth again?"), ("Where", ["have", "did"], "have", "China and the USA recently sent robots?"),
          ("Where is the Dragonfly mission", ["going", "goes"], "going", "to travel to?")]
    opl = [f'<li value="{i+1}">{a} {ch(o, r)}{"" if e == "?" else " "}{e}</li>' for i, (a, o, r, e) in enumerate(op)]
    b.page(f"""{sec(2, "Listening: Brain Battle", "10 min")}
<div style="display:flex;gap:2.5mm;align-items:center"><p style="flex:1;margin:0">Tom is a contestant on Brain Battle, a TV quiz show. His special subject is space. How many questions will he get right?</p>{img('E', 30, 20)}</div>
{audiocard(["47.1 · SLOW", "47.1 · NATURAL"])}
{sub("A", "Listen. Write the correct answers and check (✓) Tom's correct answers. What's his score?", "4 min", "47.1 · SLOW")}
<div style="font-size:8.8pt">{twocol(ql, 5)}</div>
<p style="margin:.3mm 0">Tom's score: {A("5 out of 8", "min-width:16mm")} · Did you know any of the answers?</p>
{sub("B", "Listen again and choose the correct option.", "5 min", "47.1 · NATURAL")}
<div style="font-size:8.8pt">{twocol(opl, 5)}</div>""",
    22, """<ol><li>A: a <i>contestant</i> = a person who competes on a show. Facts in the story box come from NASA.</li>
<li>B: the student should explain each choice; this prepares the Language focus.</li></ol>""")

    # Page 3
    mt = [("How fast is the Earth moving?", "c present continuous"), ("If a person went to the Moon, what would they weigh?", "e second conditional"),
          ("In what year will the comet approach the Earth again?", "b future prediction"), ("Where have China and the USA recently sent robots?", "d present perfect"),
          ("Where is the Dragonfly mission going to travel to?", "a future plan")]
    mtl = "".join(f"<li>{q} {A(c, 'min-width:28mm')}</li>" for q, c in mt)
    b.page(f"""{sec(3, "Language focus: making questions", "10 min")}
{sub("A", "Simple forms. Read and answer.", "3 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">1 How many rings <b>does</b> Saturn <b>have</b>? · 2 <b>Who discovered</b> that there are many galaxies? · 3 What <b>did</b> people <b>use to</b> say about the Moon?</div>
<ol style="margin:.5mm 0;line-height:1.65"><li>Do simple forms usually need an auxiliary (do, does, did) in questions? {ch(["yes", "no"], "yes")}</li>
<li>Why doesn't question 2 have an auxiliary? {A("Who is the subject: a subject question.", "min-width:50mm")}</li></ol>
{sub("B", "Multi-word forms. Match the questions with a–e.", "4 min")}
<ol style="line-height:1.5;font-size:8.8pt;margin:0">{mtl}</ol>
<p class="small" style="margin:.5mm 0"><b>a</b> future plan · <b>b</b> future prediction · <b>c</b> present continuous · <b>d</b> present perfect · <b>e</b> second conditional</p>
<p style="margin:.5mm 0">How do we make these questions? {A("Change the order: auxiliary + subject + verb (no do/did).", "min-width:70mm")}</p>
{sub("C", "Intonation. Does your voice go up or down?", "3 min")}
<p style="margin:.5mm 0;line-height:1.7"><i>Are you ready? · Do you know this one?</i> (yes/no questions) {ch(["up ↗", "down ↘"], "up ↗")} &nbsp; <i>Where do you live?</i> (wh- question) {ch(["up ↗", "down ↘"], "down ↘")}</p>
<div class="box sand"><h4>RULE</h4><b>Simple forms:</b> (question word) + do / does / did + subject + base form. <b>Multi-word forms:</b> (question word) + auxiliary (is, have, will, would) + subject + verb. <b>Subject questions:</b> no auxiliary, statement order. More on the next page: <b>Grammar reference</b>.</div>""",
    20, """<ol><li>A: <i>used to</i> in questions: <i>Did people use to…?</i> (no -d).</li>
<li>Drill all the questions with the right intonation; then ask the student to read the quiz host's lines.</li></ol>""")

    grammar_ref.question_forms(b)

    # Page 5
    ud = ["up ↗", "down ↘", "up ↗", "down ↘", "up ↗", "down ↘"]
    udl = "".join(f"<li>{A(x, 'min-width:14mm;text-align:center')}</li>" for x in ud)
    b.page(f"""{sub("D", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>Where you live?</td><td><b>Where do you live?</b></td><td>present simple: do.</td></tr>
<tr><td>Who did discover the galaxies?</td><td><b>Who discovered the galaxies?</b></td><td>subject question.</td></tr>
<tr><td>How many rings Saturn has?</td><td><b>How many rings does Saturn have?</b></td><td>does + base form.</td></tr>
<tr><td>Where you are going?</td><td><b>Where are you going?</b></td><td>change the order.</td></tr>
<tr><td>Did you used to play soccer?</td><td><b>Did you use to play soccer?</b></td><td>did + use (no -d).</td></tr>
<tr><td>What you would do?</td><td><b>What would you do?</b></td><td>would + subject.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "4 min")}
{audiocard(["47.2", "47.3"])}
{sub("A", "Listen and repeat. Copy the intonation.", "2 min", "47.2")}
{twocol([f'<li value="{i+1}">{s}</li>' for i, s in enumerate(S472)], 4)}
{sub("B", "Listen to six questions. Does the voice go up or down at the end?", "2 min", "47.3")}
<ol style="line-height:1.5;column-count:3;column-gap:5mm">{udl}</ol>""",
    30, """<ol><li>A: <i>does</i> and <i>did</i> are weak: /dəz/, /dɪd/ → "How many rings d'z Saturn have?"</li>
<li>B: script: 1 Are you ready? 2 Where do you live? 3 Do you know this one? 4 What would you do? 5 Have you ever been to Mars? 6 How fast is it moving? yes/no ↗, wh- ↘ (this is the general pattern; wh- questions can rise when you are friendly or surprised).</li></ol>""")

    # Page 6
    aq = [("What very small animal", "have scientists discovered in Madagascar", "Scientists have discovered the smallest known chameleon in Madagascar."),
          ("When", "did the last dodo die", "The last dodo died in the late 1600s."),
          ("Where", "do dolphins live", "Most dolphins live in the ocean, but the pink river dolphin lives in the Amazon."),
          ("If a horse and a kangaroo had a race, which", "animal would win", "The horse would win."),
          ("What pet", "did Ana use to have", "Ana used to have a dog called Mel."),
          ("How many hours a day", "does a koala sleep", "A koala sleeps about 20 hours a day."),
          ("Where", "are the scientists going to look for new animals", "They're going to look for new animals in the rainforest."),
          ("Why", "is this turtle digging a hole", "It's digging a hole to lay its eggs.")]
    aql = "".join(f"<li>{s} {A(m, 'min-width:44mm')}? <span class='small'>– {a}</span></li>" for s, m, a in aq)
    dk = [("Hmm… I'd have to", ["know", "think"], "think", "about that.", "TT"), ("I haven't", ["got", "had"], "got", "a clue.", "DK"), ("It's on the tip of my", ["nose", "tongue"], "tongue", "!", "TT"),
          ("I have no", ["thought", "idea"], "idea", ", sorry.", "DK"), ("I'm", ["afraid", "scared"], "afraid", "I don't know.", "DK"), ("That's", ["the", "a"], "a", "good question.", "TT")]
    dkl = "".join(f"<li>{a} {ch(o, r)}{'' if e[0] in '!,' else ' '}{e} {A(t, 'min-width:8mm;text-align:center')}</li>" for a, o, r, e, t in dk)
    b.page(f"""{sec(5, "Practice", "9 min")}
{sub("A", "The next contestant's subject is animals. Read the answers and write the questions. Be careful with the tenses.", "5 min")}
<ol style="line-height:1.45;font-size:8.8pt;margin:0">{aql}</ol>
{sub("B", "Difficult questions. Choose the correct word. Then write DK (I don't know) or TT (I need thinking time).", "4 min")}
<ol style="line-height:1.55;font-size:9pt;margin:0;column-count:2;column-gap:5mm">{dkl}</ol>""",
    26, """<ol><li>A: facts: the smallest known chameleon (<i>Brookesia nana</i>) was described in 2021 in Madagascar; dodos died out in the late 1600s; koalas sleep about 18–22 hours a day; the Amazon pink river dolphin lives in fresh water. Mel is Ana's childhood dog (story).</li>
<li>B: thinking-time phrases are said slowly, with a thinking voice; they're useful in speaking exams.</li></ol>""")

    # Page 7
    mine = [("Which country in South America", "has the largest population", "Brazil"), ("Which river", "carries the most water in the world", "the Amazon"),
            ("Where", "would you be if you saw a koala in the wild", "in Australia"), ("When", "did Brasília become the capital of Brazil", "in 1960"),
            ("What", "is the largest organ of the human body", "the skin"), ("How many bones", "does an adult human have", "206"),
            ("When", "did doctors do the first heart transplant", "in 1967")]
    ml = "".join(f"<li>{s} {A(q, 'min-width:46mm')}? <span class='small'>Answer: <b>{a}</b> · (2) ____ (3) ____</span></li>" for s, q, a in mine)
    tq = ["Which city is the capital of Canada? (Ottawa)", "When did the Panama Canal open? (1914)", "Did North America use to be connected to Asia? (Yes, it did.)", "How many time zones does Brazil have? (four)",
          "Which planet is closest to the sun? (Mercury)", "Which ocean is the largest? (the Pacific)"]
    b.page(f"""{sec(6, "Speaking: quiz time", "12 min")}
{sub("A", "Complete the questions for your teacher. Then add two wrong options for each one, so you have three.", "5 min")}
<ol style="line-height:1.45;font-size:8.6pt;margin:0">{ml}</ol>
{sub("B", "Ask your teacher your questions. Then answer your teacher's questions. Who has the higher score?", "5 min")}
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:9pt"><b>You:</b> Which river carries the most water in the world? Is it the Nile, the Amazon or the Mississippi? <b>Teacher:</b> Hmm, that's a good question…</div>
<p class="small" style="margin:.5mm 0">{R("Teacher's questions (give three options): " + " · ".join(tq)) if T else "Use the phrases from page 6 when a question is difficult!"}</p>
{sub("C", "Which question was the most difficult? Write one more question for your teacher.", "2 min")}""",
    27, """<ol><li>Facts: Brazil has the largest population in South America; the Amazon carries more water than any other river; Brasília became the capital in 1960; the skin is the largest organ; adults have 206 bones; the first human heart transplant was in 1967 (South Africa); the Panama Canal opened in 1914; Brazil has four time zones.</li>
<li>Mix the position of the correct answer when you ask; use the thinking-time phrases yourself.</li></ol>""")

    # Page 8
    pc = [("A2 Unit 44", "I can explain how to solve a problem and why a solution works."), ("A2 Unit 45", "I can describe a process with the present simple passive."),
          ("A2 Unit 46", "I can use food phrasal verbs with the correct word order."), ("A2 Unit 47", "I can ask correct questions in different tenses.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("How many players you need for a basketball team?", "How many players do you need…? (5 on the court)"), ("Who did run the fastest 100-meter race ever?", "Who ran…? (Usain Bolt)"),
          ("Where would you see a goalball match?", "✓ (at the Paralympics)"), ("Which three countries hosted the 2026 World Cup?", "✓ (the US, Mexico, Canada)"),
          ("How many players a soccer team has on the field?", "How many players does a soccer team have…? (11)"), ("Did polo used to be an Olympic sport?", "Did polo use to be…? (yes, until 1936)")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:40mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Sports quiz. Correct the questions. If a question is correct, write ✓. Then answer them (you can check English websites).</b></p>
<ol style="line-height:1.5;font-size:9pt">{hwl}</ol>
<p style="margin-top:1.5mm"><b>2. My quiz (50–75 words).</b> Write six quiz questions about Brazil or your city in different tenses (present, past, present perfect, future, would). Write the answers too.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Facts: a basketball team has five players on the court; Usain Bolt holds the 100 m world record (9.58 s, 2009); goalball is a Paralympic sport for blind athletes; polo was an Olympic sport until 1936. Next class: the student asks you the quiz.</p>""")

    b.extra("Audio script", f"""
{sub("47.1", "Brain Battle (slow and natural)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in S471)}</p>
{sub("47.2", "Repeat: questions")}
<p>{" · ".join(S472)}</p>
{sub("47.3", "Up or down? (3-second pause)")}
<p>{" · ".join(S473)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 47 - Question time")
