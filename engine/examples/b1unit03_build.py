# Speak! Progress B1 - Unit 03 "King of chess" (all English) - B1 format (2026-11-09)
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Progress"
setup(band="B1 · UNIT 03", audio_json="audio_b1-unit-03.json", img_dir="img")


_r = json.load(open("roteiro.json"))["units"]["b1-unit-03"]
ART = [x.split(": ", 1)[1] for x in _r["03.1 Mequinho: Brazil's king of chess"].split("\n")]
NUM = {"nineteen fifty-two": "1952", "January twenty-third, 1952": "January 23, 1952", "nineteen seventy-two": "1972", "nineteen seventy-three": "1973", "nineteen seventy-six": "1976",
       "nineteen seventy-eight": "1978", "nineteen seventy-nine": "1979", "nineteen seventies": "1970s", "nineteen eighties": "1980s", "nineteen ninety-one": "1991",
       "nineteen seventy": "1970", "two thousand two": "2002", "two thousand four": "2004", "Formula One": "Formula 1", "the age of thirteen": "the age of 13"}
def _num(t):
    for k, v in NUM.items():
        t = t.replace(k, v)
    return t
PARAS = [_num(p) for p in ART[1:]]
S032 = [x.split(": ", 1)[1] for x in _r["03.2 Repeat: used to"].split("\n")]


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
    cover = cover_html(T, "LEVEL B1 · UNIT 03", "King of chess", "A Brazilian sports legend · <b>present simple, past simple, present perfect, used to</b>",
                       [("YOU CAN", "understand a profile of a sports star and talk about how your life has changed"),
                        ("LANGUAGE", "He became… in 1972. · Brazil has produced… · People used to… · Did you use to…?"),
                        ("PRONUNCIATION", "used to /ˈjuːstə/ in connected speech")])
    kw = [("a person you compete against in a game or contest", "an opponent"), ("concentration", "focus"),
          ("a player with the highest level of skill at chess", "a grandmaster"), ("nervous or not sure about doing something", "hesitant"),
          ("a young person with an exceptional talent", "a prodigy"), ("energetic interest in an activity", "enthusiasm"),
          ("worried, unhappy or angry", "upset"), ("to become a member of a team or club", "join")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:22mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Warm-up: sports and talent", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 58, 38)}<div style="flex:1">
{sub("A", "Discuss with your teacher.", "3 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0"><li>Which sports do you enjoy playing or watching? Why?</li><li>Is chess a sport? Why or why not?</li><li>Who is the greatest Brazilian sportsperson ever?</li></ol></div></div>
{sub("B", "Key words. Write the words from the box next to the definitions.", "3 min")}
<div class="bank">enthusiasm · focus · a grandmaster · hesitant · join · an opponent · a prodigy · upset</div>
<div style="font-size:8.8pt">{twocol(kwl, 4)}</div>
{sub("C", "Tell your teacher about a talented person you know. Use three words from B.", "2 min")}""",
    25, """<ol><li>A: accept any answer to 2; chess is recognized as a sport by the International Olympic Committee, but it is not in the Olympic Games. Don't give the answer to 3 yet: the reading may surprise the student.</li>
<li>B: <i>upset</i> is a false friend for many students; it is about feelings, not about being "turned upside down".</li></ol>""", cover=cover)

    b.extra("Lesson overview · 60 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Discussion · key words: opponent, prodigy, grandmaster…</td><td>1</td></tr>
<tr><td>2 Reading</td><td>12 min</td><td>Profile: Mequinho, Brazil's king of chess (skim, scan, infer)</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>8 min</td><td>Tense review: present simple, past simple, present perfect, used to</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Past and present (study at home)</td><td>4</td></tr>
<tr><td>4 Vocabulary lab + pronunciation</td><td>8 min</td><td>Dependent prepositions · words from context · sports verbs · used to</td><td>5</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Danny's message about Bruno · then and now</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Functional language · long turn: a hobby in my life · talking point</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>4 min</td><td>Can-do · language notes · writing homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY AND THE FACTS</h4>The Linguahouse article is about a five-year-old Irish chess player; we replaced it with a profile of <b>Henrique Mecking (Mequinho)</b>, Brazil's first grandmaster, read by the Host (Studio-O). Facts checked in the English Wikipedia article "Henrique Mecking" (born January 23, 1952, in Santa Cruz do Sul; national champion at 13; grandmaster in 1972; Interzonal wins in Petrópolis 1973 and Manila 1976; world no. 3 in 1978 behind Karpov and Korchnoi; myasthenia gravis, withdrew from the 1979 Rio Interzonal, no chess in the 1980s; credits his Catholic faith; returned in 1991; Olympiads 2002 and 2004; drew with Fischer, Buenos Aires 1970) and chess.com. In the Practice, Danny writes about his roommate Bruno, a chess fan (B1 Unit 02).</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students use the present perfect with finished time (<i>I have been to Rio last year</i>), say <i>I use to</i> in the affirmative, confuse <i>used to</i> and <i>be used to</i>, and use the wrong sports verbs (<i>practice soccer, win someone, make sport</i>).</div>
<div class="box"><h4>AUDIO</h4>Track 03.1 Mequinho: Brazil's king of chess (natural and slow; listen and read) · Track 03.2 Repeat: used to</div>""")

    # Page 2 - Reading
    hd = [("A difficult time", "4"), ("A young star", "2"), ("Back to the board", "5"), ("A surprising name for Brazil", "1"), ("Among the best in the world", "3")]
    hdl = " &nbsp; ".join(f"<b>{chr(97+i)}</b> {h} {A(n, 'min-width:5mm')}" for i, (h, n) in enumerate(hd))
    fi = [("How old was he when he first won the Brazilian championship?", "13"), ("Who did he draw a game against in 1970?", "Bobby Fischer"),
          ("What happened in 1972?", "He became the first Brazilian grandmaster."), ("Who were the only better players in 1978?", "Karpov and Korchnoi"),
          ("What did he do in the 1980s?", "He didn't play chess."), ("When did he come back to chess?", "In 1991.")]
    fil = [f'<li value="{i+1}">{q} {A(a, "min-width:20mm")}</li>' for i, (q, a) in enumerate(fi)]
    art = "".join(f'<p style="margin:0 0 1mm"><b style="color:#176074">{i+1}</b> {p}</p>' for i, p in enumerate(PARAS))
    b.page(f"""{sec(2, "Reading: Brazil's king of chess", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div class="box" style="flex:1;margin:0;font-size:8.3pt;line-height:1.36;column-count:2;column-gap:4mm"><b style="font-size:9.5pt">Mequinho: Brazil's king of chess</b><br>{art}</div></div>
{audiocard(["03.1 · NATURAL", "03.1 · SLOW"])}
{sub("A", "Skim the profile in two minutes. Match the headings to paragraphs 1–5.", "2 min")}
<p style="margin:.3mm 0;font-size:8.8pt;line-height:1.7">{hdl}</p>
{sub("B", "Scan for the information.", "4 min")}
<div style="font-size:8.6pt">{twocol(fil, 3)}</div>
{sub("C", "Think about it. Discuss with your teacher.", "4 min")}
<ol style="line-height:1.4;font-size:8.8pt;margin:0"><li>Why is a great Brazilian chess player a surprise, according to the writer? {R("Brazil is famous for other sports: soccer, volleyball and Formula 1.") if T else ""}</li>
<li>He never became world champion. Why do you think many Brazilians still call him "the king of chess"? {R("Personal: the first Brazilian grandmaster, no. 3 in the world, and he came back after a terrible illness.") if T else ""}</li></ol>
<div class="box sand" style="margin-top:1mm"><h4>NOTICE: USEFUL CHUNKS</h4><i>Not many people know that… · at the age of 13 · he even drew a game against… · behind only… · But then everything changed.</i></div>""",
    25, """<ol><li>A: set a strict time limit so the student reads for gist, not every word. Then the student can listen and read (03.1) or read again in silence for B.</li>
<li>C: accept any opinion supported by the text. Myasthenia gravis is a long-term disease that makes the muscles weak; keep the discussion light.</li></ol>""")

    # Page 3 - Language focus
    tn = ["present simple", "past simple", "present perfect", "used to"]
    ex = [("Brazil is famous for soccer, volleyball and Formula 1.", "present simple", "a state now"), ("In 1972, he became the first Brazilian grandmaster.", "past simple", "a finished event, known time"),
          ("The country has produced one of the best players of the 1970s.", "present perfect", "a result up to now, no time"), ("People used to compare him to Fischer.", "used to", "a past habit, not true now"),
          ("He has never become world champion.", "present perfect", "an experience up to now")]
    exl = "".join(f"<li><i>\"{e}\"</i><br>{ch(tn, t)} {R('(' + w + ')') if T else ''}</li>" for e, t, w in ex)
    b.page(f"""{sec(3, "Language focus: past and present", "8 min")}
{sub("A", "Read the sentences from the profile. Which tense is it? Choose.", "4 min")}
<ol style="line-height:1.5;font-size:8.9pt;margin:0">{exl}</ol>
{sub("B", "Used to. Complete the negative and the question.", "2 min")}
<p style="margin:.5mm 0;line-height:1.8">I {A("didn't use to", "min-width:22mm")} like chess, but now I love it. &nbsp;·&nbsp; {A("Did", "min-width:9mm")} you {A("use to", "min-width:12mm")} play any sports?</p>
{sub("C", "Past simple or used to? Choose.", "2 min")}
<ol style="line-height:1.7;font-size:9pt;margin:0"><li>In 1970, he {ch(["drew", "used to draw"], "drew")} a game against Fischer. (one event)</li><li>As a child, I {ch(["used to play", "have played"], "used to play")} soccer every day.</li></ol>
<div class="box sand"><h4>RULE</h4><b>present simple</b> → routines and states now · <b>past simple</b> → finished events at a known time (<i>in 1972, last year, ago</i>) · <b>present perfect</b> → experiences and results up to now, no time (<i>ever, never, just, since</i>) · <b>used to</b> + infinitive → past habits and states that are not true now; negative <i>didn't use to</i>, question <i>Did… use to…?</i> More on the next page: <b>Grammar reference</b>.</div>""",
    24, """<ol><li>A: ask why each tense is used; the explanations in red help. Elicit more examples from the student's life.</li>
<li>C: <i>used to</i> is never for a single event or a number of times (<i>I went to France five times</i>, not <i>I used to go… five times</i>).</li></ol>""")

    grammar_ref.past_present_review(b)

    # Page 5 - Vocabulary lab
    pr = [("Mequinho was obsessed", "with", "chess as a teenager."), ("Brazil is often associated", "with", "soccer and samba."), ("Are you involved", "in", "any clubs or teams?"),
          ("Ana was hesitant", "about", "joining a gym."), ("Danny was upset", "about", "losing the game."), ("Rio de Janeiro is famous", "for", "its beaches."),
          ("Are you good", "at", "chess?"), ("I'm not interested", "in", "Formula 1.")]
    prl = [f'<li value="{i+1}">{a} {A(p, "min-width:11mm")} {e}</li>' for i, (a, p, e) in enumerate(pr)]
    cx = [("a game with no winner (paragraph 2)", "drew"), ("became sick (paragraph 4)", "became ill"), ("religious belief (paragraph 5)", "faith"), ("get better (paragraph 5)", "improve")]
    cxl = " &nbsp;·&nbsp; ".join(f"{d} {A(w, 'min-width:16mm')}" for d, w in cx)
    b.page(f"""{sec(4, "Vocabulary lab: words that go together", "4 min")}
{sub("A", "Dependent prepositions. Complete with the words in the box.", "2 min")}
<div class="bank">about · about · at · for · in · in · with · with</div>
<div style="font-size:8.6pt">{twocol(prl, 4)}</div>
{sub("B", "Meaning from context. Find words in the profile that mean…", "2 min")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.8">{cxl}</p>
<div class="box sand"><h4>WATCH OUT: SPORTS VERBS AND WORD CHOICE</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>I practice soccer on weekends.</td><td><b>I play soccer on weekends.</b></td><td><i>play</i> + ball games and chess; <i>practice</i> = train to improve.</td></tr>
<tr><td>He won his opponent.</td><td><b>He beat his opponent.</b></td><td>you <i>win</i> a game; you <i>beat</i> a person.</td></tr>
<tr><td>I make sport three times a week.</td><td><b>I work out / exercise three times a week.</b></td><td><i>make</i> doesn't go with sport.</td></tr>
<tr><td>I'm used to play chess when I was a kid.</td><td><b>I used to play chess…</b></td><td><i>be used to</i> + -ing = be accustomed to.</td></tr></table></div>
{sec(5, "Pronunciation lab: used to", "4 min")}
<p class="small" style="margin:.3mm 0"><b>used to</b> and <b>use to</b> sound the same: /ˈjuːstə/ – with an /s/ sound, not /z/, and a weak <i>to</i>. Compare: <i>I <b>use</b> /juːz/ my phone.</i> In a soccer game with no winner, Americans say <i>a tie</i>; in chess, <i>a draw</i>.</p>
{audiocard(["03.2"])}
{sub("A", "Listen and repeat. Then ask your teacher three questions with Did you use to…?", "4 min", "03.2")}
{twocol([f'<li value="{i+1}">{s}</li>' for i, s in enumerate(S032)], 4)}""",
    24, """<ol><li>A: also <i>good at, bad at, keen on, proud of</i>. B: <i>drew</i> is the past of <i>draw</i> (= finish a game with no winner).</li>
<li>Pronunciation: students often say /juːzd tuː/. Drill the chunk /ˈjuːstə/ as one word.</li></ol>""")

    # Page 6 - Practice
    gp = [("play", "has played / has been playing"), ("play", "plays"), ("train", "used to train"), ("stop", "stopped"), ("win", "won"), ("never / beat", "have never beaten"), ("beat", "beat"), ("not / like", "didn't use to like"), ("think", "think")]
    g = [A(a, "min-width:26mm") + f" ({v})" for v, a in gp]
    tn2 = ["something you used to do, but you don't do now", "something you didn't use to like, but you like now", "something you have done this year", "something you do every week"]
    b.page(f"""{sec(6, "Practice", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Danny writes to Ana about his roommate. Complete with the present simple, past simple, present perfect or used to.", "5 min")}</div>{img('C', 30, 20)}</div>
<div class="box" style="line-height:1.9;font-size:9pt">Hi Ana! Guess what? My roommate Bruno is obsessed with chess. He {g[0]} since he was six, and he {g[1]} online every night. When he was a teenager, he {g[2]} with a coach every Saturday, but he {g[3]} when he started college. Last year he {g[4]} a tournament in Porto Alegre. I {g[5]} him – yesterday he {g[6]} me in ten minutes! I {g[7]} chess, but now I {g[8]} it's fun. Do you play?</div>
{sub("B", "Then and now. Write true sentences about you. Then tell your teacher.", "3 min")}
<ol style="line-height:1.35;font-size:8.9pt;margin:0">{"".join(f"<li>{t}<div class='wline'></div></li>" for t in tn2)}</ol>""",
    22, """<ol><li>A: in 1 both forms are correct (since + a point in time). In 7, <i>beat</i> is the past simple too (beat – beat – beaten).</li>
<li>B: ask follow-up questions in different tenses: <i>Why did you stop? When did you start liking it?</i></li></ol>""")

    # Page 7 - Speaking
    b.page(f"""{sec(7, "Speaking: then and now", "12 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>talk about the past</th><th>talk about changes</th><th>give an opinion</th><th>agree or disagree</th></tr>
<tr><td><i>When I was younger, I used to… · Back then… · I'll never forget…</i></td><td><i>These days, I… · Over the years, I've… · It all changed when…</i></td><td><i>In my opinion… · I'd say… · If you ask me…</i></td><td><i>I see your point, but… · I'm not so sure. · Exactly!</i></td></tr></table></div>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("A", "Long turn. Prepare for one minute, then talk for two minutes about a sport or hobby in your life.", "6 min")}
<ul style="line-height:1.45;font-size:8.9pt;margin:0"><li>when and how you started</li><li>what you used to do (where, how often, with whom)</li><li>what you have achieved or learned</li><li>what is different now, and why</li></ul></div>{img('D', 32, 24)}</div>
{sub("B", "Talking point. Discuss with your teacher.", "6 min")}
<ol style="line-height:1.5;font-size:8.9pt;margin:0"><li>Who is Brazil's greatest sportsman or sportswoman? Why?</li><li>Are there any young sporting talents in Brazil right now?</li><li>Is it a good idea for children to compete at a very young age? Why or why not?</li><li>Mequinho stopped playing for more than ten years. What helps people come back after a difficult time?</li></ol>""",
    28, """<ol><li>A: don't interrupt; note mistakes for the error log (page 8), especially past simple vs present perfect. Fluency option (3-2-1): the same talk in 2 minutes, then in 1 minute.</li>
<li>B: give your own opinions and disagree sometimes, so the student uses the language in the box. Don't present uncertain facts about athletes as true; ask the student to explain instead.</li></ol>""")

    # Page 8 - Wrap-up
    pc = ["I can understand a profile of a sports star (gist, details, opinions).", "I can choose between the present simple, past simple, present perfect and <i>used to</i>.",
          "I can talk about how my life and my hobbies have changed."]
    pcr = "".join(f"<tr><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for s in pc)
    b.page(f"""{sec(8, "Wrap-up and homework", "4 min")}
{sub("A", "Can-do check", "1 min")}
<table class="ck" style="font-size:8.6pt"><tr><th>In English…</th><th style="width:16mm">Easy!</th><th style="width:16mm">Sometimes</th><th style="width:16mm">Not yet</th></tr>{pcr}</table>
{sub("B", "My language notes. Write three corrections from today's class.", "2 min")}
<div style="display:flex;gap:5mm;font-size:8.6pt"><div style="flex:1"><b>I said…</b>{lines(3)}</div><div style="flex:1"><b>Better:</b>{lines(3)}</div></div>
{sub("C", "Homework: writing (100–150 words)", "1 min")}
<p style="margin:.3mm 0"><b>Then and now.</b> Write about how your life has changed in the last few years. Read Danny's model first.</p>
<div class="box" style="font-size:8.6pt;line-height:1.4;margin:.5mm 0"><i>Two years ago, my life was very different. I lived with my mom in Chicago, and I used to spend hours playing video games. I didn't use to read at all. Last year, I worked at a supermarket to save money for my gap year. Now I live in a hostel in São Paulo, and I've made friends from all over Brazil. I've started reading again, and I've learned some Portuguese. I still play video games sometimes, but these days I usually prefer to go out and explore the city.</i></div>
<p class="small" style="margin:.3mm 0">Checklist: ☐ two things you used to do &nbsp;☐ two finished events with a time (past simple) &nbsp;☐ two experiences or results (present perfect) &nbsp;☐ your life now (present simple) &nbsp;☐ 100–150 words</p>
{lines(7)}""",
    30, """<ol><li>B (error log): during the lesson, note 3–5 real mistakes. Here, the student writes what they said and the better version; guide them to self-correct first.</li>
<li>C: when you correct, underline each verb and ask the student to say which tense it is and why.</li></ol>""")

    b.extra("Audio script", f"""
{sub("03.1", "Mequinho: Brazil's king of chess (natural and slow)")}
<p style="line-height:1.4;font-size:9pt"><i>The Host reads the profile on page 2.</i></p>
{sub("03.2", "Repeat: used to")}
<p>{" · ".join(S032)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 03 - King of chess")
