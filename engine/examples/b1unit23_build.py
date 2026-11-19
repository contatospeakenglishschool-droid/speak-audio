# Speak! Progress B1 - Unit 23 "Money and banking" (all English) - lean B1 format (rebuilt 2026-11-19)
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
setup(band="B1 · UNIT 23", audio_json="audio_b1-unit-23.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-23"]
S231 = [l.replace("March third, two thousand four", "March 3, 2004").replace("eight hundred forty-two dollars", "$842").replace("twenty minutes", "20 minutes").replace("six, two, eight, one", "6, 2, 8, 1") for l in _r["23.1 The ATM kept my card"].split("\n")]
S232 = [x.split(": ", 1)[1] for x in _r["23.2 Repeat: money amounts"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'

    # 1 Warm-up
    cover = cover_html(T, "LEVEL B1 · UNIT 23", "Money and banking", "Money when you travel · <b>unless, as long as, in case, otherwise</b>",
                       [("YOU CAN", "change money, use a bank or an ATM, solve a card problem by phone and give money tips"),
                        ("LANGUAGE", "the exchange rate · a commission · a debit card · the balance · overdrawn · freeze a card · in case it's fraud"),
                        ("PRONUNCIATION", "saying money amounts: twelve fifty, a five-dollar bill")])
    cu = [("euro (EUR)", "most countries in the European Union"), ("pound (GBP)", "the United Kingdom"), ("yen (JPY)", "Japan"),
          ("yuan (CNY)", "China"), ("dollar (USD)", "the United States"), ("real (BRL)", "Brazil")]
    cul = [f'<li value="{i+1}"><b>{c}</b> {A(w, "min-width:24mm")}</li>' for i, (c, w) in enumerate(cu)]
    b.page(f"""{sec(1, "Warm-up: money matters", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["When did you last pay for something in cash?", "Have you ever bought foreign currency for a trip?", "Do you use your bank app more than the bank branch?"], "START TALKING")}</div></div>
{sub("A", "Currencies. Where are they used? Write the country.", "3 min")}
<div class="bank">Brazil · China · Japan · most countries in the European Union · the United Kingdom · the United States</div>
<div style="font-size:8.5pt">{twocol(cul, 3)}</div>
{talk(["Read these rates aloud: EUR 0.89 = USD 1 · GBP 0.85 = EUR 1 (practice examples).", "Which currency would you like to use next? Where?"], "USE THE WORDS")}""",
    26, """<ol><li>Top box: 4 minutes.</li>
<li>A: in most codes, the first two letters show the country (<b>BR</b>L). <i>Yen</i> and <i>yuan</i> have no plural. Rates are practice examples, not real; say <i>zero point eight nine</i>, not <i>oh</i>.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Phone call: an ATM keeps Danny's card; he calls his US bank · complete · Talk about it", "unless, as long as, in case, otherwise",
                      "Complete the agent's sentences · choose · Use it (oral)", "Functional language · money amounts (23.2) · bank role-plays",
                      "Ana's money tips · bank words · word choice · writing"),
        "The Linguahouse lesson has two short generic dialogues (a foreign exchange office and a bank counter) and online banking vocabulary. Our listening is a situation that travelers really face: an ATM in São Paulo keeps Danny's debit card two weeks before his trip to Argentina (B1 Units 21–22). He calls his bank in the US; the agent, Kevin (Charon), freezes the card, checks his balance, orders a new one and explains the travel notice. The bank and its rules are fictional, so no real-world facts are stated; no real exchange rates are given (the rates on page 1 are practice examples). Danny's date of birth (March 3, 2004) is new: he is 22. In the homework, Ana gives Danny money tips for his trip.", "Students say <i>unless you don't…</i> (double negative), confuse <i>in case</i> and <i>if</i>, and use <i>will</i> after <i>as long as</i>. False friends: <i>agency</i> (a bank branch), <i>I paid in ten times</i> (in ten installments), <i>take money</i> (take out / withdraw), <i>the cash isn't working</i> (the ATM).",
        "Track 23.1 The ATM kept my card (natural and slow) · Track 23.2 Repeat: money amounts"))

    # 2 Listening
    gist = ["Someone stole his card.", "An ATM kept his card.", "He's overdrawn."]
    gp = [("I'm going to ___ the card now, so nobody can use it.", "freeze"), ("It usually takes seven to ten ___ days.", "business"),
          ("I don't want to take out cash with my credit card. The ___ are crazy.", "fees"), ("Your checking account ___ is $842.", "balance"),
          ("You're not ___, so don't worry.", "overdrawn"), ("You can add your dates in the app, under travel ___.", "notice")]
    gpl = "".join(f"<li>{s.replace('___', A(a, 'min-width:16mm'))}</li>" for s, a in gp)
    b.page(f"""{sec(2, "Listening: the ATM kept my card", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{audiocard(["23.1 · NATURAL", "23.1 · SLOW"])}
{sub("A", "Danny calls his bank in the US. Listen. What's the problem?", "2 min", "23.1")}
<p style="margin:.3mm 0;font-size:8.9pt">{ch(gist, gist[1])}</p></div>{img('B', 40, 27)}</div>
{sub("B", "Listen again and complete.", "4 min")}
<ol style="line-height:1.55;font-size:8.6pt;margin:0">{gpl}</ol>
{talk(["Why does the agent freeze the card?", "What would you do if an ATM kept your card abroad?", "Have you ever had a problem with a card or a bank? What happened?"])}""",
    26, """<ol><li>A–B: 6 minutes. <i>Freeze a card</i> = block it temporarily; <i>overdrawn</i> = with a negative balance. Remind students never to give their full card number or password on the phone.</li>
<li>Talk about it: 6 minutes. 1: so nobody can use it, in case someone gets it from the ATM.</li></ol>""")

    # 3 Grammar reference
    lean.grammar_in_class(b, grammar_ref.unless_in_case)

    # 4 Practice
    fs = [("___ the bank there gives it back to you today, I'd recommend ordering a new one.", "Unless"), ("We can send it, ___ you give us a full address.", "as long as"),
          ("Add your travel dates. ___, our system might block the card.", "Otherwise"), ("The system might block the card ___ it's fraud.", "in case")]
    fsl = "".join(f"<li><i>{s.replace('___', A(a, 'min-width:18mm'))}</i></li>" for s, a in fs)
    use = ["What do you always take on a trip, in case something goes wrong?", "Finish: <i>I never take out cash unless…</i>", "Finish: <i>You can borrow my car as long as…</i>",
           "Give a tip for travelers: <i>Tell your bank your dates. Otherwise…</i>", "What won't you do this weekend unless it's sunny?"]
    b.page(f"""{sec(4, "Practice: unless, as long as, in case", "10 min")}
{sub("A", "Complete the agent's sentences with unless, as long as, in case or otherwise.", "3 min")}
<ol style="line-height:1.85;font-size:8.9pt;margin:0">{fsl}</ol>
{sub("B", "Choose.", "1 min")}
<p style="margin:.3mm 0;font-size:8.9pt;line-height:1.7">{ch(["Unless you call", "Unless you don't call"], "Unless you call")} the bank, they'll block your card. &nbsp;·&nbsp; You can use my card as long as you {ch(["pay", "will pay"], "pay")} me back.</p>
<div class="box sand"><h4>RULE</h4><b>unless</b> = if … not · <b>as long as / provided (that)</b> = only if · <b>in case</b> = to be prepared for a possible problem · <b>otherwise</b> = if not (new sentence). Use the <b>present</b> after them for the future; no double negative after <i>unless</i>. See the <b>Grammar reference</b> on page 3.</div>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    24, """<ol><li>A–B: 4 minutes. Contrast <i>I'll take an umbrella if it rains</i> (strange) and <i>in case it rains</i> (natural).</li>
<li>Use it: 6 minutes, all oral. Correct <i>unless … don't</i> every time.</li></ol>""")

    # 5 Speaking
    b.page(f"""{sec(5, "Speaking: at the bank", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>exchange office</th><th>at the bank</th><th>a card problem</th><th>tips</th></tr>
<tr><td><i>I'd like to change… into… · What's the exchange rate? · Do you charge commission? · In twenties, please.</i></td><td><i>I'd like to check my balance. · Can I take out…? · I'd like to open an account.</i></td><td><i>My card was blocked / kept / stolen. · Could you freeze it? · How long will a new one take?</i></td><td><i>…in case… · …unless… · …as long as… · Otherwise…</i></td></tr></table></div>
{audiocard(["23.2"])}
{sub("A", "Money amounts. Listen and repeat: twelve fifty · a five-dollar bill · fifteen hundred dollars.", "4 min", "23.2")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.55">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S232))}</p>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("B", "Role-plays. You are the customer; your teacher is the clerk or the agent. Then change roles.", "10 min")}
<ol style="line-height:1.4;font-size:8.7pt;margin:0"><li>At an exchange office abroad: change 200 dollars. Ask about the rate and commission.</li><li>At the bank counter: the ATM outside isn't working. Check your balance and take out some cash.</li><li>On the phone: your credit card was stolen on vacation. Freeze it and ask for a new one.</li></ol>
<p style="margin:.3mm 0;font-size:8.5pt">{R("Teacher's card: 1 invent a rate, commission 3%, ask for ID. 2 the customer is overdrawn: no cash unless they transfer money from savings. 3 security questions first; the new card takes 5 business days, as long as the address is correct.") if T else ""}</p></div>{img('D', 28, 28)}</div>
{talk(["How do you manage money when you travel: cash or cards?", "Will cash disappear in the future? Is that good or bad?"])}""",
    28, """<ol><li>A: <i>a five-dollar bill</i> (no <i>s</i>: it's an adjective). B: follow the teacher's card; push the student to ask questions and use the target words.</li>
<li>Last 3 minutes: wrap-up (two corrections and <i>Can you solve a money problem in English?</i>).</li></ol>""")

    # H Homework
    pc = [(["in case", "unless"], "in case"), (["unless", "as long as"], "unless"), (["as long as", "in case"], "as long as"), (["Otherwise", "Unless"], "Otherwise"), (["in case", "if"], "in case")]
    p = [ch(o, a) for o, a in pc]
    ob = [("You open your banking app.", "Log in"), ("You move money from savings to checking.", "Transfer money"), ("You check that your salary arrived.", "View statement")]
    obl = "".join(f"<li>{s} {A(o, 'min-width:24mm')}</li>" for s, o in ob)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Ana sends Danny some money tips for his trip. Choose the correct words.", "")}</div>{img('C', 28, 18)}</div>
<div class="box" style="line-height:1.8;font-size:8.8pt;margin:.5mm 0"><b>From: Ana · To: Danny</b><br>Danny, I heard about the ATM! Take two cards {p[0]} one gets blocked again. Don't take out cash {p[1]} you really need it, because every withdrawal has a fee. You can pay by card almost everywhere, {p[2]} you check the fees first. Add the travel notice tonight. {p[3]}, you'll have the same problem in Argentina! And take a photo of your passport {p[4]} you lose it. Ana</div>
{sub("B", "Online banking. Which option do you click? Log in, Transfer money or View statement.", "")}
<ol style="line-height:1.5;font-size:8.6pt;margin:0">{obl}</ol>
{lean.watch_out([("I went to the bank agency.", "I went to the bank branch.", "an <i>agency</i> is a business like a travel agency."), ("I paid in ten times.", "I paid in ten installments.", "<i>installments</i> = monthly payments."), ("I need to take money.", "I need to take out / withdraw money.", "from an ATM: <i>take out</i> or <i>withdraw</i>.")])}
{lean.writing_task(sub, "Money tips for travelers: write a short post for a travel forum with your best money tips.", "Always travel with two cards in case… Don't take out cash unless…", ["four tips", "unless, in case, as long as, otherwise", "a question for readers", "100–150 words"], "I can solve a money problem and give tips with unless and in case.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class. When you correct the writing, check the linkers and the present after them.</p>""")

    script = "".join(f"<p style='margin:.5mm 0'><b>{l.split(': ', 1)[0]}:</b> {l.split(': ', 1)[1]}</p>" for l in S231)
    b.extra("Audio script", f"""
{sub("23.1", "The ATM kept my card (natural and slow)")}
<div style="line-height:1.3;font-size:8.6pt">{script}</div>
{sub("23.2", "Repeat: money amounts")}
<p>{" · ".join(S232)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 23 - Money and banking")
