# Speak! Bridge A2 - Unit 39 "Noun-tastic" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 39", audio_json="audio_a2-unit-39.json", img_dir="img")

PHOTOS = [("A", "milk chocolate", "milk chocolate"), ("B", "chocolate milk", "chocolate milk"), ("C", "shoe leather", "shoe leather"), ("D", "leather shoes", "leather shoes")]
_r = json.load(open("roteiro.json"))["units"]["a2-unit-39"]
S391 = [x.split(": ", 1)[1] for x in _r["39.1 Ana's favorite photo"].split("\n")]
S392 = [x.split(": ", 1)[1] for x in _r["39.2 Repeat: compound nouns"].split("\n")]
S393 = [x.split(". ", 1)[1] for x in [y.split(": ", 1)[1] for y in _r["39.3 Possessive 's: s, z or iz?"].split("\n")]]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 39", "Noun-tastic", "Describing things · <b>noun + noun, 's and of</b>",
                       [("YOU CAN", "describe a photo and everyday things using noun + noun, prepositional phrases, 's and of"),
                        ("LANGUAGE", "a coffee cup · a story about a dog · Marcos's laptop · the back of the picture"),
                        ("PRONUNCIATION", "stress in compound nouns · 's: /s/, /z/ or /ɪz/")])
    qq = [("a garden where people grow many types of flowers?", "a flower garden"), ("a flower that comes from this type of garden?", "a garden flower"),
          ("a special pencil that we use for drawing?", "a drawing pencil"), ("a picture that we make with this pencil?", "a pencil drawing")]
    ql = "".join(f"<li>What do we call {q} {A(a, 'min-width:28mm')}</li>" for q, a in qq)
    b.page(f"""{sec(1, "Warm-up: chocolate milk or milk chocolate?", "8 min")}
{sub("A", "Look at the photos. Which is chocolate milk and which is milk chocolate? Which is shoe leather and which is leather shoes?", "3 min")}
{photo_grid(T, PHOTOS)}
{sub("B", "Answer the questions.", "3 min")}
<ol style="line-height:1.55;margin:0">{ql}</ol>
{sub("C", "Which noun is the main thing: the first or the second? Do you know any other pairs like these?", "2 min")}""",
    22, """<ol><li>A: B is chocolate milk (a milk drink with chocolate flavor); A is milk chocolate (chocolate made with milk). C is shoe leather (material for shoes); D is leather shoes (shoes made of leather).</li>
<li>C: the second noun is the main thing. Other pairs: <i>a glass of water / a water glass</i>, <i>a house boat / a boat house</i>.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Chocolate milk or milk chocolate? Which noun is the main one?</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Ana describes a favorite family photo</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Noun + noun, prepositional phrases, 's and of</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Putting nouns together</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>4 min</td><td>Compound noun stress · 's: /s/, /z/, /ɪz/</td><td>5</td></tr>
<tr><td>5 Practice</td><td>9 min</td><td>Make noun phrases · kitchen words with -er</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Guessing game: describe the noun phrase</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Ana (Neural2-F) describes one of her favorite family photos, as she practiced describing photos with Tom in Unit 31. Her mother, Rosa, took it on her father Carlos's birthday in their kitchen in São Paulo: her husband, Marcos, and their son, Leo, are writing a story at the kitchen table, and Ana does most of the cooking. All family names come from the story (Ana's family: Marcos, Leo, Carlos, Rosa). The Linguahouse task "choose the photo" used photos of children, so the gist task is now questions.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Portuguese order is main noun + <i>de</i> + noun, so students say <i>the laptop of Marcos</i>, <i>the door of the kitchen</i> for everyday items, <i>shoes store</i>, and confuse <i>chocolate milk</i> and <i>milk chocolate</i>. They also stress the second noun.</div>
<div class="box"><h4>AUDIO</h4>Track 39.1 Ana's favorite photo (slow and natural) · Track 39.2 Repeat: compound nouns · Track 39.3 Possessive 's: s, z or iz?</div>""")

    # Page 2
    gq = [("Who took the photo?", "Ana's mother, Rosa"), ("What was the occasion?", "her father's birthday"), ("What are Marcos and Leo doing?", "writing a story on Marcos's laptop"),
          ("Who does most of the cooking?", "Ana"), ("What color was the back wall then? And now?", "green; white")]
    gql = "".join(f"<li>{q} {A(a, 'min-width:30mm')}</li>" for q, a in gq)
    op = [["the kitchen table", "the table in the kitchen"], ["the laptop of Marcos", "Marcos's laptop"], ["a dog story", "a story about a dog"], ["Leo's ideas", "the ideas of Leo"],
          ["a pencil holder", "a holder of pencils"], ["a coffee cup", "a cup for coffee"], ["the woman with the knife", "the knife woman"],
          ["my father's birthday cake", "the birthday cake of my father"], ["the back wall of the kitchen", "the kitchen's back wall"], ["the frame picture", "the picture frame"]]
    an = ["the kitchen table", "Marcos's laptop", "a story about a dog", "Leo's ideas", "a pencil holder", "a coffee cup", "the woman with the knife",
          "my father's birthday cake", "the back wall of the kitchen", "the picture frame"]
    opl = [f'<li value="{i+1}">{ch(o, a)}</li>' for i, (o, a) in enumerate(zip(op, an))]
    b.page(f"""{sec(2, "Listening: Ana's favorite photo", "10 min")}
<div style="display:flex;gap:2.5mm;align-items:center"><p style="flex:1;margin:0">In her online class, Ana describes one of her favorite family photos. It was taken in her kitchen in São Paulo.</p>{img('E', 26, 18)}{img('F', 26, 18)}{img('G', 18, 18)}</div>
{audiocard(["39.1 · SLOW", "39.1 · NATURAL"])}
{sub("A", "Listen and answer the questions.", "4 min", "39.1 · SLOW")}
<ol style="margin:0;line-height:1.5;font-size:9pt">{gql}</ol>
{sub("B", "Listen again and choose the phrases Ana uses.", "5 min", "39.1 · NATURAL")}
<div style="font-size:9pt">{twocol(opl, 6)}</div>
{sub("C", "Imagine the photo. Describe it in your own words: who is where?", "1 min")}""",
    22, """<ol><li>A: elicit <i>counter</i> = the surface in a kitchen where you prepare food. Ana's family members all come from earlier units.</li>
<li>B: let the student predict first; in many pairs both are grammatical, but only one sounds natural.</li></ol>""")

    # Page 3
    b.page(f"""{sec(3, "Language focus: putting nouns together", "10 min")}
{sub("A", "Noun + noun. Read and choose.", "3 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">1 Marcos and Leo are sitting at the <b>kitchen table</b>. · 2 There's a <b>pencil holder</b> on the table. · 3 Marcos always has a <b>coffee cup</b> with him. · 4 In the <b>picture frame</b> is another photo.</div>
<p style="margin:.5mm 0;line-height:1.7">We use noun + noun for {ch(["everyday things", "unusual things"], "everyday things")}. The main noun is the {ch(["first", "second"], "second")} one. The other noun works like {ch(["an adjective", "a verb"], "an adjective")}.</p>
{sub("B", "Noun + preposition + noun. Write the prepositions Ana uses.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">1 They're writing a story {A("about", "min-width:12mm")} a dog. · 2 They call me the woman {A("with", "min-width:10mm")} the knife. · 3 The cake {A("on", "min-width:8mm")} the counter is my father's birthday cake.</div>
<p style="margin:.5mm 0">We use a prepositional phrase when the combination is {ch(["an everyday thing", "more unusual"], "more unusual")}.</p>
{sub("C", "'s. Read and choose.", "3 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">1 They're working on <b>Marcos's</b> laptop. · 2 They write stories using <b>Leo's</b> ideas. · 3 My <b>parents'</b> bedroom is upstairs.</div>
<p style="margin:.5mm 0;line-height:1.7">'s shows that something belongs to {ch(["a person or animal", "a thing"], "a person or animal")}. The punctuation (') is called {ch(["a comma", "an apostrophe"], "an apostrophe")}. With plural owners, it goes {ch(["before", "after"], "after")} the final s.</p>
{sub("D", "Of. Read and answer.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">At that time, the <b>back wall of the kitchen</b> was green. · You can see me at the <b>back of the picture</b>.</div>
<p style="margin:.5mm 0">We use <i>of</i> when something belongs to {ch(["a person", "a thing or place"], "a thing or place")}.</p>
<div class="box sand"><h4>RULE</h4><b>noun + noun</b> for everyday things (main noun last) · <b>noun + preposition + noun</b> for less usual combinations · <b>'s / s'</b> for people, animals, countries and organizations · <b>of</b> for things and parts of things. More on the next page: <b>Grammar reference</b>.</div>""",
    25, """<ol><li>A: link back to the Warm-up: <i>milk chocolate</i> is chocolate. Compound nouns can also be one word (<i>bedroom</i>) or hyphenated (<i>ten-year-old</i>).</li>
<li>C: Marcos ends in -s, so both <i>Marcos's</i> and <i>Marcos'</i> are correct; we say /ˈmɑːrkoʊsɪz/.</li></ol>""")

    grammar_ref.noun_phrases(b)

    # Page 5
    szi = ["s", "z", "iz", "s", "z", "iz"]
    szl = "".join(f"<li>{A(x, 'min-width:10mm;text-align:center')}</li>" for x in szi)
    b.page(f"""{sub("E", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>the laptop of Marcos</td><td><b>Marcos's laptop</b></td><td>a person: 's.</td></tr>
<tr><td>the door of the kitchen / the kitchen's door</td><td><b>the kitchen door</b></td><td>everyday thing.</td></tr>
<tr><td>the house's roof</td><td><b>the roof of the house</b></td><td>a thing: of.</td></tr>
<tr><td>a shoes store</td><td><b>a shoe store</b></td><td>first noun singular.</td></tr>
<tr><td>my parent's house (two parents)</td><td><b>my parents' house</b></td><td>plural: s'.</td></tr>
<tr><td>a bike boy</td><td><b>a boy with a bike</b></td><td>unusual: preposition.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "4 min")}
{audiocard(["39.2", "39.3"])}
{sub("A", "Listen and repeat. Stress the first noun: a COFfee cup.", "2 min", "39.2")}
{twocol([f'<li value="{i+1}">{s}</li>' for i, s in enumerate(S392)], 4)}
{sub("B", "Listen to six names with 's. Does 's sound like /s/, /z/ or /ɪz/? Write s, z or iz.", "2 min", "39.3")}
<ol style="line-height:1.5;column-count:3;column-gap:5mm">{szl}</ol>
<p class="small" style="margin:.5mm 0">/s/ after /p, t, k, f/ · /ɪz/ after /s, z, ʃ, tʃ, dʒ/ · /z/ after other sounds</p>""",
    29, """<ol><li>A: compound nouns are stressed on the first noun: KITchen table, PENcil holder, BUS stop, PICture frame, BIRTHday cake.</li>
<li>B: script: 1 Kate's /s/ 2 Ana's /z/ 3 Marcos's /ɪz/ 4 Rita's /s/ 5 Tom's /z/ 6 the boss's /ɪz/. Same rule as plural -s and third person -s.</li></ol>""")

    # Page 6
    c1 = ["Brazil", "box", "chocolate", "discussion", "end", "Kate", "roof", "watercolor"]
    c2 = ["books", "cake", "coast", "dog", "house", "painting", "pets", "story"]
    cols = "".join(f"<tr><td>{a}</td><td>{b_}</td></tr>" for a, b_ in zip(c1, c2))
    ps = [("", "Brazil's coast", "has thousands of kilometers of beaches."), ("Please don't leave that big", "box of books", "on my desk."),
          ("Don't tell me what happens at the", "end of the story", ". I want to read it myself."), ("I'm making a", "chocolate cake", "for my brother's birthday."),
          ("", "Kate's dog", "chewed her favorite shoes again!"), ("Look up there! There's a big bird on the", "roof of the house", "."),
          ("Our class had a", "discussion about pets", ". Most of us prefer dogs."), ("What a beautiful", "watercolor painting", "! Did you paint it?")]
    psl = "".join(f"<li>{a}{' ' if a else ''}{A(x, 'min-width:30mm')}{'' if e[0] in '.!' else ' '}{e}</li>" for a, x, e in ps)
    er = [("grater", "cuts cheese or carrots into small pieces"), ("blender", "mixes fruit and milk into a smoothie"), ("freezer", "keeps food very cold, below zero"),
          ("can opener", "opens a can of beans"), ("peeler", "takes the skin off potatoes"), ("mixer", "mixes eggs, sugar and flour for a cake"),
          ("pot holder", "protects your hands from a hot pan"), ("juicer", "makes orange juice")]
    ers = sorted(er, key=lambda x: x[1])
    erl = "".join(f"<li>It {d}. {A(w, 'min-width:18mm')}</li>" for w, d in ers)
    b.page(f"""{sec(5, "Practice", "9 min")}
{sub("A", "Join one word from each column to complete the sentences. Use 's or of, or just the two nouns.", "5 min")}
<div style="display:flex;gap:4mm;align-items:flex-start"><table style="margin:0;font-size:8.8pt;width:38mm"><tr><th>column 1</th><th>column 2</th></tr>{cols}</table>
<ol style="flex:1;line-height:1.55;font-size:9pt;margin:0">{psl}</ol></div>
{sub("B", "Word builder: kitchen things. Many end in -er (verb + -er): a blender is a thing that blends. Write the names.", "4 min")}
<div class="bank">blender · can opener · freezer · grater · juicer · mixer · peeler · pot holder</div>
<ol style="line-height:1.5;font-size:9pt;column-count:2;column-gap:5mm">{erl}</ol>
<p class="small" style="margin:.5mm 0">Which of these do you have in your kitchen? Which do you use most?</p>""",
    25, """<ol><li>A: Brazil has more than 7,000 km of coastline, so "thousands of kilometers" is safe. Ask why each answer uses 's, of or noun + noun.</li>
<li>B: <i>can opener</i> and <i>pot holder</i> are noun + noun too. Example answer: <i>I use a mixer when I make a cake.</i></li></ol>""")

    # Page 7
    mine = ["chocolate milk", "a coffee cup", "vegetable soup", "the teacher's book", "the side of the car", "a shoe store", "a bus stop", "a song about a frog"]
    theirs = ["a flower garden", "a kitchen table", "strawberry ice cream", "a box of pens", "the children's school", "the corner of the room", "fruit salad", "a train station"]
    ml = "".join(f"<td style='padding:2mm;text-align:center;border:.8pt solid #c9dfe3'>{m}</td>" + ("</tr><tr>" if i % 4 == 3 else "") for i, m in enumerate(mine))
    tl = " · ".join(theirs)
    b.page(f"""{sec(6, "Speaking: guess the noun phrase", "12 min")}
<div style="display:flex;gap:3mm;align-items:center"><p style="flex:1;margin:0">Describe a phrase from your cards <b>without saying any of its words</b>. Your teacher guesses. Then your teacher describes phrases from secret cards, and you guess.</p>{img('E', 30, 20)}</div>
{sub("A", "Your teacher's example. What is it?", "1 min")}
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:9pt">When it's very hot in the summer, you wear this on your head, at the beach. {A("a sun hat", "min-width:20mm")}</div>
{sub("B", "Your cards. Describe them one by one.", "5 min")}
<table style="margin:0;font-size:9pt;width:100%"><tr>{ml}</tr></table>
<p class="small" style="margin:.5mm 0">Useful language: <i>It's a kind of… · You find it in… · You use it to… · It belongs to… · It's the part of…</i></p>
{sub("C", "Your teacher's secret cards. Listen and guess.", "5 min")}
<p class="small" style="margin:0">{R("Teacher's cards: " + tl) if T else "Write your guesses here:"}</p>
<div class="wline"></div><div class="wline"></div>
{sub("D", "Now make up your own noun phrase for your teacher to guess.", "1 min")}""",
    27, """<ol><li>This replaces Linguahouse's A/B pair game (and its drawing option) with a 1:1 version: the student describes, the teacher guesses, then the roles change.</li>
<li>Guide the student to the exact phrase (<i>Almost! Is it a box of pens or a pen box?</i>); accuracy with the form is the aim.</li></ol>""")

    # Page 8
    pc = [("A2 Unit 36", "I can write a clear, polite work email."), ("A2 Unit 37", "I can use -ing forms after verbs like enjoy and avoid, and as subjects."),
          ("A2 Unit 38", "I can use a/an, the and no article correctly."), ("A2 Unit 39", "I can put nouns together: a coffee cup, Leo's ideas, the end of the story.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("A bike boy ran into me in the park.", "A boy with a bike"), ("Can I fill my water bottle here, please?", "✓"), ("I never sit at the bus's front.", "the front of the bus"),
          ("Close the bathroom's curtains when you take a shower.", "the bathroom curtains"), ("The movie's beginning was slow.", "The beginning of the movie"),
          ("The house of Harry is around the corner.", "Harry's house"), ("The kitchen's door was open, and the dog ran away.", "The kitchen door"),
          ("You can find Mr. Hall in the teachers' office.", "✓")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:34mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Correct the mistakes. If a sentence is correct, write ✓.</b></p>
<ol style="line-height:1.55;font-size:9pt">{hwl}</ol>
<p style="margin-top:1.5mm"><b>2. My favorite photo (50–75 words).</b> Think of a favorite photo of your family or friends. Describe it: who took it, who is in it, where everyone is, and what is in the background.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class: the student reads the description aloud while you imagine the photo; ask questions with noun phrases: <i>What's on the kitchen table? Whose car is that?</i> Unit 40 is Review 4 (Units 31–39).</p>""")

    b.extra("Audio script", f"""
{sub("39.1", "Ana's favorite photo (slow and natural)")}
<p style="line-height:1.4">{"<br>".join(S391)}</p>
{sub("39.2", "Repeat: compound nouns")}
<p>{" · ".join(S392)}</p>
{sub("39.3", "Possessive 's: s, z or iz? (3-second pause)")}
<p>{" · ".join(S393)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 39 - Noun-tastic")
