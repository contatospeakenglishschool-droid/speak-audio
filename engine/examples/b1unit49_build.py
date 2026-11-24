# Speak! Progress B1 - Unit 49 "Longevity" (all English) - lean B1 format
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
setup(band="B1 · UNIT 49", audio_json="audio_b1-unit-49.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-49"]
S491 = [l.split(": ", 1) for l in _r["49.1 Gap Year Diaries: the secret of a long life"].split("\n")]
S492 = [x.split(": ", 1)[1] for x in _r["49.2 Repeat: the third conditional"].split("\n")]


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
    cover = cover_html(T, "LEVEL B1 · UNIT 49", "Longevity", "A long, healthy life · <b>If I had stayed…, I would have…</b>",
                       [("YOU CAN", "talk about healthy habits, explain reasons and imagine a different past"),
                        ("LANGUAGE", "longevity · life expectancy · well-being · stick to a diet · quit smoking · One explanation is… · the third conditional"),
                        ("PRONUNCIATION", "would've /ˈwʊdəv/ · I'd · hadn't")])
    words = ["life expectancy", "longevity", "neighborhood", "overweight", "premature", "wealthy", "well-being"]
    defs = {"life expectancy": "how long a person is likely to live", "longevity": "living for a long time",
            "neighborhood": "the area of a city where you live", "overweight": "having more body weight than is healthy",
            "premature": "happening too soon, earlier than expected", "wealthy": "rich",
            "well-being": "the state of feeling healthy and happy"}
    order = [4, 6, 3, 0, 5, 2, 1]
    kwl = "".join(f'<li>{A(words[i], "min-width:26mm")} <span style="color:#6b7377">= {defs[words[i]]}</span></li>' for i in order)
    b.page(f"""{sec(1, "Warm-up: a long, healthy life", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["What do you think is important for a long, healthy life? Name three things.", "Do you know anyone over ninety? What is their life like?", "Would you like to live to a hundred? Why or why not?"], "START TALKING")}</div></div>
{sub("A", "Health and well-being. Write the words from the box next to their meanings.", "3 min")}
<div class="bank">{" · ".join(words)}</div>
<ol style="font-size:8.7pt;line-height:1.75;margin:0">{kwl}</ol>
{talk(["What is the life expectancy in your city? Do you think it is going up or down? Why?", "What can a person do to avoid a premature death?", "Is your neighborhood a good place for older people? Why or why not?"], "USE THE WORDS")}""",
    30, """<ol><li>Top box: 3 minutes. Possible answers: keep active, eat well, sleep well, reduce stress, have friends, good genes, good health care.</li>
<li>A: 4 minutes with the questions. The student gives opinions, not numbers: there is no need to know real statistics. <i>Overweight</i> is the polite word; <i>obese</i> is the medical word for very overweight; avoid <i>fat</i> about people.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Gap Year Diaries: Danny interviews Ana's grandmother Lourdes, 97 · complete the table · questions · Talk about it",
                      "the third conditional: if + had done, would have done; regrets; second vs third conditional", "Choose the correct form · rewrite · Use it (oral)",
                      "would've (49.2) · explaining and speculating: One explanation is… · Why do you think…? · long turn: a decision that changed your life", "Ana's message to Carol · rewrite · watch out · writing about the oldest person you know"),
        """The Linguahouse lesson is a 2008 newspaper article that lists research results from several real universities (how many years chocolate, golf, marriage or education add to your life) and practices phrases for explaining and speculating. We did not use the article: it is full of statistics we cannot check. Instead, Danny records a Gap Year Diaries episode at Grandma Lourdes's apartment, with Ana. Lourdes turned 97 last week. She grew up on a farm and never stopped moving: she walks to the bakery every morning (two blocks) and takes the stairs when the elevator is broken. Food: rice and beans, vegetables from the street market, fruit every day, meat only on Sundays and one piece of dark chocolate after lunch. She never smoked; her husband smoked for 20 years, quit at 40 and lived until 88. Her one regret: she left school at 12 to help on the farm (she would have become a teacher), but she taught all her grandchildren to read, and if she hadn't gone to that church party, she wouldn't have met her husband. She plays cards with her neighbors every Thursday, a grandchild calls her every night, and she doesn't worry about things she can't change. Ana: good genes may be part of the reason, but the main reason is her lifestyle. We kept the Linguahouse vocabulary, the lifestyle phrases, the explaining and speculating phrases and the discussion questions, and added a new B1 grammar point: the third conditional.""",
        """<i>If I would have known</i> (<i>would</i> in the if clause); <i>would of</i>; mixing the second and third conditionals (<i>If I had studied, I would pass</i>). Vocabulary: <i>quit to smoke</i>, <i>make exercise</i>, <i>life hope</i>. Pronunciation: <i>would've</i> /ˈwʊdəv/; <i>'d</i> = <i>had</i> or <i>would</i>.""",
        "Track 49.1 Gap Year Diaries: the secret of a long life (natural and slow; Danny, Ana and Lourdes) · Track 49.2 Repeat: the third conditional"))

    # Page 2 - Listening
    rows = [("activity", "never stopped moving; walks to the bakery every morning; takes the stairs"),
            ("food", "rice and beans, vegetables, fruit every day; meat only on Sundays; one piece of dark chocolate"),
            ("smoking", "never smoked (her husband quit at forty)"),
            ("people", "cards with her neighbors on Thursdays; a grandchild calls every night"),
            ("attitude", "doesn't worry about things she can't change")]
    rt = "".join(f'<tr><td><b>{r}</b></td><td>{A(a, "min-width:90mm")}</td></tr>' for r, a in rows)
    qs = [("Why did Lourdes leave school at twelve?", "To help on the farm."),
          ("What happened to her husband after he quit smoking?", "He lived until eighty-eight."),
          ("What would Lourdes have become if she had stayed in school?", "A teacher."),
          ("What does Ana think is the main reason for her grandmother's longevity?", "Her lifestyle: she's active, eats well and is never alone (genes may be part of it).")]
    ql = "".join(f"<li>{q} {A(a, 'min-width:44mm')}</li>" for q, a in qs)
    chunks = "stick to a healthy diet · quit smoking · stay active · lose weight · be positive · adopt a healthier lifestyle"
    b.page(f"""{sec(2, "Listening: the secret of a long life", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Danny interviews Ana's grandmother Lourdes, 97. Listen and complete her habits.", "5 min")}
<table style="font-size:8.4pt;margin:.5mm 0">{rt}</table></div>{img('B', 32, 30)}</div>
{audiocard(["49.1 · NATURAL", "49.1 · SLOW"])}
{sub("B", "Listen again and answer.", "3 min")}
<ol style="line-height:1.5;font-size:8.6pt;margin:0">{ql}</ol>
<p style="margin:.6mm 0;font-size:8.6pt"><b>Think about it:</b> Lourdes has one regret, but she says "life worked out in the end". What does she mean? {A("open answer: she didn't become a teacher, but she met her husband and taught her grandchildren to read", "min-width:20mm")}</p>
<div class="box sand" style="margin:.8mm 0;font-size:8.4pt"><h4>NOTICE: USEFUL CHUNKS</h4>{chunks}</div>
{talk(["Which of Lourdes's habits do you already have? Which would be hardest for you?", "Do you agree that worrying doesn't add a day to your life?", "What is your grandparents' secret (or the secret of an older person you know)?"])}""",
    30, """<ol><li>A: play the natural version; play the slow one if needed. Accept short notes.</li>
<li>B: ask the student to find the two sentences with <i>if</i> about the past: <i>If he hadn't quit, he wouldn't have lived so long. · If I had stayed in school, I would have become a teacher.</i> They come back on page 3.</li>
<li>Notice: the student makes a true sentence with two chunks (<i>I'm trying to stick to a healthy diet</i>). Talk about it: 4 minutes.</li></ol>""")

    # Page 3
    lean.grammar_in_class(b, grammar_ref.third_conditional)

    # Page 4 - Practice
    pc = [("If I", ["had known", "would know"], "had known", "about the party, I would have come."), ("If she had left earlier, she", ["wouldn't miss", "wouldn't have missed"], "wouldn't have missed", "the bus."),
          ("We would have won if we", ["had trained", "trained"], "had trained", "more."), ("If he hadn't quit smoking, he", ["wouldn't have lived", "won't live"], "wouldn't have lived", "so long."),
          ("I", ["would have", "would of"], "would have", "called you, but my phone died."), ("If you had asked me, I", ["would help", "would have helped"], "would have helped", "you."),
          ("If I", ["had more time", "had had more time"], "had more time", "now, I'd exercise every day."), ("If they hadn't met at that party, they", ["wouldn't have got", "didn't get"], "wouldn't have got", "married.")]
    cl = "".join(f"<li>{a} {ch(o, r)} {z}</li>" for a, o, r, z in pc)
    rw = [("Lourdes left school at twelve, so she didn't become a teacher.", "If Lourdes hadn't left school at twelve, she would have become a teacher."),
          ("I didn't sleep well, so I felt tired all day.", "If I had slept well, I wouldn't have felt tired all day."),
          ("Danny helped paint Ana's kitchen, so he tried her grandmother's chicken soup.", "If Danny hadn't helped paint Ana's kitchen, he wouldn't have tried her grandmother's chicken soup.")]
    rwl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw)
    use = ["What would you have studied if you hadn't chosen your profession?", "Think of a good decision you made. What would have happened if you hadn't made it?",
           "Where would you have lived if you had been born in another country?", "What healthy habit would you have started earlier if you had known its benefits?",
           "Tell me about a small mistake. What would you have done differently?"]
    b.page(f"""{sec(4, "Practice: if I had known…", "10 min")}
{sub("A", "Choose the correct words.", "3 min")}
<ol style="line-height:1.7;font-size:8.7pt;margin:0;columns:2;column-gap:6mm">{cl}</ol>
{sub("B", "Rewrite the sentences with the third conditional.", "4 min")}
<ol style="line-height:1.45;font-size:8.7pt;margin:0">{rwl}</ol>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    30, """<ol><li>A: 3 minutes. Item 7 is a second conditional (<i>now</i>): a present situation, so <i>had more time</i>. <i>Got</i> and <i>gotten</i> are both used in American English after <i>have</i>.</li>
<li>B: accept <i>'d</i> for <i>had</i> and <i>would</i>. Item 3: Danny helped paint Ana's kitchen in B1 31 and got Grandma's chicken soup as a thank-you.</li>
<li>Use it: 3 minutes, all oral. Answer one question about yourself first as a model.</li></ol>""")

    # Page 5 - Speaking
    card = f"""<div class="box" style="margin-top:1mm;font-size:8.2pt">{R("<b>Teacher's card (B):</b> read the situations one at a time. The student gives two possible reasons with the phrases in the box. (1) Your neighbor is ninety-two and still drives to the beach every weekend. (2) A friend lost ten kilos in three months. (3) Your uncle feels much better since he moved to a small town. (4) A colleague is always sick on Mondays. (5) In some neighborhoods, people live longer than in others. There are no right answers: any logical reason is fine.")}</div>""" if T else ""
    b.page(f"""{sec(5, "Speaking: why do you think…?", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE: EXPLAINING AND SPECULATING</h4>
<table style="margin:0;font-size:8.2pt"><tr><th>a possible reason</th><th>the main reason</th><th>a cause</th><th>a different past</th></tr>
<tr><td><i>One explanation is that… · One theory is that… · It may be the reason. · Genes may be responsible.</i></td><td><i>The main reason is (that)… · I think it's mainly because…</i></td><td><i>It may be due to… · …possibly because of… · …as a consequence of… (formal)</i></td><td><i>If she hadn't…, she wouldn't have… · I would have… if I'd known…</i></td></tr></table></div>
{audiocard(["49.2"])}
{sub("A", "Listen and repeat. Say would've /ˈwʊdəv/, not would have.", "3 min", "49.2")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S492))}</p>
{sub("B", "Your teacher describes five situations. Give two possible reasons for each one with the phrases in the box.", "5 min")}{card}
{sub("C", "Discuss. Is it good to live to a very old age? What would make a long life a happy life?", "4 min")}
{sub("D", "Long turn. Talk about a decision or a chance meeting that changed your life. What happened? What would have happened if…?", "5 min")}
<p style="margin:.3mm 0;font-size:8.5pt">Plan (1 min): {lines(1)}</p>""",
    30, """<ol><li>B replaces the Linguahouse sentences about real research: the situations are imaginary, so the student only speculates. Push for variety: <i>One explanation is… / It may be due to…</i>.</li>
<li>C comes from the Linguahouse talking point. D: 1 minute to plan, 2 minutes to talk, with at least two third conditionals. Last 3 minutes: wrap-up (two corrections, and ask <i>Can you now explain reasons and imagine a different past?</i>).</li></ol>""")

    # Homework
    pc2 = [(["had heard", "would hear"], "had heard"), (["would have laughed", "would laugh"], "would have laughed"), (["hadn't", "wouldn't"], "hadn't"),
           (["would of", "would have"], "would have"), (["had stayed", "stayed"], "had stayed"), (["would have loved", "had loved"], "would have loved")]
    p = [ch(o, a) for o, a in pc2]
    rw2 = [("I didn't take an umbrella, so I got wet.", "If I had taken an umbrella, I wouldn't have got(ten) wet."),
           ("She didn't call me, so I didn't know about the party.", "If she had called me, I would have known about the party."),
           ("We missed the bus because we left late.", "If we hadn't left late, we wouldn't have missed the bus.")]
    rwl2 = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw2)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Ana writes to her cousin Carol in Orlando. Choose the correct words.", "")}</div>{img('C', 30, 19)}</div>
<div class="box" style="line-height:1.85;font-size:8.8pt;margin:.5mm 0"><b>Hi Carol!</b> Grandma's birthday was lovely. Ninety-seven candles! Danny interviewed her for his podcast. If you {p[0]} her, you {p[1]}: she told Danny to stop looking at his phone! She says that if Grandpa {p[2]} quit smoking, he wouldn't have lived so long. I {p[3]} sent you a video, but my phone died. If you {p[4]} one more week in São Paulo, she {p[5]} to see you. Next time, OK? Love, Ana</div>
{sub("B", "Rewrite the sentences with the third conditional.", "")}
<ol style="line-height:1.5;font-size:8.7pt;margin:0">{rwl2}</ol>
{lean.watch_out([("He quit to smoke last year.", "He quit smoking last year.", "<i>quit / stop / give up</i> + -ing."), ("I make exercise every day.", "I exercise / I work out every day.", "we <i>do</i> exercise, never <i>make</i> it."), ("The life hope in Brazil is going up.", "Life expectancy in Brazil is going up.", "the phrase is <i>life expectancy</i>.")])}
{lean.writing_task(sub, "Write a post for Danny's podcast page about the oldest person you know: their habits, their story and one decision that changed their life.", "The oldest person I know is…", ["their habits (food, activity, people)", "one decision that changed their life", "at least two third conditionals", "One explanation is… / The main reason is…", "100–150 words"], "I can talk about healthy habits, explain reasons and imagine a different past.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class. In A, the fifth gap is a third conditional too: Carol flew back to Orlando before the birthday. Read the writing at home and choose two mistakes to discuss in class.</p>""")

    script = "".join(f"<p style='margin:.5mm 0'><b>{s}:</b> {t}</p>" for s, t in S491)
    b.extra("Audio script", f"""
{sub("49.1", "Gap Year Diaries: the secret of a long life (natural and slow; Danny, Ana and Lourdes)")}
<div style="line-height:1.3;font-size:8.2pt">{script}</div>
{sub("49.2", "Repeat: the third conditional")}
<p>{" · ".join(S492)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 49 - Longevity")
