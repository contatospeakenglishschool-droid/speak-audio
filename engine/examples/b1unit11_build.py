# Speak! Progress B1 - Unit 11 "Relationships and dating" (all English) - B1 format (2026-11-09)
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Progress"
setup(band="B1 · UNIT 11", audio_json="audio_b1-unit-11.json", img_dir="img")


_r = json.load(open("roteiro.json"))["units"]["b1-unit-11"]
S111 = [l.replace("nineteen seventy-eight", "1978").replace("nineteen eighty-two", "1982").replace("two hundred", "200") for l in _r["11.1 Gap Year Diaries: a love story"].split("\n")]
S112 = [x.split(": ", 1)[1] for x in _r["11.2 Repeat: contracted had"].split("\n")]


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
    cover = cover_html(T, "LEVEL B1 · UNIT 11", "Relationships and dating", "Love stories · <b>the past perfect</b>",
                       [("YOU CAN", "talk about relationships and dating and tell the story of a couple"),
                        ("LANGUAGE", "ask someone out · split up · make up · a long-distance relationship · He had just moved here."),
                        ("PRONUNCIATION", "contracted had ('d)")])
    kw = [("a romantic meeting, for example dinner or the movies", "a date"), ("when someone asks their partner to marry them", "a proposal"),
          ("the period when two people have promised to get married", "an engagement"), ("the ceremony and party when two people get married", "a wedding"),
          ("a vacation for two people who have just gotten married", "a honeymoon"), ("the same date, every year, after an important event", "an anniversary"),
          ("the end of a romantic relationship", "a break-up"), ("the legal end of a marriage", "a divorce")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:22mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Warm-up: love stories", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 58, 38)}<div style="flex:1">
{sub("A", "Discuss with your teacher.", "3 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0"><li>Look at the photo. How long do you think this couple has been together?</li><li>Do you know a couple with a great love story? How did they meet?</li><li>Is dating easier or harder today than 40 years ago? Why?</li></ol></div></div>
{sub("B", "Key words. Relationship events. Write the words from the box next to the definitions.", "4 min")}
<div class="bank">an anniversary · a break-up · a date · a divorce · an engagement · a honeymoon · a proposal · a wedding</div>
<div style="font-size:8.6pt">{twocol(kwl, 4)}</div>
{sub("C", "Put the events in a typical order. Is there a typical order today?", "1 min")}""",
    25, """<ol><li>A: keep it light and general; the student doesn't need to talk about their own relationships unless they want to.</li>
<li>B: <i>engagement</i> (the period) vs <i>proposal</i> (the question). Pronunciation: <i>ANniVERsary</i>, <i>HONeymoon</i>.</li>
<li>C: possible order: date, proposal, engagement, wedding, honeymoon, anniversary. Accept other ideas.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 60 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Discussion · key words: relationship events</td><td>1</td></tr>
<tr><td>2 Listening</td><td>12 min</td><td>Podcast: Mrs. Lima's love story</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>8 min</td><td>The past perfect · by the time, already, just</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>The past perfect (study at home)</td><td>4</td></tr>
<tr><td>4 Vocabulary lab + pronunciation</td><td>8 min</td><td>People in relationships · dating prepositions · contracted <i>had</i></td><td>5</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Kate's blog: a love story with a happy ending · describing relationships</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Telling a story · long turn: a couple's story · advice role-play · talking point</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>4 min</td><td>Can-do · language notes · writing homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY</h4>The Linguahouse lesson is vocabulary only. Our original listening is a new episode of Danny's podcast <i>Gap Year Diaries</i> (B1 Unit 06). Mrs. Lima, the owner of Danny's hostel (B1 Units 02 and 04), speaks for the first time. She met her husband in 1978 at her father's bakery in São Paulo; he had just moved from Recife. Two years of long-distance relationship (he worked in Manaus), one break-up, a proposal at the bus station in 1982, a wedding the next year, 36 years of marriage, two children, the hostel; he died six years ago. Her story is fictional. At the end we learn that Bruno (single in B1 Unit 09) has asked out Paula, from the running group (B1 Unit 05). Kate's blog (Practice) continues the wedding cake she dropped in B1 Unit 02. The writing model is Bruno's parents' story from B1 Unit 09.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students say <i>married with</i> (married <b>to</b>), <i>date with someone</i> (date someone), use <i>date</i> for a doctor's <i>appointment</i>, and either avoid the past perfect or overuse it for every past action, because spoken Portuguese uses a compound past form very often.</div>
<div class="box"><h4>AUDIO</h4>Track 11.1 Gap Year Diaries: a love story (natural and slow) · Track 11.2 Repeat: contracted had</div>""")

    # Page 2 - Listening
    gist = ["how Mrs. Lima opened her hostel", "how Mrs. Lima met and married her husband", "how young people date with apps"]
    ev = [("He moved to Manaus.", "4"), ("They opened the hostel.", "7"), ("He moved to São Paulo from Recife.", "1"), ("They split up for a while.", "5"),
          ("He asked her out.", "3"), ("He bought about 200 bread rolls.", "2"), ("He proposed at the bus station.", "6")]
    evl = [f'<li value="{i+1}">{A(n, "min-width:6mm")} {s}</li>' for i, (s, n) in enumerate(ev)]
    tf = [("Mrs. Lima fell for him on their first date.", "T"), ("They wrote letters because phone calls were expensive.", "T"),
          ("They split up because he had found another girl.", "F (he had been sick)"), ("She decided to marry him only when he proposed.", "F (she had decided years before)"),
          ("They went to Ouro Preto on their honeymoon.", "T"), ("Bruno went on a date with Paula on Saturday.", "T")]
    tfl = [f'<li value="{i+1}">{s} {A(a, "min-width:9mm")}</li>' for i, (s, a) in enumerate(tf)]
    b.page(f"""{sec(2, "Listening: a love story", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{audiocard(["11.1 · NATURAL", "11.1 · SLOW"])}
{sub("A", "Listen to the podcast at natural speed. What is it mainly about? Choose.", "2 min", "11.1")}
<p style="margin:.3mm 0;font-size:8.9pt">{ch(gist, gist[1])}</p></div>{img('B', 40, 27)}</div>
{sub("B", "Listen again. Number the events in the order they happened (1–7).", "3 min")}
<ol style="line-height:1.5;font-size:8.8pt;margin:0;column-count:2">{"".join(evl)}</ol>
{sub("C", "True or false? Correct the false sentences.", "3 min")}
<div style="font-size:8.6pt">{twocol(tfl, 3)}</div>
{sub("D", "Think about it. Discuss with your teacher.", "4 min")}
<ol style="line-height:1.4;font-size:8.8pt;margin:0"><li>Why does Mrs. Lima still buy one bread roll on every anniversary? {R("It's how they met: he bought one roll every morning. It keeps the memory alive.") if T else ""}</li>
<li>"He'd ironed a shirt." How does Mrs. Lima know that Bruno likes Paula? {R("Bruno never irons anything, so the date was important to him.") if T else ""}</li>
<li>"Never go to bed angry." Is it good advice? Why or why not?</li></ol>
<div class="box sand" style="margin-top:1mm"><h4>NOTICE: USEFUL CHUNKS</h4><i>It's a long story! · Not at first. · What happened next? · So, of course, … · Speaking of love… · I knew it!</i></div>""",
    25, """<ol><li>B: the order of events is not the order in the story: <i>He had just moved</i> and <i>had bought 200 rolls</i> are told later but happened earlier. This prepares the Language focus.</li>
<li>D: accept any reasonable answer; ask for evidence from the audio.</li></ol>""")

    # Page 3 - Language focus
    fs = [("When he started coming to the bakery, he <u>had just moved</u> from Recife.", "he moved"),
          ("By the time he asked me out, he <u>had bought</u> about 200 bread rolls.", "he bought the rolls"),
          ("I thought he <u>had found</u> another girl.", "(she thought) he found a girl"),
          ("When the children <u>had left</u> home, they opened the hostel.", "the children left")]
    fsl = "".join(f"<li>{s} {A('first: ' + a, 'min-width:30mm')}</li>" for s, a in fs)
    b.page(f"""{sec(3, "Language focus: the past perfect", "8 min")}
{sub("A", "Sentences from the podcast. Which action happened first? Write it.", "3 min")}
<ol style="line-height:1.75;font-size:8.9pt;margin:0">{fsl}</ol>
{sub("B", "Complete the rules. Choose.", "3 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0"><li>We form the past perfect with {ch(["have", "had"], "had")} + past participle.</li>
<li>We use it for the {ch(["earlier", "later"], "earlier")} of two past actions.</li>
<li>When the events are told in order (<i>He proposed and she said yes.</i>), we use the {ch(["past simple", "past perfect"], "past simple")}.</li>
<li>The short form of <i>had</i> is {ch(["'s", "'d"], "'d")}: <i>He'd never been so nervous.</i></li></ol>
{sub("C", "Correct or incorrect? Choose.", "2 min")}
<ol style="line-height:1.6;font-size:8.9pt;margin:0"><li>When I got to the party, Bruno had already left. {ch(["correct", "incorrect"], "correct")}</li><li>I had met Paula yesterday at the park. {ch(["correct", "incorrect"], "incorrect")} {R("→ I met Paula yesterday") if T else ""}</li><li>She was angry because he didn't write for two months. {ch(["correct", "incorrect"], "incorrect")} {R("→ hadn't written") if T else ""}</li></ol>
<div class="box sand"><h4>RULE</h4>Past perfect = <b>had</b> + past participle (<i>had moved, had bought, hadn't written</i>). Use it to go back to an <b>earlier</b> past moment, often with <i>when, by the time, already, just, never… before</i> and after <i>thought / realized / found out</i>. Don't use it for every past action. More on the next page: <b>Grammar reference</b>.</div>""",
    24, """<ol><li>A: draw a timeline on the board for each sentence (earlier action on the left).</li>
<li>C: in 2, <i>yesterday</i> is one finished action with no earlier moment, so use the past simple.</li></ol>""")

    grammar_ref.past_perfect(b)

    # Page 5 - Vocabulary lab
    pr = [("a couple that is dating", "a boyfriend and a girlfriend"), ("a couple who have promised to get married", "a fiancé and a fiancée"),
          ("a couple on their wedding day", "a bride and a groom"), ("a married couple", "a husband and a wife")]
    prl = [f'<li value="{i+1}">{d} → {A(w, "min-width:36mm")}</li>' for i, (d, w) in enumerate(pr)]
    dp = [("Bruno was too shy to ask Paula", "out", "for weeks."), ("Finally, they went", "on", "a date on Saturday."), ("Bruno has really fallen", "for", "her."),
          ("At the café, a man was flirting", "with", "Rita all morning."), ("A guy at the bar tried to hit", "on", "Lucy, but she wasn't interested.")]
    dpl = [f'<li value="{i+1}">{a} {A(w, "min-width:9mm")} {e}</li>' for i, (a, w, e) in enumerate(dp)]
    b.page(f"""{sec(4, "Vocabulary lab: people and dating", "4 min")}
{sub("A", "People in relationships. Write two words from the box for each couple.", "2 min")}
<div class="bank">a boyfriend · a bride · a fiancé · a fiancée · a girlfriend · a groom · a husband · a wife</div>
<div style="font-size:8.5pt">{twocol(prl, 2)}</div>
{sub("B", "Dating. Complete with for, on (x2), out or with.", "2 min")}
<div style="font-size:8.5pt">{twocol(dpl, 3)}</div>
<div class="box sand"><h4>WATCH OUT: WORD CHOICE</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>She's married with a doctor.</td><td><b>She's married to a doctor.</b></td><td><i>married to</i> someone; <i>get married</i> (no object) or <i>marry</i> someone.</td></tr>
<tr><td>He dated with her for a year.</td><td><b>He dated her for a year.</b></td><td>no preposition after <i>date</i> (verb).</td></tr>
<tr><td>I have a date with the dentist.</td><td><b>I have an appointment with the dentist.</b></td><td>a <i>date</i> is romantic; doctors and dentists = <i>an appointment</i>.</td></tr></table></div>
{sec(5, "Pronunciation lab: contracted had", "4 min")}
<p class="small" style="margin:.3mm 0">In speaking, <i>had</i> is usually <b>'d</b>: <i>he'd just moved · she'd already decided</i>. Listen for the small /d/ sound: it tells you it's the past perfect.</p>
{audiocard(["11.2"])}
{sub("A", "Listen and repeat. Then tell your teacher something you had never done before you were 18.", "4 min", "11.2")}
<p style="margin:.3mm 0;font-size:8.8pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S112))}</p>""",
    24, """<ol><li>A: <i>fiancé</i> (man) and <i>fiancée</i> (woman) sound the same: /fiˈɑːnseɪ/.</li>
<li>B: <i>hit on someone</i> is informal and a little negative; <i>flirt with</i> is neutral. <i>Fall for someone</i> = start to love them.</li></ol>""")

    # Page 6 - Practice
    pc = [(["met", "had met"], "met"), (["were", "had been"], "had been"), (["long-distance", "long-term"], "long-distance"), (["grew apart", "made up"], "grew apart"),
          (["already split up", "had already split up"], "had already split up"), (["Dump", "Date"], "Dump"), (["cheated on", "fallen for"], "cheated on"),
          (["made up", "split up"], "made up"), (["proposed", "engaged"], "proposed"), (["serious", "casual"], "serious")]
    p = [ch(o, a) for o, a in pc]
    dr = [("For two years, Mrs. Lima and her husband had a", "long-distance"), ("Bruno and Paula have only been on one date. It's still", "casual"),
          ("Ana and Marcos trust each other and talk about their problems. They have a", "healthy"), ("Mrs. Lima was married for 36 years. That's a", "long-term"),
          ("Bruno ironed a shirt! He wants something", "serious")]
    drl = [f'<li value="{i+1}">{s} {A(w, "min-width:20mm")}</li>' for i, (s, w) in enumerate(dr)]
    b.page(f"""{sec(6, "Practice", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Kate writes a blog post about a couple. Choose the correct words.", "5 min")}</div>{img('C', 30, 20)}</div>
<div class="box" style="line-height:1.95;font-size:9pt"><b>Sweet Kate's Blog: a love story with a happy ending</b><br>Remember the wedding cake I dropped? Well, I baked a new one, and on Saturday I finally met the couple, Jake and Megan. They {p[0]} in college, and they {p[1]} together for six years when Megan got a job in Denver. Suddenly they were in a {p[2]} relationship. They slowly {p[3]}: they hardly ever talked, and by the time Megan came home for Christmas, they {p[4]}. Her friends said, "{p[5]} him!" But Jake hadn't {p[6]} her; he was just working too much. A year later, they met at a friend's wedding, talked all night and {p[7]}. Jake {p[8]} the next month. Now that's a {p[9]} relationship!</div>
{sub("B", "Describing relationships. Complete with casual, healthy, long-distance, long-term or serious.", "3 min")}
<div style="font-size:8.6pt"><ol style="line-height:1.8;margin:0">{"".join(drl)}</ol></div>""",
    28, """<ol><li>A: ask the student to explain each tense choice with a timeline (<i>had been together for six years when…</i> = before the job in Denver).</li>
<li>Extra vocabulary: <i>grow apart</i> = become less close; <i>dump</i> = end a relationship suddenly (informal); <i>make up</i> = forgive each other after a fight.</li></ol>""")

    # Page 7 - Speaking
    b.page(f"""{sec(7, "Speaking: telling a love story", "12 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>start a story</th><th>go back in time</th><th>react</th><th>finish</th></tr>
<tr><td><i>It's a long story… · It all started when… · This is how they met.</i></td><td><i>Before that, … · By the time…, they had… · He had just…</i></td><td><i>No way! · What happened next? · That's so romantic!</i></td><td><i>In the end, … · And now… · So that's how…</i></td></tr></table></div>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("A", "Long turn. Prepare for one minute, then talk for two minutes about a couple you know (or a famous couple).", "5 min")}
<ul style="line-height:1.45;font-size:8.9pt;margin:0"><li>how and where they met, and who asked who out</li><li>what had happened in their lives before they met</li><li>any problems (a break-up, a long-distance relationship…)</li><li>their relationship now</li></ul></div>{img('D', 32, 24)}</div>
{sub("B", "Role-play: relationship advice. Your teacher is a friend with a problem. Ask questions and give advice. Then change roles.", "4 min")}
<p style="margin:.3mm 0;font-size:8.6pt">{R("Teacher's card: You've been with your partner for two years. They've just been offered a great job in another country for a year, and they want to try a long-distance relationship. You love them, but you're not sure you can do it. You had a long-distance relationship before, and it ended badly.") if T else ""}</p>
{sub("C", "Talking point. Discuss with your teacher.", "3 min")}
<ol style="line-height:1.5;font-size:8.9pt;margin:0"><li>Do you believe in love at first sight?</li><li>Is it a good idea to date a coworker? Why or why not?</li><li>What makes a relationship healthy and strong?</li></ol>""",
    28, """<ol><li>A: if the student prefers, they can talk about a couple from a movie or a book. Don't interrupt; note mistakes for the error log (page 8), especially <i>married with</i> and the past perfect. Fluency option (3-2-1): the same story in 2 minutes, then in 1 minute.</li>
<li>B: advice language from B1 Unit 08 (<i>If I were you, I'd…</i>) is useful here.</li></ol>""")

    # Page 8 - Wrap-up
    cd = ["I can understand a long personal story on a podcast.", "I can use the past perfect to show an earlier past action.",
          "I can talk about relationships and dating and tell the story of a couple."]
    cdr = "".join(f"<tr><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for s in cd)
    b.page(f"""{sec(8, "Wrap-up and homework", "4 min")}
{sub("A", "Can-do check", "1 min")}
<table class="ck" style="font-size:8.6pt"><tr><th>In English…</th><th style="width:16mm">Easy!</th><th style="width:16mm">Sometimes</th><th style="width:16mm">Not yet</th></tr>{cdr}</table>
{sub("B", "My language notes. Write three corrections from today's class.", "2 min")}
<div style="display:flex;gap:5mm;font-size:8.6pt"><div style="flex:1"><b>I said…</b>{lines(3)}</div><div style="flex:1"><b>Better:</b>{lines(3)}</div></div>
{sub("C", "Homework: writing (100–150 words)", "1 min")}
<p style="margin:.3mm 0"><b>A love story.</b> Write the relationship history of a couple you know or a famous couple. Read Bruno's story about his parents first.</p>
<div class="box" style="font-size:8.6pt;line-height:1.4;margin:.5mm 0"><i>My parents met in Porto Alegre in 1995. My dad had broken his leg in a soccer game, and my mom was the nurse who looked after him. He had never been in a hospital before, and he was a terrible patient! He complained about everything, but she always made him laugh. By the time he left the hospital, he had fallen for her. A week later, he asked her out, and he arrived at their first date on crutches, with flowers. Once they split up for a month because my dad had forgotten her birthday, but they made up. They had been together for three years when they got married in 1998. Twenty-eight years later, they still argue about that birthday!</i></div>
<p class="small" style="margin:.3mm 0">Checklist: ☐ three relationship events &nbsp;☐ two or more past perfect verbs &nbsp;☐ one phrasal verb (<i>ask out, split up, make up</i>) &nbsp;☐ time linkers (<i>when, by the time, a year later</i>) &nbsp;☐ 100–150 words</p>
{lines(6)}""",
    30, """<ol><li>B (error log): during the lesson, note 3–5 real mistakes. Here, the student writes what they said and the better version; guide them to self-correct first.</li>
<li>C: check that the past perfect is used only for earlier actions, and <i>married to</i> / <i>got married</i>.</li></ol>""")

    script = "".join(f"<p style='margin:.6mm 0'><b>{l.split(': ', 1)[0]}:</b> {l.split(': ', 1)[1]}</p>" for l in S111)
    b.extra("Audio script", f"""
{sub("11.1", "Gap Year Diaries: a love story (natural and slow)")}
<div style="line-height:1.35;font-size:8.7pt">{script}</div>
{sub("11.2", "Repeat: contracted had")}
<p>{" · ".join(S112)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 11 - Relationships and dating")
