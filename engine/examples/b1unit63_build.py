# Speak! Progress B1 - Unit 63 "Predictions" (all English) - lean B1 format
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
setup(band="B1 · UNIT 63", audio_json="audio_b1-unit-63.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-63"]
S631 = [l.split(": ", 1)[1] for l in _r["63.1 Danny's blog: predictions that went wrong"].split("\n")]
S632 = [x.split(": ", 1)[1] for x in _r["63.2 Repeat: the before vowels and consonants"].split("\n")]


TITLE = "Grandma Lourdes and the predictions that went wrong"
INTRO = S631[0].replace(TITLE + ". ", "", 1)
PARAS = S631[1:]


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
    cover = cover_html(T, "LEVEL B1 · UNIT 63", "Predictions", "Predictions that went wrong · <b>the telephone · the elderly · people in general</b>",
                       [("YOU CAN", "make and react to predictions, and talk about things and people in general"),
                        ("LANGUAGE", "stare · claim · predict · outdated · a pioneer · spam · the + type · the rich · no article in general"),
                        ("PRONUNCIATION", "the /ðə/ and /ði/: the radio, the elderly")])
    words = ["bright", "an invention", "outdated", "a pioneer", "a sensation", "spam", "stare", "a vacuum cleaner"]
    defs = {"bright": "intelligent, with good ideas", "an invention": "something new that somebody creates for the first time",
            "outdated": "old-fashioned; no longer useful or modern", "a pioneer": "a person or company that is one of the first to do something",
            "a sensation": "something that causes great excitement and interest", "spam": "emails you don't want, usually advertisements",
            "stare": "look at something for a long time with your eyes wide open", "a vacuum cleaner": "a machine that cleans floors by sucking up dust"}
    order = [4, 7, 0, 6, 1, 3, 5, 2]
    kwl = "".join(f'<li>{A(words[i], "min-width:26mm")} <span style="color:#6b7377">= {defs[words[i]]}</span></li>' for i in order)
    b.page(f"""{sec(1, "Warm-up: great inventions", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["Look at the photo. Have you ever used a phone like this? Who had one in your family?", "What has been the most important invention of the last 100 years?", "Which invention could you never live without?"], "START TALKING")}</div></div>
{sub("A", "Key words. Write the words from the box next to their meanings.", "3 min")}
<div class="bank">{" · ".join(words)}</div>
<ol style="font-size:8.6pt;line-height:1.7;margin:0">{kwl}</ol>
{talk(["Which gadgets in your home are outdated now?", "How much spam do you get every day?", "Who is a pioneer in your area of work or study?"], "USE THE WORDS")}""",
    30, """<ol><li>Top box: 3 minutes. Accept any invention and ask <i>Why?</i> (the internet, the smartphone, the airplane, the washing machine…). Notice the student's articles: you'll come back to them on page 3.</li>
<li>A comes from the Linguahouse key words; we added <i>an invention</i> and <i>outdated</i>.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Danny's blog: Grandma Lourdes and the predictions that went wrong · who said it? · true or false · find the words",
                      "talking in general: no article with plural and uncountable nouns; the + type (the telephone); the + adjective (the rich, the elderly); nationalities", "Choose the correct words · general knowledge quiz · Use it (oral)",
                      "the /ðə/ or /ði/ (63.2) · reacting to predictions · the 2050 predictions game · long turn: a prediction about you", "reporting predictions with would · watch out · writing: life in 2050"),
        """The Linguahouse lesson is an article about famous wrong predictions made by real business people and engineers, with dates, sales numbers and quotes that are disputed. We did not use it, because we cannot check those facts. Instead, the student reads a post from Danny's blog (also recorded as audio): Grandma Lourdes (97) remembers predictions that went wrong in her life. Her father said the television would never replace the radio; a neighbor said people would drive flying cars by 2000; her teacher claimed people would never want to carry a telephone; her uncle predicted only the rich would travel by plane (now Carol flies from Orlando every year and complains about the food); a magazine said robots would do the cooking ("the microwave came"); and Lourdes predicted she would live to a hundred ("three more years"). We kept the Linguahouse key words, the "who said it" task, the reporting predictions exercise (homework), the general/specific articles practice and quiz, and the speaking task with certainty expressions. The grammar point is the Linguahouse one, new at B1: articles for talking in general.""",
        """<i>The life is short</i> (→ <i>Life is short</i>); <i>The technology changes fast</i> (→ <i>Technology</i>); <i>I love the music</i> in general (→ <i>I love music</i>); <i>the elderlies</i> (→ <i>the elderly</i>). Reported predictions: <i>He said that people will…</i> (→ <i>would</i>, when the prediction was wrong or is in the past).""",
        "Track 63.1 Danny's blog: predictions that went wrong (natural and slow; read by Danny) · Track 63.2 Repeat: the before vowels and consonants"))

    # Page 2 - Reading
    text = "".join(f"<p style='margin:0 0 .8mm'><b>{i+1}</b> {p}</p>" for i, p in enumerate(PARAS))
    who = ["a magazine", "a neighbor", "her father", "her teacher", "her uncle", "Lourdes herself"]
    preds = [("Nobody will sit and stare at a box all evening.", 2), ("I will live to a hundred.", 5), ("Robots will do all the cooking.", 0),
             ("Only the rich will travel by plane.", 4), ("People will drive flying cars by 2000.", 1), ("People will never want to carry a telephone.", 3)]
    pl = "".join(f'<li><i>{p}</i> {A(who[i], "min-width:24mm")}</li>' for p, i in preds)
    tf = [("Lourdes's father thought the television would be a big success.", "F: he thought it would never replace the radio."),
          ("Lourdes watches the news on a tablet today.", "T"), ("Carol loves the food on planes.", "F: she always complains about it.")]
    tfl = "".join(f"<li>{s} <b>T / F</b> {R(a)}</li>" for s, a in tf)
    fw = [("look for a long time (P1)", "stare"), ("said something was true without proof (P3)", "claimed"),
          ("said what would happen (P4)", "predicted"), ("a machine that heats food fast (P5)", "the microwave")]
    fwl = "".join(f"<li>{d} {A(w, 'min-width:22mm')}</li>" for d, w in fw)
    b.page(f"""{sec(2, "Reading: predictions that went wrong", "12 min")}
<div class="box" style="margin:.5mm 0;font-size:8.1pt;line-height:1.33"><div style="float:right;margin:0 0 1mm 2.5mm">{img('B', 34, 23)}</div><b style="font-size:9.4pt;color:#176074">{TITLE}</b><br><i>{INTRO}</i>{text}</div>
{audiocard(["63.1 · NATURAL", "63.1 · SLOW"])}
{sub("A", "Read and listen. Who made each prediction? Use the box.", "4 min")}
<div class="bank" style="font-size:8.3pt">{" · ".join(who)}</div>
<ol style="line-height:1.45;font-size:8.3pt;margin:0;columns:2;column-gap:5mm">{pl}</ol>
<div style="display:flex;gap:4mm"><div style="flex:1.2">
{sub("B", "True (T) or false (F)? Which prediction could still come true?", "3 min")}
<ol style="line-height:1.4;font-size:8.3pt;margin:0">{tfl}</ol>{R("Lourdes's own: she could live to a hundred.") if T else ""}</div><div style="flex:1">
{sub("C", "Find the words.", "3 min")}
<ol style="line-height:1.5;font-size:8.3pt;margin:0">{fwl}</ol></div></div>""",
    30, """<ol><li>A comes from the Linguahouse "find the information" task, with invented, personal predictions.</li>
<li>After C, ask the student to find the articles: <i>the radio, the television, people, the telephone, the rich, robots, the microwave, the young</i>. Ask: <i>Do they mean one specific thing, or things in general?</i> They come back on page 3.</li></ol>""")

    # Page 3
    lean.grammar_in_class(b, grammar_ref.generic_articles)

    # Page 4 - Practice
    pc = [("", ["Robots", "The robots"], "Robots", "will become part of everyday life."), ("", ["Computers", "The computers"], "The computers", "we use at work are very old."),
          ("", ["The music", "Music"], "Music", "helps me relax."), ("", ["Music", "The music"], "The music", "at Rafa's gig was great."),
          ("", ["A smartphone", "The smartphone"], "The smartphone", "changed the way we live."), ("", ["Elderly", "The elderly"], "The elderly", "use technology more than we think."),
          ("Lourdes listened to", ["the radio", "radio"], "the radio", "every night."), ("Thanks for", ["the advice", "advice"], "the advice", "you gave me!")]
    cl = "".join(f"<li>{a + ' ' if a else ''}{ch(o, r)} {z}</li>" for a, o, r, z in pc)
    qz = [("What is the fastest land animal?", "the cheetah"), ("Which instrument has 88 keys?", "the piano"),
          ("What is the biggest ocean in the world?", "the Pacific"), ("Which means of transport is fastest for long distances?", "the airplane")]
    qzl = "".join(f'<li>{q} {A(a, "min-width:24mm")}</li>' for q, a in qz)
    use = ["What do the young in your country do that the elderly don't understand?", "Do you think robots will do the cooking one day?",
           "Which do you prefer: books or films? Why?", "What did the internet change in your life?", "Do you play an instrument? Which instrument would you like to play?"]
    b.page(f"""{sec(4, "Practice: general or specific?", "10 min")}
{sub("A", "General or specific? Choose the correct words.", "3 min")}
<ol style="line-height:1.7;font-size:8.6pt;margin:0;columns:2;column-gap:6mm">{cl}</ol>
{sub("B", "Quick quiz. Answer with the + noun.", "3 min")}
<ol style="line-height:1.6;font-size:8.7pt;margin:0;columns:2;column-gap:6mm">{qzl}</ol>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    30, """<ol><li>A comes from the Linguahouse grammar practice, with new sentences. Ask each time: <i>In general, or which ones?</i></li>
<li>B comes from the Linguahouse quiz (general facts only): the + singular noun for a type of animal, instrument or means of transport.</li>
<li>Use it: 4 minutes, all oral. Listen for <i>the</i> before general nouns (<i>the books, the films</i>).</li></ol>""")

    # Page 5 - Speaking
    topics = ["work and jobs", "cities and transport", "food", "school and learning", "travel", "the family"]
    card = f"""<div class="box" style="margin-top:1mm;font-size:8.2pt">{R("<b>Teacher's card:</b> give your own predictions first as a model: <i>In 2050, robots will clean our homes. People won't need a driver's license. The elderly will work longer.</i> React to the student's predictions with the scale, and ask <i>Why do you think so?</i> At the end, report one prediction: <i>You predicted that people would…</i>")}</div>""" if T else ""
    b.page(f"""{sec(5, "Speaking: the world in 2050", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE: REACTING TO PREDICTIONS (FROM SURE TO NO WAY)</h4>
<table style="margin:0;font-size:8.2pt"><tr><th>sure</th><th>likely</th><th>possible</th><th>unlikely</th><th>impossible</th></tr>
<tr><td><i>That will definitely happen.</i></td><td><i>I think that's pretty likely.</i></td><td><i>I suppose that might happen.</i></td><td><i>I doubt that will happen.</i></td><td><i>There's no way that will happen!</i></td></tr></table></div>
{audiocard(["63.2"])}
{sub("A", "Listen and repeat. Say the /ðə/ before a consonant sound and /ði/ before a vowel sound.", "2 min", "63.2")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S632))}</p>
{sub("B", "The world in 2050. Make one prediction about each topic. Your teacher reacts. Then react to your teacher's predictions.", "8 min")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.7">{" &nbsp;·&nbsp; ".join(topics)}</p>{card}
{sub("C", "Discuss. Which wrong prediction in Danny's post is the funniest? Which gadgets will be outdated in twenty years?", "3 min")}
{sub("D", "Long turn. Tell your teacher about a prediction someone made about you or your family. What did they say would happen? Were they right?", "3 min")}""",
    30, """<ol><li>B comes from the Linguahouse speaking task, adapted for 1:1. Push <i>will, won't, might, be likely to</i> and general nouns without <i>the</i> (<i>People will…, Cars will…</i>).</li>
<li>Last 3 minutes: wrap-up (two corrections, and ask <i>Can you now make and react to predictions and talk about things in general?</i>).</li></ol>""")

    # Homework
    rp = [("Lourdes's father said, \"Nobody will watch television.\" (predict)", "Lourdes's father predicted (that) nobody would watch television."),
          ("Bruno said publicly, \"I will run a marathon next year.\" (declare)", "Bruno declared (that) he would run a marathon the next year."),
          ("Rafa said, giving many reasons, \"Jazz will be popular again.\" (argue)", "Rafa argued (that) jazz would be popular again."),
          ("The teacher said, \"It's not true. People won't carry phones.\" (deny)", "The teacher denied (that) people would carry phones.")]
    rpl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rp)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Reporting predictions. Rewrite the sentences with the verb in brackets and would / wouldn't.", "")}</div>{img('C', 30, 19)}</div>
<ol style="line-height:1.45;font-size:8.7pt;margin:0">{rpl}</ol>
{lean.watch_out([("The life is short.", "Life is short.", "general ideas: no article."), ("The technology changes very fast.", "Technology changes very fast.", "uncountable noun in general: no article."), ("The elderlies use tablets.", "The elderly use tablets.", "<i>the</i> + adjective = a group; no <i>-s</i>.")])}
{lean.writing_task(sub, "Write a post for Danny's blog: five predictions about life in 2050, and how sure you are about each one.", "In 2050, I think people will…", ["five predictions on different topics", "how sure you are (definitely, likely, I doubt…)", "general nouns without the, and the + type or group", "100–150 words"], "I can make and react to predictions, and talk about things and people in general.")}""",
    25, """<p>Check A in 3 minutes at the start of the next class. It comes from the Linguahouse reporting predictions exercise (claim, predict, declare, argue, deny + would), with new sentences. In item 2, <i>next year</i> becomes <i>the next year</i> or <i>the following year</i>. Read the writing at home and choose two mistakes to discuss in class.</p>""")

    b.extra("Audio script", f"""
{sub("63.1", "Danny's blog: predictions that went wrong (natural and slow; read by Danny)")}
<p style="font-size:8.4pt">The audio is the text on page 2, read in full.</p>
{sub("63.2", "Repeat: the before vowels and consonants")}
<p>{" · ".join(S632)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 63 - Predictions")
