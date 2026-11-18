# Speak! Progress B1 - Unit 22 "Refunds and exchanges" (all English) - B1 format (2026-11-18)
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Progress"
setup(band="B1 · UNIT 22", audio_json="audio_b1-unit-22.json", img_dir="img")


_r = json.load(open("roteiro.json"))["units"]["b1-unit-22"]
S221 = [l.replace("Seventy-nine ninety-nine", "$79.99").replace("thirty days", "30 days") for l in _r["22.1 A broken zipper"].split("\n")]
S222 = [x.split(": ", 1)[1] for x in _r["22.2 Repeat: weak forms in reported speech"].split("\n")]


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
    cover = cover_html(T, "LEVEL B1 · UNIT 22", "Refunds and exchanges", "Returning things in a store · <b>reported speech: she said it was…, he told me he would…</b>",
                       [("YOU CAN", "return a product, explain the problem, ask for a refund or an exchange, and report what people said"),
                        ("LANGUAGE", "faulty · cracked · a refund · a replacement · store credit · proof of purchase · She told me she could…"),
                        ("PRONUNCIATION", "weak forms in reported speech: that /ðət/, he'd, could")])
    rr = [("incorrect size", "I ordered these jeans in my size, but they're too tight."), ("not working properly", "The hair dryer stopped after five minutes, then turned back on."),
          ("missing part", "I counted all the pieces in the box. One was missing."), ("wrong product", "I ordered the newest model, but this is the old one."),
          ("didn't meet expectations", "I'm disappointed. I thought the game would be much better."), ("doesn't match the description", "The website mentioned extras that weren't in the package.")]
    rrl = "".join(f'<li>"{s}" {A(r, "min-width:34mm")}</li>' for r, s in rr)
    b.page(f"""{sec(1, "Warm-up: taking it back", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 46, 31)}<div style="flex:1">
{sub("A", "Discuss with your teacher.", "2 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0"><li>Is it easy to return a product to a store in your country?</li><li>Do you keep receipts? Where?</li><li>Have you ever returned something you bought online?</li></ol></div></div>
{sub("B", "Why are they returning it? Write a reason from the box.", "5 min")}
<div class="bank">didn't meet expectations · doesn't match the description · incorrect size · missing part · not working properly · wrong product</div>
<ol style="line-height:1.6;font-size:8.6pt;margin:0">{rrl}</ol>
{sub("C", "Can you think of other reasons to return something?", "1 min")}""",
    30, """<ol><li>B: point out <i>properly</i> (= correctly, well) and <i>meet expectations</i> (= be as good as you expected).</li>
<li>C: for example, <i>It's damaged. It's the wrong color. I changed my mind. It was a gift, and I already have one.</i></li></ol>""", cover=cover)

    b.extra("Lesson overview · 60 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Discussion · reasons to return a product</td><td>1</td></tr>
<tr><td>2 Listening</td><td>12 min</td><td>Carol returns a dress in Orlando, then leaves Ana a voice message</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>8 min</td><td>Reported speech: statements, say and tell</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Reported speech (study at home)</td><td>4</td></tr>
<tr><td>4 Vocabulary lab + pronunciation</td><td>8 min</td><td>Problems with products · options: refund, exchange, store credit · weak forms</td><td>5</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Danny's message about his headphones · reporting what people said</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Role-plays: returning items · long turn · talking point</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>4 min</td><td>Can-do · language notes · writing homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY</h4>The Linguahouse listening is a generic dialogue in a UK clothes shop. Our listening happens in the US: Carol (Leda), Ana's cousin in Orlando, returns a dress she bought for her friend Linda's wedding in Miami (B1 Unit 21). The zipper broke; she has no receipt, but she paid by card, so the clerk (Studio-O) finds the purchase and gives her a refund. Then Carol tells Ana about it in a voice message, using reported speech. The store is fictional. Verified facts: in the US, no federal law requires stores to give refunds for items that are not defective; each store sets its own return policy, and it must follow the policy it posts (FindLaw; California and Washington Attorneys General). In Brazil, the Consumer Protection Code (art. 49) gives 7 days to cancel purchases made outside the store, for example online; in a physical store, exchanging a product that is not defective is a courtesy, not an obligation. In the Practice, Danny reports a call with an online store about faulty headphones; the writing model is his complaint email.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students say <i>She said me</i> and <i>He told that</i>, and keep <i>will / can</i> in reported speech. False friends: <i>devolution</i> (return), <i>defected</i> (defective / faulty), <i>reclamation</i> (complaint), <i>the note</i> (the receipt).</div>
<div class="box"><h4>AUDIO</h4>Track 22.1 A broken zipper (natural and slow) · Track 22.2 Repeat: weak forms in reported speech</div>""")

    # Page 2 - Listening
    gist = ["a replacement", "a refund", "store credit"]
    gp = [("The zipper broke the first time she ___ the dress ___ at home.", "tried / on"), ("The clerk says the dress is definitely ___.", "faulty"),
          ("Would you like a ___? We have the same dress in green.", "replacement"), ("Do you have the receipt or any other ___?", "proof of purchase"),
          ("If you paid by card, I can find the purchase in the ___.", "system"), ("The money will go back to your card in three to five ___.", "business days"),
          ("Our return ___ is 30 days.", "policy"), ("…as long as they're ___ and you have the box.", "unworn")]
    def _fill(s, a):
        for x in a.split(" / "):
            s = s.replace("___", A(x, "min-width:12mm"), 1)
        return s
    gpl = "".join(f"<li>{_fill(s, a)}</li>" for s, a in gp)
    tf = [("Carol told the clerk she wanted a refund.", "T"), ("Carol still had the receipt.", "F (she'd thrown it away)"),
          ("The clerk said she couldn't find the purchase.", "F (she could, because Carol had paid by card)"), ("Carol can also return the shoes.", "T")]
    tfl = [f'<li value="{i+1}">{s} {A(a, "min-width:9mm")}</li>' for i, (s, a) in enumerate(tf)]
    b.page(f"""{sec(2, "Listening: a broken zipper", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{audiocard(["22.1 · NATURAL", "22.1 · SLOW"])}
{sub("A", "Carol, Ana's cousin, takes a dress back to a store in Orlando. Listen at natural speed. What does she get?", "2 min", "22.1")}
<p style="margin:.3mm 0;font-size:8.9pt">{ch(gist, "a refund")}</p></div>{img('B', 40, 27)}</div>
{sub("B", "Listen again and complete.", "4 min")}
<ol style="line-height:1.55;font-size:8.6pt;margin:0;columns:2;column-gap:5mm">{gpl}</ol>
{sub("C", "The voice message. True or false? Correct the false sentences.", "3 min")}
<div style="font-size:8.6pt">{twocol(tfl, 2)}</div>
{sub("D", "Think about it. Discuss with your teacher.", "3 min")}
<ol style="line-height:1.4;font-size:8.7pt;margin:0"><li>Why doesn't Carol want a replacement? {R("She needs the dress next week, and she doesn't like green.") if T else ""}</li><li>Would a store in your country give a refund without a receipt?</li></ol>
<div class="box sand" style="margin-top:1mm"><h4>NOTICE: USEFUL CHUNKS</h4><i>I'd like to return this. · I'm sorry to hear that. · That's the thing. · I just changed my mind. · as long as · You've been really helpful.</i></div>""",
    24, """<ol><li>B: <i>business days</i> = Monday to Friday. <i>Unworn</i> = not worn. <i>Proof of purchase</i> = a receipt, a card statement or an order email.</li>
<li>C: the voice message is the model for the Language focus: ask the student what Carol says the clerk said.</li></ol>""")

    # Page 3 - Language focus
    rs = [("\"It's no problem.\"", "She said it ___ no problem.", "was"), ("\"I can find the purchase in the system.\"", "She said she ___ find the purchase.", "could"),
          ("\"The money will go back to your card.\"", "She told me the money ___ go back to my card.", "would"), ("\"I want a refund.\"", "I told the clerk I ___ a refund.", "wanted"),
          ("\"I threw the receipt away.\"", "I said I ___ the receipt away.", "had thrown")]
    rsl = "".join(f"<li>{d} → <i>{r.replace('___', A(a, 'min-width:16mm'))}</i></li>" for d, r, a in rs)
    b.page(f"""{sec(3, "Language focus: reported speech", "8 min")}
{sub("A", "What did they say? Complete the reported sentences from Carol's voice message.", "3 min")}
<ol style="line-height:1.85;font-size:8.8pt;margin:0">{rsl}</ol>
{sub("B", "Complete the rules. Choose.", "3 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0"><li>After <i>said / told</i>, the present simple usually becomes the {ch(["past simple", "present perfect"], "past simple")}.</li>
<li><i>will</i> becomes {ch(["would", "will"], "would")}, and <i>can</i> becomes {ch(["could", "can"], "could")}.</li>
<li>The past simple often becomes the {ch(["past perfect", "present simple"], "past perfect")}: <i>I'd thrown it away</i>.</li>
<li>We use {ch(["tell", "say"], "tell")} + a person: <i>She told me…</i></li>
<li>After <i>said</i>, the word <i>that</i> is {ch(["optional", "necessary"], "optional")}.</li></ol>
{sub("C", "Correct or incorrect? Choose.", "2 min")}
<ol style="line-height:1.6;font-size:8.9pt;margin:0"><li>She said me the dress was faulty. {ch(["correct", "incorrect"], "incorrect")} {R("→ She told me / She said") if T else ""}</li><li>He told me he would call back. {ch(["correct", "incorrect"], "correct")}</li><li>They said they can't help. {ch(["correct", "incorrect"], "incorrect")} {R("→ couldn't") if T else ""}</li></ol>
<div class="box sand"><h4>RULE</h4>Reported speech: one step back in time: <b>is → was · want → wanted · can → could · will → would · bought / have bought → had bought</b>. <b>say (that)</b> + clause; <b>tell + person</b> + (that) + clause. Change pronouns: <i>"I…" → she…</i> More on the next page: <b>Grammar reference</b>.</div>""",
    27, """<ol><li>A: write the direct and reported sentences in two columns and underline the verbs.</li>
<li>B: if the information is still true, the tense can stay: <i>She said the return policy is 30 days.</i> Teach the backshift first; mention this later.</li></ol>""")

    grammar_ref.reported_statements(b)

    # Page 5 - Vocabulary lab
    pw = [("not working properly", "faulty"), ("broken or spoiled", "damaged"), ("with thin lines on the surface, but not in pieces", "cracked"),
          ("marked by something sharp", "scratched"), ("with some parts missing", "incomplete"), ("not good enough", "unsatisfactory")]
    pwl = [f'<li value="{i+1}">{d} {A(w, "min-width:20mm")}</li>' for i, (d, w) in enumerate(pw)]
    op = [("We can give you a ___ or store credit instead.", "refund"), ("It isn't working? Bring it back and we can ___ it.", "exchange"),
          ("You can get ___, but not your money back.", "store credit"), ("The washing machine has a two-year ___, so we'll fix it for free.", "warranty"),
          ("I don't want my money back. I want a ___. I love this bag!", "replacement")]
    opl = "".join(f"<li>{s.replace('___', A(a, 'min-width:18mm'))}</li>" for s, a in op)
    b.page(f"""{sec(4, "Vocabulary lab: problems and options", "4 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "What's wrong with it? Write the adjective.", "2 min")}
<div class="bank">cracked · damaged · faulty · incomplete · scratched · unsatisfactory</div></div>{img('C', 30, 20)}</div>
<div style="font-size:8.5pt">{twocol(pwl, 3)}</div>
{sub("B", "What can the store offer? Complete with exchange, refund, replacement, store credit or warranty.", "2 min")}
<ol style="line-height:1.55;font-size:8.6pt;margin:0">{opl}</ol>
<div class="box sand"><h4>WATCH OUT: FALSE FRIENDS AND WORD CHOICE</h4>
<table style="margin:0;font-size:8.2pt"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>I want to make a devolution.</td><td><b>I'd like to return this.</b></td><td>we <i>return</i> things; <i>devolution</i> is about political power.</td></tr>
<tr><td>The product is defected.</td><td><b>The product is defective / faulty.</b></td><td><i>defect</i> as a verb = leave your country or party.</td></tr>
<tr><td>I made a reclamation.</td><td><b>I made a complaint.</b></td><td><i>reclamation</i> = making land usable again.</td></tr>
<tr><td>I lost the note.</td><td><b>I lost the receipt.</b></td><td>a <i>note</i> is a short message; the paper from the store is a <i>receipt</i>.</td></tr></table></div>
{sec(5, "Pronunciation lab: weak forms in reported speech", "4 min")}
<p class="small" style="margin:.3mm 0">In reported speech, small words are weak: <i>that</i> /ðət/, <i>he'd</i> /hid/, <i>could</i> /kəd/, <i>was</i> /wəz/. The stress goes on the important information: <i>She said that it was <b>BRO</b>ken.</i></p>
{audiocard(["22.2"])}
{sub("A", "Listen and repeat. Then tell your teacher something a friend told you this week.", "4 min", "22.2")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.55">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S222))}</p>""",
    22, """<ol><li>A: <i>faulty</i> is for machines and electronics; <i>damaged</i> for anything broken or spoiled.</li>
<li>B: <i>warranty</i> (US) is more common than <i>guarantee</i> for products. <i>Exchange</i> = give it back and take another one.</li></ol>""")

    # Page 6 - Practice
    pc = [(["told", "said"], "told"), (["would", "will"], "would"), (["said", "told"], "said"), (["didn't have", "don't have"], "didn't have"),
          (["needed", "need"], "needed"), (["could", "can"], "could"), (["had", "has"], "had")]
    p = [ch(o, a) for o, a in pc]
    rp = [("The clerk: \"We don't have your size.\"", "The clerk said they didn't have my size."), ("Ana: \"I'll call you tomorrow.\"", "Ana told me she would call me the next day."),
          ("Bruno: \"I can't find the receipt.\"", "Bruno said he couldn't find the receipt."), ("Carol: \"I bought it on Saturday.\"", "Carol said she had bought it on Saturday."),
          ("The store: \"Your refund is being processed.\"", "The store told me my refund was being processed.")]
    rpl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rp)
    b.page(f"""{sec(6, "Practice", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Danny writes to Bruno about some headphones he bought online. Choose the correct words.", "4 min")}</div>{img('D', 30, 20)}</div>
<div class="box" style="line-height:1.95;font-size:9pt"><b>From: Danny · To: Bruno</b><br>Hey Bruno! Remember the headphones I ordered online? The left side stopped working after two days, so I called the store this morning. The woman {p[0]} me that they {p[1]} send me a new pair. She {p[2]} that I {p[3]} to pay for shipping. I told her I {p[4]} them before my trip, and she said she {p[5]} send them by express delivery. She also said they {p[6]} had a lot of problems with that model. So if you see a delivery guy at the hostel, it's for me! Danny</div>
{sub("B", "Report what they said. Start with said or told me.", "4 min")}
<ol style="line-height:1.55;font-size:8.8pt;margin:0">{rpl}</ol>""",
    24, """<ol><li>A: in the last gap, <i>had had</i> is correct: the past perfect of <i>have</i> ("We've had a lot of problems").</li>
<li>B: check the pronoun changes (<i>I → she, you → me</i>) and time words (<i>tomorrow → the next day</i>).</li></ol>""")

    # Page 7 - Speaking
    it = ["headphones bought online 5 days ago: only one side works", "a mug that arrived cracked", "a sweater (a gift) that is too small: no receipt", "a hair dryer that stopped working after a week"]
    itl = "".join(f"<li>{x}</li>" for x in it)
    b.page(f"""{sec(7, "Speaking: I'd like to return this", "12 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>explaining the problem</th><th>asking for options</th><th>the clerk</th><th>reporting it later</th></tr>
<tr><td><i>I'd like to return this. · It's faulty / cracked. · It doesn't work properly.</i></td><td><i>Could I get a refund? · Can I exchange it? · What are my options?</i></td><td><i>Do you have proof of purchase? · We can offer you…</i></td><td><i>She said… · He told me… · They said they'd…</i></td></tr></table></div>
{sub("A", "Role-plays. You are the customer; your teacher is the clerk. Return the items. Then change roles.", "6 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0;columns:2">{itl}</ol>
<p style="margin:.3mm 0;font-size:8.6pt">{R("Teacher's card: 1 online purchase: refund OK; you'll send a return label. 2 the store offers a replacement, not a refund. 3 no receipt: store credit only. 4 the warranty covers repairs, not refunds. After each role-play, ask the student to report what the clerk said.") if T else ""}</p>
{sub("B", "Long turn. Prepare for one minute, then talk for two minutes about a time you returned something (or wanted to).", "4 min")}
<ul style="line-height:1.45;font-size:8.9pt;margin:0"><li>what it was and what was wrong with it</li><li>what the store said</li><li>what the result was and how you felt</li></ul>
{sub("C", "Talking point. Discuss with your teacher.", "2 min")}
<ol style="line-height:1.5;font-size:8.9pt;margin:0"><li>Should stores accept returns when the customer just changed their mind?</li><li>Online or in person: where is it easier to return things?</li></ol>""",
    30, """<ol><li>A: follow the teacher's card. Then the student reports: <i>You said you could only give me store credit.</i></li>
<li>C: share the facts in the story box: US stores set their own return policies; in Brazil, online purchases can be cancelled within 7 days, but physical stores don't have to exchange products that aren't defective.</li></ol>""")

    # Page 8 - Wrap-up
    cd = ["I can return a product and explain what's wrong with it.", "I can ask for a refund, an exchange or store credit.", "I can report what people said (said / told me)."]
    cdr = "".join(f"<tr><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for s in cd)
    b.page(f"""{sec(8, "Wrap-up and homework", "4 min")}
{sub("A", "Can-do check", "1 min")}
<table class="ck" style="font-size:8.6pt"><tr><th>In English…</th><th style="width:16mm">Easy!</th><th style="width:16mm">Sometimes</th><th style="width:16mm">Not yet</th></tr>{cdr}</table>
{sub("B", "My language notes. Write three corrections from today's class.", "2 min")}
<div style="display:flex;gap:5mm;font-size:8.6pt"><div style="flex:1"><b>I said…</b>{lines(3)}</div><div style="flex:1"><b>Better:</b>{lines(3)}</div></div>
{sub("C", "Homework: writing (100–150 words)", "1 min")}
<p style="margin:.3mm 0"><b>A complaint email to an online store.</b> Explain what you bought, what's wrong, what you'd like them to do, and when. Read Danny's email first.</p>
<div class="box" style="font-size:8.6pt;line-height:1.4;margin:.5mm 0"><b>Subject: Faulty headphones, order #48213</b><br><i>Dear Customer Service, I'm writing about the wireless headphones I ordered from your website on November 10 (order #48213). They arrived on time, but after two days the left side stopped working. I've charged them fully and tried them with two different phones, so I'm sure the problem isn't the phone. Your website says that faulty products can be returned within 30 days. I would like a replacement pair, if possible. I'm traveling on December 5, so I would be grateful if you could send them before then. If a replacement isn't possible, I would like a full refund. I look forward to hearing from you. Best regards, Danny</i></div>
<p class="small" style="margin:.3mm 0">Checklist: ☐ what you bought and when &nbsp;☐ the problem &nbsp;☐ what you've already tried &nbsp;☐ what you want and by when &nbsp;☐ a polite ending &nbsp;☐ 100–150 words</p>
{lines(5)}""",
    30, """<ol><li>B (error log): during the lesson, note 3–5 real mistakes. Here, the student writes what they said and the better version; guide them to self-correct first.</li>
<li>C: check formal language (<i>I'm writing about…, I would be grateful if…, I look forward to hearing from you</i>) and the problem vocabulary.</li></ol>""")

    script = "".join(f"<p style='margin:.5mm 0'><b>{l.split(': ', 1)[0]}:</b> {l.split(': ', 1)[1]}</p>" if not l.startswith("Narrator") else f"<p style='margin:.5mm 0'><i>{l.split(': ', 1)[1]}</i></p>" for l in S221)
    b.extra("Audio script", f"""
{sub("22.1", "A broken zipper (natural and slow)")}
<div style="line-height:1.3;font-size:8.6pt">{script}</div>
{sub("22.2", "Repeat: weak forms in reported speech")}
<p>{" · ".join(S222)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 22 - Refunds and exchanges")
