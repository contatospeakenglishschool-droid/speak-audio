# Speak! Progress B1 - Unit 37 "Car problems" (all English) - lean B1 format
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
setup(band="B1 · UNIT 37", audio_json="audio_b1-unit-37.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-37"]
S371 = [l.split(": ", 1) for l in _r["37.1 At the auto shop"].split("\n")]
S372 = [x.split(": ", 1)[1] for x in _r["37.2 Repeat: compound nouns"].split("\n")]


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
    cover = cover_html(T, "LEVEL B1 · UNIT 37", "Car problems", "At the auto shop · <b>needs changing · needs to be replaced · don't need to</b>",
                       [("YOU CAN", "describe problems with a car or a machine, and arrange a repair"),
                        ("LANGUAGE", "a battery · brake pads · a leak · repair · replace · It needs changing."),
                        ("PRONUNCIATION", "stress in compound nouns: BRAKE pads")])
    kw = [("the part that gives the car electricity to start", "a battery"), ("the rubber part of a wheel, full of air", "a tire"),
          ("parts that press on the wheels to stop the car", "brake pads"), ("they clean rain off the front window", "windshield wipers"),
          ("the part that makes the car move; it uses fuel", "an engine"), ("a hole or crack where liquid escapes", "a leak")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:21mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Warm-up: when cars go wrong", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["Do you have a car? Do you like driving?", "Has your car (or a car you were in) ever broken down? What was the problem?", "Look at the photo. What do you do in this situation?"], "START TALKING")}</div></div>
{sub("A", "Key words. Write the words from the box next to the definitions.", "3 min")}
<div class="bank">a battery · brake pads · an engine · a leak · a tire · windshield wipers</div>
<div style="font-size:8.7pt">{twocol(kwl, 3)}</div>
{talk(["Can you change a flat tire? Who taught you?", "What are the most common reasons for a car to break down, in your opinion?"], "USE THE WORDS")}""",
    26, """<ol><li>Start with the questions in the top box: 4 minutes.</li>
<li>A: quick check (3 minutes), then the two questions. Common reasons: a dead battery, a flat tire, the wrong fuel, lost keys, the starter or the alternator. American English: <i>windshield</i> (not <i>windscreen</i>), <i>tire</i>, <i>hood</i>, <i>gas</i>.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Carol at the auto shop · answer the questions · fixing verbs · Talk about it",
                      "need to + verb; need + -ing / need to be + participle; don't / didn't need to", "Complete, choose · Use it (oral)",
                      "Compound noun stress (37.2) · role-play at the auto shop", "Carol's message to Ana · rewrite · word choice · writing"),
        """The Linguahouse lesson has car vocabulary, a short article on why cars break down, a dialogue at an auto repair shop (Mrs. Hobbs books a service: oil leak, broken brake light, washer fluid, brake pads) and fixing verbs (charge, check, recharge, repair, replace, service). We kept the dialogue situation and the verbs, gave it to Carol (Ana's cousin, Orlando), and used the breakdown reasons in the warm-up and the speaking cards. We did not use the article's percentages because we could not check their source. Carol's car needs a service before she drives to see a friend in Miami: possible oil leak, broken brake light, noisy wipers, a battery that died twice; she bought the car used three years ago; the last shop charged her $40 for washer fluid. The Linguahouse lesson has no grammar point; we added <i>need</i> + -ing / <i>need to be</i> + participle, which the dialogue uses naturally.""",
        """<i>The battery needs to change</i> (the battery changes itself), <i>It needs be replaced</i>, <i>You don't need pay</i>, <i>You need not to pay</i>; word choice: <i>in the mechanic</i> for <i>at the auto shop</i>, <i>the tire is empty</i> for <i>flat</i>, <i>charged me too expensive</i>. Pronunciation: compound nouns have the stress on the first word (<i>BRAKE pads, WINDshield wipers, OIL leak</i>).""",
        "Track 37.1 At the auto shop (natural and slow; Carol and the Mechanic) · Track 37.2 Repeat: compound nouns"))

    # Page 2 - Listening
    qs = [("When will Carol bring the car in?", "Thursday at nine"), ("When does she need it back?", "by Friday morning"),
          ("What might make the repair take longer?", "ordering new parts"), ("What four problems does Carol mention?", "oil leak, brake light, wipers, battery"),
          ("What does she need to pay for?", "only new parts")]
    ql = "".join(f"<li>{q} {A(a, 'min-width:44mm')}</li>" for q, a in qs)
    vb = [("The mechanic will ___ the brake pads and the tires.", "check"), ("If the battery is old, they'll ___ it with a new one.", "replace"),
          ("They might just ___ the battery.", "recharge"), ("The last shop wanted to ___ Carol $40 for washer fluid.", "charge"),
          ("They'll ___ the car on Thursday.", "service"), ("You can ___ a small crack in the windshield.", "repair")]
    vbl = "".join(f'<li>{s.replace("___", A(a, "min-width:16mm"))}</li>' for s, a in vb)
    b.page(f"""{sec(2, "Listening: at the auto shop", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Carol takes her car to an auto shop in Orlando. Listen and answer.", "4 min")}
<ol style="line-height:1.5;font-size:8.6pt;margin:0">{ql}</ol></div>{img('B', 36, 26)}</div>
{audiocard(["37.1 · NATURAL", "37.1 · SLOW"])}
{sub("B", "Fixing verbs. Complete the sentences with the words from the box.", "3 min")}
<div class="bank">charge · check · recharge · repair · replace · service</div>
<ol style="line-height:1.55;font-size:8.7pt;margin:0;columns:2">{vbl}</ol>
{talk(["Do you trust mechanics? Have you ever paid too much for a repair?", "What can you fix yourself: in a car, at home, on a computer?", "Would you buy a used car? What would you check first?"])}""",
    30, """<ol><li>A: play the natural version; play the slow one if needed. 6 minutes.</li>
<li>B: 3 minutes. <i>Repair</i> = fix something broken; <i>replace</i> = put a new one in its place; <i>service</i> = check and maintain a car or machine; <i>charge</i> someone money.</li>
<li>Talk about it: 4 minutes. Note sentences with <i>need</i> for page 3.</li></ol>""")

    # Page 3
    lean.grammar_in_class(b, grammar_ref.needs_doing)

    # Page 4 - Practice
    fs = [("The tires are old. They", "replace", "need replacing / need to be replaced"), ("The car is very dirty. It", "wash", "needs washing / needs to be washed"),
          ("The battery is dead. It", "recharge", "needs recharging / needs to be recharged"), ("There's a small crack in the windshield. It", "repair", "needs repairing / needs to be repaired"),
          ("The oil is black. It", "change", "needs changing / needs to be changed")]
    fsl = "".join(f'<li>{a} {A(ans, "min-width:58mm")} ({v}).</li>' for a, v, ans in fs)
    use = ["What in your home needs fixing or replacing right now?", "What do you need to do this week? What don't you need to do?",
           "Look at your phone or computer. Does anything need updating, cleaning or charging?", "What do people need to check before a long road trip?",
           "Tell me about something that didn't need fixing, but someone fixed it anyway."]
    b.page(f"""{sec(4, "Practice: need to, needs changing", "10 min")}
{sub("A", "Complete with need(s) + -ing or need(s) to be + participle.", "4 min")}
<ol style="line-height:1.75;font-size:8.9pt;margin:0">{fsl}</ol>
{sub("B", "Choose.", "2 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0"><li>You {ch(["don't need to", "need not to"], "don't need to")} pay extra for that.</li>
<li>The wipers need {ch(["to change", "changing"], "changing")}.</li>
<li>Do I {ch(["need", "need to"], "need to")} bring the car in early?</li></ol>
<div class="box sand"><h4>RULE</h4><b>person + need to</b> + verb · <b>thing + needs</b> + -ing or <b>needs to be</b> + participle · <b>don't need to</b> = no obligation · <i>it need<b>s</b></i>, <i>does it need</i>. See the <b>Grammar reference</b> on page 3.</div>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    24, """<ol><li>A–B: 6 minutes. Accept both forms in A.</li>
<li>Use it: 4 minutes, all oral. Push for both forms: <i>My kitchen faucet needs fixing. / It needs to be fixed.</i></li></ol>""")

    # Page 5 - Speaking
    pr = ["The car won't start, but the battery is new.", "You left the lights on all night.", "You put diesel in a gas car.",
          "The car pulls to one side and makes a strange noise.", "There's a strong smell from under the hood.", "The brakes make a loud noise.",
          "There's a crack in the windshield.", "The air conditioning doesn't work."]
    pl = "".join(f"<li>{x}</li>" for x in pr)
    b.page(f"""{sec(5, "Speaking: at the auto shop", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.3pt"><tr><th>describing a problem</th><th>asking</th><th>the mechanic</th><th>making a deal</th></tr>
<tr><td><i>It won't start. · It makes a strange noise when I… · There's a smell coming from…</i></td><td><i>How long will it take? · How much will it cost? · Is that included?</i></td><td><i>It needs replacing. · It should be ready by… · It might take longer if…</i></td><td><i>That's a bit expensive. · Can you do it by…? · OK, let's do that.</i></td></tr></table></div>
{audiocard(["37.2"])}
{sub("A", "Listen and repeat. Stress the first word: BRAKE pads, OIL leak.", "4 min", "37.2")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S372))}</p>
{sub("B", "You are the customer and your teacher is the mechanic. Choose two problems, describe them, and agree on a time and a price. Then change roles: you are the mechanic.", "14 min")}
<ol style="line-height:1.4;font-size:8.8pt;margin:0;columns:2">{pl}</ol>
{talk(["Is it better to have your own car or to use apps and public transportation? Why?", "Would you buy an electric car? Why or why not?"], "TALK ABOUT IT")}""",
    37, """<ol><li>A: compound nouns have the main stress on the first word: <i>WINDshield wipers, BRAKE pads, CAR battery, OIL leak, BRAKE light, AUto shop</i>.</li>
<li>B: as the mechanic, explain what each part needs (<i>The battery needs recharging. The tires need to be replaced.</i>), give a time and a price, and try to sell an extra service. Likely causes from the Linguahouse article: 1 the starter · 2 the battery · 3 the wrong fuel · 4 a flat tire or a damaged wheel · 5 the engine or the alternator. Last 3 minutes: wrap-up (two corrections, and ask <i>Can you now describe a problem and arrange a repair?</i>).</li></ol>""")

    # Homework
    pc = [(["replacing", "to replace"], "replacing"), (["recharging", "recharge"], "recharging"), (["to be replaced", "to replace"], "to be replaced"),
          (["to pay", "pay"], "to pay"), (["changing", "change"], "changing")]
    p = [ch(o, a) for o, a in pc]
    rw = [("Someone has to fix the brake light. (needs)", "The brake light needs fixing. / The brake light needs to be fixed."),
          ("It isn't necessary to bring the car early. (don't need to)", "You don't need to bring the car early."),
          ("Someone should check the tires. (need to be)", "The tires need to be checked.")]
    rwl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Carol writes to Ana after the service. Choose the correct words.", "")}</div>{img('C', 28, 18)}</div>
<div class="box" style="line-height:1.85;font-size:8.8pt;margin:.5mm 0"><b>Hi Ana!</b><br>Good news: I found a great auto shop! The battery didn't need {p[0]}; it only needed {p[1]}. But there was an oil leak, and a small part needed {p[2]}. I didn't need {p[3]} for the check, only for the part. The mechanic said the tires will need {p[4]} soon, so that's my next expense. The old shop charged me $40 for washer fluid, can you believe it? Carol</div>
{sub("B", "Rewrite the sentences with the words in brackets.", "")}
<ol style="line-height:1.5;font-size:8.7pt;margin:0">{rwl}</ol>
{lean.watch_out([("My car is in the mechanic.", "My car is at the auto shop. / at the mechanic's.", "<i>the mechanic</i> = the person; <i>the auto shop</i> = the place."), ("The tire is empty.", "The tire is flat. / I have a flat tire.", "tires are <i>flat</i>, not <i>empty</i>."), ("The mechanic charged me too expensive.", "The mechanic charged me too much.", "<i>charge</i> + an amount; <i>expensive</i> describes a thing.")])}
{lean.writing_task(sub, "Write an email to an auto shop. Describe two or three problems with your car (real or invented), ask how long it will take and how much it will cost, and say when you need it back.", "Hello, I'd like to bring my car in for…", ["two or three problems", "need + -ing or need to be", "two questions", "the day and time you need it back", "100–150 words"], "I can describe problems with a car and arrange a repair.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class. Read the writing at home and choose two mistakes to discuss in class.</p>""")

    script = "".join(f"<p style='margin:.5mm 0'><b>{n}:</b> {l}</p>" for n, l in S371)
    b.extra("Audio script", f"""
{sub("37.1", "At the auto shop (natural and slow; Carol and the Mechanic)")}
<div style="line-height:1.3;font-size:8.6pt">{script}</div>
{sub("37.2", "Repeat: compound nouns")}
<p>{" · ".join(S372)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 37 - Car problems")
