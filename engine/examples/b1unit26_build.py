# Speak! Progress B1 - Unit 26 "Extreme living" (all English) - lean B1 format
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
setup(band="B1 · UNIT 26", audio_json="audio_b1-unit-26.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-26"]
_n = [("three hundred and fifty-five thousand", "355,000"), ("minus thirty-five degrees Celsius", "–35 °C (–31 °F)"), ("forty-five degrees", "45 °C (113 °F)"),
      ("twenty-three to twenty-five degrees", "23–25 °C (73–77 °F)"), ("five thousand one hundred meters", "5,100 meters (16,700 feet)")]
def _num(s):
    for k, v in _n:
        s = s.replace(k, v)
    return s
S261 = [_num(l.split(": ", 1)[1]) for l in _r["26.1 Life at the extremes"].split("\n")]
S262 = [x.split(": ", 1)[1] for x in _r["26.2 Repeat: used to"].split("\n")]


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
    cover = cover_html(T, "LEVEL B1 · UNIT 26", "Extreme living", "Life in the coldest, hottest and highest places · <b>be used to, get used to</b>",
                       [("YOU CAN", "talk about extreme places and climates, and about getting used to a new situation"),
                        ("LANGUAGE", "nippy · frostbite · hardy · cope with · I'm used to the cold · You'll get used to it"),
                        ("PRONUNCIATION", "used to /ˈjuːstə/")])
    kw = [("quite cold (informal)", "nippy"), ("a condition where extreme cold damages parts of the body", "frostbite"),
          ("difficult, needing careful attention", "tricky"), ("strong, able to live in difficult conditions", "hardy"),
          ("to deal with a difficult situation", "cope with"), ("the country where you were born", "homeland")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:20mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Warm-up: hot, cold, high", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["Describe the weather today. Is it comfortable?", "What's the coldest or hottest place you've ever been to?", "Do you prefer hot weather or cold weather? Why?"], "START TALKING")}</div></div>
{sub("A", "Key words. Write the words from the box next to the definitions.", "3 min")}
<div class="bank">cope with · frostbite · hardy · homeland · nippy · tricky</div>
<div style="font-size:8.7pt">{twocol(kwl, 3)}</div>
{talk(["How do you cope with very hot days?", "Is it nippy where you live in winter? What's tricky about the weather there?"], "USE THE WORDS")}""",
    26, """<ol><li>Start with the questions in the top box: this is speaking time, not a test. 4 minutes. Push for more than <i>hot / cold</i>: <i>mild, humid, sticky, freezing, foggy</i>.</li>
<li>A: quick check (3 minutes), then the two questions. <i>Nippy</i> is informal British and American; <i>cope with</i> is very common.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Article: three extreme places · predict and check · which place? · Talk about it",
                      "used to + verb, be used to / get used to + noun or -ing", "Complete, choose · Use it (oral)",
                      "used to (26.2) · role-play: a job offer in an extreme place", "Danny's email to Rita · rewrite · word choice · writing", "Reading"),
        """The Linguahouse lesson is an adapted newspaper article about Yakutsk (2008). We wrote an original article about three extreme places, read by the Host. In the homework, Danny writes to his mom Rita about getting used to life in São Paulo before his trip south. Verified facts: Yakutsk had 355,443 people in the 2021 census; it is the coldest major city; January averages are around –38 °C; the city is built on permafrost and buildings stand on deep piles (Wikipedia, Yakutsk). Coober Pedy, South Australia, is an opal-mining town where summer can pass 45 °C; about half of the residents live in dugouts that stay at about 23–25 °C all year (estimates range from 50% to 80%; we use the lower one) (Outlook Traveller; Mining Technology; Yahoo News). La Rinconada, Peru, at about 5,100 m, is the highest permanent settlement (Guinness World Records); its economy is gold mining, and the air has about half the oxygen pressure of sea level (Live Science; Wikipedia).""",
        """<i>I'm used to wake up</i> (infinitive after <i>be used to</i>), <i>I use to…</i> for present habits, <i>used with</i>, and <i>It's making cold</i>. Pronunciation: <i>used to</i> with a z sound.""",
        "Track 26.1 Life at the extremes (natural and slow) · Track 26.2 Repeat: used to"))

    # Page 2 - Reading
    pq = [("Yakutsk has about ___ people.", ["35,000", "355,000", "3.5 million"], "355,000"),
          ("In January, the average temperature in Yakutsk is below ___.", ["–5 °C", "–15 °C", "–35 °C"], "–35 °C"),
          ("In Coober Pedy, about ___ of the people live underground.", ["10%", "half", "all"], "half"),
          ("La Rinconada is about ___ above sea level.", ["2,100 m", "3,600 m", "5,100 m"], "5,100 m")]
    pql = "".join(f"<li>{q.replace('___', '___')} {ch(o, a)}</li>" for q, o, a in pq)
    wp = [("Buildings stand on concrete piles.", "Y"), ("People live in homes cut into the rock.", "C"), ("Newcomers often get headaches.", "L"),
          ("Wearing glasses outside can be tricky.", "Y"), ("Many people work in gold mines.", "L"), ("Homes stay cool without air conditioning.", "C")]
    wpl = "".join(f"<li>{s} {A(w, 'min-width:6mm')}</li>" for s, w in wp)
    title = S261[0].split(". ", 1)[0]
    paras = [S261[0].split(". ", 1)[1]] + S261[1:]
    def bold_head(p):
        h, rest = p.split(": ", 1)[0], p.split(": ", 1)[1] if ": " in p else ""
        return f"<b>{h}:</b> {rest}" if rest and len(h) < 30 else p
    art = "".join(f"<p style='margin:0 0 1mm'>{bold_head(p) if i in (1, 2, 3) else p}</p>" for i, p in enumerate(paras))
    b.page(f"""{sec(2, "Reading: life at the extremes", "12 min")}
{sub("A", "Before you read. Guess the answers. Then read the article and check.", "4 min")}
<ol style="line-height:1.45;font-size:8.4pt;margin:0;columns:2">{pql}</ol>
<div class="box" style="margin:.5mm 0 0;font-size:7.9pt;line-height:1.32;column-count:2;column-gap:4mm"><b style="font-size:9.5pt">{title}</b><br>{art}</div>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("B", "Which place is it? Write Y (Yakutsk), C (Coober Pedy) or L (La Rinconada).", "3 min")}
<ol style="line-height:1.4;font-size:8.4pt;margin:0;columns:2">{wpl}</ol></div>{img('B', 34, 22)}</div>
{audiocard(["26.1 · NATURAL", "26.1 · SLOW"])}
{talk(["Which of the three places could you get used to? Which one never?", "Why do you think people stay in places like these?", "How does the climate in your country compare?"])}""",
    24, """<ol><li>A–B: 7 minutes. Let the student guess first, then read (they can listen to 26.1 at home). All figures are verified (see the story box).</li>
<li>Talk about it: 5 minutes. Collect the student's sentences with <i>get used to</i> for page 3.</li></ol>""")

    # Page 3 - Grammar reference
    lean.grammar_in_class(b, grammar_ref.be_get_used_to)

    # Page 4 - Practice
    fs = [("If you moved to Yakutsk, you'd have to ___ wearing several layers of clothes.", "get used to"), ("The locals are hardy people, and most of them ___ the cold.", "are used to"),
          ("For visitors, it can take a while to ___ it.", "get used to"), ("Some people never ___ it.", "get used to"),
          ("Before she moved to Yakutsk, my friend ___ live in Rio.", "used to")]
    fsl = "".join(f"<li><i>{s.replace('___', A(a, 'min-width:20mm'))}</i></li>" for s, a in fs)
    use = ["What did you use to do as a child that you don't do now?", "What are you used to doing every morning?", "What was difficult to get used to in your job or studies?",
           "What could you never get used to?", "Imagine you move to another country. What will you have to get used to?"]
    b.page(f"""{sec(4, "Practice: used to, be used to, get used to", "10 min")}
{sub("A", "Complete the sentences from the article with used to, are used to or get used to.", "3 min")}
<div class="bank">are used to · get used to · used to</div>
<ol style="line-height:1.85;font-size:8.9pt;margin:0">{fsl}</ol>
{sub("B", "Choose.", "2 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0"><li>I'm not used to {ch(["wear", "wearing"], "wearing")} so many clothes.</li>
<li>I {ch(["usually", "use to"], "usually")} wake up at seven.</li>
<li>Don't worry. You'll {ch(["get", "be"], "get")} used to the heat after a week.</li></ol>
<div class="box sand"><h4>RULE</h4><b>used to + verb</b> = past habit · <b>be used to + noun / -ing</b> = it's normal for me · <b>get used to + noun / -ing</b> = it's becoming normal · present habits: <b>usually</b>. See the <b>Grammar reference</b> on page 3.</div>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    24, """<ol><li>A–B: 4 minutes. After <i>be / get used to</i>, check the -ing form every time.</li>
<li>Use it: 6 minutes, all oral. Ask a follow-up question each time (<i>How long did it take?</i>). Correct <i>I use to</i> for present habits.</li></ol>""")

    # Page 5 - Speaking
    jobs = [("Yakutsk", "engineer on a building site", "salary: double · free apartment · very short days in winter"),
            ("Coober Pedy", "manager of an underground hotel", "salary: 50% more · free dugout home · far from any big city"),
            ("La Rinconada", "doctor at the health center", "salary: 70% more · very little oxygen · basic housing")]
    jl = "".join(f'<div class="box" style="flex:1;margin:0;font-size:8.2pt"><b>{p}</b><br><i>{j}</i><br><span class="small">{d}</span></div>' for p, j, d in jobs)
    b.page(f"""{sec(5, "Speaking: could you get used to it?", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.3pt"><tr><th>worries</th><th>reassuring</th><th>asking</th><th>deciding</th></tr>
<tr><td><i>I'm not used to… · I don't think I could get used to… · What worries me is…</i></td><td><i>Don't worry, you'll get used to it. · It's not as bad as it sounds. · Most people cope with it.</i></td><td><i>How long does it take to get used to…? · What's it like in winter / summer?</i></td><td><i>I'd give it a try. · It's not for me. · I'll think about it.</i></td></tr></table></div>
{audiocard(["26.2"])}
{sub("A", "Listen and repeat. Say &ldquo;used to&rdquo; as one word: /ˈjuːstə/. Then say which sentence is a past habit.", "4 min", "26.2")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S262))}</p>
{sub("B", "Role-play. A company offers you one of these jobs for a year. Your teacher is the recruiter and tries to convince you. Ask questions, say what you'd have to get used to, and decide.", "14 min")}
<div style="display:flex;gap:2mm;margin-top:1mm">{jl}</div>
{talk(["What's the biggest change you've had to get used to in your life?", "Would you leave your homeland for a very good job? Why or why not?"], "TALK ABOUT IT")}""",
    32, """<ol><li>A: sentence 5 (<i>I used to live in Rio</i>) is a past habit. All the others are <i>be / get used to</i>. Check the /s/ sound.</li>
<li>B: 12 minutes. Salaries and conditions on the cards are invented for the role-play. As the recruiter, answer worries with <i>You'll get used to it</i> and add good points (salary, adventure). Do two jobs if time allows. Last 3 minutes: wrap-up (two corrections, and ask <i>Can you now talk about getting used to a new situation?</i>).</li></ol>""")

    # Homework
    pc = [(["used to", "am used to"], "used to"), (["getting", "get"], "getting"), (["eating", "eat"], "eating"), (["get", "be"], "get"), (["usually", "use to"], "usually")]
    p = [ch(o, a) for o, a in pc]
    rw = [("Living in a big city is normal for me now. (be used to)", "I'm used to living in a big city."),
          ("I wore glasses when I was a child, but I don't now. (used to)", "I used to wear glasses when I was a child."),
          ("Waking up at 5 a.m. is slowly becoming normal for me. (get used to)", "I'm getting used to waking up at 5 a.m.")]
    rwl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Danny writes to his mom, Rita, before his trip south. Choose the correct words.", "")}</div>{img('C', 28, 18)}</div>
<div class="box" style="line-height:1.85;font-size:8.8pt;margin:.5mm 0"><b>Hi Mom,</b><br>Don't worry, I'm fine! When I arrived, I {p[0]} get lost every day, but now I know the city well. I'm {p[1]} used to the traffic, and I'm used to {p[2]} rice and beans almost every day. I love it! The hardest thing was the greetings: people kiss on the cheek here. It took me weeks to {p[3]} used to it. Now I {p[4]} do it without thinking. Patagonia is next, and it'll be nippy there. Bruno says I'll cope. Love, Danny</div>
{sub("B", "Rewrite the sentences with the words in brackets.", "")}
<ol style="line-height:1.5;font-size:8.7pt;margin:0">{rwl}</ol>
{lean.watch_out([("It's making cold today.", "It's cold today.", "for weather, use <i>be</i>: <i>it's cold / hot / windy</i>."), ("The climate is very hot today.", "The weather is very hot today.", "<i>weather</i> = today; <i>climate</i> = the usual weather of a place."), ("I'm used to with the heat.", "I'm used to the heat.", "no <i>with</i>; <i>to</i> + noun or -ing.")])}
{lean.writing_task(sub, "Describe a big change in your life (a new city, job, school or home). What did you have to get used to? What are you still not used to?", "When I moved to…, I had to get used to…", ["used to", "be used to", "get used to", "two key words from page 1", "100–150 words"], "I can talk about getting used to a new situation.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class. Read the writing at home and choose two mistakes to discuss in class.</p>""")

    script = "".join(f"<p style='margin:.5mm 0'>{l}</p>" for l in S261)
    b.extra("Audio script", f"""
{sub("26.1", "Life at the extremes (natural and slow; read by the Host)")}
<div style="line-height:1.3;font-size:8.6pt">{script}</div>
{sub("26.2", "Repeat: used to")}
<p>{" · ".join(S262)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 26 - Extreme living")
