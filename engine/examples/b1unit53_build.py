# Speak! Progress B1 - Unit 53 "Population science" (all English) - lean B1 format
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
setup(band="B1 · UNIT 53", audio_json="audio_b1-unit-53.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-53"]
S531 = [l.split(": ", 1) for l in _r["53.1 Gap Year Diaries: big families, small families"].split("\n")]
S532 = [x.split(": ", 1)[1] for x in _r["53.2 Repeat: will have done"].split("\n")]



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
    cover = cover_html(T, "LEVEL B1 · UNIT 53", "Population science", "Big cities and family size · <b>By 2050, we'll have…</b>",
                       [("YOU CAN", "talk about population and family size, and say what will have happened by a future time"),
                        ("LANGUAGE", "fertility rate · estimate · incentive · cope with · affordable · will have + past participle · by the time"),
                        ("PRONUNCIATION", "'ll have /əlhəv/ → /ələv/ · won't have")])
    words = ["child mortality", "the developing world", "environmental resources", "an estimate", "fertility rate", "an incentive", "primary education", "secondary education"]
    defs = {"child mortality": "the number of children who die within a certain time",
            "the developing world": "the countries with less developed economies",
            "environmental resources": "things in nature that people can use, like water, plants and oil",
            "an estimate": "a guess at the size or number of something",
            "fertility rate": "the average number of babies each woman has",
            "an incentive": "something that encourages you to do something",
            "primary education": "school for young children (in the US: elementary school)",
            "secondary education": "school for teenagers (in the US: middle and high school)"}
    order = [3, 6, 0, 5, 7, 2, 4, 1]
    kwl = "".join(f'<li>{A(words[i], "min-width:32mm")} <span style="color:#6b7377">= {defs[words[i]]}</span></li>' for i in order)
    b.page(f"""{sec(1, "Warm-up: more and more people", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["Is your city crowded? Where and when do you notice it most?", "The world population is growing. What problems could this cause in the future?", "How many brothers and sisters do you have? And your parents?"], "START TALKING")}</div></div>
{sub("A", "Key words. Write the words from the box next to their meanings.", "3 min")}
<div class="bank">{" · ".join(sorted(words, key=lambda w: w.replace("the ", "").replace("an ", "")))}</div>
<ol style="font-size:8.5pt;line-height:1.65;margin:0">{kwl}</ol>
{talk(["What incentives could encourage people to live in smaller towns?", "Which environmental resources worry you most: water, energy or land?"], "USE THE WORDS")}""",
    30, """<ol><li>Top box: 3 minutes. Possible problems: pollution, traffic, housing, competition for water, food and land. Accept opinions; there is no need to know real numbers.</li>
<li>A: 4 minutes with the questions. In American English, <i>primary school</i> is <i>elementary school</i>, and <i>secondary school</i> is <i>middle school</i> and <i>high school</i>.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Gap Year Diaries: families getting smaller and cities getting bigger, with Ana and Mrs. Lima · table · questions · Talk about it",
                      "the future perfect: will have + past participle; by, by the time, by then, in; future perfect vs future continuous; by vs until", "Choose the correct form · complete · Use it (oral)",
                      "'ll have (53.2) · predicting the future · possible or unlikely? (first and second conditional review) · long turn: your city in 2050", "Danny's email to his mom · rewrite · watch out · writing: my life in 2040"),
        """The Linguahouse lesson is a 2008 newspaper article with population statistics, UN estimates and a real professor's research, followed by first and second conditionals. We did not use the article (we cannot check its numbers), and the conditionals were already studied, so we added a Gap Year Diaries episode and a new B1 grammar point: the future perfect. Story: Mrs. Lima grew up with seven brothers and sisters above her father's bakery; she has two children and one grandchild. Grandma Lourdes had ten brothers and sisters; Ana's mother had two children (Ana and Paulo); Ana has one son. Reasons: cost, housing isn't affordable, women study and work longer, small apartments. Predictions: São Paulo will have grown; maybe people will have moved to smaller towns. By 2050 Mrs. Lima will have celebrated her ninetieth birthday; Danny will have learned perfect Portuguese (Ana: don't make promises you can't keep). The Linguahouse conditional practice is a speaking review on page 5.""",
        """<i>By 2050, the population will grow</i> (→ <i>will have grown</i>); <i>By the time you will arrive</i> (→ <i>arrive</i>); <i>by</i> vs <i>until</i>. Vocabulary: <i>fewer children</i> (not <i>less</i>); <i>growing up</i> for a population (→ <i>growing / going up</i>). Pronunciation: <i>I'll have</i> = /aɪləv/.""",
        "Track 53.1 Gap Year Diaries: big families, small families (natural and slow; Danny, Ana and Mrs. Lima) · Track 53.2 Repeat: will have done"))

    # Page 2 - Listening
    rows = [("Mrs. Lima's family", "seven brothers and sisters; now two children and one grandchild"),
            ("Ana's family", "grandmother: ten brothers and sisters; mother: two children; Ana: one son"),
            ("why families are smaller", "cost, housing isn't affordable, women study and work longer, small apartments in big cities"),
            ("São Paulo in the future", "bigger, worse traffic, or people will have moved to smaller towns")]
    rt = "".join(f'<tr><td style="width:34mm"><b>{r}</b></td><td>{A(a, "min-width:86mm")}</td></tr>' for r, a in rows)
    qs = [("Where did Mrs. Lima's family live?", "In a small house above her father's bakery."),
          ("Why might people move to smaller towns, according to Mrs. Lima?", "Many young people work from home now."),
          ("What will Mrs. Lima have done by 2050?", "She'll have celebrated her ninetieth birthday."),
          ("What does Danny promise?", "By 2050 he'll have learned perfect Portuguese.")]
    ql = "".join(f"<li>{q} {A(a, 'min-width:40mm')}</li>" for q, a in qs)
    b.page(f"""{sec(2, "Listening: big families, small families", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Danny talks to Ana and Mrs. Lima. Listen and complete the notes.", "5 min")}
<table style="font-size:8.3pt;margin:.5mm 0">{rt}</table></div>{img('B', 32, 30)}</div>
{audiocard(["53.1 · NATURAL", "53.1 · SLOW"])}
{sub("B", "Listen again and answer.", "3 min")}
<ol style="line-height:1.5;font-size:8.6pt;margin:0">{ql}</ol>
<p style="margin:.6mm 0;font-size:8.6pt"><b>Think about it:</b> Ana says "Don't make promises you can't keep!" Why does she say that to Danny? {A("open answer: perfect Portuguese is very difficult; she's joking with him", "min-width:20mm")}</p>
<div class="box sand" style="margin:.8mm 0;font-size:8.3pt"><h4>NOTICE: USEFUL CHUNKS</h4>housing isn't <b>affordable</b> · <b>cope with</b> a change · a <b>shift</b> to smaller towns · have children <b>later</b> · <b>raising</b> a child is expensive</div>
{talk(["Is your family bigger or smaller than your grandparents' family?", "Do you agree with Ana's reasons? Can you add another one?", "Would you move to a smaller town if you could work from home?"])}""",
    30, """<ol><li>A: play the natural version; play the slow one if needed. Accept short notes.</li>
<li>B: ask the student to find <i>will have</i> + past participle: <i>will have grown, will have gotten worse, will have moved, we'll have found, I'll have celebrated, I'll have learned</i>. They come back on page 3.</li>
<li>Talk about it: 4 minutes.</li></ol>""")

    # Page 3
    lean.grammar_in_class(b, grammar_ref.future_perfect)

    # Page 4 - Practice
    pc = [("By 2050, the city", ["will grow", "will have grown"], "will have grown", "a lot."), ("By the time you", ["arrive", "will arrive"], "arrive", ", we'll have eaten."),
          ("I'll have finished the report", ["by", "until"], "by", "Friday."), ("At nine tonight, I", ["'ll be watching", "'ll have watched"], "'ll be watching", "the game."),
          ("", ["Will you have finished", "Will you finish"], "Will you have finished", "by six?"), ("They", ["won't have", "won't"], "won't have", "arrived yet."),
          ("I'll stay at the hostel", ["by", "until"], "until", "December."), ("In ten years, I", ["'ll have paid", "'ll have pay"], "'ll have paid", "for my apartment.")]
    cl = "".join(f"<li>{a + ' ' if a else ''}{ch(o, r)}{'' if z.startswith(',') else ' '}{z}</li>" for a, o, r, z in pc)
    cp = [("By the end of this year, Danny", "learn", "will have learned", "a lot of Portuguese."), ("By the time Leo finishes school, Ana", "work", "will have worked", "at the hospital for twenty years."),
          ("I hope we", "find", "will have found", "a solution by then."), ("By next month, Mrs. Lima", "not / paint", "won't have painted", "the hostel.")]
    cpl = "".join(f'<li>{a} {A(r, "min-width:30mm")} ({v}) {z}</li>' for a, v, r, z in cp)
    use = ["What will you have done by the end of this year?", "By the time you're sixty, what will you have achieved?",
           "What won't you have finished by the end of this week?", "In ten years, how will your city have changed?",
           "By 2050, what will people have stopped doing?"]
    b.page(f"""{sec(4, "Practice: by then, we'll have…", "10 min")}
{sub("A", "Choose the correct words.", "3 min")}
<ol style="line-height:1.7;font-size:8.6pt;margin:0;columns:2;column-gap:6mm">{cl}</ol>
{sub("B", "Complete with the future perfect of the verb in brackets.", "4 min")}
<ol style="line-height:1.6;font-size:8.6pt;margin:0">{cpl}</ol>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    30, """<ol><li>A: 3 minutes. Item 4 is the future continuous (in progress at nine). Item 7: <i>until</i>, because the stay continues up to December.</li>
<li>B: accept the contracted forms (<i>'ll have learned</i>).</li>
<li>Use it: 3 minutes, all oral. Answer one question about yourself first as a model.</li></ol>""")

    # Page 5 - Speaking
    sits = ["It will rain this weekend.", "You will have a vacation next month.", "You speak ten languages.", "You will win the lottery.",
            "Brazil will win the next World Cup.", "You will go out with friends tonight.", "You will live in another country.", "You will become fluent in English."]
    sl = "".join(f"<li>{s}</li>" for s in sits)
    b.page(f"""{sec(5, "Speaking: the future of our cities", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE: PREDICTING THE FUTURE</h4>
<table style="margin:0;font-size:8.2pt"><tr><th>sure</th><th>probable</th><th>not sure</th><th>looking back from the future</th></tr>
<tr><td><i>It will definitely… · There's no doubt that…</i></td><td><i>It will probably… · It's likely to… · I expect…</i></td><td><i>It might… · I doubt that… · It's hard to say.</i></td><td><i>By 2050, we'll have… · By the time…, … won't have…</i></td></tr></table></div>
{audiocard(["53.2"])}
{sub("A", "Listen and repeat. Say 'll have as one short sound: I'll have /aɪləv/.", "2 min", "53.2")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S532))}</p>
{sub("B", "Possible or unlikely? For each situation, make a first or a second conditional sentence about you.", "5 min")}
<p class="small" style="margin:.3mm 0"><i>It will rain this weekend. → If it rains this weekend, I won't go to the beach. · You speak ten languages. → If I spoke ten languages, I'd work as a translator.</i></p>
<ol style="font-size:8.6pt;line-height:1.55;margin:0;columns:2;column-gap:6mm">{sl}</ol>
{sub("C", "Discuss. Are any parts of your city overcrowded? Are people having more or fewer children than in the past? Why?", "4 min")}
{sub("D", "Long turn. Your city in 2050. What will have changed? What will people have stopped doing? What won't have changed?", "4 min")}
<p style="margin:.3mm 0;font-size:8.5pt">Plan (1 min): {lines(1)}</p>""",
    30, """<ol><li>B comes from the Linguahouse conditional practice: the student decides if each situation is possible (first conditional) or unlikely or impossible (second conditional). Answers depend on the student.</li>
<li>C comes from the Linguahouse talking point. D: 1 minute to plan, 2 minutes to talk, with at least three future perfect sentences. Last 3 minutes: wrap-up (two corrections, and ask <i>Can you now say what will have happened by a future time?</i>).</li></ol>""")

    # Homework
    pc2 = [(["will have saved", "will save"], "will have saved"), (["finish", "will finish"], "finish"), (["by", "until"], "by"),
           (["'ll be finishing", "'ll have finished"], "'ll have finished"), (["won't have", "don't have"], "won't have"), (["until", "by"], "until")]
    p = [ch(o, a) for o, a in pc2]
    rw2 = [("I'll finish my course in June. (by July)", "By July, I'll have finished my course."),
           ("Ana will work at the hospital for twenty years next year. (by next year)", "By next year, Ana will have worked at the hospital for twenty years."),
           ("Danny won't learn perfect Portuguese before 2050. (by 2050)", "By 2050, Danny won't have learned perfect Portuguese.")]
    rwl2 = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw2)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Danny writes to his mom about his plans. Choose the correct words.", "")}</div>{img('C', 30, 19)}</div>
<div class="box" style="line-height:1.85;font-size:8.8pt;margin:.5mm 0"><b>Hi Mom!</b> Big news: I'm staying in São Paulo until the end of the year. By December, I {p[0]} enough money for a trip to the Amazon. By the time I {p[1]} my contract at the language school, I'll have taught more than two hundred classes! I need to send some documents to the school {p[2]} the end of the month. By Christmas, I {p[3]} my Portuguese course! Don't worry: I {p[4]} forgotten your birthday. I'll call you on Sunday, and I'll stay online {p[5]} you go to bed. Love, Danny</div>
{sub("B", "Rewrite the sentences with the future perfect and the words in brackets.", "")}
<ol style="line-height:1.5;font-size:8.7pt;margin:0">{rwl2}</ol>
{lean.watch_out([("The population of Brazil is growing up.", "The population of Brazil is growing / going up.", "people <i>grow up</i>; numbers <i>grow</i> or <i>go up</i>."), ("Today people have less children.", "Today people have fewer children.", "<i>fewer</i> + plural nouns; <i>less</i> + uncountable nouns."), ("A big part of the people live in cities.", "Most people / A large part of the population live in cities.", "<i>a large part of the population</i>; or simply <i>most people</i>.")])}
{lean.writing_task(sub, "Write a post for Danny's podcast page: my life in 2040. What will you have done? What won't you have done?", "By 2040, I'll have…", ["three things you'll have done", "one thing you won't have done", "how your city will have changed", "by, by the time, by then", "100–150 words"], "I can talk about population and family size, and say what will have happened by a future time.")}""",
    25, """<p>Check A and B in 3 minutes at the start of the next class. In A, the first <i>by December</i> takes the future perfect; the last gap is <i>until</i> because Danny stays online up to that moment. Read the writing at home and choose two mistakes to discuss in class.</p>""")

    script = "".join(f"<p style='margin:.5mm 0'><b>{s}:</b> {t}</p>" for s, t in S531)
    b.extra("Audio script", f"""
{sub("53.1", "Gap Year Diaries: big families, small families (natural and slow; Danny, Ana and Mrs. Lima)")}
<div style="line-height:1.3;font-size:8.2pt">{script}</div>
{sub("53.2", "Repeat: will have done")}
<p>{" · ".join(S532)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 53 - Population science")
