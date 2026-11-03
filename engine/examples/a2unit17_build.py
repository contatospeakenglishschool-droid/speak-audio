# Speak! Bridge A2 - Unit 17 "Phone calls" (all English, functional) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 17", audio_json="audio_a2-unit-17.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["a2-unit-17"]
def _lines(k):
    return [tuple(x.split(": ", 1)) for x in _r[k].split("\n")]
C1, C2, C3 = _lines("17.1 Call 1"), _lines("17.2 Call 2"), _lines("17.3 Voicemail")
S174 = [x.split(": ", 1)[1] for x in _r["17.4 Repeat phrases"].split("\n")]
NAMES = {"Lucy": "Lucy", "Kate": "Kate", "Receptionist": "Linda", "Paulo": "Paulo"}


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 17", "Phone calls", "Calls and voicemails · <b>informal and formal phone phrases</b>",
                       [("YOU CAN", "make and answer phone calls, take a message and leave a voicemail"),
                        ("LANGUAGE", "Could I speak to Mr. Bennett, please? · Hang on a minute. · I'll pass that on."),
                        ("PRONUNCIATION", "phrasal verbs: pick UP · hang UP · speak UP")])
    g1 = [("Can you speak up?", "I'm at a train station and it's very noisy.", "speak more loudly"), ("You're breaking up!", "We're going through a tunnel.", "your voice is on and off"),
          ("He'll pick it up.", "The phone's ringing.", "answer the phone"), ("Just say sorry and hang up.", "It's a wrong number.", "end the call")]
    g2 = [("I'll put you through.", "Ms. Watkins is available.", "connect the call"), ("I couldn't get through to anyone.", "I called the school ten times.", "make contact"),
          ("Hang on a second.", "You want to talk to my brother? OK.", "wait (informal)"), ("Could you hold on a moment?", "I'll see if the manager is available.", "wait (formal)")]
    def mt(items, opts):
        return "".join(f'<li>{c} <b>{p}</b> {A(m, "min-width:24mm")}</li>' for p, c, m in items)
    b.page(f"""{sec(1, "Warm-up: phone phrasal verbs", "8 min")}
<div style="display:flex;gap:4mm;align-items:flex-start">
<div style="width:44mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo('A')}" style="width:44mm;height:32mm;object-fit:cover;display:block"></div>
<div style="flex:1">{sub("A", "Read the sentences. Write the meaning of the phrasal verbs in bold.", "5 min")}
<div class="bank">answer the phone · end the call · speak more loudly · your voice is on and off</div>
<ol>{mt(g1, 1)}</ol></div></div>
<div class="bank">connect the call · make contact · wait (formal) · wait (informal)</div>
<ol>{mt(g2, 2)}</ol>
{sub("B", "Talk about it.", "3 min")}
<ol><li>When do you <i>not</i> pick up the phone? Do you prefer calls, voice messages or texts?</li><li>Have you had problems getting through to a company on the phone? What happened?</li></ol>""",
    22, """<ol><li>A: phrasal verb = verb + a small word (<i>up, on, through</i>). The meaning changes completely: <i>pick up</i> the phone ≠ <i>pick</i> a fruit.</li>
<li>B: many students prefer voice messages; this unit also practices voicemail.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Phone phrasal verbs</td><td>1</td></tr>
<tr><td>2 Listening</td><td>12 min</td><td>Three calls: informal, formal, voicemail</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>8 min</td><td>Informal and formal phone phrases</td><td>3</td></tr>
<tr><td>+ Language reference</td><td>–</td><td>Phone routines · phrasal verbs · voicemail · numbers</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>5 min</td><td>Phone phrases with polite intonation</td><td>5</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Ten missing words</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Role-plays: an informal call, a formal call, a voicemail</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Call 1: Kate calls Tom; Lucy answers (Kate = Neural2-G, Lucy = Neural2-C). Call 2: Kate calls the Lakeview Hotel (invented) about a wedding cake order; the receptionist Linda is a one-off voice (Studio-O). Call 3: Paulo (Neural2-I) leaves Tom a voicemail from the overnight train from New York to Chicago. Fact: Amtrak's <i>Lake Shore Limited</i> runs overnight between New York and Chicago Union Station, in about 19–20 hours (Amtrak).</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>On the phone, students say <i>I'm Kate</i> ✗ (→ <b>It's Kate / This is Kate</b>) and <i>Who is speaking?</i> ✗ (→ <b>Who's calling, please?</b>). They also use informal phrases in business calls (<i>Wait!</i>) and read numbers in pairs (<i>forty-seven, twenty-nine</i>) instead of one digit at a time.</div>
<div class="box"><h4>AUDIO</h4>Track 17.1 Call 1 (slow and natural) · Track 17.2 Call 2 · Track 17.3 Paulo's voicemail · Track 17.4 Phone phrases</div>""")

    # Page 2
    tf = [("1", "Lucy answers Tom's phone.", "T"), ("1", "Kate leaves a message about Tom's jacket.", "T"), ("2", "Mr. Bennett is on vacation.", "F: he's in a meeting until 3:00."),
          ("2", "Kate wants Mr. Bennett to email her.", "T"), ("3", "Paulo is going to arrive at ten.", "F: at eleven."), ("3", "Paulo wants Tom to text him.", "T")]
    tfl = [f'<li value="{i+1}"><b>Call {c}:</b> {s} <b>T / F</b> {R(a)}</li>' for i, (c, s, a) in enumerate(tf)]
    gp = [("Hang", "on", "a minute, I'll get him. (call 1)"), ("Please hold", "on", "a moment. (call 2)"), ("I'll put you", "through", ". (call 2)"),
          ("Sorry, can you speak", "up", ", please? (call 2)"), ("You're not picking", "up", ". (call 3)"), ("I can't get", "through", "to you. (call 3)"),
          ("I'm probably breaking", "up", ". (call 3)")]
    gpl = [f'<li value="{i+1}">{a} {A(w, "min-width:14mm")}{z}</li>' for i, (a, w, z) in enumerate(gp)]
    b.page(f"""{sec(2, "Listening: three phone calls", "12 min")}
<div style="display:flex;gap:3mm;align-items:center">
<p style="flex:1;margin:0">Call 1: Kate calls Tom. Call 2: Kate calls a hotel about a wedding cake. Call 3: Paulo leaves Tom a voicemail from the train.</p>
<div style="width:30mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo('B')}" style="width:30mm;height:20mm;object-fit:cover;display:block"></div>
<div style="width:30mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo('C')}" style="width:30mm;height:20mm;object-fit:cover;display:block"></div></div>
{audiocard(["17.1 · SLOW", "17.1 · NATURAL", "17.2", "17.3"])}
{sub("A", "Listen to the three calls. True (T) or false (F)?", "5 min")}
{twocol(tfl, 3)}
<p class="small">Which call is the most formal? Why? {R("Call 2: a business call between people who don't know each other.")}</p>
{sub("B", "Listen again. Complete with on, up or through.", "5 min")}
{twocol(gpl, 4)}""",
    22, """<p>A: play each call once; in call 2, write the order number on the board after listening (4-7-2-9-1). B: try from memory first (warm-up), then listen. Full scripts: audio scripts page. Fact: Amtrak's Lake Shore Limited (see the overview).</p>""")

    # Page 3
    rows = [("answer the phone", "Hello? · Tom's phone.", "Hello, Lakeview Hotel. How can I help you?"),
            ("ask for someone", "1", "Could I speak to Mr. Bennett, please?"), ("say who you are", "It's Kate.", "Linda 2 ___ · It's Kate Miller."),
            ("ask who is calling", "Who's this?", "3"), ("ask someone to wait", "Hang on a minute.", "Please hold on a moment."),
            ("connect the call", "4", "I'll put you through."), ("the person isn't there", "5", "I'm afraid Mr. Bennett isn't available."),
            ("leave a message", "Can you tell him that…?", "6"), ("promise to give the message", "7", "I'll make sure he gets the message."),
            ("check understanding", "8", "Would you like me to say that again?")]
    keys = {"1": "Is Tom there?", "2": "speaking", "3": "Who's calling, please?", "4": "I'll get him.", "5": "Sorry, he can't come to the phone.",
            "6": "I'd like to leave a message, please.", "7": "I'll pass that on.", "8": "Did you get that?"}
    def cell(x):
        if x in keys:
            return f"{x} {A(keys[x], 'min-width:34mm')}"
        if "2 ___" in x:
            return x.replace("2 ___", "2 " + A(keys["2"], "min-width:14mm"))
        return x
    tr = "".join(f"<tr><td><b>{s}</b></td><td>{cell(i)}</td><td>{cell(f)}</td></tr>" for s, i, f in rows)
    b.page(f"""{sec(3, "Language focus: informal and formal calls", "8 min")}
{sub("A", "Complete the table with phrases from calls 1 and 2. Look at the audio scripts if you need help.", "6 min")}
<table style="table-layout:fixed;margin-top:0;font-size:8.8pt"><tr><th style="width:32mm">step</th><th>informal (friends)</th><th>formal (business)</th></tr>{tr}</table>
{sub("B", "Informal (I) or formal (F)?", "2 min")}
<ol style="columns:2"><li>Hang on a minute. {R("I")}</li><li>Please hold on. {R("F")}</li><li>I'm afraid she isn't available. {R("F")}</li><li>Who's this? {R("I")}</li><li>I'll pass that on. {R("I")}</li><li>I'll put you through. {R("F")}</li></ol>
<div class="box sand"><h4>RULE</h4>On the phone, say <b>It's Kate</b> or <b>This is Kate</b>, not <s>I'm Kate</s>. Ask <b>Who's calling, please?</b>, not <s>Who is speaking?</s> More on the next page: <b>Language reference</b>.</div>""",
    24, """<ol><li>A: let the student use the audio scripts page (TB) or play the calls again. Drill each phrase: these routines must sound natural.</li>
<li>B: some phrases work in both styles: <i>Can I take a message?</i></li></ol>""")

    grammar_ref.phone_calls(b)

    # Page 5
    b.page(f"""{sub("C", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>Hello, I'm Kate.</td><td><b>Hello, it's Kate. / This is Kate.</b></td><td>phone routine.</td></tr>
<tr><td>Who is speaking?</td><td><b>Who's calling, please?</b></td><td>ask the caller.</td></tr>
<tr><td>Can you talk more high?</td><td><b>Can you speak up?</b></td><td>phrasal verb.</td></tr>
<tr><td>Wait. (to a customer)</td><td><b>Please hold on a moment.</b></td><td>formal.</td></tr>
<tr><td>I want to let a message.</td><td><b>I'd like to leave a message.</b></td><td>leave a message.</td></tr>
<tr><td>He turned off on me!</td><td><b>He hung up on me!</b></td><td>end the call = hang up.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "5 min")}
{audiocard(["17.4"])}
{sub("A", "Phone phrases. Listen and repeat. Copy the polite, friendly intonation.", "3 min", "17.4")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S174)}</div>
{sub("B", "Stress in phrasal verbs. Underline the stressed word.", "2 min")}
<p>pick up · hang on · speak up · put through · call back · break up</p>
<p class="small">{R("The small word is stressed: pick UP · hang ON · speak UP · put THROUGH · call BACK · break UP")}</p>
<div class="box" style="margin-top:1mm"><h4>SOUND POLITE</h4>A flat voice can sound rude on the phone. Start high and go down: <i>Could I speak to Mr. Bennett, please?</i> ↘ · <i>I'm afraid</i> = /aɪm əˈfreɪd/ (polite way to give bad news).</div>""",
    24, """<ol><li>4A: the student repeats with their back to you, like a real call.</li>
<li>4B: in phrasal verbs, the particle usually carries the stress.</li></ol>""")

    # Page 6
    p1 = [("Tom", "Hello?"), ("Kate", "Hi, Tom. ___ is Kate.", "This"), ("Tom", "Hi, Kate! Hang ___ a minute. I'm going to another room. … OK.", "on"),
          ("Kate", "I called and left a ___ about your jacket.", "message"), ("Tom", "Lucy passed it on to me. Thanks!"),
          ("Kate", "Can you ___ up? I didn't hear that.", "speak"), ("Tom", "I said thanks! Can you ___ me back in ten minutes? Someone's at the door.", "call")]
    p2 = [("Receptionist", "Hello, Sweet Kate Bakery. How ___ I help you?", "can"), ("Mr. Bennett", "Hello. Could I speak ___ Kate Miller, please?", "to"),
          ("Receptionist", "Who's calling, please?"), ("Mr. Bennett", "___ Mr. Bennett, from the Lakeview Hotel.", "It's"),
          ("Receptionist", "I'll put ___ through.", "you"), ("Kate", "Hello? Kate ___.", "speaking")]
    def dlg(rows):
        out = []
        for r in rows:
            n, t = r[0], r[1]
            if len(r) > 2:
                for w in r[2].split("; "):
                    t = t.replace("___", A(w, "min-width:12mm"), 1)
            out.append(f"<tr><td style='width:22mm'><b>{n}</b></td><td>{t}</td></tr>")
        return "".join(out)
    b.page(f"""{sec(5, "Practice", "8 min")}
{sub("A", "Complete the two calls with the missing words. Then read them aloud with your teacher.", "8 min")}
<div class="bank">call · can · It's · message · on · speak · speaking · This · to · you</div>
<p style="margin:1mm 0"><b>Call 1</b> (informal)</p>
<table style="table-layout:fixed;margin-top:0;font-size:9pt">{dlg(p1)}</table>
<p style="margin:2mm 0 1mm"><b>Call 2</b> (formal)</p>
<table style="table-layout:fixed;margin-top:0;font-size:9pt">{dlg(p2)}</table>
<p class="small">Mr. Bennett: <i>Hello, this is Mr. Bennett. I'm returning your call. Your order number is correct!</i></p>""",
    22, """<ol><li>A: first try without the box (cover it), then use it. Read the calls aloud twice and change roles.</li>
<li><i>I'm returning your call</i> = I'm calling you back.</li></ol>""")

    # Page 7
    vm = ["the name of the person you're calling", "your name", "why you're calling", "details (time, place, number)", "ask for confirmation", "close the call"]
    vmr = "".join(f"<tr><td>{x}</td><td style='height:5.5mm'></td><td></td></tr>" for x in vm)
    b.page(f"""{sec(6, "Speaking: role-plays", "12 min")}
{sub("A", "Informal call. Call your friend's home. Your teacher answers.", "4 min")}
<p class="small" style="margin:.5mm 0">Your teacher answers → you say who you are and ask for your friend → your friend isn't there → leave a message (a party on Saturday at 8) → check your teacher got it → close the call.</p>
{sub("B", "Formal call. Now you are the receptionist at a hotel in Chicago. Your teacher calls.", "4 min")}
<p class="small" style="margin:.5mm 0">Answer with the hotel's name → ask who is calling → ask the caller to wait → the manager isn't available until 4:00 → take a message → repeat the number to check → promise to give the message.</p>
{sub("C", "Voicemail. Plan a message for a friend. Then leave it for your teacher. Your teacher takes notes.", "4 min")}
<table style="table-layout:fixed;margin-top:1mm;font-size:8.8pt"><tr><th></th><th>my voicemail</th><th>my teacher's voicemail</th></tr>{vmr}</table>""",
    26, """<ol><li>A–B: sit back to back. Correct style mistakes (formal vs informal) after each call. In B, give a phone or order number one digit at a time.</li>
<li>C: your voicemail: "Hi, it's (your name). I'm calling about our class next week. Can we start at 7:30 instead of 7:00? Text me to confirm."</li></ol>""")

    # Page 8
    pc = [("A2 Unit 13", "I can explain causes and effects with zero and first conditionals."), ("A2 Unit 14", "I can join ideas with and, but, so, because and although."),
          ("A2 Unit 15", "I can put ideas in order and talk about changing my mind."), ("A2 Unit 16", "I can define people, things and places with who, that and where."),
          ("A2 Unit 17", "I can make phone calls, take a message and leave a voicemail.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Ellen", "Hello, City Coffee. 1", "Ellen speaking."), ("Paulo", "Hi, Ellen. Is Tom there? He's not picking up his cell phone."),
          ("Ellen", "2 … Sorry, he isn't here yet. 3", "Hang on a minute. ; Can I take a message?"), ("Paulo", "Yes, please. Can you tell him that my train is late? I'll be there at eleven."),
          ("Ellen", "4 You're breaking up.", "Sorry, can you say that again?"), ("Paulo", "My train is late. I'll be there at eleven. 5", "Did you get that?"),
          ("Ellen", "Yes. 6", "I'll pass that on."), ("Paulo", "Thanks. Bye!")]
    def hwrow(r):
        n, t = r[0], r[1]
        if len(r) > 2:
            ans = [a.strip() for a in r[2].split(";")]
            it = iter(ans)
            t = " ".join(f"{w} {A(next(it), 'min-width:30mm')}" if w.isdigit() else w for w in t.split(" "))
        return f"<tr><td style='width:16mm'><b>{n}</b></td><td>{t}</td></tr>"
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Paulo calls City Coffee, where Lucy works on weekends. Write the missing phrases (1–6).</b></p>
<table style="table-layout:fixed;margin-top:0;font-size:9pt">{"".join(hwrow(r) for r in hw)}</table>
<p style="margin-top:2mm"><b>2. A voicemail.</b> Write a voicemail for a friend (40–60 words). Say why you're calling, give details, and ask for confirmation. Then record it on your phone and send it to your teacher!</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>1: other answers are possible (<i>This is Ellen.</i> · <i>I'll get him.</i> · <i>I'll make sure he gets the message.</i>). Next class: listen to the student's recorded voicemail and give feedback on intonation.</p>""")

    def scr(lines):
        return "<br>".join(f"<b>{NAMES[n]}:</b> {t}" for n, t in lines)
    b.extra("Audio scripts", f"""
{sub("17.1", "Call 1: Kate calls Tom (slow and natural)")}
<p style="line-height:1.4">{scr(C1)}</p>
{sub("17.2", "Call 2: Kate calls the Lakeview Hotel")}
<p style="line-height:1.4">{scr(C2)}</p>
{sub("17.3", "Call 3: Paulo's voicemail")}
<p style="line-height:1.4">{scr(C3)}</p>
{sub("17.4", "Phone phrases")}
<p>{" · ".join(S174)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 17 - Phone calls")
