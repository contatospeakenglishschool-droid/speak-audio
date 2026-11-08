# Speak! Bridge A2 - Unit 45 "On screen" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 45", audio_json="audio_a2-unit-45.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["a2-unit-45"]
S451 = [x.split(": ", 1) for x in _r["45.1 Welcome to the studio"].split("\n")]
S452 = [x.split(": ", 1)[1] for x in _r["45.2 Repeat: the passive"].split("\n")]
S453 = [x.split(". ", 1)[1] for x in [y.split(": ", 1)[1] for y in _r["45.3 Active or passive?"].split("\n")]]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 45", "On screen", "Media jobs · <b>the present simple passive</b>",
                       [("YOU CAN", "describe how something is made, step by step, with the passive"),
                        ("LANGUAGE", "The budget is agreed. · The models are created. · The game is tested by lots of people."),
                        ("PRONUNCIATION", "is and are in passives · active or passive?")])
    vv = [("launch", "introduce a new product to the market"), ("edit", "make changes to a book or movie so that it's better"), ("design", "plan how something will look or work"),
          ("create", "make something completely new, often from your imagination"), ("produce", "make something, often something to sell"), ("promote", "try to get people to buy, like or use something")]
    vs = sorted(vv, key=lambda x: x[1])
    vl = "".join(f"<li>{d} {A(w, 'min-width:16mm')}</li>" for w, d in vs)
    ex = [("advertising: information to make people want to buy something", "commercials on TV or online"), ("budget: a plan for how to spend money", "made by people, companies or governments"),
          ("genre: a type of book, movie or game", "adventure, love story, horror"), ("target audience: the people a product is for", "teenagers, parents, people who drive a lot")]
    exs = sorted(e for _, e in ex)
    exl = "".join(f"<li>{w} {A('abcd'[exs.index(e)], 'min-width:6mm;text-align:center')}</li>" for w, e in ex)
    exsl = "".join(f"<li>{e}</li>" for e in exs)
    b.page(f"""{sec(1, "Warm-up: media jobs", "8 min")}
<div style="display:flex;gap:2mm;margin-bottom:1mm">{"".join(img(l, 34, 20) for l in "ABCD")}</div>
<div class="box" style="margin:0;font-size:9pt;line-height:1.5">Many people work in media jobs: they make movies, websites, video games or e-books. Some people <b>create</b> new ideas, while others <b>design</b> the artwork. Other people <b>edit</b> the content and <b>produce</b> the final product. Then a team <b>promotes</b> it, and the company <b>launches</b> it at a party or an online event.</div>
{sub("A", "Find the words in bold. Write them next to the meanings.", "3 min")}
<ol style="line-height:1.5;font-size:9pt;margin:0;column-count:2;column-gap:5mm">{vl}</ol>
{sub("B", "Match the words 1–4 with the examples a–d.", "3 min")}
<div style="display:flex;gap:4mm;font-size:8.8pt"><ol style="flex:1.2;line-height:1.5;margin:0">{exl}</ol><ol type="a" style="flex:.8;line-height:1.5;margin:0">{exsl}</ol></div>
{sub("C", "Would you like a media job? Which one?", "2 min")}""",
    22, """<ol><li>A: four of the six verbs have second-syllable stress: deSIGN, creATE, proDUCE, proMOTE. <i>Genre</i> /ˈʒɑːnrə/ is a French word.</li>
<li>Brazil has a big gaming and streaming audience; ask about the student's favorite games, series or apps.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Media verbs: create, design, edit, produce, promote, launch</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>A manager shows a new intern around a video game studio</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Active and passive (present simple)</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>The passive (present simple)</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>4 min</td><td>Passive phrases · active or passive?</td><td>5</td></tr>
<tr><td>5 Practice</td><td>9 min</td><td>How a website is built · genres</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Describe a process: a music video and an e-book</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>A one-off scene: at a video game studio in Chicago, the manager (Chirp3-HD-Charon) introduces Jordan, the new intern, and Nora from planning (Studio-O) explains her work. The studio, the game Castle Dreams and all the staff are invented; Jordan doesn't speak in the audio.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students forget <i>be</i> (<i>The game tested</i>), use the base form (<i>is test</i>), say <i>for</i> instead of <i>by</i> (<i>produced for Annie</i>), and regularize irregular participles (<i>choosed, finded</i>).</div>
<div class="box"><h4>AUDIO</h4>Track 45.1 Welcome to the studio (slow and natural) · Track 45.2 Repeat: the passive · Track 45.3 Active or passive?</div>""")

    # Page 2
    fx = [("Jordan is starting a three-month internship.", "six-month"), ("Nora loves creating puzzle games.", "fantasy games"),
          ("The production team agrees on the budget.", "the planning team"), ("The manager thinks testing is the easiest stage.", "the most difficult"),
          ("Natasha is working from home today.", "at a video game event"), ("Jordan doesn't know the studio's games.", "he plays them every weekend")]
    fxl = "".join(f"<li>{s} {A(c, 'min-width:28mm')}</li>" for s, c in fx)
    op = [("At the planning stage, the budget", ["is agreed", "agrees"], "is agreed", "."), ("Before we", ["are agreed", "agree"], "agree", "on the budget, we come up with an idea."),
          ("After the artwork", ["produces", "is produced"], "is produced", ", we create a prototype."), ("The character models", ["create", "are created"], "are created", "."),
          ("Marlon", ["creates", "is created"], "creates", "the models."), ("The game", ["tests", "is tested"], "is tested", "by lots of people."),
          ("When they", ["find", "are found"], "find", "a bug, they fix the code."), ("Sometimes new bugs", ["find", "are found"], "are found", "months later!")]
    opl = [f'<li value="{i+1}">{a} {ch(o, r)}{"" if e[0] in ".,!" else " "}{e}</li>' for i, (a, o, r, e) in enumerate(op)]
    b.page(f"""{sec(2, "Listening: welcome to the studio", "10 min")}
<div style="display:flex;gap:2.5mm;align-items:center"><p style="flex:1;margin:0">Jordan is starting an internship at a video game studio in Chicago. The manager introduces him to the team.</p>{img('E', 30, 20)}</div>
{audiocard(["45.1 · SLOW", "45.1 · NATURAL"])}
{sub("A", "Listen. Each sentence has one false piece of information. Correct it.", "4 min", "45.1 · SLOW")}
<ol style="font-size:9pt;line-height:1.5;margin:0">{fxl}</ol>
{sub("B", "Listen again and choose the form you hear.", "5 min", "45.1 · NATURAL")}
<div style="font-size:8.8pt">{twocol(opl, 5)}</div>
{sub("C", "Find words in the conversation that mean: to suggest a new idea (3 words) · the first working version · a mistake in the code.", "1 min")}
<p class="small" style="margin:0">{A("come up with · a prototype · a bug", "min-width:50mm")}</p>""",
    22, """<ol><li>A: an <i>intern</i> is someone who works (often for little or no money) to get experience. Predict the corrections before listening.</li>
<li>B: the student must decide who does the action; the passive is presented on the next page.</li></ol>""")

    # Page 3
    b.page(f"""{sec(3, "Language focus: active and passive", "10 min")}
{sub("A", "Compare. Read and choose.", "4 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">1 The character models <b>are created</b>, and the sound effects <b>are recorded</b>. (passive) · 2 Marlon <b>creates</b> the models, and Eloise <b>records</b> the sound effects. (active)</div>
<ol style="margin:.5mm 0;line-height:1.65"><li>In sentence 2, <i>the models</i> and <i>the sound effects</i> are the {ch(["subjects", "objects"], "objects")}.</li>
<li>The object of the active sentence becomes the {ch(["subject", "object"], "subject")} of the passive sentence.</li>
<li>In the passive sentence, we're more interested in {ch(["the actions", "the people"], "the actions")}.</li>
<li>Passive = <i>am / is / are</i> + {ch(["verb-ing", "past participle"], "past participle")}.</li></ol>
{sub("B", "Past participles. Find one regular and three irregular participles.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">The budget is agreed, and the target audience is chosen. · New bugs are found months later. · After the videos are made, they're put on social media.</div>
<p style="margin:.5mm 0">regular: {A("agreed", "min-width:16mm")} irregular: {A("chosen, found, made (also put)", "min-width:44mm")}</p>
{sub("C", "Is or are? Why?", "2 min")}
<p style="margin:.5mm 0"><i>The game <b>is</b> tested. · The models <b>are</b> created.</i> {A("is = singular subject; are = plural subject", "min-width:60mm")}</p>
{sub("D", "Who does it? Change to passive with by.", "2 min")}
<p style="margin:.5mm 0">Annie produces the basic artwork. → {A("The basic artwork is produced by Annie.", "min-width:70mm")}</p>
<div class="box sand"><h4>RULE</h4><b>Passive</b> = am / is / are + past participle. Use it when the action is more important than who does it, and to describe <b>processes</b>. Add <b>by</b> + person only if it's important. More on the next page: <b>Grammar reference</b>.</div>""",
    25, """<ol><li>Check <i>subject</i>, <i>object</i> and <i>past participle</i> before you start. Only the present simple passive is practiced in this unit.</li>
<li>Portuguese also has a passive (and often uses impersonal constructions instead); ask the student to compare.</li></ol>""")

    grammar_ref.passive_present(b)

    # Page 5
    ap = ["P", "A", "P", "A", "P", "A"]
    apl = "".join(f"<li>{A(x, 'min-width:10mm;text-align:center')}</li>" for x in ap)
    b.page(f"""{sub("E", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>The game tested by players.</td><td><b>The game is tested by players.</b></td><td>passive needs be.</td></tr>
<tr><td>The game is test every day.</td><td><b>The game is tested every day.</b></td><td>past participle.</td></tr>
<tr><td>The videos is made by Natasha's team.</td><td><b>The videos are made…</b></td><td>plural: are.</td></tr>
<tr><td>The artwork is produced for Annie.</td><td><b>…produced by Annie.</b></td><td>who does it: by.</td></tr>
<tr><td>The audience is choosed.</td><td><b>The audience is chosen.</b></td><td>irregular participle.</td></tr>
<tr><td>The models are created by someone.</td><td><b>The models are created.</b></td><td>don't add by + unknown.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "4 min")}
{audiocard(["45.2", "45.3"])}
{sub("A", "Listen and repeat. is and are are weak and linked: the budget‿is‿agreed.", "2 min", "45.2")}
{twocol([f'<li value="{i+1}">{s}</li>' for i, s in enumerate(S452)], 4)}
{sub("B", "Listen to six sentences. Are they active (A) or passive (P)?", "2 min", "45.3")}
<ol style="line-height:1.5;column-count:3;column-gap:5mm">{apl}</ol>""",
    26, """<ol><li>A: <i>is</i> often sounds like /z/ after a vowel (<i>The game's tested</i> in fast speech); <i>are</i> is /ər/.</li>
<li>B: script: 1 The game is tested by our team. 2 Marlon creates the models. 3 The sound effects are recorded. 4 They find a lot of bugs. 5 The website is launched at a party. 6 Nora writes the stories.</li></ol>""")

    # Page 6
    ws = [("I'm not sure how much you know about how a website", "build", "is built"), ("A customer comes to us with ideas. These ideas", "discuss", "are discussed"),
          ("at a meeting. At the meeting, the client also", "choose", "chooses"), ("a domain name, and this name", "register", "is registered"),
          (". We also", "find", "find"), ("a platform to host the site. Our designer", "suggest", "suggests"), ("a theme. Then the content", "add", "is added"),
          (". Sometimes an online store", "include", "is included"), (". The site", "link", "is linked"), ("to social media. Finally, the new site", "launch", "is launched")]
    wst = " ".join(f"{a} <sup>{i+1}</sup>{A(c, 'min-width:22mm')} ({v})" for i, (a, v, c) in enumerate(ws)) + " at a party or an online event."
    gn = {"books or movies": "love story, mystery, science fiction", "music": "country, hip-hop, rock", "video games": "action-adventure, puzzle, sports", "websites": "blog, business, educational"}
    gnt = "".join(f"<tr><td style='width:30mm'><b>{k}</b></td><td>{A(v, 'min-width:60mm')}</td></tr>" for k, v in gn.items())
    b.page(f"""{sec(5, "Practice", "9 min")}
{sub("A", "A manager explains how a website is built. Complete with the active or passive form of the verbs.", "6 min")}
<div class="box" style="font-size:9pt;line-height:1.9">{wst}</div>
{sub("B", "Word builder: genres. Put three genres in each group.", "3 min")}
<div class="bank">action-adventure · blog · business · country · educational · hip-hop · love story · mystery · puzzle · rock · science fiction · sports</div>
<table style="margin:0;font-size:9pt">{gnt}</table>""",
    22, """<ol><li>A: ask who does each action: if a person is the subject (the client, we, our designer), it's active.</li>
<li>B: accept reasonable variations (a mystery game, a sports website). Ask about Brazilian music genres too: samba, sertanejo, funk, MPB.</li></ol>""")

    # Page 7
    mv = ["invite a director to help", "decide on a genre for the video", "find a filming location", "create a storyboard", "film the video", "edit the video and add the titles", "make a short teaser for social media", "launch the video"]
    mvl = "".join(f"<li>{s}{(' ' + R('→ A director is invited…' if i == 0 else '')) if T else ''}</li>" for i, s in enumerate(mv))
    eb = ["The book is edited.", "A title is chosen.", "A platform is found to sell the book.", "A cover is designed.", "A book description is written.", "The book is launched on social media.", "Special discounts are offered at first.", "Online events are organized."]
    add = ["You also need costume people and make-up artists.", "It might tell a story or show the band playing.", "Always film everything several times."]
    add2 = ["Ask lots of different people to read the book first.", "It should be short, original and interesting.", "The cover should show the genre clearly."]
    b.page(f"""{sec(6, "Speaking: how is it made?", "12 min")}
<div style="display:flex;gap:3mm;align-items:center"><p style="flex:1;margin:0">You're in a band and want to make a music video. Your teacher is a writer who wants to publish an e-book.</p>{img('F', 30, 20)}</div>
<div class="two"><div class="box" style="margin:0;font-size:8.8pt"><h4>YOUR PROCESS: A MUSIC VIDEO</h4><ol style="margin:0;line-height:1.45">{mvl}</ol></div>
<div class="box sand" style="margin:0;font-size:8.8pt"><h4>ADD TO YOUR TEACHER'S PROCESS</h4><ol style="margin:0;line-height:1.45">{"".join(f"<li>{x}</li>" for x in add2)}</ol>{('<p style="margin:1mm 0 0">' + R("Teacher's process (e-book): " + " ".join(eb)) + '</p>') if T else ''}</div></div>
{sub("A", "Describe your process with the passive. Your teacher adds extra information.", "4 min")}
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:9pt">First, a director <b>is invited</b> to help. Then a genre <b>is decided</b> on…</div>
{sub("B", "Listen to your teacher's e-book process. Add the information in the box at the right moment.", "4 min")}
{sub("C", "Compare the processes.", "4 min")}
<ol style="margin:0;line-height:1.5"><li>Are any stages the same? Which process is more difficult? More expensive?</li><li>Which could make you richer or more famous? How are Brazilian music videos made popular?</li></ol>""",
    29, """<ol><li>A: when the student describes the music video, add these at the right step: "You also need costume people and make-up artists." (step 1) "It might tell a story or show the band playing." (step 2) "Always film everything several times." (step 5)</li>
<li>B: describe the e-book process from the red text; the student interrupts with the three extra points.</li></ol>""")

    # Page 8
    pc = [("A2 Unit 42", "I can understand and give advice and instructions at a pharmacy."), ("A2 Unit 43", "I can explain the rules of a game."),
          ("A2 Unit 44", "I can explain how to solve a problem and why a solution works."), ("A2 Unit 45", "I can describe a process with the present simple passive.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    wb = [("Decide on the type of webinar. (The presenter usually does this.)", "The type of webinar is decided by the presenter."), ("Choose the date and time. (The manager does this.)", "The date and time are chosen by the manager."),
          ("Make the slides. (The presenter does this.)", "The slides are made by the presenter."), ("Find a platform.", "A platform is found."),
          ("Set up the cameras. (Natasha does this.)", "The cameras are set up by Natasha."), ("Promote the webinar on social media.", "The webinar is promoted on social media.")]
    wbl = "".join(f"<li>{a}<br>{A(c, 'min-width:80mm')}</li>" for a, c in wb)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p style="margin:.5mm 0"><b>1. How to organize a webinar (an online event). Change the instructions to the passive. Use by only when it's useful.</b></p>
<ol style="line-height:1.4;font-size:8.8pt;margin:0">{wbl}</ol>
<p style="margin-top:1.5mm"><b>2. How is it made? (50–75 words)</b> Describe how something is made or done in Brazil, step by step: for example, brigadeiro, a TV show, or a product from your city. Use the passive.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class: the student reads the process; you ask passive questions: <i>How is it made? When is it sold? Is it exported?</i></p>""")

    b.extra("Audio script", f"""
{sub("45.1", "Welcome to the studio (slow and natural)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in S451)}</p>
{sub("45.2", "Repeat: the passive")}
<p>{" · ".join(S452)}</p>
{sub("45.3", "Active or passive? (3-second pause)")}
<p>{" · ".join(S453)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 45 - On screen")
