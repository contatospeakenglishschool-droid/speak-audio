# Speak! Bridge A2 - Unit 22 "Man's best friend" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 22", audio_json="audio_a2-unit-22.json", img_dir="img")

PHOTOS = [("A", "parrot", "a parrot"), ("B", "rabbit", "a rabbit"), ("C", "hamster", "a hamster"), ("D", "goldfish", "a goldfish"),
          ("E", "lizard", "a lizard"), ("F", "snake", "a snake"), ("G", "guinea pig", "a guinea pig"), ("H", "cat", "a cat")]

_r = json.load(open("roteiro.json"))["units"]["a2-unit-22"]
S221 = [x.split(": ", 1) for x in _r["22.1 Kate and Pepper"].split("\n")]
S222 = [x.split(": ", 1)[1] for x in _r["22.2 Repeat: used to"].split("\n")]
S223 = [x.split(": ", 1)[1] for x in _r["22.3 Used to or used"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'
    def box(ans):
        return A(ans, "min-width:7mm;text-align:center") if T else '<span style="display:inline-block;width:7mm;border-bottom:.8pt solid #555">&nbsp;</span>'

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 22", "Man's best friend", "Pets, then and now · <b>used to / didn't use to</b>",
                       [("YOU CAN", "talk about past habits and states and compare them with now"),
                        ("LANGUAGE", "I used to work all day. · I didn't use to know my neighbors. · Did you use to have a pet?"),
                        ("PRONUNCIATION", "used to = /ˈjuːstə/ · used (a map) = /juːzd/")])
    qs = [("I don't want to clean up after it.", "X"), ("It reduces stress.", "✓"), ("Food and visits to the vet are expensive.", "X"),
          ("You get lots of exercise.", "✓"), ("I'm allergic to fur.", "X"), ("It helps you make new friends.", "✓")]
    b.page(f"""{sec(1, "Warm-up: pets", "8 min")}
{sub("A", "Write the name of each pet.", "3 min")}
<div class="bank">cat · goldfish · guinea pig · hamster · lizard · parrot · rabbit · snake</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Are these people for (✓) or against (X) having a pet?", "2 min")}
{twocol([f'<li value="{i+1}">"{q}" {box(a)}</li>' for i, (q, a) in enumerate(qs)], 4)}
{sub("C", "Talk about it.", "3 min")}
<ol><li>Do you have a pet? Why or why not? Which pets are popular in Brazil?</li><li>Can you think of other reasons for or against having a pet?</li></ol>""",
    20, """<ol><li>A: <i>guinea pig</i> /ˈɡɪni pɪɡ/ is neither from Guinea nor a pig. <i>Goldfish</i> is the same in the plural.</li>
<li>B: elicit more reasons and write them on the board: <i>company, responsibility, travel is difficult…</i></li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Pets · for and against having a pet</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Kate meets Rita in the park with her new dog</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>used to / didn't use to · Did you use to…?</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>used to: form, habits and states, used to vs past simple</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>4 min</td><td>used to /ˈjuːstə/ · used /juːzd/</td><td>5</td></tr>
<tr><td>5 Practice</td><td>9 min</td><td>Pepper's life before and now · Word builder: things for a dog</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Guess the pet I used to have</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Kate (Tom's sister, Sweet Kate Bakery in Chicago, voice Neural2-G) adopted Pepper, a small dog, from an animal shelter three months ago. In the park she meets Rita (City Coffee manager, Chirp3-HD-Aoede). Kate talks about the good things; Rita worries about the problems. Fact: in October 2019 the American Heart Association published a review of ten studies (about 3.8 million people) in <i>Circulation: Cardiovascular Quality and Outcomes</i>: dog owners had a 24% lower risk of death from any cause. The studies were observational, so they show a link, not a cause (American Heart Association news release, October 8, 2019; ScienceDaily). The CDC also says walking or playing with pets can lower blood pressure and help with loneliness (CDC, Healthy Pets, Healthy People).</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Portuguese uses the same verb for past and present habits, so students say <i>I use to get up at six</i> ✗ for now (<i>I usually get up at six</i>). They also write <i>use to</i> in positive sentences (the <i>-d</i> is silent), add <i>-d</i> after <i>did</i> (<i>Did you used to…?</i> ✗) and use <i>used to</i> for one event (<i>I used to go to Paris last year</i> ✗).</div>
<div class="box"><h4>AUDIO</h4>Track 22.1 Kate and Pepper (slow and natural) · Track 22.2 Repeat: used to · Track 22.3 Used to or used</div>""")

    # Page 2
    kr = [("getting exercise", "K"), ("living longer", "B"), ("making friends", "K"), ("reducing stress", "K")]
    kn = [("being allergic", "R"), ("being busy", "R"), ("cleaning up", "R"), ("the cost", "R")]
    def krow(items):
        return "".join(f"<tr><td>{box(a)}</td><td>{t}</td></tr>" for t, a in items)
    det = [(["8", "15", "18"], "8", "Kate and Rita last saw each other", "months ago."),
           (["a pet store", "an animal shelter", "a friend"], "an animal shelter", "Kate adopted Pepper from", "."),
           (["3 weeks", "3 months", "3 years"], "3 months", "Kate has had Pepper for", "."),
           (["1–2", "2–3", "3–4"], "2–3", "Kate walks Pepper", "times a day."),
           (["5:30", "6:00", "6:30"], "6:00", "Kate gets up at", "."),
           (["90", "95", "100"], "95", "Rita's grandmother lived to", ".")]
    detl = "".join(f"<li>{a} {ch(o, r)}{'' if e == '.' else ' '}{e}</li>" for o, r, a, e in det)
    b.page(f"""{sec(2, "Listening: Kate and Pepper", "10 min")}
<div style="display:flex;gap:3mm;align-items:center"><p style="flex:1;margin:0">Kate has a new dog, Pepper. On Saturday morning, she meets her friend Rita in the park. Rita is the manager of City Coffee. What do you think Rita says about having a dog?</p>{img('I', 34, 23)}{img('J', 30, 23)}</div>
{audiocard(["22.1 · SLOW", "22.1 · NATURAL"])}
{sub("A", "Listen. Who talks about each idea? Write K (Kate), R (Rita) or B (both).", "3 min", "22.1 · SLOW")}
<table style="margin:0"><tr><th style="width:12mm"></th><th>Positives</th><th style="width:12mm"></th><th>Negatives</th></tr>{"".join(f"<tr><td>{box(a)}</td><td>{t}</td><td>{box(c)}</td><td>{u}</td></tr>" for (t, a), (u, c) in zip(kr, kn))}</table>
{sub("B", "Listen again. Choose the correct answer.", "4 min", "22.1 · NATURAL")}
<ol style="line-height:1.65">{detl}</ol>
{sub("C", "What did Kate read about? Do you think it's true? Why?", "2 min")}
<p class="small">{A("a study from the American Heart Association: people with dogs had a lower risk of dying early", "min-width:120mm")}</p>""",
    24, """<ol><li>A: <i>living longer</i> = B: Rita talks about her grandmother, and Kate about the study. Kate mentions money, but Rita raises it as a problem.</li>
<li>C: the 2019 AHA review found a link, not proof: active, healthy people may also be the ones who get dogs.</li></ol>""")

    # Page 3
    b.page(f"""{sec(3, "Language focus: used to", "10 min")}
{sub("A", "Study the sentences from the conversation.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.6">1. I <b>used to work</b> all day and then watch TV on the sofa every evening. Now I go out for walks with her.<br>
2. The problem was that I <b>didn't use to have</b> a good routine. Now I get up at six.<br>
3. I <b>used to be</b> so stressed.<br>
4. I <b>didn't use to know</b> any of my neighbors, but now everyone wants to talk to me.<br>
5. What kind of dogs <b>did</b> your grandmother <b>use to have</b>?</div>
{sub("B", "Choose the best option to complete the rules.", "5 min")}
<ol style="line-height:1.75"><li><b>used to + verb</b> describes things in the past that {ch(["don't happen now", "still happen"], "don't happen now")}.</li>
<li>In sentence 1, <i>used to work</i> is a {ch(["habit (a repeated action)", "single event"], "habit (a repeated action)")}. In 3 and 4, <i>be</i> and <i>know</i> are {ch(["actions", "states"], "states")}. We use <b>used to</b> for {ch(["habits only", "habits and states"], "habits and states")}.</li>
<li>In negatives and questions, we write {ch(["used to", "use to"], "use to")}, because <b>did / didn't</b> already shows the past.</li>
<li>For a habit <b>now</b>, we use {ch(["use to + verb", "the present simple"], "the present simple")}: <i>Now I get up at six.</i></li></ol>
{sub("C", "Complete the table.", "3 min")}
<table style="margin:0"><tr><th style="width:30mm"></th><th>example</th></tr>
<tr><td><b>positive</b></td><td>She {A("used to", "min-width:16mm")} walk her dogs every day.</td></tr>
<tr><td><b>negative</b></td><td>I {A("didn't use to", "min-width:22mm")} know my neighbors.</td></tr>
<tr><td><b>question</b></td><td>{A("Did", "min-width:9mm")} you {A("use to", "min-width:14mm")} have a pet? · Yes, I {A("did", "min-width:9mm")}. / No, I {A("didn't", "min-width:12mm")}.</td></tr></table>
<div class="box sand"><h4>RULE</h4><b>used to + verb</b> = past habits and states that are different now: <i>I used to be stressed. Now I'm relaxed.</i> Negative: <b>didn't use to</b> · Question: <b>Did … use to…?</b> More on the next page: <b>Grammar reference</b>.</div>""",
    22, """<ol><li>B: ask for evidence in A for each rule. Point out that the form is the same for all persons (no <i>-s</i>).</li>
<li>Personalize: <i>What did you use to do on Saturdays when you were a teenager? What do you usually do now?</i></li></ol>""")

    grammar_ref.used_to(b)

    # Page 5
    ans3 = ["used to", "used", "used to", "used", "used", "used to"]
    p3 = "".join(f"<li>{s.split('. ', 1)[1]} &nbsp; {ch(['used to /ˈjuːstə/', 'used /juːzd/'], 'used to /ˈjuːstə/' if a == 'used to' else 'used /juːzd/')}</li>"
                 for s, a in zip(S223, ans3))
    b.page(f"""{sub("D", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>I use to live in Recife.</td><td><b>I used to live in Recife.</b></td><td>positive: used (with -d).</td></tr>
<tr><td>I didn't used to like coffee.</td><td><b>I didn't use to like coffee.</b></td><td>didn't + use (no -d).</td></tr>
<tr><td>Did you used to have a pet?</td><td><b>Did you use to have a pet?</b></td><td>did + use (no -d).</td></tr>
<tr><td>I use to get up at six now.</td><td><b>I usually get up at six.</b></td><td>now = present simple.</td></tr>
<tr><td>I used to go to Paris last year.</td><td><b>I went to Paris last year.</b></td><td>one time = past simple.</td></tr>
<tr><td>Yes, I used.</td><td><b>Yes, I did.</b></td><td>short answer with did.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "4 min")}
{audiocard(["22.2", "22.3"])}
{sub("A", "Listen and repeat. Build up the sentences. Say used to as one word: /ˈjuːstə/ (yoost-tuh).", "2 min", "22.2")}
<p style="line-height:1.55;margin:.5mm 0">{" · ".join(S222)}</p>
{sub("B", "Listen. Do you hear used to /ˈjuːstə/ (a past habit) or used /juːzd/ (= utilized)? Choose while you listen.", "2 min", "22.3")}
<ol style="line-height:1.6">{p3}</ol>""",
    24, """<ol><li>A: the <i>-d</i> in <i>used to</i> disappears, and <i>s</i> sounds like /s/; in <i>used</i> (utilized) it is /z/ + /d/.</li>
<li>B: after checking, the student reads the six sentences aloud with the right sound.</li></ol>""")

    # Page 6
    pp = [("Now I drink clean water.", "used to drink", "dirty water.", "drink"),
          ("Now I have lots of food.", "didn't use to have", "much food.", "have"),
          ("Now I have a warm home.", "used to be", "cold in the winter.", "be"),
          ("Now I feel safe.", "didn't use to feel", "safe.", "feel"),
          ("Now Kate is my best friend.", "didn't use to have", "any human friends.", "have"),
          ("Now my fur is clean and soft.", "My fur used to be", "dirty.", "be"),
          ("Now I play with other dogs.", "used to fight", "with other dogs.", "fight"),
          ("Now I sleep on a soft bed.", "used to sleep", "on the street.", "sleep")]
    ppl = "".join(f"<li>{n} {'My fur' if a.startswith('My') else 'I'} {A(a.replace('My fur ', ''), 'min-width:26mm')} {e} ({v})</li>"
                  for n, a, e, v in pp)
    wb = [("bed", "where the dog sleeps"), ("brush", "you use it to clean and tidy the dog's fur"), ("collar", "a band that goes around the dog's neck"),
          ("food bowl", "a dish for the dog's food or water"), ("leash", "a long strap you use to walk the dog"), ("microchip", "a tiny electronic tag under the skin with your phone number"),
          ("toy", "a ball or other thing the dog plays with"), ("vet", "an animal doctor")]
    wbl = [f'<li value="{i+1}">{A(w, "min-width:18mm")}: {d}</li>' for i, (w, d) in enumerate(wb)]
    b.page(f"""{sec(5, "Practice", "9 min")}
{sub("A", "Before Kate adopted her, Pepper lived on the street. Complete what Pepper says with used to or didn't use to and the verb.", "5 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><ol style="flex:1;line-height:1.75;margin:0">{ppl}</ol>{img('J', 30, 24)}</div>
<p class="small" style="margin-top:1mm">Now write two sentences about yourself: one thing you <b>used to</b> do and one thing you <b>didn't use to</b> do.</p>
<div class="wline"></div>
{sub("B", "Word builder: things for a dog. Write the words from the box next to their definitions.", "4 min")}
<div class="bank">bed · brush · collar · food bowl · leash · microchip · toy · vet</div>
<ol style="line-height:1.55;font-size:9pt">{"".join(wbl)}</ol>
<p class="small">Which of these things are really necessary? Do you think dogs need clothes?</p>""",
    22, """<ol><li>A: point out <i>used to</i> + state verbs (be, have, feel) and habits (drink, fight, sleep). <i>Leash</i> is American English (British: <i>lead</i>).</li>
<li>B: in many US cities, dogs must be on a leash in public places; ask how it is in the student's city.</li></ol>""")

    # Page 7
    trow = [("It lived:", "outside / in a cage / in the house / in a tank", "in a cage, but it used to fly around the living room"),
            ("It ate:", "meat / fruit and vegetables / seeds", "seeds and fruit"),
            ("It was:", "friendly / shy / sleepy / noisy", "friendly and very noisy"),
            ("It cost:", "a lot of money / a bit of money / very little money", "a bit of money"),
            ("It needed:", "a lot of exercise / a lot of attention / special equipment", "a lot of attention"),
            ("Problems:", "allergies / dirty / dangerous / noisy", "it used to wake everyone up at 5 a.m.!")]
    tr = "".join(f"<tr><td><b>{a}</b></td><td class='small'>{o}</td><td>{R(t) if T else ''}</td></tr>" for a, o, t in trow)
    b.page(f"""{sec(6, "Speaking: guess the pet", "12 min")}
<p style="margin:0 0 1mm">Imagine you used to have one of the pets from page 1 when you were a child. Your teacher also had one. Ask yes/no questions to guess the pet.</p>
{sub("A", "Choose a pet and make notes. Use the ideas or your own.", "3 min")}
<table style="margin:0"><tr><th style="width:22mm"></th><th style="width:72mm">Ideas</th><th>My pet {'· ' + R("teacher's pet: a parrot") if T else ''}</th></tr>{tr}</table>
{sub("B", "Ask your teacher about their pet. Then answer your teacher's questions about your pet.", "6 min")}
<div class="box" style="margin-top:1mm;font-size:9pt"><b>Did</b> your pet <b>use to</b> live in the house? · Yes, it did. It <b>used to</b> live in the house. / No, it <b>didn't</b>.<br><b>Where did</b> it <b>use to</b> sleep? · <b>What did</b> it <b>use to</b> eat? · Was it a…? </div>
{sub("C", "Talk about it.", "3 min")}
<ol><li>Did your family use to have pets when you were a child? What were they like?</li><li>What did you use to do in your free time ten years ago? What do you usually do now?</li><li>Would you like to have a pet in the future? Which one, and why?</li></ol>""",
    24, """<ol><li>B: answer only yes/no until the student has asked at least five questions; insist on <i>Did… use to…?</i> and full answers. Then ask about the student's pet the same way.</li>
<li>C: note errors with <i>use to / used to</i> and with the present habit (<i>usually</i>) for feedback.</li></ol>""")

    # Page 8
    pc = [("A2 Unit 18", "I can agree and disagree with so, neither, me too and me neither."), ("A2 Unit 19", "I can tell the story of someone's life with the past simple."),
          ("A2 Unit 21", "I can tell a story with the past continuous and the past simple."), ("A2 Unit 22", "I can compare my life then and now with used to.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    ow = [("think / I / so / be / stressed / used to / I", "I think I used to be so stressed."),
          ("didn't / I / exercise / use to / much", "I didn't use to exercise much."),
          ("used to / come home / I / an empty apartment / to", "I used to come home to an empty apartment."),
          ("use to / did / you / a pet / have / ?", "Did you use to have a pet?")]
    owl = "".join(f"<li>{w}<br>{A(s, 'min-width:90mm')}</li>" for w, s in ow)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Put the words in order to make sentences.</b></p>
<ol style="line-height:1.55">{owl}</ol>
<p style="margin-top:2mm"><b>2. Then and now (50–75 words).</b> Write about something in your life that changed: a pet, a job, a city, a hobby. What did you use to do? What didn't you use to do? What do you usually do now?</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class: the student reads the text aloud. Ask follow-up questions with <i>Did you use to…?</i> and <i>What do you usually do now?</i></p>""")

    b.extra("Audio script", f"""
{sub("22.1", "Kate and Pepper (slow and natural)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in S221)}</p>
{sub("22.2", "Repeat: used to")}
<p>{" · ".join(S222)}</p>
{sub("22.3", "Used to or used")}
<p>{" · ".join(S223)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 22 - Man's best friend")
