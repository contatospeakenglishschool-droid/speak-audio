# Speak! Essentials A1 - Unit 33 "Robots" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
from speak_engine import *
setup(band="A1 · UNIT 33", audio_json="audio_a1-unit-33.json", img_dir="img")

PHOTOS = [("A", "as friends", "friend"), ("B", "caring for people", "care"), ("C", "doing housework", "housework"), ("D", "doing operations", "operations"),
          ("E", "exploring space", "space"), ("F", "fighting wars", "wars"), ("G", "helping the police", "police"), ("H", "in education", "education")]

_r = json.load(open("roteiro.json"))["units"]["a1-unit-33"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["33.1 Robots"].split("\n")]
S332 = [x.split(": ", 1)[1] for x in _r["33.2 Repeat word pairs"].split("\n")]
S333 = [x.split(": ", 1)[1] for x in _r["33.3 Repeat sentences"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LEVEL A1 · UNIT 33", "Robots", "The future · <b>will / won't for predictions · certainly, probably, possibly</b>",
                       [("YOU CAN", "make predictions about the future and say how sure you are"),
                        ("LANGUAGE", "Robots will certainly clean our houses. · I don't think robots will teach children."),
                        ("PRONUNCIATION", "won't /woʊnt/ ≠ want /wɑnt/ · I'll /aɪl/ · robot /ˈroʊbɑt/")])
    b.page(f"""{sec(1, "Warm-up: jobs for robots", "8 min")}
{sub("A", "A robot is a machine that works for people. Look at the photos. What can robots do? Write the phrase under each photo.", "3 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(w.replace(" ", "&nbsp;") for _, w, _ in PHOTOS)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Talk about it.", "5 min")}
<ol><li>Which jobs do robots do now? Which jobs are for the future?</li><li>Which jobs can robots do better than people? Why?</li><li>Do you have a robot at home (a robot vacuum cleaner, for example)?</li></ol>""",
    27, """<ol><li>A: drill <b>robot</b> /ˈroʊbɑt/: the first <i>o</i> is long, like in <i>no</i>. Brazilians often stress the last syllable (ro-BOT ✗): the stress is on the first syllable, RO-bot.</li>
<li>B: accept any idea; don't correct the future forms yet. Robot vacuum cleaners are common in Brazil too.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>8 jobs for robots with photos</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Paulo's video: Ana's predictions and a robot for Grandma Lourdes</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>will / won't for predictions · I think, I hope, I believe · certainly, probably, possibly</td><td>3</td></tr>
<tr><td>4 Pronunciation lab</td><td>5 min</td><td>won't ≠ want · weak 'll</td><td>4</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Make predictions · correct the mistakes</td><td>5</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Predictions about robots: agree or disagree? · your future</td><td>6</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>7</td></tr></table>
<div class="box"><h4>HOW THIS GUIDE WORKS</h4>Every page looks like the Student Book page with the same number. Your notes are in the <b>yellow box</b>.
<span class="red">Answers in red</span> are not in the Student Book. The <span class="time">5 min</span> chips show the time for each activity. Audio scripts are on the last page.</div>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Paulo, the photographer, records a video for his channel at Grandma Lourdes' house in Rio Claro. His sister Ana, the doctor, makes predictions about robots: they'll clean our houses and help doctors, but they won't be good teachers. Then Paulo gives Grandma a surprise: Buddy, a small robot for older people. But Buddy doesn't want to play cards… and Lourdes, 96, won't wait for a robot!</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Adding <i>to</i> after <i>will</i>: <i>Robots will to clean</i> ✗ → <b>will clean</b>. Double negatives: <i>I don't think robots won't…</i> ✗ → <b>I don't think robots will…</b> Adverb position: <i>won't probably</i> ✗ → <b>probably won't</b>. And <b>won't</b> /woʊnt/ often sounds like <b>want</b> /wɑnt/: <i>I won't go</i> means the opposite of <i>I want to go</i>!</div>
<div class="box"><h4>AUDIO</h4>Track 33.1 Paulo's video (slow and natural) · Track 33.2 Word pairs · Track 33.3 Sentences</div>""")

    # Page 2
    order = [("cleaning houses", "1"), ("exploring space", "X"), ("helping doctors with operations", "3"), ("teaching children", "2"),
             ("fighting wars", "4"), ("helping older people", "5")]
    ot = "".join(f"<tr><td style='width:12mm;text-align:center'>{A(n, 'min-width:8mm')}</td><td>{j}</td></tr>" for j, n in order)
    adj = [(["important", "interesting", "expensive"], "important", "Robots will certainly be very", "in the next ten years."),
           (["good", "bad", "interesting"], "good", "Robots won't be very", "teachers."),
           (["dangerous", "difficult", "expensive"], "expensive", "Very small robots will probably be very", "at first."),
           (["bad", "dangerous", "important"], "dangerous", "Robots in wars will possibly be", "."),
           (["good", "easy", "ready"], "ready", "I hope he'll be", "next week.")]
    al = "".join(f"<li>{a} {ch(o, r)} {c}</li>" for o, r, a, c in adj)
    b.page(f"""{sec(2, "Listening: robots in the future", "10 min")}
<p>Paulo is recording a video for his channel at Grandma Lourdes' house in Rio Claro. His sister Ana, the doctor, is there too. They're talking about robots.</p>
{audiocard(["33.1 · SLOW", "33.1 · NATURAL"])}
{sub("A", "Listen. Number the jobs 1–5 in the order Ana and Paulo talk about them. One job is extra: write X.", "3 min", "33.1 · SLOW")}
<table style="table-layout:fixed;font-size:9.3pt">{ot}</table>
{sub("B", "Listen again and choose the correct word.", "5 min", "33.1 · NATURAL")}
<ol>{al}</ol>
{sub("C", "What's the problem with Buddy? What does Grandma Lourdes do?", "2 min")}
<div class="wline">{R("Buddy has technical problems: he doesn't want to play cards. Lourdes won't wait: she asks Paulo for the cards.")}</div>""",
    26, """<ol><li>A: <b>slow</b> version. <b>a robot vacuum cleaner</b> cleans the floor alone. <b>an operation</b> = surgery in a hospital.</li>
<li>B: <b>natural</b> version. Some hospitals in Brazil and around the world already use robots in operations. Ask: <i>Do you agree with Ana?</i></li></ol>""")

    # Page 3
    b.page(f"""{sec(3, "Language focus: will for predictions", "10 min")}
{sub("A", "Read the sentences from the video. Then choose the correct option.", "4 min")}
<div class="bank" style="background:#fff;font-weight:600">So I<u>'ll</u> relax on the sofa, and the robot <u>will clean</u> my apartment. · I don't think robots <u>will teach</u> children. · Robots <u>won't be</u> very good teachers. · <u>Will</u> robots <u>be</u> dangerous?</div>
<ol><li>After <i>will</i> and <i>won't</i>, we use the verb {ch(["with to", "without to"], "without to")}.</li>
<li><i>won't</i> = {ch(["will not", "want not"], "will not")}. &nbsp; <i>I'll</i> = {ch(["I will", "I am"], "I will")}.</li>
<li><i>I don't think robots will…</i> is a {ch(["positive", "negative"], "negative")} idea.</li>
<li><i>Will</i> is the same for all people: I / you / he / she / we / they {ch(["will", "wills"], "will")}.</li></ol>
<table style="table-layout:fixed;font-size:9.3pt"><tr><td style="width:28mm"><b>+</b></td><td>Robots <b>will</b> clean our houses. · I<b>'ll</b> relax.</td></tr>
<tr><td><b>–</b></td><td>Robots <b>won't</b> be good teachers.</td></tr>
<tr><td><b>?</b></td><td><b>Will</b> robots teach our children? — Yes, they <b>will</b>. / No, they <b>won't</b>.</td></tr>
<tr><td><b>wh-?</b></td><td>When <b>will</b> robots explore Mars?</td></tr></table>
{sub("B", "How sure are you? Put the adverbs in order: 100% → 50%.", "3 min")}
<p>possibly · certainly · probably &nbsp; → &nbsp; {A("certainly", "min-width:18mm")} 100% · {A("probably", "min-width:18mm")} 80% · {A("possibly", "min-width:18mm")} 50%</p>
<div class="box sand"><h4>PREDICTIONS: USEFUL PHRASES</h4><b>I think / I believe / I predict / I hope</b> robots will help doctors. · <b>I don't think</b> robots will teach children.<br>
Adverbs go <b>after will</b> and <b>before won't</b>: Robots <b>will certainly</b> be important. · They <b>probably won't</b> be good teachers.</div>""",
    26, """<ol><li>A: <i>will</i> is the same for all subjects, like <i>can</i> (Unit 05). The contraction <i>'ll</i> is very weak: say <i>I'll</i> like <i>aisle</i>.</li>
<li>B: ask the student to make one sentence with each adverb about real life: <i>It will probably rain tomorrow.</i></li></ol>""")

    # Page 4
    b.page(f"""{sub("C", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>Robots will to clean our houses.</td><td><b>Robots will clean our houses.</b></td><td>No <i>to</i> after <i>will</i>.</td></tr>
<tr><td>I don't think robots won't teach.</td><td><b>I don't think robots will teach.</b></td><td>Only one negative.</td></tr>
<tr><td>Robots won't probably be expensive.</td><td><b>Robots probably won't be expensive.</b></td><td>Adverb before <i>won't</i>.</td></tr>
<tr><td>Robots will be certainly important.</td><td><b>Robots will certainly be important.</b></td><td>Adverb after <i>will</i>.</td></tr>
<tr><td>Will robots to do operations?</td><td><b>Will robots do operations?</b></td><td>No <i>to</i> in questions.</td></tr>
<tr><td>I hope robots don't will be dangerous.</td><td><b>I hope robots won't be dangerous.</b></td><td>Negative: <i>won't</i>.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "5 min")}
{audiocard(["33.2", "33.3"])}
{sub("A", "Long o or short o? Listen and repeat.", "2 min", "33.2")}
<table style="table-layout:fixed;margin-top:0"><tr><th>long o /oʊ/</th><th>short o /ɑ/</th></tr>
<tr><td>won't · note · hope · own</td><td>want · not · hop · on</td></tr></table>
<p class="small">Which sound is in the first syllable of <b>robot</b>? {R("the long o /oʊ/")}</p>
{sub("B", "Sentences. Listen and repeat.", "2 min", "33.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S333)}</div>
<div class="box" style="margin-top:1mm"><h4>WON'T OR WANT?</h4><b>I won't buy a robot.</b> (= I will not) ≠ <b>I want a robot.</b> Make your mouth round for <i>won't</i>, like the letter O.<br>Tongue twister: <i>I hope you won't own a lot of robots that want to hop on you!</i></div>""",
    24, """<ol><li>4A: say one word from a pair; the student says "long" or "short". Then change roles.</li>
<li>4B: the <i>'ll</i> in <i>I'll</i> and <i>he'll</i> is short; don't say "I will" in every sentence.</li></ol>""")

    # Page 5
    pr = [("think / robots / drive buses in São Paulo", "I think robots will drive buses in São Paulo."),
          ("hope / robots / not / be dangerous", "I hope robots won't be dangerous."),
          ("not think / robots / be cheap", "I don't think robots will be cheap."),
          ("predict / robots / explore Mars", "I predict robots will explore Mars."),
          ("robots / certainly / do housework", "Robots will certainly do housework."),
          ("robots / do operations?", "Will robots do operations?"),
          ("robots / probably / not / teach children", "Robots probably won't teach children."),
          ("when / robots / cook in restaurants?", "When will robots cook in restaurants?")]
    pl = "".join(f'<li value="{i+1}"><i>{p}</i><div class="wline">{R(s)}</div></li>' for i, (p, s) in enumerate(pr))
    corr = [("Robots will to visit other planets.", "Robots will visit other planets."), ("I don't think robots won't care for babies.", "I don't think robots will care for babies."),
            ("I hoping robots won't fight in wars.", "I hope robots won't fight in wars."), ("Robots won't probably be cheap.", "Robots probably won't be cheap.")]
    cl = "".join(f'<li>{w}<div class="wline">{R(c)}</div></li>' for w, c in corr)
    b.page(f"""{sec(5, "Practice", "8 min")}
{sub("A", "Make predictions about robots in ten years. Use will or won't.", "5 min")}
<p class="small">Example: <i>think / robots / help people</i> → I think robots will help people.</p>
{twocol([f'<li value="{i+1}"><i>{p}</i><div class="wline">{R(s)}</div></li>' for i, (p, s) in enumerate(pr)], 5)}
{sub("B", "Correct the mistakes.", "3 min")}
<ol>{cl}</ol>""",
    22, """<p>A: check the word order of the adverbs (5 and 7) and the question forms (6 and 8). Then ask: <i>Do you agree with these predictions?</i> B: the student says why each sentence is wrong.</p>""")

    # Page 6
    topics = ["teach children", "be our friends", "do operations", "drive taxis and buses", "cook in restaurants", "care for older people", "your own idea"]
    tp = ["They probably won't teach children.", "I don't think they'll be real friends.", "They'll certainly help doctors.", "They'll probably drive buses in ten years.", "They'll possibly cook fast food.", "I hope they'll help older people at home.", ""]
    rows = "".join(f"<tr><td style='height:8mm'><b>{t}</b></td><td></td><td class='small'>{R(x)}</td><td></td></tr>" for t, x in zip(topics, tp))
    b.page(f"""{sec(6, "Speaking", "12 min")}
{sub("A", "Robots in ten years. Write your predictions. Then ask your teacher. Do you agree or disagree?", "8 min")}
<table style="table-layout:fixed;font-size:9pt"><tr><th style="width:34mm">Will robots…?</th><th>My prediction</th><th>My teacher's prediction</th><th style="width:20mm">Agree?</th></tr>{rows}</table>
<div class="bank">I think / I don't think / I believe / I predict / I hope · certainly / probably / possibly · next year / in ten years / never · I agree. / I disagree. / I don't think so.</div>
<div class="msg" style="max-width:none;padding:2mm 4mm;line-height:1.55"><b>You:</b> Will robots cook in restaurants?<br><b>Teacher:</b> I think they'll possibly cook fast food in ten years.<br><b>You:</b> I disagree. People love real Brazilian food!</div>
{sub("B", "Your future.", "4 min")}
<ol><li>Do you want a robot at home? What will it do for you?</li><li>Where will you probably be in ten years? What will you do?</li><li>What will be different in Brazil in ten years?</li></ol>""",
    22, """<ol><li>A: your sample predictions are in red; say your real opinion if you prefer. Always ask <i>Why?</i> and disagree sometimes so the student practices <i>I agree / I disagree</i>.</li>
<li>B: listen for <i>won't</i> vs <i>want</i> and the adverb position.</li></ol>""")

    # Page 7
    pc = [("Unit 29", "I can buy clothes: ask about sizes, colors and prices, try things on and pay."), ("Unit 30", "I can talk about food with some, any, a / an and a lot of."),
          ("Unit 31", "I can ask and talk about quantity: how much, how many, a few, a little."), ("Unit 32", "I can talk about my plans and arrangements for the future."),
          ("Unit 33", "I can make predictions with will / won't and say how sure I am.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [(["will", "will to", "wills"], "will", "I think robots", "do most of the housework."), (["won't", "want", "don't"], "won't", "Robots", "be good teachers."),
          (["probably won't", "won't probably", "probably not will"], "probably won't", "Small robots", "be cheap at first."),
          (["Will robots", "Robots will", "Do robots will"], "Will robots", "", "help the police in Brazil?"),
          (["will", "won't", "will to"], "will", "I don't think robots", "fight wars."), (["certainly will", "will certainly", "will be certainly"], "will certainly", "Computers", "be important at school.")]
    hl = "".join(f"<li>{a} {ch(o, r)} {c}</li>" for o, r, a, c in hw)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:15mm"></th><th>In English…</th><th style="width:20mm">Easy!</th><th style="width:20mm">Sometimes</th><th style="width:20mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Choose the correct option.</b></p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. Ten years from now.</b> Write 6 predictions: 3 about your life and 3 about Brazil or the world. Use <i>will / won't</i>, <i>I think / I hope</i> and <i>certainly / probably / possibly</i>.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class: start with homework 2. React to the predictions: <i>Really? Why? I agree / I disagree.</i> Check <i>won't</i> pronunciation when the student reads.</p>""")

    b.extra("Audio scripts", f"""
{sub("33.1", "Paulo's video (slow and natural)")}
<p style="line-height:1.5">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("33.2", "Word pairs")}
<p>{" · ".join(S332)}</p>
{sub("33.3", "Sentences")}
<p>{" ".join(S333)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essentials 33 - Robots")
