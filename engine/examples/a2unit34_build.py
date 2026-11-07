# Speak! Bridge A2 - Unit 34 "Gap year" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 34", audio_json="audio_a2-unit-34.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["a2-unit-34"]
S341 = [x.split(": ", 1) for x in _r["34.1 Gap year plans"].split("\n")]
S342 = [x.split(": ", 1)[1] for x in _r["34.2 Repeat: going to and will"].split("\n")]
S343 = [x.split(". ", 1)[1] for x in [y.split(": ", 1)[1] for y in _r["34.3 Which future?"].split("\n")]]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 34", "Gap year", "A year off · <b>future forms: going to, will, present continuous</b>",
                       [("YOU CAN", "talk about plans, arrangements and predictions, and choose the right future form"),
                        ("LANGUAGE", "I'm going to take a year off. · I'm starting next week. · I think you'll love it. · It's going to rain."),
                        ("PRONUNCIATION", "going to /ˈɡʌnə/ in fast speech · he'll")])
    gm = [("volunteer at an animal shelter", "to help animals", "e"), ("volunteer at a school", "to teach children new skills", "h"),
          ("travel alone", "to become more independent", "c"), ("travel with a friend", "to share the adventure", "g"),
          ("learn a language", "so I can travel more easily", "a"), ("learn how to fix my car", "so I can save a lot of money", "b"),
          ("do an unpaid internship", "to get experience", "d"), ("get a job", "to make money", "f")]
    left = "".join(f"<li>{a} {A(l, 'min-width:7mm;text-align:center')}</li>" for a, _, l in gm)
    right = "".join(f"<li>{d}</li>" for l, d in sorted([(l, d) for _, d, l in gm]))
    b.page(f"""{sec(1, "Warm-up: a year off", "8 min")}
<div style="display:flex;gap:3mm;align-items:center"><p style="flex:1;margin:0">Some young people take a <b>gap year</b>: a year off before they go to college, or during their studies.</p>{img('A', 40, 24)}</div>
{sub("A", "Match the gap year activities 1–8 with the reasons a–h.", "4 min")}
<div style="display:flex;gap:4mm;font-size:9pt"><ol style="flex:1;line-height:1.55;margin:0">{left}</ol><ol type="a" style="flex:1;line-height:1.55;margin:0">{right}</ol></div>
{sub("B", "Talk about it.", "4 min")}
<ol style="line-height:1.55"><li>Are gap years common in Brazil? Why or why not?</li><li>What are the benefits of a gap year? Are there any problems?</li><li>Have you ever taken time off to travel, work or study something new? Would you like to?</li></ol>""",
    29, """<ol><li>A: an <i>internship</i> is a temporary job, often unpaid, to get experience. Drill <i>volunteer</i> /ˌvɑːlənˈtɪr/.</li>
<li>B: some American universities let admitted students start a year later; Harvard College, for example, allows students to defer for a year for travel, work or special projects (Harvard College Admissions, "Considering a Gap Year").</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Gap year activities and reasons</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Lucy and Rita talk about two gap years</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Present continuous, going to, will, present simple for the future</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Four ways to talk about the future</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>4 min</td><td>going to and will · which future?</td><td>5</td></tr>
<tr><td>5 Practice</td><td>9 min</td><td>Choose the future form · Word builder: Lucy's resume</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Plan and present your gap year</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>At City Coffee, Lucy (Neural2-C) tells Rita (Chirp3-HD-Aoede) about her gap year: she studies biology but wants to become a vet, so she's going to volunteer at the animal shelter where Kate found Pepper (Unit 22), learn to ride a horse, and maybe do an internship at a vet clinic. Rita's son Danny has just finished high school and is planning a trip to South America, starting in Brazil. Danny is a new story character. Fact: Harvard College lets admitted students defer for a year for travel, special projects or work (Harvard College Admissions, "Considering a Gap Year").</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students use <i>will</i> for every future (<i>I will meet Danny tomorrow</i>), the present simple for plans (<i>Next year I travel</i> ✗), forget <i>be</i> in <i>going to</i> (<i>I going to</i> ✗), and write <i>gonna</i>.</div>
<div class="box"><h4>AUDIO</h4>Track 34.1 Gap year plans (slow and natural) · Track 34.2 Repeat: going to and will · Track 34.3 Which future?</div>""")

    # Page 2
    tf = [("Lucy is going to help at an animal shelter.", "T"), ("Lucy wants to buy a horse.", "F: she's going to learn to ride one."),
          ("Lucy is hoping to get an internship.", "T: at a vet clinic"), ("Danny is traveling with a friend.", "T: his best friend"),
          ("Danny needs to find a job.", "F: he already works at a supermarket."), ("Danny is learning Spanish.", "F: Portuguese")]
    tfl = [f'<li value="{i+1}">{s} <b>T / F</b> {A(a, "min-width:30mm")}</li>' for i, (s, a) in enumerate(tf)]
    op = [(["I've studied", "I'm studying"], "I'm studying", "You know", "biology at the moment."),
          (["I'm going to take", "I'll take"], "I'm going to take", "So", "a year off from college."),
          (["I'll start", "I'm starting"], "I'm starting", "", "there next week."),
          (["I'm going to go", "I go"], "I'm going to go", "If I get the internship,", "with the vets on their farm visits."),
          (["They're going to", "They'll"], "They're going to", "", "save all their money."),
          (["they're leaving", "they leave"], "they're leaving", "Not yet, but", "sometime in the new year."),
          (["he's studying", "he's going to study"], "he's going to study", "After the trip,", "politics at college."),
          (["we're going to be", "we'll be"], "we're going to be", "It looks like", "busy.")]
    opl = [f'<li value="{i+1}">{(a + " ") if a else ""}{ch(o, r)} {e}</li>' for i, (o, r, a, e) in enumerate(op)]
    b.page(f"""{sec(2, "Listening: gap year plans", "10 min")}
<div style="display:flex;gap:2.5mm;align-items:center"><p style="flex:1;margin:0">At City Coffee, Lucy tells Rita about her gap year. Then Rita talks about her son, Danny, who has just finished high school.</p>{img('B', 25, 18)}{img('C', 25, 18)}{img('D', 25, 18)}</div>
{audiocard(["34.1 · SLOW", "34.1 · NATURAL"])}
{sub("A", "Listen. Are the sentences true (T) or false (F)?", "4 min", "34.1 · SLOW")}
<div style="font-size:9pt">{twocol(tfl, 4)}</div>
{sub("B", "Listen again and choose the words you hear.", "5 min", "34.1 · NATURAL")}
<div style="font-size:8.8pt">{twocol(opl, 5)}</div>
{sub("C", "Whose plan do you like more, Lucy's or Danny's? Why?", "1 min")}""",
    26, """<ol><li>A: ask the student to justify each answer with words from the conversation.</li>
<li>B: let the student predict first; both options are often grammatically possible, but only one is what the speakers say. Danny's trip starts in Brazil: ask what he should see there.</li></ol>""")

    # Page 3
    b.page(f"""{sec(3, "Language focus: future forms", "10 min")}
{sub("A", "Present continuous. Read and answer.", "3 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">1 I'm <b>studying</b> biology at the moment. · 2 I'm <b>starting</b> there next week. · 3 They're <b>working</b> at the supermarket. · 4 They're <b>leaving</b> in the new year.</div>
<p style="margin:.5mm 0;line-height:1.7">About the present: {A("1 and 3", "min-width:14mm")} &nbsp; About the future: {A("2 and 4", "min-width:14mm")} &nbsp; The future sentences are {ch(["predictions", "arrangements"], "arrangements")}.</p>
{sub("B", "Be going to. Read and choose.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">I'm <b>going to take</b> a year off. · I'm also <b>going to learn</b> how to ride a horse. · They're <b>going to save</b> all their money.</div>
<p style="margin:.5mm 0">These sentences are about {ch(["predictions", "plans and intentions"], "plans and intentions")}. Form: {A("am / is / are + going to + base form", "min-width:56mm")}</p>
{sub("C", "Two predictions. Which is an opinion? Which is based on evidence?", "3 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">1 Look at all those people at the door. It looks like we're <b>going to be</b> busy. · 2 I think he'<b>ll have</b> a great time!</div>
<p style="margin:.5mm 0">opinion: {A("2 (will)", "min-width:16mm")} &nbsp; evidence: {A("1 (going to)", "min-width:22mm")}</p>
{sub("D", "Present simple. Read and choose.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">My first lesson <b>is</b> next Friday. · The class <b>starts</b> in a few weeks.</div>
<p style="margin:.5mm 0">These sentences are about {ch(["intentions", "timetables"], "timetables")}.</p>
<div class="box sand"><h4>RULE</h4><b>arrangement</b> → present continuous · <b>plan / intention</b> → going to · <b>prediction with evidence</b> → going to · <b>prediction with opinion</b> → will · <b>timetable</b> → present simple. In fast speech, <i>going to</i> often sounds like <i>gonna</i>: never write it. More on the next page: <b>Grammar reference</b>.</div>""",
    22, """<ol><li>There is some overlap: <i>I'm going to start next week</i> is also possible; the present continuous stresses the arrangement with the shelter.</li>
<li>Drill all the examples; <i>gonna</i> is fine in the student's speech if they recognize it's informal.</li></ol>""")

    grammar_ref.future_forms(b)

    # Page 5
    fa = ["going to", "will", "present continuous", "present simple", "going to", "present continuous"]
    fal = "".join(f"<li>{A(f, 'min-width:30mm')}</li>" for f in fa)
    b.page(f"""{sub("E", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>I will meet Danny tomorrow at six.</td><td><b>I'm meeting Danny tomorrow at six.</b></td><td>an arrangement.</td></tr>
<tr><td>Next year I travel to Chile.</td><td><b>Next year I'm going to travel to Chile.</b></td><td>a plan.</td></tr>
<tr><td>I going to study biology.</td><td><b>I'm going to study biology.</b></td><td>be + going to.</td></tr>
<tr><td>Look at the sky! It will rain.</td><td><b>It's going to rain.</b></td><td>evidence.</td></tr>
<tr><td>I think you're liking the course.</td><td><b>I think you'll like the course.</b></td><td>opinion = will.</td></tr>
<tr><td>I'm gonna call you. (in an email)</td><td><b>I'm going to call you.</b></td><td>don't write gonna.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "4 min")}
{audiocard(["34.2", "34.3"])}
{sub("A", "Listen and repeat. Notice the weak going to and the short 'll.", "2 min", "34.2")}
{twocol([f'<li value="{i+1}">{s}</li>' for i, s in enumerate(S342)], 4)}
{sub("B", "Listen to six sentences. Which future form do you hear? Write going to, will, present continuous or present simple.", "2 min", "34.3")}
<ol style="line-height:1.5;column-count:2;column-gap:5mm">{fal}</ol>""",
    22, """<ol><li>A: <i>going to</i> /ˈɡoʊɪŋ tə/ or /ˈɡʌnə/; <i>he'll</i> /hil/. Students often don't hear the 'll.</li>
<li>B: script: 1 I'm going to learn to ride a horse. 2 I think you'll love it. 3 We're leaving in January. 4 The class starts at six. 5 Look at those clouds. It's going to rain. 6 I'm meeting Danny tomorrow.</li></ol>""")

    # Page 6
    pr = [("I", "'m seeing", "someone about a job on Friday. (see)", "arrangement"), ("I think you", "'ll enjoy", "working with animals. (enjoy)", "opinion"),
          ("Do you want to talk to Tom? He's outside. He", "'s cleaning", "the car. (clean)", "now"), ("Look at those big clouds over there. It", "'s going to rain", ". (rain)", "evidence"),
          ("She", "'s going to learn", "how to surf. She's always wanted to do it. (learn)", "intention"), ("The bus", "leaves", "at 8:30, so hurry up! (leave)", "timetable"),
          ("They", "'re going to get", "a dog, but they haven't decided what kind yet. (get)", "intention"), ("We", "'re having", "coffee with our best friends tomorrow. (have)", "arrangement")]
    prl = "".join(f"<li>{a} {A(v, 'min-width:24mm')}{'' if e[0] in '.' else ' '}{e} {R('(' + w + ')') if T else ''}</li>" for a, v, e, w in pr)
    cv = [("biology", "1"), ("studying", "2"), ("volunteered", "3"), ("internship", "4"), ("realized", "5"), ("took", "6"), ("change", "7")]
    def g(w):
        return A(w, "min-width:18mm")
    cvh = f"""<div class="msg" style="max-width:none;padding:2mm 3mm;font-size:8.6pt;line-height:1.5"><b>Lucy: Resume</b><br>
<b>Education</b> · 2025–2026: studied 1 {g("biology")} at college in Chicago · 2027–present: 2 {g("studying")} veterinary medicine<br>
<b>Experience</b> · 2026–2027: 3 {g("volunteered")} at an animal shelter (cleaning, feeding and walking dogs) · Jan–May 2027: 4 {g("internship")} at a vet clinic (helped with small animals, went on farm visits)<br>
<b>Personal statement</b> · After a year of biology, I 5 {g("realized")} that I really wanted to work with animals. So I 6 {g("took")} a gap year to explore this area. It was a difficult decision, but it confirmed my decision to 7 {g("change")} majors.</div>"""
    b.page(f"""{sec(5, "Practice", "9 min")}
{sub("A", "Complete with the present simple, present continuous, going to or will. Be ready to explain your choice.", "5 min")}
<ol style="line-height:1.62;font-size:9pt">{prl}</ol>
{sub("B", "Word builder: a resume. Imagine Lucy's resume after her gap year. Complete it with the words in the box.", "4 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1"><div class="bank">biology · change · internship · realized · studying · took · volunteered</div>{cvh}</div>{img('F', 30, 26)}</div>""",
    22, """<ol><li>A: the reasons in red (arrangement, opinion…) are for you; ask the student for them.</li>
<li>B: the resume is set in the future of our story, so it uses invented dates. In the US, people say <i>resume</i> (British: <i>CV</i>) and usually don't include a photo or their age. <i>Major</i> = the main subject at college.</li></ol>""")

    # Page 7
    model = ("In my gap year, I'm going to work at a hotel in Florida, because I want to improve my English. I'm starting in June. "
             "Then I'm going to travel around South America with my sister. We're leaving in October. I think it'll be the best year of my life!")
    rows = [("volunteer", "at an animal shelter / at a school / your idea", "Why?"), ("travel", "alone / with a friend", "Where? When? How long?"),
            ("learn", "a language / to drive / your idea", "How? Where?"), ("work", "an internship / a paid job", "Where? Why?")]
    rt = "".join(f"<tr><td><b>{a}</b></td><td>{o}</td><td class='small'>{q}</td><td></td></tr>" for a, o, q in rows)
    b.page(f"""{sec(6, "Speaking: my gap year", "12 min")}
<div style="display:flex;gap:3mm;align-items:center"><p style="flex:1;margin:0">Plan a gap year: real or a dream! Choose at least three activities and make notes. Think about the future forms you need.</p>{img('E', 34, 22)}</div>
{sub("A", "Listen to your teacher's gap year plan. Which future forms do you hear?", "2 min")}
<p class="small" style="margin:0">{R(model) if T else ''}</p>
{sub("B", "Plan. Write key words only.", "3 min")}
<table style="margin:0;font-size:8.8pt"><tr><th style="width:20mm"></th><th>options</th><th style="width:34mm">questions</th><th style="width:52mm">my notes</th></tr>{rt}<tr><td><b>my idea</b></td><td></td><td></td><td></td></tr></table>
{sub("C", "Present your plan. Your teacher asks questions and then repeats your plan back to you. Is it correct?", "5 min")}
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:9pt;line-height:1.45"><b>You:</b> In my gap year, I'm going to work at my family's café. <b>Teacher:</b> What are you going to do after that? <b>You:</b> I'm not sure. Maybe I'll study business. Anyway, I'm starting in August.<br><b>Teacher:</b> OK, so you're going to work at the café, and you're starting in August…</div>
{sub("D", "Which plan is more exciting, yours or your teacher's? More expensive? Better for your resume?", "2 min")}""",
    27, """<ol><li>A: future forms in the model: going to (plans), present continuous (I'm starting, we're leaving), will (I think it'll be…).</li>
<li>C: repeating the plan back gives the student a model of the forms; then swap roles.</li></ol>""")

    # Page 8
    pc = [("A2 Unit 31", "I can describe a photo for about a minute."), ("A2 Unit 32", "I can talk about timetables and personal plans for the future."),
          ("A2 Unit 33", "I can make predictions and say how sure I am."), ("A2 Unit 34", "I can choose the right future form: going to, will or the present continuous.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Do you hear that thunder? It will rain.", "It's going to rain."), ("From now on, I'm starting eating more fruit.", "I'm going to start eating more fruit."),
          ("He's going to travel around Australia during his gap year.", "✓"), ("I think you're having a great time in Paris next month.", "I think you'll have a great time."),
          ("She helps me with my homework at the moment.", "She's helping me…"), ("The new semester starts on September 3.", "✓"),
          ("They're coming over this evening with their new dog.", "✓"), ("We will play tennis at 6:30 on Thursday. (arranged)", "We're playing tennis…")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:40mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Correct the mistakes. If a sentence is correct, write ✓.</b></p>
<ol style="line-height:1.55;font-size:9pt">{hwl}</ol>
<p style="margin-top:1.5mm"><b>2. My dream gap year (50–75 words).</b> Write about your dream gap year. Include one arrangement, two plans and one prediction.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class: the student reads the text aloud; ask follow-up questions with all four forms: <i>When are you leaving? What are you going to do there? Do you think you'll like it?</i></p>""")

    b.extra("Audio script", f"""
{sub("34.1", "Gap year plans (slow and natural)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in S341)}</p>
{sub("34.2", "Repeat: going to and will")}
<p>{" · ".join(S342)}</p>
{sub("34.3", "Which future? (3-second pause)")}
<p>{" · ".join(S343)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 34 - Gap year")
