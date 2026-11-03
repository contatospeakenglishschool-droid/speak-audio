# Speak! Bridge A2 - Unit 16 "Fashion forward" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 16", audio_json="audio_a2-unit-16.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["a2-unit-16"]
PARAS = [x.split(": ", 1)[1] for x in _r["16.1 Article"].split("\n")]
S162 = [x.split(": ", 1)[1] for x in _r["16.2 Repeat words"].split("\n")]
S163 = [x.split(": ", 1)[1] for x in _r["16.3 Repeat sentences"].split("\n")]


def _article():
    t, ps = PARAS[0], PARAS[1:]
    # quotes are spoken without quotation marks in the audio; add them back for print
    ps[1] = ps[1].replace("Denim is a material that lasts for years, she says. The jeans that people throw away are perfect for new clothes.",
                          "“Denim is a material that lasts for years,” she says. “The jeans that people throw away are perfect for new clothes.”")
    ps[2] = ps[2].replace("Sewing is a skill that everybody can learn, says Grace. And the clothes you make yourself are always special.",
                          "“Sewing is a skill that everybody can learn,” says Grace. “And the clothes you make yourself are always special.”")
    ps[0] = ps[0].replace("in one season and out the next", "“in” one season and “out” the next")
    ps[0] = ps[0].replace("seventeen million", "17 million").replace("twenty eighteen", "2018")
    body = "".join(f"<p style='margin:0 0 1.2mm'><b>{i+1}</b> {p}</p>" for i, p in enumerate(ps))
    return f"""<div class="box" style="margin-top:1mm;font-size:8.9pt;line-height:1.38"><h4 style="font-size:11pt">{t.split('. ')[0]}<br><span style="font-weight:400;font-style:italic">{t.split('. ')[1]}</span></h4>
<div style="columns:2;column-gap:5mm">{body}</div></div>"""


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 16", "Fashion forward", "Green fashion · <b>relative clauses: who, which, that, where</b>",
                       [("YOU CAN", "explain and define people, things and places in one sentence"),
                        ("LANGUAGE", "Grace is a designer who makes jackets. · A thrift store is a place where you buy second-hand clothes."),
                        ("PRONUNCIATION", "deSIGNer · MAterial · enVIronment · DEnim")])
    g1 = [("Crafts", "like knitting and sewing are popular again."), ("materials", "We can make clothes from natural ___ like wool and cotton."),
          ("fashion industry", "Millions of people around the world work in the ___."), ("Designers", "___ create new clothes and show them at fashion shows.")]
    g2 = [("environment", "Cycling is better for the ___ than driving."), ("Organic", "___ farmers don't use chemicals."),
          ("recycled", "Glass, plastic and paper can be ___."), ("second-hand", "A ___ car is cheaper than a new one.")]
    def gap(items):
        out = []
        for i, (w, s) in enumerate(items):
            s = s if "___" in s else "___ " + s
            out.append(f'<li value="{i+1}">{s.replace("___", A(w, "min-width:20mm"))}</li>')
        return "".join(out)
    b.page(f"""{sec(1, "Warm-up: fashion words", "8 min")}
<div style="display:flex;gap:4mm;align-items:flex-start">
<div style="width:46mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo('A')}" style="width:46mm;height:34mm;object-fit:cover;display:block"></div>
<div style="flex:1">{sub("A", "Complete the sentences with the words in the boxes.", "5 min")}
<div class="bank">Group 1: crafts · designers · fashion industry · materials</div>
<ol>{gap(g1)}</ol></div></div>
<div class="bank">Group 2: environment · organic · recycled · second-hand</div>
<ol>{gap(g2)}</ol>
{sub("B", "Talk about it.", "3 min")}
<ol><li>Look at the clothes you're wearing today. What materials are they made of?</li><li>Do you ever buy second-hand clothes? Can you knit or sew?</li></ol>""",
    22, """<ol><li>A: <b>second-hand</b> = used before by another person; <b>organic</b> = without chemicals. Sentence 1 of Group 1 starts with a capital letter: <i>Crafts</i>.</li>
<li>B: <i>made of</i> + material (Unit 15): <i>It's made of cotton.</i></li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Fashion and environment vocabulary</td><td>1</td></tr>
<tr><td>2 Reading</td><td>10 min</td><td>Magazine article: Can fashion be green?</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Defining relative clauses: who, which, that, where</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>who / that / where · two sentences into one · leaving out the pronoun</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>5 min</td><td>Word stress · relative clauses as one unit</td><td>5</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Two sentences into one · Word builder: materials</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Definitions game</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework (50–75 words)</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Paulo, our photographer in New York, took the photos for this magazine article. The article is read by the reporter (voice Studio-O). Grace Kim and her Chicago studio are invented. Fact: Americans generated about 17 million tons of textile waste in 2018, and landfills received about 11.3 million tons of it, about two thirds (U.S. Environmental Protection Agency, "Textiles: Material-Specific Data"). <b>Thrift stores</b> are stores that sell donated second-hand clothes, often for charity; they're very common in the U.S.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Portuguese uses one relative word for people, things and places, so students say <i>the designer which</i> ✗, <i>the store what</i> ✗ or <i>a place that you can buy…</i> ✗ (→ <b>where</b>). They also repeat the object: <i>the dress that I bought it</i> ✗.</div>
<div class="box"><h4>AUDIO</h4>Track 16.1 The article (slow and natural) · Track 16.2 Word stress · Track 16.3 Relative clauses</div>""")

    # Page 2
    fd = [("the name of a designer", "Grace Kim"), ("a material that lasts for years", "denim"),
          ("a city and a government agency", "Chicago; the EPA"), ("a type of store", "thrift stores")]
    fdl = [f'<li value="{i+1}">{q} {A(a, "min-width:30mm")}</li>' for i, (q, a) in enumerate(fd)]
    b.page(f"""{sec(2, "Reading: Can fashion be green?", "10 min")}
{sub("A", "Before you read: what do you think the article says? Then read quickly and check. (Photos: Paulo)", "3 min", "16.1 · SLOW")}
{audiocard(["16.1 · SLOW", "16.1 · NATURAL"])}
{_article()}
{sub("B", "Read again. Find these things. Then explain why they are important in the article.", "7 min", "16.1 · NATURAL")}
{twocol(fdl, 2)}""",
    22, """<p>A: elicit predictions (old clothes, trash, recycling). B: the student explains in their own words, not reading aloud: <i>Grace makes jackets out of old jeans.</i> Fact: EPA, textile waste 2018 (see the overview).</p>""")

    # Page 3
    lf = [("who", "Grace Kim is a young designer", "who wants to change this", "P2"), ("where", "She has a small studio in Chicago", "where she makes jackets and bags", "P2"),
          ("that", "Denim is a material", "that lasts for years", "P2"), ("who", "Grace also works with older women", "who know how to knit and sew", "P3"),
          ("where", "These are stores", "where you can buy second-hand clothes", "P4"), ("which", "…choose materials", "which don't damage the environment", "P5")]
    lfr = "".join(f"<tr><td><b>{p}</b></td><td>{s} {A(c, 'min-width:40mm')} ({n})</td></tr>" for p, s, c, n in lf)
    b.page(f"""{sec(3, "Language focus: who, which, that, where", "10 min")}
{sub("A", "A relative clause starts with who, which, that or where and has a verb. Complete the sentences from the article.", "4 min")}
<table style="table-layout:fixed;margin-top:0;font-size:9pt"><tr><th style="width:16mm">pronoun</th><th>example</th></tr>{lfr}</table>
{sub("B", "Choose the correct options.", "3 min")}
<ol><li>We use <i>who</i> for {ch(["things", "people"], "people")}.</li><li><i>Which</i> and <i>that</i> are for {ch(["things", "people"], "things")}. In American English, <i>that</i> is more common.</li>
<li><i>Where</i> means {ch(["in that place", "at that time"], "in that place")}.</li><li>We {ch(["use", "don't use"], "don't use")} a comma before these relative clauses.</li></ol>
{sub("C", "Look at these sentences. Which word does the relative pronoun replace?", "3 min")}
<ol><li>Grace is a young designer. <u>She</u> wants to change this. {R("she → who")}</li><li>She has a studio in Chicago. She makes bags <u>there</u>. {R("there → where")}</li>
<li>The clothes (<b>that</b>) you make yourself are special. Can we leave out <i>that</i>? {R("yes: you is the subject; that is the object")}</li></ol>
<div class="box sand"><h4>RULE</h4>People = <b>who</b> · things = <b>that / which</b> · places = <b>where</b>. Don't repeat the word: <i>the jeans that people throw away</i>, not <s>throw them away</s>. More on the next page: <b>Grammar reference</b>.</div>""",
    24, """<ol><li>A: the defining clause is necessary: without it, the sentence is incomplete (<i>Grace is a young designer…</i> which one?).</li>
<li>C3: if a subject (you, we, people) comes after <i>that</i>, we can leave it out.</li></ol>""")

    grammar_ref.defining_relative_clauses(b)

    # Page 5
    b.page(f"""{sub("D", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>She's the designer which makes bags.</td><td><b>She's the designer who makes bags.</b></td><td>people = who.</td></tr>
<tr><td>It's the store what I buy jeans.</td><td><b>It's the store where I buy jeans.</b></td><td>places = where.</td></tr>
<tr><td>The dress that I bought it is small.</td><td><b>The dress (that) I bought is small.</b></td><td>don't repeat it.</td></tr>
<tr><td>Grace is a designer, who makes jackets.</td><td><b>Grace is a designer who makes jackets.</b></td><td>no comma.</td></tr>
<tr><td>It's a person works in a store.</td><td><b>It's a person who works in a store.</b></td><td>subject: keep who.</td></tr>
<tr><td>I bought a second hand jacket.</td><td><b>I bought a second-hand jacket.</b></td><td>spelling: hyphen.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "5 min")}
{audiocard(["16.2", "16.3"])}
{sub("A", "Word stress. Listen and repeat. Underline the stressed syllable.", "2 min", "16.2")}
<table style="table-layout:fixed;margin-top:0"><tr>{"".join(f"<td style='text-align:center'><b>{w}</b></td>" for w in S162)}</tr></table>
<p class="small">{R("deSIGNer · INdustry · maTErial · enVIronment · orGAnic · reCYcled · second-HAND · DEnim")}</p>
{sub("B", "Relative clauses. Listen and repeat. Don't stop before who, that or where.", "2 min", "16.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S163)}</div>
<div class="box" style="margin-top:1mm"><h4>SILENT LETTERS</h4><b>designer</b> = de-ZAI-ner: the <i>g</i> is silent · <b>industry</b> = IN-dus-try (not in-DUS-try) · <b>material</b> = ma-TEER-ee-al.</div>""",
    24, """<ol><li>4A: Brazilians often stress <i>inDUStry</i> and say the <i>g</i> in <i>designer</i>.</li>
<li>4B: the relative clause is part of the same idea, so there is no pause before it.</li></ol>""")

    # Page 6
    pr = [("I like to wear natural materials. They don't damage the environment.", "I like to wear natural materials that don't damage the environment."),
          ("Let's go to that store. They sell lovely bags there.", "Let's go to that store where they sell lovely bags."),
          ("Grace is a designer. She makes bags out of old jeans.", "Grace is a designer who makes bags out of old jeans."),
          ("I posted a photo on Instagram. Did you see it?", "Did you see the photo (that) I posted on Instagram?"),
          ("Knitting and sewing are crafts. They became popular again.", "Knitting and sewing are crafts that became popular again."),
          ("Her dress is too small. She bought it yesterday.", "The dress (that) she bought yesterday is too small.")]
    prl = "".join(f"<li>{a}<div class='wline'>{R(c)}</div></li>" for a, c in pr)
    mt = [("made from cotton plants; light and cool", "cotton"), ("from sheep; warm, for sweaters", "wool"), ("blue cotton for jeans", "denim"),
          ("made from animal skin; for shoes and jackets", "leather"), ("made by an insect; soft and shiny", "silk"), ("from a plant; perfect for hot summers", "linen")]
    mtl = [f'<li value="{i+1}">{d} {A(w, "min-width:16mm")}</li>' for i, (d, w) in enumerate(mt)]
    b.page(f"""{sec(5, "Practice", "8 min")}
{sub("A", "Make one sentence with who, that or where. Which two sentences don't need the pronoun?", "5 min")}
<ol>{prl}</ol>
<p class="small">{R("No pronoun needed: 4 and 6 (that is the object)")}</p>
{sub("B", "Word builder: materials. Complete with the words.", "3 min")}
<div class="bank">cotton · denim · leather · linen · silk · wool</div>
{twocol(mtl, 3)}
<p class="small">Define one more material: <i>It's a material that…</i></p>""",
    22, """<ol><li>A: accept <i>which</i> for things. In 6, the relative clause goes in the middle of the sentence.</li>
<li>B: from the original lesson's extension. Ask what the student is wearing.</li></ol>""")

    # Page 7
    sw = ["a coat", "a department store", "a designer", "a pilot", "boots", "cotton", "New York", "plastic"]
    tw = ["a doctor", "a grocery store", "a T-shirt", "a teacher", "sneakers", "wool", "Chicago", "a thrift store"]
    b.page(f"""{sec(6, "Speaking: the definitions game", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">
<div style="flex:1">{sub("A", "Read the example.", "2 min")}
<div class="msg" style="max-width:none;font-size:9pt"><b>You:</b> It's something that you write with.<br><b>Teacher:</b> It's a pen.<br><b>You:</b> Almost! It's something that you can erase if you make a mistake.<br><b>Teacher:</b> It's a pencil.<br><b>You:</b> That's right! Your turn.</div></div>
<div style="width:38mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo('C')}" style="width:38mm;height:30mm;object-fit:cover;display:block"></div></div>
{sub("B", "Define these words. Your teacher guesses. Then guess your teacher's words.", "7 min")}
<div class="bank">{" · ".join(sw)} · your own ideas</div>
<p class="small" style="margin:1mm 0">Start like this: <i>It's a person who… · It's something that… · It's a place where…</i></p>
{sub("C", "Which of your definitions don't need who, that or which? Say them again without it.", "3 min")}
<p class="small"><i>It's something (that) you write with.</i></p>""",
    26, f"""<ol><li>B: your words (don't show them): {" · ".join(tw)}. Give clues with all three pronouns.</li>
<li>C: only when a subject comes after the pronoun (<i>something you wear</i>).</li></ol>""")

    # Page 8
    pc = [("A2 Unit 12", "I can write a friendly email with the right phrases."), ("A2 Unit 13", "I can explain causes and effects with zero and first conditionals."),
          ("A2 Unit 14", "I can join ideas with and, but, so, because and although."), ("A2 Unit 15", "I can put ideas in order and talk about changing my mind."),
          ("A2 Unit 16", "I can define people, things and places with who, that and where.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    ro = [("a / go / have / if / It's / place / where / you / you / an accident.", "It's a place where you go if you have an accident. (a hospital)"),
          ("a / animals / care / in / It's / of / someone / takes / who / a zoo.", "It's someone who takes care of animals in a zoo. (a zookeeper)"),
          ("a / city / in / Italy / It's / people / where / travel / in boats.", "It's a city in Italy where people travel in boats. (Venice)"),
          ("admire. / It's / people / someone / young", "It's someone young people admire. (a famous athlete or singer)"),
          ("can / find / It's / on / something / you / trees.", "It's something you can find on trees. (a leaf)")]
    rol = "".join(f"<li>{a}<div class='wline'>{R(c)}</div></li>" for a, c in ro)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Put the words in order. Then guess the answer.</b></p>
<ol>{rol}</ol>
<p style="margin-top:2mm"><b>2. My favorite clothes (50–75 words).</b> Describe a piece of clothing that you love. Where did you buy it? What is it made of? Use <i>who, that</i> and <i>where</i>: <i>It's a jacket that my grandmother gave me…</i></p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>1: number 4 has no pronoun because it's the object. Next class: the student reads the text; underline the relative clauses together.</p>""")

    b.extra("Audio script", f"""
{sub("16.1", "Fashion forward: Can fashion be green? (slow and natural)")}
<p style="line-height:1.42">{"<br>".join(PARAS)}</p>
{sub("16.2", "Word stress")}
<p>{" · ".join(S162)}</p>
{sub("16.3", "Relative clauses")}
<p>{" ".join(S163)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 16 - Fashion forward")
