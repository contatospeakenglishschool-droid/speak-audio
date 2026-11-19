# Speak! Progress B1 - Unit 12 "A room with a view" (all English) - lean B1 format (rebuilt 2026-11-19)
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
setup(band="B1 · UNIT 12", audio_json="audio_b1-unit-12.json", img_dir="img")
_r = json.load(open("roteiro.json"))["units"]["b1-unit-12"]
_rep = [("nineteen eighty-one", "1981"), ("twenty eighteen", "2018"), ("forty-two", "42"), ("sixty-five", "65"), ("the United Kingdom", "the UK")]
def _num(s):
    for a, c in _rep:
        s = s.replace(a, c)
    return s
PARAS = [_num(l.split(": ", 1)[1]) for l in _r["12.1 A room with a view"].split("\n")][1:]
S122 = [x.split(": ", 1)[1] for x in _r["12.2 Repeat: must, might, can't"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'

    # 1 Warm-up
    cover = cover_html(T, "LEVEL B1 · UNIT 12", "A room with a view", "Windows, views and older people · <b>must, might, can't</b>",
                       [("YOU CAN", "understand an article about research, describe a view and speculate about people"),
                        ("LANGUAGE", "nosy · urban · set up · be up to · She must be at work. · It can't be Frank."),
                        ("PRONUNCIATION", "must, might and can't in connected speech")])
    kw = [("very important, necessary", "vital"), ("not important at all", "insignificant"), ("too curious about other people's lives", "nosy"),
          ("unkind or unpleasant to other people", "mean"), ("in or related to a city", "urban"), ("in an area of houses outside the center of a city", "suburban")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:20mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Warm-up: through the window", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["Does your home have many windows? What can you see through them?", "Do you ever watch people in the street? What do you notice?", "Look at the photo. Who do you think this woman is? What is she looking at?"], "START TALKING")}</div></div>
{sub("A", "Key words. Write the words from the box next to the definitions.", "3 min")}
<div class="bank">insignificant · mean · nosy · suburban · urban · vital</div>
<div style="font-size:8.6pt">{twocol(kwl, 3)}</div>
{talk(["Is your neighborhood urban or suburban? Do you like it?", "Do you have a nosy neighbor? What do they do?"], "USE THE WORDS")}""",
    26, """<ol><li>Top box: accept guesses for question 3; don't correct the modals yet.</li>
<li>A: <i>mean</i> = unkind (also the verb <i>mean</i>, a different word).</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Article: older people and their windows · true or false · answer the questions · Talk about it", "Modals of deduction: must, might, could, can't",
                      "How sure? · make deductions · Use it (oral)", "Functional language · must, might, can't (12.2) · photo story",
                      "Ana's email about Grandma Lourdes · phrasal verbs · word choice · writing", "Reading"),
        "The Linguahouse lesson is a reading based on an article by Charles Musselwhite (Swansea University) in <i>The Conversation</i>, December 2018. We wrote our own shorter text with the verified facts: Graham Rowles's 1981 research on older people watching their neighborhood from the window; Musselwhite interviewed 42 people in the UK, all over 65, who went outside less than once a week; they liked change and views with different levels, invented stories about people outside, worried about seeming nosy; a UK care home uses a video of a train journey as a virtual window. Sources: theconversation.com (2018) and <i>Quality in Ageing and Older Adults</i> 19(4), 2018. The audio is read by the Host. In the homework, Ana writes to Tom about Grandma Lourdes (96) and her window.",
        "Students say <i>mustn't</i> for an impossible deduction (use <i>can't</i>), use <i>can</i> for a present possibility (use <i>could / might</i>), add <i>to</i> after <i>must</i>, say <i>vision</i> for <i>view</i>, and use <i>curious</i> when they mean <i>nosy</i>.",
        "Track 12.1 A room with a view (article, natural and slow) · Track 12.2 Repeat: must, might, can't"))

    # 2 Reading
    bf = [("Windows are very important to older people who spend a lot of time indoors.", "T"), ("Only views of nature are interesting for older people.", "F (city views matter too)"),
          ("Older people often invent stories about the people they see.", "T"), ("Most of them like telling others about their window-watching.", "F (a secret)")]
    bfl = [f'<li value="{i+1}">{s} {A(a, "min-width:9mm")}</li>' for i, (s, a) in enumerate(bf)]
    qs = [("Who were the 42 interviewees?", "UK people over 65 who rarely went out"), ("What did they love most about their views?", "change"),
          ("How can technology help?", "a virtual window (a video of a train journey)")]
    qsl = [f'<li value="{i+1}">{q} {A(a, "min-width:20mm")}</li>' for i, (q, a) in enumerate(qs)]
    art = "".join(f'<p style="margin:0 0 .8mm"><b style="color:#176074">{i+1}</b> {p}</p>' for i, p in enumerate(PARAS))
    b.page(f"""{sec(2, "Reading: a room with a view", "12 min")}
{sub("A", "Before you read. True or false? Guess. Then read the article and check.", "3 min")}
<div style="font-size:8.4pt">{twocol(bfl, 2)}</div>
<div class="box" style="margin:.5mm 0 0;font-size:7.9pt;line-height:1.32;column-count:2;column-gap:4mm"><b style="font-size:9.5pt">A room with a view</b><br>{art}</div>
<div style="display:flex;gap:3mm;align-items:center;margin-top:1mm"><div style="flex:1">{audiocard(["12.1 · NATURAL", "12.1 · SLOW"])}</div>{img('B', 36, 20)}</div>
{sub("B", "Read again and answer.", "3 min")}
<div style="font-size:8.4pt">{twocol(qsl, 2)}</div>
{talk(["Why do you think the interviewees kept their window-watching a secret?", "&ldquo;Homes should be organized around the window, not the TV.&rdquo; Do you agree?", "How can families help older relatives feel connected to the world?"])}""",
    24, """<ol><li>A–B: 6 minutes. Let the student guess first. They can read and listen (12.1). The article is based on real research (see the story box).</li>
<li>Talk about it: 6 minutes. 1: they didn't want neighbors to think they were nosy.</li></ol>""")

    # 3 Grammar reference
    lean.grammar_in_class(b, grammar_ref.modals_deduction)

    # 4 Practice
    ex = [("She <u>must</u> be at work. Her car isn't here.", "100% sure: yes"), ("He <u>might</u> be a manager. He's wearing a suit.", "possible"),
          ("That <u>can't</u> be Frank. Frank is on vacation.", "100% sure: no")]
    exl = "".join(f"<li>{s} {A(a, 'min-width:24mm')}</li>" for s, a in ex)
    use = ["Your teacher isn't at home tonight. Where could they be?", "Look at a photo on your phone. Make two deductions about the people.", "Someone is knocking at your door at 11 p.m. Who might it be?",
           "Your friend hasn't answered your messages for two days. Why?", "Your teacher describes a person. Guess their job with <i>must / might / can't</i>."]
    b.page(f"""{sec(4, "Practice: must, might, can't", "10 min")}
{sub("A", "How sure is the speaker? Write 100% sure: yes, possible or 100% sure: no.", "2 min")}
<ol style="line-height:1.75;font-size:8.9pt;margin:0">{exl}</ol>
{sub("B", "Correct or incorrect? Choose.", "2 min")}
<ol style="line-height:1.6;font-size:8.9pt;margin:0"><li>She mustn't be at home. The lights are off. {ch(["correct", "incorrect"], "incorrect")} {R("→ She can't be at home.") if T else ""}</li><li>He must to live nearby. {ch(["correct", "incorrect"], "incorrect")} {R("→ He must live nearby.") if T else ""}</li></ol>
<div class="box sand"><h4>RULE</h4><b>must</b> = I'm sure it's true; <b>might / may / could</b> = it's possible; <b>can't</b> = I'm sure it's not true. After the modal: base form (<i>must be</i>) or <b>be + -ing</b> for now (<i>must be waiting</i>). No <i>to</i>. See the <b>Grammar reference</b> on page 3.</div>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    24, """<ol><li>A–B: 4 minutes. Draw a line from 0% to 100% and place the modals on it.</li>
<li>Use it: 6 minutes, all oral. Ask <i>Why do you think so?</i> to get the evidence.</li></ol>""")

    # 5 Speaking
    b.page(f"""{sec(5, "Speaking: the view from my window", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>describe a view</th><th>speculate</th><th>give evidence</th><th>react</th></tr>
<tr><td><i>In the foreground… · In the distance… · On the left / right… · Right in front of…</i></td><td><i>He must / might / can't be… · I bet… · I wonder what…</i></td><td><i>…because he's wearing… · Judging by… · He looks like…</i></td><td><i>You could be right. · I'm not so sure. · No way!</i></td></tr></table></div>
{audiocard(["12.2"])}
{sub("A", "Listen and repeat. The t in must often disappears; can't is always stressed.", "4 min", "12.2")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.55">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S122))}</p>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("B", "Photo story. Look at the man in the photo. Who is he? What's he doing? What happened before? Tell a short story with your teacher. Then describe the view from your window and the people you often see.", "10 min")}
<p style="margin:.3mm 0;font-size:8.6pt">{R("Teacher: model first: He must be waiting for someone. He's checking his watch, so the other person might be late… If there's a window, use the real view.") if T else ""}</p></div>{img('D', 32, 24)}</div>
{talk(["Would a virtual window be a good idea for people who can't go out? Why?", "Is it nosy to watch your neighbors? Where is the line?"])}""",
    28, """<ol><li>A: <i>can't</i> /kænt/ is long and stressed; <i>can</i> is short /kən/. B: push for <i>be + -ing</i> (<i>must be waiting</i>) and evidence.</li>
<li>Last 3 minutes: wrap-up (two corrections and <i>Can you make deductions about people?</i>).</li></ol>""")

    # H Homework
    pc = [(["view", "vision"], "view"), (["set up", "backed up"], "set up"), (["must", "can't"], "must"), (["might", "can't"], "can't"),
          (["could be", "must to be"], "could be"), (["nosy", "curious"], "nosy")]
    p = [ch(o, a) for o, a in pc]
    pv = [("Windows <b>let in</b> light and air.", "allow to enter"), ("What are you <b>up to</b> this weekend?", "doing"), ("She <b>set up</b> her armchair by the window.", "arranged")]
    pvl = "".join(f"<li>{s} {A(m, 'min-width:22mm')}</li>" for s, m in pv)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Ana writes to Tom about her grandmother. Choose the correct words.", "")}</div>{img('C', 28, 18)}</div>
<div class="box" style="line-height:1.8;font-size:8.8pt;margin:.5mm 0">Hi Tom! Grandma Lourdes has a lovely {p[0]} of the street, and she's {p[1]} her armchair right next to the window. Yesterday she pointed at a young man with flowers and said, "He {p[2]} be in love!" Then a woman in a suit went into the building opposite. "She {p[3]} live there," Grandma said. "She only comes on Mondays. She {p[4]} a lawyer… or a spy!" My brother says she's {p[5]}, but I think it's her way to stay connected. Love, Ana</div>
{sub("B", "What do the phrasal verbs mean? Write a word or two.", "")}
<ol style="line-height:1.5;font-size:8.6pt;margin:0">{pvl}</ol>
{lean.watch_out([("I have a beautiful vision from my window.", "I have a beautiful view from my window.", "<i>vision</i> = eyesight or a plan."), ("My neighbor is very curious about my life.", "My neighbor is very nosy.", "<i>nosy</i> = too interested in others."), ("Old people need a good view.", "Older people need a good view.", "<i>older people</i> is more polite.")])}
{lean.writing_task(sub, "The view from my window: describe the view from a window in your home, school or office, and the people you see.", "Right in front of my window, there's… In the distance, I can see… There's a man who… He must be…", ["near and far", "how it changes", "three deductions", "100–150 words"], "I can describe a view and make deductions about people.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class (ask the student for the evidence behind each modal). When you correct the writing, check: no <i>to</i> after modals, <i>can't</i> not <i>mustn't</i>.</p>""")

    b.extra("Audio script", f"""
{sub("12.1", "A room with a view (article, natural and slow)")}
<div style="line-height:1.35;font-size:8.7pt"><p><b>A room with a view</b></p>{"".join(f"<p style='margin:.6mm 0'>{p}</p>" for p in PARAS)}</div>
{sub("12.2", "Repeat: must, might, can't")}
<p>{" · ".join(S122)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 12 - A room with a view")
