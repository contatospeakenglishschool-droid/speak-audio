# Speak! Essentials A1 - Unit 34 "Money smart" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
from speak_engine import *
setup(band="A1 · UNIT 34", audio_json="audio_a1-unit-34.json", img_dir="img")

PHOTOS = [("A", "eat out", "eat out"), ("B", "fill up", "fill up"), ("C", "give up", "give up"), ("D", "heat up", "heat up"),
          ("E", "hold on", "hold on"), ("F", "think about", "think about"), ("G", "throw away", "throw away"), ("H", "worry about", "worry about")]

_r = json.load(open("roteiro.json"))["units"]["a1-unit-34"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["34.1 Messages"].split("\n")]
S342 = [x.split(": ", 1)[1] for x in _r["34.2 Repeat phrasal verbs"].split("\n")]
S343 = [x.split(": ", 1)[1] for x in _r["34.3 Repeat sentences"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LEVEL A1 · UNIT 34", "Money smart", "Saving money · <b>phrasal verbs · should / shouldn't, can / could, imperatives for advice</b>",
                       [("YOU CAN", "give and ask for advice about saving money"),
                        ("LANGUAGE", "You should give up taxis. · You could cook at home. · Don't throw it away!"),
                        ("PRONUNCIATION", "should /ʃʊd/ · could /kʊd/ (silent l) · eat OUT · give UP")])
    b.page(f"""{sec(1, "Warm-up: phrasal verbs", "8 min")}
{sub("A", "Phrasal verbs are a verb + a small word (up, out, on, away, about). Look at the photos and write the phrasal verb.", "3 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(w.replace(" ", "&nbsp;") for _, w, _ in PHOTOS)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Talk about it.", "5 min")}
<ol><li>How often do you eat out? Where do you go?</li><li>Do you heat up your lunch at work, or do you buy food?</li><li>What do you worry about? What do you want to give up?</li></ol>""",
    27, """<ol><li>A: meanings: <b>eat out</b> = eat at a restaurant · <b>fill up</b> = make full · <b>give up</b> = stop doing something · <b>heat up</b> = make hot · <b>hold on</b> = wait · <b>throw away</b> = put in the trash.</li>
<li>B: in phrasal verbs, the small word is usually stressed: eat <b>OUT</b>, give <b>UP</b>.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>8 phrasal verbs with photos</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Mia's problem and Ana's tips for saving money (voice messages)</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>should / shouldn't · can / could · imperatives · money verbs</td><td>3</td></tr>
<tr><td>4 Pronunciation lab</td><td>5 min</td><td>Phrasal verb stress · silent l in should / could</td><td>4</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Word order · match problems and advice</td><td>5</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Advice game with points · you and money</td><td>6</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>7</td></tr></table>
<div class="box"><h4>HOW THIS GUIDE WORKS</h4>Every page looks like the Student Book page with the same number. Your notes are in the <b>yellow box</b>.
<span class="red">Answers in red</span> are not in the Student Book. The <span class="time">5 min</span> chips show the time for each activity. Audio scripts are on the last page.</div>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Mia, the night nurse, wants to travel to Salvador in July, but she never has money at the end of the month: coffee, delivery food and taxis. She sends Ana a voice message, and Ana answers with tips: make coffee at home, heat up your dinner at work, fill up your own bottle, cook with friends instead of eating out, think about it for 30 days, repair your old phone, give up taxis and hold on for the January sales.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>One Portuguese verb, two English verbs: <i>Can you borrow me 50 reais?</i> ✗ → <b>Can you lend me…?</b> / <b>Can I borrow…?</b> Also <i>economize money</i> ✗ → <b>save money</b>, <i>worried with</i> ✗ → <b>worried about</b>, and <i>should to</i> ✗ → <b>should + verb</b>.</div>
<div class="box"><h4>AUDIO</h4>Track 34.1 Voice messages (slow and natural) · Track 34.2 Phrasal verbs · Track 34.3 Sentences</div>""")

    # Page 2
    tips = [("coffee", True), ("water", True), ("the gym", False), ("food and restaurants", True), ("shopping", True), ("old phone", True), ("transportation", True), ("clothes", True)]
    tt = " &nbsp; ".join(f"{'☒' if (T and t) else '☐'} {x}" for x, t in tips)
    gaps = [("You can bring your dinner and heat it", "up", "in the microwave."), ("Fill", "up", "your own bottle at home."),
            ("It's very expensive to eat", "out", "and order delivery food."), ("Before you buy something new, think", "about", "it for thirty days."),
            ("Don't throw", "away", "your old phone. You can repair it!"), ("You should give", "up", "taxis and take the subway."),
            ("You don't need to worry", "about", "traffic."), ("If you need new clothes, hold", "on", "until January.")]
    gl = [f'<li value="{i+1}">{a} {A(g, "min-width:14mm")} {c}</li>' for i, (a, g, c) in enumerate(gaps)]
    b.page(f"""{sec(2, "Listening: Mia's money problem", "10 min")}
<p>Mia, the night nurse, sends Ana a voice message about money. Then Ana answers with some tips.</p>
{audiocard(["34.1 · SLOW", "34.1 · NATURAL"])}
{sub("A", "Listen. What's Mia's problem? Then tick the topics in Ana's tips. One topic is not in her message.", "3 min", "34.1 · SLOW")}
<div class="wline">{R("She wants to travel to Salvador in July, but she never has money at the end of the month.")}</div>
<p style="margin-top:2mm">{tt}</p>
{sub("B", "Listen again and complete with up, out, on, away or about.", "5 min", "34.1 · NATURAL")}
{twocol(gl, 5)}
{sub("C", "Which tip is the best for you? Why?", "2 min")}
<div class="wline"></div>""",
    26, """<ol><li>A: <b>slow</b> version. <b>delivery food</b> = food that comes to your home (apps). The extra topic is <i>the gym</i>.</li>
<li>B: <b>natural</b> version. Ask: <i>Do people in Brazil also wait for the January sales?</i></li></ol>""")

    # Page 3
    b.page(f"""{sec(3, "Language focus: giving advice", "10 min")}
{sub("A", "Read Ana's advice. Then choose the correct option.", "4 min")}
<table style="table-layout:fixed;font-size:9.3pt"><tr><th>should / shouldn't</th><th>can / could</th><th>imperatives</th></tr>
<tr><td>You <b>should</b> give up taxis.<br>You <b>shouldn't</b> buy coffee every night.</td><td>You <b>can</b> repair it!<br>You <b>could</b> invite friends to your place.</td><td><b>Make</b> coffee at home.<br><b>Don't throw</b> away your old phone.</td></tr></table>
<ol><li>We use <i>should</i> and <i>shouldn't</i> to {ch(["give advice", "talk about rules and laws"], "give advice")}.</li>
<li>After <i>should</i>, <i>can</i> and <i>could</i>, we use the verb {ch(["with to", "without to"], "without to")}.</li>
<li><i>can</i> and <i>could</i> are {ch(["more direct", "less direct"], "less direct")} than <i>should</i>: they're ideas.</li>
<li>Imperatives (<i>Make… / Don't…</i>) are {ch(["more direct", "less direct"], "more direct")}, and they {ch(["need", "don't need"], "don't need")} a subject.</li></ol>
{sub("B", "Money verbs. Match the verbs and the meanings.", "4 min")}
<div class="bank">borrow · earn · lend · save · spend</div>
<ol><li>{A("earn", "min-width:16mm")} = get money from your job</li><li>{A("save", "min-width:16mm")} = keep money for later</li>
<li>{A("spend", "min-width:16mm")} = use money to buy things</li><li>{A("lend", "min-width:16mm")} = give money to a person for some time</li>
<li>{A("borrow", "min-width:16mm")} = take money from a person and give it back later</li></ol>
<div class="box sand"><h4>LEND OR BORROW?</h4>Mia: "Can you <b>lend</b> me fifty reais?" (Ana gives) · Mia: "Can I <b>borrow</b> fifty reais?" (Mia takes)<br><i>should</i> is the same for all people: I / you / he / she / we / they <b>should</b>. ✗ <i>she shoulds</i></div>""",
    24, """<ol><li>A: drill the advice as a chain: you say a problem, the student gives advice with <i>should</i>, then <i>could</i>, then an imperative.</li>
<li>B: in Portuguese one verb means both <i>lend</i> and <i>borrow</i>; act it out with a pen.</li></ol>""")

    # Page 4
    b.page(f"""{sub("C", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>Can you borrow me 50 reais?</td><td><b>Can you lend me 50 reais?</b></td><td>lend = give · borrow = take.</td></tr>
<tr><td>I want to economize money.</td><td><b>I want to save money.</b></td><td><i>save</i> money.</td></tr>
<tr><td>You should to cook at home.</td><td><b>You should cook at home.</b></td><td>No <i>to</i> after <i>should</i>.</td></tr>
<tr><td>You don't should eat out.</td><td><b>You shouldn't eat out.</b></td><td>Negative: <i>shouldn't</i>.</td></tr>
<tr><td>I'm worried with money.</td><td><b>I'm worried about money.</b></td><td>worry / worried <b>about</b>.</td></tr>
<tr><td>Throw it in the trash out.</td><td><b>Throw it away.</b></td><td>Phrasal verb: <i>throw away</i>.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "5 min")}
{audiocard(["34.2", "34.3"])}
{sub("A", "Phrasal verbs. Listen and repeat. The small word is stressed.", "2 min", "34.2")}
<table style="table-layout:fixed;margin-top:0"><tr>{"".join(f"<td style='text-align:center;font-size:8.8pt'><b>{w}</b></td>" for w in S342)}</tr></table>
{sub("B", "Sentences. Listen and repeat.", "2 min", "34.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S343)}</div>
<div class="box" style="margin-top:1mm"><h4>SILENT L</h4><b>should</b> /ʃʊd/ and <b>could</b> /kʊd/: we write the <i>l</i>, but we don't say it. Also <i>would</i> /wʊd/. <b>shouldn't</b> /ˈʃʊdənt/.</div>""",
    24, """<ol><li>4A: say <i>eat OUT, fill UP, give UP</i>: the stress helps the listener hear the small word.</li>
<li>4B: Brazilians often say "shoul-d" with an <i>l</i> sound; drill <i>You should save money</i> slowly, then fast.</li></ol>""")

    # Page 5
    ow = [("about / Don't / money / worry / so much", "Don't worry about money so much."), ("should / give / He / sugar / up", "He should give up sugar."),
          ("on / Hold / you buy / a new phone / before", "Hold on before you buy a new phone."), ("could / She / out / eat / on her birthday", "She could eat out on her birthday."),
          ("away / shouldn't / They / those old clothes / throw", "They shouldn't throw away those old clothes."), ("can / heat / up / You / your lunch / at work", "You can heat up your lunch at work.")]
    owl = "".join(f'<li><i>{s}</i><div class="wline">{R(c)}</div></li>' for s, c in ow)
    probs = [("I spend too much money on coffee at work.", "c"), ("I want to spend less on water bottles.", "e"), ("I spend a lot on gas and parking.", "a"),
             ("I always buy clothes I don't need.", "f"), ("I throw away a lot of food.", "b"), ("I pay for a gym, but I never go.", "d")]
    adv = ["You could give up your car and take the bus.", "You shouldn't buy so much at the supermarket. Make a list!", "Make coffee at home and take it to work.",
           "Give up the gym and walk in the park. It's free!", "Fill up your own bottle at home.", "Think about it for 30 days before you buy something."]
    pl = "".join(f'<li>{p} {A(a, "min-width:8mm")}</li>' for p, a in probs)
    al = "".join(f'<p>{"abcdef"[i]}. {x}</p>' for i, x in enumerate(adv))
    b.page(f"""{sec(5, "Practice", "8 min")}
{sub("A", "Put the words in order.", "4 min")}
{twocol([f'<li value="{i+1}"><i>{s}</i><div class="wline">{R(c)}</div></li>' for i, (s, c) in enumerate(ow)], 4)}
<p class="small">Which sentences are imperatives? Change them to <i>should / shouldn't</i>. {R("1 → You shouldn't worry about money so much. · 3 → You should hold on…")}</p>
{sub("B", "Match the problems and the advice.", "4 min")}
<div class="two"><div><ol>{pl}</ol></div><div class="small">{al}</div></div>""",
    22, """<p>A: ask the student to read each sentence aloud with the stress on the small word. B: then the student gives a different piece of advice for each problem.</p>""")

    # Page 6
    sp = ["I spend 50 reais a week on snacks and energy drinks at work.", "My closet is full of clothes that I never wear.", "My friends always want to eat out at expensive restaurants.",
          "I pay for three streaming services, but I only watch one.", "I take taxis everywhere because I'm always late.", "Every month I want to save money, but I spend everything.",
          "I often order delivery food because I'm too tired to cook.", "My phone is broken, and I want a new one today."]
    spl = "".join(f'<li>{x}</li>' for x in sp)
    b.page(f"""{sec(6, "Speaking", "12 min")}
{sub("A", "The advice game. Take turns: one person reads a problem, the other gives advice. You get 1 point for each word from the box in your advice.", "8 min")}
<div class="bank">should · shouldn't · can · could · imperative · don't + verb · eat out · fill up · give up · heat up · hold on · think about · throw away · worry about</div>
<ol>{spl}</ol>
<div class="msg" style="max-width:none;padding:2mm 4mm;line-height:1.55"><b>You:</b> I spend 50 reais a week on snacks at work.<br><b>Teacher:</b> You should give up energy drinks, and you could bring fruit from home. (3 points!)</div>
{sub("B", "You and money.", "4 min")}
<ol><li>Do you save money every month? What for?</li><li>What do you spend most of your money on?</li><li>Do you ever lend money to friends? Do you borrow money?</li><li>What's your best tip for saving money?</li></ol>""",
    22, """<ol><li>A: the student reads 1, 3, 5, 7 and you give advice; then you read 2, 4, 6, 8. Count the points together. Correct <i>should to</i> and the stress in phrasal verbs.</li>
<li>B: money can be a personal topic: let the student answer in general if they prefer.</li></ol>""")

    # Page 7
    pc = [("Unit 30", "I can talk about food with some, any, a / an and a lot of."), ("Unit 31", "I can ask and talk about quantity: how much, how many, a few, a little."),
          ("Unit 32", "I can talk about my plans and arrangements for the future."), ("Unit 33", "I can make predictions with will / won't and say how sure I am."),
          ("Unit 34", "I can give advice with should, could and imperatives, and use 8 phrasal verbs.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = ["worry", "heat", "eat", "fill", "throw", "think", "give", "hold"]
    def g(i): return f"({i+1}) {A(hw[i], 'min-width:15mm')}"
    msg = (f"Thank you for the tips! Here's my plan. I won't {g(0)} about money anymore. I'll {g(1)} up my dinner at work and I won't {g(2)} out every weekend. "
           f"I'll {g(3)} up my bottle at home, and I won't {g(4)} away my old phone. Before I buy something, I'll {g(5)} about it for 30 days. "
           f"I'll {g(6)} up taxis, and I'll {g(7)} on until January for new clothes. Salvador, here I come! Mia")
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:15mm"></th><th>In English…</th><th style="width:20mm">Easy!</th><th style="width:20mm">Sometimes</th><th style="width:20mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Mia's answer.</b> Complete with the verbs in the box.</p>
<div class="bank">eat · fill · give · heat · hold · think · throw · worry</div>
<div class="msg" style="max-width:none;line-height:2">{msg}</div>
<p style="margin-top:3mm"><b>2. My advice.</b> A friend wants to save money for a trip. Write 6 pieces of advice. Use <i>should, shouldn't, could</i>, an imperative and at least three phrasal verbs.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class: start with homework 2. The student reads the advice and you react: <i>Good idea! / That's difficult for me.</i> Next unit: 35 Safari park; then Review 4.</p>""")

    b.extra("Audio scripts", f"""
{sub("34.1", "Voice messages (slow and natural)")}
<p style="line-height:1.5">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("34.2", "Phrasal verbs")}
<p>{" · ".join(S342)}</p>
{sub("34.3", "Sentences")}
<p>{" ".join(S343)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essentials 34 - Money smart")
