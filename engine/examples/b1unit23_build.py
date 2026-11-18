# Speak! Progress B1 - Unit 23 "Money and banking" (all English) - B1 format (2026-11-18)
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Progress"
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
    def lines(n):
        return '<div class="wline"></div>' * n

    # Page 1 - Warm-up
    cover = cover_html(T, "LEVEL B1 · UNIT 23", "Money and banking", "Money when you travel · <b>unless, as long as, in case, otherwise</b>",
                       [("YOU CAN", "change money, use a bank or an ATM, solve a card problem by phone and give money tips"),
                        ("LANGUAGE", "the exchange rate · a commission · a debit card · the balance · overdrawn · freeze a card · in case it's fraud"),
                        ("PRONUNCIATION", "saying money amounts: twelve fifty, a five-dollar bill")])
    cu = [("euro (EUR)", "most countries in the European Union"), ("pound (GBP)", "the United Kingdom"), ("yen (JPY)", "Japan"), ("franc (CHF)", "Switzerland"),
          ("yuan (CNY)", "China"), ("rupee (INR)", "India"), ("dollar (USD)", "the United States"), ("real (BRL)", "Brazil")]
    cul = [f'<li value="{i+1}"><b>{c}</b> {A(w, "min-width:24mm")}</li>' for i, (c, w) in enumerate(cu)]
    b.page(f"""{sec(1, "Warm-up: money matters", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 46, 31)}<div style="flex:1">
{sub("A", "When was the last time you…", "3 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0"><li>paid for something in cash?</li><li>bought foreign currency for a trip?</li><li>went to a bank in person?</li><li>used your bank app?</li></ol></div></div>
{sub("B", "Currencies. Where are they used? Write the country.", "4 min")}
<div class="bank">Brazil · China · India · Japan · most countries in the European Union · Switzerland · the United Kingdom · the United States</div>
<div style="font-size:8.5pt">{twocol(cul, 4)}</div>
{sub("C", "Read these exchange rates aloud. Example: EUR 0.89 = USD 1 → zero point eight nine euros to the dollar.", "1 min")}
<p style="margin:.3mm 0;font-size:8.8pt">GBP 0.85 = EUR 1 &nbsp;·&nbsp; CHF 0.97 = USD 1 &nbsp;·&nbsp; JPY 143.35 = GBP 1</p>""",
    30, """<ol><li>B: in most codes, the first two letters show the country (<b>BR</b>L, <b>US</b>D). <i>Yen</i> and <i>yuan</i> have no plural: <i>ten yen</i>. The plural of <i>real</i> in English is usually <i>reais</i>.</li>
<li>C: the rates are examples for practice, not real rates. Say <i>zero</i>, not <i>oh</i>, in rates: <i>zero point eight five pounds to the euro</i>.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 60 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Discussion · currencies · reading exchange rates</td><td>1</td></tr>
<tr><td>2 Listening</td><td>12 min</td><td>Phone call: an ATM keeps Danny's card; he calls his bank in the US</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>8 min</td><td>unless, as long as, in case, otherwise</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>unless, as long as, in case, otherwise (study at home)</td><td>4</td></tr>
<tr><td>4 Vocabulary lab + pronunciation</td><td>8 min</td><td>Bank words in pairs · online banking · saying money amounts</td><td>5</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Ana's money tips for Danny's trip · rewriting with unless / in case</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Role-plays: exchange office, bank counter, calling the bank · long turn · talking point</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>4 min</td><td>Can-do · language notes · writing homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY</h4>The Linguahouse lesson has two short generic dialogues (a foreign exchange office and a bank counter) and online banking vocabulary. Our listening is a situation that travelers really face: an ATM in São Paulo keeps Danny's debit card two weeks before his trip to Argentina (B1 Units 21–22). He calls his bank in the US; the agent, Kevin (Charon), freezes the card, checks his balance, orders a new one and explains the travel notice. The bank and its rules are fictional, so no real-world facts are stated; no real exchange rates are given (the rates on page 1 are practice examples). Danny's date of birth (March 3, 2004) is new: he is 22. In the Practice, Ana gives Danny money tips for his trip. The writing model is Danny's money tips for travelers.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students say <i>unless you don't…</i> (double negative), confuse <i>in case</i> and <i>if</i>, and use <i>will</i> after <i>as long as</i>. False friends: <i>agency</i> (a bank branch), <i>I paid in ten times</i> (in ten installments), <i>take money</i> (take out / withdraw), <i>the cash isn't working</i> (the ATM).</div>
<div class="box"><h4>AUDIO</h4>Track 23.1 The ATM kept my card (natural and slow) · Track 23.2 Repeat: money amounts</div>""")

    # Page 2 - Listening
    gist = ["Someone stole his card.", "An ATM kept his card.", "He's overdrawn."]
    gp = [("I'm going to ___ the card now, so nobody can use it.", "freeze"), ("It usually takes seven to ten ___ days.", "business"),
          ("I don't want to take out cash with my credit card. The ___ are crazy.", "fees"), ("You can transfer it back to them in the ___.", "app"),
          ("Your checking account ___ is $842.", "balance"), ("You're not ___, so don't worry.", "overdrawn"), ("You can add your dates in the app, under travel ___.", "notice")]
    gpl = "".join(f"<li>{s.replace('___', A(a, 'min-width:16mm'))}</li>" for s, a in gp)
    tf = [("Money was taken out of Danny's account at the ATM.", "F (no money was taken out)"), ("The bank can send a new card to Brazil.", "T (with a full address)"),
          ("Danny wants to take out cash with his credit card.", "F (the fees are too high)"), ("Danny needs to tell the bank his travel dates.", "T")]
    tfl = [f'<li value="{i+1}">{s} {A(a, "min-width:9mm")}</li>' for i, (s, a) in enumerate(tf)]
    b.page(f"""{sec(2, "Listening: the ATM kept my card", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{audiocard(["23.1 · NATURAL", "23.1 · SLOW"])}
{sub("A", "Danny calls his bank in the US. Listen at natural speed. What's the problem?", "2 min", "23.1")}
<p style="margin:.3mm 0;font-size:8.9pt">{ch(gist, gist[1])}</p></div>{img('B', 40, 27)}</div>
{sub("B", "Listen again and complete.", "4 min")}
<ol style="line-height:1.55;font-size:8.6pt;margin:0">{gpl}</ol>
{sub("C", "True or false? Correct the false sentences.", "3 min")}
<div style="font-size:8.6pt">{twocol(tfl, 2)}</div>
{sub("D", "Think about it. Discuss with your teacher.", "3 min")}
<ol style="line-height:1.4;font-size:8.7pt;margin:0"><li>Why does the agent freeze the card? {R("So nobody can use it, in case someone gets it from the ATM.") if T else ""}</li><li>What would you do if an ATM kept your card abroad?</li></ol>
<div class="box sand" style="margin-top:1mm"><h4>NOTICE: USEFUL CHUNKS</h4><i>I'm calling from… · Before we start… · That's right. · The problem is… · In the meantime… · Phew! · Got it. · Is there anything else I can help you with?</i></div>""",
    27, """<ol><li>B: <i>freeze a card</i> = block it temporarily; <i>overdrawn</i> = with a negative balance; <i>a travel notice</i> tells the bank you'll use your card abroad.</li>
<li>Remind students never to give their full card number or password on the phone; banks only ask for the last four digits.</li></ol>""")

    # Page 3 - Language focus
    fs = [("___ the bank there gives it back to you today, I'd recommend ordering a new one.", "Unless"), ("We can send it, ___ you give us a full address.", "as long as"),
          ("Add your travel dates. ___, our system might block the card.", "Otherwise"), ("The system might block the card ___ it's fraud.", "in case")]
    fsl = "".join(f"<li><i>{s.replace('___', A(a, 'min-width:18mm'))}</i></li>" for s, a in fs)
    b.page(f"""{sec(3, "Language focus: unless, as long as, in case", "8 min")}
{sub("A", "Complete the agent's sentences with unless, as long as, in case or otherwise. Then listen again and check.", "2 min")}
<ol style="line-height:1.85;font-size:8.9pt;margin:0">{fsl}</ol>
{sub("B", "Complete the rules. Choose.", "3 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0"><li><i>unless</i> means {ch(["if … not", "if"], "if … not")}.</li>
<li><i>as long as</i> means {ch(["only if", "even if"], "only if")}.</li>
<li><i>Take cash in case the ATM doesn't work</i>: you take cash {ch(["now, to be prepared", "only when the ATM doesn't work"], "now, to be prepared")}.</li>
<li><i>Otherwise</i> means {ch(["if not", "because"], "if not")}; it usually starts a new sentence.</li>
<li>After these words, for the future, we use {ch(["the present", "will"], "the present")}.</li></ol>
{sub("C", "Correct or incorrect? Choose.", "3 min")}
<ol style="line-height:1.6;font-size:8.9pt;margin:0"><li>Unless you don't call the bank, they'll block your card. {ch(["correct", "incorrect"], "incorrect")} {R("→ Unless you call / If you don't call") if T else ""}</li><li>Take a photo of your passport in case you lose it. {ch(["correct", "incorrect"], "correct")}</li><li>You can use my card as long as you will pay me back. {ch(["correct", "incorrect"], "incorrect")} {R("→ as long as you pay me back") if T else ""}</li></ol>
<div class="box sand"><h4>RULE</h4><b>unless</b> = if … not · <b>as long as / provided (that)</b> = only if · <b>in case</b> = to be prepared for a possible problem · <b>otherwise</b> = if not (new sentence). Use the <b>present</b> after them for the future; no double negative after <i>unless</i>. More on the next page: <b>Grammar reference</b>.</div>""",
    27, """<ol><li>A: ask the student to rewrite sentence 1 with <i>if</i>: <i>If the bank doesn't give it back…</i></li>
<li>B: contrast <i>I'll take an umbrella if it rains</i> (strange) and <i>in case it rains</i> (natural).</li></ol>""")

    grammar_ref.unless_in_case(b)

    # Page 5 - Vocabulary lab
    pr = [("a debit card / a credit card", "debit: money comes from your account now; credit: you borrow and pay later"),
          ("a checking account / a savings account", "checking: for everyday use; savings: to keep money and earn interest"),
          ("in credit / overdrawn", "in credit: you have money; overdrawn: your balance is negative"),
          ("check the balance / freeze your account", "check: see how much you have; freeze: stop all payments"),
          ("bills / notes", "the same thing: paper money in the US / in the UK")]
    prl = "".join(f"<li><b>{a}</b> {R(e) if T else lines(1)}</li>" for a, e in pr)
    ob = [("You open your banking app.", "Log in"), ("You move money from savings to checking.", "Transfer money"), ("You pay your electricity bill online.", "Make a payment"),
          ("You check that your salary arrived.", "View statement"), ("The bank has your instructions.", "Process request")]
    obl = "".join(f"<li>{s} {A(o, 'min-width:24mm')}</li>" for s, o in ob)
    b.page(f"""{sec(4, "Vocabulary lab: banking", "4 min")}
{sub("A", "What's the difference? Explain to your teacher.", "2 min")}
<ol style="line-height:1.4;font-size:8.6pt;margin:0">{prl}</ol>
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("B", "Online banking. Which option do you click? Log in, Make a payment, Process request, Transfer money or View statement.", "2 min")}
<ol style="line-height:1.5;font-size:8.6pt;margin:0">{obl}</ol></div>{img('C', 30, 20)}</div>
<div class="box sand"><h4>WATCH OUT: FALSE FRIENDS AND WORD CHOICE</h4>
<table style="margin:0;font-size:8.2pt"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>I went to the bank agency.</td><td><b>I went to the bank branch.</b></td><td>an <i>agency</i> is a business like a travel agency.</td></tr>
<tr><td>I paid in ten times.</td><td><b>I paid in ten installments.</b></td><td><i>installments</i> = monthly payments.</td></tr>
<tr><td>I need to take money.</td><td><b>I need to take out / withdraw money.</b></td><td>from an account or an ATM, use <i>take out</i> or <i>withdraw</i>.</td></tr>
<tr><td>The cash isn't working.</td><td><b>The ATM / cash machine isn't working.</b></td><td><i>cash</i> = money in bills and coins.</td></tr></table></div>
{sec(5, "Pronunciation lab: money amounts", "4 min")}
<p class="small" style="margin:.3mm 0">$12.50 = <i>twelve dollars and fifty cents</i> or just <i>twelve fifty</i> · $1,500 = <i>fifteen hundred dollars</i> · a <i>five-dollar</i> bill (no <i>s</i>: it's an adjective). In American English, <i>and</i> is often dropped: <i>eight hundred forty-two</i>.</p>
{audiocard(["23.2"])}
{sub("A", "Listen and repeat. Then say the prices of three things you bought this week.", "4 min", "23.2")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.55">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S232))}</p>""",
    22, """<ol><li>A: <i>checking account</i> (US) = <i>current account</i> (UK); <i>savings account</i> earns <i>interest</i>.</li>
<li>Pronunciation: British speakers say <i>two hundred <b>and</b> eighty</i>; both are correct.</li></ol>""")

    # Page 6 - Practice
    pc = [(["in case", "unless"], "in case"), (["unless", "as long as"], "unless"), (["as long as", "in case"], "as long as"), (["Otherwise", "Unless"], "Otherwise"),
          (["in case", "if"], "in case"), (["unless", "in case"], "unless")]
    p = [ch(o, a) for o, a in pc]
    rw = [("Don't use that ATM if it isn't inside a bank. (unless)", "Don't use that ATM unless it's inside a bank."), ("Bring your passport. Maybe they'll ask for ID. (in case)", "Bring your passport in case they ask for ID."),
          ("You can borrow my card, but only if you pay me back tomorrow. (as long as)", "You can borrow my card as long as you pay me back tomorrow."),
          ("Check the fees first. If you don't, you'll pay too much. (otherwise)", "Check the fees first. Otherwise, you'll pay too much."), ("I won't change money if the rate isn't good. (unless)", "I won't change money unless the rate is good.")]
    rwl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw)
    b.page(f"""{sec(6, "Practice", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Ana sends Danny some money tips for his trip. Choose the correct words.", "4 min")}</div>{img('D', 30, 20)}</div>
<div class="box" style="line-height:1.95;font-size:9pt"><b>From: Ana · To: Danny</b><br>Danny, I heard about the ATM! A few tips for your trip: take two cards {p[0]} one gets blocked again, and keep them in different places. Don't take out cash {p[1]} you really need it, because every withdrawal has a fee. You can pay by card almost everywhere, {p[2]} you check the fees with your bank first. Add the travel notice tonight. {p[3]}, you'll have the same problem in Argentina! Take a photo of your passport {p[4]} you lose it. And buy a local SIM card, {p[5]} you want to pay a lot for roaming! Have fun! Ana</div>
{sub("B", "Rewrite the sentences with the word in brackets.", "4 min")}
<ol style="line-height:1.55;font-size:8.8pt;margin:0">{rwl}</ol>""",
    24, """<ol><li>A: in the last gap, <i>unless you want to pay a lot</i> = if you don't want to pay a lot (Ana is joking). <i>Roaming</i> = using your phone plan abroad.</li>
<li>B: in 5, the positive verb after <i>unless</i> (<i>is good</i>) replaces the negative.</li></ol>""")

    # Page 7 - Speaking
    b.page(f"""{sec(7, "Speaking: at the bank", "12 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>exchange office</th><th>at the bank</th><th>a card problem</th><th>tips</th></tr>
<tr><td><i>I'd like to change… into… · What's the exchange rate? · Do you charge commission? · In twenties, please.</i></td><td><i>I'd like to check my balance. · Can I take out…? · I'd like to open an account.</i></td><td><i>My card was blocked / kept / stolen. · Could you freeze it? · How long will a new one take?</i></td><td><i>…in case… · …unless… · …as long as… · Otherwise…</i></td></tr></table></div>
{sub("A", "Role-plays. You are the customer; your teacher is the clerk or the agent. Then change roles.", "6 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0"><li>At an exchange office abroad: change 200 dollars into the local currency. Ask about the rate and commission.</li><li>At the bank counter: the ATM outside isn't working. Check your balance and take out some cash.</li><li>On the phone: your credit card was stolen on vacation. Freeze it and ask for a new one.</li></ol>
<p style="margin:.3mm 0;font-size:8.6pt">{R("Teacher's card: 1 the rate is 'X to the dollar' (invent it), commission 3%, ask for ID. 2 the customer is overdrawn: they can't take out cash unless they transfer money from savings. 3 security questions first; the new card takes 5 business days, as long as the address is correct.") if T else ""}</p>
{sub("B", "Long turn. Prepare for one minute, then talk for two minutes about how you manage money when you travel.", "4 min")}
<ul style="line-height:1.45;font-size:8.9pt;margin:0"><li>cash or cards? which cards?</li><li>a money problem you had (or heard about)</li><li>your best tips (use in case, unless, as long as)</li></ul>
{sub("C", "Talking point. Discuss with your teacher.", "2 min")}
<ol style="line-height:1.5;font-size:8.9pt;margin:0"><li>Will cash disappear in the future? Is that good or bad?</li><li>Should schools teach children how to manage money?</li></ol>""",
    30, """<ol><li>A: follow the teacher's card; push the student to ask questions and to use the target words in tips.</li>
<li>B: don't interrupt; note mistakes for the error log (page 8), especially <i>unless … don't</i> and <i>take money</i>.</li></ol>""")

    # Page 8 - Wrap-up
    cd = ["I can change money and talk about exchange rates.", "I can solve a card problem at the bank or on the phone.", "I can give tips with unless, as long as, in case and otherwise."]
    cdr = "".join(f"<tr><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for s in cd)
    b.page(f"""{sec(8, "Wrap-up and homework", "4 min")}
{sub("A", "Can-do check", "1 min")}
<table class="ck" style="font-size:8.6pt"><tr><th>In English…</th><th style="width:16mm">Easy!</th><th style="width:16mm">Sometimes</th><th style="width:16mm">Not yet</th></tr>{cdr}</table>
{sub("B", "My language notes. Write three corrections from today's class.", "2 min")}
<div style="display:flex;gap:5mm;font-size:8.6pt"><div style="flex:1"><b>I said…</b>{lines(3)}</div><div style="flex:1"><b>Better:</b>{lines(3)}</div></div>
{sub("C", "Homework: writing (100–150 words)", "1 min")}
<p style="margin:.3mm 0"><b>Money tips for travelers.</b> Write a short post for a travel forum with your best money tips. Read Danny's post first.</p>
<div class="box" style="font-size:8.6pt;line-height:1.4;margin:.5mm 0"><b>Gap Year Diaries · Five money lessons I learned the hard way</b><br><i>Last week, an ATM in São Paulo kept my debit card, and I learned a lot! First, always travel with two cards and keep them in different places, in case one gets blocked or lost. Second, tell your bank your travel dates. Otherwise, the system might think it's fraud. Third, don't take out cash with a credit card unless it's an emergency, because the fees are high. Fourth, use ATMs inside banks if you can. I feel safer there, and if there's a problem, someone can help you. Finally, save your bank's phone number on your phone and on paper. You can solve most problems in ten minutes, as long as you stay calm. What are your tips?</i></div>
<p class="small" style="margin:.3mm 0">Checklist: ☐ an introduction &nbsp;☐ four or five tips &nbsp;☐ unless, in case, as long as, otherwise &nbsp;☐ a question for readers &nbsp;☐ 100–150 words</p>
{lines(5)}""",
    30, """<ol><li>B (error log): during the lesson, note 3–5 real mistakes. Here, the student writes what they said and the better version; guide them to self-correct first.</li>
<li>C: check the linkers and the sequence words (<i>First, Second, Finally</i>).</li></ol>""")

    script = "".join(f"<p style='margin:.5mm 0'><b>{l.split(': ', 1)[0]}:</b> {l.split(': ', 1)[1]}</p>" for l in S231)
    b.extra("Audio script", f"""
{sub("23.1", "The ATM kept my card (natural and slow)")}
<div style="line-height:1.3;font-size:8.6pt">{script}</div>
{sub("23.2", "Repeat: money amounts")}
<p>{" · ".join(S232)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 23 - Money and banking")
