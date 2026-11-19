# Speak! Progress B1 - Unit 03 "King of chess" (all English) - lean B1 format (rebuilt 2026-11-19)
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Progress"
import lean
from lean import talk
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

    # 1 Warm-up
    cover = cover_html(T, "LEVEL B1 · UNIT 03", "King of chess", "A Brazilian sports legend · <b>present simple, past simple, present perfect, used to</b>",
                       [("YOU CAN", "understand a profile of a sports star and talk about how your life has changed"),
                        ("LANGUAGE", "He became… in 1972. · Brazil has produced… · People used to… · Did you use to…?"),
                        ("PRONUNCIATION", "used to /ˈjuːstə/ in connected speech")])
    kw = [("a person you compete against in a game or contest", "an opponent"), ("a player with the highest level of skill at chess", "a grandmaster"),
          ("nervous or not sure about doing something", "hesitant"), ("a young person with an exceptional talent", "a prodigy"),
          ("energetic interest in an activity", "enthusiasm"), ("worried, unhappy or angry", "upset")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:22mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Warm-up: sports and talent", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["Which sports do you enjoy playing or watching? Why?", "Is chess a sport? Why or why not?", "Who is the greatest Brazilian sportsperson ever?"], "START TALKING")}</div></div>
{sub("A", "Key words. Write the words from the box next to the definitions.", "3 min")}
<div class="bank">enthusiasm · a grandmaster · hesitant · an opponent · a prodigy · upset</div>
<div style="font-size:8.8pt">{twocol(kwl, 3)}</div>
{talk(["Do you know a prodigy in sports, music or school? Tell me about them.", "When did you last feel hesitant or upset about a game or a competition?"], "USE THE WORDS")}""",
    26, """<ol><li>Top box (4 minutes): chess is recognized as a sport by the International Olympic Committee, but it is not in the Olympic Games. Don't answer question 3 yet: the reading may surprise the student.</li>
<li>A: <i>upset</i> is about feelings, not about being "turned upside down".</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Profile of Mequinho: headings · scan for facts · Talk about it", "Past and present: present simple, past simple, present perfect, used to",
                      "Which tense? · used to · Use it (oral)", "Functional language · used to (03.2) · long turn: a hobby in my life",
                      "Danny's message about Bruno · prepositions · word choice · writing", "Reading"),
        "The Linguahouse article is about a five-year-old Irish chess player; we replaced it with a profile of <b>Henrique Mecking (Mequinho)</b>, Brazil's first grandmaster, read by the Host (Studio-O). Facts checked in the English Wikipedia article \"Henrique Mecking\" (born January 23, 1952, in Santa Cruz do Sul; national champion at 13; grandmaster in 1972; Interzonal wins in Petrópolis 1973 and Manila 1976; world no. 3 in 1978 behind Karpov and Korchnoi; myasthenia gravis, withdrew from the 1979 Rio Interzonal, no chess in the 1980s; credits his Catholic faith; returned in 1991; Olympiads 2002 and 2004; drew with Fischer, Buenos Aires 1970) and chess.com. In the homework, Danny writes about his roommate Bruno, a chess fan (B1 Unit 02).",
        "Students use the present perfect with finished time (<i>I have been to Rio last year</i>), say <i>I use to</i> in the affirmative, confuse <i>used to</i> and <i>be used to</i>, and use the wrong sports verbs (<i>practice soccer, win someone, make sport</i>).",
        "Track 03.1 Mequinho: Brazil's king of chess (natural and slow; listen and read) · Track 03.2 Repeat: used to"))

    # 2 Reading
    hd = [("A difficult time", "4"), ("A young star", "2"), ("Back to the board", "5"), ("A surprising name for Brazil", "1"), ("Among the best in the world", "3")]
    hdl = " &nbsp; ".join(f"<b>{chr(97+i)}</b> {h} {A(n, 'min-width:5mm')}" for i, (h, n) in enumerate(hd))
    fi = [("How old was he when he first won the Brazilian championship?", "13"), ("What happened in 1972?", "the first Brazilian grandmaster"),
          ("Who were the only better players in 1978?", "Karpov and Korchnoi"), ("When did he come back to chess?", "in 1991")]
    fil = [f'<li value="{i+1}">{q} {A(a, "min-width:20mm")}</li>' for i, (q, a) in enumerate(fi)]
    art = "".join(f'<p style="margin:0 0 1mm"><b style="color:#176074">{i+1}</b> {p}</p>' for i, p in enumerate(PARAS))
    b.page(f"""{sec(2, "Reading: Brazil's king of chess", "12 min")}
<div class="box" style="margin:0;font-size:8.2pt;line-height:1.34;column-count:2;column-gap:4mm"><b style="font-size:9.5pt">Mequinho: Brazil's king of chess</b><br>{art}</div>
{audiocard(["03.1 · NATURAL", "03.1 · SLOW"])}
{sub("A", "Skim the profile in two minutes. Match the headings to paragraphs 1–5.", "2 min")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.6">{hdl}</p>
{sub("B", "Scan for the information.", "3 min")}
<div style="font-size:8.6pt">{twocol(fil, 2)}</div>
{talk(["Why is a great Brazilian chess player a surprise, according to the writer?", "He never became world champion. Why do many Brazilians still call him &ldquo;the king of chess&rdquo;?", "What helps people come back after a difficult time?"])}""",
    24, """<ol><li>A–B: 6 minutes. Set a strict time for A so the student reads for gist. The student can listen and read (03.1).</li>
<li>Talk about it: 6 minutes. 1: Brazil is famous for soccer, volleyball and Formula 1. 2: personal (first Brazilian grandmaster, world no. 3, came back after a serious illness). Myasthenia gravis makes the muscles weak; keep it light.</li></ol>""")

    # 3 Grammar reference
    lean.grammar_in_class(b, grammar_ref.past_present_review)

    # 4 Practice
    tn = ["present simple", "past simple", "present perfect", "used to"]
    ex = [("Brazil is famous for soccer, volleyball and Formula 1.", "present simple"), ("In 1972, he became the first Brazilian grandmaster.", "past simple"),
          ("The country has produced one of the best players of the 1970s.", "present perfect"), ("People used to compare him to Fischer.", "used to")]
    exl = "".join(f"<li><i>\"{e}\"</i><br>{ch(tn, t)}</li>" for e, t in ex)
    use = ["Tell me something you used to do as a child.", "Tell me something you didn't use to like, but you like now.", "Ask me: <i>Did you use to…?</i> (three questions)",
           "Tell me something you've done this year, and when you did it.", "Tell me about a sport or hobby you do every week."]
    b.page(f"""{sec(4, "Practice: past and present", "10 min")}
{sub("A", "Read the sentences from the profile. Which tense is it? Choose.", "3 min")}
<ol style="line-height:1.5;font-size:8.9pt;margin:0">{exl}</ol>
{sub("B", "Used to. Complete the negative and the question.", "1 min")}
<p style="margin:.5mm 0;line-height:1.8">I {A("didn't use to", "min-width:22mm")} like chess, but now I love it. &nbsp;·&nbsp; {A("Did", "min-width:9mm")} you {A("use to", "min-width:12mm")} play any sports?</p>
<div class="box sand"><h4>RULE</h4><b>present simple</b> → routines and states now · <b>past simple</b> → finished events at a known time · <b>present perfect</b> → experiences and results up to now, no time · <b>used to</b> + infinitive → past habits and states that are not true now. See the <b>Grammar reference</b> on page 3.</div>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    24, """<ol><li>A–B: 4 minutes. Ask why each tense is used. <i>Used to</i> is never for one event or a number of times (<i>I went to France five times</i>).</li>
<li>Use it: 6 minutes, all oral. Ask follow-ups in different tenses: <i>Why did you stop? When did you start?</i></li></ol>""")

    # 5 Speaking
    b.page(f"""{sec(5, "Speaking: then and now", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>talk about the past</th><th>talk about changes</th><th>give an opinion</th><th>agree or disagree</th></tr>
<tr><td><i>When I was younger, I used to… · Back then… · I'll never forget…</i></td><td><i>These days, I… · Over the years, I've… · It all changed when…</i></td><td><i>In my opinion… · I'd say… · If you ask me…</i></td><td><i>I see your point, but… · I'm not so sure. · Exactly!</i></td></tr></table></div>
{audiocard(["03.2"])}
{sub("A", "Listen and repeat. used to sounds like /ˈjuːstə/, with an /s/ sound and a weak to.", "4 min", "03.2")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.55">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {s}" for i, s in enumerate(S032))}</p>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("B", "Long turn. Prepare for one minute, then talk for two minutes about a sport or hobby in your life.", "8 min")}
<ul style="line-height:1.45;font-size:8.9pt;margin:0"><li>when and how you started</li><li>what you used to do (where, how often, with whom)</li><li>what you have achieved or learned</li><li>what is different now, and why</li></ul></div>{img('D', 32, 24)}</div>
{talk(["Is it a good idea for children to compete at a very young age? Why?", "Who is Brazil's greatest sportsman or sportswoman? Why?"])}""",
    28, """<ol><li>A: students often say /juːzd tuː/; drill the chunk /ˈjuːstə/ as one word. B: don't interrupt; note mistakes (past simple vs present perfect). Fluency option (3-2-1).</li>
<li>Talk about it: give your own opinions and disagree sometimes. Don't present uncertain facts about athletes as true. Last 3 minutes: wrap-up.</li></ol>""")

    # H Homework
    gp = [("play", "has played / has been playing"), ("train", "used to train"), ("stop", "stopped"), ("win", "won"), ("beat", "beat"), ("not / like", "didn't use to like")]
    g = [A(a, "min-width:24mm") + f" ({v})" for v, a in gp]
    pr = [("Danny was upset", "about", "losing the game."), ("Are you good", "at", "chess?"), ("I'm not interested", "in", "Formula 1.")]
    prl = " &nbsp;·&nbsp; ".join(f"{a} {A(p, 'min-width:10mm')} {e}" for a, p, e in pr)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Danny writes to Ana about his roommate. Complete with the present simple, past simple, present perfect or used to.", "")}</div>{img('C', 28, 18)}</div>
<div class="box" style="line-height:1.8;font-size:8.8pt;margin:.5mm 0">Hi Ana! Guess what? My roommate Bruno is obsessed with chess. He {g[0]} since he was six. When he was a teenager, he {g[1]} with a coach every Saturday, but he {g[2]} when he started college. Last year he {g[3]} a tournament in Porto Alegre. Yesterday he {g[4]} me in ten minutes! I {g[5]} chess, but now I think it's fun. Do you play?</div>
{sub("B", "Complete with the correct preposition.", "")}
<p style="margin:.3mm 0;line-height:1.9;font-size:8.8pt">{prl}</p>
{lean.watch_out([("I practice soccer on weekends.", "I play soccer on weekends.", "<i>play</i> + ball games and chess; <i>practice</i> = train."), ("He won his opponent.", "He beat his opponent.", "you <i>win</i> a game; you <i>beat</i> a person."), ("I'm used to play chess when I was a kid.", "I used to play chess…", "<i>be used to</i> + -ing = be accustomed to.")])}
{lean.writing_task(sub, "Then and now: write about how your life has changed in the last few years.", "Two years ago, my life was very different. I used to…", ["used to", "past simple with a time", "present perfect", "100–150 words"], "I can talk about how my life and my hobbies have changed.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class. In A, 1 has two correct answers; in 5, <i>beat</i> is the past simple too (beat – beat – beaten). When you correct the writing, ask the student which tense each verb is and why.</p>""")

    b.extra("Audio script", f"""
{sub("03.1", "Mequinho: Brazil's king of chess (natural and slow)")}
<p style="line-height:1.4;font-size:9pt"><i>The Host reads the profile on page 2.</i></p>
{sub("03.2", "Repeat: used to")}
<p>{" · ".join(S032)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 03 - King of chess")
