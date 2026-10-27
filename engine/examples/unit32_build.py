# Speak! Essentials A1 - Unit 32 "On the calendar" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
from speak_engine import *
setup(band="A1 · UNIT 32", audio_json="audio_a1-unit-32.json", img_dir="img")

PHOTOS = [("A", "clean the house", "clean"), ("B", "do yoga", "yoga"), ("C", "get a haircut", "haircut"), ("D", "go jogging", "jogging"),
          ("E", "have a meeting", "meeting"), ("F", "see the dentist", "dentist"), ("G", "take an exam", "exam"), ("H", "watch a movie", "movie")]

_r = json.load(open("roteiro.json"))["units"]["a1-unit-32"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["32.1 Lunch"].split("\n")]
S322 = [x.split(": ", 1)[1] for x in _r["32.2 Repeat time phrases"].split("\n")]
S323 = [x.split(": ", 1)[1] for x in _r["32.3 Repeat sentences"].split("\n")]
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LEVEL A1 · UNIT 32", "On the calendar", "Plans and arrangements · <b>present continuous and be going to for the future</b>",
                       [("YOU CAN", "talk about your plans and arrangements and find a time to meet"),
                        ("LANGUAGE", "I'm seeing the dentist at 11:30. · I'm going to clean the bakery."),
                        ("PRONUNCIATION", "going to → gonna /ˈɡɑnə/ (speech only) · on Monday · at eleven")])
    b.page(f"""{sec(1, "Warm-up: in my planner", "8 min")}
{sub("A", "Look at the photos. Write the activity under each photo.", "3 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(w.replace(" ", "&nbsp;") for _, w, _ in PHOTOS)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "On, at or in? Then talk: which activities are in your planner this week?", "5 min")}
<p>{A("on", "min-width:12mm")} Monday, Friday evening &nbsp;·&nbsp; {A("at", "min-width:12mm")} 7:30, eleven o'clock, noon &nbsp;·&nbsp; {A("in", "min-width:12mm")} the morning, December, 2027</p>""",
    26, """<ol><li>A: a <b>planner</b> is a small book or an app with a calendar where you write your plans. <i>see the dentist</i> = go to the dentist.</li>
<li>B: <b>on</b> + days and dates, <b>at</b> + times, <b>in</b> + parts of the day, months, years. American English: <i>on the weekend</i>.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>8 planner activities with photos · on / at / in</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Tom and Kate try to find a day for lunch</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Present continuous (arrangements) and be going to (plans)</td><td>3</td></tr>
<tr><td>4 Pronunciation lab</td><td>5 min</td><td>Time phrases · gonna and wanna</td><td>4</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Tom's trip to São Paulo: questions and answers</td><td>5</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Compare planners and find a time to meet · your plans</td><td>6</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>7</td></tr></table>
<div class="box"><h4>HOW THIS GUIDE WORKS</h4>Every page looks like the Student Book page with the same number. Your notes are in the <b>yellow box</b>.
<span class="red">Answers in red</span> are not in the Student Book. The <span class="time">5 min</span> chips show the time for each activity. Audio scripts are on the last page.</div>
<div class="box sand"><h4>THE STORY CONTINUES</h4>It's December in Chicago. Tom calls his sister Kate to have lunch before Christmas, but they're both busy: Kate is going to clean the bakery, she's having brunch with Lucy and meeting a supplier; Tom is going to watch the Bears game, he's taking his Portuguese exam and seeing the dentist. Finally, they're both free on Thursday: lunch at City Coffee. On page 5, Tom plans a week in São Paulo with Ana, Marcos and Paulo.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>In Portuguese, the simple present often talks about the future, so students say <i>I go to the dentist tomorrow</i> ✗ → <b>I'm going to the dentist / I'm seeing the dentist tomorrow</b>. They also forget <i>be</i>: <i>I going to study</i> ✗ → <b>I'm going to study</b>, and mix prepositions: <i>in Monday, on the morning</i> ✗.</div>
<div class="box"><h4>AUDIO</h4>Track 32.1 Lunch this week? (slow and natural) · Track 32.2 Time phrases · Track 32.3 Sentences</div>""")

    # Page 2
    kate = ["", "", ("1:00 pm", "meeting with a supplier"), "", "Pizza night!", ("", "clean the bakery"), ("11:00 am", "brunch with Lucy")]
    tom = ["Jogging!", "11:30 am Dentist", "", "", ("11:00 am", "Portuguese exam"), "Free!", ("", "watch the Bears game")]
    def cell(x):
        if isinstance(x, tuple):
            return f"{x[0]} * {A(x[1], 'min-width:34mm')}"
        return x
    pt = "".join(f"<tr><td><b>{d}</b></td><td class='small'>{cell(k)}</td><td class='small'>{cell(t)}</td></tr>" for d, k, t in zip(DAYS, kate, tom))
    b.page(f"""{sec(2, "Listening: lunch this week?", "10 min")}
<p>It's December in Chicago. Tom calls his sister Kate. He wants to have lunch with her before Christmas.</p>
{audiocard(["32.1 · SLOW", "32.1 · NATURAL"])}
{sub("A", "Listen. When and where do they decide to have lunch?", "2 min", "32.1 · SLOW")}
<div class="wline">{R("On Thursday, at City Coffee.")}</div>
{sub("B", "Listen again and complete the planners next to the *. One activity is extra.", "6 min", "32.1 · NATURAL")}
<div class="bank">brunch with Lucy · buy a Christmas tree · clean the bakery · meeting with a supplier · Portuguese exam · watch the Bears game</div>
<table style="table-layout:fixed;font-size:9pt"><tr><th style="width:26mm"></th><th>Kate's planner</th><th>Tom's planner</th></tr>{pt}</table>
{sub("C", "Why is Tom taking a Portuguese exam? Guess!", "2 min")}
<div class="wline">{R("Open answer: he visited Ana in São Paulo (Units 22–23) and he's learning Portuguese.")}</div>""",
    26, """<ol><li>A: <b>slow</b> version. <b>brunch</b> = breakfast + lunch, late in the morning. <b>a supplier</b> = a company that sells things to Kate's bakery (flour, sugar…).</li>
<li>B: <b>natural</b> version. The Bears are Chicago's football team. Extra item: <i>buy a Christmas tree</i>.</li></ol>""")

    # Page 3
    b.page(f"""{sec(3, "Language focus: talking about the future", "10 min")}
{sub("A", "Read the sentences from the phone call. Then choose the correct option.", "4 min")}
<table style="table-layout:fixed;font-size:9.3pt"><tr><th>Present continuous</th><th>be going to + verb</th></tr>
<tr><td>I'm having brunch with Lucy at eleven.<br>I'm taking my Portuguese exam on Friday at eleven.<br>I'm meeting a new supplier at one o'clock.</td>
<td>I'm going to clean the bakery on Saturday.<br>I'm going to watch the Bears game.<br>I'm going to make pizza in the evening.</td></tr></table>
<ol><li>Present continuous sentences are often {ch(["arrangements with other people", "plans just for me"], "arrangements with other people")}, with a fixed time.</li>
<li><i>Be going to</i> sentences are often {ch(["arrangements with other people", "plans or intentions"], "plans or intentions")}, sometimes with no fixed time.</li>
<li>Both forms talk about the {ch(["present", "future"], "future")} here.</li></ol>
{sub("B", "Complete the table.", "4 min")}
<table style="table-layout:fixed;font-size:9.3pt"><tr><th style="width:24mm"></th><th>be going to</th><th>present continuous</th></tr>
<tr><td><b>+</b></td><td>She {A("'s going to", "min-width:22mm")} clean the bakery.</td><td>She {A("'s meeting", "min-width:22mm")} a supplier at one.</td></tr>
<tr><td><b>–</b></td><td>I {A("'m not going to", "min-width:26mm")} watch the game.</td><td>I {A("'m not doing", "min-width:22mm")} anything on Thursday.</td></tr>
<tr><td><b>?</b></td><td>{A("Are", "min-width:12mm")} you going to make pizza?</td><td>What {A("are", "min-width:12mm")} you doing this weekend?</td></tr>
<tr><td><b>short answers</b></td><td colspan="2">Yes, I am. / No, I'm not. · Yes, she is. / No, she isn't.</td></tr></table>
<div class="box sand"><h4>REMEMBER</h4><b>be</b> + going to + base form: I<b>'m</b> going to study. ✗ <i>I going to study</i><br>
With <i>go</i>, we usually say <b>I'm going to the bank</b> (not <i>I'm going to go to the bank</i>, but both are correct).</div>""",
    26, """<ol><li>A: the difference is small and native speakers often use both. The key idea: present continuous = it's in the planner, with a time or with other people.</li>
<li>B: drill the contractions: <i>She's going to · I'm not going to · What are you doing?</i></li></ol>""")

    # Page 4
    b.page(f"""{sub("C", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>I go to the dentist tomorrow.</td><td><b>I'm going to the dentist tomorrow.</b></td><td>Future: not the simple present.</td></tr>
<tr><td>I going to study tonight.</td><td><b>I'm going to study tonight.</b></td><td>Don't forget <i>be</i>.</td></tr>
<tr><td>She's going to cleans the car.</td><td><b>She's going to clean the car.</b></td><td>going to + base form.</td></tr>
<tr><td>What you are doing on Friday?</td><td><b>What are you doing on Friday?</b></td><td>Question order: <i>are</i> + you.</td></tr>
<tr><td>See you in Monday!</td><td><b>See you on Monday!</b></td><td><i>on</i> + days.</td></tr>
<tr><td>I'm meeting her on the morning.</td><td><b>I'm meeting her in the morning.</b></td><td><i>in</i> the morning / afternoon.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "5 min")}
{audiocard(["32.2", "32.3"])}
{sub("A", "Time phrases. Listen and repeat.", "2 min", "32.2")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S322)}</div>
{sub("B", "Sentences. Listen and repeat.", "2 min", "32.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S323)}</div>
<div class="box" style="margin-top:1mm"><h4>GONNA AND WANNA</h4>In fast, informal speech, <b>going to</b> sounds like <b>gonna</b> /ˈɡɑnə/ and <b>want to</b> sounds like <b>wanna</b> /ˈwɑnə/: <i>I'm gonna call you. Wanna have a coffee?</i><br>
OK: talking to friends, songs, text messages to friends. ✗ Not OK: exams, emails to your boss, job interviews.</div>""",
    25, """<ol><li>4A: link the words: <i>on_Monday</i>, <i>at_eleven</i>, <i>in_December</i>.</li>
<li>4B: the student can understand <i>gonna</i> and <i>wanna</i> in movies and songs, but should write <i>going to</i> and <i>want to</i>.</li></ol>""")

    # Page 5
    plan = [("Monday", "9:00 pm Fly to São Paulo"), ("Tuesday", "12:30 Lunch with Ana and Marcos"), ("Wednesday", "Visit Ibirapuera Park"),
            ("Thursday", "8:00 pm New Year's Eve party at Ana's"), ("Friday", "Go to the beach in Santos"), ("Saturday", "Try feijoada"), ("Sunday", "10:00 am Fly back to Chicago")]
    ptab = "".join(f"<tr><td style='width:24mm'><b>{d}</b></td><td>{x}</td></tr>" for d, x in plan)
    qa = [("Q", "When is he flying to São Paulo?", "He's flying to São Paulo on Monday at 9 pm.", "A"),
          ("Q", "Who is he having lunch with on Tuesday?", "He's having lunch with Ana and Marcos.", "A"),
          ("A", "He's going to visit Ibirapuera Park.", "What's he going to do on Wednesday?", "P"),
          ("Q", "What is he doing on Thursday evening?", "He's going to a New Year's Eve party at Ana's at 8 pm.", "A"),
          ("A", "Yes, he is. He's going to go to the beach in Santos.", "Is he going to go to the beach on Friday?", "P"),
          ("Q", "What's he going to try on Saturday?", "He's going to try feijoada.", "P"),
          ("A", "He's flying back to Chicago on Sunday at 10 am.", "When is he flying back to Chicago?", "A")]
    ql = "".join(f"<li>{('<b>Q:</b> ' + g) if k == 'Q' else ('<b>A:</b> ' + g)} <span style='float:right'>{A(m, 'min-width:8mm')}</span><div class='wline'>{R(('A: ' if k == 'Q' else 'Q: ') + w)}</div></li>" for k, g, w, m in qa)
    b.page(f"""{sec(5, "Practice", "8 min")}
{sub("A", "Tom is going to spend a week in São Paulo. Look at his planner.", "1 min")}
<table style="table-layout:fixed;font-size:9pt;margin-top:0">{ptab}</table>
{sub("B", "Write the answer (A) or the question (Q). Then write A (arrangement) or P (plan) on the right.", "7 min")}
<ol style="line-height:1.4">{ql}</ol>""",
    22, """<p>A–B: arrangements have a time or other people (a flight, a lunch, a party); plans are Tom's own ideas. <b>Ibirapuera Park</b> is a big park in São Paulo; <b>Santos</b> is a city on the coast near São Paulo. Ask: <i>What else can Tom do in São Paulo?</i></p>""")

    # Page 6
    acts = ["get up early", "finish a work project", "play soccer with friends", "have a meeting", "eat a cheeseburger",
            "get a haircut", "meet my brother and go to a concert", "do yoga at home", "clean the house"]
    tp = ["7:00 pm dinner with my parents", "going to clean the house", "", "6:30 pm doctor's appointment", "", "going to go to the beach", "1:00 pm lunch with friends"]
    rows = "".join(f"<tr><td style='height:7.5mm'><b>{d}</b></td><td></td><td class='small'>{R(t)}</td></tr>" for d, t in zip(DAYS, tp))
    b.page(f"""{sec(6, "Speaking", "12 min")}
{sub("A", "Choose five activities and write them in your planner. Add a time for arrangements.", "3 min")}
<div class="bank">{" · ".join(acts)}</div>
<table style="table-layout:fixed;font-size:9pt"><tr><th style="width:26mm"></th><th>My planner</th><th>My teacher's planner</th></tr>{rows}</table>
{sub("B", "Ask your teacher and complete the second column. Then find a day to meet and plan something together.", "5 min")}
<div class="msg" style="max-width:none;padding:2mm 4mm;line-height:1.55"><b>You:</b> What are you doing on Monday?<br><b>Teacher:</b> I'm having dinner with my parents at seven. What about you?<br><b>You:</b> I'm going to do yoga at home. Are you free on Wednesday?</div>
{sub("C", "And your real plans?", "4 min")}
<ol><li>What are you doing this weekend? Do you have any arrangements?</li><li>What are you going to do on New Year's Eve?</li><li>Are you going to travel next year? Where?</li></ol>""",
    22, """<ol><li>B: your planner is in red. Answer with the right form: <i>I'm having… / I'm going to…</i> You're both free on Wednesday or Friday: plan something (a coffee, a movie).</li>
<li>C: correct <i>I go to… tomorrow</i> → <i>I'm going to…</i></li></ol>""")

    # Page 7
    pc = [("Unit 28", "I can ask questions in the present and past with who, whose, which…"), ("Unit 29", "I can buy clothes: ask about sizes, colors and prices, try things on and pay."),
          ("Unit 30", "I can talk about food with some, any, a / an and a lot of."), ("Unit 31", "I can ask and talk about quantity: how much, how many, a few, a little."),
          ("Unit 32", "I can talk about my plans and arrangements for the future.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    ow = [("taking / tomorrow / an English exam / at ten / They're", "They're taking an English exam tomorrow at ten.", "A"),
          ("going / get up / to / She's / early every day this week", "She's going to get up early every day this week.", "P"),
          ("this afternoon? / Are / a meeting / having / they", "Are they having a meeting this afternoon?", "A"),
          ("to / going / He's / cook / this weekend / a big lunch", "He's going to cook a big lunch this weekend.", "P"),
          ("seeing / I'm / the doctor / at four o'clock / today", "I'm seeing the doctor today at four o'clock.", "A"),
          ("you / going / Are / go swimming / to / on Saturday?", "Are you going to go swimming on Saturday?", "P")]
    owl = "".join(f"<li><i>{s}</i> <span style='float:right'>{A(m, 'min-width:8mm')}</span><div class='wline'>{R(c)}</div></li>" for s, c, m in ow)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:15mm"></th><th>In English…</th><th style="width:20mm">Easy!</th><th style="width:20mm">Sometimes</th><th style="width:20mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Put the words in order.</b> Then write A (arrangement) or P (plan).</p>
<ol style="line-height:1.35">{owl}</ol>
<p style="margin-top:2mm"><b>2. My week.</b> Write 6 sentences about your plans and arrangements for next week. Use the present continuous and <i>be going to</i>.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    16, """<p>Next class: start with homework 2. Ask questions: <i>What are you doing on…? Are you going to…?</i></p>""")

    b.extra("Audio scripts", f"""
{sub("32.1", "Lunch this week? (slow and natural)")}
<p style="line-height:1.5">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("32.2", "Time phrases")}
<p>{" · ".join(S322)}</p>
{sub("32.3", "Sentences")}
<p>{" ".join(S323)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essentials 32 - On the calendar")
