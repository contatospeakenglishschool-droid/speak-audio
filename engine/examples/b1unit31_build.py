# Speak! Progress B1 - Unit 31 "Home improvements" (all English) - lean B1 format
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
setup(band="B1 · UNIT 31", audio_json="audio_b1-unit-31.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-31"]
S311 = _r["31.1 Ana's new kitchen"].split("\n")
S312 = [x.split(": ", 1)[1] for x in _r["31.2 Repeat: have something done"].split("\n")]


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
    cover = cover_html(T, "LEVEL B1 · UNIT 31", "Home improvements", "Ana's new kitchen · <b>have / get something done</b>",
                       [("YOU CAN", "talk about repairs at home, decide what to do yourself and what to have done by a professional"),
                        ("LANGUAGE", "a leak · a plumber · an electrician · DIY · We're having the kitchen remodeled."),
                        ("PRONUNCIATION", "stress in have something done")])
    kw = [("water that escapes from a hole or crack in a pipe", "a leak"), ("a person who fixes pipes, sinks and toilets", "a plumber"),
          ("a person who fixes wires, lights and outlets", "an electrician"), ("a person who fixes or changes locks", "a locksmith"),
          ("making or fixing things at home yourself, without a professional", "DIY"), ("to make a screw or a handle firmer", "tighten")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:21mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Warm-up: tools and repairs", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["Can you name the tools in the photo? Which ones do you have at home?", "Are you good at fixing things? What was the last thing you fixed?", "Which tool would you use to put a picture on the wall?"], "START TALKING")}</div></div>
{sub("A", "Key words. Write the words from the box next to the definitions.", "3 min")}
<div class="bank">DIY · an electrician · a leak · a locksmith · a plumber · tighten</div>
<div style="font-size:8.7pt">{twocol(kwl, 3)}</div>
{talk(["Have you ever had a leak or a problem with the electricity at home? What did you do?", "Do you enjoy DIY, or do you prefer to call a professional?"], "USE THE WORDS")}""",
    26, """<ol><li>Start with the questions in the top box: 4 minutes. Tools in the photo: hammer, screwdriver, wrench, pliers. Encourage <i>I'd use a hammer and a nail.</i></li>
<li>A: quick check (3 minutes). <i>DIY</i> = Do It Yourself, pronounced /ˌdiː aɪ ˈwaɪ/. <i>plumber</i>: the b is silent /ˈplʌmər/.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Phone call: Ana is having her kitchen remodeled · who does what? · true or false · Talk about it",
                      "have / get something done", "Complete, choose · Use it (oral)",
                      "Stress (31.2) · role-play: tenant and landlord with a list of problems", "Kate's bakery makeover · rewrite · word choice · writing"),
        """The Linguahouse lesson is vocabulary (tools, DIY phrases, professionals) with the structure <i>have something done</i>. Our listening is a phone call: Ana (doctor, São Paulo) is having her kitchen remodeled. Her husband Marcos tried to fix a leak himself and made it worse, so they called a plumber; an electrician is coming on Friday; Danny, back from his trip (Review 3), offers to help paint the walls at the weekend in exchange for pizza and Grandma Lourdes's chicken soup (Unit 16). In the homework, Kate writes on her blog about a makeover at Sweet Kate Bakery in Chicago. No external facts in this unit.""",
        """<i>I cut my hair</i> / <i>I'm going to fix my car</i> for jobs other people do, wrong word order (<i>I had painted the walls</i> for <i>I had the walls painted</i>), the base form instead of the participle (<i>had it fix</i>), and <i>reform</i> for <i>renovate / remodel</i>. Pronunciation: silent b in <i>plumber</i>.""",
        "Track 31.1 Ana's new kitchen (natural and slow) · Track 31.2 Repeat: have something done"))

    # Page 2 - Listening
    who = [("the new cabinets", "P"), ("the leak (the first time)", "M"), ("the pipes", "P"), ("the electricity", "P"), ("the walls", "D")]
    wl = "".join(f"<li>{s} {A(w, 'min-width:6mm')}</li>" for s, w in who)
    tf = [("Ana is having the kitchen remodeled.", "T"), ("The new stove is already in the kitchen.", "F"), ("Marcos fixed the leak with a video's help.", "F"),
          ("The electrician is coming on Friday.", "T"), ("Ana thinks the painter is too expensive.", "T"), ("Danny wants to be paid for his work.", "F")]
    tfl = "".join(f"<li>{s} {A(w, 'min-width:6mm')}</li>" for s, w in tf)
    b.page(f"""{sec(2, "Listening: Ana's new kitchen", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{audiocard(["31.1 · NATURAL", "31.1 · SLOW"])}
{sub("A", "Danny calls Ana. She's having work done in her kitchen. Listen. Who does (or will do) each job? Write P (a professional), M (Marcos) or D (Danny and Ana).", "3 min", "31.1")}
<ol style="line-height:1.5;font-size:8.8pt;margin:0;columns:2">{wl}</ol></div>{img('B', 40, 27)}</div>
{sub("B", "Listen again. Write T (true) or F (false). Correct the false sentences.", "3 min")}
<ol style="line-height:1.6;font-size:8.8pt;margin:0;columns:2">{tfl}</ol>
{talk(["Was Marcos right to try to fix the leak himself? Why?", "Have you ever made something worse when you tried to fix it?", "Would you help a friend paint their home? What would you ask for in return?"])}""",
    30, """<ol><li>A–B: 6 minutes. Corrections: 2 it's coming next week · 3 he made it worse · 6 he only wants food (pizza and soup). In A, the walls are D: Ana and Danny will paint them themselves.</li>
<li>Talk about it: 6 minutes. Collect sentences with <i>I had… / I got…</i> for page 3.</li></ol>""")

    # Page 3
    lean.grammar_in_class(b, grammar_ref.have_something_done)

    # Page 4 - Practice
    fs = [("We're having the kitchen ___ (remodel).", "remodeled"), ("We're having new cabinets ___ (install).", "installed"),
          ("Last month we had the pipes ___ (check) by a plumber.", "checked"), ("We were going to have the walls ___ (paint).", "painted"),
          ("I need to get my phone ___ (repair).", "repaired")]
    fsl = "".join(f"<li><i>{s.replace('___', A(a, 'min-width:20mm'))}</i></li>" for s, a in fs)
    use = ["When did you last have your hair cut? Where?", "What do you do yourself at home, and what do you have done?", "Have you ever had something stolen? What happened?",
           "What would you like to have done in your home?", "What do you need to get fixed or checked soon (car, phone, eyes, teeth…)?"]
    b.page(f"""{sec(4, "Practice: have something done", "10 min")}
{sub("A", "Complete the sentences with the past participle of the verbs.", "3 min")}
<ol style="line-height:1.85;font-size:8.9pt;margin:0">{fsl}</ol>
{sub("B", "Choose.", "2 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0"><li>I went to the hairdresser and {ch(["cut my hair", "had my hair cut"], "had my hair cut")}.</li>
<li>Marcos {ch(["fixed the leak", "had the leak fixed"], "had the leak fixed")} by a plumber in the end.</li>
<li>We {ch(["had the walls painted", "had painted the walls"], "had the walls painted")} by a professional.</li></ol>
<div class="box sand"><h4>RULE</h4><b>have / get + object + past participle</b> = someone else does the job for you · <b>have</b> changes tense (<i>I'm having, I had, I'll have</i>) · <b>by</b> + the person, only if important. See the <b>Grammar reference</b> on page 3.</div>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    24, """<ol><li>A–B: 4 minutes. In B3, explain the difference: <i>had painted the walls</i> = past perfect (they did it themselves, before).</li>
<li>Use it: 6 minutes, all oral. Correct <i>I cut my hair</i> every time the student means a hairdresser.</li></ol>""")

    # Page 5 - Speaking
    probs = ["The door handle is loose.", "There's a crack in the living room wall.", "The bathroom light doesn't work.", "There's no electricity in the bedroom.",
             "The shower head is broken.", "The kitchen walls are very dirty.", "There's a leak under the sink.", "You lost one of the keys."]
    pl = "".join(f"<li>{p}</li>" for p in probs)
    b.page(f"""{sec(5, "Speaking: the new apartment", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.3pt"><tr><th>reporting a problem</th><th>asking for action</th><th>offering a solution</th><th>agreeing a deal</th></tr>
<tr><td><i>There's a problem with… · … doesn't work. · … is loose / broken / leaking.</i></td><td><i>Could you have it fixed? · When can you get someone to check it?</i></td><td><i>You'll need to tighten the screws. · Check the fuse box. · I'll have it replaced.</i></td><td><i>OK, if you… I'll… · That's fair. · Who's going to pay for it?</i></td></tr></table></div>
{audiocard(["31.2"])}
{sub("A", "Listen and repeat. Stress the object and the participle (pipes checked, kitchen remodeled).", "4 min", "31.2")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S312))}</p>
{sub("B", "Role-play. You've just moved into an old apartment. You find these problems. Your teacher is the landlord. Report each problem and agree who will fix it: you (DIY) or a professional, and who will pay.", "14 min")}
<ol style="line-height:1.45;font-size:8.8pt;margin:0;columns:2">{pl}</ol>
{talk(["Should landlords or tenants pay for small repairs? Why?", "Which home jobs should always be done by a professional?"], "TALK ABOUT IT")}""",
    35, """<ol><li>A: the stress falls on the object and the participle; <i>have / had</i> is weak.</li>
<li>B: 12 minutes. As the landlord, offer DIY solutions first (<i>You just need to tighten the screws / change the bulb / check the fuse box</i>) and only have the big jobs done (the leak, the crack, the electricity). The lost key is the tenant's cost: the student should have the lock changed or a key copied. Last 3 minutes: wrap-up (two corrections, and ask <i>Can you now explain what you need to have done at home?</i>).</li></ol>""")

    # Homework
    pc = [(["had", "made"], "had"), (["painted", "paint"], "painted"), (["installed", "install"], "installed"), (["get", "do"], "get"), (["fixed", "fix"], "fixed")]
    p = [ch(o, a) for o, a in pc]
    rw = [("A hairdresser cut my hair yesterday. (have)", "I had my hair cut yesterday."), ("A mechanic is going to check our car. (get)", "We're going to get our car checked."),
          ("Someone stole Danny's phone on the bus. (have)", "Danny had his phone stolen on the bus.")]
    rwl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Kate writes on her bakery blog in Chicago. Choose the correct words.", "")}</div>{img('C', 28, 18)}</div>
<div class="box" style="line-height:1.85;font-size:8.8pt;margin:.5mm 0"><b>Sweet Kate's blog · Our bakery makeover</b><br>We closed for a week in January and {p[0]} the whole bakery renovated. First, we had the walls {p[1]} a warm yellow. Then we had new lights {p[2]} over the counter. My brother Tom offered to fix the old oven himself, but I said no! We had to {p[3]} a professional to do it, and now it's working perfectly. The only thing we still need to have {p[4]} is the front door. Come and see us!</div>
{sub("B", "Rewrite the sentences with have or get something done.", "")}
<ol style="line-height:1.5;font-size:8.7pt;margin:0">{rwl}</ol>
{lean.watch_out([("We're going to reform the kitchen.", "We're going to renovate / remodel the kitchen.", "<i>reform</i> is for laws and systems, not houses."), ("The lamp burned.", "The bulb has gone / burned out.", "change the <b>bulb</b>, not the lamp."), ("I'll call the plumber to arrange the pipes.", "I'll call a plumber to fix / repair the pipes.", "<i>arrange</i> = organize.")])}
{lean.writing_task(sub, "Describe the home improvements you would like to make where you live. What would you do yourself, and what would you have done by a professional? Why?", "If I had the money, I'd have the kitchen…", ["three things you'd have done", "two things you'd do yourself (DIY)", "reasons", "100–150 words"], "I can talk about repairs and things I have done by professionals.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class. The writing task is from the Linguahouse lesson. Read it at home and choose two mistakes to discuss in class.</p>""")

    script = "".join(f"<p style='margin:.4mm 0'><b>{l.split(': ', 1)[0]}:</b> {l.split(': ', 1)[1]}</p>" for l in S311)
    b.extra("Audio script", f"""
{sub("31.1", "Ana's new kitchen (natural and slow)")}
<div style="line-height:1.3;font-size:8.6pt">{script}</div>
{sub("31.2", "Repeat: have something done")}
<p>{" · ".join(S312)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 31 - Home improvements")
