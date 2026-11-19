# Speak! Progress B1 - Unit 28 "At the hotel" (all English) - lean B1 format
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
setup(band="B1 · UNIT 28", audio_json="audio_b1-unit-28.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-28"]
S281 = [l.replace("three-oh-four", "304").replace("seven to ten thirty", "7 to 10:30") for l in _r["28.1 Checking in and checking out"].split("\n")]
S282 = [x.split(": ", 1)[1] for x in _r["28.2 Repeat: polite requests"].split("\n")]


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
    cover = cover_html(T, "LEVEL B1 · UNIT 28", "At the hotel", "Danny in Buenos Aires · <b>Would you mind…? Do you mind if I…?</b>",
                       [("YOU CAN", "check in, ask for services, solve a problem with the bill and check out politely"),
                        ("LANGUAGE", "complimentary · en-suite · housekeeper · Would you mind telling me…? · Would it be possible to…?"),
                        ("PRONUNCIATION", "polite intonation in requests")])
    kw = [("given for free", "complimentary"), ("(a bathroom) joined to a bedroom, only for that room", "en-suite"),
          ("a person who cleans and tidies the rooms", "housekeeper"), ("a person who helps guests with information, tickets and tours", "concierge"),
          ("features or services that make a place comfortable", "amenities"), ("(a vacation) with all meals and drinks in one price", "all-inclusive")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:21mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Warm-up: a good hotel", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["How often do you stay in hotels? Why?", "Order these from 1 to 5 for you: a good view, room service, friendly staff, fast Wi-Fi, a quiet room.", "What's the difference between a double room and a twin room?"], "START TALKING")}</div></div>
{sub("A", "Key words. Write the words from the box next to the definitions.", "3 min")}
<div class="bank">all-inclusive · amenities · complimentary · concierge · en-suite · housekeeper</div>
<div style="font-size:8.7pt">{twocol(kwl, 3)}</div>
{talk(["What amenities are essential for you in a hotel? What complimentary things do you like?", "All-inclusive vacations: good or bad? Why?"], "USE THE WORDS")}""",
    30, """<ol><li>Start with the questions in the top box: 4 minutes. Question 3: a <b>double</b> room has one big bed for two people; a <b>twin</b> room has two separate beds.</li>
<li>A: quick check (3 minutes). Pronunciation: <i>compli<b>men</b>tary</i> (4–5 syllables), <i>en-<b>suite</b></i> /ɒn ˈswiːt/, <i>con<b>cierge</b></i> /kɒnsiˈeəʒ/.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Danny checks in and checks out of a hotel in Buenos Aires · the problem · true or false · Talk about it",
                      "polite requests: Could you…?, Would you mind + -ing?, Do you mind if I…?, Would it be possible to…?", "Complete, choose · Use it (oral)",
                      "Polite intonation (28.2) · role-play: guest and receptionist with problem cards", "Danny's hotel review · polite requests · word choice · writing"),
        """The Linguahouse lesson has five short dialogues (booking, checking in, checking out), hotel vocabulary and adjectives for hotel reviews. Our listening joins check-in and check-out in one story: after two weeks in Patagonia (B1 Unit 21), Danny stays three nights at the Tango Garden Hotel, a fictional small hotel in Buenos Aires. He asks for the laundry service (his clothes are filthy after the trip) and finds a wrong minibar charge on his bill. The receptionist is a one-off voice. Danny still has no surname: he booked under his first name. In the homework, Danny writes the hotel review he promised. No external facts in this unit.""",
        """Too direct requests (<i>I want the bill</i>, <i>Give me a towel</i>), <i>Would you mind to…</i>, answering <i>Yes</i> to <i>Would you mind…?</i> when they mean OK, and flat intonation. Vocabulary: <i>double</i> vs <i>twin</i>, <i>a view to the sea</i> for <i>a view of the sea</i>, <i>lift</i> (British) vs <i>elevator</i> (American).""",
        "Track 28.1 Checking in and checking out (natural and slow) · Track 28.2 Repeat: polite requests"))

    # Page 2 - Listening
    gist = ["The room isn't clean.", "There's a wrong charge on the bill.", "He can't pay by card."]
    tf = [("Danny booked the room on the phone.", "F"), ("His room has its own bathroom.", "T"), ("Breakfast is included in the price.", "T"),
          ("The laundry is ready the next day.", "F"), ("Danny had two drinks from the minibar.", "F"), ("The hotel keeps his bags until his bus leaves.", "T")]
    tfl = "".join(f"<li>{s} {A(w, 'min-width:6mm')}</li>" for s, w in tf)
    b.page(f"""{sec(2, "Listening: checking in and checking out", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{audiocard(["28.1 · NATURAL", "28.1 · SLOW"])}
{sub("A", "After two weeks in Patagonia, Danny stays at a hotel in Buenos Aires. Listen. What's the problem when he checks out?", "2 min", "28.1")}
<p style="margin:.3mm 0;font-size:8.9pt">{ch(gist, gist[1])}</p></div>{img('B', 40, 27)}</div>
{sub("B", "Listen again. Write T (true) or F (false). Correct the false sentences.", "4 min")}
<ol style="line-height:1.6;font-size:8.8pt;margin:0;columns:2">{tfl}</ol>
{talk(["Have you ever had a problem with a hotel bill? What happened?", "What do you do when a hotel or restaurant makes a mistake? Do you complain?", "Do you write online reviews? Do you read them before you book?"])}""",
    30, """<ol><li>A–B: 6 minutes. Corrections: 1 he booked online · 4 it's ready the same day (before ten) · 5 he didn't open the minibar.</li>
<li>Talk about it: 7 minutes. Note the requests the student uses in their stories; you'll make them more polite on page 3.</li></ol>""")

    # Page 3
    lean.grammar_in_class(b, grammar_ref.polite_requests)

    # Page 4 - Practice
    fs = [("___ telling me what time breakfast is served?", "Would you mind"), ("___ leave my backpack here for an hour?", "Do you mind if I"),
          ("___ tell me what this charge is for?", "Could you"), ("___ to leave my bags here until then?", "Would it be possible"),
          ("___ pay by card?", "Can I")]
    fsl = "".join(f"<li><i>{s.replace('___', A(a, 'min-width:30mm'))}</i></li>" for s, a in fs)
    use = ["Ask the hotel to call you a taxi. (Would you mind…?)", "Ask if you can check out at 2 p.m. (Would it be possible…?)", "Ask a colleague to send you a file. (Could you…?)",
           "Ask your teacher if you can open the window. (Do you mind if I…?)", "Ask a neighbor to water your plants next week. (I was wondering if…)"]
    b.page(f"""{sec(4, "Practice: polite requests", "10 min")}
{sub("A", "Complete the requests from the conversation.", "3 min")}
<div class="bank">Can I · Could you · Do you mind if I · Would it be possible · Would you mind</div>
<ol style="line-height:1.85;font-size:8.9pt;margin:0">{fsl}</ol>
{sub("B", "Choose.", "2 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0"><li>Would you mind {ch(["to close", "closing"], "closing")} the door?</li>
<li>Do you mind if I {ch(["use", "would use"], "use")} your phone?</li>
<li><i>Would you mind waiting a moment?</i> — If it's OK, say: {ch(["Yes, I would.", "Not at all."], "Not at all.")}</li></ol>
<div class="box sand"><h4>RULE</h4><b>Would you mind</b> + -ing · <b>Do you mind if I</b> + present · <b>Would it be possible to</b> + verb · <b>Could you / Can I</b> + verb · <i>Not at all</i> = OK. See the <b>Grammar reference</b> on page 3.</div>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    24, """<ol><li>A–B: 4 minutes. Point out that question 3 in B is a trap: <i>Yes, I would</i> means you <i>do</i> mind (= no).</li>
<li>Use it: 6 minutes, all oral. Answer each request (sometimes say no politely: <i>I'm afraid…</i>) so the student hears the answers too.</li></ol>""")

    # Page 5 - Speaking
    gcards = [("Check in", "You arrive at 10 a.m. Check-in is at 3 p.m. Ask to check in early or leave your bags."),
              ("A problem", "Your room is next to the elevator and it's very noisy. Ask for another room."),
              ("Services", "Ask about the laundry service, Wi-Fi password and a good restaurant nearby."),
              ("Check out", "There's a charge for room service on your bill. You didn't order it. Your flight is at 9 p.m.")]
    gl = "".join(f'<div class="box" style="flex:1;margin:0;font-size:8.1pt"><b>{t}</b><br>{d}</div>' for t, d in gcards)
    b.page(f"""{sec(5, "Speaking: at the front desk", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.3pt"><tr><th>receptionist</th><th>guest: asking</th><th>guest: complaining</th><th>answering</th></tr>
<tr><td><i>How can I help you? · Could you fill in this form? · Here's your key card. · I'm afraid we're fully booked.</i></td><td><i>I have a reservation under… · Would you mind…? · Would it be possible to…? · What time is checkout?</i></td><td><i>I'm sorry, but there's a problem with… · Could you tell me what this charge is for? · I didn't order…</i></td><td><i>Certainly. · Not at all. · Of course not. · I do apologize. · I'm afraid that's not possible.</i></td></tr></table></div>
{audiocard(["28.2"])}
{sub("A", "Listen and repeat. Start high and sound friendly. Which requests ask for permission?", "4 min", "28.2")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.55">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S282))}</p>
{sub("B", "Role-play. You are the guest; your teacher is the receptionist. Do the four cards in order, from check-in to check-out. Then swap: you are the receptionist.", "14 min")}
<div style="display:flex;gap:2mm;margin-top:1mm">{gl}</div>
{talk(["Would you like to work at a hotel front desk? Why or why not?", "What's the best hotel you've ever stayed in? What made it special?"], "TALK ABOUT IT")}""",
    32, """<ol><li>A: permission = 3 (<i>Do you mind if I…</i>), 4 (<i>leave my bags</i>) and 6 (<i>I was wondering if I could…</i>); 5 (<i>Could I have…</i>) is a request for a thing. Flat intonation sounds rude: exaggerate the rise and fall.</li>
<li>B: 12 minutes. As receptionist, say no politely once (<i>I'm afraid check-in is at three, but you can leave your bags</i>) and solve the bill problem only if the student is polite. Swap: be a difficult guest. Last 3 minutes: wrap-up (two corrections, and ask <i>Can you now solve a problem at a hotel politely?</i>).</li></ol>""")

    # Homework
    pc = [(["spacious", "cramped"], "spacious"), (["immaculate", "shabby"], "immaculate"), (["contemporary", "old-fashioned"], "contemporary"), (["patient", "impatient"], "patient"), (["basic", "luxurious"], "luxurious")]
    p = [ch(o, a) for o, a in pc]
    rw = [("Give me a towel.", "Could I have a towel, please? / Could you bring me a towel, please?"), ("Wait here.", "Would you mind waiting here?"),
          ("I want to leave my bags here.", "Do you mind if I leave my bags here? / Would it be possible to leave my bags here?")]
    rwl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Danny writes the hotel review he promised. Choose the correct adjectives.", "")}</div>{img('C', 28, 18)}</div>
<div class="box" style="line-height:1.85;font-size:8.8pt;margin:.5mm 0"><b>★★★★★ Great stay after Patagonia!</b><br>My room was {p[0]}, with plenty of space for all my gear, and the en-suite bathroom was {p[1]}: not a single mark anywhere. The design is {p[2]}, with modern art on the walls. There was a small mistake on my bill, but the receptionist was very {p[3]} and fixed it in a minute. It isn't a {p[4]} hotel, but it has everything you need, and breakfast is complimentary. Highly recommended! — Danny</div>
{sub("B", "Make the requests polite.", "")}
<ol style="line-height:1.5;font-size:8.7pt;margin:0">{rwl}</ol>
{lean.watch_out([("I want the bill.", "Could I have the bill, please?", "<i>I want</i> sounds rude in a request."), ("The room has a view to the sea.", "The room has a view of the sea.", "a view <b>of</b> something."), ("We need a double room with two beds.", "We need a twin room.", "<i>double</i> = one big bed; <i>twin</i> = two beds.")])}
{lean.writing_task(sub, "Write an online review of a hotel you stayed in: the room, the staff, the amenities, any problem, and your recommendation.", "I stayed at… for… nights. The room was…", ["three adjectives (spacious, cramped, immaculate…)", "a problem and how they solved it", "a recommendation", "100–150 words"], "I can check in, ask for services and solve a problem at a hotel.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class (B: accept any polite form). The writing task is Linguahouse's option 2. Read it at home and choose two mistakes to discuss in class.</p>""")

    script = "".join(f"<p style='margin:.4mm 0'><b>{l.split(': ', 1)[0]}:</b> {l.split(': ', 1)[1]}</p>" for l in S281)
    b.extra("Audio script", f"""
{sub("28.1", "Checking in and checking out (natural and slow)")}
<div style="line-height:1.28;font-size:8.5pt">{script}</div>
{sub("28.2", "Repeat: polite requests")}
<p>{" · ".join(S282)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 28 - At the hotel")
