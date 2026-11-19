# Speak! Progress B1 - Unit 22 "Refunds and exchanges" (all English) - lean B1 format (rebuilt 2026-11-19)
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
    def _fill(s, a):
        for x in a.split(" / "):
            s = s.replace("___", A(x, "min-width:12mm"), 1)
        return s

    # 1 Warm-up
    cover = cover_html(T, "LEVEL B1 · UNIT 22", "Refunds and exchanges", "Returning things in a store · <b>reported speech: she said it was…, he told me he would…</b>",
                       [("YOU CAN", "return a product, explain the problem, ask for a refund or an exchange, and report what people said"),
                        ("LANGUAGE", "faulty · cracked · a refund · a replacement · store credit · proof of purchase · She told me she could…"),
                        ("PRONUNCIATION", "weak forms in reported speech: that /ðət/, he'd, could")])
    rr = [("incorrect size", "I ordered these jeans in my size, but they're too tight."), ("not working properly", "The hair dryer stopped after five minutes."),
          ("missing part", "I counted all the pieces in the box. One was missing."), ("wrong product", "I ordered the newest model, but this is the old one.")]
    rrl = "".join(f'<li>"{s}" {A(r, "min-width:30mm")}</li>' for r, s in rr)
    b.page(f"""{sec(1, "Warm-up: taking it back", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["Is it easy to return a product to a store in your country?", "Do you keep receipts? Where?", "Have you ever returned something you bought online?"], "START TALKING")}</div></div>
{sub("A", "Why are they returning it? Write a reason from the box.", "3 min")}
<div class="bank">incorrect size · missing part · not working properly · wrong product</div>
<ol style="line-height:1.6;font-size:8.6pt;margin:0">{rrl}</ol>
{talk(["Can you think of other reasons to return something?", "What's the worst thing you've ever bought?"], "USE THE WORDS")}""",
    26, """<ol><li>Top box: 4 minutes.</li>
<li>A: <i>properly</i> = correctly, well. Other reasons: <i>It's damaged. It's the wrong color. I changed my mind.</i></li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Carol returns a dress in Orlando, then leaves Ana a voice message · complete · Talk about it", "Reported speech: statements, say and tell",
                      "What did they say? · choose · Use it (oral)", "Functional language · weak forms (22.2) · returning items role-plays",
                      "Danny's message about his headphones · problems with products · word choice · writing"),
        "The Linguahouse listening is a generic dialogue in a UK clothes shop. Our listening happens in the US: Carol (Leda), Ana's cousin in Orlando, returns a dress she bought for her friend Linda's wedding in Miami (B1 Unit 21). The zipper broke; she has no receipt, but she paid by card, so the clerk (Studio-O) finds the purchase and gives her a refund. Then Carol tells Ana about it in a voice message, using reported speech. The store is fictional. Verified facts: in the US, no federal law requires stores to give refunds for items that are not defective; each store sets its own return policy, and it must follow the policy it posts (FindLaw; California and Washington Attorneys General). In Brazil, the Consumer Protection Code (art. 49) gives 7 days to cancel purchases made outside the store, for example online; in a physical store, exchanging a product that is not defective is a courtesy, not an obligation. In the homework, Danny reports a call with an online store about faulty headphones.", 'Students say <i>She said me</i> and <i>He told that</i>, and keep <i>will / can</i> in reported speech. False friends: <i>devolution</i> (return), <i>defected</i> (defective / faulty), <i>reclamation</i> (complaint), <i>the note</i> (the receipt).',
        "Track 22.1 A broken zipper (natural and slow) · Track 22.2 Repeat: weak forms in reported speech"))

    # 2 Listening
    gist = ["a replacement", "a refund", "store credit"]
    gp = [("The zipper broke the first time she ___ the dress ___ at home.", "tried / on"), ("The clerk says the dress is definitely ___.", "faulty"),
          ("Do you have the receipt or any other ___?", "proof of purchase"), ("If you paid by card, I can find the purchase in the ___.", "system"),
          ("The money will go back to your card in three to five ___.", "business days"), ("Our return ___ is 30 days.", "policy")]
    gpl = "".join(f"<li>{_fill(s, a)}</li>" for s, a in gp)
    b.page(f"""{sec(2, "Listening: a broken zipper", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{audiocard(["22.1 · NATURAL", "22.1 · SLOW"])}
{sub("A", "Carol, Ana's cousin, takes a dress back to a store in Orlando. Listen. What does she get?", "2 min", "22.1")}
<p style="margin:.3mm 0;font-size:8.9pt">{ch(gist, "a refund")}</p></div>{img('B', 40, 27)}</div>
{sub("B", "Listen again and complete.", "4 min")}
<ol style="line-height:1.55;font-size:8.6pt;margin:0;columns:2;column-gap:5mm">{gpl}</ol>
{talk(["Why doesn't Carol want a replacement?", "Would a store in your country give a refund without a receipt?", "In Carol's voice message, what did the clerk say? Tell your teacher."])}""",
    26, """<ol><li>A–B: 6 minutes. <i>Business days</i> = Monday to Friday. <i>Proof of purchase</i> = a receipt, a card statement or an order email.</li>
<li>Talk about it: 6 minutes. 1: she needs the dress next week, and she doesn't like green. 3 prepares the grammar: <i>She said she could…</i></li></ol>""")

    # 3 Grammar reference
    lean.grammar_in_class(b, grammar_ref.reported_statements)

    # 4 Practice
    rs = [("\"It's no problem.\"", "She said it ___ no problem.", "was"), ("\"I can find the purchase in the system.\"", "She said she ___ find the purchase.", "could"),
          ("\"The money will go back to your card.\"", "She told me the money ___ go back to my card.", "would"), ("\"I threw the receipt away.\"", "I said I ___ the receipt away.", "had thrown")]
    rsl = "".join(f"<li>{d} → <i>{r.replace('___', A(a, 'min-width:16mm'))}</i></li>" for d, r, a in rs)
    use = ["What did your boss or teacher say to you this week?", "Report something a friend told you recently.", "Your teacher says three sentences. Report them: <i>You said…</i>",
           "What did the weather forecast say about tomorrow?", "Tell me about a phone call with a company. What did they tell you?"]
    b.page(f"""{sec(4, "Practice: reported speech", "10 min")}
{sub("A", "What did they say? Complete the reported sentences from Carol's voice message.", "3 min")}
<ol style="line-height:1.85;font-size:8.8pt;margin:0">{rsl}</ol>
{sub("B", "Choose.", "1 min")}
<p style="margin:.3mm 0;font-size:8.9pt;line-height:1.7">She {ch(["told me", "said me"], "told me")} the dress was faulty. &nbsp;·&nbsp; They said they {ch(["couldn't", "can't"], "couldn't")} help.</p>
<div class="box sand"><h4>RULE</h4>One step back in time: <b>is → was · want → wanted · can → could · will → would · bought → had bought</b>. <b>say (that)</b> + clause; <b>tell + person</b> + (that) + clause. Change pronouns: <i>"I…" → she…</i> See the <b>Grammar reference</b> on page 3.</div>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    24, """<ol><li>A–B: 4 minutes. Write direct and reported sentences in two columns and underline the verbs.</li>
<li>Use it: 6 minutes, all oral. Correct <i>said me</i> and <i>told that</i> every time.</li></ol>""")

    # 5 Speaking
    it = ["headphones bought online 5 days ago: only one side works", "a mug that arrived cracked", "a sweater (a gift) that is too small: no receipt", "a hair dryer that stopped working after a week"]
    itl = "".join(f"<li>{x}</li>" for x in it)
    b.page(f"""{sec(5, "Speaking: I'd like to return this", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>explaining the problem</th><th>asking for options</th><th>the clerk</th><th>reporting it later</th></tr>
<tr><td><i>I'd like to return this. · It's faulty / cracked. · It doesn't work properly.</i></td><td><i>Could I get a refund? · Can I exchange it? · What are my options?</i></td><td><i>Do you have proof of purchase? · We can offer you…</i></td><td><i>She said… · He told me… · They said they'd…</i></td></tr></table></div>
{audiocard(["22.2"])}
{sub("A", "Weak forms. Listen and repeat: She said that /ðət/ it was BROken.", "4 min", "22.2")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.55">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S222))}</p>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("B", "Role-plays. You are the customer; your teacher is the clerk. Return the items. After each one, report what the clerk said. Then change roles.", "10 min")}
<ol style="line-height:1.45;font-size:8.8pt;margin:0;columns:2">{itl}</ol>
<p style="margin:.3mm 0;font-size:8.5pt">{R("Teacher's card: 1 online: refund OK; you'll send a return label. 2 a replacement, not a refund. 3 no receipt: store credit only. 4 the warranty covers repairs, not refunds.") if T else ""}</p></div>{img('D', 28, 28)}</div>
{talk(["Should stores accept returns when the customer just changed their mind?", "Online or in person: where is it easier to return things?"])}""",
    28, """<ol><li>B: after each role-play, the student reports: <i>You said you could only give me store credit.</i></li>
<li>Talk about it: share the facts in the story box (US store policies; Brazil's 7-day right for online purchases). Last 3 minutes: wrap-up.</li></ol>""")

    # H Homework
    pc = [(["told", "said"], "told"), (["would", "will"], "would"), (["said", "told"], "said"), (["needed", "need"], "needed"), (["could", "can"], "could")]
    p = [ch(o, a) for o, a in pc]
    pw = [("not working properly", "faulty"), ("with thin lines on the surface, but not in pieces", "cracked"), ("marked by something sharp", "scratched")]
    pwl = "".join(f"<li>{d} {A(w, 'min-width:18mm')}</li>" for d, w in pw)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Danny writes to Bruno about some headphones he bought online. Choose the correct words.", "")}</div>{img('C', 28, 18)}</div>
<div class="box" style="line-height:1.8;font-size:8.8pt;margin:.5mm 0"><b>From: Danny · To: Bruno</b><br>Hey Bruno! The left side of my new headphones stopped working, so I called the store. The woman {p[0]} me that they {p[1]} send me a new pair. She {p[2]} that I didn't have to pay for shipping. I told her I {p[3]} them before my trip, and she said she {p[4]} send them by express delivery. Danny</div>
{sub("B", "What's wrong with it? Write cracked, faulty or scratched.", "")}
<ol style="line-height:1.5;font-size:8.6pt;margin:0">{pwl}</ol>
{lean.watch_out([("I want to make a devolution.", "I'd like to return this.", "we <i>return</i> things."), ("The product is defected.", "The product is defective / faulty.", "<i>defect</i> as a verb = leave your country."), ("I lost the note.", "I lost the receipt.", "a <i>note</i> is a short message.")])}
{lean.writing_task(sub, "A complaint email to an online store: explain what you bought, what's wrong, what you'd like them to do, and when.", "Dear Customer Service, I'm writing about the… I ordered on… After two days,…", ["the problem", "what you've tried", "what you want and by when", "100–150 words"], "I can return a product and report what people said.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class. When you correct the writing, check formal language (<i>I'm writing about…, I would be grateful if…</i>).</p>""")

    script = "".join(f"<p style='margin:.5mm 0'><b>{l.split(': ', 1)[0]}:</b> {l.split(': ', 1)[1]}</p>" if not l.startswith("Narrator") else f"<p style='margin:.5mm 0'><i>{l.split(': ', 1)[1]}</i></p>" for l in S221)
    b.extra("Audio script", f"""
{sub("22.1", "A broken zipper (natural and slow)")}
<div style="line-height:1.3;font-size:8.6pt">{script}</div>
{sub("22.2", "Repeat: weak forms in reported speech")}
<p>{" · ".join(S222)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 22 - Refunds and exchanges")
