# Speak! Progress B1 - Unit 13 "Health and illness" (all English) - B1 format (2026-11-09)
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Progress"
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
    def lines(n):
        return '<div class="wline"></div>' * n

    # Page 1 - Warm-up
    cover = cover_html(T, "LEVEL B1 · UNIT 13", "Health and illness", "Symptoms, remedies and injuries · <b>giving advice: should, ought to, had better</b>",
                       [("YOU CAN", "describe symptoms, understand a doctor's advice and give advice from soft to strong"),
                        ("LANGUAGE", "a sore throat · I keep sneezing · a decongestant · twist your ankle · You'd better rest."),
                        ("PRONUNCIATION", "-ache /eɪk/ and tricky health words")])
    kw = [("to blow air out of your nose suddenly and loudly, often with a cold", "sneeze"), ("to push air out of your throat with a short, loud sound", "cough"),
          ("when your throat hurts and it's difficult to swallow", "a sore throat"), ("when liquid keeps coming out of your nose", "a runny nose"),
          ("when your nose is full and you can't breathe through it", "a blocked nose"), ("a body heat higher than normal (also called a fever)", "a temperature"),
          ("a general pain in your stomach, often after bad food", "an upset stomach"), ("when you feel you're going to throw up", "feel like vomiting")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:22mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Warm-up: feeling under the weather", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 36)}<div style="flex:1">
{sub("A", "Discuss with your teacher.", "3 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0"><li>Look at the photo. What do you think is wrong with her?</li><li>When you get sick, do you go to work or stay at home? Why?</li><li>Do you prefer home remedies (tea, soup, rest) or medicine from the pharmacy?</li></ol></div></div>
{sub("B", "Key words. Symptoms. Write the words from the box next to the definitions.", "4 min")}
<div class="bank">a blocked nose · cough · an upset stomach · feel like vomiting · a runny nose · sneeze · a sore throat · a temperature</div>
<div style="font-size:8.6pt">{twocol(kwl, 4)}</div>
{sub("C", "Which symptoms do people usually have with a cold? And with food poisoning?", "1 min")}""",
    38, """<ol><li>A: <i>feel under the weather</i> = feel a little sick (informal). Keep it light; the student doesn't need to share private health details.</li>
<li>B: we say <i>I've got / I have</i> + symptom noun (<i>a sore throat, a temperature</i>) and <i>I keep</i> + verb-ing (<i>I keep sneezing</i>). <i>Throw up</i> = vomit (informal).</li>
<li>C: a cold: sneezing, a runny or blocked nose, a sore throat, a cough. Food poisoning: an upset stomach, feeling like vomiting, sometimes a temperature.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 60 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Discussion · key words: symptoms</td><td>1</td></tr>
<tr><td>2 Listening</td><td>12 min</td><td>Phone call: Danny describes his symptoms to Ana</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>8 min</td><td>Giving advice: from soft to strong</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Giving advice (study at home)</td><td>4</td></tr>
<tr><td>4 Vocabulary lab + pronunciation</td><td>8 min</td><td>Remedies · ache, hurt, pain · health words</td><td>5</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Bruno's message about his injury · advice for the characters</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Guess the illness · long turn · role-play at the pharmacy · talking point</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>4 min</td><td>Can-do · language notes · writing homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY</h4>The Linguahouse lesson is vocabulary only (symptoms, common conditions, remedies, injuries). Our original listening is a phone call: Danny has the flu at the hostel, and Ana, a doctor in a São Paulo emergency department (B1 Unit 06), gives him advice. Mrs. Lima has made him soup again (as in B1 Unit 02), Bruno wants to give him old antibiotics, and Danny has to cancel his Saturday tours with Carla at City Steps Tours (B1 Units 07–08). Bruno twisted his ankle at the running group (B1 Unit 05). Ana's medical facts are general and verified: antibiotics act on bacteria, not on viruses such as the flu and colds; a cold is usually milder than the flu (U.S. Centers for Disease Control and Prevention, cdc.gov). The writing model is Ana's email to her cousin Carol in Orlando (B1 Unit 04), who can't sleep. Nothing in the unit is medical advice for a real student.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students say <i>I'm with a headache</i> (I have a headache), <i>I'm constipated</i> for a cold (it means you can't go to the bathroom!), use <i>remedy</i> for every medicine, and translate <i>injury</i> wrongly. In grammar, they say <i>had better to</i> and use <i>had better</i> for polite advice, where it can sound like a warning or a threat.</div>
<div class="box"><h4>AUDIO</h4>Track 13.1 A call to Dr. Ana (natural and slow) · Track 13.2 Repeat: health words</div>""")

    # Page 2 - Listening
    gist = ["a cold", "the flu", "food poisoning"]
    sy = [("a sore throat", "✓"), ("a headache", "✓"), ("an upset stomach", "✗"), ("body aches", "✓"), ("sneezing", "✓"), ("a cough", "✓"),
          ("a temperature", "✓"), ("breathing problems", "✗"), ("a blocked nose", "✓"), ("a runny nose", "✗")]
    syl = "".join(f'<span style="display:inline-block;width:36mm">☐ {s} {R(a) if T else ""}</span>' for s, a in sy)
    adv = [("Bruno thinks Danny ought to take", "antibiotics"), ("Ana says Danny should stay in bed and drink lots of", "water"),
           ("For the throat, Ana suggests tea with", "honey"), ("Danny had better call Carla and cancel his", "tours"),
           ("Bruno should put an ice pack on his ankle and keep his", "foot up"), ("Danny should see a doctor if the fever doesn't go down in", "three days")]
    advl = [f'<li value="{i+1}">{s} {A(w, "min-width:16mm")}</li>' for i, (s, w) in enumerate(adv)]
    b.page(f"""{sec(2, "Listening: a call to Dr. Ana", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{audiocard(["13.1 · NATURAL", "13.1 · SLOW"])}
{sub("A", "Danny is sick and calls his friend Ana, a doctor. Listen at natural speed. What does Ana think Danny has?", "2 min", "13.1")}
<p style="margin:.3mm 0;font-size:8.9pt">{ch(gist, gist[1])}</p></div>{img('B', 40, 27)}</div>
{sub("B", "Listen again. Check (✓) the symptoms Danny has.", "3 min")}
<div style="font-size:8.7pt;line-height:1.7">{syl}</div>
{sub("C", "Complete the advice with one or two words.", "3 min")}
<div style="font-size:8.6pt">{twocol(advl, 3)}</div>
{sub("D", "Think about it. Discuss with your teacher.", "4 min")}
<ol style="line-height:1.4;font-size:8.8pt;margin:0"><li>Why does Ana say "No!" so strongly about the antibiotics? {R("They only work on bacteria; the flu is a virus, so they won't help. Taking old medicine without a doctor is a bad idea.") if T else ""}</li>
<li>"Of course she has!" What does Ana think of Mrs. Lima? {R("That she's very kind and always looks after Danny.") if T else ""}</li>
<li>Do you ever ask a friend or relative for medical advice instead of seeing a doctor? Is it a good idea?</li></ol>
<div class="box sand" style="margin-top:1mm"><h4>NOTICE: USEFUL CHUNKS</h4><i>How are you feeling? · I feel awful. · It sounds like… · Got it. · even if you're not hungry · Poor Bruno! · Promise?</i></div>""",
    23, """<ol><li>A: Ana explains the difference: the flu starts suddenly, with a high temperature and body aches; a cold is slower and milder.</li>
<li>B: Danny says his stomach is fine and he can breathe; his nose is <i>blocked</i>, not <i>runny</i>.</li>
<li>C: point out the advice forms (<i>ought to, had better, If I were you</i>): they prepare the Language focus.</li></ol>""")

    # Page 3 - Language focus
    fs = [("If I were you, I'd stay in bed for a few days.", "personal advice"), ("You'd better not take them.", "a strong warning"),
          ("Why don't you ask Mrs. Lima for some tea with honey?", "a friendly suggestion"), ("You ought to eat something.", "normal advice (= should)")]
    fsl = "".join(f"<li>{s} {A(a, 'min-width:30mm')}</li>" for s, a in fs)
    b.page(f"""{sec(3, "Language focus: giving advice", "8 min")}
{sub("A", "Sentences from the phone call. What kind of advice is each one? Write: a friendly suggestion, normal advice, personal advice or a strong warning.", "3 min")}
<ol style="line-height:1.75;font-size:8.9pt;margin:0">{fsl}</ol>
{sub("B", "Complete the rules. Choose.", "3 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0"><li><i>Ought to</i> means the same as {ch(["should", "must"], "should")}.</li>
<li>After <i>had better</i>, we use the {ch(["base form", "to + base form"], "base form")}: <i>You'd better rest.</i></li>
<li>The negative is {ch(["You hadn't better go.", "You'd better not go."], "You'd better not go.")}</li>
<li><i>Had better</i> talks about {ch(["the past", "now or the near future"], "now or the near future")}, and it is {ch(["softer", "stronger"], "stronger")} than <i>should</i>.</li>
<li>After <i>If I were you,</i> we use {ch(["I'd", "I will"], "I'd")} + base form.</li></ol>
{sub("C", "Correct or incorrect? Choose.", "2 min")}
<ol style="line-height:1.6;font-size:8.9pt;margin:0"><li>You'd better to call the doctor. {ch(["correct", "incorrect"], "incorrect")} {R("→ You'd better call") if T else ""}</li><li>Why don't you take a hot shower? {ch(["correct", "incorrect"], "correct")}</li><li>If I was you, I will rest. {ch(["correct", "incorrect"], "incorrect")} {R("→ If I were you, I'd rest.") if T else ""}</li></ol>
<div class="box sand"><h4>RULE</h4>Give advice with <b>should / ought to</b> + base form. Make it softer with <b>Why don't you…?</b> or <b>You might want to…</b>, more personal with <b>If I were you, I'd…</b>, and stronger with <b>had better ('d better)</b> + base form: it's a warning (or there will be a problem). Negative: <b>You'd better not…</b> More on the next page: <b>Grammar reference</b>.</div>""",
    24, """<ol><li>A: draw a scale on the board from soft to strong and place each form on it.</li>
<li>B: <i>had better</i> looks like a past form, but it refers to now. Be careful with bosses or strangers: <i>You'd better…</i> can sound like a threat. <i>You might want to…</i> is safer.</li></ol>""")

    grammar_ref.advice_strong_soft(b)

    # Page 5 - Vocabulary lab
    rm = [("antibiotics", "a bacterial infection"), ("a painkiller (aspirin, ibuprofen)", "a migraine or a toothache"), ("a decongestant", "a blocked nose"),
          ("moisturizer", "dry skin"), ("tissues", "a runny nose"), ("a throat lozenge", "a sore throat"), ("sleeping pills", "insomnia")]
    rml = [f'<li value="{i+1}">{r} → {A(p, "min-width:30mm")}</li>' for i, (r, p) in enumerate(rm)]
    ahs = [f"My finger {ch(['hurts', 'pain'], 'hurts')} when I write.", f"I've got a terrible {ch(['pain', 'ache'], 'pain')} in my chest.",
           f"I've got a {ch(['toothache', 'tooth pain'], 'toothache')}.", f"My eyes {ch(['ache', 'pain'], 'ache')} after a day at the computer."]
    b.page(f"""{sec(4, "Vocabulary lab: remedies and pain", "4 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Remedies. Which problem is each remedy for? Write from the box.", "2 min")}
<div class="bank">a bacterial infection · a blocked nose · dry skin · insomnia · a migraine or a toothache · a runny nose · a sore throat</div></div>{img('D', 34, 23)}</div>
<div style="font-size:8.5pt">{twocol(rml, 4)}</div>
{sub("B", "Ache, hurt or pain? Choose.", "2 min")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.7">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {s}" for i, s in enumerate(ahs))}</p>
<div class="box sand"><h4>WATCH OUT: FALSE FRIENDS AND WORD CHOICE</h4>
<table style="margin:0;font-size:8.3pt"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>I'm constipated. (with a cold)</td><td><b>I've got a cold. My nose is blocked.</b></td><td><i>constipated</i> = you can't go to the bathroom!</td></tr>
<tr><td>Did you take your remedy?</td><td><b>Did you take your medicine?</b></td><td><i>medicine</i> = what you take; a <i>remedy</i> is a treatment, often a home remedy (tea, honey).</td></tr>
<tr><td>I'm with a headache.</td><td><b>I have / I've got a headache.</b></td><td>symptoms take <i>have / have got</i>.</td></tr>
<tr><td>He had an injury from his boss.</td><td><b>His boss insulted him.</b></td><td>an <i>injury</i> = damage to your body: <i>a knee injury</i>.</td></tr></table></div>
{sec(5, "Pronunciation lab: health words", "4 min")}
<p class="small" style="margin:.3mm 0"><i>Ache</i> sounds like <i>take</i> /eɪk/: <i>HEADache, STOMachache</i>. Careful: <i>cough</i> /kɔːf/, <i>throat</i> /θroʊt/, <i>tissue</i> /ˈtɪʃuː/, <i>MEDicine</i> (3 syllables), <i>ALlergy</i> but <i>alLERgic</i>.</p>
{audiocard(["13.2"])}
{sub("A", "Listen and repeat. Then tell your teacher about the last time you had one of these problems.", "4 min", "13.2")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.55">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S132))}</p>""",
    27, """<ol><li>A: a <i>painkiller</i> is the general word; <i>lozenge</i> = a cough drop. Ask: <i>Which of these do you have at home?</i></li>
<li>B: <i>hurt</i> is a verb (<i>My back hurts</i>); <i>ache</i> is a verb and a noun for a long, dull pain; <i>pain</i> is a noun (<i>a pain in my chest</i>). Compounds: <i>headache, toothache, earache, backache, stomachache</i>.</li></ol>""")

    # Page 6 - Practice
    pw = [("twisted", "twisted"), ("swollen", "swollen"), ("bruise", "bruise"), ("ice pack", "ice pack"), ("painkillers", "painkillers"), ("crutches", "crutches")]
    pc = [A(w, "min-width:16mm") for w, _ in pw]
    ad = [("Kate burned her hand on the oven at the bakery.", "You'd better put it under cold running water right now."),
          ("Lucy cut her finger while she was slicing onions.", "Why don't you put a Band-Aid on it?"),
          ("Tom has had a backache for a week. He grades papers all day.", "If I were you, I'd see a doctor and take more breaks."),
          ("Grandma Lourdes can't sleep at night.", "She ought to avoid coffee in the afternoon."),
          ("Rita has a terrible migraine, but she wants to work.", "You might want to go home and lie down.")]
    adl = "".join(f'<li>{s}<br>{R(a) if T else lines(1)}</li>' for s, a in ad)
    b.page(f"""{sec(6, "Practice", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Bruno writes to the running group. Complete his message with the words from the box.", "4 min")}
<div class="bank">bruise · crutches · ice pack · painkillers · swollen · twisted</div></div>{img('C', 30, 20)}</div>
<div class="box" style="line-height:1.95;font-size:9pt"><b>Running group chat</b><br>Hi guys! Bad news: I won't be at practice for a while. On Sunday I stepped in a hole near the lake and {pc[0]} my ankle. By the evening it was really {pc[1]}, about twice its normal size, and today there's a huge purple {pc[2]} on it. My friend Ana (she's a doctor) says nothing is broken, but I'd better rest it for two weeks. So now I'm on the sofa with an {pc[3]} and my foot up on three pillows. I'm taking {pc[4]} because it still hurts when I walk, and my roommate Danny has the flu, so we're a great team! Fortunately, I don't need {pc[5]}. See you all at the 10K in December... I hope!</div>
{sub("B", "The characters have problems. Give advice. Use a different form each time: should, ought to, had better, If I were you, Why don't you, You might want to.", "4 min")}
<ol style="line-height:1.55;font-size:8.8pt;margin:0">{adl}</ol>""",
    28, """<ol><li>A: <i>twist / sprain your ankle</i>; <i>swollen</i> (adj., from <i>swell</i>); <i>a bruise</i> = a purple mark. <i>Crutches</i>: the sticks you walk with.</li>
<li>B: answers in red are examples. Ask why the student chose a soft or strong form (a burn needs action now: <i>had better</i>).</li></ol>""")

    # Page 7 - Speaking
    b.page(f"""{sec(7, "Speaking: what's the matter?", "12 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>ask</th><th>describe</th><th>advise</th><th>react</th></tr>
<tr><td><i>What's the matter? · How are you feeling? · How long have you had it?</i></td><td><i>I feel awful. · I've got a… · I keep… · It hurts when I…</i></td><td><i>It sounds like… · If I were you, I'd… · You'd better…</i></td><td><i>Poor you! · I hope you feel better soon. · Get well soon!</i></td></tr></table></div>
{sub("A", "Guess the illness. Describe the symptoms of a cold, the flu, a hangover, an allergy, a migraine or food poisoning. Your teacher guesses and gives advice. Then change roles.", "3 min")}
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("B", "Long turn. Prepare for one minute, then talk for two minutes about a time you were sick or injured.", "5 min")}
<ul style="line-height:1.45;font-size:8.9pt;margin:0"><li>what happened and what your symptoms were</li><li>who looked after you and what advice they gave</li><li>what remedies or treatment helped</li><li>what you would do differently now</li></ul></div></div>
{sub("C", "Role-play: at the pharmacy. You are the pharmacist. Your teacher is a customer. Ask questions and give advice. Then change roles.", "2 min")}
<p style="margin:.3mm 0;font-size:8.6pt">{R("Teacher's card: You've got a cough and a sore throat, and it's been three days. You have an important presentation tomorrow, and you want something strong to stop the cough. You're allergic to aspirin. You think you need antibiotics.") if T else ""}</p>
{sub("D", "Talking point. Discuss with your teacher.", "2 min")}
<ol style="line-height:1.5;font-size:8.9pt;margin:0"><li>Have you ever broken a bone? What happened?</li><li>What illnesses are common in your city or country? What causes them?</li><li>Do people in your country take too much medicine without a doctor?</li></ol>""",
    36, """<ol><li>A: if the student chooses a hangover, <i>I've got a hangover</i> = I feel sick after drinking too much alcohol.</li>
<li>B: don't interrupt; note mistakes for the error log (page 8), especially <i>I'm with…</i> and <i>had better to</i>. Fluency option (3-2-1): the same story in 2 minutes, then in 1 minute. If the student prefers, they can talk about a friend or relative.</li>
<li>C: the pharmacist should notice the aspirin allergy and explain that antibiotics don't work for a cough caused by a virus.</li></ol>""")

    # Page 8 - Wrap-up
    cd = ["I can describe my symptoms and understand a doctor's advice.", "I can give advice from soft to strong (should, ought to, had better).",
          "I can talk about remedies, pain and injuries."]
    cdr = "".join(f"<tr><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for s in cd)
    b.page(f"""{sec(8, "Wrap-up and homework", "4 min")}
{sub("A", "Can-do check", "1 min")}
<table class="ck" style="font-size:8.6pt"><tr><th>In English…</th><th style="width:16mm">Easy!</th><th style="width:16mm">Sometimes</th><th style="width:16mm">Not yet</th></tr>{cdr}</table>
{sub("B", "My language notes. Write three corrections from today's class.", "2 min")}
<div style="display:flex;gap:5mm;font-size:8.6pt"><div style="flex:1"><b>I said…</b>{lines(3)}</div><div style="flex:1"><b>Better:</b>{lines(3)}</div></div>
{sub("C", "Homework: writing (100–150 words)", "1 min")}
<p style="margin:.3mm 0"><b>An email of advice.</b> A friend has a health problem (they can't sleep, they have a backache, or they're always tired). Write an email with advice. Read Ana's email to her cousin Carol first.</p>
<div class="box" style="font-size:8.6pt;line-height:1.4;margin:.5mm 0"><i>Hi Carol! I'm sorry you still can't sleep. Three weeks is a long time! I think the problem might be your phone. You told me you check your work emails in bed, so you'd better stop doing that right now. If I were you, I'd leave the phone in the kitchen at night. You also ought to stop drinking coffee after lunch. I know you love it, but it stays in your body for hours. Why don't you try a short walk after dinner, or a warm shower before bed? Please don't take sleeping pills without talking to your doctor. And if nothing changes in two weeks, you should see a specialist. Let me know how it goes. Get some rest! Love, Ana</i></div>
<p class="small" style="margin:.3mm 0">Checklist: ☐ say you're sorry about the problem &nbsp;☐ four different advice forms &nbsp;☐ one reason for each piece of advice &nbsp;☐ a friendly ending &nbsp;☐ 100–150 words</p>
{lines(5)}""",
    30, """<ol><li>B (error log): during the lesson, note 3–5 real mistakes. Here, the student writes what they said and the better version; guide them to self-correct first.</li>
<li>C: check the advice forms (no <i>to</i> after <i>had better</i> and <i>should</i>; <i>ought <b>to</b></i>) and that each piece of advice has a reason (<i>because…, so…</i>).</li></ol>""")

    script = "".join(f"<p style='margin:.6mm 0'><b>{l.split(': ', 1)[0]}:</b> {l.split(': ', 1)[1]}</p>" for l in S131)
    b.extra("Audio script", f"""
{sub("13.1", "A call to Dr. Ana (natural and slow)")}
<div style="line-height:1.35;font-size:8.7pt">{script}</div>
{sub("13.2", "Repeat: health words")}
<p>{" · ".join(S132)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 13 - Health and illness")
