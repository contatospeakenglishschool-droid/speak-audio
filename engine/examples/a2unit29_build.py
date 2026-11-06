# Speak! Bridge A2 - Unit 29 "Air travel" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 29", audio_json="audio_a2-unit-29.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["a2-unit-29"]
S291 = [x.split(": ", 1) for x in _r["29.1 At the airport"].split("\n")]
S292 = [x.split(": ", 1)[1] for x in _r["29.2 Repeat: questions and requests"].split("\n")]
S293 = [x.split(": ", 1)[1] for x in _r["29.3 Rising or falling?"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 29", "Air travel", "At the airport and on the plane · <b>questions, requests and instructions</b>",
                       [("YOU CAN", "check in, go through security and understand announcements on a plane"),
                        ("LANGUAGE", "May I see your passport, please? · Place your bag on the scale. · We are about to take off."),
                        ("PRONUNCIATION", "rising ↗ and falling ↘ intonation · aisle /aɪl/")])
    wu = [("a seat next to the walkway in the middle of the plane", "aisle seat"), ("the machine that weighs your bag at check-in", "scale"),
          ("the people who look after passengers on a plane", "flight attendants"), ("the document with your seat number that you need to get on the plane", "boarding pass"),
          ("a small table on the back of the seat in front of you", "tray table"), ("the place where you wait to get on your plane", "departure gate"),
          ("you fasten it when you sit down on a plane", "seat belt"), ("the space above the seats for your carry-on bag", "overhead bin")]
    wl = "".join(f'<li>{d} {A(a, "min-width:28mm")}</li>' for d, a in wu)
    b.page(f"""{sec(1, "Warm-up: air travel words", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">{sub("A", "Match the words with the definitions.", "5 min")}
<div class="bank">aisle seat · boarding pass · departure gate · flight attendants · overhead bin · scale · seat belt · tray table</div></div>{img('A', 30, 22)}{img('C', 30, 22)}</div>
<ol style="line-height:1.5;font-size:9pt">{wl}</ol>
{sub("B", "Talk about it.", "3 min")}
<ol style="line-height:1.55"><li>How often do you fly? Do you prefer a window seat or an aisle seat?</li><li>Have you ever used English at an airport or on a plane? What happened?</li></ol>""",
    25, """<ol><li>A: <i>aisle</i> has a silent <i>s</i>: /aɪl/, like <i>I'll</i>. To <i>board</i> = to get on a plane. In the US, people say <i>flight attendants</i> (also <i>cabin crew</i>), <i>overhead bin</i> (British: <i>overhead locker</i>) and <i>carry-on bag</i> (British: <i>hand luggage</i>).</li>
<li>B: point out that many international flights use English, even between non-English-speaking countries.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Air travel words</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Ana at O'Hare: check-in, security, on the plane</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Questions, requests, instructions and announcements</td><td>3</td></tr>
<tr><td>+ Language reference</td><td>–</td><td>Four kinds of sentences · intonation · useful phrases</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>4 min</td><td>Rising and falling intonation</td><td>5</td></tr>
<tr><td>5 Practice</td><td>9 min</td><td>One missing word · Word builder: airport words</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Two role-plays: check-in and on the plane</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Ana (Neural2-F), Tom's online student from Brazil, flies home to São Paulo after a visit to Chicago. Situation 1: check-in agent (Studio-O). Situation 2: a security officer (Chirp3-HD-Charon). Situation 3: a passenger (Chirp3-HD-Charon) and flight attendant announcements (Studio-O). Facts: Terminal 5 is O'Hare's international terminal, with the M gates (Airport Improvement, "O'Hare Unveils Larger, More Modern Terminal 5"); gate M12 is an example, as gates change every day. Since July 8, 2025, the TSA no longer requires most travelers to take off their shoes at U.S. security checkpoints (DHS announcement, reported by Kiplinger and Frommer's), so our officer asks for a belt and jacket instead. In the US, security uses <i>bins</i>, not <i>trays</i>.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students use imperatives as requests (<i>Give me a water</i> ✗), say <i>What?</i> instead of <i>Sorry?</i>, answer requests with nothing or <i>Here is</i> ✗, use flat intonation in questions, and pronounce the <i>s</i> in <i>aisle</i>.</div>
<div class="box"><h4>AUDIO</h4>Track 29.1 At the airport (slow and natural) · Track 29.2 Repeat: questions and requests · Track 29.3 Rising or falling?</div>""")

    # Page 2
    g1 = [("M", "ay", "I see your passport, please?"), ("A", "re", "you checking any bags today?"), ("D", "id", "you pack your bag yourself?"), ("P", "lace", "your bag on the scale, please."), ("The flight will be r", "eady", "to board at 4:35.")]
    g2 = [("P", "lace", "your items in the bin."), ("T", "ake", "off your belt and your jacket."), ("S", "tep", "this way, please."), ("A", "re", "you wearing any jewelry?"), ("C", "an", "you open your bag, please?")]
    g3 = [("Please p", "lace", "your bags in the overhead bins."), ("Please fasten your seat belt when we switch on the s", "ign", "."), ("We are about to t", "ake", "off."), ("We'll shortly be p", "assing", "through the cabin with drinks and snacks.")]
    def gl(items):
        return "".join(f"<li>{a}{A(g, 'min-width:11mm')}{'' if e[0] in '.' else ' '}{e}</li>" for a, g, e in items)
    b.page(f"""{sec(2, "Listening: at the airport", "10 min")}
<div style="display:flex;gap:3mm;align-items:center"><p style="flex:1;margin:0">Ana, Tom's online student from Brazil, is flying home to São Paulo after a visit to Chicago. Listen to three situations at O'Hare Airport.</p>{img('B', 28, 19)}{img('D', 28, 19)}</div>
{audiocard(["29.1 · SLOW", "29.1 · NATURAL"])}
{sub("A", "Listen and answer the questions.", "3 min", "29.1 · SLOW")}
<ol style="line-height:1.45;font-size:9pt"><li><b>Check-in:</b> How many bags does Ana check? What's her gate? {A("one bag · gate M12", "min-width:35mm")}</li>
<li><b>Security:</b> Number these in the order you hear them: ☐ bag ☐ belt and jacket ☐ bin ☐ jewelry {A("bin 1 · belt and jacket 2 · jewelry 3 · bag 4", "min-width:50mm")}</li>
<li><b>On the plane:</b> What three problems does Ana have? {A("someone is in her seat · no room in the bin · she spills her coffee", "min-width:70mm")}</li></ol>
{sub("B", "Listen again and complete the sentences. The first letter is given.", "5 min", "29.1 · NATURAL")}
<div style="display:flex;gap:3mm;font-size:8.7pt"><div style="flex:1"><b>Check-in</b><ol style="line-height:1.45;margin:0">{gl(g1)}</ol></div><div style="flex:1"><b>Security</b><ol style="line-height:1.45;margin:0">{gl(g2)}</ol></div></div>
<b style="font-size:8.7pt">On the plane</b><ol style="line-height:1.45;margin:0;font-size:8.7pt">{gl(g3)}</ol>""",
    22, """<ol><li>A: pause after each situation to check. <i>Turbulence</i> = when the plane moves suddenly because of the air outside.</li>
<li>B: let the student predict the words first. Read the script aloud together if there is time.</li></ol>""")

    # Page 3
    instr = ["Place your bag on the scale.", "Go through security and make your way to gate M12.", "Step this way, please.", "Take off your belt and your jacket."]
    ann = ["Please fasten your seat belt when we switch on the sign.", "We are about to take off.", "We'll shortly be passing through the cabin with drinks and snacks.", "If you need anything, please ask a flight attendant."]
    rows = "".join(f"<tr><td>{a}</td><td>{c}</td></tr>" for a, c in zip(instr, ann))
    b.page(f"""{sec(3, "Language focus: questions, requests and instructions", "10 min")}
{sub("A", "Study the table. Then choose the correct option.", "5 min")}
<table style="margin:0;font-size:8.6pt"><tr><th style="width:22mm"></th><th>questions</th><th>requests</th><th>responding to requests</th></tr>
<tr><td><b>staff</b></td><td>Where are you flying to today? · Are you checking any bags today? · Did you pack your bag yourself? · Are you wearing any jewelry?</td><td>May I see your passport, please? · Can you open your bag, please? · Could you show me your boarding pass, please?</td><td rowspan="2">Here you are. · OK. · Of course. · Sure.</td></tr>
<tr><td><b>passenger</b></td><td>Are you sure this is your seat?</td><td>Do you have any napkins?</td></tr></table>
<ol style="line-height:1.65;font-size:9pt"><li>When someone makes a request, they {ch(["want you to do something", "need information"], "want you to do something")}. We often use <b>may, can</b> and <b>could</b>.</li>
<li>Can you say no when security staff ask you to open your bag? {A("No. The request is polite, but you have to do it.", "min-width:60mm")}</li>
<li>When someone asks a question, they {ch(["want you to do something", "need information"], "need information")}.</li>
<li>Yes/no questions and requests usually have {ch(["rising", "falling"], "rising")} intonation. Wh- questions (where, how many) have {ch(["rising", "falling"], "falling")} intonation.</li>
<li>We usually {ch(["don't need", "need"], "need")} to say something when we respond to a question or request. If you don't understand, ask the person to repeat it.</li></ol>
{sub("B", "Instructions and announcements. Choose the correct option. Then label the columns.", "5 min")}
<ol style="line-height:1.65;font-size:9pt"><li>Instructions {ch(["suggest what to do", "tell you what you need to do"], "tell you what you need to do")}.</li>
<li>Announcements give instructions or information to {ch(["many people", "one person"], "many people")}.</li>
<li>After an instruction or an announcement, we usually need to {ch(["do something", "say something"], "do something")}.</li></ol>
<table style="margin:0;table-layout:fixed;font-size:8.6pt"><tr><td><b>1</b> {A("instructions", "min-width:25mm")}</td><td><b>2</b> {A("announcements", "min-width:25mm")}</td></tr>{rows}</table>""",
    27, """<ol><li>A: drill the questions and requests with clear intonation; the intonation is a clue to the response the speaker expects.</li>
<li>Requests sound polite (<i>May I see…?</i>), but they are not optional. Compare with the direct <i>Show me your passport.</i></li></ol>""")

    grammar_ref.service_language(b)

    # Page 5
    rf = ["↘", "↗", "↘", "↗", "↘", "↗"]
    rfl = "".join(f"<li>{s} {A(r, 'min-width:10mm;text-align:center')}</li>" for s, r in zip(S293, rf))
    b.page(f"""{sub("C", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>Give me a water.</td><td><b>Could I have some water, please?</b></td><td>a polite request.</td></tr>
<tr><td>What? (to a flight attendant)</td><td><b>Sorry? / Could you repeat that, please?</b></td><td>What? sounds rude.</td></tr>
<tr><td>Here is. (giving your passport)</td><td><b>Here you are.</b></td><td>fixed expression.</td></tr>
<tr><td>I need to take off my belt? </td><td><b>Do I need to take off my belt?</b></td><td>question form with do.</td></tr>
<tr><td>Where is the gate M12?</td><td><b>Where is gate M12?</b></td><td>no the before gate + number.</td></tr>
<tr><td>a-is-le seat /aɪsəl/</td><td><b>aisle seat /aɪl/</b></td><td>silent s.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "4 min")}
{audiocard(["29.2", "29.3"])}
{sub("A", "Listen and repeat. Copy the intonation.", "2 min", "29.2")}
{twocol([f'<li value="{i+1}">{s}</li>' for i, s in enumerate(S292)], 4)}
{sub("B", "Listen. Does the voice go up ↗ or down ↘ at the end? Write the arrow.", "2 min", "29.3")}
<ol style="line-height:1.55">{rfl}</ol>
<p class="small" style="margin:0">Then ask your teacher the questions. Your teacher answers.</p>""",
    27, """<ol><li>A: 1–2 are wh- questions (falling); 3–5 are yes/no questions and a request (rising). 6 <i>Sorry, which gate?</i> is a short wh- question to ask for repetition.</li>
<li>B: exaggerate the intonation at first; students with flat intonation can sound unfriendly or unclear.</li></ol>""")

    # Page 6
    mw = [("___ I see your passport, please?", "May / Can / Could"), ("Are you checking ___ bags today?", "any"), ("Did you pack your bag ___?", "yourself"),
          ("___ your bag on the scale.", "Place"), ("Place your ___ in the bin.", "items"), ("___ this way, please.", "Step"),
          ("___ you open your bag, please?", "Can / Could"), ("Please place ___ bags in the overhead bins.", "your"),
          ("Please fasten your ___ when we switch on the sign.", "seat belt"), ("We'll shortly be passing ___ the cabin with drinks and snacks.", "through")]
    def blank(s, w):
        return s.replace("___", A(w, "min-width:16mm"))
    wb = [("What does <b>step</b> mean in <i>Step this way</i>?", "walk"), ("Which word in the airport sentences means <b>put</b>?", "place"),
          ("<i>Take off your belt</i>: what does <b>take off</b> mean? What's the opposite?", "remove · put on"),
          ("<i>The plane takes off</i>: what does it mean? What's the opposite?", "leave the ground · land"),
          ("<i>We are <b>about to</b> take off. We'll <b>shortly</b> be passing…</i> What do they mean?", "very soon (about to = the next thing)")]
    wbl = "".join(f"<li>{q} {A(a, 'min-width:40mm')}</li>" for q, a in wb)
    b.page(f"""{sec(5, "Practice", "9 min")}
{sub("A", "Complete each sentence with one missing word. Try from memory first.", "5 min")}
<p class="small" style="margin:0"><i>Example: Are you ___ this is your seat? → Are you <b>sure</b> this is your seat?</i></p>
{twocol([f'<li value="{i+1}">{blank(s, w)}</li>' for i, (s, w) in enumerate(mw)], 6)}
{sub("B", "Word builder: airport words. Answer the questions.", "4 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><ol style="flex:1;line-height:1.6;font-size:9pt;margin:0">{wbl}</ol>{img('E', 30, 24)}</div>""",
    22, """<ol><li>A: when you check, ask the student to read each sentence aloud with the correct intonation.</li>
<li>B: <i>place</i> and <i>step</i> are formal words used by staff; in everyday English we say <i>put</i> and <i>come / walk</i>.</li></ol>""")

    # Page 7
    rp1 = [("greet the passenger; ask the destination", "answer"), ("request: passport", "give your passport"), ("ask: check any bags?", "say how many"),
           ("instruction: put the bag on the scale", "do it"), ("security question: did you pack…?", "answer"), ("boarding pass; gate number and boarding time", "ask for repetition; thank the agent")]
    rp2 = [("greet the passenger; request: boarding pass", "show your boarding pass"), ("explain where the seat is (window / aisle)", "find your seat"),
           ("request: bags in the overhead bin", "do it"), ("announcement: seat belts", "fasten your seat belt"),
           ("announcement: drinks and snacks", "order something; make a request (a blanket? napkins?)"), ("help the passenger", "say thank you")]
    def rp(items, a, bb):
        return f'<table style="margin:0;font-size:8.6pt"><tr><th>{a}</th><th>{bb}</th></tr>' + "".join(f"<tr><td>{2*i+1} {x}</td><td>{2*i+2} {y}</td></tr>" for i, (x, y) in enumerate(items)) + "</table>"
    b.page(f"""{sec(6, "Speaking: role-plays", "12 min")}
<div style="display:flex;gap:3mm;align-items:center"><p style="flex:1;margin:0">Plan and act out two conversations with your teacher. Use the language from this unit and natural intonation. Don't write; just look at the plan.</p>{img('F', 32, 19)}</div>
{sub("A", "At check-in. Your teacher is the airline agent; you are the passenger.", "5 min")}
{rp(rp1, "Teacher: airline agent", "You: passenger")}
{sub("B", "On the plane. Your teacher is the flight attendant; you are the passenger.", "5 min")}
{rp(rp2, "Teacher: flight attendant", "You: passenger")}
{sub("C", "Change roles and do it again. This time the passenger doesn't understand something and asks for repetition.", "2 min")}
<p class="small" style="margin:0"><i>Sorry, which gate? · Could you repeat that, please? · Sorry, what time?</i></p>""",
    22, """<ol><li>Model the first two lines to show how the prompts become natural speech: <i>Good morning. Where are you flying to today? — To Miami.</i></li>
<li>C: speak a little fast or quietly on purpose so the student has a real reason to ask for repetition.</li></ol>""")

    # Page 8
    pc = [("A2 Unit 26", "I can describe people's personalities with modifiers."), ("A2 Unit 27", "I can compare people and things with comparatives and superlatives."),
          ("A2 Unit 28", "I can use adverbs in the correct position."), ("A2 Unit 29", "I can check in, go through security and understand announcements on a plane.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    steps = ["You show your passport and say where you're going.", "You answer some questions about your bags, and you check them.",
             "You put your things in a bin so a machine can check that they're safe.", "You may also need to take off your belt and jacket.",
             "You walk through a duty-free area where you can buy things without paying tax.", "You find your departure gate.",
             "You board the plane and find your seat.", "You put your carry-on bag in the overhead bin.", "You fasten your seat belt.", "The plane takes off."]
    import random
    rnd = random.Random(29)
    shuffled = steps[1:]
    rnd.shuffle(shuffled)
    order_items = [steps[0]] + shuffled
    stl = "".join(f'<li>{("<b>1</b> ____" if s == steps[0] else A(str(steps.index(s) + 1), "min-width:7mm;text-align:center"))} {s}</li>' for s in order_items)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Number the steps 1–10 to show what happens when you travel by plane. Number 1 is done for you.</b></p>
<ul style="list-style:none;padding-left:0;line-height:1.55;font-size:9pt">{stl}</ul>
<p style="margin-top:1.5mm"><b>2. My last trip (50–75 words).</b> Write about the last time you traveled by plane, bus or car. Where did you go? Did anything go wrong? Use at least two airport words from this unit.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    20, """<p>Number 1 is given in the SB: the student writes 1 next to the passport sentence. Next class: role-play the opposite situation: arriving in the US (immigration, baggage claim and customs). Review 3 is next.</p>""")

    b.extra("Audio script", f"""
{sub("29.1", "At the airport (slow and natural)")}
<p style="line-height:1.35;font-size:8.6pt">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in S291)}</p>
{sub("29.2", "Repeat: questions and requests")}
<p>{" · ".join(S292)}</p>
{sub("29.3", "Rising or falling?")}
<p>{" · ".join(S293)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 29 - Air travel")
