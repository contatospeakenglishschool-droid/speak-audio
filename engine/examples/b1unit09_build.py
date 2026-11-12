# Speak! Progress B1 - Unit 09 "Love at first byte" (all English) - B1 format (2026-11-09)
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Progress"
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
    def lines(n):
        return '<div class="wline"></div>' * n

    # Page 1 - Warm-up
    cover = cover_html(T, "LEVEL B1 · UNIT 09", "Love at first byte", "How couples meet · <b>describing trends: past simple, present perfect, present continuous</b>",
                       [("YOU CAN", "understand an article about a social trend and talk about relationships and change"),
                        ("LANGUAGE", "asked her out · broke up · got engaged · has become · are getting · more and more"),
                        ("PRONUNCIATION", "linking in relationship phrases")])
    ev = [("Leo and Bia met through a mutual friend.", "1"), ("Leo asked Bia out on a date.", "2"), ("They started dating.", "3"),
          ("After a year of constant arguing, they broke up.", "4"), ("A few months later, they got back together.", "5"),
          ("They fell in love again and decided to get engaged.", "6"), ("Six months later, they got married.", "7"), ("Sadly, after ten years of marriage, they got divorced.", "8")]
    order = [3, 6, 0, 7, 4, 2, 5, 1]
    evl = [f'<li style="list-style:none">{A(ev[i][1], "min-width:5mm")} {ev[i][0]}</li>' for i in order]
    b.page(f"""{sec(1, "Warm-up: love and relationships", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 58, 38)}<div style="flex:1">
{sub("A", "Discuss with your teacher.", "3 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0"><li>Which social media and apps do you use? What for?</li><li>Where did your parents or grandparents meet?</li><li>What are the most common ways to meet a partner today?</li></ol></div></div>
{sub("B", "Key words. Put the events in order (1–8).", "4 min")}
<ul style="font-size:8.8pt;line-height:1.55;margin:0;padding-left:2mm;column-count:2;column-gap:5mm">{"".join(evl)}</ul>
{sub("C", "Which of these phrases can you use to tell the story of a couple you know?", "1 min")}""",
    25, """<ol><li>A: be sensitive: some students prefer not to talk about their own relationships. Let them talk about friends, family or famous couples.</li>
<li>B: American English: <i>date</i> or <i>be seeing</i> someone. <i>A mutual friend</i> = a friend of both.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 60 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Discussion · key words: relationship phrases in order</td><td>1</td></tr>
<tr><td>2 Reading</td><td>12 min</td><td>Article: Love at first byte, how couples meet (skim, scan, infer)</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>8 min</td><td>Describing trends: past simple, present perfect, present continuous</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Describing trends (study at home)</td><td>4</td></tr>
<tr><td>4 Vocabulary lab + pronunciation</td><td>8 min</td><td>Words from context · relationship verbs · false friends · linking</td><td>5</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Kate's blog: love then and now · trends in my life</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Functional language · long turn: how people meet · debate · talking point</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>4 min</td><td>Can-do · language notes · writing homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY AND THE FACTS</h4>The Linguahouse article (The Independent, 2012) reports a British dating-website poll. We replaced it with an article about a peer-reviewed study, read by the Host (Studio-O). Facts checked in the paper itself: Rosenfeld, M. J., Thomas, R. J. &amp; Hausen, S. (2019), "Disintermediating your friends: How online dating in the United States displaces other ways of meeting", <i>PNAS</i> 116(36), author copy at web.stanford.edu/~mrosenfe. Data: How Couples Meet and Stay Together 2017 (3,086 heterosexual respondents). About 39% of heterosexual couples who met in 2017 met online (about 22% in 2009; 0% before 1995); about 65% of same-sex couples; online overtook friends around 2013 (friends were the top way from the end of World War II to 2013); meeting through family, church, the neighborhood and school have declined since 1940; graphical web c. 1995, smartphones after 2007; phone apps were at least half of the growth 2010–2017; third-person help among online couples fell from 11.2% (2009) to 3.7% (2017); how couples met had no significant effect on breakup. The figures are for the US. In the Practice, Kate writes about her grandparents; in the writing model, Bruno tells how his parents met.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students say <i>She married with him</i>, <i>I'm dating with…</i> and <i>We knew each other at a party</i> (for the first time, use <i>meet</i>), use the present perfect with finished years, and say <i>less people</i>.</div>
<div class="box"><h4>AUDIO</h4>Track 09.1 Love at first byte (natural and slow; listen and read) · Track 09.2 Repeat: linking in relationship phrases</div>""")

    # Page 2 - Reading
    hd = [("Are online couples weaker?", "7"), ("Less help from friends", "6"), ("The numbers", "3"), ("Why it happened", "5"), ("The end of an old tradition", "4")]
    hdl = " &nbsp; ".join(f"<b>{chr(97+i)}</b> {h} {A(n, 'min-width:5mm')}" for i, (h, n) in enumerate(hd))
    fi = [("Who did the study, and when?", "Rosenfeld, Thomas and Hausen, in 2019."), ("What % of couples who met in 2017 met online?", "About 39% (heterosexual couples)."),
          ("And in 2009?", "About 22%."), ("Until 2013, what was the most popular way to meet?", "Through friends."),
          ("Which two technologies helped online dating grow?", "The graphical web and smartphones (apps)."), ("Did online couples break up more often?", "No, there was no significant effect.")]
    fil = [f'<li value="{i+1}">{q} {A(a, "min-width:20mm")}</li>' for i, (q, a) in enumerate(fi)]
    art = "".join(f'<p style="margin:0 0 .8mm"><b style="color:#176074">{i+1}</b> {p}</p>' for i, p in enumerate(PARAS))
    b.page(f"""{sec(2, "Reading: how couples meet", "12 min")}
<div class="box" style="margin:0;font-size:8pt;line-height:1.33;column-count:2;column-gap:4mm"><b style="font-size:9.5pt">Love at first byte</b><br>{art}</div>
<div style="display:flex;gap:3mm;align-items:center;margin-top:1mm"><div style="flex:1">{audiocard(["09.1 · NATURAL", "09.1 · SLOW"])}</div>{img('B', 36, 20)}</div>
{sub("A", "Skim the article in two minutes. Match the headings to paragraphs 3–7.", "2 min")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.7">{hdl}</p>
{sub("B", "Scan for the information.", "4 min")}
<div style="font-size:8.5pt">{twocol(fil, 3)}</div>
{sub("C", "Think about it. Discuss with your teacher.", "4 min")}
<ol style="line-height:1.4;font-size:8.7pt;margin:0"><li>Why do you think people use their friends less to find a partner now? {R("Personal: apps make it easy to meet strangers directly; more privacy; more choice.") if T else ""}</li>
<li>The study is about the US. Do you think the results are similar in Brazil? {R("Personal: don't state figures for Brazil; ask for the student's experience.") if T else ""}</li></ol>
<div class="box sand" style="margin-top:1mm"><h4>NOTICE: USEFUL CHUNKS</h4><i>above all · The results were clear. · even higher · since then · At the same time, … · In other words, … · What matters is…</i></div>""",
    25, """<ol><li>A: set a strict time limit. Then the student can listen and read (09.1). The title is a pun on <i>love at first sight</i> (a <i>byte</i> is a unit of computer data).</li>
<li>B: point out that the figures are for the US and for one survey; good readers notice where data comes from.</li></ol>""")

    # Page 3 - Language focus
    tr = [("Smartphones became popular after 2007.", "a", "past simple"), ("Meeting online has become the most common way couples meet.", "c", "present perfect"),
          ("People are meeting online more often.", "b", "present continuous"), ("Traditional ways of meeting have been declining for decades.", "d", "present perfect continuous")]
    kinds = ["a finished change in the past", "a change in progress now", "a change from the past up to now (result now)", "a change that started in the past and continues"]
    trl = "".join(f"<li>{s} {A(k + (' – ' + t if T else ''), 'min-width:8mm')}</li>" for s, k, t in tr)
    kl = " &nbsp; ".join(f"<b>{chr(97+i)}</b> {k}" for i, k in enumerate(kinds))
    gp = [("More and more people", "are getting", "(get) married later in life."), ("The internet", "became", "(become) widely used in the late 1990s."),
          ("Since 2010, phone apps", "have changed", "(change) the way people date."), ("These days, people", "are spending", "(spend) more time on their phones."),
          ("Online dating", "has been growing", "(grow) for years.")]
    gpl = "".join(f"<li>{a} {A(f, 'min-width:24mm')} {e}</li>" for a, f, e in gp)
    b.page(f"""{sec(3, "Language focus: describing trends", "8 min")}
{sub("A", "Read the sentences from the article. Match them to the kinds of change a–d.", "3 min")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.6">{kl}</p>
<ol style="line-height:1.7;font-size:8.9pt;margin:0">{trl}</ol>
{sub("B", "Complete with the correct form of the verb. Sometimes more than one answer is possible.", "4 min")}
<ol style="line-height:1.75;font-size:8.9pt;margin:0">{gpl}</ol>
{sub("C", "Choose.", "1 min")}
<p style="margin:.3mm 0;font-size:8.9pt">People are having {ch(["fewer", "less"], "fewer")} children, and they spend {ch(["fewer", "less"], "less")} time with their neighbors.</p>
<div class="box sand"><h4>RULE</h4><b>past simple</b> → a finished change (<i>in 2007, in the 1990s</i>) · <b>present perfect</b> → a change up to now (<i>since then, has become</i>) · <b>present perfect continuous</b> → a change that continues (<i>for decades</i>) · <b>present continuous</b> → a change in progress (<i>these days, more and more</i>). <i>fewer</i> + countable, <i>less</i> + uncountable. More on the next page: <b>Grammar reference</b>.</div>""",
    24, """<ol><li>B: in 3, <i>have changed</i> or <i>have been changing</i>; in 5, <i>has grown</i> is also possible. Accept answers the student can justify.</li>
<li>Ask the student for trends in their city: <i>What is changing in São Paulo / your town?</i></li></ol>""")

    grammar_ref.describing_trends(b)

    # Page 5 - Vocabulary lab
    cx = [("most of all (paragraph 1)", "above all"), ("a set of questions to many people (paragraph 2)", "a survey"), ("the number (paragraph 3)", "the figure"),
          ("passed, became more popular than (paragraph 4)", "overtook"), ("going down (paragraph 4)", "declining"), ("ending a relationship (paragraph 7)", "breaking up")]
    cxl = [f'<li value="{i+1}">{d} {A(w, "min-width:18mm")}</li>' for i, (d, w) in enumerate(cx)]
    rv = [("They", "hit it off", "immediately and talked for hours."), ("He", "asked", "her out after the class."), ("After two years, they", "split up", "."),
          ("She's", "seeing", "someone from work."), ("I think he's", "fallen", "for her!")]
    rvl = " &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {a} {A(v, 'min-width:14mm')}{e if e == '.' else ' ' + e}" for i, (a, v, e) in enumerate(rv))
    b.page(f"""{sec(4, "Vocabulary lab: love and change", "4 min")}
{sub("A", "Meaning from context. Find words or phrases in the article that mean…", "2 min")}
<div style="font-size:8.6pt">{twocol(cxl, 3)}</div>
{sub("B", "Relationship verbs. Complete with asked, fallen, hit it off, seeing or split up.", "2 min")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.9">{rvl}</p>
<div class="box sand"><h4>WATCH OUT: FALSE FRIENDS AND PREPOSITIONS</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>She married with a doctor.</td><td><b>She married a doctor. / She got married to a doctor.</b></td><td>no <i>with</i> after <i>marry</i>.</td></tr>
<tr><td>I'm dating with Bia.</td><td><b>I'm dating Bia. / I'm seeing Bia.</b></td><td><i>date</i> + person, no preposition.</td></tr>
<tr><td>We knew each other at a party.</td><td><b>We met at a party.</b></td><td>the first time = <i>meet</i>; <i>know</i> = already know.</td></tr></table></div>
{sec(5, "Pronunciation lab: linking", "4 min")}
<p class="small" style="margin:.3mm 0">In relationship phrases, a consonant links to the next vowel: <i>asked_her_out · fell_in love · broke_up · got_engaged</i>.</p>
{audiocard(["09.2"])}
{sub("A", "Listen and repeat. Then tell your teacher the story of a couple from a movie or series.", "4 min", "09.2")}
<p style="margin:.3mm 0;font-size:8.8pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S092))}</p>""",
    24, """<ol><li>B: <i>hit it off</i> = like each other immediately; <i>fall for</i> = start to love; <i>split up</i> = break up; <i>be seeing someone</i> = be dating.</li>
<li>Pronunciation: in <i>asked her out</i>, the <i>h</i> of <i>her</i> often disappears: /æskt ər aʊt/.</li></ol>""")

    # Page 6 - Practice
    pr = [(["met", "have met"], "met"), (["used to go", "have gone"], "used to go"), (["was", "has been"], "was"), (["has changed", "changed"], "has changed"),
          (["are using", "used"], "are using"), (["more and more", "most and most"], "more and more"), (["has become", "is becoming"], "has become"),
          (["fewer", "less"], "fewer"), (["is getting", "got"], "is getting")]
    p = [ch(o, a) for o, a in pr]
    st = ["In my city, more and more people…", "Since I was a child, technology has…", "These days, people are…", "In the last few years, I have stopped…"]
    b.page(f"""{sec(6, "Practice", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Kate writes about love on her bakery blog. Choose the correct words.", "5 min")}</div>{img('C', 30, 22)}</div>
<div class="box" style="line-height:1.95;font-size:9pt"><b>Sweet Kate's Blog: love, then and now</b><br>This week I made a wedding cake for a couple who {p[0]} on a dating app. It made me think about my grandparents. They {p[1]} to dances every Saturday, and Grandma always says it {p[2]} love at first sight. So much {p[3]} since then! Today, most of my customers {p[4]} apps to meet people, and {p[5]} couples order cakes for their "first date anniversary". Online dating {p[6]} completely normal. My grandparents say people have {p[7]} children now and get married later. And my bakery? It {p[8]} busier every year, so maybe love isn't changing that much after all!</div>
{sub("B", "Trends in your life. Complete the sentences so they are true for you. Then tell your teacher.", "3 min")}
<ol style="line-height:1.35;font-size:8.9pt;margin:0">{"".join(f"<li>{t}<div class='wline'></div></li>" for t in st)}</ol>""",
    22, """<ol><li>A: ask the student to name the kind of change for each verb (finished, up to now, in progress).</li>
<li>B: in 4, <i>stopped</i> + -ing (Unit 05). Ask follow-up questions.</li></ol>""")

    # Page 7 - Speaking
    b.page(f"""{sec(7, "Speaking: how people meet", "12 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>describe change</th><th>compare then and now</th><th>argue a point</th><th>concede</th></tr>
<tr><td><i>More and more people… · It's getting… · …has become…</i></td><td><i>In the past, people used to… · Nowadays, … · Compared to…</i></td><td><i>The main reason is… · Look at… · That's why…</i></td><td><i>That's true, but… · I see what you mean, however…</i></td></tr></table></div>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("A", "Long turn. Prepare for one minute, then talk for two minutes about how people meet partners and friends today.", "5 min")}
<ul style="line-height:1.45;font-size:8.9pt;margin:0"><li>how people met in the past in your family</li><li>how people meet now</li><li>what has changed, and why</li><li>what you think is the best way to meet someone</li></ul></div>{img('D', 32, 24)}</div>
{sub("B", "Mini-debate. \"Meeting someone online is better than meeting through friends.\" Choose a side. Your teacher takes the other side.", "4 min")}
{sub("C", "Talking point. Discuss with your teacher.", "3 min")}
<ol style="line-height:1.5;font-size:8.9pt;margin:0"><li>Is online dating popular in Brazil? Why or why not?</li><li>What are the advantages and disadvantages of social media for relationships?</li><li>Do you know any couples who met online?</li></ol>""",
    28, """<ol><li>A: if the student prefers, they can talk about how people make friends. Note mistakes for the error log (page 8). Fluency option (3-2-1): the same talk in 2 minutes, then in 1 minute.</li>
<li>B: give the student a minute to think of two reasons. Argue the other side politely and use the language in the box.</li></ol>""")

    # Page 8 - Wrap-up
    pc = ["I can understand an article about a social trend (gist, figures, opinions).", "I can describe trends with the past simple, present perfect and present continuous.",
          "I can tell the story of a relationship and talk about how things are changing."]
    pcr = "".join(f"<tr><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for s in pc)
    b.page(f"""{sec(8, "Wrap-up and homework", "4 min")}
{sub("A", "Can-do check", "1 min")}
<table class="ck" style="font-size:8.6pt"><tr><th>In English…</th><th style="width:16mm">Easy!</th><th style="width:16mm">Sometimes</th><th style="width:16mm">Not yet</th></tr>{pcr}</table>
{sub("B", "My language notes. Write three corrections from today's class.", "2 min")}
<div style="display:flex;gap:5mm;font-size:8.6pt"><div style="flex:1"><b>I said…</b>{lines(3)}</div><div style="flex:1"><b>Better:</b>{lines(3)}</div></div>
{sub("C", "Homework: writing (100–150 words)", "1 min")}
<p style="margin:.3mm 0"><b>How they met.</b> Tell the story of how a couple you know met (family, friends, or a famous couple), and say how things are different today. Read Bruno's story first.</p>
<div class="box" style="font-size:8.6pt;line-height:1.4;margin:.5mm 0"><i>My parents met in Porto Alegre in 1995. My mom was a nurse, and my dad was a patient with a broken leg! He asked her out on his last day in the hospital, and they hit it off immediately. They dated for three years and got married in 1998. Of course, there were no apps then. People used to meet at work, at parties or through friends. Things have changed a lot since then. Most of my friends have met their partners online, and more and more people are using apps to find friends, too. I'm not seeing anyone at the moment, because I spend all day in front of a screen. Maybe I should try an app!</i></div>
<p class="small" style="margin:.3mm 0">Checklist: ☐ four relationship phrases &nbsp;☐ past simple for the story &nbsp;☐ present perfect or present continuous for change &nbsp;☐ <i>more and more</i> &nbsp;☐ 100–150 words</p>
{lines(6)}""",
    30, """<ol><li>B (error log): during the lesson, note 3–5 real mistakes. Here, the student writes what they said and the better version; guide them to self-correct first.</li>
<li>C: the student can write about a famous couple if they prefer. Check <i>marry</i> without <i>with</i> and the tenses for change.</li></ol>""")

    b.extra("Audio script", f"""
{sub("09.1", "Love at first byte (natural and slow)")}
<p style="line-height:1.4;font-size:9pt"><i>The Host reads the article on page 2.</i></p>
{sub("09.2", "Repeat: linking in relationship phrases")}
<p>{" · ".join(S092)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 09 - Love at first byte")
