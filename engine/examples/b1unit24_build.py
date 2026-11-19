# Speak! Progress B1 - Unit 24 "For and against" (all English) - LEAN B1 format: 4 class pages + 2 home pages (pilot 2026-11-19)
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Progress"
setup(band="B1 · UNIT 24", audio_json="audio_b1-unit-24.json", img_dir="img")


_r = json.load(open("roteiro.json"))["units"]["b1-unit-24"]
S241 = [l.replace("five euros", "€5").replace("or ten", "or €10") for l in _r["24.1 Is tourism good for a town"].split("\n")]
S242 = [x.split(": ", 1)[1] for x in _r["24.2 Repeat: agreeing and disagreeing"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'
    def lines(n):
        return '<div class="wline"></div>' * n
    def talk(qs, title="TALK ABOUT IT"):
        return f'<div class="box sand" style="margin-top:1.5mm"><h4>{title}</h4><ol style="margin:0;line-height:1.5;font-size:8.9pt">' + "".join(f"<li>{q}</li>" for q in qs) + "</ol></div>"

    # ---------- IN CLASS ----------
    # Page 1 - Warm-up
    cover = cover_html(T, "LEVEL B1 · UNIT 24", "For and against", "Tourism: good or bad? · <b>although, however, despite, on the other hand</b>",
                       [("YOU CAN", "discuss the pros and cons of an issue, agree and disagree politely, and contrast ideas"),
                        ("LANGUAGE", "a tourist trap · nightlife · locals · run-down · That may be true, but… · despite the crowds"),
                        ("PRONUNCIATION", "strong and polite disagreement")])
    kw = [("visiting interesting places on vacation", "sightseeing"), ("bars, clubs and shows in the evening", "nightlife"),
          ("a place that charges tourists too much", "a tourist trap"), ("people who live in a place", "locals"),
          ("in very bad condition", "run-down"), ("how comfortable people's lives are", "the standard of living")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:22mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Warm-up: tourists everywhere", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["What kind of vacations do you enjoy? Why?", "What's the most crowded tourist place you've been to?", "Do tourists visit your city? Do locals like them?"], "START TALKING")}</div></div>
{sub("A", "Key words. Write the words from the box next to the definitions.", "3 min")}
<div class="bank">locals · nightlife · run-down · sightseeing · the standard of living · a tourist trap</div>
<div style="font-size:8.7pt">{twocol(kwl, 3)}</div>
{talk(["Name a tourist trap you know. Why is it a trap?", "Is the nightlife good where you live?"], "USE THE WORDS")}""",
    26, """<ol><li>Start with the questions in the top box: this is speaking time, not a test. 4 minutes.</li>
<li>A: quick check (3 minutes), then the student answers the two questions with the new words. <i>Locals</i> is a noun here (= local people).</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", """
<table><tr><th>Stage</th><th>Where</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>class</td><td>7 min</td><td>Discussion · 6 key words · questions with the words</td><td>1</td></tr>
<tr><td>2 Listening</td><td>class</td><td>13 min</td><td>Podcast debate: is tourism good for a town? · Talk about it</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>class</td><td>12 min</td><td>although, however, despite, on the other hand · Use it (oral)</td><td>3</td></tr>
<tr><td>4 Speaking</td><td>class</td><td>20 min</td><td>Agreeing and disagreeing (24.2) · debate cards</td><td>4</td></tr>
<tr><td>Wrap-up</td><td>class</td><td>3 min</td><td>Two corrections from your notes · can-do question</td><td>–</td></tr>
<tr><td>Grammar reference</td><td>home</td><td>–</td><td>although, however, despite</td><td>5</td></tr>
<tr><td>Homework</td><td>home</td><td>–</td><td>Practice · word choice · writing (100–150 words)</td><td>6</td></tr></table>
<div class="box"><h4>NEW B1 FORMAT (PILOT)</h4>This unit has <b>4 pages for the class</b> and <b>2 pages for home</b>. Each class page ends with a box of questions so the student speaks most of the time. Controlled practice, word choice and writing are homework. Check the homework quickly at the start of the next class (3–5 minutes).</div>
<div class="box sand"><h4>THE STORY</h4>The Linguahouse lesson is a discussion about a European town after a tourism boom, with expressions for agreeing and disagreeing. Our listening is an episode of Danny's podcast <i>Gap Year Diaries</i> (B1 Unit 06) with Ana and Bruno. The historic coastal town Danny visited is not named. Verified fact: Venice charges day-trippers aged 14 and over an access fee of €5 on peak days (Fridays to Sundays from April to July in 2026), or €10 if they book less than four days ahead; overnight visitors don't pay it (Euronews, 2026; Lonely Planet). Other statements in the debate are opinions.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4><i>Despite of…</i>, <i>despite + subject + verb</i>, <i>although… but…</i> in one sentence, <i>in the other hand</i>, <i>I'm agree</i>, and <i>actually</i> for <i>currently</i>. Brazilians also tend to disagree too directly in English (<i>You're wrong</i>) or too softly; teach the scale on page 4.</div>
<div class="box"><h4>AUDIO</h4>Track 24.1 Is tourism good for a town? (natural and slow) · Track 24.2 Repeat: agreeing and disagreeing</div>""")

    # Page 2 - Listening
    gist = ["Everyone agrees that tourism is good.", "They have different opinions.", "Everyone agrees that tourism is bad."]
    who = [("Tourism creates jobs and improves the standard of living.", "Ana"), ("Rent is too expensive for locals because of vacation rentals.", "Bruno"),
           ("The town was full of tourist traps.", "Danny"), ("Tourist money helps to restore old buildings.", "Ana"),
           ("Venice charges day-trippers a fee.", "Bruno"), ("A small fee won't stop people from visiting Venice.", "Ana"), ("The nightlife is bad for locals.", "Bruno")]
    wl = "".join(f"<li>{s} {A(w, 'min-width:13mm')}</li>" for s, w in who)
    b.page(f"""{sec(2, "Listening: is tourism good for a town?", "13 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{audiocard(["24.1 · NATURAL", "24.1 · SLOW"])}
{sub("A", "Danny, Ana and Bruno discuss tourism on Danny's podcast. Listen. What happens?", "2 min", "24.1")}
<p style="margin:.3mm 0;font-size:8.9pt">{ch(gist, gist[1])}</p></div>{img('B', 40, 27)}</div>
{sub("B", "Listen again. Who says it? Write Ana, Bruno or Danny.", "4 min")}
<ol style="line-height:1.55;font-size:8.8pt;margin:0">{wl}</ol>
{talk(["Who do you agree with most: Ana, Bruno or Danny? Why?", "Should popular cities charge tourists a fee? How much?", "Vacation rentals: good for travelers, bad for locals?"])}""",
    29, """<ol><li>A–B: 6 minutes. Play the natural version; use the slow one only if needed. The Venice fact is real (see the story box).</li>
<li>Talk about it: 7 minutes. Take the opposite side to make the student defend their opinion; note useful phrases they need for page 4.</li></ol>""")

    # Page 3 - Language focus
    fs = [("___ the crowds, a lot of locals are better off.", "Despite"), ("___ it was beautiful, the center was full of tourist traps.", "Although"),
          ("I don't know. ___, it shows that the problem is real.", "However"), ("___ the fee, I'd still go tomorrow.", "In spite of"),
          ("The nightlife is great for tourists. ___, the locals can't sleep!", "On the other hand")]
    fsl = "".join(f"<li><i>{s.replace('___', A(a, 'min-width:24mm'))}</i></li>" for s, a in fs)
    use = ["Talk about your city: <i>Although it's…, …</i>", "Talk about your job or studies: <i>Despite…, I…</i>", "Give one good point about social media. <i>On the other hand, …</i>",
           "Talk about a trip: <i>It was… However, …</i>", "Compare two cities: <i>…, whereas…</i>"]
    b.page(f"""{sec(3, "Language focus: although, however, despite", "12 min")}
{sub("A", "Complete the sentences from the podcast with the words in the box.", "3 min")}
<div class="bank">although · despite · however · in spite of · on the other hand</div>
<ol style="line-height:1.85;font-size:8.9pt;margin:0">{fsl}</ol>
{sub("B", "Choose.", "2 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0"><li><i>Although</i> is followed by {ch(["subject + verb", "a noun"], "subject + verb")}.</li>
<li><i>Despite / In spite of</i> are followed by {ch(["subject + verb", "a noun or -ing"], "a noun or -ing")}.</li>
<li><i>However</i> and <i>On the other hand</i> usually start {ch(["a new sentence", "the same sentence"], "a new sentence")}.</li></ol>
<div class="box sand"><h4>RULE</h4><b>although</b> + subject + verb · <b>despite / in spite of</b> + noun / -ing (never <i>despite of</i>) · <b>However,</b> / <b>On the other hand,</b> + new sentence. More at home: <b>Grammar reference</b>, page 5.</div>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    24, """<ol><li>A–B: 5 minutes. Point to the form after each word; the full explanation is on page 5 for home.</li>
<li>Use it: 7 minutes, all oral. Accept any logical idea; correct only the structure. Push for two sentences each time.</li></ol>""")

    # Page 4 - Speaking
    st = ["Tourists should pay a fee to visit popular cities.", "Vacation rentals should be limited in city centers.", "Travel broadens the mind.",
          "Social media is a waste of time.", "English is an easy language to learn.", "It's better to visit one place slowly than many places fast.",
          "The best movies were made a long time ago.", "Everyone should learn a second language at school."]
    stl = "".join(f"<li>{x}</li>" for x in st)
    b.page(f"""{sec(4, "Speaking: for and against", "20 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.3pt"><tr><th>asking</th><th>giving an opinion</th><th>adding / contrasting</th><th>agreeing</th><th>disagreeing</th></tr>
<tr><td><i>What do you think? · What's your opinion about…?</i></td><td><i>I think… · In my opinion… · I feel… · I'd say…</i></td><td><i>On top of that… · What's more… · However… · On the other hand…</i></td><td><i>I totally agree. · That's true. · Absolutely. · You're right.</i></td><td><i>That may be true, but… · I'm not sure about that. · I disagree. · You must be joking!</i></td></tr></table></div>
{audiocard(["24.2"])}
{sub("A", "Listen and repeat. Then mark each phrase: +++ strong, ++ normal, + polite.", "4 min", "24.2")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x} {A(m, 'min-width:7mm')}" for i, (x, m) in enumerate(zip(S242, ["agree", "agree", "+", "+", "+", "++", "+++", "+++"])))}</p>
{sub("B", "Debate. Choose a statement. Give your opinion and two reasons. Your teacher disagrees, so defend your opinion. Then choose another one.", "14 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0;columns:2">{stl}</ol>
{talk(["When is it better to disagree politely? Give examples (your boss, a friend, a client…).", "Is it easy for you to disagree in English? Why?"], "TALK ABOUT IT")}""",
    26, """<ol><li>A: <i>That may be true, but… / You could be right, but… / I'm not sure about that</i> are polite (+); <i>I disagree</i> is normal (++); <i>You must be joking! / Come on!</i> are strong (+++), only with friends.</li>
<li>B: always take the other side. After each debate, give one correction and one phrase to upgrade (<i>I think → I'd say</i>). Last 3 minutes: wrap-up (two corrections, and ask <i>Can you now disagree politely in English?</i>).</li></ol>""")

    # ---------- AT HOME ----------
    grammar_ref.contrast_linkers(b)

    pc = [(["Although", "Despite"], "Although"), (["despite", "although"], "despite"), (["However", "Although"], "However"), (["On top of that", "On the other hand"], "On top of that"),
          (["in spite of", "although"], "in spite of")]
    p = [ch(o, a) for o, a in pc]
    rw = [("The hotel was expensive. We loved it. (although)", "Although the hotel was expensive, we loved it."), ("It rained. We went to the beach. (despite)", "Despite the rain, we went to the beach."),
          ("The city is beautiful. It's very crowded. (however)", "The city is beautiful. However, it's very crowded.")]
    rwl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Kate writes on her blog about tourists in her neighborhood in Chicago. Choose the correct words.", "")}</div>{img('C', 28, 18)}</div>
<div class="box" style="line-height:1.85;font-size:8.8pt;margin:.5mm 0"><b>Sweet Kate's blog · Tourists on my street</b><br>{p[0]} I love my customers, summer is a strange time on my street. Tourists fill the sidewalks {p[1]} the heat, and they take photos of everything, even my cupcakes! {p[2]}, I can't complain: my sales double in July. {p[3]}, many visitors leave nice reviews online. So, {p[4]} the noise and the lines, I say: welcome, tourists!</div>
{sub("B", "Join the sentences with the word in brackets.", "")}
<ol style="line-height:1.5;font-size:8.7pt;margin:0">{rwl}</ol>
<div class="box sand" style="margin:1mm 0"><h4>WATCH OUT: WORD CHOICE</h4>
<table style="margin:0;font-size:8.1pt"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>I'm agree.</td><td><b>I agree.</b></td><td><i>agree</i> is a verb, not an adjective.</td></tr>
<tr><td>Actually, tourism is growing.</td><td><b>Currently / At the moment, tourism is growing.</b></td><td><i>actually</i> = in fact.</td></tr>
<tr><td>In my opinion, I think…</td><td><b>In my opinion… / I think…</b></td><td>use one, not both.</td></tr></table></div>
{sub("C", "Writing (100–150 words, in your notebook). Is tourism good for your city? Give points for and against, and your opinion. Use although, however, despite and on the other hand.", "")}
<p class="small" style="margin:.3mm 0"><b>Start like this:</b> <i>Tourism brings money to my city. However, …</i> &nbsp;☐ for &nbsp;☐ against &nbsp;☐ your opinion &nbsp;☐ four linkers &nbsp;☐ 100–150 words</p>
<p class="small" style="margin:.3mm 0"><b>Can do:</b> I can discuss the pros and cons of an issue and disagree politely. ☐ Easy! ☐ Sometimes ☐ Not yet</p>""",
    20, """<p>Check A and B in 3 minutes at the start of the next class. Read the writing at home and choose two mistakes to discuss in class.</p>""")

    script = "".join(f"<p style='margin:.5mm 0'><b>{l.split(': ', 1)[0]}:</b> {l.split(': ', 1)[1]}</p>" for l in S241)
    b.extra("Audio script", f"""
{sub("24.1", "Is tourism good for a town? (natural and slow)")}
<div style="line-height:1.3;font-size:8.6pt">{script}</div>
{sub("24.2", "Repeat: agreeing and disagreeing")}
<p>{" · ".join(S242)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 24 - For and against")
