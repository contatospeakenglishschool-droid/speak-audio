# Speak! Bridge A2 - Unit 33 "Self-driving cars" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 33", audio_json="audio_a2-unit-33.json", img_dir="img")

PHOTOS = [("A", "car keys", "car keys"), ("B", "accident", "accident"), ("C", "mirror", "mirror"), ("D", "steering wheel", "steering wheel"),
          ("E", "speed limit", "speed limit"), ("F", "lanes", "lanes"), ("G", "dashboard", "dashboard"), ("H", "seats", "seats")]
_r = json.load(open("roteiro.json"))["units"]["a2-unit-33"]
S331 = [x.split(": ", 1)[1] for x in _r["33.1 Who's behind the wheel?"].split("\n")]
S332 = [x.split(": ", 1)[1] for x in _r["33.2 Repeat: predictions"].split("\n")]
S333 = [x.split(". ", 1)[1] for x in [y.split(": ", 1)[1] for y in _r["33.3 Want or won't?"].split("\n")]]
BOLD = ["predictions", "controls", "prevent", "effects", "efficiently", "replace", "result in", "technology"]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 33", "Self-driving cars", "The future of driving · <b>predictions: will, might, likely</b>",
                       [("YOU CAN", "make predictions about the future and say how sure you are"),
                        ("LANGUAGE", "It'll probably be cheaper. · They might prevent accidents. · It's unlikely to happen soon."),
                        ("PRONUNCIATION", "won't /woʊnt/ or want /wɑːnt/ · it'll")])
    b.page(f"""{sec(1, "Warm-up: in the car", "8 min")}
{sub("A", "Write the words under the photos.", "4 min")}
<div class="bank">accident · car keys · dashboard · lanes · mirror · seats · speed limit · steering wheel</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Talk about it.", "4 min")}
<ol style="line-height:1.5"><li>Do you drive? Do you have a driver's license? Do you enjoy driving?</li><li>How has driving changed in the last ten years? Think of apps, electric cars and cameras.</li><li>What changes do you expect in the next ten years?</li></ol>""",
    22, """<ol><li>A: in the US, speed limits are in miles per hour (25 mph is about 40 km/h). <i>Lanes</i>: the parts of a road for one line of cars. Also teach <i>driver's license</i> (British: <i>driving licence</i>).</li>
<li>B: students may mention self-driving cars; that's the topic of the reading.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Car and driving words</td><td>1</td></tr>
<tr><td>2 Reading</td><td>10 min</td><td>Who's behind the wheel? An article about self-driving cars</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Predictions: will, may / might / could, likely to</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Making predictions: how sure are you?</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>4 min</td><td>Predictions · want or won't?</td><td>5</td></tr>
<tr><td>5 Practice</td><td>9 min</td><td>Same meaning, different words · Word builder: driving expressions</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Predictions about self-driving cars and drones</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>An American newspaper article about self-driving cars, read by the Reporter (Studio-O). Carol, Paulo's cousin in Orlando, is quoted: she has tried a robotaxi. Facts: SAE International's standard J3016 describes six levels of driving automation, Level 0 to Level 5, and the US Department of Transportation uses it; there are no Level 5 cars on public roads (SAE International; NHTSA, "Automated Vehicles for Safety"). Waymo runs paid driverless taxis in more than ten US metro areas, including Phoenix, Los Angeles, Atlanta and Orlando (AP, February 2026; Waymo announcements, 2026). NHTSA estimates that 39,345 people died in traffic crashes in the US in 2024 (NHTSA press release, April 2025). The original lesson used British sources; we wrote a new American article.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students add <i>to</i> after modals (<i>might to be</i> ✗), say <i>It likely to</i> without <i>be</i>, put <i>probably</i> in the wrong place (<i>It will be probably</i>), confuse <i>won't</i> and <i>want</i>, and use <i>will</i> for every prediction.</div>
<div class="box"><h4>AUDIO</h4>Track 33.1 Who's behind the wheel? (article, slow and natural) · Track 33.2 Repeat: predictions · Track 33.3 Want or won't?</div>""")

    # Page 2
    paras = S331[1:]
    def bold(p):
        for w in BOLD:
            p = p.replace(" " + w + " ", f" <b>{w}</b> ").replace(" " + w + ".", f" <b>{w}</b>.").replace(" " + w + ",", f" <b>{w}</b>,")
        return p
    art = "".join(f"<p style='margin:0 0 .9mm'>{bold(p)}</p>" for p in paras)
    qs = [("How does the computer help at the lowest levels?", "with parking or staying in a lane"), ("What can the driver do at Level 5?", "work or sleep"),
          ("Where can people already ride in driverless taxis?", "in more than ten US cities (Phoenix, Los Angeles, Atlanta, Orlando…)"),
          ("How many people died in crashes on US roads in 2024?", "about 39,000"), ("Which two groups will probably find self-driving cars very useful?", "older people and some people with disabilities")]
    ql = "".join(f"<li>{q} {A(a, 'min-width:40mm')}</li>" for q, a in qs)
    b.page(f"""{sec(2, "Reading: who's behind the wheel?", "10 min")}
<div style="display:flex;gap:2mm;align-items:center"><div style="flex:1">{audiocard(["33.1 · SLOW", "33.1 · NATURAL"])}</div>{img('I', 34, 18)}</div>
<div class="box" style="margin-top:1mm;font-size:8.5pt;line-height:1.36"><h4 style="font-size:11pt;margin:0 0 .5mm">{S331[0]}</h4><div style="column-count:2;column-gap:5mm">{art}</div></div>
{sub("A", "Read and listen to the article. Answer the questions.", "6 min", "33.1 · SLOW")}
<ol style="line-height:1.45;font-size:9pt">{ql}</ol>
{sub("B", "What was the most surprising information in the article? Would you ride in a robotaxi?", "2 min")}""",
    25, """<ol><li>A: let the student read first, then play the natural version. A <i>robotaxi</i> is a taxi with no driver; people book it with an app.</li>
<li>B: Carol is Paulo's cousin in Orlando (story character). Ask: <i>Do you think robotaxis will come to Brazil? When?</i></li></ol>""")

    # Page 3
    voc = [("guesses about what will happen in the future", "predictions"), ("makes a machine work in a certain way", "controls"), ("stop something from happening", "prevent"),
           ("things that happen because of something else", "effects"), ("quickly and without waste", "efficiently"), ("take the place of something", "replace"),
           ("cause something to happen", "result in"), ("new machines and computers developed by science", "technology")]
    vl = [f'<li value="{i+1}">{d} {A(w, "min-width:20mm")}</li>' for i, (d, w) in enumerate(voc)]
    b.page(f"""{sec(3, "Language focus: making predictions", "10 min")}
{sub("A", "Word builder. Find the words in bold in the article for these meanings.", "3 min")}
<div style="font-size:8.8pt">{twocol(vl, 5)}</div>
{sub("B", "Read the sentences from the article. Then choose the correct option.", "7 min")}
<div class="box" style="margin-top:1mm;font-size:8.8pt;line-height:1.45">1 Level 5 cars <b>won't be</b> available for many years. · 2 They <b>might prevent</b> thousands of accidents. · 3 Drivers <b>could become</b> too confident.<br>
4 They <b>will probably be</b> better for the environment. · 5 It <b>will certainly be</b> cheaper. · 6 If robotaxis become popular, this <b>might result</b> in big changes.<br>
7 The biggest winners <b>are likely to be</b> older people.</div>
<ol style="line-height:1.62;font-size:9pt"><li>After <i>will, won't, might, could</i> we use {ch(["the base form", "to + verb", "verb-ing"], "the base form")}.</li>
<li>With <i>will / won't</i> we feel {ch(["sure", "not very sure"], "sure")}. With <i>may, might, could</i> we feel {ch(["sure", "less sure"], "less sure")}.</li>
<li><i>Probably</i> and <i>certainly</i> are {ch(["adjectives", "adverbs"], "adverbs")}. They go {ch(["between will and the verb", "at the end"], "between will and the verb")}.</li>
<li>Sentence 6 is about a {ch(["real", "unreal"], "real")} possible situation, but the result is not certain.</li>
<li>After <i>be likely</i> we use {ch(["the base form", "to + base form"], "to + base form")}. It means we are {ch(["certain", "guessing, but quite sure"], "guessing, but quite sure")}. The opposite is {A("unlikely", "min-width:16mm")}.</li></ol>
<div class="box sand"><h4>RULE</h4><b>will / won't</b> = sure · <b>will probably / probably won't</b> = quite sure · <b>may / might / could</b> = maybe · <b>be likely / unlikely to</b> = probably / probably not. More on the next page: <b>Grammar reference</b>.</div>""",
    28, """<ol><li>A: <i>efficiently</i> is the only adverb; the others are nouns or verbs. Drill <i>predictions</i>, <i>technology</i> (stress: preDICtions, techNOLogy).</li>
<li>B: drill all seven sentences, contracting <i>will</i>: <i>They'll probably be…</i></li></ol>""")

    grammar_ref.predictions(b)

    # Page 5
    ww = ["won't", "want", "want", "won't", "won't", "want"]
    wwl = "".join(f"<li>{A(w, 'min-width:16mm')}</li>" for w in ww)
    b.page(f"""{sub("C", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>It might to be expensive.</td><td><b>It might be expensive.</b></td><td>modal + base form.</td></tr>
<tr><td>It will be probably cheaper.</td><td><b>It will probably be cheaper.</b></td><td>adverb after will.</td></tr>
<tr><td>Robotaxis likely to be popular.</td><td><b>Robotaxis are likely to be popular.</b></td><td>be likely to.</td></tr>
<tr><td>It will not probably happen.</td><td><b>It probably won't happen.</b></td><td>probably before won't.</td></tr>
<tr><td>I think it couldn't happen. (= maybe not)</td><td><b>I think it might not happen.</b></td><td>might not / may not.</td></tr>
<tr><td>I want drive. (= I won't)</td><td><b>I won't drive.</b> /woʊnt/</td><td>won't ≠ want.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "4 min")}
{audiocard(["33.2", "33.3"])}
{sub("A", "Listen and repeat. Use the short forms.", "2 min", "33.2")}
{twocol([f'<li value="{i+1}">{s}</li>' for i, s in enumerate(S332)], 4)}
{sub("B", "Listen to six sentences. Do you hear want or won't? Write the word.", "2 min", "33.3")}
<ol style="line-height:1.5;column-count:3;column-gap:5mm">{wwl}</ol>""",
    31, """<ol><li>A: <i>it'll</i> /ˈɪtəl/; <i>they're likely</i>; <i>unlikely</i> stresses <i>LIKE</i>.</li>
<li>B: <i>won't</i> has the long /oʊ/ of <i>go</i>; <i>want</i> has the /ɑ/ of <i>hot</i>. Also, <i>want</i> is usually followed by <i>to</i> or a noun. Script: 1 I won't drive to work. 2 I want a new car. 3 They want to try a robotaxi. 4 She won't sell her car. 5 We won't need a license. 6 I want to learn to drive.</li></ol>""")

    # Page 6
    tr = [("I'm sure taxi drivers will lose their jobs if robotaxis become very popular. (definitely)", "Taxi drivers will definitely lose their jobs if robotaxis become very popular."),
          ("If robotaxis become popular, people will probably sell their cars. (likely)", "If robotaxis become popular, people are likely to sell their cars."),
          ("Perhaps people will use robotaxis instead of buses. (may)", "People may use robotaxis instead of buses."),
          ("It's possible that we will see Level 5 cars in the next 20 years. (could)", "We could see Level 5 cars in the next 20 years."),
          ("Self-driving cars are very unlikely to cause many accidents. (won't)", "Self-driving cars (probably) won't cause many accidents."),
          ("Some people aren't sure if they will feel safe in a robotaxi. (might)", "Some people might not feel safe in a robotaxi."),
          ("Not many people think robotaxis will completely replace normal cars. (unlikely)", "Robotaxis are unlikely to completely replace normal cars."),
          ("We think robotaxis might be popular with older people. (probably)", "Robotaxis will probably be popular with older people.")]
    trl = "".join(f"<li>{o}<br>{A(n, 'min-width:110mm')}</li>" for o, n in tr)
    ex = [("a back-seat driver", "a passenger who gives the driver advice they don't want", "c"), ("It's driving me crazy!", "It's making me very annoyed.", "a"),
          ("You drive a hard bargain.", "You don't accept a lower price easily.", "e"), ("in the driver's seat", "in control of a situation", "b"),
          ("a drive-in", "an outdoor movie theater where you watch from your car", "d")]
    left = "".join(f"<li>{a} {A(l, 'min-width:7mm;text-align:center')}</li>" for a, _, l in ex)
    right = "".join(f"<li>{d}</li>" for l, d in sorted([(l, d) for _, d, l in ex]))
    b.page(f"""{sec(5, "Practice", "9 min")}
{sub("A", "Rewrite the sentences with the word in brackets. Keep the same meaning.", "6 min")}
<ol style="line-height:1.32;font-size:8.8pt">{trl}</ol>
{sub("B", "Word builder: driving expressions. Match 1–5 with a–e.", "3 min")}
<div style="display:flex;gap:4mm;font-size:8.8pt"><ol style="flex:1;line-height:1.5;margin:0">{left}</ol><ol type="a" style="flex:1;line-height:1.5;margin:0">{right}</ol></div>
<p class="small" style="margin:.8mm 0 0">Do you know a back-seat driver? Is there a drive-in movie theater near you?</p>""",
    27, """<ol><li>A: accept other correct answers (e.g. 3 <i>might / could</i>; 5 <i>will almost certainly not</i>). This type of exercise is common in exams.</li>
<li>B: drive-in theaters were very popular in the US in the 1950s; a few still exist.</li></ol>""")

    # Page 7
    you = ["children going to school alone in robotaxis", "hackers taking control of cars", "drones delivering food orders", "drones finding rare animals in the wild"]
    tea = [("driving tests and driver's licenses", "Driving tests will probably change a lot. Maybe in 20 years young people won't need a license."),
           ("car chases in action movies", "Car chases are unlikely to disappear. Movies might show chases between robot cars!"),
           ("drones watching traffic", "The police will certainly use drones to watch traffic, because it's cheaper than a helicopter."),
           ("drones planting trees", "Drones could plant trees in places that are difficult to reach.")]
    yl = "".join(f"<li>{x}</li>" for x in you)
    tl = "".join(f"<li>{x}<br><span class='small'>{R(y) if T else ''}</span></li>" for x, y in tea)
    b.page(f"""{sec(6, "Speaking: the future of cars and drones", "12 min")}
<div style="display:flex;gap:3mm;align-items:center"><p style="flex:1;margin:0">A <b>drone</b> is a small flying machine that someone controls from the ground. You and your teacher are going to discuss the future of self-driving cars and drones.</p>{img('J', 32, 22)}</div>
<div class="bank">will · won't · might · may · could · likely · unlikely · definitely · certainly · probably · possibly</div>
<div class="two"><div>{sub("A", "Your topics. Prepare a prediction about each one.", "3 min")}<ol style="line-height:1.55;font-size:9pt;margin:0">{yl}</ol></div>
<div>{sub("B", "Your teacher's topics. Listen and agree or disagree.", "")}<ol style="line-height:1.4;font-size:9pt;margin:0">{tl}</ol></div></div>
{sub("C", "Take turns. Give a prediction, a reason and an example. Then react.", "6 min")}
<p class="small" style="margin:0"><i>A: I think drones will definitely deliver food orders in big cities, because they're faster than motorcycles. — B: Maybe, but they're unlikely to deliver heavy things.</i></p>
{sub("D", "Which predictions do you both feel sure about? Which do you disagree about?", "3 min")}""",
    27, """<ol><li>B: the teacher's predictions in red are models; read them one at a time and ask: <i>Do you agree? How sure are you, 0% or 100%?</i></li>
<li>C: insist on a range of forms, not only <i>will</i>; tick each word in the box when the student uses it.</li></ol>""")

    # Page 8
    pc = [("A2 Unit 29", "I can check in, go through security and understand announcements on a plane."), ("A2 Unit 31", "I can describe a photo for about a minute."),
          ("A2 Unit 32", "I can talk about timetables and personal plans for the future."), ("A2 Unit 33", "I can make predictions and say how sure I am.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    ro = [("certainly / drones / The police / to / traffic. / use / watch / will", "The police will certainly use drones to watch traffic."),
          ("to deliver / drones / things / to people. / use / very large / We / won't", "We won't use drones to deliver very large things to people."),
          ("drones. / find / If we / in the wild, we / might / need to / rare animals / use", "If we need to find rare animals in the wild, we might use drones."),
          ("to deliver / drones / Doctors / may / medicine / to / use / sick people.", "Doctors may use drones to deliver medicine to sick people."),
          ("are / be useful / Drones / likely / make maps. / to / when we", "Drones are likely to be useful when we make maps."),
          ("are / be / completely / Drones / from hackers. / safe / to / unlikely", "Drones are unlikely to be completely safe from hackers."),
          ("deliver / Drones / order / online. / probably / that we / things / will", "Drones will probably deliver things that we order online."),
          ("be / break down. / could / dangerous / Drones / if they / to people", "Drones could be dangerous to people if they break down.")]
    rol = "".join(f'<li><span class="small">{w}</span><br>{A(s, "min-width:110mm")}</li>' for w, s in ro)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Put the words in order to make predictions about drones.</b></p>
<ol style="line-height:1.35;font-size:9pt">{rol}</ol>
<p style="margin-top:1.5mm"><b>2. My city in 2040 (50–75 words).</b> How will people move around your city in 2040? Use at least four different ways to make predictions.</p>""",
    18, """<p>Next class: the student reads the text aloud; ask <i>How sure are you?</i> after each prediction. Follow-up idea: discuss whether robotaxis could work in Brazilian cities.</p>""")

    b.extra("Audio script", f"""
{sub("33.1", "Who's behind the wheel? (slow and natural)")}
<p style="line-height:1.38;font-size:8.8pt">{"<br>".join(S331)}</p>
{sub("33.2", "Repeat: predictions")}
<p>{" · ".join(S332)}</p>
{sub("33.3", "Want or won't? (3-second pause)")}
<p>{" · ".join(S333)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 33 - Self-driving cars")
