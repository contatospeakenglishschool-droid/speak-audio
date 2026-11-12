# Speak! Progress B1 - Unit 12 "A room with a view" (all English) - B1 format (2026-11-09)
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Progress"
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
    def lines(n):
        return '<div class="wline"></div>' * n

    # Page 1 - Warm-up
    cover = cover_html(T, "LEVEL B1 · UNIT 12", "A room with a view", "Windows, views and older people · <b>must, might, can't</b>",
                       [("YOU CAN", "understand an article about research, describe a view and speculate about people"),
                        ("LANGUAGE", "nosy · urban · set up · be up to · She must be at work. · It can't be Frank."),
                        ("PRONUNCIATION", "must, might and can't in connected speech")])
    kw = [("very important, necessary", "vital"), ("not important at all", "insignificant"), ("to be able to get, use or experience something", "access"),
          ("a person who answers questions in an interview or a study", "an interviewee"), ("too curious about other people's lives", "nosy"),
          ("unkind or unpleasant to other people", "mean"), ("in or related to a city", "urban"), ("in an area of houses outside the center of a city", "suburban")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:20mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Warm-up: through the window", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 58, 38)}<div style="flex:1">
{sub("A", "Discuss with your teacher.", "3 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0"><li>Does your home have many windows? What can you see through them?</li><li>Do you ever watch people in the street? What do you notice?</li><li>Look at the photo. Who do you think this woman is? What is she looking at?</li></ol></div></div>
{sub("B", "Key words. Write the words from the box next to the definitions.", "4 min")}
<div class="bank">access · an interviewee · insignificant · mean · nosy · suburban · urban · vital</div>
<div style="font-size:8.6pt">{twocol(kwl, 4)}</div>
{sub("C", "Is your neighborhood urban or suburban? Do you have a nosy neighbor?", "1 min")}""",
    25, """<ol><li>A: accept guesses for question 3; don't correct the modals yet, they come on page 3.</li>
<li>B: <i>access</i> is a verb here (<i>access the world</i>) and a noun (<i>have access to</i>). <i>Mean</i> = unkind (also the verb <i>mean</i>, a different word).</li></ol>""", cover=cover)

    b.extra("Lesson overview · 60 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Discussion · key words from the article</td><td>1</td></tr>
<tr><td>2 Reading</td><td>12 min</td><td>Article: why a room with a view matters to older people</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>8 min</td><td>Modals of deduction: must, might, could, can't</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Must, might, can't (study at home)</td><td>4</td></tr>
<tr><td>4 Vocabulary lab + pronunciation</td><td>8 min</td><td>Phrasal verbs from the article · word choice · must / might / can't</td><td>5</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Ana's email: Grandma Lourdes's window · deductions</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Speculating · long turn: the view from my window · photo story · talking point</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>4 min</td><td>Can-do · language notes · writing homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY</h4>The Linguahouse lesson is a reading based on an article by Charles Musselwhite (Swansea University) in <i>The Conversation</i>, December 2018. We wrote our own shorter text with the verified facts: Graham Rowles's 1981 research on older people watching their neighborhood from the window; Musselwhite interviewed 42 people in the UK, all over 65, who went outside less than once a week; they liked change and views with different levels, invented stories about people outside, worried about seeming nosy; a UK care home uses a video of a train journey as a virtual window. Sources: theconversation.com ("Why windows with a view are so important to older people", 2018) and the paper in <i>Quality in Ageing and Older Adults</i> 19(4), 2018. The audio is read by the Host. In Practice, Ana writes to Tom about Grandma Lourdes (96, A2 Bridge) and her window; in the writing model, Danny describes the view from his hostel room.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students say <i>mustn't</i> for an impossible deduction (use <i>can't</i>), use <i>can</i> for a present possibility (use <i>could / might</i>), add <i>to</i> after <i>must</i>, say <i>vision</i> for <i>view</i>, and use <i>curious</i> when they mean <i>nosy</i>.</div>
<div class="box"><h4>AUDIO</h4>Track 12.1 A room with a view (article, natural and slow) · Track 12.2 Repeat: must, might, can't</div>""")

    # Page 2 - Reading
    bf = [("Windows are very important to older people who spend a lot of time indoors.", "T"), ("Only views of nature are interesting for older people.", "F (city views matter too)"),
          ("Older people often invent stories about the people they see.", "T"), ("Most of them like telling others about their window-watching.", "F (they kept it a secret)")]
    bfl = [f'<li value="{i+1}">{s} {A(a, "min-width:9mm")}</li>' for i, (s, a) in enumerate(bf)]
    qs = [("What was Rowles's discovery in 1981?", "They took part in community life from the window."), ("Who were the 42 interviewees?", "UK people over 65 who rarely went out."),
          ("What did they love most about their views?", "Change, expected and unexpected."), ("What kind of view did they prefer?", "Views with different levels: near and far."),
          ("How can technology help?", "A virtual window, e.g. a video of a train journey.")]
    qsl = [f'<li value="{i+1}">{q} {A(a, "min-width:20mm")}</li>' for i, (q, a) in enumerate(qs)]
    art = "".join(f'<p style="margin:0 0 .8mm"><b style="color:#176074">{i+1}</b> {p}</p>' for i, p in enumerate(PARAS))
    b.page(f"""{sec(2, "Reading: a room with a view", "12 min")}
{sub("A", "Before you read. True or false? Guess. Then read the article and check.", "3 min")}
<div style="font-size:8.5pt">{twocol(bfl, 2)}</div>
<div class="box" style="margin:.5mm 0 0;font-size:8pt;line-height:1.33;column-count:2;column-gap:4mm"><b style="font-size:9.5pt">A room with a view</b><br>{art}</div>
<div style="display:flex;gap:3mm;align-items:center;margin-top:1mm"><div style="flex:1">{audiocard(["12.1 · NATURAL", "12.1 · SLOW"])}</div>{img('B', 36, 20)}</div>
{sub("B", "Read again and answer the questions.", "4 min")}
<div style="font-size:8.5pt">{twocol(qsl, 3)}</div>
{sub("C", "Think about it. Discuss with your teacher.", "4 min")}
<ol style="line-height:1.4;font-size:8.7pt;margin:0"><li>Why do you think the interviewees kept their window-watching a secret? {R("They didn't want neighbors to think they were nosy.") if T else ""}</li>
<li>"Homes should be organized around the window, not the TV." Do you agree?</li></ol>
<div class="box sand" style="margin-top:1mm"><h4>NOTICE: USEFUL CHUNKS</h4><i>and that's it · Back in 1981, … · In this way, … · just as interesting · make sense of · However, … · His main message, though, is simple.</i></div>""",
    21, """<ol><li>A: let the student guess first; the reading then has a purpose. They can read and listen (12.1) at the same time.</li>
<li>The article is based on real research (see the story box). <i>Carers</i> = people who look after the elderly or sick.</li></ol>""")

    # Page 3 - Language focus
    ex = [("She <u>must</u> be at work. Her car isn't here.", "100% sure: yes"), ("He <u>might</u> be a manager. He's wearing a suit.", "possible"),
          ("It <u>could</u> be his sister. They look alike.", "possible"), ("That <u>can't</u> be Frank. Frank is on vacation.", "100% sure: no")]
    exl = "".join(f"<li>{s} {A(a, 'min-width:24mm')}</li>" for s, a in ex)
    dd = [("The lights are off.", "They must be out / can't be at home."), ("He's checking his watch every minute.", "He must be waiting for someone."),
          ("She's carrying a big bag and a map.", "She might be a tourist."), ("He's only 20.", "He can't be the manager.")]
    ddl = "".join(f"<li>{s} {A(r, 'min-width:44mm')}</li>" for s, r in dd)
    b.page(f"""{sec(3, "Language focus: must, might, can't", "8 min")}
{sub("A", "The interviewees made guesses about people. How sure is the speaker? Write 100% sure: yes, possible or 100% sure: no.", "3 min")}
<ol style="line-height:1.75;font-size:8.9pt;margin:0">{exl}</ol>
{sub("B", "Make a deduction about each person. Use must, might, could or can't.", "3 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0">{ddl}</ol>
{sub("C", "Correct or incorrect? Choose.", "2 min")}
<ol style="line-height:1.6;font-size:8.9pt;margin:0"><li>They must be waiting for the bus. {ch(["correct", "incorrect"], "correct")}</li><li>She mustn't be at home. The lights are off. {ch(["correct", "incorrect"], "incorrect")} {R("→ She can't be at home.") if T else ""}</li><li>He must to live nearby. {ch(["correct", "incorrect"], "incorrect")} {R("→ He must live nearby.") if T else ""}</li></ol>
<div class="box sand"><h4>RULE</h4>For deductions about the present: <b>must</b> = I'm sure it's true; <b>might / may / could</b> = it's possible; <b>can't</b> = I'm sure it's not true. After the modal, use the base form (<i>must be, might know</i>) or <b>be + -ing</b> for now (<i>must be waiting</i>). No <i>to</i>. More on the next page: <b>Grammar reference</b>.</div>""",
    24, """<ol><li>A: draw a line from 0% to 100% and ask the student to place the four modals on it.</li>
<li>B: accept any logical deduction; ask <i>Why do you think so?</i> to get the evidence.</li></ol>""")

    grammar_ref.modals_deduction(b)

    # Page 5 - Vocabulary lab
    pv = [("Many of them <b>set up</b> their furniture to get the best view.", "organize or arrange"), ("What they saw <b>backed up</b> what they heard on the news.", "confirm or support"),
          ("They wondered what people might <b>be up to</b>.", "be doing (often something secret)"), ("Windows <b>let in</b> light and air.", "allow to enter"),
          ("She told a young man to <b>tuck in</b> his shirt.", "put the end inside your pants"), ("…and to <b>pull up</b> his pants.", "lift clothes that are too low")]
    mn = ["allow to enter", "be doing (often something secret)", "confirm or support", "lift clothes that are too low", "organize or arrange", "put the end inside your pants"]
    mnl = " &nbsp; ".join(f"<b>{chr(97+i)}</b> {m}" for i, m in enumerate(mn))
    pvl = "".join(f"<li>{s} {A(chr(97 + mn.index(m)), 'min-width:6mm')}</li>" for s, m in pv)
    b.page(f"""{sec(4, "Vocabulary lab: phrasal verbs", "4 min")}
{sub("A", "Match the phrasal verbs in bold to the meanings a–f.", "2 min")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.6">{mnl}</p>
<ol style="line-height:1.55;font-size:8.7pt;margin:0">{pvl}</ol>
{sub("B", "Ask and answer with your teacher.", "2 min")}
<ol style="line-height:1.45;font-size:8.7pt;margin:0;column-count:2"><li>How is your living room set up?</li><li>Do your windows let in a lot of light?</li><li>What are you up to this weekend?</li><li>Do you tuck in your shirt for work?</li></ol>
<div class="box sand"><h4>WATCH OUT: WORD CHOICE</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>I have a beautiful vision from my window.</td><td><b>I have a beautiful view from my window.</b></td><td><i>view</i> = what you see from a place; <i>vision</i> = your eyesight or a plan for the future.</td></tr>
<tr><td>My neighbor is very curious about my life.</td><td><b>My neighbor is very nosy.</b></td><td><i>curious</i> is neutral or positive; <i>nosy</i> = too interested in other people's lives.</td></tr>
<tr><td>Old people need a good view.</td><td><b>Older people need a good view.</b></td><td><i>older people</i> or <i>the elderly</i> is more polite.</td></tr></table></div>
{sec(5, "Pronunciation lab: must, might, can't", "4 min")}
<p class="small" style="margin:.3mm 0">In fast speech, the <i>t</i> in <i>must</i> often disappears before a consonant: <i>She mus(t) be…</i> But <b>can't</b> is always stressed, so the listener doesn't hear <i>can</i>.</p>
{audiocard(["12.2"])}
{sub("A", "Listen and repeat. Then look out of a window and make three deductions about what you see.", "4 min", "12.2")}
<p style="margin:.3mm 0;font-size:8.8pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S122))}</p>""",
    24, """<ol><li>A: <i>pants</i> (American English) = <i>trousers</i> (British English). <i>What are you up to?</i> is also a friendly greeting: <i>Hey, what are you up to?</i></li>
<li>Pronunciation: <i>can't</i> /kænt/ is long and stressed; <i>can</i> is short /kən/.</li></ol>""")

    # Page 6 - Practice
    pc = [(["view", "vision"], "view"), (["set up", "backed up"], "set up"), (["must", "can't"], "must"), (["might", "can't"], "can't"),
          (["could be", "must to be"], "could be"), (["is up to", "is up"], "is up to"), (["nosy", "curious"], "nosy"), (["can't", "mustn't"], "can't"), (["backs up", "lets in"], "backs up")]
    p = [ch(o, a) for o, a in pc]
    dx = [("Sweet Kate Bakery is closed today, and it's a Tuesday.", "Kate might be on vacation / sick."), ("Danny isn't answering his phone. It's Sunday morning.", "He must be giving a tour."),
          ("Bruno is smiling at his phone.", "He could be texting Paula."), ("Mrs. Lima's hostel is full.", "She can't have a free room.")]
    dxl = "".join(f"<li>{s} {A(r, 'min-width:42mm')}</li>" for s, r in dx)
    b.page(f"""{sec(6, "Practice", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Ana writes to Tom about her grandmother. Choose the correct words.", "5 min")}</div>{img('C', 30, 20)}</div>
<div class="box" style="line-height:1.95;font-size:9pt"><b>Subject: Grandma's window</b><br>Hi Tom! I read an article about older people and windows, and it made me think of Grandma Lourdes. She has a lovely {p[0]} of the street from her living room, and she's {p[1]} her armchair right next to the window. Yesterday she pointed at a young man with flowers and said, "He {p[2]} be in love. Look at his face!" Then a woman in a suit went into the building opposite. "She {p[3]} live there," Grandma said. "She only comes on Mondays. She {p[4]} a lawyer… or a spy!" She always wants to know what everyone {p[5]}. My brother says she's {p[6]}, but I think it's her way to stay connected to the world. She {p[7]} be bored with a view like that! And everything she sees {p[8]} what she hears on TV. Love, Ana</div>
{sub("B", "What's going on? Make deductions with must, might, could or can't.", "3 min")}
<ol style="line-height:1.85;font-size:8.8pt;margin:0">{dxl}</ol>""",
    26, """<ol><li>A: Grandma Lourdes is Ana's 96-year-old grandmother (A2 Bridge). Ask the student to justify each modal: what is the evidence?</li>
<li>B: accept any logical answer with the correct form; push for <i>be + -ing</i> (<i>must be giving</i>).</li></ol>""")

    # Page 7 - Speaking
    b.page(f"""{sec(7, "Speaking: the view from my window", "12 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>describe a view</th><th>speculate</th><th>give evidence</th><th>react</th></tr>
<tr><td><i>In the foreground… · In the distance… · On the left / right… · Right in front of…</i></td><td><i>He must / might / can't be… · I bet… · I'd say she's… · I wonder what…</i></td><td><i>…because he's wearing… · Judging by… · He looks like…</i></td><td><i>You could be right. · I'm not so sure. · No way!</i></td></tr></table></div>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("A", "Long turn. Prepare for one minute, then talk for two minutes about the view from your window.", "5 min")}
<ul style="line-height:1.45;font-size:8.9pt;margin:0"><li>what you can see near and far away</li><li>how it changes (seasons, day and night, roadwork…)</li><li>the people you often see, and who you think they are</li><li>your ideal view</li></ul></div>{img('D', 32, 24)}</div>
{sub("B", "Photo story. Look at the man in the photo. Who is he? What's he doing? What happened before? What's going to happen? Tell a short story with your teacher.", "4 min")}
<p style="margin:.3mm 0;font-size:8.6pt">{R("Teacher: model first: He must be waiting for someone. He's checking his watch, so the other person might be late. He's just finished work… Then ask: Who could he be waiting for? Use the present continuous, the past simple and the present perfect with just.") if T else ""}</p>
{sub("C", "Talking point. Discuss with your teacher.", "3 min")}
<ol style="line-height:1.5;font-size:8.9pt;margin:0"><li>How can families help older relatives feel connected to the world?</li><li>Would a virtual window be a good idea? Why or why not?</li><li>Is it nosy to watch your neighbors? Where is the line?</li></ol>""",
    28, """<ol><li>A: don't interrupt; note mistakes for the error log (page 8), especially <i>mustn't</i> / <i>can't</i> and <i>vision</i> / <i>view</i>. Fluency option (3-2-1): the same talk in 2 minutes, then in 1 minute.</li>
<li>B: the Linguahouse picture task. If the classroom (or the student's room) has a window, use the real view instead.</li></ol>""")

    # Page 8 - Wrap-up
    cd = ["I can understand an article about a piece of research.", "I can use must, might, could and can't to make deductions.",
          "I can describe a view and speculate about the people I see."]
    cdr = "".join(f"<tr><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for s in cd)
    b.page(f"""{sec(8, "Wrap-up and homework", "4 min")}
{sub("A", "Can-do check", "1 min")}
<table class="ck" style="font-size:8.6pt"><tr><th>In English…</th><th style="width:16mm">Easy!</th><th style="width:16mm">Sometimes</th><th style="width:16mm">Not yet</th></tr>{cdr}</table>
{sub("B", "My language notes. Write three corrections from today's class.", "2 min")}
<div style="display:flex;gap:5mm;font-size:8.6pt"><div style="flex:1"><b>I said…</b>{lines(3)}</div><div style="flex:1"><b>Better:</b>{lines(3)}</div></div>
{sub("C", "Homework: writing (100–150 words)", "1 min")}
<p style="margin:.3mm 0"><b>The view from my window.</b> Describe the view from a window in your home, school or office, and the people you see. Read Danny's text first.</p>
<div class="box" style="font-size:8.6pt;line-height:1.4;margin:.5mm 0"><i>My room at the hostel isn't big, but it has a great view. Right in front of the window there's a small bakery, and in the distance I can see the tall buildings of Paulista Avenue. In the morning, the street is full of people going to work. There's a man in a gray suit who buys coffee at exactly 7:15 every day. He must be a banker, or he might be a lawyer. He's always in a hurry! In the afternoon, an old woman feeds the birds in the square. She must love them, because she talks to them. At night, the view changes completely: the buildings light up, and it's beautiful. Bruno says I'm nosy. I can't be nosy. I'm a tour guide! Watching people is my job.</i></div>
<p class="small" style="margin:.3mm 0">Checklist: ☐ near and far (<i>in front of, in the distance</i>) &nbsp;☐ how the view changes &nbsp;☐ three deductions (<i>must, might, can't</i>) &nbsp;☐ one phrasal verb &nbsp;☐ 100–150 words</p>
{lines(6)}""",
    30, """<ol><li>B (error log): during the lesson, note 3–5 real mistakes. Here, the student writes what they said and the better version; guide them to self-correct first.</li>
<li>C: check the modals (no <i>to</i>, <i>can't</i> not <i>mustn't</i>) and the description words for near and far.</li></ol>""")

    b.extra("Audio script", f"""
{sub("12.1", "A room with a view (article, natural and slow)")}
<div style="line-height:1.35;font-size:8.7pt"><p><b>A room with a view</b></p>{"".join(f"<p style='margin:.6mm 0'>{p}</p>" for p in PARAS)}</div>
{sub("12.2", "Repeat: must, might, can't")}
<p>{" · ".join(S122)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 12 - A room with a view")
