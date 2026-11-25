# Speak! Progress B1 - Unit 57 "Emergencies" (all English) - lean B1 format
import sys, os, json
_h = os.path.dirname(os.path.abspath(__file__))
for _d in ("/home/claude/speak-audio/engine", os.path.join(_h, "..", "speak-audio", "engine"), os.path.join(_h, "..", "..", "speak-audio", "engine"),
           os.path.join(_h, "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Progress"
import lean
from lean import talk
setup(band="B1 · UNIT 57", audio_json="audio_b1-unit-57.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-57"]
S571 = [l.split(": ", 1) for l in _r["57.1 Three emergency calls"].split("\n")]
S572 = [x.split(": ", 1)[1] for x in _r["57.2 Repeat: there's been, there might be"].split("\n")]




def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'
    def lines(n):
        return '<div class="wline"></div>' * n

    # Page 1 - Warm-up
    cover = cover_html(T, "LEVEL B1 · UNIT 57", "Emergencies", "Calling for help · <b>There's been an accident!</b>",
                       [("YOU CAN", "make an emergency call, report what happened and answer the operator's questions"),
                        ("LANGUAGE", "break-in · trapped · unconscious · squad car · I'd like to report… · there's been / there might be"),
                        ("PRONUNCIATION", "there's been /ðərz bɪn/ · fast, clear numbers and addresses")])
    words = ["ambulance", "break-in", "fire truck", "hurt", "squad car", "trapped", "unconscious", "wildfire"]
    defs = {"ambulance": "a vehicle that paramedics use to take people to the hospital", "break-in": "when someone enters a building or a car illegally, by force",
            "fire truck": "a vehicle that firefighters use", "hurt": "with a physical injury",
            "squad car": "a police car", "trapped": "unable to move or escape from a place",
            "unconscious": "not awake because of an injury or illness", "wildfire": "a fire in nature that can spread very quickly"}
    order = [4, 7, 0, 6, 1, 3, 5, 2]
    kwl = "".join(f'<li>{A(words[i], "min-width:24mm")} <span style="color:#6b7377">= {defs[words[i]]}</span></li>' for i in order)
    b.page(f"""{sec(1, "Warm-up: in an emergency", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["Have you ever called an emergency number? What happened?", "Do you know the emergency numbers in Brazil? And in the US?", "What emergencies are common in your city?"], "START TALKING")}</div></div>
{sub("A", "Key words. Write the words from the box next to their meanings.", "3 min")}
<div class="bank">{" · ".join(words)}</div>
<ol style="font-size:8.6pt;line-height:1.7;margin:0">{kwl}</ol>
{talk(["Have you ever seen a wildfire, a break-in or an accident?", "What would you do if you saw someone unconscious in the street?"], "USE THE WORDS")}""",
    30, """<ol><li>Top box: 3 minutes. Emergency numbers: in the US and Canada, 911 for everything; in Brazil, 190 (police), 192 (ambulance) and 193 (firefighters).</li>
<li>A: 4 minutes with the questions. <i>Squad car</i> is American English (also <i>police car, patrol car, cruiser</i>).</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("three 911 calls from Carol in Orlando: a fire, a break-in, an accident · which emergency? · useful expressions · Talk about it",
                      "there + be in all tenses and with modals: there's been, there was, there'll be, there might be, there must have been, there seems to be", "Choose the correct form · rewrite · Use it (oral)",
                      "there's been (57.2) · emergency workers · role-play: emergency calls · long turn: an emergency you saw", "Carol's message to Ana · present perfect or past? · watch out · writing: an emergency"),
        """The Linguahouse lesson has three emergency calls (a wildfire, a break-in and a car accident), useful expressions, and the present perfect for fresh news (<i>There's been a car accident</i>). The present perfect was already studied, so we kept the calls but rewrote them with Carol (Leda) in Orlando, which makes a real 911 call natural in English, and added a new B1 grammar point: there + be in all tenses and with modals. Story: (1) smoke from her neighbor's garage at 42 Palm Street; the neighbors' car isn't there, but there might be a dog inside; firefighters on their way. (2) Someone broke into Carol's car at the mall (parked at two; sunglasses and a bag with her laptop stolen); an officer in about twenty minutes. (3) An accident on the highway after the airport exit; one driver seems to be unconscious, someone might be trapped; ambulance and fire truck. Operator = Charon. The Linguahouse present perfect practice is kept as a homework review.""",
        """<i>Has an accident</i> / <i>Had a lot of smoke</i> (→ <i>There's been / There was</i>); <i>There will have</i> (→ <i>There will be</i>). Vocabulary: <i>denounce</i> (→ <i>report</i>, a false friend); <i>My car was robbed</i> (→ <i>broken into</i>; things are <i>stolen</i>, people and places are <i>robbed</i>); <i>call to the police</i> (→ <i>call the police</i>).""",
        "Track 57.1 Three emergency calls (natural and slow; Carol and the operator) · Track 57.2 Repeat: there's been, there might be"))

    # Page 2 - Listening
    exp = ["Can you see if anyone is hurt?", "I'd like to report a break-in.", "I want to report a fire.", "Is anyone inside the house?", "Was anything stolen?", "We need an ambulance right away!"]
    gaps = [("1", "Carol", "I want to report a fire."), ("1", "Operator", "Is anyone inside the house?"), ("2", "Carol", "I'd like to report a break-in."),
            ("2", "Operator", "Was anything stolen?"), ("3", "Carol", "We need an ambulance right away!"), ("3", "Operator", "Can you see if anyone is hurt?")]
    gl = "".join(f'<li>Dialogue {d} · {w}: {A(e, "min-width:52mm")}</li>' for d, w, e in gaps)
    b.page(f"""{sec(2, "Listening: three emergency calls", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
<p style="margin:0 0 1mm;font-size:8.8pt">Ana's cousin Carol lives in Orlando, Florida. It's been a crazy week: she calls 911 three times.</p>
{sub("A", "Listen. What is the emergency in each call?", "3 min")}
<p style="margin:0;font-size:8.7pt;line-height:1.7">1 {A("a fire (smoke from a garage)", "min-width:40mm")}<br>2 {A("a break-in (her car)", "min-width:40mm")}<br>3 {A("a car accident on the highway", "min-width:40mm")}</p></div>{img('B', 38, 28)}</div>
{audiocard(["57.1 · NATURAL", "57.1 · SLOW"])}
{sub("B", "Useful expressions. Listen again and complete with the sentences from the box.", "5 min")}
<div class="bank" style="font-size:8.5pt">{" · ".join(exp)}</div>
<ol style="line-height:1.55;font-size:8.6pt;margin:0">{gl}</ol>
<p style="margin:.6mm 0;font-size:8.6pt"><b>Think about it:</b> In call 3, the operator says "Don't move anyone." Why? {A("moving an injured person can make the injury worse; wait for the paramedics", "min-width:20mm")}</p>
{talk(["Which call was the most serious? Why?", "What information does the operator always ask for?", "Would you stay calm in a situation like this?"])}""",
    35, """<ol><li>A: play the natural version; play the slow one if needed.</li>
<li>B: then ask the student to find <i>there</i> + <i>be</i>: <i>There's smoke coming, there might be a dog, there wasn't anything else, There'll be someone there, There's been an accident, there might be someone trapped</i>. They come back on page 3.</li>
<li>The operator always asks <b>what</b>, <b>where</b> and <b>is anyone hurt</b>: practice this order in the role-play on page 5.</li></ol>""")

    # Page 3
    lean.grammar_in_class(b, grammar_ref.there_be)

    # Page 4 - Practice
    pc = [("Help!", ["There's been", "Has been"], "There's been", "an accident!"), ("When I arrived,", ["there was", "had"], "there was", "a lot of smoke."),
          ("Don't worry.", ["There'll be", "There will have"], "There'll be", "someone there soon."), ("Be careful:", ["there might be", "there might to be"], "there might be", "a dog inside."),
          ("", ["There were", "There was"], "There were", "three cars in the accident."), ("The lights are off.", ["There must have been", "There must be had"], "There must have been", "a power cut."),
          ("", ["There seems to be", "It seems to be"], "There seems to be", "a fire in the park."), ("", ["Has there been", "Have been there"], "Has there been", "an accident?")]
    cl = "".join(f"<li>{a + ' ' if a else ''}{ch(o, r)} {z}</li>" for a, o, r, z in pc)
    rw = [("An accident happened on the highway a few minutes ago. (There's been)", "There's been an accident on the highway."),
          ("Maybe someone is in the car. (There might)", "There might be someone in the car."),
          ("I'm sure a problem happened with the electricity. (There must have)", "There must have been a problem with the electricity.")]
    rwl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw)
    use = ["Has there been an emergency in your street or building recently?", "Were there many people at the last event you went to?",
           "Will there be any changes in your life next year?", "Is there anything strange in your street today? What might there be?",
           "Think of the last power cut you had. What must there have been?"]
    b.page(f"""{sec(4, "Practice: there's been, there might be", "10 min")}
{sub("A", "Choose the correct words.", "3 min")}
<ol style="line-height:1.7;font-size:8.6pt;margin:0;columns:2;column-gap:6mm">{cl}</ol>
{sub("B", "Rewrite the sentences with there + be.", "4 min")}
<ol style="line-height:1.45;font-size:8.7pt;margin:0">{rwl}</ol>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    30, """<ol><li>A: 3 minutes. Item 5: <i>were</i> agrees with <i>three cars</i>. In conversation, <i>there's</i> + plural is common, but not in writing.</li>
<li>B: accept <i>There has been</i> / <i>There's been</i>.</li>
<li>Use it: 3 minutes, all oral. Push for the right tense in each answer.</li></ol>""")

    # Page 5 - Speaking
    em = [("a house fire", "a firefighter"), ("a car accident", "a paramedic"), ("a break-in", "a police officer"), ("someone drowning", "a lifeguard"), ("a building collapse", "a rescue worker")]
    eml = "".join(f'<li>{e} → {A(w, "min-width:24mm")}</li>' for e, w in em)
    sit = ["There's a house on fire across your street.", "You're on the highway and you see a car crash.", "You come home and your laptop isn't there. The window is open.",
           "Your car window is broken and your bag is missing.", "Someone has fallen in the street and isn't moving."]
    card = f"""<div class="box" style="margin-top:1mm;font-size:8.2pt">{R("<b>Teacher's card (C):</b> you are the operator. Ask in this order: <i>What's your emergency? · What's the address / Where exactly are you? · Is anyone hurt? · When did it happen? · Can we call you at this number?</i> Then give one instruction: <i>Stay away from… / Don't touch anything. / Don't move him.</i> Change roles after two calls.")}</div>""" if T else ""
    b.page(f"""{sec(5, "Speaking: emergency calls", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE: AN EMERGENCY CALL</h4>
<table style="margin:0;font-size:8.2pt"><tr><th>the caller</th><th>the operator</th><th>instructions</th></tr>
<tr><td><i>I'd like to report… · There's been… · We need an ambulance right away! · I'm on… / in front of… / across from…</i></td><td><i>What's your emergency? · Where exactly are you? · Is anyone hurt? · Was anything stolen? · Can we call you at this number?</i></td><td><i>Stay away from… · Don't move anyone. · Don't touch anything. · Help is on the way.</i></td></tr></table></div>
{audiocard(["57.2"])}
{sub("A", "Listen and repeat. Say there's been as one quick group: /ðərz bɪn/.", "2 min", "57.2")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S572))}</p>
{sub("B", "Who comes? Match the emergency with the emergency worker.", "2 min")}
<ol style="font-size:8.5pt;line-height:1.5;margin:0;columns:2;column-gap:6mm">{eml}</ol>
{sub("C", "Role-play. Choose a situation and call for help. Your teacher is the operator. Invent the details (address, names). Then change roles.", "8 min")}
<ol style="font-size:8.5pt;line-height:1.45;margin:0">{"".join(f"<li>{s}</li>" for s in sit)}</ol>{card}
{sub("D", "Long turn. Tell your teacher about an emergency you saw or heard about. What happened? Who came? What would you do differently?", "3 min")}""",
    30, """<ol><li>B: other answers are possible (for example a paramedic for drowning). C comes from the Linguahouse role-play; insist on a clear address with <i>on / in front of / across from</i>.</li>
<li>D: no real names needed. Last 3 minutes: wrap-up (two corrections, and ask <i>Can you now make an emergency call?</i>).</li></ol>""")

    # Homework
    pc2 = [(["There's been", "It's been"], "There's been"), (["there was", "had"], "there was"), (["there might be", "there might"], "there might be"),
           (["Was", "Were"], "Was"), (["there'll be", "there will have"], "there'll be"), (["there must have been", "there must be"], "there must have been")]
    p = [ch(o, a) for o, a in pc2]
    pp = [("Help! Somebody", "has stolen", "(steal) my wallet!"), ("Yesterday I", "lost", "(lose) my keys at the mall."), ("Last week there", "was", "(be) an accident on my street."),
          ("", "Have you seen", "(you / see) my phone anywhere? I can't find it."), ("Somebody", "broke", "(break) into my car last night.")]
    ppl = "".join(f'<li>{a + " " if a else ""}{A(v, "min-width:24mm")} {z}</li>' for a, v, z in pp)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Carol tells Ana about her crazy week. Choose the correct words.", "")}</div>{img('C', 30, 19)}</div>
<div class="box" style="line-height:1.85;font-size:8.8pt;margin:.5mm 0"><b>Hi Ana!</b> What a week! {p[0]} a fire in my neighbor's garage, a break-in and an accident. On Monday {p[1]} smoke everywhere, and I thought {p[2]} a dog inside. Luckily, the house was empty. {p[3]} anything stolen from my car? Yes, my laptop! The police say {p[4]} more officers at the mall next month. And on the highway, {p[5]} a problem with one of the cars. Everyone is OK now. I need a vacation in São Paulo! Love, Carol</div>
{sub("B", "Review: present perfect or past simple? Complete with the verbs in brackets.", "")}
<ol style="line-height:1.55;font-size:8.6pt;margin:0">{ppl}</ol>
{lean.watch_out([("I want to denounce a robbery.", "I want to report a robbery.", "<i>denounce</i> = criticize strongly in public; to the police you <i>report</i>."), ("My car was robbed.", "My car was broken into. / My bag was stolen.", "things are <i>stolen</i>; people and places are <i>robbed</i>."), ("I called to the police.", "I called the police.", "<i>call</i> somebody: no <i>to</i>.")])}
{lean.writing_task(sub, "Write a post for Danny's blog: an emergency you saw or heard about (real or invented).", "Last year there was…", ["what happened, where and when", "who called for help and who came", "how it ended", "three forms of there + be (there's been, there might be…)", "100–150 words"], "I can make an emergency call, report what happened and answer the operator's questions.")}""",
    25, """<p>Check A and B in 3 minutes at the start of the next class. B comes from the Linguahouse present perfect practice: fresh news (<i>has stolen</i>) vs a finished time (<i>yesterday, last week, last night</i>). Read the writing at home and choose two mistakes to discuss in class.</p>""")

    def scr(lst):
        return "".join(f"<p style='margin:.4mm 0'><b>{n}:</b> {t}</p>" if n != "Narrator" else f"<p style='margin:1mm 0 .3mm'><i>{t}</i></p>" for n, t in lst)
    b.extra("Audio script", f"""
{sub("57.1", "Three emergency calls (natural and slow; Carol and the operator)")}
<div style="line-height:1.28;font-size:8.2pt">{scr(S571)}</div>
{sub("57.2", "Repeat: there's been, there might be")}
<p>{" · ".join(S572)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 57 - Emergencies")
