# Speak! Progress B1 - Unit 48 "Taking time out of your relationship" (all English) - lean B1 format
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
setup(band="B1 · UNIT 48", audio_json="audio_b1-unit-48.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-48"]
TX = json.load(open("text.json"))
S482 = [x.split(": ", 1)[1] for x in _r["48.2 Repeat: idioms"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'
    def lines(n):
        return '<div class="wline"></div>' * n
    def paras(t):
        ps = t.split("\n")
        return "".join(f"<p style='margin:0 0 .9mm'>{'<b>' + p + '</b>' if i == 0 or i == len(ps) - 1 else p}</p>" for i, p in enumerate(ps))

    # Page 1 - Warm-up
    cover = cover_html(T, "LEVEL B1 · UNIT 48", "<span style=\"font-size:.72em\">Taking time out of your relationship</span>", "Relationships and personal goals · <b>He asked me what I wanted</b>",
                       [("YOU CAN", "understand and give advice about relationships, and report questions and requests"),
                        ("LANGUAGE", "compromise · mundane · pursue · stuck in a rut · a heart to heart · asked if · told me to"),
                        ("PRONUNCIATION", "linking in idioms: stuck_in_a rut · once_in_a blue moon")])
    kw = [("very ordinary and therefore not interesting", "mundane"),
          ("honest and clear about what you think and want", "upfront"),
          ("an agreement where each person accepts a little less than they wanted", "compromise"),
          ("to work for a long time to get something you really want", "pursue"),
          ("a situation that never changes and is therefore boring", "monotony"),
          ("happy because you are getting what you want from life", "fulfilled")]
    kwl = "".join(f'<li>{A(w, "min-width:24mm")} <span style="color:#6b7377">= {d}</span></li>' for d, w in kw)
    b.page(f"""{sec(1, "Warm-up: relationships today", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["How have relationships changed in the last ten years?", "Is it important to have the same interests as your partner?", "Do you have a bucket list? What's on it?"], "START TALKING")}</div></div>
{sub("A", "Key words. Write the words from the box next to the definitions.", "3 min")}
<div class="bank">{" · ".join(sorted(w for d, w in kw))}</div>
<ol style="font-size:8.8pt;line-height:1.75;margin:0">{kwl}</ol>
{talk(["What dream would you like to pursue?", "What compromises would you never make in a relationship?", "Which part of your week is the most mundane? How could you change it?"], "USE THE WORDS")}""",
    28, """<ol><li>Top box: 3 minutes. Check <i>bucket list</i> (things you want to do before you die) and <i>compromise</i>. Keep it general: the student doesn't need to talk about their own relationship.</li>
<li>A: 4 minutes with the questions. <i>compromise</i> is a false friend for Brazilians: it is not an appointment (that's <i>a commitment</i> or <i>plans</i>).</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Reading (also on audio): an advice column, Dear Jo: should we take a break? · choose the title · true, false or not given · Talk about it",
                      "reported questions (if / whether, wh- + statement word order) and reported requests and orders (ask / tell somebody (not) to)", "Report the questions and requests · Use it (oral)",
                      "idioms (48.2) · be the columnist: give advice and report the letter · long turn: relationship breaks, yes or no?", "idioms in a story about Rafa · report questions · watch out · writing a letter to Dear Jo"),
        """The Linguahouse lesson has a short monologue about a couple who spend a summer apart, vocabulary (upfront, fulfilled, pursue, monotony, mundane, compromise), a magazine article on relationship breaks based on BBC and Guardian reports with a real expert, idioms and a discussion. We replaced the article with an original advice column (a fictional reader from Curitiba and a fictional columnist, Jo), so there are no unverified facts or real people; the vocabulary, the idioms and the topic stay. The reader has been married for twelve years and feels stuck in a rut; after a heart to heart, her husband asked her what she wanted and if she wanted to go alone to a three-month cooking course in Lisbon. Jo: a step in the right direction; be upfront, agree on money, calls and an end date. New grammar: reported questions and requests (reported statements were in Unit 22). Homework: Rafa joined a jazz band (Unit 47).""",
        """Question word order in reported questions (<i>He asked me what did I want</i>); <i>say me / told to me</i>; <i>told me don't worry</i>; no tense change. Vocabulary: <i>compromise</i> (false friend), <i>discuss about</i>. Pronunciation: linking in idioms.""",
        "Track 48.1 Dear Jo: should we take a break? (the reading, natural and slow; Host) · Track 48.2 Repeat: idioms"))

    # Page 2 - Reading
    tf = [("The couple have been together since college.", "T"), ("The writer is unhappy with her job.", "NG"),
          ("Her husband got angry when she told him about her dream.", "F"), ("Her sister thinks the break is a good idea.", "F"),
          ("Jo says they should agree on money, calls and an end date.", "T"), ("Jo thinks three months is too long.", "F")]
    tfl = "".join(f"<li>{s} {A(a, 'min-width:8mm')}</li>" for s, a in tf)
    b.page(f"""{sec(2, "Reading: Dear Jo", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Read the advice column. Which is the best title for Jo's answer?", "2 min")}
<p style="margin:.3mm 0;font-size:8.6pt"><b>a</b> A recipe for disaster &nbsp; <b>b</b> A step in the right direction &nbsp; <b>c</b> A selfish move &nbsp; {A("b", "min-width:8mm")}</p></div>{img('B', 30, 18)}</div>
<div style="display:flex;gap:4mm;font-size:8.1pt;line-height:1.36;margin:.8mm 0">
<div class="box" style="flex:1;margin:0;padding:2mm 2.5mm">{paras(TX["L"])}</div>
<div class="box sand" style="flex:1.35;margin:0;padding:2mm 2.5mm">{paras(TX["J"])}</div></div>
{audiocard(["48.1 · NATURAL", "48.1 · SLOW"])}
{sub("B", "True (T), false (F) or not given (NG)?", "4 min")}
<ol style="line-height:1.45;font-size:8.5pt;margin:0;columns:2;column-gap:6mm">{tfl}</ol>
{talk(["Do you agree with Jo? Would you give the same advice?", "Can a relationship break work? When would it not work?", "Do you know anyone who took a break from something (a job, a city, a relationship)? Did it help?"])}""",
    30, """<ol><li>A: 2 minutes, skim only. B: ask the student to underline the evidence. Item 2: she never says she hates her job; it's her routine. You can also play the audio while the student reads.</li>
<li>Find the idioms in the text: <i>stuck in a rut, a heart to heart, one foot out the door, a step in the right direction, the root of the problem, take a breather, once in a blue moon, a new chapter</i>. They come back on page 5 and in the homework.</li>
<li>Talk about it: 4 minutes. Keep it general if the student prefers.</li></ol>""")

    # Page 3
    lean.grammar_in_class(b, grammar_ref.reported_questions)

    # Page 4 - Practice
    rq = [("\"Are you happy here?\" Ana asked Carol.", "Ana asked Carol if / whether she was happy there."),
          ("\"Where do you want to go?\" he asked me.", "He asked me where I wanted to go."),
          ("\"When will you come back?\" my sister asked.", "My sister asked (me) when I would come back."),
          ("\"Please call me every night,\" she told him.", "She asked him to call her every night."),
          ("\"Don't worry about the money,\" he told her.", "He told her not to worry about the money."),
          ("\"Have you booked your flight?\" Mom asked me.", "Mom asked me if / whether I had booked my flight.")]
    rql = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rq)
    use = ["What did someone ask you this week? What did you answer?", "Has anyone ever asked you to keep a secret? Did you keep it?",
           "What did your parents always tell you to do (or not to do) when you were a teenager?", "Think of a job interview or a first date. What did they ask you?",
           "Report three questions I asked you today."]
    b.page(f"""{sec(4, "Practice: what did they ask?", "10 min")}
{sub("A", "Report the questions and requests.", "6 min")}
<ol style="line-height:1.45;font-size:8.7pt;margin:0">{rql}</ol>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    30, """<ol><li>A: 6 minutes. Check word order first, then the tense. Item 1: <i>here → there</i>. Item 4: a request with <i>please</i> → <i>asked him to</i>.</li>
<li>Use it: 4 minutes, all oral. The last question works best at the end of the class: ask two or three questions earlier and see if the student remembers them.</li></ol>""")

    # Page 5 - Speaking
    card = f"""<div class="box" style="margin-top:1mm;font-size:8.2pt">{R("<b>Teacher's card (B):</b> read this letter aloud: <i>Dear Jo, my boyfriend got a job offer in Canada for six months. He asked me if I would wait for him. My mother told me not to accept, and my best friend asked me why I wanted a long-distance relationship. I love him, but I'm not sure. What should I do? Confused in Recife.</i> The student gives advice as Jo. Then ask: <i>What did Confused ask? What did her mother tell her?</i>: the student reports.")}</div>""" if T else ""
    b.page(f"""{sec(5, "Speaking: dear Jo", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.2pt"><tr><th>giving advice</th><th>warning</th><th>reporting</th><th>idioms</th></tr>
<tr><td><i>If I were you, I'd… · Why don't you…? · It might be a good idea to…</i></td><td><i>Be careful not to… · Make sure you… · Otherwise…</i></td><td><i>She asked me if… · He wanted to know why… · They told me to…</i></td><td><i>stuck in a rut · a heart to heart · take a breather · a new chapter</i></td></tr></table></div>
{audiocard(["48.2"])}
{sub("A", "Listen and repeat. Link the words: stuck_in_a rut · once_in_a blue moon.", "3 min", "48.2")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S482))}</p>
{sub("B", "Be the columnist. Your teacher reads you a letter. Give advice like Jo. Then report what the reader asked and what people told her.", "7 min")}{card}
{sub("C", "Long turn. \"Taking a break from a relationship, a job or a city is a good idea.\" Agree or disagree? Give two reasons and an example.", "5 min")}
<p style="margin:.3mm 0;font-size:8.5pt">Plan (1 min): {lines(1)}</p>
{talk(["Do you think relationship breaks appeal only to young couples? Why?"], "TALK ABOUT IT")}""",
    30, """<ol><li>A: the idioms from the reading, with linking.</li>
<li>B practices advice and the grammar together. C: 1 minute to plan, 2 minutes to talk; the student can choose to talk about a job or a city instead of a relationship. Last 3 minutes: wrap-up (two corrections, and ask <i>Can you now give advice and report questions and requests?</i>).</li></ol>""")

    # Homework
    gaps = ["stuck in a rut", "once in a blue moon", "a heart to heart", "take a breather", "a new chapter"]
    g = [A(x, "min-width:26mm") if T else '<span style="display:inline-block;min-width:26mm;border-bottom:.6pt solid #555">&nbsp;</span>' for x in gaps]
    rw2 = [("\"Do you like your new job?\" Ana asked Danny.", "Ana asked Danny if / whether he liked his new job."),
           ("\"What time does your class start?\" Bruno asked me.", "Bruno asked me what time my class started."),
           ("\"Don't be late!\" the director told Danny.", "The director told Danny not to be late.")]
    rwl2 = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw2)
    bank = sorted(gaps, key=lambda x: x[2:] if x.startswith("a ") else x)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Complete Rafa's story with the idioms from the box.", "")}
<div class="bank" style="font-size:8.6pt">{" · ".join(bank)}</div></div>{img('C', 30, 19)}</div>
<div class="box" style="line-height:1.9;font-size:8.8pt;margin:.5mm 0">Last year Rafa felt really down: the same tours, the same routine, every single day. He was {g[0]}. One night he called his older brother, something he does only {g[1]} because they live far apart. They talked for hours and had a real {g[2]}. His brother told him to go somewhere quiet for a weekend to {g[3]}. Rafa came back with a plan and started {g[4]}: he joined a jazz band!</div>
{sub("B", "Report the questions and orders.", "")}
<ol style="line-height:1.5;font-size:8.7pt;margin:0">{rwl2}</ol>
{lean.watch_out([("He asked me what did I want.", "He asked me what I wanted.", "reported questions: subject + verb, no <i>did</i>."), ("She said me to wait.", "She told me to wait.", "<i>tell</i> + person; <i>say</i> without a person."), ("We discussed about the problem.", "We discussed the problem.", "<i>discuss</i> has no preposition.")])}
{lean.writing_task(sub, "Write a letter to Dear Jo about a problem (real or invented): work, family, friends or a relationship.", "Dear Jo, I need your advice.", ["what the problem is", "a conversation: what someone asked you and what they told you to do", "two idioms from the unit", "your question for Jo", "100–150 words"], "I can understand and give advice about relationships, and report questions and requests.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class. Next class: read the student's letter and answer it together, as Jo. Choose two mistakes to discuss.</p>""")

    b.extra("Audio script", f"""
{sub("48.1", "Dear Jo: should we take a break? (the reading, natural and slow; Host)")}
<p>The audio is the text on page 2, read in full.</p>
{sub("48.2", "Repeat: idioms")}
<p>{" · ".join(S482)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 48 - Taking time out of your relationship")
