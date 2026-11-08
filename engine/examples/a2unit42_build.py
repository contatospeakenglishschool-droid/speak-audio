# Speak! Bridge A2 - Unit 42 "Ask the pharmacist" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 42", audio_json="audio_a2-unit-42.json", img_dir="img")

PHOTOS = [("A", "pills", "pills"), ("B", "a bandage", "bandage"), ("C", "ointment", "ointment"), ("D", "sunscreen", "sunscreen"),
          ("E", "a thermometer", "thermometer"), ("F", "cough syrup", "cough syrup")]
_r = json.load(open("roteiro.json"))["units"]["a2-unit-42"]
S421 = [x.split(": ", 1) for x in _r["42.1 At the pharmacy"].split("\n")]
S422 = [x.split(": ", 1)[1] for x in _r["42.2 Repeat: build the sentence"].split("\n")]
S423 = [x.split(". ", 1)[1] for x in [y.split(": ", 1)[1] for y in _r["42.3 Can or can't?"].split("\n")]]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 42", "Ask the pharmacist", "At the pharmacy · <b>advice and instructions</b>",
                       [("YOU CAN", "ask for help at a pharmacy, understand advice and instructions, and check you understand"),
                        ("LANGUAGE", "You should… · It's a good idea to… · I recommend… · You have to… · You can't… · It's important that you…"),
                        ("PRONUNCIATION", "building long sentences · can /kən/ or can't /kænt/")])
    it = [("insect repellent", "to prevent mosquito bites"), ("pills", "painkillers for a headache"), ("eye drops", "for dry or sore eyes"), ("a bandage", "for a small cut"),
          ("ointment", "for a skin rash or allergy"), ("sunscreen", "to protect your skin outside"), ("a thermometer", "to check if you have a fever"), ("cough syrup", "for a cough")]
    rs = sorted(r for _, r in it)
    lt = "abcdefgh"
    itl = "".join(f"<li>{w} {A(lt[rs.index(r)], 'min-width:6mm;text-align:center')}</li>" for w, r in it)
    rsl = "".join(f"<li>{r}</li>" for r in rs)
    b.page(f"""{sec(1, "Warm-up: at the pharmacy", "8 min")}
<div style="display:flex;gap:2mm;margin-bottom:1mm">{"".join(img(l, 28, 20) for l in "ABCDEF")}</div>
{sub("A", "Match the things you can buy at a pharmacy (1–8) with the reasons (a–h).", "4 min")}
<div style="display:flex;gap:4mm;font-size:9pt"><ol style="flex:.8;line-height:1.5;margin:0">{itl}</ol><ol type="a" style="flex:1.2;line-height:1.5;margin:0">{rsl}</ol></div>
{sub("B", "Which things sometimes need a prescription (a paper from a doctor)? In Brazil, what can you buy without one?", "4 min")}""",
    27, """<ol><li>A: drill <i>cough</i> /kɔːf/, <i>thermometer</i> /θərˈmɑːmɪtər/. In the US, people often say <i>a Band-Aid</i> (a brand name) for a small bandage. <i>Painkillers</i> = medicine for pain.</li>
<li>B: eye drops, cough medicine, painkillers and skin creams sometimes need a prescription. In US drugstores, many medicines are sold "over the counter".</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Things you buy at a pharmacy and why</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>A pharmacist and three customers (one of them Lucy, one Priya)</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Advice and instructions</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>should, it's a good idea to, I recommend · must, have to, need to, can't, it's important that</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>4 min</td><td>Build the sentence · can or can't?</td><td>5</td></tr>
<tr><td>5 Practice</td><td>9 min</td><td>Same meaning, different words · health expressions</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Pharmacy role-plays and checking you understand</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>At a Chicago pharmacy, a pharmacist (Chirp3-HD-Charon) helps three customers: a mother whose son has a fever and a cough (Studio-O), Lucy (Neural2-C), who's going to an outdoor music festival and needs sunscreen and insect repellent, and Priya (Chirp3-HD-Kore), a medical student who studies on her laptop a lot and gets a refill of her eye drops. The pharmacy, prices and products are invented.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students put <i>to</i> after modals (<i>You must to take, You should to rest</i>), say <i>I recommend you this</i>, and don't hear the difference between <i>can</i> and <i>can't</i>, which is dangerous with medical instructions.</div>
<div class="box"><h4>AUDIO</h4>Track 42.1 At the pharmacy (slow and natural) · Track 42.2 Repeat: build the sentence · Track 42.3 Can or can't?</div>""")

    # Page 2
    grid = [("Dialogue 1", "her son is sick", "a thermometer and cough syrup", "pay at the register at the front"),
            ("Dialogue 2", "going to a music festival", "sunscreen and insect repellent", "pay here, by card"),
            ("Dialogue 3", "dry eyes", "a prescription refill", "nothing to pay")]
    gt = "".join(f"<tr><td><b>{d}</b></td><td>{A(a, 'min-width:30mm')}</td><td>{A(b_, 'min-width:36mm')}</td><td>{A(c, 'min-width:30mm')}</td></tr>" for d, a, b_, c in grid)
    tf = [("The pharmacist says the mother should check her son's temperature regularly.", "T"), ("She should call the doctor when she gets home.", "F: only if the fever goes very high or lasts more than two days."),
          ("Lucy has to put on sunscreen once a day.", "F: every couple of hours"), ("The insect repellent is cheap.", "F: it's more expensive than the supermarket stuff."),
          ("Priya has used these eye drops before.", "T: it's a refill."), ("The pharmacist tells Priya something new about the computer.", "F: she already knows.")]
    tfl = [f'<li value="{i+1}">{s} <b>T / F</b> {A(a, "min-width:12mm")}</li>' for i, (s, a) in enumerate(tf)]
    b.page(f"""{sec(2, "Listening: at the pharmacy", "10 min")}
<div style="display:flex;gap:2.5mm;align-items:center"><p style="flex:1;margin:0">A pharmacist in Chicago talks to three customers. The second is Lucy, and the third is Priya, her roommate.</p>{img('G', 26, 18)}{img('H', 26, 18)}</div>
{audiocard(["42.1 · SLOW", "42.1 · NATURAL"])}
{sub("A", "Listen. Complete the table for each dialogue: the problem, what they get, and how they pay.", "4 min", "42.1 · SLOW")}
<table style="margin:0;font-size:8.8pt"><tr><th style="width:18mm"></th><th>the problem</th><th>what they get</th><th>paying</th></tr>{gt}</table>
{sub("B", "Listen again. True (T) or false (F)?", "4 min", "42.1 · NATURAL")}
<ol style="font-size:8.8pt;line-height:1.45;margin:0">{"".join(tfl)}</ol>
{sub("C", "What do these words mean: side effects, in stock, insurance, a refill?", "2 min")}
<p class="small" style="margin:0">{R("side effects: problems some medicine can cause · in stock: in the store, ready to sell · insurance: a company pays your medical costs · a refill: more of the same medicine on the same prescription") if T else ""}</p>""",
    27, """<ol><li>A: stop after each dialogue to check. Dialogue 2: "Just tap your card on the machine." Dialogue 3: the insurance pays.</li>
<li>C: in the US, most people have health insurance through work or a government program; pharmacies ask for it with a prescription.</li></ol>""")

    # Page 3
    ai = [("You <b>should check</b> his temperature regularly.", "A"), ("If his fever goes very high, you <b>need to call</b> the doctor.", "I"), ("<b>I recommend</b> this sunscreen.", "A"),
          ("You <b>have to remember</b> to put more on every couple of hours.", "I"), ("With this condition, <b>it's important that you limit</b> your time on the computer.", "I"), ("<b>It's also a good idea to do</b> some eye exercises every day.", "A")]
    ail = "".join(f"<li>{s} {A(a, 'min-width:7mm;text-align:center')}</li>" for s, a in ai)
    b.page(f"""{sec(3, "Language focus: advice and instructions", "10 min")}
<div class="box" style="margin-top:0;font-size:9pt"><b>Advice</b> = it's a good idea to do (or not do) something. <b>Instructions</b> = it's necessary to do (or not do) something.</div>
{sub("A", "Read the sentences from the pharmacy. Is each phrase in bold advice (A) or an instruction (I)?", "3 min")}
<ol style="line-height:1.55;font-size:9pt;margin:0">{ail}</ol>
{sub("B", "Look at A again and answer.", "4 min")}
<ol style="margin:0;line-height:1.7"><li>Which phrases use <i>to</i> + base form? {A("need to call, have to remember, a good idea to do", "min-width:50mm")}</li>
<li>What comes after <i>It's important that</i>? {ch(["a base form", "subject + verb"], "subject + verb")}</li>
<li>What comes after <i>recommend</i> in sentence 3? {ch(["a noun", "to + verb"], "a noun")}</li></ol>
{sub("C", "Two more instructions. Which phrase in A has the same grammar as must and can't?", "3 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">You <b>must take</b> this medicine ten minutes before meals. · You <b>can't drive</b> while you're taking this medicine.</div>
<p style="margin:.5mm 0">{A("should (and shouldn't): modal + base form, no to", "min-width:70mm")}</p>
<div class="box sand"><h4>RULE</h4><b>Advice:</b> should + base form · it's a good idea to + base form · I recommend + noun / (that) you + base form. <b>Instructions:</b> must / have to / need to + base form · can't + base form · it's important that + subject + verb. No <i>to</i> after <i>should, must, can't</i>. More on the next page: <b>Grammar reference</b>.</div>""",
    20, """<ol><li>A clause = subject + verb (<i>you limit</i>). <i>I recommend that you…</i> uses the same pattern.</li>
<li>Drill with a build-up chain (Pronunciation lab, 42.2).</li></ol>""")

    grammar_ref.advice_instructions(b)

    # Page 5
    cc = ["can", "can't", "can't", "can", "can", "can't"]
    ccl = "".join(f"<li>{A(c, 'min-width:12mm;text-align:center')}</li>" for c in cc)
    b.page(f"""{sub("D", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>You must to take one pill.</td><td><b>You must take one pill.</b></td><td>no to after must.</td></tr>
<tr><td>You should to rest.</td><td><b>You should rest.</b></td><td>no to after should.</td></tr>
<tr><td>I recommend you this cream.</td><td><b>I recommend this cream.</b></td><td>recommend + noun.</td></tr>
<tr><td>It's important you must sleep.</td><td><b>It's important that you sleep.</b></td><td>that + subject + verb.</td></tr>
<tr><td>She musts take it with food.</td><td><b>She must take it with food.</b></td><td>no -s on modals.</td></tr>
<tr><td>I didn't understand. Repeat!</td><td><b>Sorry, could you repeat that?</b></td><td>polite request.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "4 min")}
{audiocard(["42.2", "42.3"])}
{sub("A", "Listen and repeat. Build the sentence step by step.", "2 min", "42.2")}
{twocol([f'<li value="{i+1}">{s}</li>' for i, s in enumerate(S422)], 4)}
{sub("B", "Listen to six instructions. Do you hear can or can't? Write it.", "2 min", "42.3")}
<ol style="line-height:1.5;column-count:3;column-gap:5mm">{ccl}</ol>
<p class="small" style="margin:.5mm 0">can = short and weak: /kən/ · can't = long and stressed: /kænt/ (the t is often silent)</p>""",
    31, """<ol><li>A: the build-up chain helps the student say long sentences with natural rhythm; do it with other sentences from page 3 too.</li>
<li>B: script: 1 You can take it with food. 2 You can't drive after you take this. 3 You can't drink alcohol with this medicine. 4 You can pay at the front. 5 You can buy it without a prescription. 6 You can't give this to children. In American English the final t of can't is often not heard: listen for the long, stressed vowel.</li></ol>""")

    # Page 6
    tr = [("If you're worried about mosquitoes, you should wear long sleeves. (idea)", "If you're worried about mosquitoes, ___ long sleeves.", "it's a good idea to wear"),
          ("It's not a good idea to spend a lot of time near water. (shouldn't)", "___ a lot of time near water.", "You shouldn't spend"),
          ("You should buy two bottles of sunscreen. (recommend)", "___ two bottles of sunscreen.", "I recommend that you buy"),
          ("You must call the doctor if your rash gets worse. (have)", "___ the doctor if your rash gets worse.", "You have to call"),
          ("You can't forget to take your painkillers. (important)", "___ to take your painkillers.", "It's important that you remember"),
          ("This is the best thermometer on the market. (recommend)", "___.", "I recommend this thermometer"),
          ("It's important that you read the instructions carefully. (need)", "___ the instructions carefully.", "You need to read")]
    trl = "".join(f"<li>{a}<br>{c.replace('___', A(r, 'min-width:44mm'))}</li>" for a, c, r in tr)
    hx = [("I caught a cold last week, and", "I missed a few days of work."), ("I'm feeling a bit under the weather,", "so I think I'll go home early."),
          ("If you don't feel better soon,", "you need to go for a checkup."), ("You'll feel better tomorrow if", "you have an early night."),
          ("We're sorry you're sick, and", "we hope you get well soon."), ("You're just going to have to", "take it easy for a few days.")]
    he = sorted(e for _, e in hx)
    hxl = "".join(f"<li>{s} {A('abcdef'[he.index(e)], 'min-width:6mm;text-align:center')}</li>" for s, e in hx)
    hel = "".join(f"<li>{e}</li>" for e in he)
    b.page(f"""{sec(5, "Practice", "9 min")}
{sub("A", "Complete the second sentence so it means the same as the first. Use the word in brackets.", "5 min")}
<ol style="line-height:1.45;font-size:8.8pt;margin:0">{trl}</ol>
{sub("B", "Word builder: health expressions. Match the halves.", "4 min")}
<div style="display:flex;gap:4mm;font-size:8.8pt"><ol style="flex:1;line-height:1.5;margin:0">{hxl}</ol><ol type="a" style="flex:1;line-height:1.5;margin:0">{hel}</ol></div>""",
    26, """<ol><li>A: sentence transformations like these are common in exams. In 5, <i>It's important that you don't forget</i> is also correct.</li>
<li>B: <i>under the weather</i> = a little sick; <i>take it easy</i> = rest; <i>have an early night</i> = go to bed early; <i>a checkup</i> = a general visit to the doctor.</li></ol>""")

    # Page 7
    rp1 = [("Pharmacist", "greet the customer"), ("Customer", "ask for painkillers"), ("Pharmacist", "taken them before?"), ("Customer", "yes"),
           ("Pharmacist", "any side effects?"), ("Customer", "answer"), ("Pharmacist", "check: in stock"), ("Customer", "ask: take with meals?"),
           ("Pharmacist", "answer with an instruction"), ("Customer", "ask where to pay"), ("Pharmacist", "pay at the front"), ("Customer", "thank")]
    rp2 = [("Pharmacist", "greet the customer"), ("Customer", "prescription for a skin rash"), ("Pharmacist", "used it before?"), ("Customer", "ask for instructions"),
           ("Pharmacist", "give two instructions and one piece of advice"), ("Customer", "ask a question about the ointment"), ("Pharmacist", "answer"), ("Customer", "ask for bandages"),
           ("Pharmacist", "not in stock: suggest another store"), ("Customer", "ask: does insurance pay?"), ("Pharmacist", "answer"), ("Customer", "thank")]
    def rp(lst):
        return "".join(f"<tr><td style='width:22mm'><b>{i+1} {w}</b></td><td>{t}</td></tr>" for i, (w, t) in enumerate(lst))
    b.page(f"""{sec(6, "Speaking: pharmacy role-plays", "12 min")}
<div class="two"><div><b>Role-play 1</b><table style="margin:0;font-size:8.4pt">{rp(rp1)}</table></div><div><b>Role-play 2</b><table style="margin:0;font-size:8.4pt">{rp(rp2)}</table></div></div>
{sub("A", "Role-play 1: your teacher is the pharmacist and you are the customer. Then change roles.", "5 min")}
{sub("B", "Role-play 2: you are the pharmacist. Use advice and instructions.", "4 min")}
<div class="box sand" style="font-size:9pt"><h4>CHECK THAT YOU UNDERSTAND</h4><i>I'm sorry, could you say that again? · Could you repeat that, please? · So, let me check: I have to take two pills now and two more before bed?</i></div>
{sub("C", "Do it again. This time, the customer doesn't understand something and asks the pharmacist to repeat or checks.", "3 min")}""",
    28, """<ol><li>Model the first two lines: <i>Good morning. How can I help you? / Hi. I need some painkillers for a headache.</i> As the pharmacist, use <i>should, have to, can't, it's important that</i>.</li>
<li>C: speak a little fast on purpose so the student needs to ask you to repeat. This is the most useful real-life skill of the lesson.</li></ol>""")

    # Page 8
    pc = [("A2 Unit 38", "I can use a/an, the and no article correctly."), ("A2 Unit 39", "I can put nouns together: a coffee cup, Leo's ideas, the end of the story."),
          ("A2 Unit 41", "I can talk about quantities with some, any, much, many, enough and plenty of."), ("A2 Unit 42", "I can understand and give advice and instructions at a pharmacy.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    def x(w):
        return R(f"<s>{w}</s>") if T else w
    hwd = f"""<div class="msg" style="max-width:none;padding:2mm 3mm;font-size:8.8pt;line-height:1.55;background:#fff;border:.8pt solid #c9dfe3">
<b>Pharmacist:</b> Hello. What can I do for you?<br><b>Customer:</b> Hi. My neighbor isn't feeling well, and she asked me to pick up her prescription. Her name is Shirley Jeffrey.<br>
<b>Pharmacist:</b> Right, I have her pills here. You {x("are")} have to explain something to her. Her usual medicine isn't in {x("the")} stock, so the doctor changed her prescription. She must {x("to")} take one pill three times a day, not two pills twice a day.<br>
<b>Customer:</b> Are the instructions on the box?<br><b>Pharmacist:</b> Yes, but it's important that you {x("must")} tell her. She can't {x("to")} take the new pills like the old ones. If she has any questions, she should {x("have")} call the doctor.<br>
<b>Customer:</b> I'll tell her. I also need some eye drops for my allergies.<br><b>Pharmacist:</b> I recommend {x("it")} these. But if you get any side effects {x("things")} like headaches, then you {x("won't")} shouldn't use them anymore. It's {x("like")} a good idea to try another brand then.</div>"""
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p style="margin:.5mm 0"><b>1. The pharmacist's sentences have 10 extra words. Cross them out.</b></p>
{hwd}
<p style="margin-top:1.5mm"><b>2. Advice for a friend (50–75 words).</b> A friend is going to the beach in Brazil for a week. Write a message with two pieces of advice and two instructions about health and the sun.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Extra words: are, the, to, must, to, have, it, things, won't, like. Next class: the student reads the message aloud; you ask <i>Why should I…? Do I have to…?</i></p>""")

    b.extra("Audio script", f"""
{sub("42.1", "At the pharmacy (slow and natural)")}
<p style="line-height:1.35;font-size:8.8pt">{"<br>".join(f"<b>{n}:</b> {t}" if n != "Narrator" else f"<i>{t}</i>" for n, t in S421)}</p>
{sub("42.2", "Repeat: build the sentence")}
<p>{" · ".join(S422)}</p>
{sub("42.3", "Can or can't? (3-second pause)")}
<p>{" · ".join(S423)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 42 - Ask the pharmacist")
