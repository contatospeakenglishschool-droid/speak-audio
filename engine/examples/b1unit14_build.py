# Speak! Progress B1 - Unit 14 "At the restaurant" (all English) - B1 format (2026-11-09)
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Progress"
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
    def lines(n):
        return '<div class="wline"></div>' * n

    # Page 1 - Warm-up
    cover = cover_html(T, "LEVEL B1 · UNIT 14", "At the restaurant", "Ordering and paying · <b>indirect questions: Could you tell me…? Do you know if…?</b>",
                       [("YOU CAN", "order a meal, ask about dishes politely, and deal with the check and the tip"),
                        ("LANGUAGE", "an appetizer · a side dish · the check · a tip · What does it come with? · Do you know if it's spicy?"),
                        ("PRONUNCIATION", "polite intonation in requests and indirect questions")])
    kw = [("a small amount of food before the main part of a meal (also: a starter)", "an appetizer"), ("the largest or most important part of a meal", "the main course"),
          ("an extra food served on a separate plate, like fries or a salad", "a side dish"), ("sweet food that you eat at the end of a meal", "dessert"),
          ("the piece of paper that shows how much you have to pay", "the check"), ("extra money you leave for the server", "a tip"),
          ("an amount added to the check to pay for the service", "a service charge"), ("a trained, skilled cook who runs a restaurant kitchen", "a chef")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:22mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Warm-up: eating out", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 36)}<div style="flex:1">
{sub("A", "Discuss with your teacher.", "3 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0"><li>How often do you eat out? Do you prefer to eat in or eat out?</li><li>What's the best restaurant you know? What do you usually order there?</li><li>What do you find stressful about restaurants (ordering, the check, the tip…)?</li></ol></div></div>
{sub("B", "Key words. Write the words from the box next to the definitions.", "4 min")}
<div class="bank">an appetizer · a chef · the check · dessert · the main course · a service charge · a side dish · a tip</div>
<div style="font-size:8.6pt">{twocol(kwl, 4)}</div>
{sub("C", "You are traveling abroad. Plan a meal from an international menu: an appetizer, a main course with a side dish, and a dessert.", "1 min")}""",
    30, """<ol><li>A: <i>eat in</i> = eat at home; <i>eat out</i> = eat at a restaurant.</li>
<li>B: <i>check</i> is American English (British: <i>bill</i>). <i>Appetizer</i> (US) = <i>starter</i> (UK). A <i>cook</i> is anyone who cooks; a <i>chef</i> is a trained professional. <i>Server</i> is the neutral word for waiter/waitress.</li>
<li>C: for example, a Caesar salad (appetizer), steak with fries or a vegetable lasagna (main course), cheesecake (dessert). Students who travel will see these dishes on menus all over the world.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 60 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Discussion · key words: parts of a meal, the check</td><td>1</td></tr>
<tr><td>2 Listening</td><td>12 min</td><td>Dialogue: Danny takes Ana to a bistro with an international menu</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>8 min</td><td>Indirect questions</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Indirect questions (study at home)</td><td>4</td></tr>
<tr><td>4 Vocabulary lab + pronunciation</td><td>8 min</td><td>Restaurant language by function · polite intonation</td><td>5</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Carol's message about tipping · making questions polite</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Role-play: an international menu · long turn · talking point</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>4 min</td><td>Can-do · language notes · writing homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY</h4>The Linguahouse lesson uses a dialogue in an English-style restaurant and a dinner between two business contacts. Our original listening brings both ideas together: Danny has recovered from the flu (B1 Unit 13) and takes Ana to a bistro with an international menu to thank her. He asks the server about the dishes with indirect questions, mentions his nut allergy, orders a steak (medium), changes his drink order, and insists on paying (<i>It's on me</i>). The restaurant is fictional. Facts about tipping are verified: in Brazil, a 10% service charge is common on the check, but it is optional, and the restaurant must make that clear (Procon-SP; Idec). In the United States, the usual guideline for a sit-down restaurant is a tip of 15 to 20% (Emily Post Institute; Pew Research Center 2023). Carol (Orlando, B1 Units 04 and 13) writes about tipping in the Practice. The writing model is Danny's online review of the restaurant.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students say <i>Can you bring the account?</i> (the check), <i>I want a coke</i> (sounds rude: <i>I'll have / I'd like</i>), <i>I'm satisfied</i> for <i>I'm full</i>, and keep question word order in indirect questions: <i>Do you know where is the restroom?</i></div>
<div class="box"><h4>AUDIO</h4>Track 14.1 Dinner is on me (natural and slow) · Track 14.2 Repeat: polite questions</div>""")

    # Page 2 - Listening
    gist = ["to celebrate his new job", "to thank Ana for her help", "to meet Ana's husband"]
    ordr = [("appetizer", "–", "tomato soup"), ("main course", "steak (medium), mashed potatoes", "mushroom risotto"), ("drink", "iced tea", "sparkling water"), ("dessert", "nothing (full)", "nothing (full)")]
    ordt = "".join(f"<tr><td><b>{a}</b></td><td>{A(d, 'min-width:30mm')}</td><td>{A(n, 'min-width:30mm')}</td></tr>" for a, d, n in ordr)
    tf = [("Danny is allergic to nuts.", "T"), ("Danny first orders a lemonade.", "T"),
          ("Danny wants his steak rare.", "F (medium)"), ("Ana pays for dinner.", "F (Danny pays)"), ("The 10% service charge is required by law.", "F (it's optional)")]
    tfl = [f'<li value="{i+1}">{s} {A(a, "min-width:9mm")}</li>' for i, (s, a) in enumerate(tf)]
    b.page(f"""{sec(2, "Listening: dinner is on me", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{audiocard(["14.1 · NATURAL", "14.1 · SLOW"])}
{sub("A", "Danny takes Ana to a bistro. Listen at natural speed. Why does he invite her?", "2 min", "14.1")}
<p style="margin:.3mm 0;font-size:8.9pt">{ch(gist, gist[1])}</p></div>{img('B', 40, 27)}</div>
{sub("B", "Listen again. What do they order? Complete the table.", "3 min")}
<table style="font-size:8.6pt;margin:.5mm 0"><tr><th style="width:24mm"></th><th>Danny</th><th>Ana</th></tr>{ordt}</table>
{sub("C", "True or false? Correct the false sentences.", "3 min")}
<div style="font-size:8.6pt">{twocol(tfl, 3)}</div>
{sub("D", "Think about it. Discuss with your teacher.", "4 min")}
<ol style="line-height:1.4;font-size:8.8pt;margin:0"><li>"I didn't want to ask." Why does Ana ask Danny, not the server, about <i>medium</i>? {R("She was embarrassed, or she didn't want to look like she didn't know.") if T else ""}</li>
<li>Do you know how you like your steak: rare, medium or well-done? Do you have any food allergies?</li><li>Who should pay when you invite someone to dinner in your culture?</li></ol>
<div class="box sand" style="margin-top:1mm"><h4>NOTICE: USEFUL CHUNKS</h4><i>Dinner is on me. · What does it come with? · Make that a… · Just water for me. · I don't have room for… · If you insist. · Next time is on me. · Deal.</i></div>""",
    22, """<ol><li>B: the focus is the restaurant language (<i>I'd like to start with…, for my main course…, What does it come with?</i>). Teach <i>How would you like your steak?</i> (rare, medium, well-done) and <i>dressing</i>: travelers hear them everywhere.</li>
<li>C: Danny says <i>make that</i> to change his order. Ana explains that the 10% service charge is optional in Brazil.</li></ol>""")

    # Page 3 - Language focus
    fs = [("What's today's special?", "Could you tell me what today's special is?"), ("Does the risotto have any nuts in it?", "Do you know if the risotto has any nuts in it?"),
          ("What does medium mean?", "Do you know what medium means?"), ("Should I leave a tip?", "Do you know if I should leave a tip?")]
    fsl = "".join(f"<li><i>{d}</i> → {A(i, 'min-width:60mm')}</li>" for d, i in fs)
    b.page(f"""{sec(3, "Language focus: indirect questions", "8 min")}
{sub("A", "Danny's questions from the dialogue. Write the polite form he used.", "3 min")}
<ol style="line-height:1.85;font-size:8.9pt;margin:0">{fsl}</ol>
{sub("B", "Complete the rules. Choose.", "3 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0"><li>Indirect questions sound {ch(["more polite", "less polite"], "more polite")} than direct questions.</li>
<li>After <i>Could you tell me / Do you know</i>, the word order is {ch(["question order (is it)", "normal order (it is)"], "normal order (it is)")}.</li>
<li>In indirect questions, we {ch(["use", "don't use"], "don't use")} <i>do / does / did</i>.</li>
<li>For yes/no questions, we add {ch(["if / whether", "that"], "if / whether")}: <i>Do you know if it's spicy?</i></li></ol>
{sub("C", "Correct or incorrect? Choose.", "2 min")}
<ol style="line-height:1.6;font-size:8.9pt;margin:0"><li>Could you tell me where is the restroom? {ch(["correct", "incorrect"], "incorrect")} {R("→ where the restroom is") if T else ""}</li><li>I was wondering if you have a table for four. {ch(["correct", "incorrect"], "correct")}</li><li>Do you know what time does the kitchen close? {ch(["correct", "incorrect"], "incorrect")} {R("→ what time the kitchen closes") if T else ""}</li></ol>
<div class="box sand"><h4>RULE</h4>Start with <b>Could you tell me… / Do you know… / I was wondering…</b>, then use normal word order: question word + <b>subject + verb</b> (<i>what the special is, where the restroom is, what time it opens</i>). No <i>do/does/did</i>. For yes/no questions, add <b>if</b> or <b>whether</b>. More on the next page: <b>Grammar reference</b>.</div>""",
    29, """<ol><li>A: highlight the word order with two colors: <i>What <b>is</b> today's special?</i> → <i>…what today's special <b>is</b>.</i></li>
<li>A: in 2 and 3, <i>does</i> disappears and the verb takes <i>-s</i>: <i>has, means</i>.</li><li>B: <i>whether</i> is a little more formal than <i>if</i>. <i>I was wondering if…</i> is the most polite start, good for reservations and requests.</li></ol>""")

    grammar_ref.indirect_questions(b)

    # Page 5 - Vocabulary lab
    ph = [("Are you ready to order?", "taking an order"), ("What would you recommend?", "asking about dishes"), ("I'll have the steak, medium.", "ordering"),
          ("No, wait... make that a juice.", "changing an order"), ("What does it come with?", "asking about dishes"), ("I'd like to start with…", "ordering"),
          ("Could we have the check, please?", "paying"), ("Keep the change.", "paying")]
    phl = [f'<li value="{i+1}"><i>{p}</i> {A(c, "min-width:26mm")}</li>' for i, (p, c) in enumerate(ph)]
    cw = [(["eat in", "eat out"], "eat out", "We almost never cook on Fridays. We usually", "."), (["plate", "dish"], "plate", "My", " was dirty, so I asked for another one."),
          (["cook", "chef"], "chef", "The food was excellent. Compliments to the", "!"), (["dish", "plate"], "dish", "Lasagna is a typical Italian", ".")]
    cws = " &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {p} {ch(o, a)}{e}" for i, (o, a, p, e) in enumerate(cw))
    b.page(f"""{sec(4, "Vocabulary lab: restaurant language", "4 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "What is each phrase for? Write: taking an order, ordering, changing an order, asking about dishes or paying.", "2 min")}</div>{img('D', 34, 23)}</div>
<div style="font-size:8.5pt">{twocol(phl, 4)}</div>
{sub("B", "Choose the correct word.", "2 min")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.7">{cws}</p>
<div class="box sand"><h4>WATCH OUT: FALSE FRIENDS AND WORD CHOICE</h4>
<table style="margin:0;font-size:8.3pt"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>Can you bring the account?</td><td><b>Could we have the check, please?</b></td><td>at a restaurant = <i>the check</i> (US) or <i>the bill</i> (UK); an <i>account</i> is at a bank.</td></tr>
<tr><td>I want a coke.</td><td><b>I'll have / I'd like a coke.</b></td><td><i>I want</i> sounds rude when you order.</td></tr>
<tr><td>No, thanks. I'm satisfied.</td><td><b>No, thanks. I'm full.</b></td><td><i>satisfied</i> = happy with something; after eating = <i>full</i>.</td></tr>
<tr><td>What's the plate of the day?</td><td><b>What's today's special?</b></td><td>a <i>plate</i> is what you eat from; the dish of the day = <i>the special</i>.</td></tr></table></div>
{sec(5, "Pronunciation lab: polite questions", "4 min")}
<p class="small" style="margin:.3mm 0">Polite questions start high and have a friendly fall-rise at the end. Notice the connected speech: <i>Could you</i> /kʊdʒə/, <i>Would you</i> /wʊdʒə/, <i>Do you know</i> /dəjəˈnoʊ/.</p>
{audiocard(["14.2"])}
{sub("A", "Listen and repeat. Copy the polite intonation. Then ask your teacher three polite questions about their favorite restaurant.", "4 min", "14.2")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.55">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S142))}</p>""",
    25, """<ol><li>A: add <i>Can I take your order?</i> (taking an order), <i>Do you serve vegetarian dishes?</i> (asking about dishes), <i>This is for you.</i> (tipping).</li>
<li>B: a <i>dish</i> is food prepared in a particular way and also a container; a <i>plate</i> is the flat dish you eat from.</li></ol>""")

    # Page 6 - Practice
    pc = [(["check", "account"], "check"), (["tip", "change"], "tip"), (["15 to 20", "5 to 10"], "15 to 20"), (["servers", "chefs"], "servers"),
          (["included", "optional"], "optional"), (["on me", "for me"], "on me"), (["if", "that"], "if")]
    p = [ch(o, a) for o, a in pc]
    dq = [("Is there a vegetarian option?", "Could you tell me if there's a vegetarian option?"), ("Where can I park?", "Do you know where I can park?"),
          ("How much is the fixed-price lunch?", "Could you tell me how much the fixed-price lunch is?"), ("Do you take reservations?", "I was wondering if you take reservations."),
          ("What time does the kitchen close?", "Do you know what time the kitchen closes?")]
    dql = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in dq)
    b.page(f"""{sec(6, "Practice", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Carol (Orlando) answers Danny's question about tipping. Choose the correct words.", "4 min")}</div>{img('C', 30, 20)}</div>
<div class="box" style="line-height:1.95;font-size:9pt"><b>From: Carol · To: Danny</b><br>Hi Danny! Your mom told me about your dinner with Ana. So you want to know about tipping here? OK! In the US, when the server brings the {p[0]}, you usually add a {p[1]}. For a sit-down restaurant, most people leave {p[2]} percent of the bill, more for great service. It's part of how {p[3]} earn a living, so people don't skip it. In Brazil it's different: a 10% service charge is often on the check, but it's {p[4]}. And when an American friend says "It's {p[5]}," it means they're paying! One more tip: if you aren't sure, just ask the server politely, "Could you tell me {p[6]} the tip is included?" Hugs, Carol</div>
{sub("B", "Make the questions polite. Use Could you tell me…, Do you know… or I was wondering if…", "4 min")}
<ol style="line-height:1.55;font-size:8.8pt;margin:0">{dql}</ol>""",
    24, """<ol><li>A: point out <i>It's on me</i> = I'm paying, and <i>skip</i> = not do something.</li>
<li>B: answers in red are examples; accept any correct start. Check the word order and that there is no <i>do/does</i> after the start.</li></ol>""")

    # Page 7 - Speaking
    b.page(f"""{sec(7, "Speaking: a table for two", "12 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>server</th><th>customer: ask</th><th>customer: order</th><th>host / guest</th></tr>
<tr><td><i>Are you ready to order? · Anything to drink? · Can I get you some dessert?</i></td><td><i>Could you tell me what's in…? · Do you know if…? · What would you recommend?</i></td><td><i>I'd like to start with… · I'll have… · Make that… · Just water for me.</i></td><td><i>It's on me. · Let me get this. · OK, if you insist. · Next time is on me.</i></td></tr></table></div>
{sub("A", "Role-play: an international restaurant. Write a short menu with three dishes from any country (for example, Italian, Japanese or Mexican food). You are the server. Your teacher is a tourist who asks a lot of questions. Then change roles: your teacher is the server.", "6 min")}
<div style="display:flex;gap:4mm;font-size:8.6pt"><div style="flex:1"><b>Dish 1:</b>{lines(1)}</div><div style="flex:1"><b>Dish 2:</b>{lines(1)}</div><div style="flex:1"><b>Dish 3:</b>{lines(1)}</div></div>
<p style="margin:.3mm 0;font-size:8.6pt">{R("Teacher's card (tourist): You're vegetarian, you're allergic to nuts, and you want to know what each dish comes with. Change your drink order once. At the end, ask if the service charge is included.") if T else ""}</p>
{sub("B", "Long turn. Prepare for one minute, then talk for two minutes about a memorable meal at a restaurant (great or terrible).", "4 min")}
<ul style="line-height:1.45;font-size:8.9pt;margin:0"><li>where and when it was, and who you were with</li><li>what you ordered (appetizer, main course, dessert)</li><li>the service and the check: who paid?</li><li>why you remember it</li></ul>
{sub("C", "Talking point. Discuss with your teacher.", "2 min")}
<ol style="line-height:1.5;font-size:8.9pt;margin:0"><li>Should tips be optional, or should restaurants pay servers more?</li><li>When friends eat out, is it better to split the check or take turns paying?</li></ol>""",
    30, """<ol><li>A: help the student describe dishes: <i>It's a kind of…, It's made with…, It's served with…</i>. Push for indirect questions when the student is the customer.</li>
<li>B: don't interrupt; note mistakes for the error log (page 8), especially <i>I want…</i> and question word order. Fluency option (3-2-1): the same story in 2 minutes, then in 1 minute.</li></ol>""")

    # Page 8 - Wrap-up
    cd = ["I can order a meal and ask about dishes in a restaurant.", "I can ask polite indirect questions (Could you tell me…? Do you know if…?).",
          "I can talk about the check, tips and who pays."]
    cdr = "".join(f"<tr><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for s in cd)
    b.page(f"""{sec(8, "Wrap-up and homework", "4 min")}
{sub("A", "Can-do check", "1 min")}
<table class="ck" style="font-size:8.6pt"><tr><th>In English…</th><th style="width:16mm">Easy!</th><th style="width:16mm">Sometimes</th><th style="width:16mm">Not yet</th></tr>{cdr}</table>
{sub("B", "My language notes. Write three corrections from today's class.", "2 min")}
<div style="display:flex;gap:5mm;font-size:8.6pt"><div style="flex:1"><b>I said…</b>{lines(3)}</div><div style="flex:1"><b>Better:</b>{lines(3)}</div></div>
{sub("C", "Homework: writing (100–150 words)", "1 min")}
<p style="margin:.3mm 0"><b>A restaurant review.</b> Write an online review of a restaurant you know. Read Danny's review first.</p>
<div class="box" style="font-size:8.6pt;line-height:1.4;margin:.5mm 0"><b>★★★★★ A cozy bistro with great steaks</b><br><i>Last Friday I took a friend to this small bistro to say thank you, and it was the best meal I've had in months. The place is simple but cozy, with soft music and candles. Our server was patient with all my questions: I'm allergic to nuts, and he checked every dish for me. My steak was perfect, medium as I asked, and it came with creamy mashed potatoes and a fresh salad. My friend had the mushroom risotto and loved it. We were too full for dessert, but the chocolate cake looked great. It isn't cheap, and the 10% service charge is on the check, but the service deserved it. Tip: book a table on weekends. I'll definitely go back!</i></div>
<p class="small" style="margin:.3mm 0">Checklist: ☐ the place and the atmosphere &nbsp;☐ the food (describe one dish) &nbsp;☐ the service and the price &nbsp;☐ a recommendation &nbsp;☐ 100–150 words</p>
{lines(5)}""",
    30, """<ol><li>B (error log): during the lesson, note 3–5 real mistakes. Here, the student writes what they said and the better version; guide them to self-correct first.</li>
<li>C: check restaurant vocabulary (<i>check, server, side dish, full</i>) and adjectives for food and places (<i>cozy, spicy, homemade</i>).</li></ol>""")

    script = "".join(f"<p style='margin:.5mm 0'><b>{l.split(': ', 1)[0]}:</b> {l.split(': ', 1)[1]}</p>" for l in S141)
    b.extra("Audio script", f"""
{sub("14.1", "Dinner is on me (natural and slow)")}
<div style="line-height:1.3;font-size:8.5pt">{script}</div>
{sub("14.2", "Repeat: polite questions")}
<p>{" · ".join(S142)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 14 - At the restaurant")
