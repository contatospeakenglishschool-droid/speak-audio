# Speak! Progress B1 - Unit 11 "Relationships and dating" (all English) - lean B1 format (rebuilt 2026-11-19)
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

    # 1 Warm-up
    cover = cover_html(T, "LEVEL B1 · UNIT 11", "Relationships and dating", "Love stories · <b>the past perfect</b>",
                       [("YOU CAN", "talk about relationships and dating and tell the story of a couple"),
                        ("LANGUAGE", "ask someone out · split up · make up · a long-distance relationship · He had just moved here."),
                        ("PRONUNCIATION", "contracted had ('d)")])
    kw = [("a romantic meeting, for example dinner or the movies", "a date"), ("when someone asks their partner to marry them", "a proposal"),
          ("the ceremony and party when two people get married", "a wedding"), ("a vacation for two people who have just gotten married", "a honeymoon"),
          ("the same date, every year, after an important event", "an anniversary"), ("the end of a romantic relationship", "a break-up")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:22mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Warm-up: love stories", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["Look at the photo. How long do you think this couple has been together?", "Do you know a couple with a great love story?", "Is dating easier or harder today than 40 years ago? Why?"], "START TALKING")}</div></div>
{sub("A", "Key words. Relationship events. Write the words from the box next to the definitions.", "3 min")}
<div class="bank">an anniversary · a break-up · a date · a honeymoon · a proposal · a wedding</div>
<div style="font-size:8.6pt">{twocol(kwl, 3)}</div>
{talk(["Put the events in A in a typical order. Is there a typical order today?", "What's the best place for a honeymoon? Why?"], "USE THE WORDS")}""",
    26, """<ol><li>Top box: keep it light and general; the student doesn't need to talk about their own relationships unless they want to.</li>
<li>A: pronunciation <i>anniVERsary</i>, <i>HONeymoon</i>. Possible order: date, proposal, wedding, honeymoon, anniversary.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Podcast: Mrs. Lima's love story · order of events · Talk about it", "The past perfect",
                      "Which happened first? · choose the rule · Use it (oral)", "Functional language · contracted had (11.2) · relationship advice role-play",
                      "Kate's blog: a love story · describing relationships · word choice · writing"),
        "The Linguahouse lesson is vocabulary only. Our listening is a new episode of Danny's podcast <i>Gap Year Diaries</i> (B1 Unit 06). Mrs. Lima, the owner of Danny's hostel, speaks for the first time (en-US-Chirp3-HD-Vindemiatrix). She met her husband in 1978 at her father's bakery in São Paulo; he had just moved from Recife. Two years of long-distance relationship (he worked in Manaus), one break-up, a proposal at the bus station in 1982, a wedding the next year, 36 years of marriage, two children, the hostel; he died six years ago. Her story is fictional. At the end we learn that Bruno has asked out Paula, from the running group. Kate's blog (homework) continues the wedding cake she dropped in B1 Unit 02.",
        "Students say <i>married with</i> (married <b>to</b>), <i>date with someone</i> (date someone), use <i>date</i> for a doctor's <i>appointment</i>, and either avoid the past perfect or overuse it for every past action.",
        "Track 11.1 Gap Year Diaries: a love story (natural and slow) · Track 11.2 Repeat: contracted had"))

    # 2 Listening
    gist = ["how Mrs. Lima opened her hostel", "how Mrs. Lima met and married her husband", "how young people date with apps"]
    ev = [("He moved to Manaus.", "4"), ("They opened the hostel.", "7"), ("He moved to São Paulo from Recife.", "1"), ("They split up for a while.", "5"),
          ("He asked her out.", "3"), ("He bought about 200 bread rolls.", "2"), ("He proposed at the bus station.", "6")]
    evl = [f'<li value="{i+1}">{A(n, "min-width:6mm")} {s}</li>' for i, (s, n) in enumerate(ev)]
    b.page(f"""{sec(2, "Listening: a love story", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{audiocard(["11.1 · NATURAL", "11.1 · SLOW"])}
{sub("A", "Listen to Danny's podcast. What is it mainly about? Choose.", "2 min", "11.1")}
<p style="margin:.3mm 0;font-size:8.9pt">{ch(gist, gist[1])}</p></div>{img('B', 40, 27)}</div>
{sub("B", "Listen again. Number the events in the order they happened (1–7).", "4 min")}
<ol style="line-height:1.5;font-size:8.8pt;margin:0;column-count:2">{"".join(evl)}</ol>
{talk(["Why does Mrs. Lima still buy one bread roll on every anniversary?", "&ldquo;He'd ironed a shirt.&rdquo; How does Mrs. Lima know that Bruno likes Paula?", "&ldquo;Never go to bed angry.&rdquo; Is it good advice? Why?"])}""",
    26, """<ol><li>A–B: 6 minutes. The order of events is not the order in the story: <i>He had just moved</i> and <i>had bought 200 rolls</i> are told later but happened earlier. This prepares the grammar.</li>
<li>Talk about it: 6 minutes. 1: it's how they met; it keeps the memory alive. 2: Bruno never irons anything.</li></ol>""")

    # 3 Grammar reference
    lean.grammar_in_class(b, grammar_ref.past_perfect)

    # 4 Practice
    fs = [("When he started coming to the bakery, he <u>had just moved</u> from Recife.", "he moved"),
          ("By the time he asked me out, he <u>had bought</u> about 200 bread rolls.", "he bought the rolls"),
          ("I thought he <u>had found</u> another girl.", "(she thought) he found a girl")]
    fsl = "".join(f"<li>{s} {A('first: ' + a, 'min-width:30mm')}</li>" for s, a in fs)
    use = ["Tell me something you had never done before you were 18.", "When you got to class / work today, what had already happened?", "Tell me about a time you were late. What had happened?",
           "By the time you were 15, had you traveled abroad?", "Finish the sentence: <i>I was nervous because I had never…</i>"]
    b.page(f"""{sec(4, "Practice: the past perfect", "10 min")}
{sub("A", "Sentences from the podcast. Which action happened first? Write it.", "2 min")}
<ol style="line-height:1.75;font-size:8.9pt;margin:0">{fsl}</ol>
{sub("B", "Choose.", "2 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0"><li>We use the past perfect for the {ch(["earlier", "later"], "earlier")} of two past actions.</li>
<li>When events are told in order (<i>He proposed and she said yes.</i>), we use the {ch(["past simple", "past perfect"], "past simple")}.</li></ol>
<div class="box sand"><h4>RULE</h4>Past perfect = <b>had</b> + past participle (<i>had moved, hadn't written</i>). Use it to go back to an <b>earlier</b> past moment, often with <i>when, by the time, already, just, never… before</i>. Don't use it for every past action. See the <b>Grammar reference</b> on page 3.</div>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    24, """<ol><li>A–B: 4 minutes. Draw a timeline for each sentence (earlier action on the left).</li>
<li>Use it: 6 minutes, all oral. Correct overuse: <i>I had met Paula yesterday</i> → <i>I met</i>.</li></ol>""")

    # 5 Speaking
    b.page(f"""{sec(5, "Speaking: telling a love story", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>start a story</th><th>go back in time</th><th>react</th><th>finish</th></tr>
<tr><td><i>It's a long story… · It all started when… · This is how they met.</i></td><td><i>Before that, … · By the time…, they had… · He had just…</i></td><td><i>No way! · What happened next? · That's so romantic!</i></td><td><i>In the end, … · And now… · So that's how…</i></td></tr></table></div>
{audiocard(["11.2"])}
{sub("A", "Contracted had. Listen and repeat: he'd just moved · she'd already decided.", "4 min", "11.2")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.55">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S112))}</p>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("B", "Role-play: relationship advice. Your teacher is a friend with a problem. Ask questions and give advice. Then change roles.", "10 min")}
<p style="margin:.3mm 0;font-size:8.6pt">{R("Teacher's card: You've been with your partner for two years. They've just been offered a great job in another country for a year, and they want to try a long-distance relationship. You love them, but you're not sure you can do it. You had a long-distance relationship before, and it ended badly.") if T else ""}</p></div>{img('D', 32, 24)}</div>
{talk(["Tell me the story of a couple you know (or a famous couple). What had happened before they met?", "Do you believe in love at first sight? What makes a relationship strong?"])}""",
    28, """<ol><li>A: listen for the small /d/: it tells you it's the past perfect. B: advice language (<i>If I were you, I'd…</i>) is useful here.</li>
<li>Talk about it: let the student talk about a couple from a movie if they prefer. Last 3 minutes: wrap-up.</li></ol>""")

    # H Homework
    pc = [(["met", "had met"], "met"), (["were", "had been"], "had been"), (["long-distance", "long-term"], "long-distance"),
          (["already split up", "had already split up"], "had already split up"), (["made up", "split up"], "made up"), (["proposed", "engaged"], "proposed")]
    p = [ch(o, a) for o, a in pc]
    dr = [("Bruno and Paula have only been on one date. It's still", "casual"), ("Ana and Marcos trust each other. They have a", "healthy"),
          ("Mrs. Lima was married for 36 years. That's a", "long-term")]
    drl = "".join(f"<li>{s} {A(w, 'min-width:18mm')} relationship.</li>" for s, w in dr)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Kate writes a blog post about a couple. Choose the correct words.", "")}</div>{img('C', 28, 18)}</div>
<div class="box" style="line-height:1.8;font-size:8.8pt;margin:.5mm 0"><b>Sweet Kate's Blog: a love story with a happy ending</b><br>Remember the wedding cake I dropped? I finally met the couple, Jake and Megan. They {p[0]} in college, and they {p[1]} together for six years when Megan got a job in Denver. Suddenly they were in a {p[2]} relationship. By the time Megan came home for Christmas, they {p[3]}. A year later, they met at a friend's wedding, talked all night and {p[4]}. Jake {p[5]} the next month!</div>
{sub("B", "Complete with casual, healthy or long-term.", "")}
<ol style="line-height:1.5;font-size:8.6pt;margin:0">{drl}</ol>
{lean.watch_out([("She's married with a doctor.", "She's married to a doctor.", "<i>married to</i> someone."), ("He dated with her for a year.", "He dated her for a year.", "no preposition after <i>date</i>."), ("I have a date with the dentist.", "I have an appointment with the dentist.", "a <i>date</i> is romantic.")])}
{lean.writing_task(sub, "A love story: write the relationship history of a couple you know or a famous couple.", "My parents met in… He had just… By the time…, they had…", ["relationship events", "two past perfect verbs", "ask out / split up / make up", "100–150 words"], "I can talk about relationships and tell the story of a couple.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class (explain each tense with a timeline). When you correct the writing, check that the past perfect is used only for earlier actions.</p>""")

    script = "".join(f"<p style='margin:.6mm 0'><b>{l.split(': ', 1)[0]}:</b> {l.split(': ', 1)[1]}</p>" for l in S111)
    b.extra("Audio script", f"""
{sub("11.1", "Gap Year Diaries: a love story (natural and slow)")}
<div style="line-height:1.35;font-size:8.7pt">{script}</div>
{sub("11.2", "Repeat: contracted had")}
<p>{" · ".join(S112)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 11 - Relationships and dating")
