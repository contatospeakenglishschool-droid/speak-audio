# Speak! Progress B1 - Unit 51 "Pet benefits" (all English) - lean B1 format
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
setup(band="B1 · UNIT 51", audio_json="audio_b1-unit-51.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-51"]
S511 = [l.split(": ", 1)[1] for l in _r["51.1 Danny's blog: our new roommate has four legs"].split("\n")]
S512 = [x.split(": ", 1)[1] for x in _r["51.2 Repeat: must have, should have"].split("\n")]


TITLE = "Our new roommate has four legs"
PARAS = [S511[0].replace(TITLE + ". ", "", 1)] + S511[1:]


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
    cover = cover_html(T, "LEVEL B1 · UNIT 51", "Pet benefits", "Animals and well-being · <b>He must have… · We should have…</b>",
                       [("YOU CAN", "talk about the pros and cons of pets, guess what happened and say what someone should have done"),
                        ("LANGUAGE", "stroke · confide in · isolation · self-esteem · relieve stress · must have · should have · On the whole…"),
                        ("PRONUNCIATION", "must've /ˈmʌstəv/ · should've /ˈʃʊdəv/")])
    words = ["confide", "immune system", "isolation", "playmate", "recover", "self-esteem", "stroke", "well-being"]
    defs = {"confide": "(in somebody) to tell them a secret because you trust them",
            "immune system": "the part of your body that fights against diseases",
            "isolation": "the feeling of being alone and lonely",
            "playmate": "a friend that a child often plays with",
            "recover": "to become healthy or happy again after an illness or a sad time",
            "self-esteem": "confidence in yourself and your abilities",
            "stroke": "to move your hand gently over an animal's head or back",
            "well-being": "the state of feeling happy, healthy and comfortable"}
    order = [3, 7, 0, 5, 1, 6, 2, 4]
    kwl = "".join(f'<li>{A(words[i], "min-width:24mm")} <span style="color:#6b7377">= {defs[words[i]]}</span></li>' for i in order)
    b.page(f"""{sec(1, "Warm-up: people and pets", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["Do you have a pet, or did you have one as a child? Why or why not?", "Which animals are popular pets in Brazil?", "Are you a dog person or a cat person?"], "START TALKING")}</div></div>
{sub("A", "Key words. Write the words from the box next to their meanings.", "3 min")}
<div class="bank">{" · ".join(words)}</div>
<ol style="font-size:8.6pt;line-height:1.7;margin:0">{kwl}</ol>
{talk(["What do you do to relieve stress? Does an animal help?", "Who do you confide in when you have a problem?", "Is isolation a problem for older people in your city?"], "USE THE WORDS")}""",
    30, """<ol><li>Top box: 3 minutes. Accept any animals: dogs, cats, birds, fish, turtles.</li>
<li>A: 4 minutes with the questions. In American English, <i>pet</i> is also a verb: <i>Can I pet your dog?</i> (= stroke). <i>Confide</i> takes <i>in</i>: <i>She confides in her dog.</i></li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Danny's blog: Mrs. Lima adopts a dog for the hostel · questions · find the words · Talk about it",
                      "past modals: must have / might have / can't have (guessing); should have / shouldn't have / could have (regret, criticism)", "Choose the correct form · rewrite · Use it (oral)",
                      "must've, should've (51.2) · developing an argument (In general, For example, In addition, However, On the whole) · What happened? · long turn: benefits and drawbacks", "Mrs. Lima's note to the guests · rewrite · watch out · writing: pets in apartments",
                      listen_label="Reading"),
        """The Linguahouse lesson is a newspaper article that summarizes real studies on the health benefits of pets (with statistics and named universities). We did not use the article, because we cannot check its numbers. Instead, the student reads a post from Danny's blog, also recorded as audio. Last month Mrs. Lima adopted a dog from an animal shelter: Pipoca. He must have lived on the street (he was thin and scared); he can't have been more than two. Guests stroke him and relax; Mrs. Lima walks him twice a day and feels less isolated in the evenings since her husband died ("I confide in him more than in my children!"). Danny walked him when he was homesick; Bruno has a new running partner (Pipoca runs faster). Problems: one guest was allergic and changed rooms; last Sunday someone left the gate open and Pipoca disappeared for three hours (found at the bakery); they should have checked the gate. We kept the Linguahouse key words, the health collocations, the argument linkers, the talking points and the discussion topics, and added a new B1 grammar point: past modals.""",
        """<i>He must lived / must have went</i>; <i>should of</i>; <i>mustn't have</i> for an impossible past (→ <i>can't have</i>). Vocabulary: <i>I create a dog</i> (→ <i>have / raise</i>); <i>pass the hand on</i> (→ <i>stroke / pet</i>); <i>educated</i> (→ <i>well-behaved</i>). Pronunciation: <i>must've</i> /ˈmʌstəv/, <i>should've</i> /ˈʃʊdəv/.""",
        "Track 51.1 Danny's blog: our new roommate has four legs (natural and slow; read by Danny) · Track 51.2 Repeat: must have, should have"))

    # Page 2 - Reading
    text = "".join(f"<p style='margin:0 0 1mm'>{p}</p>" for p in PARAS)
    qs = [("Where did Pipoca come from, and what did he look like?", "From an animal shelter; he was very thin and scared."),
          ("How does Pipoca help tired guests?", "They stroke him and relax."),
          ("How has the dog changed Mrs. Lima's life?", "She walks twice a day and feels less alone; she talks to him."),
          ("What two problems does Danny mention?", "A guest was allergic; Pipoca ran away when the gate was left open.")]
    ql = "".join(f"<li>{q} {A(a, 'min-width:40mm')}</li>" for q, a in qs)
    fw = [("very slim, maybe not healthy (P1)", "thin"), ("a place for animals with no home (P1)", "shelter"), ("two times (P2)", "twice")]
    fwl = " &nbsp;·&nbsp; ".join(f"{d} {A(w, 'min-width:14mm')}" for d, w in fw)
    b.page(f"""{sec(2, "Reading: a new roommate", "12 min")}
{sub("A", "Read Danny's blog post. What is the new roommate? Is Danny for or against pets in hostels now?", "5 min")}
<div class="box" style="margin:.5mm 0;font-size:8.3pt;line-height:1.38"><div style="float:right;margin:0 0 1mm 2.5mm">{img('B', 34, 23)}</div><b style="font-size:9.4pt;color:#176074">{TITLE}</b><br>{text}</div>
{audiocard(["51.1 · NATURAL", "51.1 · SLOW"])}
{sub("B", "Read again and answer.", "4 min")}
<ol style="line-height:1.45;font-size:8.5pt;margin:0">{ql}</ol>
<p style="margin:.6mm 0;font-size:8.5pt"><b>Find the words:</b> {fwl}</p>
<div class="box sand" style="margin:.8mm 0;font-size:8.3pt"><h4>NOTICE: HEALTH COLLOCATIONS</h4>relieve stress · make trips to the doctor · recover from an illness · improve your well-being · spread disease</div>""",
    30, """<ol><li>A: a dog, Pipoca; Danny is for it now (<i>our hostel feels more like a home</i>). Students can read and listen at the same time.</li>
<li>B: ask the student to find <i>must have, can't have, should have</i> in the text. They come back on page 3. Point out the linkers too: <i>In general, For example, In addition, On top of that, Indeed, However, On the other hand</i> (page 5).</li>
<li>Collocations: ask <i>What helps you relieve stress? What can improve your well-being?</i></li></ol>""")

    # Page 3
    lean.grammar_in_class(b, grammar_ref.past_modals)

    # Page 4 - Practice
    pc = [("The floor is wet. The dog", ["must have", "should have"], "must have", "knocked over his water."), ("You", ["must have", "should have"], "should have", "told me you were allergic!"),
          ("She", ["can't have", "mustn't have"], "can't have", "seen the message: her phone was off."), ("He's not answering. He", ["might have", "should have"], "might have", "gone to bed early."),
          ("We", ["shouldn't have", "can't have"], "shouldn't have", "left the gate open."), ("They must have", ["went", "gone"], "gone", "for a walk."),
          ("You look tired. You", ["must be", "must have been"], "must be", "exhausted."), ("I could have", ["helped", "help"], "helped", "you, but you didn't ask.")]
    cl = "".join(f"<li>{a} {ch(o, r)} {z}</li>" for a, o, r, z in pc)
    rw = [("I'm sure someone left the gate open. (must)", "Someone must have left the gate open."),
          ("It was a mistake to give the dog chocolate. (shouldn't)", "You shouldn't have given the dog chocolate."),
          ("I'm sure he wasn't more than two years old. (can't)", "He can't have been more than two years old.")]
    rwl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw)
    use = ["Your neighbor's dog barked all night. What might have happened?", "A friend arrived at work with wet hair and no umbrella. What must have happened?",
           "Think of a mistake you made with a pet or a plant. What should you have done?", "Your cat is sleeping in the laundry basket, and there are clean clothes on the floor. What must have happened?",
           "Tell me about something you should have done last week but didn't."]
    b.page(f"""{sec(4, "Practice: what must have happened?", "10 min")}
{sub("A", "Choose the correct words.", "3 min")}
<ol style="line-height:1.7;font-size:8.7pt;margin:0;columns:2;column-gap:6mm">{cl}</ol>
{sub("B", "Rewrite the sentences with the modal in brackets.", "4 min")}
<ol style="line-height:1.45;font-size:8.7pt;margin:0">{rwl}</ol>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    30, """<ol><li>A: 3 minutes. Item 7 is about now (<i>You look tired</i>), so <i>must be</i>. Item 3: <i>can't have</i>, not <i>mustn't have</i>.</li>
<li>B: accept <i>We / Someone shouldn't have…</i> in item 2.</li>
<li>Use it: 3 minutes, all oral. Accept any logical guess; ask <i>How sure are you?</i> to push for <i>must / might / can't</i>.</li></ol>""")

    # Page 5 - Speaking
    card = f"""<div class="box" style="margin-top:1mm;font-size:8.2pt">{R("<b>Teacher's card (B):</b> read the scenes one at a time. The student guesses with must have / might have / can't have, then says what someone should or shouldn't have done. (1) You come home. The sofa cushion is on the floor, and the dog is hiding under the bed. (2) Your neighbor's cat came back after three days, fat and happy. (3) A friend's new puppy cried all night. (4) The fish in the office aquarium are gone, and the office cat looks very pleased.")}</div>""" if T else ""
    topics = ["using social media", "cell phones", "drinking coffee", "living in a big city", "living in the countryside", "using public transportation", "having a pet in an apartment"]
    b.page(f"""{sec(5, "Speaking: developing an argument", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE: DEVELOPING AN ARGUMENT</h4>
<table style="margin:0;font-size:8.2pt"><tr><th>talking in general</th><th>giving an example</th><th>adding a point</th><th>a supporting point</th><th>a contrast</th></tr>
<tr><td><i>In general, … · On the whole, …</i></td><td><i>For example, … · …, for instance, …</i></td><td><i>In addition, … · Furthermore, (formal) · On top of that, (informal)</i></td><td><i>Indeed, …</i></td><td><i>However, … · But… · On the other hand, …</i></td></tr></table></div>
{audiocard(["51.2"])}
{sub("A", "Listen and repeat. Say must've, should've, might've.", "3 min", "51.2")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S512))}</p>
{sub("B", "What happened? Your teacher describes four scenes. Guess what happened and say what someone should have done.", "4 min")}{card}
{sub("C", "Discuss. Is it ethical to keep pets? What animals should not be kept as pets? Why?", "4 min")}
{sub("D", "Long turn. Choose a topic. Talk about the benefits and drawbacks for two minutes. Use at least four linkers from the box.", "5 min")}
<div class="bank" style="font-size:8.6pt;background:#fff">{" · ".join(topics)}</div>
<p style="margin:.3mm 0;font-size:8.5pt">Plan (1 min, notes only): {lines(1)}</p>""",
    30, """<ol><li>B: any logical answer is fine; push for both kinds of modal (<i>The dog must have… · You shouldn't have left…</i>).</li>
<li>C comes from the Linguahouse talking point; D is the Linguahouse discussion, with one extra topic. 1 minute for notes (no full sentences), 2 minutes to talk; then ask one follow-up question. Last 3 minutes: wrap-up (two corrections, and ask <i>Can you now talk about pros and cons and guess what happened?</i>).</li></ol>""")

    # Homework
    pc2 = [(["must have", "should have"], "must have"), (["might have", "should have"], "might have"), (["can't have", "must have"], "must have"),
           (["should have", "must have"], "should have"), (["shouldn't have", "can't have"], "shouldn't have"), (["can't have", "mustn't have"], "can't have")]
    p = [ch(o, a) for o, a in pc2]
    rw2 = [("I'm sure the dog ate my sandwich. (must)", "The dog must have eaten my sandwich."),
           ("It wasn't a good idea to leave the door open. (shouldn't)", "You shouldn't have left the door open."),
           ("Maybe she forgot her keys. (might)", "She might have forgotten her keys.")]
    rwl2 = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw2)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Mrs. Lima writes a note for the hostel board. Choose the correct words.", "")}</div>{img('C', 30, 19)}</div>
<div class="box" style="line-height:1.85;font-size:8.8pt;margin:.5mm 0"><b>Dear guests,</b> last Sunday Pipoca ran away. Someone {p[0]} left the gate open. We were very worried: he {p[1]} been hit by a car! But he {p[2]} been very hungry, because the baker says he ate three cheese breads. We {p[3]} checked the gate, so from now on, please close it. And Bruno, you {p[4]} given him chocolate. It's bad for dogs! He {p[5]} liked it much anyway: he left half of it on the floor. Thank you! Mrs. Lima</div>
{sub("B", "Rewrite the sentences with the modal in brackets.", "")}
<ol style="line-height:1.5;font-size:8.7pt;margin:0">{rwl2}</ol>
{lean.watch_out([("I create a dog and two cats.", "I have a dog and two cats.", "<i>create</i> = make something new; for animals: <i>have, raise</i>."), ("I passed my hand on the dog.", "I stroked / petted the dog.", "<i>stroke</i> or <i>pet</i> an animal."), ("My dog is very educated.", "My dog is very well-behaved / well-trained.", "<i>educated</i> = with a good education (people).")])}
{lean.writing_task(sub, "Write a short opinion text: the benefits and drawbacks of having a pet in an apartment.", "In general, I think…", ["two benefits with an example", "one or two drawbacks", "at least four linkers (In addition, However, On the whole…)", "one past modal (must have, should have)", "100–150 words"], "I can talk about the pros and cons of pets, guess what happened and say what someone should have done.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class. In A, the last gap is <i>can't have</i> (the opposite of <i>must have</i>), not <i>mustn't have</i>. Read the writing at home and choose two mistakes to discuss in class.</p>""")

    script = "".join(f"<p style='margin:.5mm 0'>{t}</p>" for t in S511)
    b.extra("Audio script", f"""
{sub("51.1", "Danny's blog: our new roommate has four legs (natural and slow; read by Danny)")}
<p style="font-size:8.4pt">The audio is the text on page 2, read in full.</p>
{sub("51.2", "Repeat: must have, should have")}
<p>{" · ".join(S512)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 51 - Pet benefits")
