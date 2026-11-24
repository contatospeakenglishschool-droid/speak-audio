# Speak! Progress B1 - Unit 46 "Apologies, excuses and promises" (all English) - lean B1 format
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
setup(band="B1 · UNIT 46", audio_json="audio_b1-unit-46.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-46"]
S461 = [l.split(": ", 1) for l in _r["46.1 Four apologies"].split("\n")]
S462 = [x.split(": ", 1)[1] for x in _r["46.2 Repeat: apologies and promises"].split("\n")]


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
    cover = cover_html(T, "LEVEL B1 · UNIT 46", "<span style=\"font-size:.72em\">Apologies, excuses and promises</span>", "Saying sorry · <b>Sorry I'm late · I apologize for… · It won't happen again</b>",
                       [("YOU CAN", "apologize, make an excuse, accept or refuse an apology and make a promise"),
                        ("LANGUAGE", "apologize for · blame · forgive · make an excuse · regret · sorry about / for / to · I'll…"),
                        ("PRONUNCIATION", "sounding sincere: stress on SO sorry, aPOLogize, aGAIN")])
    kw = [("to stop being angry with somebody for something they did", "forgive somebody for"),
          ("to feel sorry about something you did or didn't do, and wish it were different", "regret"),
          ("to say that a person is responsible for something bad", "blame somebody for"),
          ("to give a reason why you did something wrong (maybe not the real one)", "make an excuse"),
          ("to say that you are sorry for something", "apologize for"),
          ("to make something clear by giving more details", "explain")]
    kwl = "".join(f'<li>{A(w, "min-width:34mm")} <span style="color:#6b7377">= {d}</span></li>' for d, w in kw)
    b.page(f"""{sec(1, "Warm-up: saying sorry", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 50, 34)}<div style="flex:1">
{talk(["Look at the photo. What happened? Who should apologize, and what should they say?", "Is it easy for you to say sorry? In which language is it easier?", "Do people apologize a lot where you live?"], "START TALKING")}</div></div>
{sub("A", "Key words. Write the words from the box next to the definitions.", "3 min")}
<div class="bank" style="font-size:8.6pt">{" · ".join(sorted(w for d, w in kw))}</div>
<ol style="font-size:8.7pt;line-height:1.75;margin:0">{kwl}</ol>
{talk(["When was the last time you had to apologize to somebody? Why?", "Has anyone ever blamed you for something that wasn't your fault?", "<i>The dog ate my homework</i> is a classic joke excuse. Did you make a lot of excuses as a child? Which ones?"], "USE THE WORDS")}""",
    28, """<ol><li>Top box: 3 minutes. Possible answers: somebody dropped or stepped on the phone; they should apologize and offer to pay for the repair.</li>
<li>A: 4 minutes with the questions. <i>make an excuse</i> often suggests the reason isn't completely true. Check the prepositions: <i>apologize for, blame somebody for, forgive somebody for</i>.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Four short scenes: Danny late for class, Bruno and the sandwich, a lost delivery, no fish at the restaurant · where, who, what for, accepted? · promises · Talk about it",
                      "sorry about / for / to / (that); apologize (to somebody) for; blame / forgive / thank somebody for + -ing; regret + -ing; promises with will", "Choose the correct form · match apologies and promises · Use it (oral)",
                      "apologies and promises (46.2) · role-plays: apologize, make an excuse, promise; the teacher decides to forgive or not", "Danny's complaint email · put a conversation in order · watch out · writing an apology email"),
        """The Linguahouse lesson has vocabulary (apologize, forgive, make an excuse, blame, explain, regret), six short dialogues in different places, a grammar focus on <i>sorry</i> and <i>apologize</i>, matching apologies with promises, and role-plays. We kept the structure and the grammar, with original dialogues about our characters. Story: (1) Danny is late for class at the language school because his bus broke down; the director (Studio-O) says his students are still arriving. (2) Bruno ate Danny's chicken sandwich from the hostel fridge; he buys Danny lunch. (3) Danny's lamp, ordered ten days ago with express delivery, went to the wrong address; the agent (Charon) sends a new one and refunds the delivery. (4) At a restaurant, the waiter (Charon) has no fish left for Carol; she has the chicken, and he brings a free dessert for Carol and Ana. No real-world facts are given.""",
        """<i>Excuse me</i> to apologize after a mistake (it's <i>Sorry</i>); <i>apologize you</i>; <i>explain me</i>; <i>sorry for to be</i>; <i>forgive me to forget</i>; <i>I promise I call</i> (no <i>will</i>). Pronunciation: a flat <i>sorry</i> sounds rude; stress <i>SO sorry</i> and let the voice fall.""",
        "Track 46.1 Four apologies (natural and slow; Danny, the director, Bruno, an agent, a waiter, Carol and Ana) · Track 46.2 Repeat: apologies and promises"))

    # Page 2 - Listening
    rows = [("1", "the language school", "Danny", "being late: his bus broke down", "yes"),
            ("2", "the hostel", "Bruno", "eating Danny's sandwich", "yes"),
            ("3", "on the phone", "the agent", "delivering the lamp to the wrong address", "not at first: Danny wants a refund"),
            ("4", "a restaurant", "the waiter", "having no fish left", "yes")]
    rt = "".join(f'<tr><td><b>{n}</b></td><td>{A(p, "min-width:20mm")}</td><td>{A(w, "min-width:14mm")}</td><td>{A(f, "min-width:30mm")}</td><td>{A(y, "min-width:12mm")}</td></tr>' for n, p, w, f, y in rows)
    qs = [("What does Danny promise the director?", "It won't happen again (and he'll call next time)."),
          ("How will Bruno make it up to Danny?", "He'll buy Danny lunch, anything he wants."),
          ("What will the company do?", "Send a new lamp tomorrow and refund the delivery."),
          ("What does the waiter offer?", "A free dessert.")]
    ql = "".join(f"<li>{q} {A(a, 'min-width:50mm')}</li>" for q, a in qs)
    b.page(f"""{sec(2, "Listening: four apologies", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Listen to four short scenes. Where are they? Who apologizes, and what for? Is the apology accepted?", "5 min")}
<table style="font-size:8.4pt;margin:.5mm 0"><tr><th></th><th>where?</th><th>who?</th><th>what for?</th><th>accepted?</th></tr>{rt}</table></div>{img('B', 30, 28)}</div>
{audiocard(["46.1 · NATURAL", "46.1 · SLOW"])}
{sub("B", "Listen again. What does each person promise or offer?", "3 min")}
<ol style="line-height:1.5;font-size:8.6pt;margin:0">{ql}</ol>
<p style="margin:.6mm 0;font-size:8.6pt"><b>Think about it:</b> Which apology is the most formal? Which words show it? {A("Scene 3: We sincerely apologize for…, sir, I understand.", "min-width:20mm")}</p>
{talk(["Which person in the scenes would you forgive fastest? Why?", "Have you ever had a problem with a delivery? What did the company do?", "What do you do when a restaurant makes a mistake with your order?"])}""",
    30, """<ol><li>A: play the natural version; play the slow one if needed. In scene 3, Danny accepts the solution in the end.</li>
<li>B: ask the student to repeat the exact apologies: <i>I'm so sorry I'm late. I have to apologize. I'm sorry to hear that. We sincerely apologize for the mistake. I'm sorry about that.</i> They come back on page 3.</li>
<li>Talk about it: 4 minutes. Accepting: <i>That's OK. Don't worry. It doesn't matter.</i> Refusing: <i>I'm afraid that's not good enough.</i></li></ol>""")

    # Page 3
    lean.grammar_in_class(b, grammar_ref.apologies_promises)

    # Page 4 - Practice
    pc = [("Sorry", ["to keep", "for keep"], "to keep", "you waiting."), ("We apologize", ["for", "about"], "for", "the delay."),
          ("I'm sorry", ["for losing", "to lose"], "for losing", "your book last week."), ("Don't blame Tom", ["of", "for"], "for", "the mistake. It wasn't his fault."),
          ("I really regret", ["not taking", "to not take"], "not taking", "the train."), ("Will you forgive me", ["for forgetting", "to forget"], "for forgetting", "your birthday?"),
          ("Could you explain", ["to me", "me"], "to me", "what happened?"), ("I promise I", ["call", "'ll call"], "'ll call", "you tomorrow.")]
    cl = "".join(f"<li>{a} {ch(o, r)} {z}</li>" for a, o, r, z in pc)
    ap = ["I apologize for breaking your window.", "Sorry I didn't call you today.", "I'm sorry, I left your dictionary at home.",
          "Sorry about the mess in your kitchen.", "I'm so sorry for losing the book you lent me.", "We apologize for not telling you about the new class time."]
    pr = ["I'll buy you a new one.", "I'll clean it up right now.", "I'll call you first thing tomorrow.", "I'll pay for the damage.",
          "We'll make sure to contact you next time.", "I won't forget to bring it next time."]
    order = [4, 3, 0, 5, 1, 2]  # letters a-f show these promises; apology i matches promise i
    letter = {o: "abcdef"[k] for k, o in enumerate(order)}
    key = {0: 3, 1: 2, 2: 5, 3: 1, 4: 0, 5: 4}  # apology -> promise
    apl = "".join(f'<li>{x} {A(letter[key[i]], "min-width:6mm")}</li>' for i, x in enumerate(ap))
    prl = "".join(f'<div><b>{"abcdef"[k]}</b>&nbsp; {pr[o]}</div>' for k, o in enumerate(order))
    use = ["Is there anything you regret doing, or not doing, last year?", "Is it easy for you to forgive people? Who do you forgive fastest?",
           "What's the worst excuse you've ever heard at work or school?", "Have you ever made a promise you couldn't keep?", "Who apologizes more in your family?"]
    b.page(f"""{sec(4, "Practice: sorry for or sorry to?", "10 min")}
{sub("A", "Choose the correct words.", "3 min")}
<ol style="line-height:1.7;font-size:8.7pt;margin:0;columns:2;column-gap:6mm">{cl}</ol>
{sub("B", "Match the apologies (1–6) with the promises (a–f).", "3 min")}
<div style="display:flex;gap:5mm;font-size:8.5pt"><ol style="flex:1.1;margin:0;line-height:1.5">{apl}</ol><div style="flex:1;line-height:1.5">{prl}</div></div>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    30, """<ol><li>A: 3 minutes. Item 1: <i>sorry to</i> for something happening now. Item 8: a promise needs <i>will</i>.</li>
<li>B: this is the Linguahouse matching task. Ask: which apologies are more formal? (<i>I apologize, We apologize</i>.)</li>
<li>Use it: 4 minutes, all oral. Listen for <i>regret + -ing</i> and <i>forgive somebody for</i>.</li></ol>""")

    # Page 5 - Speaking
    sit = ["You borrowed your teacher's book and lost it. Apologize and promise something.",
           "Your teacher says you ate the sandwich they left in the fridge. Explain that it wasn't you.",
           "You missed a meeting with your teacher yesterday. Apologize and make an excuse.",
           "You stepped on your teacher's phone and cracked the screen. Apologize, explain and promise."]
    sl = "".join(f"<li>{x}</li>" for x in sit)
    card = f"""<div class="box" style="margin-top:1mm;font-size:8.2pt">{R("<b>Teacher's card (B):</b> react naturally. Accept two apologies (<i>Don't worry about it. / It doesn't matter.</i>) and refuse one (<i>I'm afraid that's not good enough. / That isn't a good excuse!</i>): the student must try again with a better promise. In situation 2, don't believe the student at first. Then swap: you apologize for being late for class, and the student decides.")}</div>""" if T else ""
    b.page(f"""{sec(5, "Speaking: I'm so sorry!", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.2pt"><tr><th>apologizing</th><th>excuses and explaining</th><th>accepting / refusing</th><th>promising</th></tr>
<tr><td><i>I'm so sorry about… · I'm really sorry I… · I'd like to apologize for…</i></td><td><i>You see, … · It's just that… · It wasn't me, I promise! · I didn't mean to.</i></td><td><i>Don't worry about it. · It doesn't matter. · I'm afraid that's not good enough.</i></td><td><i>It won't happen again. · I'll make it up to you. · I promise I'll…</i></td></tr></table></div>
{audiocard(["46.2"])}
{sub("A", "Listen and repeat. Sound sincere: I'm SO sorry · It won't happen aGAIN.", "3 min", "46.2")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S462))}</p>
{sub("B", "Role-plays. Do each situation with your teacher. Your teacher decides: forgive you or not?", "10 min")}
<ol style="line-height:1.5;font-size:8.6pt;margin:0">{sl}</ol>{card}
{talk(["What's the hardest apology you've ever had to make? Did the person forgive you?"], "TALK ABOUT IT")}""",
    30, """<ol><li>A: a flat, quick <i>sorry</i> sounds rude. Model a slow fall on <i>SO sorry</i>.</li>
<li>B: the Linguahouse role-plays, adapted for 1:1. Push for three parts: apology + excuse or explanation + promise. Last 3 minutes: wrap-up (two corrections, and ask <i>Can you now apologize and make a promise?</i>).</li></ol>""")

    # Homework
    pc2 = [(["about", "for"], "about"), (["for", "about"], "for"), (["would", "will"], "would"), (["to say", "for say"], "to say"),
           (["for", "of"], "for"), (["to me", "me"], "to me")]
    p = [ch(o, a) for o, a in pc2]
    conv = ["I was stuck in a traffic jam on the bridge. I really regret not taking the subway!", "Thanks for your understanding. It won't happen again.",
            "I'm so sorry for arriving late this morning.", "Oh, don't blame yourself. We're all late sometimes.", "Don't worry about it. What happened?"]
    cnum = {0: 3, 1: 5, 2: 1, 3: 4, 4: 2}
    cvl = "".join(f'<li style="list-style:none">{A(str(cnum[i]), "min-width:6mm")} {x}</li>' for i, x in enumerate(conv))
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "The new lamp didn't arrive either. Danny writes to the company. Choose the correct words.", "")}</div>{img('C', 30, 19)}</div>
<div class="box" style="line-height:1.85;font-size:8.7pt;margin:.5mm 0"><b>Dear Customer Service,</b> I am writing {p[0]} my order of a desk lamp. On Monday your agent apologized {p[1]} delivering it to the wrong address and promised that a new lamp {p[2]} arrive the next day. I'm sorry {p[3]} that it still hasn't arrived. I don't want to blame your drivers {p[4]} this, but I paid for express delivery. Could you please explain {p[5]} what happened? I would like a full refund. Sincerely, Danny</div>
{sub("B", "Put the conversation in order (1–5).", "")}
<ol style="line-height:1.45;font-size:8.6pt;margin:0;padding-left:2mm">{cvl}</ol>
{lean.watch_out([("Excuse me, I'm late!", "Sorry I'm late!", "<i>Excuse me</i> = before (attention); <i>Sorry</i> = after a mistake."), ("I apologize you.", "I apologize to you. / I apologize.", "<i>apologize to</i> somebody <i>for</i> something."), ("Explain me the problem.", "Explain the problem to me.", "<i>explain</i> something <i>to</i> somebody.")])}
{lean.writing_task(sub, "You missed a good friend's birthday party. Write an email to apologize.", "Dear …, I'm so sorry I missed your party on Saturday.", ["an apology with sorry or apologize", "an excuse or an explanation", "something you regret", "a promise: I'll make it up to you…", "100–150 words"], "I can apologize, make an excuse, accept or refuse an apology and make a promise.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class. In A, <i>promised that a new lamp would arrive</i>: <i>will</i> becomes <i>would</i> in a reported promise. B is the Linguahouse optional extension. Read the writing at home and choose two mistakes to discuss in class.</p>""")

    script = "".join((f"<p style='margin:1mm 0 .3mm'><b>Scene {t.rstrip('.')}</b></p>" if s == "Narrator" else f"<p style='margin:.4mm 0'><b>{s}:</b> {t}</p>") for s, t in S461)
    b.extra("Audio script", f"""
{sub("46.1", "Four apologies (natural and slow)")}
<div style="line-height:1.3;font-size:8.4pt">{script}</div>
{sub("46.2", "Repeat: apologies and promises")}
<p>{" · ".join(S462)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 46 - Apologies, excuses and promises")
