# Speak! Progress B1 - Unit 52 "Animals" (all English) - lean B1 format
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
setup(band="B1 · UNIT 52", audio_json="audio_b1-unit-52.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-52"]
S521 = [l.split(": ", 1) for l in _r["52.1 Gap Year Diaries: live from the Pantanal"].split("\n")]
S522 = [x.split(": ", 1)[1] for x in _r["52.2 Repeat: I saw it drinking"].split("\n")]



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
    cover = cover_html(T, "LEVEL B1 · UNIT 52", "Animals", "Wildlife and animal expressions · <b>I saw it cross · I heard them calling</b>",
                       [("YOU CAN", "describe animals and say what you saw, heard or felt on a trip"),
                        ("LANGUAGE", "predator · prey · endangered species · as quiet as a mouse · see / hear / watch + object + verb"),
                        ("PRONUNCIATION", "weak as /əz/ in similes · linking: saw_it, heard_a")])
    animals = ["a bee", "a cow", "a crab", "an elephant", "a fly", "a gorilla", "a monkey", "an octopus", "a pig", "a sheep", "a spider", "a whale"]
    cats = [("in the jungle", "an elephant, a gorilla, a monkey"), ("in the sea", "a crab, an octopus, a whale"),
            ("on a farm", "a cow, a pig, a sheep"), ("in your home or garden", "a bee, a fly, a spider")]
    ct = "".join(f'<tr><td style="width:36mm"><b>{c}</b></td><td>{A(a, "min-width:80mm")}</td></tr>' for c, a in cats)
    b.page(f"""{sec(1, "Warm-up: where do they live?", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["What's your favorite animal? Why?", "Which wild animals have you seen in Brazil?", "Are you afraid of any animals?"], "START TALKING")}</div></div>
{sub("A", "Where can you usually find these animals? Write them in the table.", "3 min")}
<div class="bank">{" · ".join(animals)}</div>
<table style="font-size:8.6pt;margin:.8mm 0">{ct}</table>
{talk(["Add two more animals to each group.", "Which of these animals would you never touch?", "What unusual animals do people keep as pets?"], "USE THE WORDS")}""",
    30, """<ol><li>Top box: 3 minutes. Pre-teach <i>wild</i> (not living with people) and <i>in the wild</i> (in nature, not in a zoo).</li>
<li>A: 4 minutes with the questions. Spiders are possible in the jungle too: accept it. Extra animals: jungle (a parrot, a snake, a jaguar), sea (a shark, a dolphin), farm (a horse, a goat, a chicken), home or garden (an ant, a mosquito).</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Gap Year Diaries live from the Pantanal: Danny and Bruno · which animals? · questions · Talk about it",
                      "verbs of perception: see / hear / watch / feel / notice + object + base form or -ing; see vs watch vs look at; hear vs listen to", "Choose the correct form · join the sentences · Use it (oral)",
                      "weak forms (52.2) · animal similes · describing animals: guess the animal · long turn: an animal you saw in the wild", "Bruno's message to his uncle · predator and prey · watch out · writing about an amazing animal"),
        """The Linguahouse lesson is vocabulary only: classifying animals by habitat, naming wild animals, predators and prey, animal similes and a guessing game. It has no listening and no grammar, so we added a Gap Year Diaries episode and a new B1 grammar point: verbs of perception (I saw it cross / I saw it crossing). Story: Danny and Bruno are at a small lodge by a river in the Pantanal (the trip planned in Review 4). At five a.m. they heard howler monkeys screaming outside their window (Danny was as scared as a rabbit). On a boat trip they saw dozens of caimans lying in the sun and watched a family of capybaras swim across the river; a huge green insect landed on Danny's head. Bruno's favorite moment: two blue macaws flew over the boat. When Bruno was a kid, his uncle took him there and he saw a jaguar drinking from the river (Unit 32); the guide noticed fresh tracks near the lodge, so they are going out again tonight. In the homework, Bruno tells his uncle that they saw a jaguar. The animal facts are kept simple and general: these animals all live in the Pantanal.""",
        """<i>I saw the monkeys to jump</i> (no <i>to</i>); <i>I heard she sing</i> (object pronoun); <i>I listened a noise</i> (→ <i>heard</i>). Vocabulary: <i>an animal in extinction</i> (→ <i>an endangered species</i>); <i>bug</i> for insects in informal American English. Pronunciation: weak <i>as</i> /əz/ in similes.""",
        "Track 52.1 Gap Year Diaries: live from the Pantanal (natural and slow; Danny and Bruno) · Track 52.2 Repeat: I saw it drinking"))

    # Page 2 - Listening
    seen = [("howler monkeys", True), ("caimans", True), ("capybaras", True), ("a snake", False), ("an insect", True), ("macaws", True), ("a toucan", False), ("a jaguar (when Bruno was a kid)", True)]
    tl = " &nbsp; ".join(f"☐ {t}{(' ' + R('✓')) if ok else ''}" for t, ok in seen)
    qs = [("Why did they wake up at five o'clock?", "They heard howler monkeys screaming outside the window."),
          ("What were the caimans doing?", "Lying in the sun."),
          ("What happened to Danny on the boat?", "A huge green insect landed on his head."),
          ("Why are they going out again tonight?", "The guide noticed fresh jaguar tracks near the lodge.")]
    ql = "".join(f"<li>{q} {A(a, 'min-width:46mm')}</li>" for q, a in qs)
    b.page(f"""{sec(2, "Listening: live from the Pantanal", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
<p style="margin:0 0 1mm;font-size:8.8pt">Danny and Bruno are on a trip to the Pantanal, a huge wetland in the center-west of Brazil.</p>
{sub("A", "Listen. Which animals do they talk about? Check six.", "3 min")}
<p style="font-weight:600;font-size:8.7pt;line-height:1.6;margin:0">{tl}</p></div>{img('B', 36, 26)}</div>
{audiocard(["52.1 · NATURAL", "52.1 · SLOW"])}
{sub("B", "Listen again and answer.", "4 min")}
<ol style="line-height:1.5;font-size:8.6pt;margin:0">{ql}</ol>
<p style="margin:.6mm 0;font-size:8.6pt"><b>Think about it:</b> Danny says there's "a slight chance" they will see a jaguar, but Bruno says "a good chance". Why do you think they disagree? {A("open answer: Bruno is excited and has seen one before; Danny doesn't want to be disappointed", "min-width:20mm")}</p>
<div class="box sand" style="margin:.8mm 0;font-size:8.4pt"><h4>NOTICE: ANIMAL SIMILES</h4>I was <b>as scared as a rabbit</b>. · I was <b>as quiet as a mouse</b>. (similes compare two things with <b>as … as</b>)</div>
{talk(["Have you ever been to the Pantanal or the Amazon? Would you like to go?", "What's the most amazing animal you've seen in the wild?", "Would you go out at night to look for a jaguar?"])}""",
    35, """<ol><li>A: play the natural version; play the slow one if needed. The snake and the toucan are not mentioned.</li>
<li>B: ask the student to find what they <i>heard</i>, <i>saw</i>, <i>watched</i>, <i>felt</i> and <i>noticed</i>: <i>heard something screaming, saw caimans lying, watched capybaras swim, felt something land, saw two macaws fly, saw a jaguar drinking, noticed some fresh tracks</i>. They come back on page 3.</li>
<li>Talk about it: 4 minutes.</li></ol>""")

    # Page 3
    lean.grammar_in_class(b, grammar_ref.perception_verbs)

    # Page 4 - Practice
    pc = [("I saw the monkeys", ["jump", "to jump"], "jump", "from tree to tree."), ("We", ["heard", "listened"], "heard", "a strange noise last night."),
          ("I heard", ["she", "her"], "her", "singing in the shower."), ("We watched the sun", ["set", "sets"], "set", "over the river."),
          ("Did you", ["listen to", "hear"], "listen to", "the birds this morning? They were beautiful."), ("I felt the boat", ["moving", "to move"], "moving", "under my feet."),
          ("", ["Look at", "Look"], "Look at", "that bird! It's huge!"), ("She noticed a man", ["following", "follows"], "following", "her.")]
    cl = "".join(f"<li>{a + ' ' if a else ''}{ch(o, r)} {z}</li>" for a, o, r, z in pc)
    rw = [("The capybaras swam across the river. We watched them.", "We watched the capybaras swim across the river."),
          ("The monkeys were screaming. I heard them.", "I heard the monkeys screaming."),
          ("Something landed on my head. I felt it.", "I felt something land on my head.")]
    rwl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw)
    use = ["What did you hear when you woke up this morning?", "Have you ever seen an animal do something funny or strange? What did you see it do?",
           "What can you see people doing from your window right now?", "Have you ever felt the ground shake or a building move?",
           "Do you like watching animals? Where: at the zoo, in the wild, on TV?"]
    b.page(f"""{sec(4, "Practice: what did you see?", "10 min")}
{sub("A", "Choose the correct words.", "3 min")}
<ol style="line-height:1.7;font-size:8.7pt;margin:0;columns:2;column-gap:6mm">{cl}</ol>
{sub("B", "Join the sentences. Start with the person.", "4 min")}
<ol style="line-height:1.45;font-size:8.7pt;margin:0">{rwl}</ol>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    30, """<ol><li>A: 3 minutes. Item 5: <i>listen to</i> because they paid attention for some time. Item 8: <i>follow</i> is also possible (<i>noticed a man follow her</i>), but <i>following</i> is more natural for an action in progress.</li>
<li>B: in item 2, <i>scream</i> is also correct, but <i>screaming</i> shows a long, repeated action.</li>
<li>Use it: 3 minutes, all oral. Push for an object + verb after every <i>see / hear / watch</i>.</li></ol>""")

    # Page 5 - Speaking
    sim = ["bat", "bee", "cow", "fox", "mouse", "rabbit"]
    sim_l = [("as quiet as a", "mouse"), ("as blind as a", "bat"), ("as scared as a", "rabbit"), ("as busy as a", "bee"), ("as cunning as a", "fox"), ("as awkward as a", "cow", " on roller skates")]
    sl = "".join(f'<li>{x[0]} {A(x[1], "min-width:14mm")}{x[2] if len(x) > 2 else ""}</li>' for x in sim_l)
    card = f"""<div class="box" style="margin-top:1mm;font-size:8.2pt">{R("<b>Teacher's card (C):</b> think of an animal (for example a crocodile, an eagle, a dolphin, a bee). Give one clue at a time with the phrases in the box; the student guesses after each clue. Then change roles: the student chooses an animal. Play three or four rounds each.")}</div>""" if T else ""
    b.page(f"""{sec(5, "Speaking: describing animals", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE: DESCRIBING AN ANIMAL</h4>
<table style="margin:0;font-size:8.2pt"><tr><th>where</th><th>food</th><th>habits</th><th>abilities and danger</th></tr>
<tr><td><i>It lives in the sea / on a farm / in the jungle. · It can be found in Africa / South America.</i></td><td><i>It preys on… · It feeds on… · It's a predator. · It's prey for…</i></td><td><i>It hunts at night / during the day. · It lives in groups. · It needs … to survive.</i></td><td><i>It can fly / swim / climb trees. · It can bite / sting / poison you. · It's an endangered species.</i></td></tr></table></div>
{audiocard(["52.2"])}
{sub("A", "Listen and repeat. Say as /əz/: as quiet as a mouse.", "2 min", "52.2")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S522))}</p>
{sub("B", "Animal similes. Complete them with the animals from the box. Then use one to describe someone you know.", "4 min")}
<div class="bank" style="font-size:8.6pt;background:#fff">{" · ".join(sim)}</div>
<ol style="font-size:8.6pt;line-height:1.55;margin:0;columns:2;column-gap:6mm">{sl}</ol>
{sub("C", "Guess the animal. Your teacher thinks of an animal and gives clues. Guess it. Then change roles.", "5 min")}{card}
{sub("D", "Long turn. What wild animals live in your region? Are any of them endangered? Tell your teacher about an animal you saw in the wild (or would love to see).", "4 min")}""",
    30, """<ol><li>B: <i>as busy as a bee</i> replaces a Linguahouse simile that is rude about people's weight. <i>Cunning</i> = clever in a dishonest way.</li>
<li>C comes from the Linguahouse guessing game. D: give opinions, not numbers; there is no need to know real statistics. Last 3 minutes: wrap-up (two corrections, and ask <i>Can you now describe animals and say what you saw and heard?</i>).</li></ol>""")

    # Homework
    pc2 = [(["see", "to see"], "see"), (["walking", "walks"], "walking"), (["heard", "listened"], "heard"), (["him", "he"], "him"),
           (["drink", "drinks"], "drink"), (["watched", "looked"], "watched")]
    p = [ch(o, a) for o, a in pc2]
    pp = [("an eagle", "a mouse"), ("a crocodile", "a zebra"), ("a dolphin", "small fish"), ("a wolf", "a rabbit"), ("a spider", "a butterfly"), ("a leopard", "a goat")]
    prey_sorted = sorted([y for x, y in pp], key=lambda s: s.split(" ", 1)[-1])
    ppl = "".join(f'<li>{x} → {A(y, "min-width:22mm")}</li>' for x, y in pp)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Bruno writes to his uncle after the trip. Choose the correct words.", "")}</div>{img('C', 30, 19)}</div>
<div class="box" style="line-height:1.85;font-size:8.8pt;margin:.5mm 0"><b>Hi Uncle Beto!</b> Guess what? Twenty years later, I saw a jaguar again! On our last night, the guide made us {p[0]} the tracks near the lodge, and two hours later we saw a big jaguar {p[1]} along the river. Nobody said a word. Then we {p[2]} Danny whispering "Wow!" and the jaguar looked at {p[3]}! It didn't run away. We saw it {p[4]} from the river, just like the one you showed me. We {p[5]} it for ten minutes. Thanks for bringing me here when I was a kid! Bruno</div>
{sub("B", "Predator and prey. Match each predator with its typical prey.", "")}
<div class="bank" style="font-size:8.6pt">{" · ".join(prey_sorted)}</div>
<ol style="font-size:8.6pt;line-height:1.55;margin:0;columns:2;column-gap:6mm">{ppl}</ol>
{lean.watch_out([("It's an animal in extinction.", "It's an endangered species.", "the phrase is <i>endangered species</i>."), ("I listened a strange noise.", "I heard a strange noise.", "<i>hear</i> = the sound reaches you; <i>listen to</i> = you pay attention."), ("Look the monkey!", "Look at the monkey!", "<i>look at</i> something.")])}
{lean.writing_task(sub, "Write a post for Danny's podcast page: the most amazing animal you've seen (in the wild, at a zoo or on a trip).", "The most amazing animal I've ever seen…", ["where and when you saw it", "what you saw it doing / heard it doing", "how you felt (a simile?)", "at least three verbs of perception", "100–150 words"], "I can describe animals and say what I saw, heard or felt on a trip.")}""",
    25, """<p>Check A and B in 3 minutes at the start of the next class. In A, <i>made us see</i>: <i>make</i> also takes the base form. Uncle Beto is new: Bruno's uncle from Unit 32 now has a name. Read the writing at home and choose two mistakes to discuss in class.</p>""")

    script = "".join(f"<p style='margin:.5mm 0'><b>{s}:</b> {t}</p>" for s, t in S521)
    b.extra("Audio script", f"""
{sub("52.1", "Gap Year Diaries: live from the Pantanal (natural and slow; Danny and Bruno)")}
<div style="line-height:1.3;font-size:8.3pt">{script}</div>
{sub("52.2", "Repeat: I saw it drinking")}
<p>{" · ".join(S522)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 52 - Animals")
