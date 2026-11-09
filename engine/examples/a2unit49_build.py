# Speak! Bridge A2 - Unit 49 "Made in Brazil" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 49", audio_json="audio_a2-unit-49.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["a2-unit-49"]
S491 = [x.split(": ", 1) for x in _r["49.1 Discover Brazil"].split("\n")]
S492 = [x.split(": ", 1)[1] for x in _r["49.2 Repeat: the past passive"].split("\n")]
S493 = [x.split(". ", 1)[1] for x in [y.split(": ", 1)[1] for y in _r["49.3 Is or was?"].split("\n")]]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 49", "Made in Brazil", "Famous places and firsts · <b>the past simple passive</b>",
                       [("YOU CAN", "talk about the history of famous places, buildings and inventions with the past passive"),
                        ("LANGUAGE", "It was built in 1960. · The buildings were designed by Niemeyer. · When was it opened? · Who was it designed by?"),
                        ("PRONUNCIATION", "weak was /wəz/ and were /wər/ · is or was?")])
    qz = [("Christ the Redeemer was inaugurated in", ["1891", "1931", "1971"], "1931"), ("Brasília became the capital in", ["1930", "1960", "1990"], "1960"),
          ("The Maracanã stadium was opened for the World Cup in", ["1950", "1970", "2014"], "1950"), ("Santos-Dumont's plane, the 14-bis, was flown in", ["Rio", "Paris", "New York"], "Paris")]
    qzl = "".join(f"<li>{a} {ch(o, r)}.</li>" for a, o, r in qz)
    b.page(f"""{sec(1, "Warm-up: Brazil quiz", "8 min")}
<div style="display:flex;gap:2mm;margin-bottom:1mm">{img('A', 34, 22)}{img('B', 34, 22)}{img('C', 34, 22)}{img('F', 34, 22)}</div>
{sub("A", "What do you know? Choose the answers. You'll check them in the listening.", "4 min")}
<ol style="line-height:1.7;margin:0">{qzl}</ol>
{sub("B", "Talk about it.", "4 min")}
<ol style="line-height:1.5;margin:0"><li>Which of these places have you visited? Which would you show a visitor from the US?</li><li>What other famous Brazilian places, people or inventions do you know?</li>
<li>Look at the sentences in A. Who did the actions? Is it important?</li></ol>""",
    26, """<ol><li>A: the answers are in the listening; don't confirm yet. Facts: Christ the Redeemer was inaugurated on October 12, 1931; Brasília on April 21, 1960; the Maracanã opened in June 1950; the 14-bis flew in Paris in 1906.</li>
<li>B3: these sentences are passive; the action is more important than who did it.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Brazil quiz</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Paulo practices his "Discover Brazil" webinar with Maya</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>The past simple passive</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>The passive (past simple)</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>4 min</td><td>was and were · is or was?</td><td>5</td></tr>
<tr><td>5 Practice</td><td>9 min</td><td>World firsts and famous works</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>History quiz: ask and answer with the past passive</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>This is an extra Speak! unit (Linguahouse has no lesson here) that extends Unit 45 into the past. Paulo (Neural2-I), a Brazilian travel agent in New York, practices a webinar for American clients, "Discover Brazil", with his colleague Maya (Studio-O). Facts: Christ the Redeemer was inaugurated on October 12, 1931, and was chosen as one of the New Seven Wonders of the World in 2007; it was designed by Brazilian engineer Heitor da Silva Costa with French sculptor Paul Landowski and engineer Albert Caquot. Brasília was built in about 41 months, planned by Lúcio Costa, with most public buildings by Oscar Niemeyer, and inaugurated on April 21, 1960. The Maracanã opened in June 1950 for the World Cup and was rebuilt for the 2014 World Cup. Alberto Santos-Dumont flew the 14-bis at Bagatelle, Paris, in front of a crowd on October 23, 1906; in Brazil he is often called "the father of aviation" (the "first flight" is debated).</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students leave out <i>was/were</i> (<i>It built in 1960</i>), make agreement mistakes (<i>the buildings was</i>), use regular endings for irregular verbs (<i>builded, flied</i>), and keep statement order in questions (<i>When was opened the stadium?</i>).</div>
<div class="box"><h4>AUDIO</h4>Track 49.1 Discover Brazil (slow and natural) · Track 49.2 Repeat: the past passive · Track 49.3 Is or was?</div>""")

    # Page 2
    tf = [("Christ the Redeemer was chosen as a New Wonder of the World in 2007.", "T"), ("The statue was designed only by Brazilians.", "F: by Brazilian and French artists and engineers."),
          ("Brasília was built in less than four years.", "T"), ("All the buildings in Brasília were planned by Lúcio Costa.", "F: Costa planned the city; Niemeyer designed many buildings."),
          ("The Maracanã was rebuilt for the 2014 World Cup.", "T"), ("Before 1960, the capital of Brazil was São Paulo.", "F: it was Rio.")]
    tfl = [f'<li value="{i+1}">{s} <b>T / F</b> {A(a, "min-width:12mm")}</li>' for i, (s, a) in enumerate(tf)]
    op = [("The statue", ["inaugurated", "was inaugurated"], "was inaugurated", "in 1931."), ("In 2007, it", ["was chosen", "chose"], "was chosen", "as a New Wonder of the World."),
          ("It", ["was designed", "designed"], "was designed", "by a team of artists and engineers."), ("The city", ["planned", "was planned"], "was planned", "by Lúcio Costa."),
          ("Many of the buildings", ["was", "were"], "were", "designed by Niemeyer."), ("Why", ["was the capital moved", "the capital was moved"], "was the capital moved", "there?"),
          ("The stadium", ["was opened", "opened was"], "was opened", "in 1950."), ("His plane", ["was flown", "was flied"], "was flown", "in Paris.")]
    opl = [f'<li value="{i+1}">{a} {ch(o, r)} {e}</li>' for i, (a, o, r, e) in enumerate(op)]
    b.page(f"""{sec(2, "Listening: Discover Brazil", "10 min")}
<div style="display:flex;gap:2.5mm;align-items:center"><p style="flex:1;margin:0">Paulo, Ana's brother, works at a travel agency in New York. He's going to give a webinar about Brazil for American clients. He practices with his colleague Maya.</p>{img('E', 28, 18)}</div>
{audiocard(["49.1 · SLOW", "49.1 · NATURAL"])}
{sub("A", "Listen and check your quiz answers on page 1. Then answer true (T) or false (F).", "4 min", "49.1 · SLOW")}
<div style="font-size:8.8pt">{twocol(tfl, 4)}</div>
{sub("B", "Listen again and choose the correct option.", "5 min", "49.1 · NATURAL")}
<div style="font-size:8.8pt">{twocol(opl, 5)}</div>
{sub("C", "Which fact surprised you the most? What would you add to Paulo's webinar?", "1 min")}""",
    22, """<ol><li>A: the capital moved from Rio to Brasília in 1960 to bring development to the center of the country.</li>
<li>B: the student should notice was/were + participle; save the rules for the next page.</li></ol>""")

    # Page 3
    b.page(f"""{sec(3, "Language focus: the past simple passive", "10 min")}
{sub("A", "Compare. Read and choose.", "3 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">1 The city <b>is planned</b> very well. (present) · 2 The city <b>was planned</b> by Lúcio Costa. (past) · 3 Lúcio Costa <b>planned</b> the city. (active)</div>
<ol style="margin:.5mm 0;line-height:1.65"><li>Past passive = {ch(["was / were", "is / are"], "was / were")} + past participle.</li>
<li>In sentence 2, we're more interested in {ch(["the city", "Lúcio Costa"], "the city")}. In sentence 3, we're more interested in {ch(["the city", "Lúcio Costa"], "Lúcio Costa")}.</li></ol>
{sub("B", "Was or were? Why?", "2 min")}
<p style="margin:.5mm 0">The statue {A("was", "min-width:10mm")} inaugurated in 1931. · Many buildings {A("were", "min-width:10mm")} designed by Niemeyer. → {A("was = singular; were = plural", "min-width:44mm")}</p>
{sub("C", "Questions. Put the words in order.", "3 min")}
<ol style="margin:0;line-height:1.7"><li>the stadium / When / opened / was / ? {A("When was the stadium opened?", "min-width:50mm")}</li>
<li>designed / Who / it / was / by / ? {A("Who was it designed by?", "min-width:44mm")}</li>
<li>the capital / Why / moved / was / ? {A("Why was the capital moved?", "min-width:44mm")}</li></ol>
{sub("D", "Write the past participles.", "2 min")}
<p style="margin:.5mm 0;line-height:1.7">build {A("built", "min-width:12mm")} · choose {A("chosen", "min-width:12mm")} · fly {A("flown", "min-width:12mm")} · open {A("opened", "min-width:12mm")} · design {A("designed", "min-width:14mm")} · write {A("written", "min-width:12mm")}</p>
<div class="box sand"><h4>RULE</h4><b>Past passive</b> = was / were + past participle. Use it for history, inventions and events when the thing is more important than the person. Add <b>by</b> + person if it's important. Questions: (question word) + was / were + subject + participle. More on the next page: <b>Grammar reference</b>.</div>""",
    20, """<ol><li>Remind the student of Unit 45 (is / are + participle) and compare.</li>
<li>Drill the questions with falling intonation: <i>When was it ↘ opened?</i></li></ol>""")

    grammar_ref.passive_past(b)

    # Page 5
    iw = ["is", "was", "is", "was", "was", "is"]
    iwl = "".join(f"<li>{A(x, 'min-width:10mm;text-align:center')}</li>" for x in iw)
    b.page(f"""{sub("E", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>Brasília built in 1960.</td><td><b>Brasília was built in 1960.</b></td><td>passive needs was.</td></tr>
<tr><td>The buildings was designed by Niemeyer.</td><td><b>The buildings were designed…</b></td><td>plural: were.</td></tr>
<tr><td>The plane was flied in Paris.</td><td><b>The plane was flown in Paris.</b></td><td>irregular participle.</td></tr>
<tr><td>When was opened the stadium?</td><td><b>When was the stadium opened?</b></td><td>question order.</td></tr>
<tr><td>It was designed for Niemeyer.</td><td><b>It was designed by Niemeyer.</b></td><td>who did it: by.</td></tr>
<tr><td>The statue is inaugurated in 1931.</td><td><b>The statue was inaugurated in 1931.</b></td><td>past: was.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "4 min")}
{audiocard(["49.2", "49.3"])}
{sub("A", "Listen and repeat. was = /wəz/, were = /wər/: short and weak.", "2 min", "49.2")}
{twocol([f'<li value="{i+1}">{s}</li>' for i, s in enumerate(S492)], 4)}
{sub("B", "Listen to six sentences. Do you hear is or was?", "2 min", "49.3")}
<ol style="line-height:1.5;column-count:3;column-gap:5mm">{iwl}</ol>""",
    30, """<ol><li>A: <i>was</i> and <i>were</i> are strong only at the end or in short answers: <i>Yes, it WAS.</i> <i>wasn't</i> /ˈwʌzənt/ is always strong.</li>
<li>B: script: 1 The statue is visited by millions of people. 2 The stadium was opened in 1950. 3 Coffee is grown in Minas Gerais. 4 The city was planned by Lúcio Costa. 5 The plane was flown in Paris. 6 Portuguese is spoken in Brazil.</li></ol>""")

    # Page 6
    pr = [("The telephone", "was invented", "by Alexander Graham Bell in 1876. (invent)"), ("Penicillin", "was discovered", "by Alexander Fleming in 1928. (discover)"),
          ("The Mona Lisa", "was painted", "by Leonardo da Vinci. (paint)"), ("The Eiffel Tower", "was built", "for the 1889 World's Fair in Paris. (build)"),
          ("Brazil's first World Cup", "was won", "in 1958, in Sweden. (win)"), ("Coffee", "was first brought", "to Brazil in the 1700s. (first bring)"),
          ("The first <i>Harry Potter</i> book", "was written", "by J.K. Rowling. (write)"), ("Machu Picchu", "was built", "by the Incas in the 1400s. (build)")]
    prl = "".join(f"<li>{a} {A(v, 'min-width:28mm')} {e}</li>" for a, v, e in pr)
    aq = [("Niemeyer designed many buildings in Brasília.", "Many buildings in Brasília were designed by Niemeyer."), ("They opened the Maracanã in 1950.", "The Maracanã was opened in 1950."),
          ("People chose the statue as a New Wonder in 2007.", "The statue was chosen as a New Wonder in 2007."), ("Did they build Brasília in four years?", "Was Brasília built in four years?")]
    aql = "".join(f"<li>{a}<br>{A(c, 'min-width:80mm')}</li>" for a, c in aq)
    b.page(f"""{sec(5, "Practice", "9 min")}
{sub("A", "World firsts and famous works. Complete with the past passive.", "5 min")}
<ol style="line-height:1.55;font-size:9pt;margin:0">{prl}</ol>
{sub("B", "Rewrite in the passive. Leave out by + person when it isn't important.", "4 min")}
<ol style="line-height:1.4;font-size:8.8pt;margin:0">{aql}</ol>""",
    27, """<ol><li>A: all facts are well known: Bell's telephone patent (1876), Fleming's penicillin (1928), the Eiffel Tower for the 1889 Exposition Universelle, Brazil's first World Cup in Sweden (1958), coffee brought to Brazil in 1727, Machu Picchu built by the Incas in the 15th century.</li>
<li>B: in 2 and 3, <i>they</i> and <i>people</i> aren't important, so we don't add <i>by</i>.</li></ol>""")

    # Page 7
    mine = [("When / the Christ the Redeemer statue / inaugurate?", "When was the Christ the Redeemer statue inaugurated? (1931)"), ("Who / Brasília / plan / by?", "Who was Brasília planned by? (Lúcio Costa)"),
            ("Where / the 14-bis / fly?", "Where was the 14-bis flown? (in Paris)"), ("When / the Maracanã / open?", "When was the Maracanã opened? (1950)")]
    ml = "".join(f"<li>{w}<br>{A(q, 'min-width:80mm')}</li>" for w, q in mine)
    tq = ["Who was the telephone invented by? (Bell)", "When was penicillin discovered? (1928)", "What was the Eiffel Tower built for? (the 1889 World's Fair)", "Where was Brazil's first World Cup won? (in Sweden, 1958)",
          "Who was Machu Picchu built by? (the Incas)"]
    b.page(f"""{sec(6, "Speaking: history quiz", "12 min")}
<div style="display:flex;gap:3mm;align-items:center"><p style="flex:1;margin:0">You and your teacher are going to quiz each other. Use the past passive. Close page 2 and page 6 first!</p>{img('A', 28, 18)}</div>
{sub("A", "Make questions from the prompts. Then ask your teacher.", "4 min")}
<ol style="line-height:1.45;font-size:8.8pt;margin:0">{ml}</ol>
{sub("B", "Answer your teacher's questions. Use full sentences: It was invented by…", "4 min")}
<p class="small" style="margin:0">{R("Teacher's questions: " + " · ".join(tq)) if T else ""}</p>
{sub("C", "Your city. Tell your teacher about a famous place in your city: When was it built? Who was it designed by? Why was it built? Is it still used today?", "4 min")}""",
    22, """<ol><li>A–B: insist on correct question order and full passive answers. If the student doesn't know, they can guess: <i>I think it was invented by…</i></li>
<li>C: the student may not know exact dates; accept "in the 1950s / about 100 years ago".</li></ol>""")

    # Page 8
    pc = [("A2 Unit 46", "I can use food phrasal verbs with the correct word order."), ("A2 Unit 47", "I can ask correct questions in different tenses."),
          ("A2 Unit 48", "I can plan and write a short opinion essay."), ("A2 Unit 49", "I can talk about history with the past simple passive.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Brasília built in less than four years.", "was built"), ("The buildings was designed by Oscar Niemeyer.", "were designed"), ("When was opened the Maracanã?", "When was the Maracanã opened?"),
          ("The statue was chosen as a New Wonder in 2007.", "✓"), ("The 14-bis was flied in Paris.", "was flown"), ("Penicillin discovered by Fleming.", "was discovered")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:36mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Correct the mistakes. If a sentence is correct, write ✓.</b></p>
<ol style="line-height:1.55;font-size:9pt">{hwl}</ol>
<p style="margin-top:1.5mm"><b>2. A famous place in my city (50–75 words).</b> Write about a famous building, monument or place in your city or state. When was it built? Who was it built by? Why? Use at least four past passives.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class: the student presents the place like Paulo's webinar. Unit 50 is Review 5 (Units 41–49), the last unit of A2 Bridge.</p>""")

    b.extra("Audio script", f"""
{sub("49.1", "Discover Brazil (slow and natural)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in S491)}</p>
{sub("49.2", "Repeat: the past passive")}
<p>{" · ".join(S492)}</p>
{sub("49.3", "Is or was? (3-second pause)")}
<p>{" · ".join(S493)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 49 - Made in Brazil")
