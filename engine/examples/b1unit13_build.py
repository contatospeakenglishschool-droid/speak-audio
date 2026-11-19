# Speak! Progress B1 - Unit 13 "Health and illness" (all English) - lean B1 format (rebuilt 2026-11-19)
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
setup(band="B1 · UNIT 13", audio_json="audio_b1-unit-13.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-13"]
S131 = [l.replace("thirty-eight point nine", "38.9") for l in _r["13.1 A call to Dr. Ana"].split("\n")]
S132 = [x.split(": ", 1)[1] for x in _r["13.2 Repeat: health words"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'

    # 1 Warm-up
    cover = cover_html(T, "LEVEL B1 · UNIT 13", "Health and illness", "Symptoms, remedies and injuries · <b>giving advice: should, ought to, had better</b>",
                       [("YOU CAN", "describe symptoms, understand a doctor's advice and give advice from soft to strong"),
                        ("LANGUAGE", "a sore throat · I keep sneezing · a decongestant · twist your ankle · You'd better rest."),
                        ("PRONUNCIATION", "-ache /eɪk/ and tricky health words")])
    kw = [("to blow air out of your nose suddenly and loudly", "sneeze"), ("to push air out of your throat with a short, loud sound", "cough"),
          ("when your throat hurts and it's difficult to swallow", "a sore throat"), ("when liquid keeps coming out of your nose", "a runny nose"),
          ("a body heat higher than normal (also called a fever)", "a temperature"), ("a general pain in your stomach, often after bad food", "an upset stomach")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:22mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Warm-up: feeling under the weather", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["Look at the photo. What do you think is wrong with her?", "When you get sick, do you go to work or stay at home? Why?", "Do you prefer home remedies (tea, soup, rest) or medicine from the pharmacy?"], "START TALKING")}</div></div>
{sub("A", "Key words. Symptoms. Write the words from the box next to the definitions.", "3 min")}
<div class="bank">cough · a runny nose · sneeze · a sore throat · a temperature · an upset stomach</div>
<div style="font-size:8.6pt">{twocol(kwl, 3)}</div>
{talk(["Which symptoms do people usually have with a cold? And with food poisoning?", "When did you last have a sore throat or a temperature? What did you do?"], "USE THE WORDS")}""",
    26, """<ol><li>Top box: <i>feel under the weather</i> = feel a little sick (informal). Keep it light; the student doesn't need to share private health details.</li>
<li>A: <i>I've got / I have</i> + symptom noun (<i>a sore throat</i>) and <i>I keep</i> + -ing (<i>I keep sneezing</i>).</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Phone call: Danny has the flu and calls Ana · symptoms · Talk about it", "Giving advice: should, ought to, had better, If I were you",
                      "Soft or strong advice? · choose the rule · Use it (oral)", "Functional language · health words (13.2) · pharmacy role-play",
                      "Bruno's message about his ankle · remedies · word choice · writing"),
        "The Linguahouse lesson is vocabulary only (symptoms, conditions, remedies, injuries). Our listening is a phone call: Danny has the flu at the hostel, and Ana, a doctor in a São Paulo emergency department (B1 Unit 06), gives him advice. Mrs. Lima has made him soup again, Bruno wants to give him old antibiotics, and Danny has to cancel his Saturday tours with Carla at City Steps Tours. Bruno twisted his ankle at the running group. Ana's medical facts are general and verified: antibiotics act on bacteria, not on viruses such as the flu and colds; a cold is usually milder than the flu (U.S. Centers for Disease Control and Prevention, cdc.gov). Nothing in the unit is medical advice for a real student.",
        "Students say <i>I'm with a headache</i> (I have a headache), <i>I'm constipated</i> for a cold, use <i>remedy</i> for every medicine, and translate <i>injury</i> wrongly. In grammar, they say <i>had better to</i> and use <i>had better</i> for polite advice, where it can sound like a warning.",
        "Track 13.1 A call to Dr. Ana (natural and slow) · Track 13.2 Repeat: health words"))

    # 2 Listening
    gist = ["a cold", "the flu", "food poisoning"]
    sy = [("a sore throat", "✓"), ("a headache", "✓"), ("an upset stomach", "✗"), ("body aches", "✓"), ("a cough", "✓"), ("a temperature", "✓"), ("a blocked nose", "✓"), ("a runny nose", "✗")]
    syl = "".join(f'<span style="display:inline-block;width:36mm">☐ {s} {R(a) if T else ""}</span>' for s, a in sy)
    b.page(f"""{sec(2, "Listening: a call to Dr. Ana", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{audiocard(["13.1 · NATURAL", "13.1 · SLOW"])}
{sub("A", "Danny is sick and calls his friend Ana, a doctor. Listen. What does Ana think Danny has?", "2 min", "13.1")}
<p style="margin:.3mm 0;font-size:8.9pt">{ch(gist, gist[1])}</p></div>{img('B', 40, 27)}</div>
{sub("B", "Listen again. Check (✓) the symptoms Danny has.", "4 min")}
<div style="font-size:8.7pt;line-height:1.7">{syl}</div>
{talk(["Why does Ana say &ldquo;No!&rdquo; so strongly about the antibiotics?", "&ldquo;Of course she has!&rdquo; What does Ana think of Mrs. Lima?", "Do you ask friends for medical advice instead of seeing a doctor? Is it a good idea?"])}""",
    26, """<ol><li>A–B: 6 minutes. The flu starts suddenly, with a high temperature and body aches; a cold is slower and milder. Danny's nose is <i>blocked</i>, not <i>runny</i>.</li>
<li>Talk about it: 6 minutes. 1: antibiotics only work on bacteria; the flu is a virus. 2: she's very kind and always looks after Danny.</li></ol>""")

    # 3 Grammar reference
    lean.grammar_in_class(b, grammar_ref.advice_strong_soft)

    # 4 Practice
    fs = [("If I were you, I'd stay in bed for a few days.", "personal advice"), ("You'd better not take them.", "a strong warning"),
          ("Why don't you ask Mrs. Lima for some tea with honey?", "a friendly suggestion"), ("You ought to eat something.", "normal advice (= should)")]
    fsl = "".join(f"<li>{s} {A(a, 'min-width:30mm')}</li>" for s, a in fs)
    use = ["I've had a headache all week. What should I do?", "I can't sleep at night. Give me personal advice: <i>If I were you…</i>", "I want to go to work with a temperature of 39 °C. Warn me: <i>You'd better…</i>",
           "I've twisted my ankle. Give me a friendly suggestion: <i>Why don't you…?</i>", "Your teacher has a problem (a backache, stress…). Give advice in three different ways."]
    b.page(f"""{sec(4, "Practice: giving advice", "10 min")}
{sub("A", "Sentences from the call. Write: a friendly suggestion, normal advice, personal advice or a strong warning.", "3 min")}
<ol style="line-height:1.75;font-size:8.9pt;margin:0">{fsl}</ol>
{sub("B", "Choose.", "1 min")}
<p style="margin:.3mm 0;font-size:8.9pt;line-height:1.7">You'd better {ch(["call", "to call"], "call")} the doctor. &nbsp;·&nbsp; {ch(["You'd better not go.", "You hadn't better go."], "You'd better not go.")}</p>
<div class="box sand"><h4>RULE</h4><b>should / ought to</b> + base form = normal advice · <b>Why don't you…? / You might want to…</b> = softer · <b>If I were you, I'd…</b> = personal · <b>had better ('d better)</b> + base form = a strong warning; negative <b>You'd better not…</b> See the <b>Grammar reference</b> on page 3.</div>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    24, """<ol><li>A–B: 4 minutes. Draw a scale from soft to strong. <i>Had better</i> looks past but refers to now; with bosses or strangers it can sound like a threat.</li>
<li>Use it: 6 minutes, all oral. Ask the student to give a reason with each piece of advice.</li></ol>""")

    # 5 Speaking
    b.page(f"""{sec(5, "Speaking: what's the matter?", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>ask</th><th>describe</th><th>advise</th><th>react</th></tr>
<tr><td><i>What's the matter? · How are you feeling? · How long have you had it?</i></td><td><i>I feel awful. · I've got a… · I keep… · It hurts when I…</i></td><td><i>It sounds like… · If I were you, I'd… · You'd better…</i></td><td><i>Poor you! · I hope you feel better soon. · Get well soon!</i></td></tr></table></div>
{audiocard(["13.2"])}
{sub("A", "Health words. Listen and repeat: ache /eɪk/ · cough /kɔːf/ · MEDicine · alLERgic.", "4 min", "13.2")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.55">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S132))}</p>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("B", "Role-play: at the pharmacy. You are the pharmacist. Your teacher is a customer. Ask questions and give advice. Then change roles: describe a cold, a migraine or an allergy.", "10 min")}
<p style="margin:.3mm 0;font-size:8.6pt">{R("Teacher's card: You've got a cough and a sore throat, and it's been three days. You have an important presentation tomorrow, and you want something strong to stop the cough. You're allergic to aspirin. You think you need antibiotics.") if T else ""}</p></div>{img('D', 32, 24)}</div>
{talk(["Tell me about a time you were sick or injured. Who looked after you?", "Do people in your country take too much medicine without a doctor?"])}""",
    28, """<ol><li>B: the pharmacist should notice the aspirin allergy and explain that antibiotics don't work for a cough caused by a virus.</li>
<li>Talk about it: the student can talk about a friend or relative. Last 3 minutes: wrap-up (two corrections and <i>Can you give advice from soft to strong?</i>).</li></ol>""")

    # H Homework
    pw = ["twisted", "swollen", "bruise", "ice pack", "painkillers", "crutches"]
    pc = [A(w, "min-width:16mm") for w in pw]
    rm = [("a decongestant", "a blocked nose"), ("a throat lozenge", "a sore throat"), ("tissues", "a runny nose")]
    rml = " &nbsp;·&nbsp; ".join(f"{r} → {A(p, 'min-width:22mm')}" for r, p in rm)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Bruno writes to the running group. Complete with bruise, crutches, ice pack, painkillers, swollen, twisted.", "")}</div>{img('C', 28, 18)}</div>
<div class="box" style="line-height:1.8;font-size:8.8pt;margin:.5mm 0">Hi guys! Bad news: on Sunday I stepped in a hole near the lake and {pc[0]} my ankle. By the evening it was really {pc[1]}, and today there's a huge purple {pc[2]} on it. Ana says nothing is broken, but I'd better rest it for two weeks. So now I'm on the sofa with an {pc[3]} and my foot up. I'm taking {pc[4]} because it still hurts. Fortunately, I don't need {pc[5]}. See you at the 10K in December... I hope!</div>
{sub("B", "Which problem is each remedy for?", "")}
<p style="margin:.3mm 0;line-height:1.9;font-size:8.6pt">{rml}</p>
{lean.watch_out([("I'm constipated. (with a cold)", "I've got a cold. My nose is blocked.", "<i>constipated</i> = you can't go to the bathroom!"), ("Did you take your remedy?", "Did you take your medicine?", "<i>remedy</i> = a treatment, often a home remedy."), ("I'm with a headache.", "I have / I've got a headache.", "symptoms take <i>have / have got</i>.")])}
{lean.writing_task(sub, "An email of advice: a friend has a health problem (they can't sleep, they have a backache, or they're always tired). Write with advice.", "Hi…! I'm sorry you still… If I were you, I'd… You'd better…", ["four advice forms", "a reason for each", "a friendly ending", "100–150 words"], "I can describe symptoms and give advice from soft to strong.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class. When you correct the writing, check the advice forms (no <i>to</i> after <i>had better</i> and <i>should</i>; <i>ought <b>to</b></i>).</p>""")

    script = "".join(f"<p style='margin:.6mm 0'><b>{l.split(': ', 1)[0]}:</b> {l.split(': ', 1)[1]}</p>" for l in S131)
    b.extra("Audio script", f"""
{sub("13.1", "A call to Dr. Ana (natural and slow)")}
<div style="line-height:1.35;font-size:8.7pt">{script}</div>
{sub("13.2", "Repeat: health words")}
<p>{" · ".join(S132)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 13 - Health and illness")
