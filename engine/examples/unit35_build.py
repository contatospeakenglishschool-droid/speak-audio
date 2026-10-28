# Speak! Essentials A1 - Unit 35 "Safari park" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
from speak_engine import *
setup(band="A1 · UNIT 35", audio_json="audio_a1-unit-35.json", img_dir="img")

PHOTOS = [("A", "buy souvenirs", "souvenirs"), ("B", "drive slowly", "drive"), ("C", "feed the animals", "feed"), ("D", "leave the car", "car"),
          ("E", "leave the road", "road"), ("F", "open the windows", "windows"), ("G", "take pictures", "pictures"), ("H", "touch the animals", "touch")]
YES = {"buy souvenirs", "drive slowly", "take pictures"}

_r = json.load(open("roteiro.json"))["units"]["a1-unit-35"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["35.1 Safari"].split("\n")]
S352 = [x.split(": ", 1)[1] for x in _r["35.2 Repeat words"].split("\n")]
S353 = [x.split(": ", 1)[1] for x in _r["35.3 Repeat sentences"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LEVEL A1 · UNIT 35", "Safari park", "Rules · <b>must / mustn't · can / can't · imperatives</b>",
                       [("YOU CAN", "understand and explain rules in a park, a building or at work"),
                        ("LANGUAGE", "You must stay in your car. · You mustn't use a flash. · Don't feed the animals."),
                        ("PRONUNCIATION", "mustn't /ˈmʌsənt/ (silent t) · can /kən/ ≠ can't /kænt/")])
    yn = " &nbsp;·&nbsp; ".join(f"{l} {A('yes' if w in YES else 'no', 'min-width:10mm')}" for l, w, _ in PHOTOS)
    b.page(f"""{sec(1, "Warm-up: at a safari park", "8 min")}
{sub("A", "A safari park is a kind of zoo: you drive through it in your car. Write the phrase under each photo.", "3 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(w.replace(" ", "&nbsp;") for _, w, _ in PHOTOS)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Does the safari park want visitors to do these things? Write yes or no. Why are these rules important?", "5 min")}
<p style="line-height:2">{yn}</p>""",
    26, """<ol><li>A: <b>souvenirs</b> /ˌsuːvəˈnɪrz/ = things you buy to remember a place. <b>leave the road</b> = drive off the road.</li>
<li>B: the rules keep the visitors and the animals safe. Ask: <i>Did you ever visit a zoo or a safari park? Where?</i></li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>8 actions at a safari park · yes or no?</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Visitor information at Green Valley Safari Park · Paulo and the monkey</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>must / mustn't (rules) · can / can't (permission) · imperatives</td><td>3</td></tr>
<tr><td>4 Pronunciation lab</td><td>5 min</td><td>Silent t in mustn't · can ≠ can't</td><td>4</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Say the rules in another way · rules at a farm hotel</td><td>5</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Guess the place from the rules · rules in your life</td><td>6</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>7</td></tr></table>
<div class="box"><h4>HOW THIS GUIDE WORKS</h4>Every page looks like the Student Book page with the same number. Your notes are in the <b>yellow box</b>.
<span class="red">Answers in red</span> are not in the Student Book. The <span class="time">5 min</span> chips show the time for each activity. Audio scripts are on the last page.</div>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Paulo, Ana and Marcos visit Green Valley Safari Park (an invented park near São Paulo). A guide gives the rules: stay in your car, don't open the windows, don't leave the road, don't feed the animals, no flash, no smoking. Paulo the photographer wasn't listening: he looks for his flash and opens the window… and a monkey takes his sunglasses!</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Translating Portuguese rule phrases word for word: <i>It's forbidden smoke</i> ✗ → <b>You can't smoke / No smoking</b>; <i>Is permitted take photos?</i> ✗ → <b>Can I take photos?</b> Also <i>must to</i> ✗, <i>don't must</i> ✗ → <b>mustn't</b>, and saying the <i>t</i> in <i>mustn't</i>. Note: American English often prefers <i>can't</i> or <i>Don't…</i> to <i>mustn't</i>, but all three are correct.</div>
<div class="box"><h4>AUDIO</h4>Track 35.1 Visitor information (slow and natural) · Track 35.2 must, can, don't · Track 35.3 Rules</div>""")

    # Page 2
    rules = [("Stay in your car.", True), ("Wear your seat belt.", False), ("Don't open the windows or doors.", True), ("Don't leave the road.", True),
             ("Don't feed the animals.", True), ("Don't play loud music.", False), ("Don't use a flash.", True), ("Don't smoke.", True)]
    rl = "".join(f"<td style='width:25%;font-size:9pt'>{'☒' if (T and t) else '☐'} {x}</td>" + ("</tr><tr>" if i == 3 else "") for i, (x, t) in enumerate(rules))
    det = [(["should", "must", "can"], "must", "First, you", "stay in your car."), (["shouldn't", "must", "must not"], "must not", "So you", "open your windows or doors."),
           (["can't", "don't", "won't"], "can't", "You", "leave the road for any reason."), (["Can't", "Don't", "Mustn't"], "Don't", "", "touch or feed the animals."),
           (["can", "will", "should"], "can", "You", "take photographs, of course…"), (["shouldn't", "mustn't", "won't"], "mustn't", "…but you", "use a flash."),
           (["should", "will", "can"], "can", "At the end of your visit, you", "buy souvenirs in our shop.")]
    dl = [f'<li value="{i+1}">{a} {ch(o, r)} {c}</li>' for i, (o, r, a, c) in enumerate(det)]
    b.page(f"""{sec(2, "Listening: welcome to the safari park", "10 min")}
<p>Paulo, Ana and Marcos are visiting Green Valley Safari Park near São Paulo. Before they drive in, they listen to the visitor information.</p>
{audiocard(["35.1 · SLOW", "35.1 · NATURAL"])}
{sub("A", "Listen. Which six rules does the guide talk about? Tick them.", "3 min", "35.1 · SLOW")}
<table style="table-layout:fixed;margin-top:0"><tr>{rl}</tr></table>
{sub("B", "Choose the correct words. Then listen again and check.", "5 min", "35.1 · NATURAL")}
{twocol(dl, 5)}
{sub("C", "What happens to Paulo at the end? Why?", "2 min")}
<div class="wline">{R("A monkey takes his sunglasses, because he opened the window.")}</div>""",
    26, """<ol><li>A: <b>slow</b> version. Extra rules: <i>Wear your seat belt</i> and <i>Don't play loud music</i>. <b>a flash</b> = the light on a camera.</li>
<li>B: <b>natural</b> version. Ask: <i>Which rule did Paulo break? Two rules!</i> (the flash and the window).</li></ol>""")

    # Page 3
    b.page(f"""{sec(3, "Language focus: rules", "10 min")}
{sub("A", "Read the rules from the safari park. Then choose the correct option.", "5 min")}
<table style="table-layout:fixed;font-size:9.3pt"><tr><th>must / mustn't</th><th>can / can't</th><th>imperatives</th></tr>
<tr><td>You <b>must</b> stay in your car.<br>You <b>mustn't</b> use a flash.</td><td>You <b>can</b> take photographs.<br>You <b>can't</b> leave the road.</td><td><b>Drive</b> slowly.<br><b>Don't</b> feed the animals.</td></tr></table>
<ol><li><i>must</i> and <i>mustn't</i> explain {ch(["advice", "rules and laws"], "rules and laws")}. After them, we use the verb {ch(["with to", "without to"], "without to")}.</li>
<li><i>must</i> = it's {ch(["necessary", "your choice"], "necessary")}. <i>can</i> = it's {ch(["necessary", "OK, your choice"], "OK, your choice")}.</li>
<li><i>can't</i> has the same meaning as {ch(["mustn't", "must"], "mustn't")}.</li>
<li>Imperatives {ch(["need", "don't need"], "don't need")} a subject. The negative is <b>Don't</b> + verb.</li></ol>
{sub("B", "Necessary, OK or not OK? Write N, OK or X.", "3 min")}
<ol><li>You must buy a ticket. {A("N", "min-width:9mm")}</li><li>You can park here. {A("OK", "min-width:9mm")}</li><li>Don't smoke. {A("X", "min-width:9mm")}</li><li>You mustn't run. {A("X", "min-width:9mm")}</li><li>You can't swim here. {A("X", "min-width:9mm")}</li></ol>
<div class="box sand"><h4>REMEMBER</h4><b>must</b> is the same for all people: I / you / he / she / we / they <b>must</b>. ✗ <i>he musts</i><br>
Rules on signs: <b>No smoking.</b> = You can't smoke. · <b>No photos.</b> = You mustn't take photos.</div>""",
    26, """<ol><li>A: <i>mustn't</i> and <i>must</i> are very different: mustn't = not OK; must = necessary. Compare with <i>should</i> (Unit 34): advice, not a rule.</li>
<li>B: then ask about rules at the student's work or building.</li></ol>""")

    # Page 4
    b.page(f"""{sub("C", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>It's forbidden smoke here.</td><td><b>You can't smoke here. / No smoking.</b></td><td>Use <i>can't</i> or a sign.</td></tr>
<tr><td>Is permitted take photos?</td><td><b>Can I take photos?</b></td><td>Ask with <i>Can I…?</i></td></tr>
<tr><td>You must to stay in the car.</td><td><b>You must stay in the car.</b></td><td>No <i>to</i> after <i>must</i>.</td></tr>
<tr><td>You don't must open the window.</td><td><b>You mustn't open the window.</b></td><td>Negative: <i>mustn't</i>.</td></tr>
<tr><td>Don't to touch the animals.</td><td><b>Don't touch the animals.</b></td><td>No <i>to</i> after <i>don't</i>.</td></tr>
<tr><td>He musts wear a helmet.</td><td><b>He must wear a helmet.</b></td><td><i>must</i>: same for all people.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "5 min")}
{audiocard(["35.2", "35.3"])}
{sub("A", "Listen and repeat.", "2 min", "35.2")}
<table style="table-layout:fixed;margin-top:0"><tr>{"".join(f"<td style='text-align:center'><b>{w}</b></td>" for w in S352)}</tr></table>
<div class="box" style="margin-top:1mm"><h4>CAN OR CAN'T?</h4><b>mustn't</b> /ˈmʌsənt/: the first <i>t</i> is silent. · <b>can</b> is short and weak /kən/: You <i>can</i> take photos. · <b>can't</b> is long and strong /kænt/: You <b>CAN'T</b> leave the road. Say the final <i>t</i>!</div>
{sub("B", "Rules. Listen and repeat.", "2 min", "35.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S353)}</div>""",
    24, """<ol><li>4A: say a sentence with <i>can</i> or <i>can't</i>; the student holds up a thumb up (can) or down (can't).</li>
<li>4B: Brazilians often say "mus-ti-nt": practice /ˈmʌsənt/ slowly.</li></ol>""")

    # Page 5
    rp = [("Don't touch the animals.", "You mustn't / can't touch the animals."), ("Drive slowly.", "You must drive slowly."),
          ("It's OK to take photographs.", "You can take photographs."), ("No smoking.", "You can't / mustn't smoke. / Don't smoke."),
          ("You mustn't open the windows.", "Don't open the windows. / You can't open the windows."), ("You must stay in your car.", "Stay in your car. / Don't leave your car.")]
    rpl = [f'<li value="{i+1}">{s}<div class="wline">{R(c)}</div></li>' for i, (s, c) in enumerate(rp)]
    signs = [("Animal food: 5 reais at the door.", "You can buy food for the animals."), ("Our animals don't eat human food.", "You mustn't give your lunch to the animals."),
             ("Our goats are friendly!", "You can touch the goats."), ("Our horses are for adults only.", "Children can't ride the horses."),
             ("Wash your hands after you touch the animals.", "You must wash your hands."), ("Stay on the path.", "You mustn't leave the path.")]
    sl = "".join(f'<li>{s}<div class="wline">{R(c)}</div></li>' for s, c in signs)
    b.page(f"""{sec(5, "Practice", "8 min")}
{sub("A", "Say the same rule in a different way.", "4 min")}
{twocol(rpl, 4)}
{sub("B", "Ana and Marcos take Leo to a farm hotel. Read the signs and write the rules. Use must, mustn't, can or can't.", "4 min")}
{twocol([f'<li value="{i+1}">{s}<div class="wline">{R(c)}</div></li>' for i, (s, c) in enumerate(signs)], 4)}""",
    22, """<p>A: accept all correct forms. B: a <b>farm hotel</b> is a hotel on a farm in the countryside, very popular with Brazilian families; children can see and touch farm animals. Ask: <i>Did you ever stay at a farm hotel?</i></p>""")

    # Page 6
    places = ["a library", "a swimming pool", "a plane", "a hospital", "a museum", "a gym", "a movie theater", "an exam room"]
    tr = [("a plane", "You must wear your seat belt. You can't use the bathroom when the plane takes off. You can watch movies."),
          ("a library", "You mustn't talk on the phone. You can borrow books. Don't eat here.")]
    b.page(f"""{sec(6, "Speaking", "12 min")}
{sub("A", "Guess the place! Your teacher reads three rules. Guess the place. Then choose a place and say three rules. Your teacher guesses.", "7 min")}
<div class="bank">{" · ".join(places)}</div>
<div class="msg" style="max-width:none;padding:2mm 4mm;line-height:1.55"><b>You:</b> You must be quiet. You can look at old things. You mustn't touch the paintings.<br><b>Teacher:</b> Is it a museum?<br><b>You:</b> Yes, it is!</div>
<p class="small" style="margin-top:2mm">My rules for <b>____________</b>:</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>
{sub("B", "Rules in your life.", "5 min")}
<ol><li>What are the rules in your building or condo? (pets, noise, the pool, parking…)</li><li>What are the rules at your work or school? Which rules do you like? Which don't you like?</li>
<li>What rules did you have at home when you were a child?</li></ol>""",
    26, f"""<ol><li>A: start with your examples: {R(tr[0][1] + " (" + tr[0][0] + ") · " + tr[1][1] + " (" + tr[1][0] + ")")}. Then the student writes three rules for a secret place.</li>
<li>B: question 3 reviews the past simple. Brazilian condos have a lot of rules: a good topic!</li></ol>""")

    # Page 7
    pc = [("Unit 31", "I can ask and talk about quantity: how much, how many, a few, a little."), ("Unit 32", "I can talk about my plans and arrangements for the future."),
          ("Unit 33", "I can make predictions with will / won't and say how sure I am."), ("Unit 34", "I can give advice with should, could and imperatives, and use 8 phrasal verbs."),
          ("Unit 35", "I can understand and explain rules with must, mustn't, can and can't.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    lf = [("The animals mustn't eat special food.", "The animals must eat special food."), ("You can buy animal food at the entrance.", "correct ✓"),
          ("The animals must eat chocolate and candy.", "The animals mustn't / can't eat chocolate and candy."), ("You can stay on the path.", "You must stay on the path."),
          ("After your visit, you must buy souvenirs.", "After your visit, you can buy souvenirs."), ("You can't smoke anywhere in the park.", "correct ✓")]
    lfl = "".join(f'<li>{w}<div class="wline">{R(c)}</div></li>' for w, c in lf)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:15mm"></th><th>In English…</th><th style="width:20mm">Easy!</th><th style="width:20mm">Sometimes</th><th style="width:20mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. The petting zoo.</b> Are these rules logical? Correct the wrong ones. Two are correct.</p>
<ol style="line-height:1.3">{lfl}</ol>
<p style="margin-top:2mm"><b>2. House rules.</b> Write 6 rules for your home, your office or your building. Use <i>must, mustn't, can, can't</i> and imperatives.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    16, """<p>Next class: <b>Review 4</b> (Units 28–35). Start with homework 2 and ask: <i>Which rule is the most important? Why?</i></p>""")

    b.extra("Audio scripts", f"""
{sub("35.1", "Visitor information (slow and natural)")}
<p style="line-height:1.5">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("35.2", "must, can, don't")}
<p>{" · ".join(S352)}</p>
{sub("35.3", "Rules")}
<p>{" ".join(S353)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essentials 35 - Safari park")
