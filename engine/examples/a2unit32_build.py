# Speak! Bridge A2 - Unit 32 "Northern lights" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 32", audio_json="audio_a2-unit-32.json", img_dir="img")

PHOTOS = [("A", "glacier", "glacier"), ("B", "iceberg", "iceberg"), ("C", "whale", "whale"), ("D", "sea otter", "sea otter"),
          ("E", "moose", "moose"), ("F", "hot spring", "hot spring"), ("G", "Northern Lights", "aurora"), ("H", "bear", "bear")]
_r = json.load(open("roteiro.json"))["units"]["a2-unit-32"]
S321 = [x.split(": ", 1) for x in _r["32.1 The Alaska tour"].split("\n")]
S322 = [x.split(": ", 1)[1] for x in _r["32.2 Repeat: build it up"].split("\n")]
S323 = [x.split(": ", 1)[1] for x in _r["32.3 Repeat: questions about plans"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 32", "Northern lights", "Travel plans in Alaska · <b>present simple and present continuous for the future</b>",
                       [("YOU CAN", "talk about travel timetables and your personal plans"),
                        ("LANGUAGE", "The bus leaves at seven. · We're having dinner at six. · What time does it start? · Are you coming?"),
                        ("PRONUNCIATION", "linking: leaves‿at seven · lands‿at two")])
    b.page(f"""{sec(1, "Warm-up: wild places", "8 min")}
{sub("A", "Write the words under the photos.", "4 min")}
<div class="bank">bear · glacier · hot spring · iceberg · moose · Northern Lights · sea otter · whale</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Talk about it.", "4 min")}
<ol style="line-height:1.5"><li>Which US state has all these things? {A("Alaska", "min-width:20mm")}</li><li>Have you ever seen snow, a glacier or the Northern Lights? Would you like to?</li><li>Do you prefer hot places like Brazil or cold places? Why?</li></ol>""",
    22, """<ol><li>A: <i>glacier</i> /ˈɡleɪʃər/; <i>moose</i> is the same in the singular and plural (one moose, two moose). The Northern Lights are also called the <i>aurora borealis</i>.</li>
<li>B: Alaska is the largest US state; it's very far north, so it has long summer days and long winter nights.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Nature words: Alaska</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Paulo and Carol talk about their Alaska tour</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Present simple (timetables) and present continuous (arrangements)</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Present tenses for the future: form, use, questions</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>4 min</td><td>Linking · questions about plans</td><td>5</td></tr>
<tr><td>5 Practice</td><td>9 min</td><td>Ten sentences · Word builder: travel talk</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Information gap: the last three days of the tour</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Paulo (New York, Neural2-I) and his cousin Carol (Orlando, Chirp3-HD-Leda) are going on a guided tour of Alaska in September with Maya, Paulo's colleague from the travel agency (Unit 06). They talk on the phone about the plan. The tour itself is invented, but the places are real. Facts: the aurora season in Fairbanks runs from about August 21 to April 21 (Explore Fairbanks, explorefairbanks.com, "Aurora Season"); boat tours from Seward into Kenai Fjords National Park visit tidewater glaciers, and people often see whales and sea otters (National Park Service, nps.gov/kefj, "Boat Tours"); Chena Hot Springs is about 60 miles from Fairbanks (alaska.org). Boat tour seasons usually end in mid to late September, so the tour is in early September.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students use the present simple for personal plans (<i>Tomorrow I meet my sister</i> ✗), forget the third-person -s with timetables (<i>The bus leave at seven</i> ✗), make questions without auxiliaries (<i>What time the tour starts?</i> ✗) and use <i>will</i> for everything.</div>
<div class="box"><h4>AUDIO</h4>Track 32.1 The Alaska tour (slow and natural) · Track 32.2 Repeat: build it up · Track 32.3 Repeat: questions about plans</div>""")

    # Page 2
    def cell(w):
        return A(w, "min-width:18mm")
    plan = f"""<table style="margin:0;font-size:8.6pt;table-layout:fixed"><tr><th style="width:24mm"></th><th>morning</th><th>afternoon</th><th>evening</th></tr>
<tr><td><b>Day 1</b> (Monday)</td><td>—</td><td>arrive in Anchorage at 2:00</td><td>early dinner with Maya at 1 {cell("six")}</td></tr>
<tr><td><b>Day 2</b> (Tuesday)</td><td>bus to Seward at 7:00</td><td>boat trip: 2 {cell("glaciers")}, icebergs, 3 {cell("whales")}, 4 {cell("sea otters")}</td><td>—</td></tr>
<tr><td><b>Day 3</b> (Wednesday)</td><td>—</td><td>fly to 5 {cell("Fairbanks")} at 3:00</td><td>6 {cell("Northern Lights")} tour</td></tr>
<tr><td><b>Day 4</b> (Thursday)</td><td>Paulo: 7 {cell("photography")} tour</td><td>Carol and Maya: 8 {cell("hot spring")}</td><td>—</td></tr></table>"""
    vb = [(["lands", "is landing"], "lands", "It says the flight", "in Anchorage at two o'clock on Monday."),
          (["have", "'re having"], "'re having", "We", "an early dinner at a seafood restaurant."),
          (["do you meet", "are you meeting"], "are you meeting", "What time", "?"),
          (["leaves", "is leaving"], "leaves", "The bus", "at seven to take us to Seward."),
          (["starts", "is starting"], "starts", "The boat trip", "at eleven."),
          (["take", "'m taking"], "'m taking", "I", "my warmest jacket."),
          (["leaves", "is leaving"], "leaves", "On Wednesday the plane", "at three."),
          (["Do you and Maya come", "Are you and Maya coming"], "Are you and Maya coming", "", "?"),
          (["go", "are going"], "are going", "Maya and I", "to the hot spring."),
          (["doesn't leave", "isn't leaving"], "doesn't leave", "The bus", "until after lunch.")]
    vbl = [f'<li value="{i+1}">{(a + " ") if a else ""}{ch(o, r)}{e if e == "?" else " " + e}</li>' for i, (o, r, a, e) in enumerate(vb)]
    b.page(f"""{sec(2, "Listening: the Alaska tour", "10 min")}
<p style="margin:0">Paulo and his cousin Carol are going on a guided tour of Alaska in September with Maya, Paulo's colleague from the travel agency. They talk on the phone about the plan.</p>
{audiocard(["32.1 · SLOW", "32.1 · NATURAL"])}
{sub("A", "Listen and complete the plan. Use one or two words.", "4 min", "32.1 · SLOW")}
{plan}
{sub("B", "Choose the correct verb form. Then listen again and check.", "5 min", "32.1 · NATURAL")}
<div style="font-size:8.8pt">{twocol(vbl, 6)}</div>
{sub("C", "Who do you agree with: Paulo or Carol? What would you choose on Thursday?", "1 min")}""",
    20, """<ol><li>A: let the student read the table first and predict. <i>Seward</i> /ˈsuːərd/ is a small port town south of Anchorage.</li>
<li>B: don't explain the rule yet. Ask the student to read the script aloud (TB last page) if there is time.</li></ol>""")

    # Page 3
    b.page(f"""{sec(3, "Language focus: present tenses for the future", "10 min")}
{sub("A", "Read the sentences. Then choose the correct option.", "3 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">The flight <b>lands</b> at two o'clock on Monday. · The bus <b>leaves</b> at seven. · The boat trip <b>starts</b> at eleven.</div>
<ol style="line-height:1.7"><li>The verb form is the {ch(["present simple", "present continuous"], "present simple")}. Every sentence has {ch(["a time", "a person's name"], "a time")}.</li>
<li>These are {ch(["personal plans", "the tour's timetable"], "the tour's timetable")}, and they are {ch(["certain", "uncertain"], "certain")}.</li></ol>
{sub("B", "Read the sentences. Then choose the correct option.", "3 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">Maya and I <b>are having</b> an early dinner. · I<b>'m going</b> on the photography tour. · Maya and I <b>are going</b> to the hot spring.</div>
<ol style="line-height:1.7"><li>The verb form is the {ch(["present simple", "present continuous"], "present continuous")}.</li>
<li>These are {ch(["personal plans", "the tour's timetable"], "personal plans")}: the people have already {ch(["decided and arranged them", "read them in a brochure"], "decided and arranged them")}.</li></ol>
{sub("C", "Questions. How do we make them?", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">What time <b>does</b> the boat trip <b>start</b>? · <b>Are</b> you and Maya <b>coming</b>? · What time <b>are</b> you <b>meeting</b>?</div>
<p style="margin:.5mm 0;line-height:1.7">present simple: {A("(question word) + do / does + subject + verb", "min-width:60mm")}<br>present continuous: {A("(question word) + am / is / are + subject + verb-ing", "min-width:60mm")}</p>
<div class="box sand"><h4>RULE</h4><b>Timetables</b> (transportation, tours, events): <b>present simple</b> + time. <b>Personal arrangements</b>: <b>present continuous</b> + time. Don't forget the <b>-s</b>: <i>the bus leaves</i>. More on the next page: <b>Grammar reference</b>.</div>""",
    27, """<ol><li>Concept question: <i>Who decided that the bus leaves at seven? (the tour company) Who decided to have dinner at six? (Carol and Maya)</i></li>
<li>Both forms are certain; neither is a guess. Contrast with <i>maybe I'll…</i> later in the course.</li></ol>""")

    grammar_ref.present_for_future(b)

    # Page 5
    b.page(f"""{sub("D", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>Tomorrow I meet my sister for lunch.</td><td><b>Tomorrow I'm meeting my sister for lunch.</b></td><td>personal arrangement.</td></tr>
<tr><td>The bus leave at seven.</td><td><b>The bus leaves at seven.</b></td><td>he / she / it: -s.</td></tr>
<tr><td>What time the tour starts?</td><td><b>What time does the tour start?</b></td><td>do / does in questions.</td></tr>
<tr><td>You are coming with us?</td><td><b>Are you coming with us?</b></td><td>question word order.</td></tr>
<tr><td>The museum is opening at 9:00 every day.</td><td><b>The museum opens at 9:00 every day.</b></td><td>a timetable.</td></tr>
<tr><td>I will have dinner with Carol tonight. (arranged)</td><td><b>I'm having dinner with Carol tonight.</b></td><td>an arranged plan.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "4 min")}
{audiocard(["32.2", "32.3"])}
{sub("A", "Build it up. Listen and repeat. Link the final consonant to the next vowel: lands‿at, leaves‿at.", "2 min", "32.2")}
{twocol([f'<li value="{i+1}">{s}</li>' for i, s in enumerate(S322)], 5)}
{sub("B", "Listen and repeat the questions. Then ask your teacher about their plans for the weekend.", "2 min", "32.3")}
{twocol([f'<li value="{i+1}">{s}</li>' for i, s in enumerate(S323)], 4)}""",
    20, """<ol><li>A: linking helps students remember the -s: <i>leave<b>s‿a</b>t</i> sounds like "leave-zat".</li>
<li>B: wh- questions fall at the end; <i>Are you coming…?</i> and <i>Does the bus…?</i> rise.</li></ol>""")

    # Page 6
    pr = [("", "Are", "we", "having", "lunch together after the tour? (have)"), ("The bus", "leaves", "", "", "for the airport right after breakfast tomorrow. (leave)"),
          ("Paulo", "is meeting", "", "", "Maya for coffee later today. (meet)"), ("Carol is really tired. She", "is staying", "", "", "in tonight. (stay)"),
          ("The glacier tour", "starts", "", "", "early, at 7:30. (start)"), ("They", "'re trying", "", "", "reindeer sausage for dinner tonight. Do you want to join them? (try)"),
          ("When", "does", "the concert", "finish", "? (finish)"), ("This afternoon, we", "'re visiting", "", "", "the gift shop to buy a present for my dad. (visit)"),
          ("What time", "do", "we", "arrive", "at the hotel on Friday? (arrive)"), ("We", "fly", "", "", "home on Sunday afternoon. (fly)")]
    def pl(a, v1, m, v2, e):
        s = (a + " " if a else "") + A(v1, "min-width:16mm")
        if v2:
            s += f" {m} " + A(v2, "min-width:14mm")
        return s + ("" if e[0] == "?" else " ") + e
    prl = "".join(f"<li>{pl(*x)}</li>" for x in pr)
    wb = [("The rest of the day is free.", "There are no more activities today.", "d"), ("We can sleep late.", "We can stay in bed in the morning.", "a"),
          ("No way!", "Absolutely not!", "f"), ("You're going to be jealous!", "You'll wish you had it too!", "b"),
          ("It's cold on the water.", "It's cold on the boat.", "e"), ("the aurora season", "the months when you can see the Northern Lights", "c")]
    left = "".join(f"<li>{a} {A(l, 'min-width:7mm;text-align:center')}</li>" for a, _, l in wb)
    right = "".join(f"<li>{d}</li>" for l, d in sorted([(l, d) for _, d, l in wb]))
    b.page(f"""{sec(5, "Practice", "9 min")}
{sub("A", "Complete the sentences with the present simple or the present continuous.", "6 min")}
<ol style="line-height:1.62;font-size:9pt">{prl}</ol>
{sub("B", "Word builder: travel talk from the conversation. Match 1–6 with a–f.", "3 min")}
<div style="display:flex;gap:4mm;font-size:9pt"><ol style="flex:1;line-height:1.55;margin:0">{left}</ol><ol type="a" style="flex:1;line-height:1.55;margin:0">{right}</ol></div>""",
    22, """<ol><li>A: ask the student to justify each answer: <i>timetable or arrangement?</i> 10: <i>fly</i> (timetable) and <i>'re flying</i> (our plan) are both correct.</li>
<li>B: <i>sleep late</i> (American English) = <i>sleep in</i>. Reindeer sausage is a popular food in Alaska.</li></ol>""")

    # Page 7
    q = '<span style="color:#9aa3a8">?</span>'
    def tc(sb, tb):
        return R(tb) if T else (sb if sb else q)
    rows = [("Day 5 (Friday)", ("9:00–12:00 glacier hike: easy or difficult trail?", None), ("", "1:30–4:30 museum: Alaska history or Alaska Native art?"), ("7:00 dinner: salmon, reindeer sausage or vegetarian?", None)),
            ("Day 6 (Saturday)", ("", "10:00 visit to a sled dog kennel: meet the dogs or ride on a summer sled?"), ("free afternoon: shopping for local art or warm sweaters?", None), ("", "8:00 goodbye party at the hotel")),
            ("Day 7 (Sunday)", ("11:00 bus to the airport: window or aisle seat on the plane?", None), ("", "1:30 the plane takes off; it lands in New York at 11:45 p.m."), ("—", None))]
    def c(x):
        sb, tb = x
        return sb if tb is None else tc(sb, tb)
    rt = "".join(f"<tr><td><b>{d}</b></td><td>{c(m)}</td><td>{c(a)}</td><td>{c(e)}</td></tr>" for d, m, a, e in rows)
    b.page(f"""{sec(6, "Speaking: the last three days", "12 min")}
<p style="margin:0">You're on the same Alaska tour as Paulo, Carol and Maya. Here are the last three days.</p>
{sub("A", "Read the plan. For each activity with two options, circle the option you want.", "2 min")}
<table style="margin:0;font-size:8.6pt;table-layout:fixed"><tr><th style="width:22mm"></th><th>morning</th><th>afternoon</th><th>evening</th></tr>{rt}</table>
{sub("B", "Some information is missing (?). Ask your teacher questions and complete the plan.", "5 min")}
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:9pt;line-height:1.45"><b>You:</b> What do we do on Friday afternoon?<br><b>Teacher:</b> We visit a museum from 1:30 to 4:30. You can choose: Alaska history or Alaska Native art.<br><b>You:</b> I'm going to the Alaska Native art museum. I love art!</div>
<div class="wline"></div><div class="wline"></div>
{sub("C", "Now tell your teacher your choices for the three days. Use the present continuous.", "3 min")}
<p class="small" style="margin:0"><i>On Friday morning I'm doing the easy trail, because…</i></p>
{sub("D", "Talk about it: What other activities would you like to do in Alaska? What are you doing next weekend?", "2 min")}""",
    27, """<ol><li>B: the red information is only in your guide; answer with the present simple (timetable). Make the student ask full questions: <i>What time does the bus leave? What do we do on Saturday morning?</i></li>
<li>C: insist on the present continuous for the student's choices (arrangements).</li></ol>""")

    # Page 8
    pc = [("A2 Unit 28", "I can use adverbs in the correct position."), ("A2 Unit 29", "I can check in, go through security and understand announcements on a plane."),
          ("A2 Unit 31", "I can describe a photo for about a minute."), ("A2 Unit 32", "I can talk about timetables and personal plans for the future.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Where does the tour finish?", "", "It finishes outside the hotel."), ("", "Who are you having breakfast with?", "I'm having breakfast with my sister."),
          ("When do we arrive back at the hotel?", "", "We arrive back at 6:00."), ("Are you visiting the museum or the gallery?", "", "I'm visiting the gallery."),
          ("", "What time are we meeting?", "We're meeting at 4:30."), ("Where are you sitting on the bus today?", "", "I'm sitting at the front, with Maya."),
          ("", "Does the movie start at 3:00?", "No, it starts at 2:30."), ("", "What time does the bus leave?", "The bus leaves at 7:00.")]
    def hwi(qq, qa, ans):
        if qq:
            return f"<li>{qq}<br>{A(ans, 'min-width:90mm')}</li>"
        return f"<li>{A(qa, 'min-width:90mm')}<br>{ans}</li>"
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Write the question or the answer. Use the present simple or the present continuous. Invent the details.</b></p>
<div style="font-size:8.8pt">{twocol([f'<li value="{i+1}">' + hwi(*x)[4:] for i, x in enumerate(hw)], 5)}</div>
<p style="margin-top:1.5mm"><b>2. My plans (50–75 words).</b> Write a message to a friend about your plans for next weekend. Include one timetable (a movie, a bus, a class) and two arrangements with other people.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Accept any sensible invented details in 1. Next class: the student reads the message aloud; ask questions: <i>What time does the movie start? Who are you going with?</i></p>""")

    b.extra("Audio script", f"""
{sub("32.1", "The Alaska tour (slow and natural)")}
<p style="line-height:1.42">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in S321)}</p>
{sub("32.2", "Repeat: build it up")}
<p>{" · ".join(S322)}</p>
{sub("32.3", "Repeat: questions about plans")}
<p>{" · ".join(S323)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 32 - Northern lights")
