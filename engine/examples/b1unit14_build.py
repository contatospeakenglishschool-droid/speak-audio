# Speak! Progress B1 - Unit 14 "At the restaurant" (all English) - lean B1 format (rebuilt 2026-11-19)
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Progress"
import lean
from lean import talk
setup(band="B1 · UNIT 14", audio_json="audio_b1-unit-14.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-14"]
S141 = [l.replace("ten percent", "10%").replace("twenty percent", "20%") for l in _r["14.1 Dinner is on me"].split("\n")]
S142 = [x.split(": ", 1)[1] for x in _r["14.2 Repeat: polite questions"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'

    # 1 Warm-up
    cover = cover_html(T, "LEVEL B1 · UNIT 14", "At the restaurant", "Ordering and paying · <b>indirect questions: Could you tell me…? Do you know if…?</b>",
                       [("YOU CAN", "order a meal, ask about dishes politely, and deal with the check and the tip"),
                        ("LANGUAGE", "an appetizer · a side dish · the check · a tip · What does it come with? · Do you know if it's spicy?"),
                        ("PRONUNCIATION", "polite intonation in requests and indirect questions")])
    kw = [("a small amount of food before the main part of a meal (also: a starter)", "an appetizer"), ("the largest or most important part of a meal", "the main course"),
          ("an extra food served on a separate plate, like fries or a salad", "a side dish"), ("the piece of paper that shows how much you have to pay", "the check"),
          ("extra money you leave for the server", "a tip"), ("an amount added to the check to pay for the service", "a service charge")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:22mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Warm-up: eating out", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["How often do you eat out? Do you prefer to eat in or eat out?", "What's the best restaurant you know? What do you order there?", "What's stressful about restaurants abroad (ordering, the check, the tip…)?"], "START TALKING")}</div></div>
{sub("A", "Key words. Write the words from the box next to the definitions.", "3 min")}
<div class="bank">an appetizer · the check · the main course · a service charge · a side dish · a tip</div>
<div style="font-size:8.6pt">{twocol(kwl, 3)}</div>
{talk(["You're traveling abroad. Plan a meal from an international menu: an appetizer, a main course with a side dish, and a dessert.", "Do you always leave a tip? How much?"], "USE THE WORDS")}""",
    26, """<ol><li>Top box: <i>eat in</i> = eat at home; <i>eat out</i> = eat at a restaurant.</li>
<li>A: <i>check</i> is American English (British: <i>bill</i>). <i>Appetizer</i> (US) = <i>starter</i> (UK). <i>Server</i> is the neutral word for waiter/waitress.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Dialogue: Danny takes Ana to a bistro · what they order · Talk about it", "Indirect questions",
                      "Make the questions polite · choose the rule · Use it (oral)", "Functional language · polite intonation (14.2) · restaurant role-play",
                      "Carol's email about tipping · restaurant phrases · word choice · writing"),
        "The Linguahouse lesson uses a dialogue in an English-style restaurant and a dinner between two business contacts. Our listening brings both ideas together: Danny has recovered from the flu (B1 Unit 13) and takes Ana to a bistro with an international menu to thank her. He asks the server about the dishes with indirect questions, mentions his nut allergy, orders a steak (medium), changes his drink order, and insists on paying (<i>It's on me</i>). The restaurant is fictional. Verified facts: in Brazil, a 10% service charge is common on the check, but it is optional, and the restaurant must make that clear (Procon-SP; Idec). In the United States, the usual guideline for a sit-down restaurant is a tip of 15 to 20% (Emily Post Institute; Pew Research Center 2023). Carol (Orlando) writes about tipping in the homework.",
        "Students say <i>Can you bring the account?</i> (the check), <i>I want a coke</i> (sounds rude: <i>I'll have / I'd like</i>), <i>I'm satisfied</i> for <i>I'm full</i>, and keep question word order in indirect questions: <i>Do you know where is the restroom?</i>",
        "Track 14.1 Dinner is on me (natural and slow) · Track 14.2 Repeat: polite questions"))

    # 2 Listening
    gist = ["to celebrate his new job", "to thank Ana for her help", "to meet Ana's husband"]
    ordr = [("appetizer", "–", "tomato soup"), ("main course", "steak (medium), mashed potatoes", "mushroom risotto"), ("drink", "iced tea", "sparkling water")]
    ordt = "".join(f"<tr><td><b>{a}</b></td><td>{A(d, 'min-width:30mm')}</td><td>{A(n, 'min-width:30mm')}</td></tr>" for a, d, n in ordr)
    b.page(f"""{sec(2, "Listening: dinner is on me", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{audiocard(["14.1 · NATURAL", "14.1 · SLOW"])}
{sub("A", "Danny takes Ana to a bistro. Listen. Why does he invite her?", "2 min", "14.1")}
<p style="margin:.3mm 0;font-size:8.9pt">{ch(gist, gist[1])}</p></div>{img('B', 40, 27)}</div>
{sub("B", "Listen again. What do they order? Complete the table.", "4 min")}
<table style="font-size:8.6pt;margin:.5mm 0"><tr><th style="width:24mm"></th><th>Danny</th><th>Ana</th></tr>{ordt}</table>
{talk(["&ldquo;I didn't want to ask.&rdquo; Why does Ana ask Danny, not the server, about <i>medium</i>?", "How do you like your steak: rare, medium or well-done? Do you have any food allergies?", "Who should pay when you invite someone to dinner in your culture?"])}""",
    26, """<ol><li>A–B: 6 minutes. Teach <i>How would you like your steak?</i> (rare, medium, well-done) and <i>dressing</i>: travelers hear them everywhere.</li>
<li>Talk about it: 6 minutes. 1: she was embarrassed, or she didn't want to look like she didn't know.</li></ol>""")

    # 3 Grammar reference
    lean.grammar_in_class(b, grammar_ref.indirect_questions)

    # 4 Practice
    fs = [("What's today's special?", "Could you tell me what today's special is?"), ("Does the risotto have any nuts in it?", "Do you know if the risotto has any nuts in it?"),
          ("What does medium mean?", "Do you know what medium means?")]
    fsl = "".join(f"<li><i>{d}</i> → {A(i, 'min-width:60mm')}</li>" for d, i in fs)
    use = ["Ask your teacher about a restaurant: <i>Could you tell me…?</i>", "Ask about the menu: <i>Do you know if…?</i>", "Ask for a table for four on Saturday: <i>I was wondering if…</i>",
           "Ask where the restroom is, politely.", "Your teacher asks direct questions. Make them polite."]
    b.page(f"""{sec(4, "Practice: indirect questions", "10 min")}
{sub("A", "Danny's questions from the dialogue. Write the polite form he used.", "3 min")}
<ol style="line-height:1.85;font-size:8.9pt;margin:0">{fsl}</ol>
{sub("B", "Choose.", "1 min")}
<p style="margin:.3mm 0;font-size:8.9pt;line-height:1.7">Could you tell me where {ch(["the restroom is", "is the restroom"], "the restroom is")}? &nbsp;·&nbsp; Do you know {ch(["if", "that"], "if")} it's spicy?</p>
<div class="box sand"><h4>RULE</h4>Start with <b>Could you tell me… / Do you know… / I was wondering…</b>, then use normal word order: question word + <b>subject + verb</b>. No <i>do/does/did</i>. For yes/no questions, add <b>if</b> or <b>whether</b>. See the <b>Grammar reference</b> on page 3.</div>
{talk(use, "USE IT: ASK OUT LOUD")}""",
    24, """<ol><li>A–B: 4 minutes. Highlight the word order with two colors: <i>What <b>is</b> today's special?</i> → <i>…what today's special <b>is</b>.</i></li>
<li>Use it: 6 minutes, all oral. Answer as a server; correct the word order every time.</li></ol>""")

    # 5 Speaking
    b.page(f"""{sec(5, "Speaking: a table for two", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>server</th><th>customer: ask</th><th>customer: order</th><th>host / guest</th></tr>
<tr><td><i>Are you ready to order? · Anything to drink? · Can I get you some dessert?</i></td><td><i>Could you tell me what's in…? · Do you know if…? · What would you recommend?</i></td><td><i>I'd like to start with… · I'll have… · Make that… · Just water for me.</i></td><td><i>It's on me. · Let me get this. · OK, if you insist. · Next time is on me.</i></td></tr></table></div>
{audiocard(["14.2"])}
{sub("A", "Polite questions. Listen and repeat. Copy the friendly fall-rise: Could you /kʊdʒə/…", "4 min", "14.2")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.55">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S142))}</p>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("B", "Role-play: an international restaurant. Write a short menu with three dishes from any country. You are the server; your teacher is a tourist who asks a lot of questions. Then change roles.", "10 min")}
<div style="display:flex;gap:3mm;font-size:8.6pt"><div style="flex:1"><b>Dish 1:</b><div class="wline"></div></div><div style="flex:1"><b>Dish 2:</b><div class="wline"></div></div><div style="flex:1"><b>Dish 3:</b><div class="wline"></div></div></div>
<p style="margin:.3mm 0;font-size:8.6pt">{R("Teacher's card (tourist): You're vegetarian, you're allergic to nuts, and you want to know what each dish comes with. Change your drink order once. At the end, ask if the service charge is included.") if T else ""}</p></div>{img('D', 32, 24)}</div>
{talk(["Tell me about a memorable meal at a restaurant (great or terrible).", "Should tips be optional, or should restaurants pay servers more?"])}""",
    28, """<ol><li>B: help the student describe dishes: <i>It's a kind of…, It's made with…, It's served with…</i>. Push for indirect questions when the student is the customer.</li>
<li>Last 3 minutes: wrap-up (two corrections and <i>Can you order and ask about dishes politely?</i>).</li></ol>""")

    # H Homework
    pc = [(["check", "account"], "check"), (["tip", "change"], "tip"), (["15 to 20", "5 to 10"], "15 to 20"), (["included", "optional"], "optional"),
          (["on me", "for me"], "on me"), (["if", "that"], "if")]
    p = [ch(o, a) for o, a in pc]
    ph = [("Are you ready to order?", "taking an order"), ("What does it come with?", "asking about dishes"), ("Could we have the check, please?", "paying")]
    phl = "".join(f"<li><i>{x}</i> {A(c, 'min-width:24mm')}</li>" for x, c in ph)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Carol (Orlando) answers Danny's question about tipping. Choose the correct words.", "")}</div>{img('C', 28, 18)}</div>
<div class="box" style="line-height:1.8;font-size:8.8pt;margin:.5mm 0"><b>From: Carol · To: Danny</b><br>Hi Danny! In the US, when the server brings the {p[0]}, you usually add a {p[1]}. For a sit-down restaurant, most people leave {p[2]} percent of the bill. In Brazil it's different: a 10% service charge is often on the check, but it's {p[3]}. And when an American friend says "It's {p[4]}," it means they're paying! If you aren't sure, ask the server politely, "Could you tell me {p[5]} the tip is included?" Hugs, Carol</div>
{sub("B", "What is each phrase for? Write: taking an order, asking about dishes or paying.", "")}
<ol style="line-height:1.5;font-size:8.6pt;margin:0">{phl}</ol>
{lean.watch_out([("Can you bring the account?", "Could we have the check, please?", "at a restaurant = <i>the check</i> (US) or <i>the bill</i> (UK)."), ("I want a coke.", "I'll have / I'd like a coke.", "<i>I want</i> sounds rude when you order."), ("No, thanks. I'm satisfied.", "No, thanks. I'm full.", "after eating = <i>full</i>.")])}
{lean.writing_task(sub, "A restaurant review: write an online review of a restaurant you know.", "Last Friday I took a friend to… The place is… Our server was…", ["the place", "the food (one dish)", "the service and the price", "100–150 words"], "I can order a meal and ask about dishes politely.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class. <i>It's on me</i> = I'm paying. When you correct the writing, check restaurant vocabulary (<i>check, server, side dish, full</i>).</p>""")

    script = "".join(f"<p style='margin:.5mm 0'><b>{l.split(': ', 1)[0]}:</b> {l.split(': ', 1)[1]}</p>" for l in S141)
    b.extra("Audio script", f"""
{sub("14.1", "Dinner is on me (natural and slow)")}
<div style="line-height:1.3;font-size:8.5pt">{script}</div>
{sub("14.2", "Repeat: polite questions")}
<p>{" · ".join(S142)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 14 - At the restaurant")
