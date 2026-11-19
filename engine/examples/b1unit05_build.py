# Speak! Progress B1 - Unit 05 "On the run" (all English) - lean B1 format (rebuilt 2026-11-19)
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
setup(band="B1 · UNIT 05", audio_json="audio_b1-unit-05.json", img_dir="img")
_r = json.load(open("roteiro.json"))["units"]["b1-unit-05"]
PARAS = [
    "If you think a marathon sounds tough, try to imagine running 217 kilometers through Death Valley, in California, in the middle of summer. For the Brazilian runner Valmir Nunes, born in 1964, the 42 kilometers of a conventional marathon are almost a warm-up.",
    "Any race longer than a marathon is called an ultramarathon, or an ultra. Many ultras take place on unusual terrain, like deserts and mountains, and runners have to keep going for many hours, sometimes for a whole day and night. For most participants, victory simply means finishing the race.",
    "Nunes became one of the best ultrarunners in the world in the 1990s. In 1991, he won the 100-kilometer world championship. In 1995, in the Netherlands, he managed to set a world record for the distance: 6 hours, 18 minutes and 9 seconds. And in 2001, he won the Spartathlon, a 246-kilometer race in Greece, in just over 23 hours.",
    "His most famous challenge came in 2007, at the Badwater Ultramarathon in Death Valley. Temperatures reached 46 °C, but he didn't stop running, and he became the first runner to finish the race in less than 24 hours. His record of 22 hours, 51 minutes and 29 seconds lasted 12 years, until a Japanese runner managed to break it in 2019.",
    "Nunes kept competing as he got older. In 2010, at the age of 46, he won a 24-hour race on a treadmill in Porto Alegre, running more than 215 kilometers. That same year, he published a book about his experiences as an ultrarunner.",
    "He also coaches runners who want to complete marathons and ultramarathons. In 1998, he encouraged Sirlene Pinho to start running competitively. Nine years later, she won a bronze medal in the marathon at the Pan American Games."]
S052 = [x.split(": ", 1)[1] for x in _r["05.2 Repeat: weak to"].split("\n")]


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
    cover = cover_html(T, "LEVEL B1 · UNIT 05", "On the run", "A Brazilian ultrarunner · <b>verb patterns: infinitive or -ing</b>",
                       [("YOU CAN", "understand an article about an athlete and talk about challenges, plans and achievements"),
                        ("LANGUAGE", "He managed to set a record. · He kept competing. · She encouraged me to start. · stop running / stop to drink"),
                        ("PRONUNCIATION", "weak <i>to</i> /tə/")])
    kw = [("something difficult that needs a lot of effort or skill", "a challenge"), ("physical damage to the body, for example a broken bone", "an injury"),
          ("the ability to continue doing something hard for a long time", "endurance"), ("the best result ever in a sport", "a record"),
          ("to stop trying", "give up"), ("a person who trains athletes", "a coach")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:22mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Warm-up: going the distance", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["Are you involved in any sports or physical activities? How often?", "What's the longest distance you have ever walked, run or cycled?", "Why do you think some people run marathons?"], "START TALKING")}</div></div>
{sub("A", "Key words. Write the words from the box next to the definitions.", "3 min")}
<div class="bank">a challenge · a coach · endurance · give up · an injury · a record</div>
<div style="font-size:8.8pt">{twocol(kwl, 3)}</div>
{talk(["Tell me about a challenge you've had. Did you ever want to give up?", "Have you ever had an injury? What happened?"], "USE THE WORDS")}""",
    26, """<ol><li>Top box (4 minutes): a marathon is 42.195 km (26.2 miles). If the student runs, ask about their races and times.</li>
<li>A: <i>endurance</i> is a key word for the article. <i>Give up</i> + -ing (<i>give up smoking</i>) comes back in the Practice.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Article: Valmir Nunes · headings · scan for facts · Talk about it", "Infinitive or -ing? Verb patterns",
                      "Complete from the article · stop / remember · Use it (oral)", "Functional language · weak to (05.2) · role-play: persuade",
                      "Danny's message about his running group · collocations · word choice · writing", "Reading"),
        "The Linguahouse article (2006) is about the American ultrarunner Dean Karnazes; we replaced it with an article about the Brazilian <b>Valmir Nunes</b>, read by the Host (Studio-O). Facts checked in the English and Portuguese Wikipedia articles \"Valmir Nunes\": born January 16, 1964; 100 km world champion in 1991; 100 km world record in 1995 (Winschoten, Netherlands, 6:18:09); Spartathlon winner in 2001 (246 km, 23:18:05); Badwater 2007: the first runner under 24 hours (22:51:29) in temperatures of 46 °C, a record that lasted 12 years until Yoshihiko Ishikawa (Japan) ran 21:33:01 in 2019; won a 24-hour treadmill race in Porto Alegre in 2010 (215.6 km, aged 46); published a book about his ultrarunning career in 2010; in 1998 he encouraged Sirlene Pinho to start running competitively, and she won the marathon bronze at the 2007 Pan American Games. In the homework, Danny joins Bruno's running group (B1 Units 02–04).",
        "Students use <i>for</i> + infinitive for purpose (<i>I run for stay fit</i>), say <i>I want that you come</i>, use the infinitive after prepositions (<i>I'm thinking to run</i>) and confuse <i>stop running</i> with <i>stop to run</i>. <i>Assist a race</i> is a false friend (= <i>watch</i>).",
        "Track 05.1 Valmir Nunes: running through the heat (natural and slow; listen and read) · Track 05.2 Repeat: weak to"))

    # 2 Reading
    hd = [("A record in the heat", "4"), ("Helping others", "6"), ("What is an ultra?", "2"), ("Still running after 40", "5"), ("A champion of the 1990s", "3")]
    hdl = " &nbsp; ".join(f"<b>{chr(97+i)}</b> {h} {A(n, 'min-width:5mm')}" for i, (h, n) in enumerate(hd))
    fi = [("What did he win in 1991?", "the 100 km world championship"), ("What was special about his race in 2007?", "first under 24 hours at Badwater"),
          ("How long did his Badwater record last?", "12 years"), ("How did he help Sirlene Pinho?", "he encouraged her to run competitively")]
    fil = [f'<li value="{i+1}">{q} {A(a, "min-width:20mm")}</li>' for i, (q, a) in enumerate(fi)]
    art = "".join(f'<p style="margin:0 0 1mm"><b style="color:#176074">{i+1}</b> {p}</p>' for i, p in enumerate(PARAS))
    b.page(f"""{sec(2, "Reading: running through the heat", "12 min")}
<div class="box" style="margin:0;font-size:8.2pt;line-height:1.34;column-count:2;column-gap:4mm"><b style="font-size:9.5pt">Valmir Nunes: running through the heat</b><br>{art}</div>
<div style="display:flex;gap:3mm;align-items:center;margin-top:1mm"><div style="flex:1">{audiocard(["05.1 · NATURAL", "05.1 · SLOW"])}</div>{img('B', 40, 22)}</div>
{sub("A", "Skim the article in two minutes. Match the headings to paragraphs 2–6.", "2 min")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.6">{hdl}</p>
{sub("B", "Scan for the information.", "3 min")}
<div style="font-size:8.6pt">{twocol(fil, 2)}</div>
{talk(["Why does the writer say a marathon is &ldquo;almost a warm-up&rdquo; for Nunes?", "&ldquo;Victory simply means finishing the race.&rdquo; Can finishing be a victory? Why?", "Is running 200 kilometers healthy, or too extreme?"])}""",
    24, """<ol><li>A–B: 6 minutes. Set a strict time for A. The student can listen and read (05.1). Death Valley is a desert in California; 46 °C is about 115 °F.</li>
<li>Talk about it: 6 minutes. 1: his races are much longer (100 km, 217 km, 246 km, 24 hours). 2–3: personal.</li></ol>""")

    # 3 Grammar reference
    lean.grammar_in_class(b, grammar_ref.verb_patterns)

    # 4 Practice
    ex = [("he managed", "to set", "set"), ("he didn't stop", "running", "run"), ("Nunes kept", "competing", "compete"), ("he encouraged Sirlene Pinho", "to start", "start")]
    exl = "".join(f"<li>…{a} {A(f, 'min-width:18mm')} ({v})…</li>" for a, f, v in ex)
    use = ["Tell me something you've decided to do this year.", "Tell me something you've given up, or want to give up.", "Who encouraged you to learn English?",
           "Tell me something you'll never forget doing.", "What do you need to remember to do this week?"]
    b.page(f"""{sec(4, "Practice: infinitive or -ing?", "10 min")}
{sub("A", "Complete the phrases from the article with the correct form of the verb.", "2 min")}
<ol style="line-height:1.7;font-size:8.9pt;margin:0;column-count:2">{exl}</ol>
{sub("B", "Different meaning. Match the sentences to the meanings.", "2 min")}
<p style="margin:.3mm 0;font-size:8.9pt;line-height:1.7"><b>1</b> He stopped running at the age of 50. {A("b", "min-width:6mm")} &nbsp; <b>2</b> He stopped to drink some water. {A("a", "min-width:6mm")}<br><b>a</b> He stopped in order to do something else. &nbsp; <b>b</b> He didn't do it anymore.</p>
<div class="box sand"><h4>RULE</h4><b>to + infinitive</b> after <i>decide, hope, manage, need, want</i> and for purpose · <b>-ing</b> after <i>enjoy, give up, keep, finish, avoid</i> and after prepositions · <b>object + to</b> after <i>encourage, tell, ask</i> · <b>stop, remember, forget, try</b> change meaning. See the <b>Grammar reference</b> on page 3.</div>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    24, """<ol><li>A–B: 4 minutes. The form comes from the <b>first</b> verb, not from the meaning.</li>
<li>Use it: 6 minutes, all oral. Check the pattern after each verb and ask a follow-up.</li></ol>""")

    # 5 Speaking
    b.page(f"""{sec(5, "Speaking: challenges", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>achievements</th><th>plans and hopes</th><th>persuade</th><th>hesitate or refuse</th></tr>
<tr><td><i>I managed to… · It took me… · I'll never forget…</i></td><td><i>I'm planning to… · I'd love to… · I hope to…</i></td><td><i>Why don't you…? · You should definitely… · Come on, it'll be fun!</i></td><td><i>I'm not sure I could… · I'd rather not. · Maybe next year.</i></td></tr></table></div>
{audiocard(["05.2"])}
{sub("A", "Weak to. Listen and repeat: decided_to /tə/ run · want_to · need_to.", "4 min", "05.2")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.55">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S052))}</p>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("B", "Role-play. Your teacher wants you to sign up for a 10K race in three months. Listen, ask questions and give reasons. Then change roles: persuade your teacher to try something new.", "10 min")}
<p style="margin:.3mm 0;font-size:8.6pt">{R("Teacher's card: the race is on a Sunday at 7 a.m.; a running group meets twice a week; the coach is free; you can walk part of the race; all money goes to a children's hospital. Use: encourage you to…, you won't regret…, it's worth trying…") if T else ""}</p></div>{img('D', 32, 24)}</div>
{talk(["What's the biggest challenge you've ever set yourself? Did you manage to do it?", "What's something you'd love to try, but you're not sure you could do?"])}""",
    28, """<ol><li>A: in fast speech, <i>want to</i> often sounds like <i>wanna</i>. B: let the student hesitate first, then answer their questions; then the student persuades you (a cooking class, a new language, a trip…).</li>
<li>Talk about it: note mistakes in verb patterns. Last 3 minutes: wrap-up (two corrections and <i>Can you talk about challenges and plans?</i>).</li></ol>""")

    # H Homework
    gp = [("join", "to join"), ("go", "going"), ("sign up", "to sign up"), ("eat", "eating"), ("drink", "to drink"), ("finish", "to finish")]
    g = [A(a, "min-width:18mm") + f" ({v})" for v, a in gp]
    co = [("A Japanese runner", "broke", "his record in 2019."), ("I've", "signed up for", "a 10K in December."), ("He was injured, so he", "dropped out of", "the race.")]
    col = " &nbsp;·&nbsp; ".join(f"{a} {A(v, 'min-width:18mm')} {e}" for a, v, e in co)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Danny writes to Ana. Complete with to + infinitive or -ing.", "")}</div>{img('C', 28, 18)}</div>
<div class="box" style="line-height:1.8;font-size:8.8pt;margin:.5mm 0">Hi Ana! Bruno persuaded me {g[0]} his running group. We meet in Ibirapuera Park, and I really enjoy {g[1]} with them. I've even decided {g[2]} for a 10K race in December! I've given up {g[3]} junk food. Yesterday I had to stop {g[4]} some water after 5 km – it was so hot! Now I hope {g[5]} the 10K in less than an hour. Danny</div>
{sub("B", "Complete with break, drop out of or sign up for.", "")}
<p style="margin:.3mm 0;line-height:1.9;font-size:8.6pt">{col}</p>
{lean.watch_out([("I assisted the São Silvestre race on TV.", "I watched the São Silvestre race on TV.", "<i>assist</i> = help."), ("I'm training to the race.", "I'm training for the race.", "train <b>for</b> an event."), ("He made a new record.", "He set / broke a new record.", "<i>set</i> or <i>break</i> a record.")])}
{lean.writing_task(sub, "My challenge: write about a challenge you set yourself.", "Two years ago, I decided to… At first, it was hard. I kept…", ["to + infinitive", "-ing", "object + to", "100–150 words"], "I can talk about challenges, plans and achievements.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class (5 = stop in order to drink). When you correct the writing, underline each verb pattern and ask which group it belongs to.</p>""")

    b.extra("Audio script", f"""
{sub("05.1", "Valmir Nunes: running through the heat (natural and slow)")}
<p style="line-height:1.4;font-size:9pt"><i>The Host reads the article on page 2.</i></p>
{sub("05.2", "Repeat: weak to")}
<p>{" · ".join(S052)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 05 - On the run")
