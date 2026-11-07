# Speak! Bridge A2 - Unit 37 "Well-being" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 37", audio_json="audio_a2-unit-37.json", img_dir="img")

PHOTOS = [("A", "swimming", "swimming"), ("B", "running", "running"), ("C", "cycling", "cycling"), ("D", "meditation", "meditation"),
          ("E", "yoga", "yoga"), ("F", "hiking", "hiking"), ("G", "dance class", "dance class"), ("H", "tennis", "tennis")]
_r = json.load(open("roteiro.json"))["units"]["a2-unit-37"]
S371 = [x.split(": ", 1) for x in _r["37.1 The Feel Good podcast"].split("\n")]
S372 = [x.split(": ", 1)[1] for x in _r["37.2 Repeat: -ing forms"].split("\n")]
S373 = [x.split(". ", 1)[1] for x in [y.split(": ", 1)[1] for y in _r["37.3 Write the -ing word"].split("\n")]]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 37", "Well-being", "Keeping fit and happy · <b>-ing forms (gerunds)</b>",
                       [("YOU CAN", "talk about exercise and well-being, and use -ing forms as nouns and after verbs like enjoy, avoid and miss"),
                        ("LANGUAGE", "Swimming is good for your heart. · I enjoy running. · Thanks for joining us. · I look forward to seeing you."),
                        ("PRONUNCIATION", "-ing /ɪŋ/ · linking in -ing phrases")])
    b.page(f"""{sec(1, "Warm-up: ways to keep fit", "8 min")}
{sub("A", "Look at the photos. Name the activities.", "2 min")}
{photo_grid(T, PHOTOS)}
{sub("B", "Talk about it.", "6 min")}
<ol style="line-height:1.5;margin:0"><li>Do you do any of these activities? Have you ever tried any of them?</li><li>Which activity is best for your heart? Which is the most relaxing?</li>
<li>Which activities can you do inside, outside or both? Which do people usually do alone?</li><li>What activities are popular in Brazil? Think of the beach, the park and the gym.</li></ol>""",
    22, """<ol><li>A: drill <i>meditation</i> /ˌmɛdɪˈteɪʃən/ and <i>yoga</i> /ˈjoʊɡə/. Collocations: <i>go</i> swimming / running / cycling / hiking; <i>do</i> yoga / meditation; <i>play</i> tennis; <i>take</i> a dance class.</li>
<li>B: accept any reasonable answers; the student will hear some of these ideas in the podcast.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Activities to keep fit and relax</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Priya on the Feel Good podcast</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>-ing forms as subjects, objects, after prepositions and verbs</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>-ing forms (gerunds)</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>4 min</td><td>-ing phrases · write the -ing word</td><td>5</td></tr>
<tr><td>5 Practice</td><td>9 min</td><td>Order the words · go, play or do?</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Questions about your life with -ing forms</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Priya (Chirp3-HD-Kore; Units 26 and 35), Tom and Lucy's roommate and a medical student, is the guest on the Feel Good podcast (Host: Studio-O). In Unit 26 she does yoga; here she also teaches yoga at a community center and goes running along Lake Michigan. The podcast is invented. Fact: the CDC says adults need at least 150 minutes of moderate-intensity physical activity a week, for example 30 minutes a day, five days a week (CDC, "Adult Activity: An Overview").</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students use the infinitive where English needs a gerund: <i>To walk is good</i>, <i>Thanks for help me</i>, <i>I enjoy to run</i>, <i>I look forward to see you</i>, <i>go to swim</i>. They may also say <i>runing</i> or pronounce -ing as /ɪŋɡ/.</div>
<div class="box"><h4>AUDIO</h4>Track 37.1 The Feel Good podcast (slow and natural) · Track 37.2 Repeat: -ing forms · Track 37.3 Write the -ing word</div>""")

    # Page 2
    op = [("Priya teaches", ["yoga", "dance", "swimming"], "yoga", "at a community center."), ("Well-being means feeling", ["relaxed", "healthy and happy", "beautiful"], "healthy and happy", "."),
          ("Adults need at least 150 minutes of activity a", ["day", "week", "month"], "week", "."), ("The host goes to the gym once a", ["week", "month", "day"], "month", "."),
          ("The host used to", ["swim", "run", "cycle"], "cycle", "to work."), ("Priya goes running", ["along the lake", "in a gym", "at night"], "along the lake", "once a week.")]
    opl = [f'<li value="{i+1}">{a} {ch(o, r)}{"" if e == "." else " "}{e}</li>' for i, (a, o, r, e) in enumerate(op)]
    gp = [("I want to start by a", "sking", "you to define well-being."), ("We hear a lot a", "bout", "well-being these days."),
          ("If you d", "islike", "exercising, you should consider changing activities."), ("I always avoid g", "oing", "to the gym."),
          ("A lot of people e", "njoy", "exercising if they can be outside."), ("Or you might think about c", "ycling", "."),
          ("I m", "iss", "cycling!"), ("In bad weather, you can k", "eep", "cycling."), ("D", "ancing", "is a really fun workout."),
          ("I actually look f", "orward", "to running in the snow!")]
    gpl = [f'<li value="{i+1}">{a}{A(m, "min-width:14mm")}{"" if e == "." else " "}{e}</li>' for i, (a, m, e) in enumerate(gp)]
    b.page(f"""{sec(2, "Listening: the Feel Good podcast", "10 min")}
<div style="display:flex;gap:2.5mm;align-items:center"><p style="flex:1;margin:0">Priya, Tom and Lucy's roommate, is a medical student. Today she's a guest on Feel Good, a Chicago podcast. The topic is well-being.</p>{img('I', 26, 18)}{img('E', 26, 18)}</div>
{audiocard(["37.1 · SLOW", "37.1 · NATURAL"])}
{sub("A", "Listen and choose the correct option.", "4 min", "37.1 · SLOW")}
<div style="font-size:9pt">{twocol(opl, 4)}</div>
{sub("B", "Listen again and complete the words. The first letter is given.", "5 min", "37.1 · NATURAL")}
<div style="font-size:8.8pt">{twocol(gpl, 6)}</div>
{sub("C", "Do you get 150 minutes of activity a week? What's your favorite way to keep fit?", "1 min")}""",
    24, """<ol><li>A: the CDC (Centers for Disease Control and Prevention) recommends at least 150 minutes of moderate activity a week, for example fast walking.</li>
<li>B: let the student predict first; most gaps are verbs that go with an -ing form, used in the Language focus.</li></ol>""")

    # Page 3
    vb = ["avoid", "dislike", "enjoy", "keep", "look forward to", "miss", "think about"]
    b.page(f"""{sec(3, "Language focus: -ing forms", "10 min")}
{sub("A", "Nouns in a sentence. Match the words in bold with a, b or c.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">1 <b>Yoga</b> is the best way to keep fit. {A("c", "min-width:6mm")} · 2 Today we're going to discuss <b>well-being</b>. {A("b", "min-width:6mm")} · 3 Thanks for your <b>advice</b>! {A("a", "min-width:6mm")}<br><b>a</b> after a preposition &nbsp; <b>b</b> object of the sentence &nbsp; <b>c</b> subject of the sentence</div>
{sub("B", "Verb + -ing can do the same jobs. Match again.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">1 <b>Running</b> is an activity you can do in your local park. {A("c", "min-width:6mm")} · 2 Thanks for <b>joining</b> us. {A("a", "min-width:6mm")} · 3 My friends and I discuss <b>running</b> a lot. {A("b", "min-width:6mm")}</div>
<p class="small" style="margin:.5mm 0">When verb + -ing works like a noun, it's called a <b>gerund</b>.</p>
{sub("C", "Some verbs need a gerund after them: <i>If you dislike <b>exercising</b>…</i> Look at 2B. Find six more.", "3 min")}
<p style="margin:.5mm 0">{A(" · ".join(x for x in vb if x != "dislike"), "min-width:100mm")}</p>
{sub("D", "Other -ing forms. Match 1–3 with a–c.", "3 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">1 What about if it's <b>raining</b>? {A("c", "min-width:6mm")} · 2 Exercise is something we have to do, even if it's <b>boring</b>. {A("a", "min-width:6mm")} · 3 I <b>go running</b> along the lake once a week. {A("b", "min-width:6mm")}<br><b>a</b> an adjective &nbsp; <b>b</b> go + -ing for an activity &nbsp; <b>c</b> a continuous verb</div>
<div class="box sand"><h4>RULE</h4>A <b>gerund</b> (verb + -ing) works like a noun: as a <b>subject</b> (<i>Swimming is fun.</i>), an <b>object</b> (<i>I discuss running.</i>), after a <b>preposition</b> (<i>Thanks for joining us.</i>) and after verbs like <b>enjoy, avoid, dislike, miss, keep, consider, think about, look forward to</b>. More on the next page: <b>Grammar reference</b>.</div>""",
    20, """<ol><li>A–B: explain <i>subject</i>, <i>object</i> and <i>preposition</i> with simple examples if needed.</li>
<li>C: <i>think about</i> and <i>look forward to</i> are phrasal verbs; their last word is a preposition, so a gerund follows.</li></ol>""")

    grammar_ref.gerunds(b)

    # Page 5
    wa = ["eating", "Walking", "joining", "doing", "opening", "swimming"]
    gaps = ["I avoid ___ late at night.", "___ is great exercise.", "We're thinking about ___ a gym.", "She finished ___ her homework.", "Do you mind ___ the window?", "He's really good at ___."]
    gl = "".join(f"<li>{g.replace('___', A(w, 'min-width:18mm'))}</li>" for g, w in zip(gaps, wa))
    b.page(f"""{sub("E", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>To walk is the best exercise.</td><td><b>Walking is the best exercise.</b></td><td>gerund as subject.</td></tr>
<tr><td>Thanks for help me.</td><td><b>Thanks for helping me.</b></td><td>preposition + -ing.</td></tr>
<tr><td>I enjoy to run in the park.</td><td><b>I enjoy running in the park.</b></td><td>enjoy + -ing.</td></tr>
<tr><td>I look forward to see you.</td><td><b>I look forward to seeing you.</b></td><td>to is a preposition.</td></tr>
<tr><td>Let's go to swim.</td><td><b>Let's go swimming.</b></td><td>go + -ing.</td></tr>
<tr><td>I like runing.</td><td><b>I like running.</b></td><td>double the n.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "4 min")}
{audiocard(["37.2", "37.3"])}
{sub("A", "Listen and repeat. Say -ing as /ɪŋ/: no /g/ at the end.", "2 min", "37.2")}
{twocol([f'<li value="{i+1}">{s}</li>' for i, s in enumerate(S372)], 4)}
{sub("B", "Listen and write the -ing word you hear.", "2 min", "37.3")}
<ol style="line-height:1.6;column-count:2;column-gap:5mm;font-size:9pt">{gl}</ol>""",
    29, """<ol><li>A: /ɪŋ/ ends with the back of the tongue up, with no /g/ sound; Brazilians often add /g/ or /i/ (<i>running-ee</i>). Link: <i>going‿to the gym</i>, <i>looking‿forward</i>.</li>
<li>B: script: 1 I avoid eating late at night. 2 Walking is great exercise. 3 We're thinking about joining a gym. 4 She finished doing her homework. 5 Do you mind opening the window? 6 He's really good at swimming.</li></ol>""")

    # Page 6
    ow = [("about / Do / cycling / me? / talk / to / want / with / you", "Do you want to talk about cycling with me?", "after a preposition"),
          ("a deer! / cycling / the park / through / We / we saw / were / when", "We were cycling through the park when we saw a deer!", "continuous verb"),
          ("a lot. / and / discuss / friends / I / My / running", "My friends and I discuss running a lot.", "object"),
          ("for / good / heart. / is / Swimming / very / your", "Swimming is very good for your heart.", "subject"),
          ("a / buy / goggles. / good / idea / It's / swimming / to", "It's a good idea to buy swimming goggles.", "adjective"),
          ("in the winter. / keep / outdoors / running / With / warm clothes, / you can", "With warm clothes, you can keep running outdoors in the winter.", "after keep"),
          ("alone, / go / Most people / running / but I / with a friend. / run", "Most people go running alone, but I run with a friend.", "go + -ing"),
          ("don't have / I / it. / really miss / running / time / to do / when I", "I really miss running when I don't have time to do it.", "after miss")]
    owl = "".join(f"<li>{w}<br>{A(s + ((' (' + u + ')') if T else ''), 'min-width:100mm')}</li>" for w, s, u in ow)
    gpd = [("go", "swimming, running, cycling, hiking"), ("play", "tennis, soccer, volleyball"), ("do", "yoga, meditation, exercise")]
    gpt = "".join(f"<tr><td style='width:14mm'><b>{v}</b></td><td>{A(w, 'min-width:70mm')}</td></tr>" for v, w in gpd)
    b.page(f"""{sec(5, "Practice", "9 min")}
{sub("A", "Put the words in order. How is the -ing form used in each sentence?", "6 min")}
<ol style="line-height:1.45;font-size:8.8pt;margin:0">{owl}</ol>
{sub("B", "Word builder: go, play or do? Put the activities in the table.", "3 min")}
<div class="bank">cycling · exercise · hiking · meditation · running · soccer · swimming · tennis · volleyball · yoga</div>
<table style="margin:0;font-size:9pt">{gpt}</table>
<p class="small" style="margin:.5mm 0"><b>go</b> + -ing activity · <b>play</b> + games with a ball · <b>do</b> + other activities</p>""",
    20, """<ol><li>A: do number 1 together. The uses in red come from the Language focus.</li>
<li>B: in American English, <i>soccer</i> (British <i>football</i>). <i>Football</i> in the US is American football.</li></ol>""")

    # Page 7
    prompts = [("an activity I do for exercise", "walking"), ("something I think about doing when I wake up", "drinking coffee"),
               ("something I look forward to doing every day", "reading in bed"), ("something I try to avoid doing", "checking my phone at night"),
               ("something I'd miss doing if I stopped", "teaching English"), ("something I enjoy doing on vacation", "swimming in the ocean"),
               ("something I want to keep doing when I'm older", "traveling"), ("how I'd describe English grammar (an adjective)", "interesting")]
    pt = "".join(f"<tr><td>{p}</td><td></td><td>{R(t) if T else ''}</td></tr>" for p, t in prompts)
    b.page(f"""{sec(6, "Speaking: my life in -ing forms", "12 min")}
<div style="display:flex;gap:3mm;align-items:center"><p style="flex:1;margin:0">Complete the <b>me</b> column with -ing forms. Then ask your teacher and complete the <b>my teacher</b> column.</p>{img('F', 30, 20)}</div>
{sub("A", "Write your answers.", "3 min")}
<table style="margin:0;font-size:8.8pt"><tr><th></th><th style="width:38mm">me</th><th style="width:38mm">my teacher</th></tr>{pt}</table>
{sub("B", "Ask and answer. Ask an extra question each time.", "7 min")}
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:9pt;line-height:1.45"><b>You:</b> Tell me an activity you do for exercise. <b>Teacher:</b> Walking is an activity I do for exercise. <b>You:</b> How often do you go walking? <b>Teacher:</b> Every morning. What about you? <b>You:</b> The activity I do for exercise is swimming…</div>
{sub("C", "How many answers are the same or similar? What's the most surprising answer?", "2 min")}""",
    22, """<ol><li>A: the red answers are a model for your side; replace them with your real answers.</li>
<li>B: insist on full sentences with -ing forms: <i>Walking is…</i>, <i>I look forward to reading…</i>. The last question needs an adjective (<i>interesting, confusing</i>).</li></ol>""")

    # Page 8
    pc = [("A2 Unit 34", "I can choose the right future form: going to, will or the present continuous."), ("A2 Unit 35", "I can make suggestions and offers when I plan a day out."),
          ("A2 Unit 36", "I can write a clear, polite work email."), ("A2 Unit 37", "I can use -ing forms after verbs like enjoy and avoid, and as subjects.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("I was swim in the ocean when I saw a dolphin!", "swimming"), ("I'm looking forward to run again when the weather is nicer.", "running"),
          ("If you dislike walk, try a dance class!", "walking"), ("Lots of people wear cycle shorts.", "cycling"), ("Thanks for walk with me.", "walking"),
          ("To walk is the best form of exercise.", "Walking"), ("Would you like to go cycle with me sometime?", "cycling"), ("You should consider to walk to work.", "walking")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:22mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Each sentence needs an -ing form. Correct the mistakes.</b></p>
<ol style="line-height:1.55;font-size:9pt">{hwl}</ol>
<p style="margin-top:1.5mm"><b>2. My well-being (50–75 words).</b> What do you do to stay healthy and happy? Write about things you enjoy doing, things you avoid doing and one thing you're thinking about starting.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class: the student reads the text aloud; ask follow-up questions with gerunds: <i>Why do you enjoy…? What's stopping you from starting…?</i></p>""")

    b.extra("Audio script", f"""
{sub("37.1", "The Feel Good podcast (slow and natural)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in S371)}</p>
{sub("37.2", "Repeat: -ing forms")}
<p>{" · ".join(S372)}</p>
{sub("37.3", "Write the -ing word (3-second pause)")}
<p>{" · ".join(S373)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 37 - Well-being")
