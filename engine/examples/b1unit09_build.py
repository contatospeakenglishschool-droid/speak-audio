# Speak! Progress B1 - Unit 09 "Love at first byte" (all English) - lean B1 format (rebuilt 2026-11-19)
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
setup(band="B1 · UNIT 09", audio_json="audio_b1-unit-09.json", img_dir="img")
_r = json.load(open("roteiro.json"))["units"]["b1-unit-09"]
PARAS = [
    "For most of the 20th century, people met their partners in the same few places: at school, at church, in the neighborhood, through their family, and above all, through their friends. Then the internet arrived, and everything started to change.",
    "In 2019, three sociologists, Michael Rosenfeld, Reuben Thomas and Sonia Hausen, published a study about how couples in the United States meet. They used a national survey from 2017, which included more than 3,000 people with partners of the opposite sex.",
    "The results were clear. About 39% of the heterosexual couples who met in 2017 met online. In 2009, the figure was about 22%, and before 1995, it was zero. Among same-sex couples, the number was even higher: about 65%.",
    "From the end of the Second World War until about 2013, the most popular way to meet a partner in the US was through friends. But around 2013, meeting online overtook meeting through friends, and since then, it has become the most common way couples meet. At the same time, the traditional ways of meeting, like meeting through family, at church or in the neighborhood, have been declining for decades.",
    "Technology explains a lot of this change. The graphical web appeared around 1995, and smartphones became popular after 2007. According to the study, phone apps were responsible for at least half of the growth in meeting online between 2010 and 2017.",
    "Interestingly, people are not only meeting online more often. They are also using their friends less. In 2009, about 11% of the couples who met online had some help from another person. By 2017, that number had fallen to less than 4%.",
    "So, are online relationships weaker? The researchers found no evidence of that. How couples met had no significant effect on the chance of breaking up. In other words, it doesn't matter where you find love. What matters is what you do with it."]
S092 = [x.split(": ", 1)[1] for x in _r["09.2 Repeat: linking in relationship phrases"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'

    # 1 Warm-up
    cover = cover_html(T, "LEVEL B1 · UNIT 09", "Love at first byte", "How couples meet · <b>describing trends: past simple, present perfect, present continuous</b>",
                       [("YOU CAN", "understand an article about a social trend and talk about relationships and change"),
                        ("LANGUAGE", "asked her out · broke up · got engaged · has become · are getting · more and more"),
                        ("PRONUNCIATION", "linking in relationship phrases")])
    ev = [("Leo and Bia met through a mutual friend.", "1"), ("Leo asked Bia out on a date.", "2"), ("They started dating.", "3"),
          ("After a year of arguing, they broke up.", "4"), ("A few months later, they got back together.", "5"), ("They got married.", "6")]
    order = [3, 5, 0, 4, 2, 1]
    evl = [f'<li style="list-style:none">{A(ev[i][1], "min-width:5mm")} {ev[i][0]}</li>' for i in order]
    b.page(f"""{sec(1, "Warm-up: love and relationships", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["Which social media and apps do you use? What for?", "Where did your parents or grandparents meet?", "What are the most common ways to meet a partner today?"], "START TALKING")}</div></div>
{sub("A", "Key words. Put the events in order (1–6).", "3 min")}
<ul style="font-size:8.8pt;line-height:1.55;margin:0;padding-left:2mm;column-count:2;column-gap:5mm">{"".join(evl)}</ul>
{talk(["Tell me the story of a couple you know (family, friends or famous). Use phrases from A.", "Do you know anyone who got back together after breaking up?"], "USE THE WORDS")}""",
    26, """<ol><li>Top box: be sensitive; some students prefer not to talk about their own relationships. Let them talk about friends, family or famous couples.</li>
<li>A: American English: <i>date</i> or <i>be seeing</i> someone.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Article: how couples meet (a real study) · headings · scan for facts · Talk about it", "Describing trends: past simple, present perfect, present continuous",
                      "Kinds of change · complete the trends · Use it (oral)", "Functional language · linking (09.2) · mini-debate",
                      "Kate's blog: love then and now · relationship verbs · word choice · writing", "Reading"),
        "The Linguahouse article (The Independent, 2012) reports a British dating-website poll. We replaced it with an article about a peer-reviewed study, read by the Host (Studio-O). Facts checked in the paper: Rosenfeld, M. J., Thomas, R. J. &amp; Hausen, S. (2019), \"Disintermediating your friends: How online dating in the United States displaces other ways of meeting\", <i>PNAS</i> 116(36). Data: How Couples Meet and Stay Together 2017 (3,086 heterosexual respondents). About 39% of heterosexual couples who met in 2017 met online (about 22% in 2009; 0% before 1995); about 65% of same-sex couples; online overtook friends around 2013; phone apps were at least half of the growth 2010–2017; third-person help among online couples fell from 11.2% (2009) to 3.7% (2017); how couples met had no significant effect on breakup. The figures are for the US. In the homework, Kate writes about her grandparents.",
        "Students say <i>She married with him</i>, <i>I'm dating with…</i> and <i>We knew each other at a party</i> (for the first time, use <i>meet</i>), use the present perfect with finished years, and say <i>less people</i>.",
        "Track 09.1 Love at first byte (natural and slow; listen and read) · Track 09.2 Repeat: linking in relationship phrases"))

    # 2 Reading
    hd = [("Are online couples weaker?", "7"), ("Less help from friends", "6"), ("The numbers", "3"), ("Why it happened", "5"), ("The end of an old tradition", "4")]
    hdl = " &nbsp; ".join(f"<b>{chr(97+i)}</b> {h} {A(n, 'min-width:5mm')}" for i, (h, n) in enumerate(hd))
    fi = [("What % of couples who met in 2017 met online?", "about 39%"), ("Until 2013, what was the most popular way to meet?", "through friends"),
          ("Which technologies helped online dating grow?", "the web and smartphone apps"), ("Did online couples break up more often?", "no")]
    fil = [f'<li value="{i+1}">{q} {A(a, "min-width:20mm")}</li>' for i, (q, a) in enumerate(fi)]
    art = "".join(f'<p style="margin:0 0 .8mm"><b style="color:#176074">{i+1}</b> {p}</p>' for i, p in enumerate(PARAS))
    b.page(f"""{sec(2, "Reading: how couples meet", "12 min")}
<div class="box" style="margin:0;font-size:7.9pt;line-height:1.32;column-count:2;column-gap:4mm"><b style="font-size:9.5pt">Love at first byte</b><br>{art}</div>
<div style="display:flex;gap:3mm;align-items:center;margin-top:1mm"><div style="flex:1">{audiocard(["09.1 · NATURAL", "09.1 · SLOW"])}</div>{img('B', 36, 20)}</div>
{sub("A", "Skim the article in two minutes. Match the headings to paragraphs 3–7.", "2 min")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.6">{hdl}</p>
{sub("B", "Scan for the information.", "3 min")}
<div style="font-size:8.5pt">{twocol(fil, 2)}</div>
{talk(["Why do you think people use their friends less to find a partner now?", "The study is about the US. Do you think the results are similar in Brazil?", "Would you use an app to meet new friends?"])}""",
    24, """<ol><li>A–B: 6 minutes. The title is a pun on <i>love at first sight</i> (a <i>byte</i> is a unit of computer data). The figures are for the US and for one survey.</li>
<li>Talk about it: 6 minutes. Don't state figures for Brazil; ask for the student's experience.</li></ol>""")

    # 3 Grammar reference
    lean.grammar_in_class(b, grammar_ref.describing_trends)

    # 4 Practice
    tr = [("Smartphones became popular after 2007.", "a"), ("Meeting online has become the most common way couples meet.", "c"),
          ("People are meeting online more often.", "b"), ("Traditional ways of meeting have been declining for decades.", "d")]
    kinds = ["a finished change in the past", "a change in progress now", "a change up to now (result now)", "a change that started in the past and continues"]
    trl = "".join(f"<li>{s} {A(k, 'min-width:8mm')}</li>" for s, k in tr)
    kl = " &nbsp; ".join(f"<b>{chr(97+i)}</b> {k}" for i, k in enumerate(kinds))
    use = ["How has your city changed in the last ten years?", "What are more and more people doing these days?", "What did people use to do that they don't do now?",
           "How has technology changed the way you work or study?", "What's getting more expensive, and what's getting cheaper?"]
    b.page(f"""{sec(4, "Practice: describing trends", "10 min")}
{sub("A", "Read the sentences from the article. Match them to the kinds of change a–d.", "3 min")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.6">{kl}</p>
<ol style="line-height:1.7;font-size:8.9pt;margin:0">{trl}</ol>
{sub("B", "Choose.", "1 min")}
<p style="margin:.3mm 0;font-size:8.9pt">People are having {ch(["fewer", "less"], "fewer")} children, and they spend {ch(["fewer", "less"], "less")} time with their neighbors.</p>
<div class="box sand"><h4>RULE</h4><b>past simple</b> → a finished change · <b>present perfect</b> → a change up to now · <b>present perfect continuous</b> → a change that continues · <b>present continuous</b> → a change in progress (<i>these days, more and more</i>) · <i>fewer</i> + countable, <i>less</i> + uncountable. See the <b>Grammar reference</b> on page 3.</div>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    24, """<ol><li>A–B: 4 minutes. Ask why each tense is used.</li>
<li>Use it: 6 minutes, all oral. Push for <i>more and more</i>, <i>has become</i> and <i>used to</i>.</li></ol>""")

    # 5 Speaking
    b.page(f"""{sec(5, "Speaking: how people meet", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>describe change</th><th>compare then and now</th><th>argue a point</th><th>concede</th></tr>
<tr><td><i>More and more people… · It's getting… · …has become…</i></td><td><i>In the past, people used to… · Nowadays, … · Compared to…</i></td><td><i>The main reason is… · Look at… · That's why…</i></td><td><i>That's true, but… · I see what you mean, however…</i></td></tr></table></div>
{audiocard(["09.2"])}
{sub("A", "Linking. Listen and repeat: asked_her_out · fell_in love · broke_up.", "4 min", "09.2")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.55">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S092))}</p>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("B", "Mini-debate. &ldquo;Meeting someone online is better than meeting through friends.&rdquo; Choose a side and give two reasons. Your teacher takes the other side. Then debate: &ldquo;Social media is good for relationships.&rdquo;", "10 min")}</div>{img('D', 32, 24)}</div>
{talk(["Is online dating popular in Brazil? Why or why not?", "Do you know any couples who met online? How did it go?"])}""",
    28, """<ol><li>A: in <i>asked her out</i>, the <i>h</i> of <i>her</i> often disappears. B: give the student a minute to think of two reasons; argue the other side politely.</li>
<li>Last 3 minutes: wrap-up (two corrections and <i>Can you talk about trends and change?</i>).</li></ol>""")

    # H Homework
    pr = [(["met", "have met"], "met"), (["used to go", "have gone"], "used to go"), (["has changed", "changed"], "has changed"),
          (["are using", "used"], "are using"), (["has become", "is becoming"], "has become"), (["fewer", "less"], "fewer")]
    p = [ch(o, a) for o, a in pr]
    rv = [("They", "hit it off", "immediately and talked for hours."), ("He", "asked", "her out after the class."), ("After two years, they", "split up", ".")]
    rvl = " &nbsp;·&nbsp; ".join(f"{a} {A(v, 'min-width:14mm')}{e if e == '.' else ' ' + e}" for a, v, e in rv)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Kate writes about love on her bakery blog. Choose the correct words.", "")}</div>{img('C', 28, 18)}</div>
<div class="box" style="line-height:1.8;font-size:8.8pt;margin:.5mm 0"><b>Sweet Kate's Blog: love, then and now</b><br>This week I made a wedding cake for a couple who {p[0]} on a dating app. It made me think about my grandparents. They {p[1]} to dances every Saturday. So much {p[2]} since then! Today, most of my customers {p[3]} apps to meet people. Online dating {p[4]} completely normal. My grandparents say people have {p[5]} children now and get married later.</div>
{sub("B", "Complete with asked, hit it off or split up.", "")}
<p style="margin:.3mm 0;line-height:1.9;font-size:8.6pt">{rvl}</p>
{lean.watch_out([("She married with a doctor.", "She married a doctor. / She got married to a doctor.", "no <i>with</i> after <i>marry</i>."), ("I'm dating with Bia.", "I'm dating Bia. / I'm seeing Bia.", "<i>date</i> + person, no preposition."), ("We knew each other at a party.", "We met at a party.", "the first time = <i>meet</i>.")])}
{lean.writing_task(sub, "How they met: tell the story of how a couple you know met, and say how things are different today.", "My parents met in… He asked her out… Things have changed a lot since then…", ["relationship phrases", "past simple for the story", "present perfect / continuous for change", "100–150 words"], "I can tell the story of a relationship and talk about how things are changing.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class (ask the student to name the kind of change for each verb). The student can write about a famous couple if they prefer.</p>""")

    b.extra("Audio script", f"""
{sub("09.1", "Love at first byte (natural and slow)")}
<p style="line-height:1.4;font-size:9pt"><i>The Host reads the article on page 2.</i></p>
{sub("09.2", "Repeat: linking in relationship phrases")}
<p>{" · ".join(S092)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 09 - Love at first byte")
