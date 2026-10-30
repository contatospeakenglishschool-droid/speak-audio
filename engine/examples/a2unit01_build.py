# Speak! Bridge A2 - Unit 01 "It's like this" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 01", audio_json="audio_a2-unit-01.json", img_dir="img")

PHOTOS = [("A", "bright", "bright red flowers"), ("B", "dark", "dark purple fruit"), ("C", "deep", "deep blue sea"), ("D", "light", "light green leaves"),
          ("E", "pale", "pale pink shell"), ("F", "shiny", "shiny black eyes"), ("G", "spotted", "spotted fur"), ("H", "striped", "striped fur")]
CAPS = {"A": "___ red flowers", "B": "___ purple fruit", "C": "___ blue sea", "D": "___ green leaves", "E": "___ pink shell", "F": "___ black eyes", "G": "___ fur", "H": "___ fur"}

_r = json.load(open("roteiro.json"))["units"]["a2-unit-01"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["01.1 Shelter"].split("\n")]
S012 = [x.split(": ", 1)[1] for x in _r["01.2 Repeat words"].split("\n")]
S013 = [x.split(": ", 1)[1] for x in _r["01.3 Repeat questions"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 01", "It's like this", "Describing people and animals · <b>four questions with like</b>",
                       [("YOU CAN", "ask and talk about appearance, personality, likes and wishes"),
                        ("LANGUAGE", "What does he look like? · What's he like? · What does he like doing? · Would he like…?"),
                        ("PRONUNCIATION", "striped /straɪpt/ (1 syllable) · spotted /ˈspɑtɪd/ · What's she like?")])
    grid = photo_grid(T, PHOTOS).replace('<div class="pad"></div>', '<div class="pad"></div>')
    caps = " &nbsp;·&nbsp; ".join(f"<b>{l}</b> {CAPS[l]}" for l, _, _ in PHOTOS)
    b.page(f"""{sec(1, "Warm-up: shades and patterns", "8 min")}
{sub("A", "Look at the photos. Which word describes each one? Write it under the photo.", "3 min")}
<div class="bank">bright · dark · deep · light · pale · shiny · spotted · striped</div>
{grid}
<p class="small" style="margin-top:1.5mm">{caps}</p>
{sub("B", "Answer the questions.", "5 min")}
<ol><li>Which two words are patterns? {R("spotted, striped")}</li><li>Which words mean a strong color? Which mean a weak color? {R("strong: bright, deep, dark · weak: light, pale")}</li>
<li>Which two words have two syllables? {R("shiny, spotted (striped has only one!)")}</li></ol>""",
    22, """<ol><li>A: these are common collocations: <i>bright red, deep blue, pale pink, shiny black</i>. Ask for more examples around the room or in the student's clothes.</li>
<li>B: <b>striped</b> /straɪpt/ has one syllable; <b>spotted</b> /ˈspɑtɪd/ has two (-ed after t = /ɪd/).</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Shades and patterns: bright, pale, spotted, striped…</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Paulo's first job in New York: photos at an animal shelter</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Four questions with like · like doing / like to do</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Four questions with like: form, meaning, short answers</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>5 min</td><td>Shade and pattern words · the four questions</td><td>5</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Shelter profiles · Word builder: appearance or personality?</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Information gap: animal or volunteer? · people you know</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework (50–75 words)</td><td>8</td></tr></table>
<div class="box"><h4>WELCOME TO SPEAK! BRIDGE (A2)</h4>Same 7-page structure as Speak! Essentials, with more vocabulary, longer conversations, a Word builder and longer written homework. Every page looks like the Student Book page with the same number. Your notes are in the <b>yellow box</b>; <span class="red">answers in red</span> are not in the Student Book.</div>
<div class="box sand"><h4>THE STORY CONTINUES</h4>A new chapter: <b>Paulo now lives in New York</b>, where he works as a photographer and tour guide. His first job is taking photos for Brooklyn Paws, an animal shelter (an invented place) that finds homes for dogs and cats. Jess, who works there, introduces the animals: playful Max, calm Rocky, sociable Ginger and lazy Luna… who would like a nap. Later in the course we'll also meet Carol, Ana's cousin in Florida.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>In Portuguese, one question covers both appearance and personality, so students say <i>How is he?</i> ✗ (that asks about health). Teach <b>What's he like?</b> (personality) and <b>What does he look like?</b> (appearance). Also: <i>He likes play</i> ✗ → <b>likes playing / likes to play</b>; <i>Would you like?</i> — <i>Yes, I like</i> ✗ → <b>Yes, I would</b>; <i>brown hairs</i> ✗ → <b>brown hair</b>.</div>
<div class="box"><h4>AUDIO</h4>Track 01.1 At the shelter (slow and natural) · Track 01.2 Shades and patterns · Track 01.3 The four questions</div>""")

    # Page 2
    an = [("Max", "light brown", "playful", "chasing balls", "go out for a walk"), ("Rocky", "dark brown, white spot", "calm", "watching people", "go out for a walk"),
          ("Luna", "pale gray, dark stripes", "lazy", "doesn't like other cats", "take a nap"), ("Ginger", "bright orange", "sociable", "people", "a snack / my sandwich")]
    an[0] = ("Max", "light brown", "playful", "chasing balls", "—")
    rows = "".join(f"<tr><td><b>{n}</b></td><td class='small'>{R(a)}</td><td class='small'>{R(c)}</td><td class='small'>{R(l)}</td><td class='small'>{R(w)}</td></tr>" for n, a, c, l, w in an)
    b.page(f"""{sec(2, "Listening: at the animal shelter", "10 min")}
<p>Paulo, Ana's brother, now lives in New York. His first job there is taking photos of the animals at Brooklyn Paws, an animal shelter, for its adoption website. Jess works at the shelter.</p>
{audiocard(["01.1 · SLOW", "01.1 · NATURAL"])}
{sub("A", "Listen. How many dogs and how many cats does Jess introduce?", "2 min", "01.1 · SLOW")}
<div class="wline">{R("two dogs (Max and Rocky) and two cats (Luna and Ginger)")}</div>
{sub("B", "Listen again and complete the table. Write one or two words.", "6 min", "01.1 · NATURAL")}
<table style="table-layout:fixed;font-size:9pt"><tr><th style="width:18mm"></th><th>looks like</th><th>is (personality)</th><th>likes</th><th>would like (now)</th></tr>{rows}</table>
<div class="bank">bright orange · calm · chasing balls · dark brown · go out for a walk · lazy · light brown · pale gray · people · playful · sociable · take a nap · watching people</div>
{sub("C", "Which animal would you like to adopt? Why?", "2 min")}
<div class="wline"></div>""",
    26, """<ol><li>A: <b>slow</b> version. <b>an animal shelter</b> = a place for dogs and cats without a home; people go there to <b>adopt</b> a pet. Very common in the US.</li>
<li>B: <b>natural</b> version. Max's "would like" is not in the audio: accept "—". Luna doesn't like other cats; Ginger likes people.</li></ol>""")

    # Page 3
    b.page(f"""{sec(3, "Language focus: four questions with like", "10 min")}
{sub("A", "Read the questions and answers from the conversation. Match each question with the information it asks for.", "4 min")}
<table style="table-layout:fixed;font-size:9.3pt"><tr><th>Question</th><th>Answer</th><th style="width:42mm">It asks about…</th></tr>
<tr><td>1. What does Max <b>look like</b>?</td><td>He has light brown fur.</td><td>{A("appearance", "min-width:30mm")}</td></tr>
<tr><td>2. What's Luna <b>like</b>?</td><td>She's a little lazy.</td><td>{A("personality", "min-width:30mm")}</td></tr>
<tr><td>3. What does Rocky <b>like doing</b>?</td><td>He likes to sit and watch people.</td><td>{A("things he usually enjoys", "min-width:30mm")}</td></tr>
<tr><td>4. <b>Would</b> you <b>like</b> to meet more animals?</td><td>Yes, I would!</td><td>{A("something you want now", "min-width:30mm")}</td></tr></table>
<div class="bank">appearance · personality · something you want now · things he usually enjoys</div>
{sub("B", "Choose the correct option.", "3 min")}
<ol><li><i>What does he like doing?</i> = <i>What does he like to do?</i> Both are {ch(["correct", "wrong"], "correct")}.</li>
<li>After <i>would like</i>, we use {ch(["to + verb", "verb + -ing"], "to + verb")}: She'd like to take a nap.</li>
<li>The short answer to <i>Would you like…?</i> is {ch(["Yes, I like.", "Yes, I would."], "Yes, I would.")}</li></ol>
{sub("C", "Write the four questions about Max and Rocky (they).", "3 min")}
<div class="two"><div><div class="wline">1. {R("What do they look like?")}</div><div class="wline">2. {R("What are they like?")}</div></div>
<div><div class="wline">3. {R("What do they like doing?")}</div><div class="wline">4. {R("Would they like…?")}</div></div></div>
<div class="box sand"><h4>REMEMBER</h4><b>look like</b> = appearance · <b>be like</b> = personality · <b>like</b> = enjoy (usually) · <b>would like</b> = want (now, polite)<br>
'd = would: She<b>'d</b> like a snack. · He<b>'d</b> like to go out.</div>""",
    24, """<ol><li>A: the four questions sound similar. Say one question; the student says the type of answer it needs. Then change roles.</li>
<li>B: American English prefers <i>like to do</i> a little; British English prefers <i>like doing</i>. Both are fine.</li></ol>""")

    # Grammar reference (before Common mistakes)
    grammar_ref.questions_with_like(b)

    # Page 4
    b.page(f"""{sub("D", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>How is your brother? (= personality)</td><td><b>What's your brother like?</b></td><td><i>How is he?</i> asks about health.</td></tr>
<tr><td>What does she look?</td><td><b>What does she look like?</b></td><td>Appearance: <i>look like</i>.</td></tr>
<tr><td>He likes play with balls.</td><td><b>He likes playing / to play…</b></td><td>like + -ing or to + verb.</td></tr>
<tr><td>I would like go out.</td><td><b>I'd like to go out.</b></td><td>would like + <i>to</i>.</td></tr>
<tr><td>Would you like a coffee? — Yes, I like.</td><td><b>Yes, I would. / Yes, please.</b></td><td>Short answer with <i>would</i>.</td></tr>
<tr><td>She has long brown hairs.</td><td><b>She has long brown hair.</b></td><td><i>hair</i> is uncountable.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "5 min")}
{audiocard(["01.2", "01.3"])}
{sub("A", "Shades and patterns. Listen and repeat. How many syllables?", "2 min", "01.2")}
<table style="table-layout:fixed;margin-top:0"><tr>{"".join(f"<td style='text-align:center'><b>{w}</b><br><span class='small'>{R(n) if T else '___'}</span></td>" for w, n in zip(S012, ['1','1','1','1','1','2','2','1']))}</tr></table>
{sub("B", "The four questions. Listen and repeat.", "2 min", "01.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S013)}</div>
<div class="box" style="margin-top:1mm"><h4>LISTEN CAREFULLY</h4>In fast speech, <b>What's she like?</b> sounds like <i>whatshee-like</i>, and <b>What does she…</b> sounds like <i>whuddushee</i>. The last word tells you the question: <b>like?</b> (personality) or <b>look like?</b> (appearance).</div>""",
    24, """<ol><li>4A: <b>striped</b> = 1 syllable /straɪpt/, <b>spotted</b> = 2 /ˈspɑtɪd/, <b>shiny</b> = 2 /ˈʃaɪni/.</li>
<li>4B: wh- questions go down at the end; <i>Would she like a snack?</i> goes up.</li></ol>""")

    # Page 5
    jess = [("What does Jess look like?", "She's tall and has short curly", "hair", "."), ("What's Jess like?", "She's very", "patient", ". She's never angry with the animals."),
            ("What does Jess like doing?", "She likes", "walking", "the dogs in the park on Sundays."), ("What would Jess like?", "She'd like a", "vacation", "! She works six days a week.")]
    ginger = [("What does Ginger look like?", "She has bright orange", "fur", "and green eyes."), ("What's Ginger like?", "She's really", "sociable", ". She loves people."),
              ("What does Ginger like doing?", "She likes", "to", "sleep in the sun."), ("What would Ginger like?", "She'd like a new", "toy", "because she lost her old one.")]
    def prof(rows): return "".join(f"<li><div class='wline' style='min-height:5mm'>{R(q)}</div>{a} {A(g, 'min-width:16mm')} {c}</li>" for q, a, g, c in rows)
    wb = [("tall", "A"), ("friendly", "P"), ("curly hair", "A"), ("shy", "P"), ("a beard", "A"), ("patient", "P"), ("glasses", "A"), ("lazy", "P"), ("slim", "A"), ("funny", "P")]
    wbl = " &nbsp; ".join(f"{w} {A(x, 'min-width:8mm')}" for w, x in wb)
    b.page(f"""{sec(5, "Practice", "8 min")}
{sub("A", "Paulo is writing profiles for the shelter website. Write the question for each answer. Then complete the answers.", "5 min")}
<div class="bank">fur · hair · patient · sociable · to · toy · vacation · walking</div>
<div class="two"><div><b style="color:#0f4a5a">Jess (volunteer coordinator)</b><ol>{prof(jess)}</ol></div><div><b style="color:#0f4a5a">Ginger (cat)</b><ol>{prof(ginger)}</ol></div></div>
<div class="box" style="margin-top:1mm"><h4>WORD BUILDER: APPEARANCE (A) OR PERSONALITY (P)?</h4><span style="line-height:2">{wbl}</span></div>""",
    22, """<p>A: the student writes the four questions with <i>look like / be like / like doing / would like</i>, then fills the gaps. Word builder: ask the student to describe a family member with two A words and two P words. More words come from the bonus lesson <i>Describing appearance</i> (Vocabulary to Go).</p>""")

    # Page 6
    mine = [("Bella (dog)", "black and white, spotted", "friendly", "swim in the lake", "a bowl of water"), ("Mike (volunteer)", "light blue eyes, a beard", "helpful", "read about history", "a cup of coffee")]
    theirs = [("Oscar (cat)", "gray and white, striped tail", "shy", "eat fish (alone!)", "a quiet place"), ("Nina (volunteer)", "short dark hair, glasses", "funny", "cook for her friends", "to go home and sleep")]
    def tr(rows, show):
        return "".join(f"<tr><td><b>{n}</b></td>" + "".join(f"<td class='small'>{x if show else R(x)}</td>" for x in r) + "</tr>" for n, *r in rows)
    head = "<tr><th style='width:28mm'>name</th><th>looks like</th><th>is like</th><th>likes</th><th>would like now</th></tr>"
    b.page(f"""{sec(6, "Speaking", "12 min")}
{sub("A", "Information gap. Answer your teacher's questions about Bella and Mike. Then ask about Oscar and Nina and complete the table.", "7 min")}
<p class="small"><b>Your information</b></p>
<table style="table-layout:fixed;font-size:8.8pt;margin-top:0">{head}{tr(mine, True)}</table>
<p class="small"><b>Ask your teacher</b> (What does… look like? What's… like? What does… like doing? What would… like?)</p>
<table style="table-layout:fixed;font-size:8.8pt;margin-top:0">{head}{"".join(f"<tr><td style='height:8mm'><b>{n}</b></td>" + "".join(f"<td class='small'>{R(x)}</td>" for x in r) + "</tr>" for n, *r in theirs)}</table>
<div class="msg" style="max-width:none;padding:1.5mm 4mm;line-height:1.5"><b>You:</b> What does Oscar look like? <b>Teacher:</b> He's gray and white, and he has a striped tail. <b>You:</b> Is Oscar a cat?</div>
{sub("B", "People you know. Choose a friend or a family member. Your teacher asks the four questions.", "5 min")}
<ol><li>What does he / she look like?</li><li>What's he / she like?</li><li>What does he / she like doing on the weekend?</li><li>What would he / she like for his / her next birthday?</li></ol>""",
    22, """<ol><li>A: you have Oscar and Nina (in red). The student has Bella and Mike. Use the four questions; at the end the student says who is an animal and who is a volunteer.</li>
<li>B: then answer the four questions about someone in your family. Correct <i>How is…?</i> for personality.</li></ol>""")

    # Page 7
    pc = [("A1 Unit 32", "I can talk about my plans and arrangements for the future."), ("A1 Unit 33", "I can make predictions with will / won't."),
          ("A1 Unit 34", "I can give advice with should, could and imperatives."), ("A1 Unit 35", "I can explain rules with must, mustn't, can and can't."),
          ("A2 Unit 01", "I can ask and talk about appearance, personality, likes and wishes.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [(["look", "look like", "like"], "look like", "What does your sister", "? — She has long dark hair."), (["What's", "How is", "What does"], "What's", "", "your boss like? — He's very calm."),
          (["walk", "walking", "to walking"], "walking", "My dog likes", "in the park."), (["have", "to have", "having"], "to have", "I'd like", "a nap now."),
          (["Yes, I like.", "Yes, I would.", "Yes, I do."], "Yes, I would.", "Would you like some tea? —", ""), (["hair", "hairs", "a hair"], "hair", "He has short gray", ".")]
    hl = "".join(f"<li>{a} {ch(o, r)} {c}</li>" for o, r, a, c in hw)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Choose the correct option.</b></p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. A profile (50–75 words).</b> Write a profile of a pet or a person you know for a website. Answer the four questions: What does … look like? What's … like? What does … like doing? What would … like?</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class: start with homework 2. Ask the four questions about the profile before you read it. Welcome to A2: the homework is longer now, so correct it and keep it as a writing sample.</p>""")

    b.extra("Audio scripts", f"""
{sub("01.1", "At the animal shelter (slow and natural)")}
<p style="line-height:1.5">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("01.2", "Shades and patterns")}
<p>{" · ".join(S012)}</p>
{sub("01.3", "The four questions")}
<p>{" ".join(S013)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 01 - It's like this")
