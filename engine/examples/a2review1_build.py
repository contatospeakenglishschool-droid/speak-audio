# Speak! Bridge A2 - Review 1 (Units 01-09), all English - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
_se.SERIES = "Bridge"
setup(band="A2 · REVIEW 1", audio_json="audio_a2-review-1.json", img_dir="img")

PHOTOS = [("A", "spotted", "Unit 01"), ("B", "a password", "Unit 02"), ("C", "leaves", "Unit 03"), ("D", "check my phone", "Unit 04"),
          ("E", "teammates", "Unit 06"), ("F", "break my arm", "Unit 07"), ("G", "do a zip line", "Unit 08"), ("H", "move to a new house", "Unit 09")]

_r = json.load(open("roteiro.json"))["units"]["a2-review-1"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["R1.1 Sweet Kate"].split("\n")]
S12 = [x.split(": ", 1)[1] for x in _r["R1.2 Write the words"].split("\n")][1:]
S13 = [tuple(x.split(": ", 1)) for x in _r["R1.3 Dialogues"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LEVEL A2 · REVIEW 1", "Review 1", "Units 01–09 · like · verb patterns · prepositions · the present perfect",
                       [("YOU CAN", "check what you learned in Units 01–09 and plan what to practice"),
                        ("LANGUAGE", "What's he like? · avoid using · afraid of · It smells fresh. · I've just… · Have you ever…? · for / since"),
                        ("PRONUNCIATION", "letter names · weak for, of, to · contractions I've, she's")])
    b.page(f"""{sec(1, "Warm-up: photo memory", "5 min")}
{sub("A", "One photo from each unit. Write the word or phrase. Then say one sentence about it with the grammar of that unit.", "5 min")}
<div class="bank">break my arm · check my phone · do a zip line · leaves · move to a new house · a password · spotted · teammates</div>
{photo_grid(T, PHOTOS)}
<p class="small" style="margin-top:2mm"><b>Example:</b> do a zip line → <i>Have you ever done a zip line? — Yes, I have. I did one in Brazil in 2019.</i></p>""",
    20, """<p>Photos A–H come from Units 01–09 in order (Unit 05 has no photo). Push each unit's grammar: <i>like</i> (01), verb patterns (02), senses (03), prepositions (04), compliments (06), <i>just</i> (07), <i>ever</i> (08), <i>for / since</i> (09).</p>""", cover=cover)

    b.extra("Review overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Units</th><th>SB page</th></tr>
<tr><td>1 Warm-up: photo memory</td><td>5 min</td><td>01–09</td><td>1</td></tr>
<tr><td>2 Listening: Megan visits Sweet Kate</td><td>10 min</td><td>01–09</td><td>2</td></tr>
<tr><td>3 Grammar: like, verb patterns, prepositions</td><td>8 min</td><td>01, 02, 04</td><td>3</td></tr>
<tr><td>4 Grammar: senses and the present perfect</td><td>10 min</td><td>03, 07, 08, 09</td><td>4</td></tr>
<tr><td>5 Vocabulary</td><td>8 min</td><td>03, 05, 07, 09</td><td>5</td></tr>
<tr><td>6 Pronunciation and social English</td><td>9 min</td><td>05, 06</td><td>6</td></tr>
<tr><td>7 Reflect and homework</td><td>5 min</td><td>01–09</td><td>7</td></tr></table>
<div class="box"><h4>HOW THIS GUIDE WORKS</h4>Every page looks like the Student Book page with the same number. Your notes are in the <b>yellow box</b>; <span class="red">answers in red</span> are not in the Student Book. This is a review: don't teach everything again. Let the student work, then focus on the mistakes that come back. The grammar reference pages of Units 07–09 are useful here.</div>
<div class="box sand"><h4>THE STORY SO FAR</h4>March in Chicago. Megan (Unit 09) visits Sweet Kate with Tom. Kate has had the bakery for eight years and changed her passwords after the hack (Unit 02); Lucy has just taken off her cast after her bike accident (Unit 07) and still has her phone rules (Unit 04); Paulo calls from Central Park, where he's forest bathing with tourists (Unit 03), and tells them that Ana swam with manatees in Florida (Unit 08). Megan asks the Unit 01 question: <i>What's he like?</i> (about Pancake the cat).</div>
<div class="box"><h4>THE TOP 5 MISTAKES TO WATCH</h4>1. <i>How is he?</i> (personality) → <b>What's he like?</b> 2. <i>avoid to use / I want that you</i> → <b>avoid using / I want you to</b>. 3. <i>worried with / good in</i> → <b>worried about / good at</b>. 4. <i>I'm hearing / It smells well</i> → <b>I hear / It smells good</b>. 5. <i>I live here since 2015 / I have been there last year</i> → <b>I've lived here since 2015 / I went there last year</b>.</div>
<div class="box"><h4>AUDIO</h4>Track R1.1 At Sweet Kate (slow and natural) · Track R1.2 Spelling · Track R1.3 Two dialogues</div>""")

    # Page 2
    topics = [("Kate's bakery", True), ("a password", True), ("a bike accident", True), ("a radio show", False), ("forest bathing", True), ("swimming with manatees", True), ("Tom's cat", True)]
    tl = " &nbsp; ".join(f"☐ {t}{(' ' + R('✓')) if ok else ''}" for t, ok in topics)
    tf = [("Megan and Kate have met before.", "F: Tom introduces them."), ("Kate has had the bakery for eight years.", "T"),
          ("Lucy has just come from the doctor.", "T"), ("Lucy fell off her bike in March.", "F: in January."),
          ("Megan has done forest bathing.", "F: she hasn't, but she'd like to."), ("Pancake is lazy and always hungry.", "T")]
    tfl = [f'<li value="{i+1}">{s} <b>T / F</b> {R(a)}</li>' for i, (s, a) in enumerate(tf)]
    find = [("a question with like (Unit 01)", "What's he like?"), ("a verb + -ing (Unit 02)", "avoid using"), ("a sense verb + adjective (Unit 03)", "it smells amazing / it tastes delicious / my arm feels weak"),
            ("a compliment (Unit 06)", "What a beautiful bakery!"), ("the present perfect with just (Unit 07)", "I've just come from the doctor."),
            ("a question with ever (Unit 08)", "Have you ever done that?"), ("for or since (Unit 09)", "for eight years")]
    fl = "".join(f"<li>{x} {R(y)}</li>" for x, y in find)
    b.page(f"""{sec(2, "Listening: Megan visits Sweet Kate", "10 min")}
<p>It's March. Megan is in Chicago for a conference, and Tom takes her to his sister's bakery.</p>
{audiocard(["R1.1 · SLOW", "R1.1 · NATURAL"])}
{sub("A", "Listen. What do they talk about? Check (✓) six topics. One topic is extra.", "2 min", "R1.1 · SLOW")}
<p style="font-weight:600">{tl}</p>
{sub("B", "Listen again. True (T) or false (F)? Correct the false sentences.", "4 min", "R1.1 · NATURAL")}
{twocol(tfl, 4)}
{sub("C", "Find one example in the conversation of each form.", "4 min")}
<ol>{fl}</ol>""",
    22, """<p>A: the extra topic is <i>a radio show</i> (Unit 04). C: let the student read the script (TB last page) to find the forms, or play the natural version again and pause.</p>""")

    # Page 3
    lk = [("What's Pancake like?", "He's lazy, friendly and always hungry."), ("What does Megan look like?", "She's tall, with short dark hair."),
          ("What does Kate like doing?", "She likes baking cakes."), ("Would Megan like to try forest bathing?", "Yes, she would.")]
    lkl = "".join(f"<li>{q} <span class='small'>→</span> {R(a)}</li>" for q, a in lk)
    lka = " · ".join(a for _, a in [lk[1], lk[3], lk[0], lk[2]])
    vp = [(["to change", "changing"], "changing", "Kate avoids", "the same password twice… no, she avoids using it twice!"),
          (["to visit", "visiting"], "to visit", "Megan wants", "Paulo in New York."), (["to stop", "stop"], "to stop", "The doctor told Lucy", "riding her bike for a month."),
          (["to ride", "riding"], "riding", "Lucy can't stand", "the bus."), (["to wear", "wearing"], "to wear", "Megan always tells her patients", "a helmet."),
          (["to have", "having"], "having", "Tom doesn't mind", "a lazy cat.")]
    vpl = [f'<li value="{i+1}">{a} {ch(o, r)} {c}</li>' for i, (o, r, a, c) in enumerate(vp)]
    vpl[0] = '<li value="1">Kate avoids ' + ch(["to use", "using"], "using") + ' the same password twice.</li>'
    pr = [("Lucy was afraid", "of", "riding her bike again."), ("Megan is interested", "in", "forest bathing."), ("Kate is responsible", "for", "everything at the bakery."),
          ("Tom is worried", "about", "Pancake's weight."), ("There's a big increase", "in", "online scams."), ("Is there a solution", "to", "lazy cats?")]
    prl = [f'<li value="{i+1}">{a} {A(p, "min-width:12mm")} {c}</li>' for i, (a, p, c) in enumerate(pr)]
    b.page(f"""{sec(3, "Grammar: like, verb patterns, prepositions", "8 min")}
{sub("A", "Unit 01. Match the questions with the answers.", "2 min")}
<div class="bank" style="background:#fff">{lka}</div>
<ol>{lkl}</ol>
{sub("B", "Unit 02. Choose the correct form.", "3 min")}
{twocol(vpl, 4)}
{sub("C", "Unit 04. Complete with about, for, in, of or to.", "3 min")}
{twocol(prl, 4)}""",
    24, """<ol><li>A: <b>like</b> = personality; <b>look like</b> = appearance; <b>like doing</b> = preferences; <b>would like</b> = wishes.</li>
<li>B: <i>tell / want + person + to</i>; <i>avoid, can't stand, don't mind + -ing</i>. C: ask for one true sentence for each phrase.</li></ol>""")

    # Page 4
    ss = [(["smells", "is smelling"], "smells", "Mmm, this bread", "amazing!"), (["I'm tasting", "I taste"], "I'm tasting", "Shh!", "the new cake. Don't talk to me."),
          (["hear", "am hearing"], "hear", "I", "a strange noise in the kitchen."), (["looks", "is looking"], "looks", "Your cat", "very happy.")]
    ssl = [f'<li value="{i+1}">{a} {ch(o, r)} {c}</li>' for i, (o, r, a, c) in enumerate(ss)]
    pp = [("Lucy", "has just taken", "off her cast. (just / take)"), ("", "Have you ever swum", "with manatees? (you / ever / swim)"),
          ("Ana", "swam", "with manatees last month. (swim)"), ("Megan", "has never done", "forest bathing. (never / do)"),
          ("Kate", "has had", "the bakery for eight years. (have)"), ("Tom", "has known", "Megan since college. (know)"),
          ("Paulo", "moved", "to New York last year. (move)"), ("I", "haven't seen", "you for ages! (not see)")]
    ppl = [f'<li value="{i+1}">{a} {A(v, "min-width:26mm")} {c}</li>' for i, (a, v, c) in enumerate(pp)]
    fs = ["2015", "ages", "Monday", "three weeks", "I was a child", "a long time"]
    fsa = ["since", "for", "since", "for", "since", "for"]
    fst = "".join(f"<td style='text-align:center'>{x}<br>{R(y)}</td>" for x, y in zip(fs, fsa))
    b.page(f"""{sec(4, "Grammar: senses and the present perfect", "10 min")}
{sub("A", "Unit 03. Choose the correct form.", "2 min")}
{twocol(ssl, 3)}
{sub("B", "Units 07–09. Complete with the present perfect or the past simple.", "5 min")}
{twocol(ppl, 5)}
{sub("C", "Unit 09. for or since?", "2 min")}
<table style="table-layout:fixed;margin-top:0"><tr>{fst}</tr></table>
<div class="box sand"><h4>REMEMBER</h4>Present perfect = no finished time (<b>just, ever, never, for, since</b>). Past simple = a finished time (<b>last month, in 2019, ago</b>). See the grammar reference pages in Units 07–09.</div>""",
    24, """<ol><li>A: 2 is an action (continuous); 1, 3, 4 describe or are state verbs.</li>
<li>B: ask the student to underline the time words first. 3 and 7 have a finished time (past simple).</li></ol>""")

    # Page 5
    ps = [("receipt", "noun"), ("humid", "adjective"), ("carefully", "adverb"), ("spell", "verb"), ("them", "pronoun"), ("next to", "preposition")]
    pst = "".join(f"<td style='text-align:center'><b>{w}</b><br>{R(p)}</td>" for w, p in ps)
    wf = [("humid", "humidity"), ("decide", "decision"), ("happy", "happiness"), ("easy", "easily")]
    wfl = "".join(f"<li>{a} → {A(n, 'min-width:22mm')}</li>" for a, n in wf)
    sa = [("A lemon tastes", "sour"), ("Honey feels", "sticky"), ("Tree bark feels", "rough"), ("Toothpaste smells", "minty")]
    sal = "".join(f"<li>{a} {A(w, 'min-width:16mm')}.</li>" for a, w in sa)
    tr = [("a small cut", "a Band-Aid"), ("a broken leg", "a cast"), ("a sprained ankle", "an ice pack / a bandage"), ("a small burn", "cream")]
    trl = "".join(f"<li>{a} → {A(w, 'min-width:26mm')}</li>" for a, w in tr)
    le = [("graduate", "from college"), ("get", "married"), ("move", "to a new house"), ("start", "a new job")]
    lel = " · ".join(f"<b>{v}</b> {A(n, 'min-width:20mm')}" for v, n in le)
    b.page(f"""{sec(5, "Vocabulary", "8 min")}
{sub("A", "Unit 05. What kind of word is it? Write noun, verb, adjective, adverb, pronoun or preposition.", "2 min")}
<table style="table-layout:fixed;margin-top:0"><tr>{pst}</tr></table>
<div class="two"><div>{sub("B", "Unit 05. Word families: write the noun or adverb.", "2 min")}
<ol>{wfl}</ol></div>
<div>{sub("C", "Unit 03. Complete with a sense adjective.", "1 min")}
<div class="bank">minty · rough · sour · sticky</div><ol>{sal}</ol></div></div>
<div class="two"><div>{sub("D", "Unit 07. Which treatment?", "2 min")}
<div class="bank">a Band-Aid · a cast · cream · an ice pack</div><ol>{trl}</ol></div>
<div>{sub("E", "Unit 09. Complete the life events.", "1 min")}
<div class="bank">from college · married · a new job · to a new house</div><p style="line-height:2">{lel}</p></div></div>""",
    22, """<p>After each block, ask for a personal sentence: <i>When did you graduate from college? What tastes sour? Have you ever needed a cast?</i></p>""")

    # Page 6
    d1 = [("Lucy", "That dress really suits <u>to</u> you! Where <u>you got</u> it?"), ("Kate", "Thanks! Actually, my mom gave it to me."),
          ("Lucy", "What a beautiful <u>!</u> And congratulations <u>for</u> eight years of Sweet Kate!"), ("Kate", "You're too <u>much</u> kind. It was a team effort.")]
    d2 = [("Megan", "Sorry, how do you <u>call</u> this word? K-N-I-F-E."), ("Tom", "Knife. The K is silent."),
          ("Megan", "And what <u>means</u> crumb?"), ("Tom", "It's a very small piece of bread or cake."), ("Megan", "What kind of word <u>it is</u>?"), ("Tom", "It's a noun. One crumb, two crumbs.")]
    def dlg(lines):
        return "<br>".join(f"<b>{n}:</b> {t}" for n, t in lines)
    b.page(f"""{sec(6, "Pronunciation and social English", "9 min")}
{audiocard(["R1.2", "R1.3"])}
{sub("A", "Unit 05. Listen and write the words you hear spelled.", "3 min", "R1.2")}
<table style="table-layout:fixed;margin-top:0"><tr>{"".join(f"<td style='height:9mm;vertical-align:bottom'>{i+1}. {R(s.split('. ', 1)[1].replace('-', '').rstrip('.').lower())}</td>" for i, s in enumerate(S12))}</tr></table>
{sub("B", "Units 05–06. Each dialogue has mistakes (underlined). Correct them. Then listen and check.", "4 min", "R1.3")}
<div class="two"><div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.8pt;line-height:1.5"><b>Dialogue 1</b><br>{dlg(d1)}</div>
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.8pt;line-height:1.5"><b>Dialogue 2</b><br>{dlg(d2)}</div></div>
<p class="small">{R("1: suits you · Where did you get it? · What a beautiful color! · congratulations on · You're too kind. — 2: how do you say · what does crumb mean? · What kind of word is it?")}</p>
{sub("C", "Role-play the dialogues with your teacher. Then compliment your teacher on something real and ask about a word in your book.", "2 min")}""",
    24, """<ol><li>A: 3-second pause after each word. Check the letters Brazilians confuse: E/I, A/E, G/J.</li>
<li>B: in the Student Book the mistakes are underlined to help; in 1, <i>What a beautiful!</i> needs a noun.</li></ol>""")

    # Page 7
    cd = [("01", "I can ask and talk about appearance, personality, likes and wishes."), ("02", "I can use verb + to, verb + -ing and verb + person + to."),
          ("03", "I can describe a place with my senses and use state verbs correctly."), ("04", "I can use adjectives and nouns with the right preposition."),
          ("05", "I can ask about words in class and name parts of speech."), ("06", "I can praise, compliment and congratulate people, and respond politely."),
          ("07", "I can talk about accidents that just happened with the present perfect."), ("08", "I can ask about life experiences and give details with the past simple."),
          ("09", "I can say how long things have been true with for and since.")]
    cdr = "".join(f"<tr><td><b>Unit {u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in cd)
    b.page(f"""{sec(7, "Reflect and homework", "5 min")}
{sub("A", "How are you doing? Check one box for each line.", "2 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{cdr}</table>
{sub("B", "My goals. What do you want to practice more? Write two things.", "2 min")}
<div class="wline"></div><div class="wline"></div>
{sub("C", "Homework", "1 min")}
<p><b>A message to Megan (70–90 words).</b> Megan wants to know about you. Write her a message. Include:</p>
<ol><li>what you're like and what you like doing;</li><li>how long you've lived in your city and had your job or studies (for / since);</li>
<li>one thing you've never done and one amazing experience (with details in the past simple);</li><li>something you want to do this year (verb + to).</li></ol>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Look at the "Not yet" lines and plan two short review activities for the next classes. The homework uses grammar from all nine units: correct it carefully and keep it as a writing sample. Next: Unit 11, Party time.</p>""")

    b.extra("Audio scripts", f"""
{sub("R1.1", "At Sweet Kate (slow and natural)")}
<p style="line-height:1.42">{"<br>".join(f"<b>{n}:</b> {t}" if n != "Narrator" else f"<i>{t}</i>" for n, t in SCRIPT)}</p>
{sub("R1.2", "Spelling (3-second pause after each word)")}
<p>{" · ".join(S12)}</p>
{sub("R1.3", "Two dialogues (correct versions)")}
<p style="line-height:1.42">{"<br>".join(f"<b>{n}:</b> {t}" if n != "Narrator" else f"<i>{t}</i>" for n, t in S13)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 10 - Review 1")
