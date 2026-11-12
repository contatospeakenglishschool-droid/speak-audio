# Speak! Progress B1 - Unit 05 "On the run" (all English) - B1 format (2026-11-09)
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Progress"
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

    # Page 1 - Warm-up
    cover = cover_html(T, "LEVEL B1 · UNIT 05", "On the run", "A Brazilian ultrarunner · <b>verb patterns: infinitive or -ing</b>",
                       [("YOU CAN", "understand an article about an athlete and talk about challenges, plans and achievements"),
                        ("LANGUAGE", "He managed to set a record. · He kept competing. · She encouraged me to start. · stop running / stop to drink"),
                        ("PRONUNCIATION", "weak <i>to</i> /tə/")])
    kw = [("something difficult that needs a lot of effort or skill", "a challenge"), ("physical damage to the body, for example a broken bone", "an injury"),
          ("the type of land in an area, for example deserts or mountains", "terrain"), ("the ability to continue doing something hard for a long time", "endurance"),
          ("the best result ever in a sport", "a record"), ("to stop trying", "give up"),
          ("a person who trains athletes", "a coach"), ("a running machine at the gym", "a treadmill")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:22mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Warm-up: going the distance", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 58, 38)}<div style="flex:1">
{sub("A", "Discuss with your teacher.", "3 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0"><li>Are you involved in any sports or physical activities? How often do you practice?</li><li>What is the longest distance you have ever walked, run or cycled?</li><li>Why do you think some people run marathons?</li></ol></div></div>
{sub("B", "Key words. Write the words from the box next to the definitions.", "3 min")}
<div class="bank">a challenge · a coach · endurance · give up · an injury · a record · terrain · a treadmill</div>
<div style="font-size:8.8pt">{twocol(kwl, 4)}</div>
{sub("C", "Tell your teacher about a challenge in your life. Use three words from B.", "2 min")}""",
    25, """<ol><li>A: a marathon is 42.195 km (26.2 miles). If the student runs, ask about their races and times.</li>
<li>B: <i>endurance</i> is a key word for the article. <i>Give up</i> is a phrasal verb followed by -ing (<i>give up smoking</i>): it comes back in the Language focus.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 60 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Discussion · key words: challenge, injury, terrain, endurance…</td><td>1</td></tr>
<tr><td>2 Reading</td><td>12 min</td><td>Article: Valmir Nunes, running through the heat (skim, scan, infer)</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>8 min</td><td>Verb patterns: infinitive or -ing</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Infinitive or -ing? (study at home)</td><td>4</td></tr>
<tr><td>4 Vocabulary lab + pronunciation</td><td>8 min</td><td>Words from context · record and race collocations · weak <i>to</i></td><td>5</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Danny's message about his running group · sentences about you</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Functional language · long turn: a challenge · role-play: persuade · talking point</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>4 min</td><td>Can-do · language notes · writing homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY AND THE FACTS</h4>The Linguahouse article (2006) is about the American ultrarunner Dean Karnazes; we replaced it with an article about the Brazilian <b>Valmir Nunes</b>, read by the Host (Studio-O). Facts checked in the English and Portuguese Wikipedia articles "Valmir Nunes": born January 16, 1964; 100 km world champion in 1991; 100 km world record in 1995 (Winschoten, Netherlands, 6:18:09); Spartathlon winner in 2001 (246 km, 23:18:05); Badwater 2007: the first runner under 24 hours (22:51:29) in temperatures of 46 °C, a record that lasted 12 years until Yoshihiko Ishikawa (Japan) ran 21:33:01 in 2019; won a 24-hour treadmill race in Porto Alegre in 2010 (215.6 km, aged 46); published a book about his ultrarunning career in 2010; coaches runners; in 1998 he encouraged Sirlene Pinho to start running competitively, and she won the marathon bronze at the 2007 Pan American Games. In the Practice, Danny joins Bruno's running group (B1 Units 02–04).</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students use <i>for</i> + infinitive for purpose (<i>I run for stay fit</i>), say <i>I want that you come</i>, use the infinitive after prepositions (<i>I'm thinking to run</i>, <i>look forward to see</i>) and confuse <i>stop running</i> with <i>stop to run</i>. <i>Assist a race</i> is a false friend (= <i>watch</i>).</div>
<div class="box"><h4>AUDIO</h4>Track 05.1 Valmir Nunes: running through the heat (natural and slow; listen and read) · Track 05.2 Repeat: weak to</div>""")

    # Page 2 - Reading
    hd = [("A record in the heat", "4"), ("Helping others", "6"), ("What is an ultra?", "2"), ("Still running after 40", "5"), ("A champion of the 1990s", "3")]
    hdl = " &nbsp; ".join(f"<b>{chr(97+i)}</b> {h} {A(n, 'min-width:5mm')}" for i, (h, n) in enumerate(hd))
    fi = [("How are ultras different from conventional marathons?", "They're longer than 42 km, often on unusual terrain; finishing is a victory."),
          ("What did he win in 1991?", "The 100 km world championship."), ("What was special about his race in 2007?", "He was the first to finish Badwater in under 24 hours, in 46 °C."),
          ("How long did his Badwater record last?", "12 years (until 2019)."), ("What two things did he do in 2010?", "He won a 24-hour treadmill race and published a book."),
          ("How did he help Sirlene Pinho?", "He encouraged her to start running competitively.")]
    fil = [f'<li value="{i+1}">{q} {A(a, "min-width:20mm")}</li>' for i, (q, a) in enumerate(fi)]
    art = "".join(f'<p style="margin:0 0 1mm"><b style="color:#176074">{i+1}</b> {p}</p>' for i, p in enumerate(PARAS))
    b.page(f"""{sec(2, "Reading: running through the heat", "12 min")}
<div class="box" style="margin:0;font-size:8.3pt;line-height:1.36;column-count:2;column-gap:4mm"><b style="font-size:9.5pt">Valmir Nunes: running through the heat</b><br>{art}</div>
<div style="display:flex;gap:3mm;align-items:center;margin-top:1mm"><div style="flex:1">{audiocard(["05.1 · NATURAL", "05.1 · SLOW"])}</div>{img('B', 40, 22)}</div>
{sub("A", "Skim the article in two minutes. Match the headings to paragraphs 2–6.", "2 min")}
<p style="margin:.3mm 0;font-size:8.8pt;line-height:1.7">{hdl}</p>
{sub("B", "Scan for the information.", "4 min")}
<div style="font-size:8.6pt">{twocol(fil, 3)}</div>
{sub("C", "Think about it. Discuss with your teacher.", "4 min")}
<ol style="line-height:1.4;font-size:8.8pt;margin:0"><li>Why does the writer say a marathon is "almost a warm-up" for Nunes? {R("His races are much longer: 100 km, 217 km, 246 km, or 24 hours.") if T else ""}</li>
<li>"Victory simply means finishing the race." Do you agree that finishing can be a victory? Why? {R("Personal.") if T else ""}</li></ol>
<div class="box sand" style="margin-top:1mm"><h4>NOTICE: USEFUL CHUNKS</h4><i>If you think… sounds tough, try to imagine… · in the middle of summer · keep going · in just over 23 hours · as he got older · Nine years later, …</i></div>""",
    25, """<ol><li>A: set a strict time limit so the student reads for gist. Then the student can listen and read (05.1) or read again in silence for B. Death Valley is a desert in California, one of the hottest places on Earth.</li>
<li>B: accept short answers. 46 °C is about 115 °F.</li></ol>""")

    # Page 3 - Language focus
    ex = [("he managed", "to set", "set"), ("he didn't stop", "running", "run"), ("he became the first runner", "to finish", "finish"), ("Nunes kept", "competing", "compete"),
          ("he encouraged Sirlene Pinho", "to start", "start"), ("runners who want", "to complete", "complete")]
    exl = "".join(f"<li>…{a} {A(f, 'min-width:18mm')} ({v})…</li>" for a, f, v in ex)
    cat = [("verb + to + infinitive", "manage, want"), ("verb + -ing", "keep, stop (= not do anymore)"), ("verb + object + to + infinitive", "encourage someone")]
    catl = "".join(f"<li>{c}: {A(v, 'min-width:40mm')}</li>" for c, v in cat)
    b.page(f"""{sec(3, "Language focus: infinitive or -ing?", "8 min")}
{sub("A", "Complete the phrases from the article with the correct form of the verb. Check in the text.", "3 min")}
<ol style="line-height:1.7;font-size:8.9pt;margin:0;column-count:2">{exl}</ol>
{sub("B", "Write the first verbs from A in the correct group.", "2 min")}
<ol style="line-height:1.7;font-size:8.9pt;margin:0">{catl}</ol>
{sub("C", "Different meaning. Match the sentences to the meanings.", "3 min")}
<p style="margin:.3mm 0;font-size:8.9pt;line-height:1.7"><b>1</b> He stopped running at the age of 50. {A("b", "min-width:6mm")} &nbsp; <b>2</b> He stopped to drink some water. {A("a", "min-width:6mm")} &nbsp;&nbsp; <b>a</b> He stopped in order to do something else. &nbsp; <b>b</b> He didn't do it anymore.<br>
<b>3</b> I remember running my first race. {A("d", "min-width:6mm")} &nbsp; <b>4</b> Remember to take your water bottle. {A("c", "min-width:6mm")} &nbsp;&nbsp; <b>c</b> Don't forget to do it. &nbsp; <b>d</b> I have a memory of it.</p>
<div class="box sand"><h4>RULE</h4><b>to + infinitive</b> after <i>decide, hope, manage, need, plan, want…</i> and for purpose (<i>I run to stay fit</i>) · <b>-ing</b> after <i>enjoy, give up, keep, finish, avoid…</i> and after prepositions (<i>good at running</i>) · <b>object + to + infinitive</b> after <i>encourage, tell, ask, advise, want</i> · <b>stop, remember, forget, try</b> change meaning. More on the next page: <b>Grammar reference</b>.</div>""",
    24, """<ol><li>A: ask the student to find each phrase in the article first; the form comes from the <b>first</b> verb, not from the meaning.</li>
<li>C: <i>remember doing</i> = the action first, the memory later; <i>remember to do</i> = remember first, then act.</li></ol>""")

    grammar_ref.verb_patterns(b)

    # Page 5 - Vocabulary lab
    cx = [("usual, traditional (paragraph 1)", "conventional"), ("people who take part (paragraph 2)", "participants"), ("success in a competition (paragraph 2)", "victory"),
          ("continue (paragraph 2)", "keep going"), ("a little more than (paragraph 3)", "just over"), ("as a serious competitor (paragraph 6)", "competitively")]
    cxl = [f'<li value="{i+1}">{d} {A(w, "min-width:20mm")}</li>' for i, (d, w) in enumerate(cx)]
    co = [("Nunes", "set", "a world record in 1995."), ("A Japanese runner", "broke", "his Badwater record in 2019."), ("Who", "holds", "the record for the 100 meters?"),
          ("I'd like to", "take part in", "a race next year."), ("I've", "signed up for", "a 10K in December."), ("He was injured, so he", "dropped out of", "the race.")]
    col = [f'<li value="{i+1}">{a} {A(v, "min-width:18mm")} {e}</li>' for i, (a, v, e) in enumerate(co)]
    b.page(f"""{sec(4, "Vocabulary lab: records and races", "4 min")}
{sub("A", "Meaning from context. Find words or phrases in the article that mean…", "2 min")}
<div style="font-size:8.6pt">{twocol(cxl, 3)}</div>
{sub("B", "Collocations. Complete with the words in the box. Use the correct form.", "2 min")}
<div class="bank">break · drop out of · hold · set · sign up for · take part in</div>
<div style="font-size:8.6pt">{twocol(col, 3)}</div>
<div class="box sand"><h4>WATCH OUT: FALSE FRIENDS AND WORD CHOICE</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>I assisted the São Silvestre race on TV.</td><td><b>I watched the São Silvestre race on TV.</b></td><td><i>assist</i> = help.</td></tr>
<tr><td>I'm training to the race.</td><td><b>I'm training for the race.</b></td><td>train <b>for</b> an event.</td></tr>
<tr><td>He made a new record.</td><td><b>He set / broke a new record.</b></td><td><i>set</i> or <i>break</i> a record.</td></tr></table></div>
{sec(5, "Pronunciation lab: weak to", "4 min")}
<p class="small" style="margin:.3mm 0">Before a consonant, <i>to</i> is usually weak: /tə/, not /tuː/. It joins the verb before it: <i>decided_to /dɪˈsaɪdɪdtə/ run · want_to · need_to</i>.</p>
{audiocard(["05.2"])}
{sub("A", "Listen and repeat. Then tell your teacher two things you want to do this year.", "4 min", "05.2")}
<p style="margin:.3mm 0;font-size:8.8pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S052))}</p>""",
    24, """<ol><li>B: <i>set</i> = make a new best result; <i>break</i> = beat the old record; <i>hold</i> = have it now.</li>
<li>Pronunciation: in fast speech, <i>want to</i> often sounds like <i>wanna</i>.</li></ol>""")

    # Page 6 - Practice
    gp = [("join", "to join"), ("go", "going"), ("sign up", "to sign up"), ("eat", "eating"), ("get", "to get"), ("drink", "to drink"), ("tell / stretch", "telling … to stretch"), ("finish", "finishing"), ("finish", "to finish"), ("come", "to come")]
    g = [A(a, "min-width:20mm") + f" ({v})" for v, a in gp]
    mb = ["I've always wanted", "I'd never consider", "I can't stand", "When I was a child, my parents encouraged me", "I need to remember"]
    b.page(f"""{sec(6, "Practice", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Danny writes to Ana. Complete with the correct form of the verbs: to + infinitive or -ing.", "5 min")}</div>{img('C', 30, 20)}</div>
<div class="box" style="line-height:1.95;font-size:9pt">Hi Ana! Guess what? Bruno persuaded me {g[0]} his running group. We meet in Ibirapuera Park, and I really enjoy {g[1]} with them. I've even decided {g[2]} for a 10K race in December! I've given up {g[3]} junk food, and I'm trying {g[4]} to bed earlier. Yesterday I had to stop {g[5]} some water after 5 km – it was so hot! Our coach keeps {g[6]} us before and after. I'll never forget {g[7]} my first 5 km last week. Now I hope {g[8]} the 10K in less than an hour. Do you want {g[9]} and watch? Danny</div>
{sub("B", "Complete the sentences so they are true for you. Then tell your teacher.", "3 min")}
<ol style="line-height:1.35;font-size:8.9pt;margin:0">{"".join(f"<li>{t} …<div class='wline'></div></li>" for t in mb)}</ol>""",
    22, """<ol><li>A: 7 = <i>telling us to stretch</i> (keep + -ing, tell + object + to); 6 = stop in order to drink.</li>
<li>B: check the pattern (<i>consider -ing, encouraged me to…</i>) and ask follow-up questions.</li></ol>""")

    # Page 7 - Speaking
    b.page(f"""{sec(7, "Speaking: challenges", "12 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>achievements</th><th>plans and hopes</th><th>persuade</th><th>hesitate or refuse</th></tr>
<tr><td><i>I managed to… · It took me… · I'll never forget…</i></td><td><i>I'm planning to… · I'd love to… · I hope to…</i></td><td><i>Why don't you…? · You should definitely… · Come on, it'll be fun!</i></td><td><i>I'm not sure I could… · I'd rather not. · Maybe next year.</i></td></tr></table></div>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("A", "Long turn. Prepare for one minute, then talk for two minutes about a challenge in your life (sports, study, work or travel).", "5 min")}
<ul style="line-height:1.45;font-size:8.9pt;margin:0"><li>what you decided to do, and why</li><li>how you prepared</li><li>what was difficult, and how you kept going</li><li>what you managed to do in the end</li></ul></div>{img('D', 32, 24)}</div>
{sub("B", "Role-play. Your teacher wants you to sign up for a 10K race in three months. Listen, ask questions and give reasons. Then change roles: persuade your teacher to try something new.", "4 min")}
<p style="margin:.3mm 0;font-size:8.6pt">{R("Teacher's card: the race is on a Sunday at 7 a.m.; a running group meets twice a week; the coach is free; you can walk part of the race; all money goes to a children's hospital. Use: encourage you to…, you won't regret…, it's worth trying…") if T else ""}</p>
{sub("C", "Talking point. Discuss with your teacher.", "3 min")}
<ol style="line-height:1.5;font-size:8.9pt;margin:0"><li>Is running 200 kilometers healthy, or is it too extreme? Why?</li><li>What other amazing feats of endurance do you know about?</li></ol>""",
    28, """<ol><li>A: don't interrupt; note mistakes for the error log (page 8), especially the verb patterns. Fluency option (3-2-1): the same talk in 2 minutes, then in 1 minute.</li>
<li>B: use the card in red; let the student hesitate first, then answer their questions. Then the student persuades you (a cooking class, a new language, a trip…).</li></ol>""")

    # Page 8 - Wrap-up
    pc = ["I can understand an article about an athlete (gist, details, opinions).", "I can use verbs + infinitive or -ing correctly.",
          "I can talk about challenges, plans and achievements, and persuade someone."]
    pcr = "".join(f"<tr><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for s in pc)
    b.page(f"""{sec(8, "Wrap-up and homework", "4 min")}
{sub("A", "Can-do check", "1 min")}
<table class="ck" style="font-size:8.6pt"><tr><th>In English…</th><th style="width:16mm">Easy!</th><th style="width:16mm">Sometimes</th><th style="width:16mm">Not yet</th></tr>{pcr}</table>
{sub("B", "My language notes. Write three corrections from today's class.", "2 min")}
<div style="display:flex;gap:5mm;font-size:8.6pt"><div style="flex:1"><b>I said…</b>{lines(3)}</div><div style="flex:1"><b>Better:</b>{lines(3)}</div></div>
{sub("C", "Homework: writing (100–150 words)", "1 min")}
<p style="margin:.3mm 0"><b>My challenge.</b> Write about a challenge you set yourself. Read Ana's text first.</p>
<div class="box" style="font-size:8.6pt;line-height:1.4;margin:.5mm 0"><i>Two years ago, I decided to learn to swim properly. I could swim a little, but I always avoided going into deep water. A friend from the hospital encouraged me to join a class, so I signed up for lessons twice a week at 6 a.m. At first, it was really hard. I kept swallowing water, and I almost gave up after the first month. But my teacher told me to relax and to breathe slowly, and it worked. Last summer, I managed to swim one kilometer in the sea for the first time. I'll never forget reaching the beach at the end! Now I'm planning to take part in an open-water race next year.</i></div>
<p class="small" style="margin:.3mm 0">Checklist: ☐ verb + to + infinitive (<i>decide, manage, plan</i>) &nbsp;☐ verb + -ing (<i>avoid, keep, give up</i>) &nbsp;☐ verb + object + to (<i>encourage, tell</i>) &nbsp;☐ past simple for the story &nbsp;☐ 100–150 words</p>
{lines(7)}""",
    30, """<ol><li>B (error log): during the lesson, note 3–5 real mistakes. Here, the student writes what they said and the better version; guide them to self-correct first.</li>
<li>C: when you correct, underline each verb pattern and ask the student to say which group it belongs to.</li></ol>""")

    b.extra("Audio script", f"""
{sub("05.1", "Valmir Nunes: running through the heat (natural and slow)")}
<p style="line-height:1.4;font-size:9pt"><i>The Host reads the article on page 2.</i></p>
{sub("05.2", "Repeat: weak to")}
<p>{" · ".join(S052)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 05 - On the run")
