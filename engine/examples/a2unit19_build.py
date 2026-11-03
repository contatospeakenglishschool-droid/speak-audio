# Speak! Bridge A2 - Unit 19 "The Royals" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 19", audio_json="audio_a2-unit-19.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["a2-unit-19"]
PARAS = [x.split(": ", 1)[1] for x in _r["19.1 Grace Kelly"].split("\n")]
S192 = [x.split(": ", 1)[1] for x in _r["19.2 Past endings"].split("\n")]
S193 = [x.split(": ", 1)[1] for x in _r["19.3 Irregular verbs"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 19", "The Royals", "An American princess · <b>past simple review</b>",
                       [("YOU CAN", "tell the story of someone's life and ask about the past"),
                        ("LANGUAGE", "She met the prince in 1955. · When did they get married? · She didn't make any more movies."),
                        ("PRONUNCIATION", "-ed: watched /t/ · moved /d/ · wanted /ɪd/")])
    ma = [("The king and queen have three children:", "two princes and a princess.", "c"), ("The royal family", "lives in a palace.", "a"),
          ("The princess works with a charity", "that helps children.", "b"), ("The prince often gives interviews", "to journalists about his work.", "d")]
    mb = [("After dating for two years, my sister and her boyfriend", "announced their engagement.", "d"), ("They're going to have a big wedding", "in the spring, with 200 guests.", "c"),
          ("My uncle had a happy marriage for ten years,", "but sadly it ended in divorce.", "a"), ("My grandfather says that when he dies,", "he wants a small funeral.", "b")]
    def mtab(items):
        ends = sorted([(k, e) for _, e, k in items])
        return "".join(f"<tr><td>{i+1}. {a} {R(k)}</td><td>{ends[i][0]}. {ends[i][1]}</td></tr>" for i, (a, _, k) in enumerate(items))
    b.page(f"""{sec(1, "Warm-up: royal families and life events", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 44, 28)}
<div style="flex:1">{sub("A", "Match the halves of the sentences.", "5 min")}
<table style="table-layout:fixed;margin-top:0;font-size:8.8pt">{mtab(ma)}</table></div></div>
<table style="table-layout:fixed;margin-top:1.5mm;font-size:8.8pt">{mtab(mb)}</table>
<p class="small">Underline the words about royal families and life events. Do you know them all?</p>
{sub("B", "Talk about it.", "3 min")}
<ol><li>Which royal families do you know? Are they often in the news in Brazil?</li><li>Would you like to be a prince or a princess? Why or why not?</li></ol>""",
    22, """<ol><li>A: <b>engagement</b> = a promise to get married · <b>wedding</b> = the ceremony · <b>marriage</b> = the relationship · <b>funeral</b> = the ceremony after someone dies. Drill <i>palace</i> (PAL-iss) and <i>charity</i>.</li>
<li>B: the U.S. has no royal family, but Americans love royal news: millions watched the royal weddings on TV.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Royal family and life event words</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Hollywood History: Grace Kelly, the American princess</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Past simple: time references, irregular verbs, -ed, did</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Past simple review: forms, spelling, three -ed sounds, irregulars</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>5 min</td><td>-ed endings · irregular verbs</td><td>5</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Grace's children · Word builder: life events</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Information gap: Meghan Markle and Kate Middleton</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework (50–75 words)</td><td>8</td></tr></table>
<div class="box sand"><h4>AN AMERICAN TAKE ON "THE ROYALS"</h4>The original lesson is about Princess Diana. Here the story is about Grace Kelly, an American actress who became Princess of Monaco, told by a podcast host (voice Studio-O). Facts: born in Philadelphia on November 12, 1929 (Encyclopaedia Britannica); Best Actress Oscar for <i>The Country Girl</i> at the March 1955 ceremony; met Prince Rainier III at the palace in Monaco while at the Cannes Film Festival in 1955; married him in April 1956, and more than 30 million people watched on live TV (HISTORY.com, "Grace Kelly and Prince Rainier marry"); three children: Caroline (1957), Albert (1958) and Stephanie (1965); died on September 14, 1982, the day after a car accident (Britannica). Albert studied political science at Amherst College, Massachusetts, graduating in 1981, and has been Prince of Monaco since 2005 (Prince's Palace of Monaco). Speaking: Meghan Markle (born in Los Angeles, 1981; studied at Northwestern University near Chicago) and Catherine (Kate) Middleton.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students pronounce every <i>-ed</i> as an extra syllable (<i>watch-ed</i> ✗), keep the past form after <i>did</i> (<i>Did she won?</i> ✗) and make questions without <i>did</i> (<i>When they got married?</i> ✗).</div>
<div class="box"><h4>AUDIO</h4>Track 19.1 Grace Kelly (slow and natural) · Track 19.2 -ed endings · Track 19.3 Irregular verbs</div>""")

    # Page 2
    tl = [("1929", "Grace was born in Philadelphia."), ("After high school", "She moved to New York and studied acting."), ("1", "She won an Oscar for Best Actress.", "1955"),
          ("2", "She met Prince Rainier for the first time.", "1955"), ("3", "They announced their engagement.", "January 1956"), ("4", "They got married in Monaco.", "April 1956"),
          ("5", "She had a car accident and died the next day.", "September 1982"), ("Today", "Her son Albert is the Prince of Monaco.")]
    tlr = "".join(f"<tr><td style='width:34mm'><b>{x[0]}</b> {A(x[2], 'min-width:22mm') if len(x) > 2 else ''}</td><td>{x[1]}</td></tr>" for x in tl)
    tf = [("Grace's family was poor.", "F: rich and famous in Philadelphia."), ("She made three movies with Alfred Hitchcock.", "T"),
          ("Monaco is a big country in South America.", "F: a very small country near France."), ("More than 30 million people watched the wedding on TV.", "T"),
          ("After the wedding, she made more movies.", "F: she didn't make any more movies."), ("As a princess, she helped children and artists.", "T")]
    tfl = [f'<li value="{i+1}">{s} <b>T / F</b> {R(a)}</li>' for i, (s, a) in enumerate(tf)]
    b.page(f"""{sec(2, "Listening: the American princess", "10 min")}
<div style="display:flex;gap:3mm;align-items:center"><p style="flex:1;margin:0">Royal families are often in the news, and Americans love royal stories. But did you know that an American movie star became a real princess? Listen to <i>Hollywood History</i>.</p>{img('D', 32, 21)}{img('B', 32, 21)}</div>
{audiocard(["19.1 · SLOW", "19.1 · NATURAL"])}
{sub("A", "Listen and complete the timeline of Grace Kelly's life.", "5 min", "19.1 · SLOW")}
<table style="table-layout:fixed;margin-top:0;font-size:9pt">{tlr}</table>
{sub("B", "Listen again. True (T) or false (F)? Correct the false sentences.", "5 min", "19.1 · NATURAL")}
{twocol(tfl, 3)}""",
    22, """<p>A: practice saying years first: 1929 = nineteen twenty-nine, 1956 = nineteen fifty-six. Photos: Philadelphia today and the harbor in Monaco. Sources: Britannica, HISTORY.com (see the overview).</p>""")

    # Page 3
    irr = [("become", "became"), ("begin", "began"), ("feel", "felt"), ("get", "got"), ("have", "had"), ("make", "made"), ("meet", "met"), ("write", "wrote"), ("win", "won"), ("be", "was / were")]
    irt = "".join(f"<td style='text-align:center'><b>{a}</b><br>{A(p, 'min-width:12mm')}</td>" for a, p in irr)
    b.page(f"""{sec(3, "Language focus: the past simple", "10 min")}
{sub("A", "Read the sentences. Underline the time references and circle the irregular verbs.", "3 min")}
<ol style="font-size:9pt"><li>Grace Kelly was born in Philadelphia <u>in 1929</u>. {R("time: in 1929 · irregular: was")}</li>
<li><u>After high school</u>, she moved to New York and studied acting. {R("time: after high school · regular: moved, studied")}</li>
<li><u>In 1955</u>, she won an Oscar, and she met Prince Rainier for the first time. {R("time: in 1955 · irregular: won, met")}</li>
<li>They wrote letters to each other <u>for months</u>. {R("time: for months · irregular: wrote")}</li></ol>
{sub("B", "Complete the table of irregular verbs from the podcast.", "3 min")}
<table style="table-layout:fixed;margin-top:0;font-size:8.6pt"><tr>{irt}</tr></table>
{sub("C", "Questions and negatives. Choose the correct options.", "4 min")}
<div class="bank" style="background:#fff">When <b>did</b> they <b>get</b> married? · <b>Did</b> she <b>win</b> an Oscar? Yes, she <b>did</b>. · She <b>didn't make</b> any more movies.</div>
<ol><li>In past simple questions we use {ch(["do", "did"], "did")}.</li><li>After <i>did</i> / <i>didn't</i>, the verb is in the {ch(["base form", "past form"], "base form")}: <i>win</i>, not <i>won</i>.</li>
<li>Short answers: <i>Yes, she</i> {ch(["did", "won"], "did")}.</li></ol>
<div class="box sand"><h4>RULE</h4>Positive: past form (<i>met, moved</i>). Negative and question: <b>did / didn't + base verb</b> (<i>didn't meet · Did she meet?</i>). More on the next page: <b>Grammar reference</b>.</div>""",
    24, """<ol><li>A: <i>in 1955, after high school, for months, the next day</i> are all time references; biographies are full of them.</li>
<li>B: have the student say the pairs aloud (become–became…).</li></ol>""")

    grammar_ref.past_simple_review(b)

    # Page 5
    b.page(f"""{sub("D", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>Did she won an Oscar?</td><td><b>Did she win an Oscar?</b></td><td>did + base verb.</td></tr>
<tr><td>When they got married?</td><td><b>When did they get married?</b></td><td>question = did.</td></tr>
<tr><td>She didn't made more movies.</td><td><b>She didn't make…</b></td><td>didn't + base verb.</td></tr>
<tr><td>watch-ED (2 syllables)</td><td><b>watched /wɑːtʃt/</b></td><td>/ɪd/ only after t, d.</td></tr>
<tr><td>She was born on 1929.</td><td><b>She was born in 1929.</b></td><td>in + year.</td></tr>
<tr><td>They married with Grace in 1956.</td><td><b>Rainier married Grace. / They got married.</b></td><td>no with.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "5 min")}
{audiocard(["19.2", "19.3"])}
{sub("A", "-ed endings. Listen and repeat. Write each group's sound: /t/, /d/ or /ɪd/.", "2 min", "19.2")}
<table style="table-layout:fixed;margin-top:0;font-size:9pt"><tr><th>{R("/t/")}</th><th>{R("/d/")}</th><th>{R("/ɪd/")}</th></tr><tr>{"".join(f"<td>{s.replace('.', ',').rstrip(',')}</td>" for s in S192)}</tr></table>
{sub("B", "Irregular verbs. Listen and repeat.", "2 min", "19.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S193)}</div>
<div class="box" style="margin-top:1mm"><h4>ONE SYLLABLE</h4><b>watched, helped, worked, moved, called</b> = one syllable. Only <b>wanted, started, visited, decided</b> get an extra syllable /ɪd/, because the verb ends in <b>t</b> or <b>d</b>.</div>""",
    24, """<ol><li>4A: tap the syllables on the table: <i>watched</i> (1 tap), <i>wanted</i> (2 taps).</li>
<li>4B: then say the base form; the student says the past.</li></ol>""")

    # Page 6
    gp = [("was", "be"), ("studied", "study"), ("was", "be"), ("studied", "study"), ("graduated", "graduate"), ("became", "become"), ("married", "marry")]
    o = [A(w, "min-width:16mm") + f" ({v})" for w, v in gp]
    le = [("fall", "in love"), ("go on", "a first date"), ("get", "engaged"), ("get", "married"), ("have", "a baby"), ("get", "divorced"), ("retire", "from work"), ("pass", "away (= die, polite)")]
    lel = [f'<li value="{i+1}">{A(v, "min-width:12mm")} {n}</li>' for i, (v, n) in enumerate(le)]
    b.page(f"""{sec(5, "Practice", "8 min")}
{sub("A", "Read about two of Grace's children. Complete with the past simple of the verbs.", "5 min")}
<div class="msg" style="max-width:none;font-size:9pt;line-height:1.6"><b>Caroline</b> {o[0]} born in 1957. She {o[1]} in Paris.<br>
<b>Albert</b> {o[2]} born in 1958. Like his mother, he loved the United States. He {o[3]} political science at Amherst College in Massachusetts and {o[4]} in 1981. In 2005, he {o[5]} the Prince of Monaco, and in 2011 he {o[6]} Charlene, a South African swimmer from the Olympic Games.</div>
<p class="small" style="margin-top:1mm">Now ask your teacher two questions about the text: <i>Where did Albert study? When did he…?</i></p>
{sub("B", "Word builder: life events. Complete with the verbs.", "3 min")}
<div class="bank">fall · get · get · get · go on · have · pass · retire</div>
{twocol(lel, 4)}""",
    22, """<ol><li>A: check <i>graduated</i> /ɪd/ and <i>married</i> /d/. Fact: Prince's Palace of Monaco.</li>
<li>B: <i>get married</i> is more common than <i>marry</i> in everyday speech.</li></ol>""")

    # Page 7
    meg = [("born in", "Los Angeles", "Where was she born?"), ("started acting when she was", "a child", "When did she start acting?"),
           ("studied at", "Northwestern University, near Chicago", "Where did she study?"), ("acted in TV shows, for example", "Suits", "What TV show did she act in?"),
           ("met Prince Harry in 2016.", "A friend", "Who introduced them?"), ("got married at", "Windsor Castle", "Where did they get married?"),
           ("now live in", "California", "Where do they live now?")]
    mtext = (f"Meghan Markle was born in 1) ______ in 1981. She started acting when 2) ______. She studied at 3) ______ and then acted in TV shows, for example 4) ______. "
             f"She met Prince Harry in 2016: 5) ______ introduced them. They got married at 6) ______ in 2018. Later, they decided to leave their royal jobs, and they now live in 7) ______.")
    for i, (_, a, _) in enumerate(meg):
        mtext = mtext.replace(f"{i+1}) ______", f"{i+1}) {A(a, 'min-width:20mm')}")
    qkey = " · ".join(f"{i+1} {q}" for i, (_, _, q) in enumerate(meg))
    ktext = ("Catherine (Kate) Middleton was born in England in <b>1982</b>. At school, she played <b>hockey</b> and other sports. She studied <b>art history</b> at the University of St Andrews in Scotland, "
             "where she met <b>Prince William</b>. They announced their engagement in <b>2010</b> and got married at <b>Westminster Abbey</b> in London in 2011. They have <b>three</b> children.")
    b.page(f"""{sec(6, "Speaking: two princesses", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><p style="flex:1;margin:0">Two women who married into the British royal family: one from the U.S. and one from England. Ask and answer questions to complete the information.</p>{img('C', 30, 20)}</div>
{sub("A", "Text 1: Meghan, the American. Prepare the questions. Then ask your teacher and complete the text.", "6 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.6">{mtext}</div>
<p class="small" style="margin:.5mm 0">Start your questions with: 1 Where · 2 When · 3 Where · 4 What · 5 Who · 6 Where · 7 Where</p>
<p class="small">{R(qkey)}</p>
{sub("B", "Text 2: Kate, the English princess. Now your teacher asks you. Answer with the information in bold.", "6 min")}
<div class="box" style="margin-top:1mm;font-size:9pt">{ktext}</div>""",
    26, """<ol><li>A: answer the student's questions with the information in the text (TB). Insist on <i>did</i> and the base verb; 7 is present simple (<i>do they live</i>).</li>
<li>B: ask: When was she born? What sport did she play? What did she study? Who did she meet there? When did they announce their engagement? Where did they get married? How many children do they have?</li></ol>""")

    # Page 8
    pc = [("A2 Unit 15", "I can put ideas in order and talk about changing my mind."), ("A2 Unit 16", "I can define people, things and places with who, that and where."),
          ("A2 Unit 17", "I can make phone calls, take a message and leave a voicemail."), ("A2 Unit 18", "I can agree and disagree with so, neither, me too and me neither."),
          ("A2 Unit 19", "I can tell the story of someone's life with the past simple.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    rn = [("is", "was"), ("becomes", "became"), ("meets", "met"), ("write", "wrote"), ("get", "got"), ("have", "had"), ("dies", "died")]
    rt = (f"Prince Rainier III <s>{rn[0][0]}</s> {R(rn[0][1])} born in 1923. He <s>{rn[1][0]}</s> {R(rn[1][1])} the Prince of Monaco in 1949. In 1955, he <s>{rn[2][0]}</s> {R(rn[2][1])} Grace Kelly. "
          f"They <s>{rn[3][0]}</s> {R(rn[3][1])} letters for months, and they <s>{rn[4][0]}</s> {R(rn[4][1])} married in 1956. They <s>{rn[5][0]}</s> {R(rn[5][1])} three children. Rainier <s>{rn[6][0]}</s> {R(rn[6][1])} in 2005.")
    if not T:
        rt = rt.replace("<s>", "<b>").replace("</s>", "</b>")
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Rewrite the text in the past simple. Change the verbs in bold.</b></p>
<div class="msg" style="max-width:none;font-size:9pt;line-height:1.6">{rt}</div>
<p style="margin-top:2mm"><b>2. A life story (50–75 words).</b> Write about the life of a famous person you admire (or someone in your family). Use time references: <i>in 1990, after school, three years later…</i></p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>1: Rainier III was Prince of Monaco from 1949 until his death in 2005; then his son Albert became prince. Next class: the student reads the life story; ask follow-up questions with <i>did</i>.</p>""")

    b.extra("Audio script", f"""
{sub("19.1", "Hollywood History: Grace Kelly (slow and natural)")}
<p style="line-height:1.42">{"<br>".join(PARAS)}</p>
{sub("19.2", "-ed endings")}
<p>{" · ".join(S192)}</p>
{sub("19.3", "Irregular verbs")}
<p>{" · ".join(S193)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 19 - The Royals")
