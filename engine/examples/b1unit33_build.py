# Speak! Progress B1 - Unit 33 "Metro stress" (all English) - lean B1 format
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
setup(band="B1 · UNIT 33", audio_json="audio_b1-unit-33.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-33"]
_n = [("two thousand fourteen", "2014"), ("two thousand four", "2004"), ("nine hundred and nine", "909"), ("sixty thousand", "60,000"),
      ("sixty-one and ninety minutes", "61 and 90 minutes")]
def _num(s):
    for k, v in _n:
        s = s.replace(k, v)
    return s
S331 = [_num(l.split(": ", 1)[1]) for l in _r["33.1 Is your commute making you unhappy"].split("\n")]
S332 = [x.split(": ", 1)[1] for x in _r["33.2 Repeat: is said to, is thought to"].split("\n")]


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
    cover = cover_html(T, "LEVEL B1 · UNIT 33", "Metro stress", "Is your commute making you unhappy? · <b>It is said that… / is thought to…</b>",
                       [("YOU CAN", "talk about commuting and transport problems, and report what research and experts say"),
                        ("LANGUAGE", "a commuter · rush hour · overcrowding · Commuting is said to be… · It is believed that…"),
                        ("PRONUNCIATION", "weak forms: is said to, is thought to")])
    kw = [("a person who travels regularly to and from work", "a commuter"), ("the busiest time of day on roads and trains", "rush hour"),
          ("when there are too many people in a place", "overcrowding"), ("dirty, with harmful chemicals in the air or water", "polluted"),
          ("a period of work, for example from 7 p.m. to 7 a.m.", "a shift"), ("to hurry, to do something very fast", "rush")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:21mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Warm-up: getting around", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["How do you get around your city? How long does it take you?", "What are the advantages and disadvantages of the way you travel?", "Look at the photo. How do you feel in places like this?"], "START TALKING")}</div></div>
{sub("A", "Key words. Write the words from the box next to the definitions.", "3 min")}
<div class="bank">a commuter · overcrowding · polluted · rush · rush hour · a shift</div>
<div style="font-size:8.7pt">{twocol(kwl, 3)}</div>
{talk(["What time is rush hour in your city? How do you avoid it?", "Is overcrowding or pollution the bigger problem where you live?"], "USE THE WORDS")}""",
    26, """<ol><li>Start with the questions in the top box: 4 minutes.</li>
<li>A: quick check (3 minutes), then the two questions. <i>Rush</i> is a verb (<i>Passengers rush to the doors</i>); <i>rush hour</i> is a noun.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Article: is your commute making you unhappy? · find the information · true or false · Talk about it",
                      "It is said that… / is said to…; expected, believed, thought, found, estimated", "Complete, choose · Use it (oral)",
                      "Weak forms (33.2) · problem-solving: fix your city's transport", "Tom's email from Chicago · rewrite · word choice · writing", "Reading"),
        """The Linguahouse lesson is an article on stress in the Moscow metro (The Independent, 2009) that focuses on suicides; we replaced it with an original article on commuting and well-being, read by the Host, and kept the lesson's grammar (the passive and <i>is expected to</i>). Verified facts: Kahneman, Krueger, Schkade, Schwarz and Stone (Science, 2004) asked 909 working women to reconstruct the previous day; commuting was the least enjoyable activity (University of Michigan; PubMed). The UK Office for National Statistics (2014, about 60,000 people) found commuters had lower life satisfaction and higher anxiety, with the worst effects for journeys of 61–90 minutes and no such effects for three hours or more (ONS via Channel 4 News; IBTimes). Stutzer and Frey (Scandinavian Journal of Economics, 2008) called it the commuting paradox: German workers with longer commutes reported lower life satisfaction. In the homework, Tom (teacher, Chicago) writes to Ana about his new bike commute.""",
        """<i>Is said that…</i> (no <i>it</i>), mixing the two structures (<i>is said that it is</i>), <i>expected rise</i> without <i>to</i>, and the false friend <i>transit</i> for <i>traffic</i> (<i>There was a lot of transit</i>). Pronunciation: <i>is said to</i> /ɪzˈsedtə/ is fast and weak.""",
        "Track 33.1 Is your commute making you unhappy? (natural and slow; read by the Host) · Track 33.2 Repeat: is said to, is thought to"))

    # Page 2 - Reading
    fi = [("the number of women in Kahneman's study", "909"), ("the least enjoyable activity in that study", "commuting"),
          ("the commute time with the worst effects in the UK", "61–90 minutes"), ("the name economists give to this problem", "the commuting paradox")]
    fil = "".join(f"<li>{q} {A(a, 'min-width:24mm')}</li>" for q, a in fi)
    tf = [("Working was less enjoyable than commuting.", "F"), ("UK commuters were more anxious than non-commuters.", "T"), ("People with very long commutes were the unhappiest.", "F"),
          ("A better salary is usually enough to make up for a long commute.", "F")]
    tfl = "".join(f"<li>{s} {A(w, 'min-width:6mm')}</li>" for s, w in tf)
    title = S331[0].rstrip("?") + "?"
    art = "".join(f"<p style='margin:0 0 1mm'>{p}</p>" for p in S331[1:])
    b.page(f"""{sec(2, "Reading: is your commute making you unhappy?", "12 min")}
<div class="box" style="margin:0;font-size:7.9pt;line-height:1.32;column-count:2;column-gap:4mm"><b style="font-size:9.5pt">{title}</b><br>{art}</div>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("A", "Read the article. Find the information.", "3 min")}
<ol style="line-height:1.5;font-size:8.5pt;margin:0">{fil}</ol></div>{img('B', 34, 24)}</div>
{sub("B", "Write T (true) or F (false). Correct the false sentences.", "3 min")}
<ol style="line-height:1.45;font-size:8.5pt;margin:0;columns:2">{tfl}</ol>
{audiocard(["33.1 · NATURAL", "33.1 · SLOW"])}
{talk(["Does the article match your experience? Is commuting the worst part of your day?", "Would you accept a longer commute for a better salary? How much longer?", "How could you make your commute more pleasant?"])}""",
    30, """<ol><li>A–B: 6 minutes. Corrections: 1 commuting was the least enjoyable · 3 the worst was 61–90 minutes; 3 hours or more showed no such effects · 4 the extra money doesn't seem to be enough. All figures are verified (see the story box).</li>
<li>Talk about it: 6 minutes. Note sentences with <i>is said to / was found to</i> in the text for page 3.</li></ol>""")

    # Page 3
    lean.grammar_in_class(b, grammar_ref.passive_reporting)

    # Page 4 - Practice
    fs = [("People often say that commuting is the worst part of the day.", "Commuting is often said to be the worst part of the day."),
          ("Researchers found that commuting was the least enjoyable activity.", "Commuting was found to be the least enjoyable activity."),
          ("People think they use the time to work or relax.", "They are thought to use the time to work or relax."),
          ("People believe that working from home helps.", "It is believed that working from home helps.")]
    fsl = "".join(f'<li><i>{d}</i><br>{A(i, "min-width:90mm")}</li>' for d, i in fs)
    use = ["What is your city said to be famous for?", "What is expected to happen to prices / traffic / the weather next year?", "Tell me something that is believed to be good for your health.",
           "What is your favorite restaurant said to do best?", "Name a place in Brazil that is thought to be dangerous or overcrowded. Is it true?"]
    b.page(f"""{sec(4, "Practice: it is said that, is said to", "10 min")}
{sub("A", "Rewrite the sentences from the article with the passive.", "4 min")}
<ol style="line-height:1.6;font-size:8.9pt;margin:0">{fsl}</ol>
{sub("B", "Choose.", "2 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0"><li>{ch(["Is said", "It is said"], "It is said")} that the metro is faster.</li>
<li>House prices are expected {ch(["fall", "to fall"], "to fall")} next year.</li>
<li>The bridge is said {ch(["to have cost", "to cost"], "to have cost")} millions when it was built.</li></ol>
<div class="box sand"><h4>RULE</h4><b>It is said / believed / expected that</b> + clause · <b>subject + is said / believed / expected to</b> + verb · <b>to have + participle</b> for an earlier action · never drop <i>it</i>. See the <b>Grammar reference</b> on page 3.</div>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    24, """<ol><li>A–B: 6 minutes. In A4, accept <i>Working from home is believed to help.</i> too.</li>
<li>Use it: 4 minutes, all oral. Then ask: <i>Do you think it's true?</i> to move from reporting to opinion.</li></ol>""")

    # Page 5 - Speaking
    sol = ["more bus lanes", "free public transport for students and retirees", "a charge for cars in the city center", "more bike lanes and shared bikes",
           "companies let people work from home two days a week", "trains every 2 minutes at rush hour", "more trees and less pollution", "start school and work at different times"]
    sl = "".join(f"<li>{x}</li>" for x in sol)
    b.page(f"""{sec(5, "Speaking: fix your city's transport", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.3pt"><tr><th>describing a problem</th><th>reporting</th><th>suggesting</th><th>objecting</th></tr>
<tr><td><i>The main problem is… · At rush hour, … · It takes forever to…</i></td><td><i>It is said that… · … is expected to… · It's believed to reduce…</i></td><td><i>What we need is… · One solution would be to… · Why don't we…?</i></td><td><i>That would be too expensive. · Who's going to pay for it? · That won't work because…</i></td></tr></table></div>
{audiocard(["33.2"])}
{sub("A", "Listen and repeat. Say &ldquo;is said to&rdquo; and &ldquo;is thought to&rdquo; quickly, like one word.", "4 min", "33.2")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S332))}</p>
{sub("B", "You are on your city council. First, describe the three biggest transport problems in your city. Then choose the three best solutions from the list and defend them. Your teacher is a council member who disagrees.", "14 min")}
<ol style="line-height:1.45;font-size:8.8pt;margin:0;columns:2">{sl}</ol>
{talk(["Should cars be banned from city centers? Why or why not?", "Is working from home the best solution to traffic? Who can't do it?"], "TALK ABOUT IT")}""",
    32, """<ol><li>A: the stress is on the participle (<i>SAID, THOUGHT, BElieved</i>); <i>is</i> and <i>to</i> are weak.</li>
<li>B: 12 minutes. Object to each solution (cost, who pays, it won't work in Brazil). Push the student to report support with the passive (<i>It is said to reduce traffic in other cities</i>). Last 3 minutes: wrap-up (two corrections, and ask <i>Can you now report what experts say about a problem?</i>).</li></ol>""")

    # Homework
    pc = [(["is said", "says"], "is said"), (["to be", "be"], "to be"), (["It is", "Is"], "It is"), (["to have", "have"], "to have"), (["expected", "expecting"], "expected")]
    p = [ch(o, a) for o, a in pc]
    rw = [("People say the L is the fastest way to get downtown. (is said to)", "The L is said to be the fastest way to get downtown."),
          ("Experts expect that traffic will get worse. (It is expected)", "It is expected that traffic will get worse."),
          ("People believe that cycling reduces stress. (is believed to)", "Cycling is believed to reduce stress.")]
    rwl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Tom writes to Ana from Chicago about his new way of getting to work. Choose the correct words.", "")}</div>{img('C', 28, 18)}</div>
<div class="box" style="line-height:1.85;font-size:8.8pt;margin:.5mm 0"><b>Hi Ana,</b><br>Guess what? I've started cycling to school! Driving downtown {p[0]} to be the most stressful way to travel here, and I agree. The train is said {p[1]} faster, but at rush hour it's packed. {p[2]} believed that cyclists arrive at work in a better mood, and so far that's true for me. My neighbor is said {p[3]} cycled to work for 30 years, even in winter! More bike lanes are {p[4]} to open next year. How's your commute to the hospital? Tom</div>
{sub("B", "Rewrite the sentences with the words in brackets.", "")}
<ol style="line-height:1.5;font-size:8.7pt;margin:0">{rwl}</ol>
{lean.watch_out([("There was a lot of transit today.", "There was a lot of traffic today. / There was a traffic jam.", "<i>transit</i> = public transportation in the US."), ("I take two hours in the traffic.", "I spend two hours in traffic. / It takes me two hours.", "<i>spend</i> time; <i>it takes me</i> + time."), ("I'm going to the work.", "I'm going to work.", "no <i>the</i> with work, school, home.")])}
{lean.writing_task(sub, "What are the main problems with getting around your city? What could be done to solve them? Use the passive to report what people or experts say.", "In my city, getting to work is said to be…", ["two problems", "two solutions", "three passive reporting structures", "your opinion", "100–150 words"], "I can talk about transport problems and report what experts say.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class. <i>The L</i> is Chicago's train system. The writing task is the Linguahouse talking point. Read it at home and choose two mistakes to discuss in class.</p>""")

    script = "".join(f"<p style='margin:.5mm 0'>{l}</p>" for l in S331)
    b.extra("Audio script", f"""
{sub("33.1", "Is your commute making you unhappy? (natural and slow; read by the Host)")}
<div style="line-height:1.3;font-size:8.6pt">{script}</div>
{sub("33.2", "Repeat: is said to, is thought to")}
<p>{" · ".join(S332)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 33 - Metro stress")
