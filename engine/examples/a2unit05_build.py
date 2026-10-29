# Speak! Bridge A2 - Unit 05 "Language for learning" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 05", audio_json="audio_a2-unit-05.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["a2-unit-05"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["05.1 Online class"].split("\n")]
S052 = [x.split(": ", 1)[1] for x in _r["05.2 Repeat letters"].split("\n")]
S053 = [x.split(": ", 1)[1] for x in _r["05.3 Repeat questions"].split("\n")]

EMAIL = ("Hi Ana! Life in Orlando is great, but the weather is very humid. I work at a dental office now, and my English is getting better every day. "
         "Last weekend I got a terrible sunburn at Cocoa Beach, about an hour from Orlando. I didn't use sunscreen… big mistake! "
         "Here's something funny about shopping in the US: the price on the shelf doesn't include sales tax, so the total on your receipt is always higher. "
         "Come and visit with Marcos and Leo!<br>Love, Carol")


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1: one big photo + letters (abstract topic)
    cover = cover_html(T, "LEVEL A2 · UNIT 05", "Language for learning", "Questions for class · <b>parts of speech and word families</b>",
                       [("YOU CAN", "ask about words in class and spell clearly"),
                        ("LANGUAGE", "What does it mean? · How do you spell it? · What kind of word is it?"),
                        ("PRONUNCIATION", "letter names: A /eɪ/ · E /iː/ · I /aɪ/ · G /dʒiː/ · J /dʒeɪ/")])
    pairs = [("E", "I", "E"), ("G", "J", "J"), ("A", "E", "A"), ("I", "Y", "Y"), ("K", "Q", "Q"), ("R", "H", "H"), ("V", "W", "W"), ("B", "P", "P")]
    pl = "".join(f"<td style='text-align:center;font-weight:700'>{ch([a, c], r)}</td>" for a, c, r in pairs)
    b.page(f"""{sec(1, "Warm-up: letters and spelling", "8 min")}
<div style="display:flex;gap:4mm;align-items:flex-start">
<div style="width:58mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo('A')}" style="width:58mm;height:40mm;object-fit:cover;display:block"></div>
<div style="flex:1">{sub("A", "Listen to your teacher. Circle the letter you hear.", "3 min")}
<table style="table-layout:fixed;margin-top:1mm"><tr>{pl}</tr></table>
<p class="small">Which letters are difficult for you?</p></div></div>
{sub("B", "Which letters have the same vowel sound as these words?", "2 min")}
<table style="table-layout:fixed;margin-top:0"><tr><th>tree /iː/</th><th>train /eɪ/</th><th>rice /aɪ/</th><th>you /uː/</th></tr>
<tr><td>{A("B C D E G P T V Z", "min-width:30mm")}</td><td>{A("A H J K", "min-width:20mm")}</td><td>{A("I Y", "min-width:12mm")}</td><td>{A("Q U W", "min-width:14mm")}</td></tr></table>
{sub("C", "Spell for your teacher: your full name, your street and the name of your company or school.", "3 min")}""",
    22, """<ol><li>A: read the letter in red twice. Brazilians confuse <b>E/I</b>, <b>G/J</b>, <b>A/E</b>, and say <b>H</b> and <b>R</b> the Portuguese way. <b>Y</b> = "why", <b>W</b> = "double u", <b>Z</b> = "zee" in American English.</li>
<li>C: write what you hear and show it. If you write it wrong, the student corrects you.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Letter names and spelling</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>An online class: Ana reads an email from her cousin Carol</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Parts of speech · what to learn about each one</td><td>3</td></tr>
<tr><td>4 Pronunciation lab</td><td>5 min</td><td>Letters by vowel sound · classroom questions</td><td>4</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Complete the questions · Word builder: word families</td><td>5</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Word challenge · the NATO alphabet · learning vocabulary</td><td>6</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework (50–75 words)</td><td>7</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Ana has an online class with Tom. They read an email from <b>Carol, Ana's cousin, who lives in Orlando, Florida</b> (her first appearance; voice Chirp 3 HD Leda when she speaks). Carol works at a dental office, got a sunburn at Cocoa Beach and is surprised by sales tax, which is not included in the shelf price in the US. Ana asks Tom about the new words. The email is original; Cocoa Beach is on Florida's Atlantic coast, about an hour's drive east of Orlando.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Classroom questions copied from Portuguese: <i>How do you call this?</i> ✗ → <b>What do you call this?</b>; <i>What means humid?</i> ✗ → <b>What does humid mean?</b>; <i>How you spell?</i> ✗ → <b>How do you spell it?</b>; <i>I have a doubt</i> ✗ → <b>I have a question</b>. Letter names E/I, G/J and A/E are also confusing.</div>
<div class="box"><h4>AUDIO</h4>Track 05.1 The online class (slow and natural) · Track 05.2 Letters · Track 05.3 Classroom questions</div>""")

    # Page 2: listening + Carol's email
    asked = [("humid", True), ("weather", False), ("sunburn", True), ("beach", False), ("sunscreen", True), ("shelf", False), ("receipt", True)]
    al = " &nbsp; ".join(f"☐ {w}{(' ' + R('✓')) if ok else ''}" for w, ok in asked)
    qs = [("How do you", "say", "the next word?"), ("What does humid", "mean", "?"), ("", "Can", "we say Orlando has a lot of humid?"),
          ("What", "kind", "of word is sunburn?"), ("How do you", "spell", "it?"), ("What do you", "call", "this white cream?"), ("How do you", "pronounce", "this word?")]
    ql = [f'<li value="{i+1}">{a} {A(w, "min-width:17mm")} {c}</li>' for i, (a, w, c) in enumerate(qs)]
    b.page(f"""{sec(2, "Listening: an online class", "10 min")}
<p>Ana has an online English class with Tom. Today she brings an email from her cousin Carol, who lives in Orlando, Florida.</p>
<div style="display:flex;gap:3mm;border:1pt solid #c9dfe3;border-radius:2mm;padding:2mm 3mm;margin-bottom:1.5mm">
<div style="flex:1;font-size:9pt;line-height:1.42"><div style="font-size:7pt;font-weight:800;letter-spacing:.14em;color:#7d858a">FROM: CAROL · SUBJECT: Hello from Florida!</div>{EMAIL}</div>
<img src="{photo('B')}" style="width:34mm;height:34mm;object-fit:cover;border-radius:1.5mm"></div>
{audiocard(["05.1 · SLOW", "05.1 · NATURAL"])}
{sub("A", "Listen. Which words does Ana ask about? Check (✓) four words.", "2 min", "05.1 · SLOW")}
<p style="font-weight:600">{al}</p>
{sub("B", "Listen again. Complete Ana's questions.", "5 min", "05.1 · NATURAL")}
{twocol(ql, 5)}
{sub("C", "Is there another word in the email you don't know? Ask your teacher with a question from B.", "2 min")}""",
    22, """<p>A: let the student read the email first, without a dictionary. B: guess, listen, check. Drill each question with the right intonation: <i>wh-</i> questions go down, <i>Can we say…?</i> goes up. If there's time, read the script (TB last page): you are Tom, the student is Ana.</p>""")

    # Page 3
    pos = [("verb", "an action or a state", "mean, read, spell, remember"), ("noun", "a person, a thing or an idea", "beach, cousin, receipt, humidity"),
           ("adjective", "describes a noun", "humid, terrible, silent"), ("adverb", "describes a verb or an adjective", "slowly, really, always"),
           ("pronoun", "replaces a noun", "she, it, we, them"), ("preposition", "connects a word to a noun", "at, on, from, next to")]
    pt = "".join(f"<tr><td>{A(p, 'min-width:22mm')}</td><td>{m}</td><td>{e}</td></tr>" for p, m, e in pos)
    odd = [("at · go · in · on", "go: verb; the others are prepositions"), ("slowly · really · nice · always", "nice: adjective; the others are adverbs"),
           ("swim · eat · food · sleep", "food: noun; the others are verbs"), ("he · him · boy · she", "boy: noun; the others are pronouns"),
           ("humid · humidity · sunny · terrible", "humidity: noun; the others are adjectives")]
    ol = [f'<li value="{i+1}">{w} {R(a)}</li>' for i, (w, a) in enumerate(odd)]
    learn = [("verbs", "regular or irregular?"), ("nouns", "countable or uncountable?"), ("pronouns", "subject or object?"), ("prepositions", "time or place?"), ("adverbs", "how or how often?")]
    lt = "".join(f"<tr><td style='width:30mm'>{i+1}. {learn[i][0]}</td><td>{chr(97+i)}. {learn[[2, 0, 4, 1, 3][i]][1]}</td></tr>" for i in range(5))
    b.page(f"""{sec(3, "Language focus: parts of speech", "10 min")}
{sub("A", "Tom says: “Humid is an adjective.” Complete the table with these parts of speech.", "3 min")}
<div class="bank">adjective · adverb · noun · preposition · pronoun · verb</div>
<table style="table-layout:fixed;margin-top:0;font-size:9pt"><tr><th style="width:30mm">part of speech</th><th>meaning</th><th>examples</th></tr>{pt}</table>
{sub("B", "Quick check. Cross out the word that is different. Say why.", "3 min")}
{twocol(ol, 4)}
{sub("C", "What do you need to learn about each part of speech? Match.", "4 min")}
<table style="table-layout:fixed;margin-top:0;font-size:9pt;width:80%">{lt}</table>
<p class="small">{R(" · ".join(f"{i+1} {chr(97 + [2, 0, 4, 1, 3].index(i))}" for i in range(5)))}</p>
<div class="box sand"><h4>TIP</h4>A good dictionary tells you the part of speech: <b>humid</b> <i>adj.</i>, <b>humidity</b> <i>n.</i> When you write a new word in your notebook, write the part of speech too.</div>""",
    24, """<ol><li>B: many words can be two parts of speech: <i>love, drink, call</i> (noun and verb). Ask the student for an example sentence of each.</li>
<li>C: ask for an example of each: <i>go – went</i>, <i>advice</i>, <i>them</i>…</li></ol>""")

    # Page 4
    groups = ["/eɪ/", "/iː/", "/ɛ/", "/aɪ/", "/oʊ/", "/uː/", "/ɑr/"]
    b.page(f"""{sub("D", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>How do you call this?</td><td><b>What do you call this?</b></td><td>what + call.</td></tr>
<tr><td>What means humid?</td><td><b>What does humid mean?</b></td><td>question with does.</td></tr>
<tr><td>How you spell it?</td><td><b>How do you spell it?</b></td><td>don't forget do.</td></tr>
<tr><td>How is the pronounce of this word?</td><td><b>How do you pronounce this word?</b></td><td>pronounce is a verb.</td></tr>
<tr><td>I have a doubt.</td><td><b>I have a question.</b></td><td>doubt = not sure.</td></tr>
<tr><td>Is it a noun or adjective?</td><td><b>Is it a noun or an adjective?</b></td><td>an before a vowel.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "5 min")}
{audiocard(["05.2", "05.3"])}
{sub("A", "Letters with the same vowel sound. Listen and repeat.", "2 min", "05.2")}
<table style="table-layout:fixed;margin-top:0;font-size:9pt"><tr>{"".join(f"<th style='text-align:center'>{g}</th>" for g in groups)}</tr>
<tr>{"".join(f"<td style='text-align:center'><b>{l.rstrip('.')}</b></td>" for l in S052)}</tr></table>
{sub("B", "Classroom questions. Listen and repeat.", "2 min", "05.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S053)}</div>
<div class="box" style="margin-top:1mm"><h4>STRESS AND INTONATION</h4>Stress the important word: <i>What does it <b>MEAN</b>? How do you <b>SPELL</b> it?</i> Wh- questions go down ↘; yes/no questions go up ↗: <i>Can we say this?</i> ↗</div>""",
    24, """<ol><li>4A: the hardest for Brazilians: <b>E</b> /iː/ vs <b>I</b> /aɪ/, <b>G</b> /dʒiː/ vs <b>J</b> /dʒeɪ/, <b>R</b> /ɑr/ and <b>H</b> /eɪtʃ/.</li>
<li>4B: <i>doubt</i> exists, but it means "not being sure", not "a question".</li></ol>""")

    # Page 5
    dl = [("say", "Lucy: Sorry, how do you", "this street name?"), ("spell", "Tom: Wacker Drive. Do you want me to", "it? W-A-C-K-E-R."),
          ("mean", "Lucy: Thanks. And what does <i>tip</i>", "?"), ("noun", "Tom: It's money for a waiter. Here it's a", "."),
          ("say", "Lucy: Can we", "“I tip the waiter”?"), ("verb", "Tom: Yes! Tip can also be a", "."),
          ("call", "Lucy: Great. And what do you", "the paper with the price?"), ("pronounce", "Tom: A check. And the other one is a receipt. Can you", "it?")]
    dll = "".join(f"<li>{a} {A(w, 'min-width:18mm')} {c}</li>" for w, a, c in dl)
    fam = [("humid", "humidity", "adjective → noun"), ("electric", "electricity", "adjective → noun"), ("happy", "happiness", "adjective → noun"),
           ("careful", "carefully", "adjective → adverb"), ("easy", "easily", "adjective → adverb"), ("decide", "decision", "verb → noun"),
           ("inform", "information", "verb → noun"), ("pronounce", "pronunciation", "verb → noun")]
    ft = "".join(f"<tr><td>{a}</td><td>{A(n, 'min-width:26mm')}</td><td class='small'>{k}</td></tr>" for a, n, k in fam)
    cf = [(["humid", "humidity"], "humidity", "There's a lot of", "in Orlando in the summer."), (["careful", "carefully"], "carefully", "Please read the questions", "."),
          (["happy", "happiness"], "happy", "Carol is very", "in Florida."), (["pronounce", "pronunciation"], "pronunciation", "Your", "is getting better!")]
    cfl = "".join(f"<li>{a} {ch(o, r)} {c}</li>" for o, r, a, c in cf)
    b.page(f"""{sec(5, "Practice", "8 min")}
{sub("A", "Lucy asks Tom about words. Complete the conversation.", "3 min")}
<div class="bank">call · mean · noun · pronounce · say (×2) · spell · verb</div>
<ol>{dll}</ol>
{sub("B", "Word builder: word families. Complete the table.", "3 min")}
<div class="bank">carefully · decision · easily · electricity · happiness · humidity · information · pronunciation</div>
<table style="table-layout:fixed;margin-top:0;font-size:9pt;width:85%">{ft}</table>
{sub("C", "Choose the correct word.", "2 min")}
<ol>{cfl}</ol>""",
    22, """<ol><li>A: <b>tip</b> is a noun and a verb; in the US people usually tip 15–20% in restaurants. A <b>check</b> = the bill in a restaurant.</li>
<li>B: point out the spelling: pro<b>nounce</b> → pro<b>nun</b>ciation (no <i>o</i>!). Common endings: -ity, -ness, -ly, -tion, -sion.</li></ol>""")

    # Page 6
    words = [("receipt", "noun"), ("island", "noun"), ("Wednesday", "noun"), ("comfortable", "adjective"), ("knife", "noun"), ("quickly", "adverb")]
    wt = "".join(f"<td style='text-align:center;height:10mm'><b>{w}</b><br>{R(p)}</td>" for w, p in words)
    defs = ["a hot, wet day → <i>humid</i>", "a person who lives near you → <i>neighbor</i>", "the opposite of <i>always</i> → <i>never</i>", "you use it to cut food → <i>knife</i>"]
    NATO = ["Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike",
            "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "X-ray", "Yankee", "Zulu"]
    cell = lambda w: f"<td style='text-align:center;padding:.8mm .5mm'><b style='color:#0f4a5a'>{w[0]}</b><br><span class='small'>{w}</span></td>"
    nato = "".join("<tr>" + "".join(cell(w) for w in NATO[r * 9:(r + 1) * 9]) + ("<td></td>" if r == 2 else "") + "</tr>" for r in range(3))
    b.page(f"""{sec(6, "Speaking", "12 min")}
{sub("A", "Word challenge. Your teacher asks about these words: How do you spell it? What kind of word is it? What does it mean?", "4 min")}
<table style="table-layout:fixed;margin-top:0"><tr>{wt}</tr></table>
{sub("B", "Change roles. Your teacher explains a word but doesn't say it. Ask questions and guess the word.", "4 min")}
<div class="msg" style="max-width:none;padding:1.5mm 4mm"><b>Teacher:</b> It's something you use to cut food. <b>You:</b> What kind of word is it? <b>Teacher:</b> A noun. <b>You:</b> Is it a knife? How do you spell it? <b>Teacher:</b> K-N-I-F-E. The K is silent!</div>
<div class="box" style="margin-top:1.5mm"><h4>THE NATO ALPHABET</h4>Pilots, doctors and call centers use words to say letters clearly. Use them for difficult letters: <b>E</b> as in Echo, <b>I</b> as in India.<table style="table-layout:fixed;margin:1mm 0 0;font-size:8pt">{nato}</table></div>
{sub("C", "You and new words.", "4 min")}
<ol><li>How do you learn new words? Do you write them in a notebook or use an app?</li><li>Which English word is the most difficult for you to spell? And to pronounce?</li>
<li>Spell your email address using the NATO alphabet for the difficult letters.</li></ol>""",
    26, """<ol><li>A: silent letters: rece<b>i</b>pt (p), <b>i</b>sland (s), We<b>d</b>nesday (d), <b>k</b>nife (k); <i>comfortable</i> = COMF-ter-ble (three syllables).</li>
<li>B: ideas for you: """ + " · ".join(defs) + """.</li></ol>""")

    # Page 7
    pc = [("A2 Unit 01", "I can ask about appearance, personality, likes and wishes."), ("A2 Unit 02", "I can use verb + to, verb + -ing and verb + person + to."),
          ("A2 Unit 03", "I can describe a place with my senses and use state verbs correctly."), ("A2 Unit 04", "I can use adjectives and nouns with the right preposition."),
          ("A2 Unit 05", "I can ask about words in class and name parts of speech.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    order = [("d", "Student: Sorry, how do you say this word? I-S-L-A-N-D."), ("a", "Teacher: Island. The S is silent."),
             ("e", "Student: What does it mean?"), ("b", "Teacher: It's land with water all around it, like Florianópolis."),
             ("f", "Student: Oh! What kind of word is it?"), ("c", "Teacher: It's a countable noun: one island, two islands.")]
    shuffled = [order[i] for i in (1, 3, 5, 0, 2, 4)]
    ordl = "".join(f"<li style='list-style:none'>☐ {R(str([o[1] for o in order].index(t) + 1))} {t}</li>" for _, t in shuffled)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Put the conversation in order (1–6).</b></p>
<ul style="padding-left:2mm">{ordl}</ul>
<p style="margin-top:2mm"><b>2. Reply to Carol (50–75 words).</b> Thank her for the email, react to her sunburn, tell her about the weather in your city and ask her two questions. Then underline one noun, one verb, one adjective and one adverb in your email.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class: the student reads the email; you ask <i>What kind of word is…?</i> about the underlined words. Keep using the classroom questions in every class from now on.</p>""")

    b.extra("Audio scripts", f"""
{sub("05.1", "The online class (slow and natural)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("05.2", "Letters")}
<p>{" · ".join(S052)}</p>
{sub("05.3", "Classroom questions")}
<p>{" ".join(S053)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 05 - Language for learning")
