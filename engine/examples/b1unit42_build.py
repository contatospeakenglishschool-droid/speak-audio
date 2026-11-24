# Speak! Progress B1 - Unit 42 "Common expressions" (all English) - lean B1 format
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
setup(band="B1 · UNIT 42", audio_json="audio_b1-unit-42.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-42"]
S421 = [l.split(": ", 1) for l in _r["42.1 Gap Year Diaries: what do you say when...?"].split("\n")]
_l2 = [l.split(": ", 1)[1] for l in _r["42.2 Listen and respond: social expressions"].split("\n")]
S422 = list(zip(_l2[0::2], _l2[1::2]))  # (prompt, response)


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
    cover = cover_html(T, "LEVEL B1 · UNIT 42", "Common expressions", "Saying the right thing · <b>Bless you! · What a week! · How kind of you!</b>",
                       [("YOU CAN", "use common social expressions and react to good and bad news"),
                        ("LANGUAGE", "Good luck · Same to you · Help yourself · Never mind · What a…! · How…! · so / such"),
                        ("PRONUNCIATION", "exclamations: start high and fall")])
    kw = [("I have an important exam tomorrow.", "Good luck!"), ("Achoo!", "Bless you!"),
          ("Cheers!", "Cheers!"), ("I'm going to drive home now, but I'm really tired.", "Be careful!"),
          ("Sorry, we don't have time to stop at the market.", "Never mind."), ("Can I take another chocolate?", "Help yourself."),
          ("Have a good weekend!", "Same to you!"), ("Could you pass me the salt, please?", "Here you are."),
          ("My uncle died yesterday.", "I'm so sorry for your loss."), ("I passed my driving test!", "Congratulations!")]
    kwl = "".join(f'<li>{s} {A(r, "min-width:28mm")}</li>' for s, r in kw)
    bank = sorted({r.rstrip("!.") for s, r in kw})
    b.page(f"""{sec(1, "Warm-up: what do you say?", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 50, 33)}<div style="flex:1">
{talk(["When do people raise a glass and say something? What do they say in your country?", "Is it easy to know what to say at a wedding, a party or a funeral?", "Which polite expressions do you use every day?"], "START TALKING")}</div></div>
{sub("A", "Respond to each sentence with an expression from the box.", "4 min")}
<div class="bank" style="font-size:8.6pt">{" · ".join(bank)}</div>
<ol style="font-size:8.6pt;line-height:1.6;margin:0;columns:2;column-gap:6mm">{kwl}</ol>
{talk(["When did you last say <i>Congratulations</i>? Who to, and why?", "Who says <i>Help yourself</i> in your home? When?", "What do you say when someone sneezes? Is there a different answer in English?"], "USE THE EXPRESSIONS")}""",
    34, """<ol><li>Top box: 3 minutes.</li>
<li>A: the student says the answers out loud first, then writes. The Linguahouse lesson uses <i>My condolences</i>; in spoken American English <i>I'm so sorry for your loss</i> (or just <i>I'm so sorry</i>) is more common. <i>My condolences</i> is more formal and frequent in cards and messages. <i>Same to you</i> answers a wish (<i>Have a good weekend! Happy New Year!</i>), never <i>Good luck</i> before your own exam: then say <i>Thanks!</i></li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Gap Year Diaries: Danny tells Bruno about his week of good news and social mistakes · what did Danny say? · questions · Talk about it",
                      "exclamations: What (a / an)…! · How…! · so / such (a)…! · ready-made reactions", "Complete with what, what a, how, so, such · react in writing · Use it (oral)",
                      "listen and respond: social expressions (42.2) · react to the teacher's news · long turn: a week of ups and downs", "Danny's message to his mom · rewrite as exclamations · watch out · writing"),
        """The Linguahouse lesson is a short practice of ten social expressions (Good luck, Bless you, Cheers, Be careful, Never mind, Help yourself, Same to you, Here you are, My condolences, Congratulations) with two sets of sentences to respond to. It has no listening text and no grammar, so we added an episode of Danny's podcast, Gap Year Diaries, and a new B1 grammar point: exclamations (What a…! How…! so / such). Basic <i>What a + adjective + noun</i> appeared in A2 compliments; this unit covers the whole system. Story: Danny got the job at the language school (interview on Thursday, phone call on Friday morning). His mistakes: he answered Mrs. Lima's <i>Good luck!</i> with <i>Same to you!</i>; said nothing when the director sneezed; took five cookies after <i>Help yourself</i>. He celebrated with Ana on Friday (she paid while he was in the restroom). On Saturday Rafa's grandfather died, so they didn't go to the beach. On Monday Bruno drives Danny to his first day at work (Bruno's dad is the terrible driver, Unit 34). No real-world facts are given.""",
        """<i>What a terrible weather / What a good news</i> (uncountable nouns); <i>How beautiful day!</i> for <i>What a beautiful day!</i>; <i>so a nice…</i> for <i>such a nice…</i>; a literal translation of the Brazilian reply to a sneeze instead of <i>Bless you</i>; <i>Congratulations</i> on a birthday (<i>Happy birthday!</i>); <i>Same for you</i>. Pronunciation: exclamations start high and fall; <i>Congratulations</i> has its stress on <i>-LA-</i>.""",
        "Track 42.1 Gap Year Diaries: what do you say when…? (natural and slow; Danny and Bruno) · Track 42.2 Listen and respond: social expressions (pauses to answer)"))

    # Page 2 - Listening
    mo = [("Mrs. Lima says <i>Good luck!</i>", "Same to you!", "Thanks!"),
          ("The director sneezes.", "nothing", "Bless you!"),
          ("The director says <i>Help yourself.</i>", "takes five cookies", "takes one or two"),
          ("Rafa's grandfather died.", "(thinks of) My condolences", "I'm so sorry for your loss."),
          ("Rafa says sorry about the beach trip.", "Never mind! We can go another time.", "the same: perfect!")]
    mt = "".join(f'<tr><td>{s}</td><td>{A(d, "min-width:30mm")}</td><td>{A(r, "min-width:30mm")}</td></tr>' for s, d, r in mo)
    qs = [("How did the interview end?", "She laughed, they talked for an hour, and the school called him on Friday morning: he got the job."),
          ("What did Ana and Danny do on Friday night?", "They had dinner to celebrate. Ana said Cheers. Ana paid when Danny went to the restroom."),
          ("Why didn't Danny and Rafa go to the beach?", "Rafa's grandfather died."),
          ("Why will Danny say <i>Be careful!</i> on Monday?", "Bruno is driving him to work and Danny says he's a terrible driver.")]
    ql = "".join(f"<li>{q} {A(a, 'min-width:50mm')}</li>" for q, a in qs)
    b.page(f"""{sec(2, "Listening: Gap Year Diaries", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Listen to Danny's podcast. What did Danny say or do? What is the right response?", "5 min")}
<table style="font-size:8.4pt;margin:.5mm 0"><tr><th>situation</th><th>Danny said / did</th><th>the right response</th></tr>{mt}</table></div>{img('B', 34, 30)}</div>
{audiocard(["42.1 · NATURAL", "42.1 · SLOW"])}
{sub("B", "Listen again and answer.", "3 min")}
<ol style="line-height:1.5;font-size:8.6pt;margin:0">{ql}</ol>
<p style="margin:.6mm 0;font-size:8.6pt"><b>Think about it:</b> Danny says he "froze" when the director sneezed. Why do people freeze in a foreign language, even when they know the words? {A("open answer: stress, no time to think, new rules", "min-width:20mm")}</p>
{talk(["Have you ever said the wrong thing at the wrong moment? What happened?", "Which of Danny's mistakes could happen to you in English?", "When someone says <i>Help yourself</i>, how much do you take?"])}""",
    30, """<ol><li>A: play the natural version; play the slow one if needed. Row 5 is the one thing Danny gets right.</li>
<li>B: accept short answers. Ask the student to repeat Bruno's reactions: <i>What a week! How embarrassing! What a relief! How rude!</i> They come back on page 3.</li>
<li>Talk about it: 4 minutes. Danny's podcast <i>Gap Year Diaries</i> appeared in earlier units.</li></ol>""")

    # Page 3
    lean.grammar_in_class(b, grammar_ref.exclamations)

    # Page 4 - Practice
    comp = [("I got the job!", "That's", "such", "great news!"),
            ("My flight was canceled.", "Oh no!", "What a", "shame!"),
            ("I brought you some flowers.", "", "How", "kind of you!"),
            ("It's raining again.", "", "What", "awful weather!"),
            ("I passed my driving test.", "You must be", "so", "happy!"),
            ("My new neighbors invited me to dinner.", "They're", "such", "nice people!"),
            ("I answered <i>Good luck</i> with <i>Same to you</i>.", "", "How", "embarrassing!"),
            ("I found my wallet in the car!", "", "What a", "relief!")]
    cl = "".join(f'<li><i>"{q}"</i> → {a} {A(m, "min-width:14mm")} {z}</li>' for q, a, m, z in comp)
    rw = [("My sister had a baby last night!", "Congratulations! What wonderful news! / How exciting!"),
          ("I can't come to your party. I have to work.", "Never mind. / What a shame! Maybe next time."),
          ("I have my final exam tomorrow.", "Good luck! You're so well prepared.")]
    rwl = "".join(f'<li><i>"{d}"</i><br>{R("Possible: " + i) if T else lines(1)}</li>' for d, i in rw)
    use = ["Your best friend is getting married in Paris.", "Your teacher forgot your class today.", "It's 40 °C (104 °F) today.",
           "Your neighbor plays the drums at 2 a.m.", "You find R$100 in an old jacket.", "Your friend's cat is sick."]
    b.page(f"""{sec(4, "Practice: how do you react?", "10 min")}
{sub("A", "Complete the reactions with what, what a, how, so or such.", "4 min")}
<ol style="line-height:1.75;font-size:8.7pt;margin:0">{cl}</ol>
{sub("B", "Write a reaction: a social expression + an exclamation.", "3 min")}
<ol style="line-height:1.45;font-size:8.7pt;margin:0">{rwl}</ol>
{talk(use, "USE IT: REACT OUT LOUD WITH AN EXCLAMATION")}""",
    32, """<ol><li>A: 4 minutes. Check with the test: a noun after the gap → <i>what (a)</i> or <i>such (a)</i>; an adjective alone → <i>how</i> or <i>so</i>. Items 1 and 4: <i>news</i> and <i>weather</i> are uncountable.</li>
<li>B: accept any natural combination.</li>
<li>Use it: 3 minutes, all oral. Read each situation as your own news (<i>My best friend is getting married in Paris!</i>); the student reacts and asks a follow-up question.</li></ol>""")

    # Page 5 - Speaking
    pr = "".join(f'<li>{p} {A(r, "min-width:26mm")}</li>' for p, r in S422)
    card = f"""<div class="box" style="margin-top:1mm;font-size:8.2pt">{R("<b>Teacher's card (B):</b> say each piece of news with feeling: I'm moving to Australia next month. · My car was stolen last night. · I met my favorite singer at the airport. · I locked my keys in the car. · My son got into medical school. · I lost my phone, but a stranger returned it. After each reaction, ask a follow-up question or wait for one.")}</div>""" if T else ""
    b.page(f"""{sec(5, "Speaking: reacting to news", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.2pt"><tr><th>good news</th><th>bad news</th><th>a surprise</th><th>a small problem</th></tr>
<tr><td><i>Congratulations! · Good for you! · That's such great news!</i></td><td><i>I'm so sorry to hear that. · That's awful. · Is there anything I can do?</i></td><td><i>Really? · No way! · You're kidding! · What a coincidence!</i></td><td><i>Never mind. · Don't worry about it. · What a shame!</i></td></tr></table></div>
{audiocard(["42.2"])}
{sub("A", "Listen. Respond in the pause, then listen to the answer and repeat it with the same intonation.", "5 min", "42.2")}
<ol style="font-size:8.4pt;line-height:1.5;margin:0;columns:2;column-gap:6mm">{pr}</ol>
{sub("B", "Your teacher tells you some news. React with an expression or an exclamation and ask a question.", "5 min")}{card}
{sub("C", "Long turn. Tell your teacher about a week with ups and downs (real or invented): two good things and two bad things. Your teacher reacts. Then swap.", "6 min")}
<p style="margin:.3mm 0;font-size:8.5pt">Plan (1 min): {lines(1)}</p>
{talk(["Which expression from this unit would you like to use this week? When?"], "TALK ABOUT IT")}""",
    30, """<ol><li>A: pause the audio if the student needs more time. Model the fall in <i>Congratulations!</i> and <i>Bless you!</i></li>
<li>B is the Linguahouse practice, adapted for 1:1. C: 1 minute to plan, 2 minutes to talk, then you tell your week and the student reacts. Last 3 minutes: wrap-up (two corrections, and ask <i>Can you now react to good and bad news?</i>).</li></ol>""")

    # Homework
    pc = [(["What a", "What"], "What a"), (["so", "such"], "so"), (["How", "What"], "How"), (["such a", "so"], "such a"),
          (["Thanks", "Same to you"], "Thanks"), (["What", "What a"], "What")]
    p = [ch(o, a) for o, a in pc]
    rw2 = [("The weather is terrible. (What)", "What terrible weather!"),
           ("You are very kind. (How … of you)", "How kind of you!"),
           ("It was a very long day. (such)", "It was such a long day!")]
    rwl2 = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw2)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Danny writes to his mom on Sunday night. Choose the correct words.", "")}</div>{img('C', 30, 19)}</div>
<div class="box" style="line-height:1.85;font-size:8.8pt;margin:.5mm 0"><b>Hi Mom!</b> {p[0]} week! I got the job at the language school! I was {p[1]} nervous at the interview, and I took five cookies when the director said "Help yourself". {p[2]} embarrassing! But she's {p[3]} nice person, and she just laughed. When Mrs. Lima said "Good luck", I answered "Same to you". Next time I'll just say {p[4]}! Rafa's grandfather died on Saturday, so we didn't go to the beach. I start on Monday. {p[5]} good news, right? Love, Danny</div>
{sub("B", "Rewrite the sentences as exclamations with the words in brackets.", "")}
<ol style="line-height:1.5;font-size:8.7pt;margin:0">{rwl2}</ol>
{lean.watch_out([("Congratulations! (on someone's birthday)", "Happy birthday!", "<i>Congratulations</i> is for something you did: a new job, an exam, a wedding."), ("Same for you!", "Same to you!", "the preposition is <i>to</i>."), ("How beautiful day!", "What a beautiful day!", "a noun after the adjective → <i>what a</i>.")])}
{lean.writing_task(sub, "A friend sent you a message with three pieces of news: a new job, a sick cat and a trip to Japan next month. Write a reply. React to each piece of news and ask questions.", "Hi …! Thanks for your message. What a month!", ["a reaction to each piece of news", "What (a)…! · How…! · so / such", "two social expressions from page 1", "two questions", "100–150 words"], "I can use common social expressions and react to good and bad news.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class. In A, <i>such a nice person</i>: a singular noun after the adjective. Read the writing at home and choose two mistakes to discuss in class.</p>""")

    script = "".join(f"<p style='margin:.5mm 0'><b>{s}:</b> {t}</p>" for s, t in S421)
    b.extra("Audio script", f"""
{sub("42.1", "Gap Year Diaries: what do you say when…? (natural and slow; Danny and Bruno)")}
<div style="line-height:1.3;font-size:8.3pt">{script}</div>
{sub("42.2", "Listen and respond: social expressions (a 3-second pause after each line)")}
<p style="font-size:8.4pt">{" · ".join(f"<i>{p}</i> → <b>{r}</b>" for p, r in S422)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 42 - Common expressions")
