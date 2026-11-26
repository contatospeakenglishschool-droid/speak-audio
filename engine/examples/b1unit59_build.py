# Speak! Progress B1 - Unit 59 "War and conflict" (all English) - lean B1 format
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
setup(band="B1 · UNIT 59", audio_json="audio_b1-unit-59.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-59"]
S591 = [l.split(": ", 1) for l in _r["59.1 Gap Year Diaries: The Last Bridge"].split("\n")]
S592 = [x.split(": ", 1)[1] for x in _r["59.2 Repeat: past perfect continuous"].split("\n")]




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
    cover = cover_html(T, "LEVEL B1 · UNIT 59", "War and conflict", "Talking about war films and the news · <b>they'd been fighting for years…</b>",
                       [("YOU CAN", "talk about war and conflict, review a film and tell a story with the past perfect continuous"),
                        ("LANGUAGE", "troops · truce · casualties · invade · advance / retreat · release hostages · past perfect continuous"),
                        ("PRONUNCIATION", "weak form of had been: they'd been /ðeɪd bɪn/")])
    words = ["allies", "casualties", "civilian", "invade", "outbreak", "troops", "truce", "wounded"]
    defs = {"allies": "countries or groups that are on the same side", "casualties": "people who are injured or killed in a war or an accident",
            "civilian": "a person who is not a soldier", "invade": "to enter a country by force with an army",
            "outbreak": "the start of a war or a disease", "troops": "groups of soldiers",
            "truce": "an agreement to stop fighting for a period of time", "wounded": "injured, especially by a weapon"}
    order = [4, 7, 0, 6, 1, 3, 5, 2]
    kwl = "".join(f'<li>{A(words[i], "min-width:24mm")} <span style="color:#6b7377">= {defs[words[i]]}</span></li>' for i in order)
    b.page(f"""{sec(1, "Warm-up: war on screen", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["Look at the photo. What story could this old helmet tell?", "Do you like war films or series? Which one do you remember best?", "Why do you think people make so many films about war?"], "START TALKING")}</div></div>
{sub("A", "Key words. Write the words from the box next to their meanings.", "3 min")}
<div class="bank">{" · ".join(words)}</div>
<ol style="font-size:8.6pt;line-height:1.7;margin:0">{kwl}</ol>
{talk(["Which words do you often hear in the news?", "Who suffers most in a war: soldiers or civilians? Why?", "Do you think there are more conflicts now than in the past?"], "USE THE WORDS")}""",
    30, """<ol><li>This topic can be sensitive. If the student has a personal or family connection to a conflict, keep the focus on films and vocabulary, and let them decide how much to share.</li>
<li>A: 4 minutes. Note <i>casualties</i> includes the injured, not only the dead; <i>wounded</i> /ˈwuːndɪd/ rhymes with <i>food</i>.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Gap Year Diaries: a review of the film The Last Bridge · opposites · true or false · Talk about it",
                      "past perfect continuous (had been + -ing): duration up to a past moment, causes, expectations; vs past perfect simple", "Choose the correct form · explain the situation · Use it (oral)",
                      "weak form had been (59.2) · contradicting · radio war role-play · long turn: a war film or book", "collocations (release hostages, spread propaganda…) · watch out · writing: a film review"),
        """The Linguahouse lesson is a vocabulary worksheet with no listening or reading: a dialogue between a government and rebels (opposites), sentences with real historical wars, dates and casualty numbers, and terrorism collocations. We did not use the historical sentences, because we cannot check every date and number. Instead, we created a Gap Year Diaries episode: on movie night at the hostel, Danny and Bruno review The Last Bridge, an invented war film set in an invented country. The rebels and the government had been fighting for six years; the rebels had captured an old bridge; Lena, a nurse who'd been working near the bridge for twenty years, treats soldiers from both sides; the rebels take hostages (including her brother) and both sides spread propaganda; Lena helps negotiate a truce and a prisoner exchange. Danny gives it four stars; Bruno three and a half (too long; he'd been hoping for more action). We kept all the Linguahouse vocabulary, the opposites dialogue (now a role-play), the collocations and the talking points, and added a new B1 grammar point: the past perfect continuous.""",
        """<i>They were fighting for six years when…</i> (→ <i>had been fighting</i>); <i>I had been knowing him</i> (→ <i>had known</i>). Vocabulary: <i>The thieves invaded the house</i> (→ <i>broke into</i>); <i>the soldiers were hurted</i> (→ <i>wounded / injured</i>).""",
        "Track 59.1 Gap Year Diaries: The Last Bridge (natural and slow; Danny and Bruno) · Track 59.2 Repeat: past perfect continuous"))

    # Page 2 - Listening
    opp = [("advance", "retreat"), ("alive", "dead"), ("soldier", "civilian"), ("capture", "release"), ("rebel", "loyalist"), ("attack", "defend")]
    oppl = "".join(f'<li>{a} ↔ {A(o, "min-width:20mm")}</li>' for a, o in opp)
    tf = [("When the film starts, the war has just broken out.", "F: they had been fighting for six years."),
          ("Lena only helped soldiers from the government.", "F: she treated everyone."),
          ("The government said the rebel leader was dead.", "T: but he was still alive."),
          ("The film ends with a big battle.", "F: people talk at a table; they negotiate a truce.")]
    tfl = "".join(f"<li>{s} <b>T / F</b> {R(a)}</li>" for s, a in tf)
    b.page(f"""{sec(2, "Listening: The Last Bridge", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
<p style="margin:0 0 1mm;font-size:8.8pt">It's movie night at the hostel. On their podcast, Gap Year Diaries, Danny and Bruno review a war film called <i>The Last Bridge</i>. The film and the country are invented.</p>
{sub("A", "Listen. Did they like the film? How many stars does each one give?", "3 min")}
<p style="margin:0;font-size:8.7pt;line-height:1.7">Danny {A("four out of five", "min-width:34mm")} &nbsp; Bruno {A("three and a half (too long)", "min-width:40mm")}</p></div>{img('B', 38, 26)}</div>
{audiocard(["59.1 · NATURAL", "59.1 · SLOW"])}
<div style="display:flex;gap:4mm"><div style="flex:.8">
{sub("B", "Opposites. Write the opposite. Most pairs are in the review.", "3 min")}
<ol style="line-height:1.55;font-size:8.5pt;margin:0;columns:2;column-gap:3mm">{oppl}</ol></div><div style="flex:1.2">
{sub("C", "Listen again. True (T) or false (F)?", "3 min")}
<ol style="line-height:1.4;font-size:8.3pt;margin:0">{tfl}</ol></div></div>
<p style="margin:.6mm 0;font-size:8.6pt"><b>Think about it:</b> Bruno says "Both sides lied all the time. That felt very real." What does he mean? {A("in a war, each side uses propaganda; the truth is often the first victim", "min-width:20mm")}</p>
{talk(["Would you watch The Last Bridge? Why or why not?", "Do you prefer war films with a lot of action or with more dialogue?", "Why do you think Lena helped both sides?"])}""",
    35, """<ol><li>A: play the natural version; play the slow one if needed.</li>
<li>B: <i>retreat</i> and <i>defend</i> are not in the review; the other pairs are (<i>alive / dead, soldiers / civilians, captured / release, rebel / loyalist</i>).</li>
<li>Then ask the student to find <i>had been</i> + -ing: <i>had been fighting, She'd been working, I'd been expecting, I'd been hoping</i>. They come back on page 3.</li></ol>""")

    # Page 3
    lean.grammar_in_class(b, grammar_ref.past_perfect_continuous)

    # Page 4 - Practice
    pc = [("When the film started, they", ["were fighting", "had been fighting"], "had been fighting", "for six years."),
          ("Lena was exhausted. She", ["had been working", "has been working"], "had been working", "all night."),
          ("They", ["had been knowing", "had known"], "had known", "each other since school."),
          ("By the evening, she", ["had treated", "had been treating"], "had treated", "forty soldiers."),
          ("His boots were muddy. He", ["had been walking", "has walked"], "had been walking", "in the rain."),
          ("How long", ["they had been", "had they been"], "had they been", "negotiating?"),
          ("Danny's eyes were red. He", ["has been crying", "had been crying"], "had been crying", "at the end."),
          ("We", ["had been waiting", "have been waiting"], "had been waiting", "for an hour when the film began.")]
    cl = "".join(f"<li>{a} {ch(o, r)} {z}</li>" for a, o, r, z in pc)
    rw = [("The soldiers were exhausted. (march / all night)", "They had been marching all night."),
          ("Lena's hands were shaking. (operate / for ten hours)", "She had been operating for ten hours."),
          ("Bruno was angry when he arrived. (wait for the bus / for an hour)", "He had been waiting for the bus for an hour.")]
    rwl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw)
    use = ["What had you been doing just before this class started?", "Think of a day you were exhausted. What had you been doing?",
           "Have you ever been disappointed by a film? What had you been expecting?", "How long had you been studying English when you started classes with me?",
           "When you met your best friend, how long had you been living in that place?"]
    b.page(f"""{sec(4, "Practice: they'd been fighting for years", "10 min")}
{sub("A", "Choose the correct words.", "3 min")}
<ol style="line-height:1.7;font-size:8.6pt;margin:0;columns:2;column-gap:6mm">{cl}</ol>
{sub("B", "Explain the situation. Use had been + -ing.", "4 min")}
<ol style="line-height:1.45;font-size:8.7pt;margin:0">{rwl}</ol>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    30, """<ol><li>A: 3 minutes. Item 3: <i>know</i> is a state verb. Item 4: a number (forty) → past perfect simple.</li>
<li>B: contractions are fine and natural: <i>They'd been marching…</i></li>
<li>Use it: 3 minutes, all oral. Accept the past perfect simple with state verbs (<i>I'd lived there for…</i> is also correct).</li></ol>""")

    # Page 5 - Speaking
    gov = [("The rebels are losing the war.", "No, that's a lie. The loyalists are losing."),
           ("The rebel leader is dead.", "That's not true. He's still alive."),
           ("Our troops are advancing toward the bridge.", "That's not correct. Your troops are retreating."),
           ("The rebels are going to release all the prisoners.", "On the contrary, we're going to capture more loyalists."),
           ("There are only soldiers near the bridge.", "That's not what's happening. There are mostly civilians."),
           ("The rebels are only defending their positions.", "Wrong! We're preparing to attack.")]
    gl = "".join(f"<li><i>{g}</i>{(' ' + R('→ ' + a)) if T else ''}</li>" for g, a in gov)
    b.page(f"""{sec(5, "Speaking: that's not true!", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE: CONTRADICTING AND REVIEWING A FILM</h4>
<table style="margin:0;font-size:8.2pt"><tr><th>contradicting</th><th>strongly</th><th>about a film</th><th>giving a verdict</th></tr>
<tr><td><i>That's not true. · That's not correct. · That's not what's happening.</i></td><td><i>That's a lie! · On the contrary… · Nonsense!</i></td><td><i>It's set in… · At the start, … had been… · The acting is…</i></td><td><i>I'd give it… stars. · It's worth watching. · It's too long.</i></td></tr></table></div>
{audiocard(["59.2"])}
{sub("A", "Listen and repeat. Say had been quickly: they'd been /ðeɪd bɪn/.", "2 min", "59.2")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S592))}</p>
{sub("B", "Radio war. In The Last Bridge, both sides have a radio station. Your teacher reads the government news. You are the rebels' radio: contradict each one with the opposite.", "5 min")}
<ol style="line-height:1.45;font-size:8.4pt;margin:0">{gl}</ol>
{sub("C", "Discuss. How have wars changed? Why do people take hostages? Should governments agree to their demands?", "4 min")}
{sub("D", "Long turn. Tell your teacher the story of a war film, series or book you know. Start with the situation: At the start, … had been… Then say what happened and give it stars.", "4 min")}""",
    30, """<ol><li>B comes from the Linguahouse civil war dialogue. Read the government lines like a radio presenter; the student answers with the opposite and functional language. Then swap roles.</li>
<li>C and D come from the Linguahouse questions. Last 3 minutes: wrap-up (two corrections, and ask <i>Can you now review a film and tell a story with the past perfect continuous?</i>).</li></ol>""")

    # Homework
    bank = ["agree to the demands", "hijack a plane", "negotiate a prisoner exchange", "plant a bomb", "release some hostages", "spread propaganda"]
    sents = [("Lena helped both sides", 2, ": five rebels for ten hostages."), ("Both sides used the radio to", 5, "and make people afraid."),
             ("In the thriller, two men try to", 1, "and fly it to an island."), ("After twelve hours of talks, the rebels decided to", 4, ", mainly the older people."),
             ("The government didn't want to", 0, ", so the talks continued."), ("The police caught the man before he could", 3, "under the bridge.")]
    sl = "".join(f'<li>{a} {A(bank[i], "min-width:40mm")}{"" if z[0] in ",:" else " "}{z}</li>' for a, i, z in sents)
    b.page(f"""{sec("H", "Homework", "at home")}
{sub("A", "Collocations. Complete the sentences with the phrases from the box.", "")}
<div class="bank">{" · ".join(bank)}</div>
<ol style="line-height:1.6;font-size:8.6pt;margin:0">{sl}</ol>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("B", "Complete with the past perfect continuous or the past perfect simple.", "")}
<ol style="line-height:1.7;font-size:8.6pt;margin:0">
<li>When the truce was signed, the two sides {A("had been fighting", "min-width:28mm")} (fight) for six years.</li>
<li>By the end of the film, the bridge {A("had been destroyed", "min-width:28mm")} (destroy).</li>
<li>Bruno was hungry because he {A("hadn't eaten", "min-width:28mm")} (not eat) anything since lunch.</li>
<li>I {A("had been hoping", "min-width:28mm")} (hope) for a happy ending, but there wasn't one.</li></ol></div>{img('C', 30, 22)}</div>
{lean.watch_out([("They were fighting for six years when the war ended.", "They had been fighting for six years when the war ended.", "duration up to a past moment → <i>had been</i> + -ing."), ("Thieves invaded my house last night.", "Thieves broke into my house last night.", "<i>invade</i> = an army enters a country."), ("Many soldiers were hurted.", "Many soldiers were wounded / injured.", "<i>wounded</i> = by a weapon; <i>hurt</i> is irregular.")])}
{lean.writing_task(sub, "Write a review of a film or series about war or conflict for Danny's blog. Don't tell the ending!", "The film is set in…", ["where and when it's set", "the situation at the start (had been + -ing)", "what you liked and didn't like", "how many stars you give it", "100–150 words"], "I can talk about war and conflict, review a film and tell a story with the past perfect continuous.")}""",
    25, """<p>Check A and B in 3 minutes at the start of the next class. A comes from the Linguahouse collocations exercise, with new sentences about films. In B, item 2 is passive (<i>had been destroyed</i>), not continuous: a good contrast to discuss. Read the writing at home and choose two mistakes to discuss in class.</p>""")

    def scr(lst):
        return "".join(f"<p style='margin:.4mm 0'><b>{n}:</b> {t}</p>" for n, t in lst)
    b.extra("Audio script", f"""
{sub("59.1", "Gap Year Diaries: The Last Bridge (natural and slow; Danny and Bruno)")}
<div style="line-height:1.28;font-size:8.2pt">{scr(S591)}</div>
{sub("59.2", "Repeat: past perfect continuous")}
<p>{" · ".join(S592)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 59 - War and conflict")
