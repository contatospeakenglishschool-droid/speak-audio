# Speak! Progress B1 - Unit 04 "People's appearance" (all English) - B1 format (2026-11-09)
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Progress"
setup(band="B1 · UNIT 04", audio_json="audio_b1-unit-04.json", img_dir="img")



_r = json.load(open("roteiro.json"))["units"]["b1-unit-04"]
NUMS = {"twelve-hour": "12-hour"}
def _fix(t):
    for k, v in NUMS.items():
        t = t.replace(k, v)
    return t
S041 = [_fix(x) for x in _r["04.1 Ana calls Danny: a favor at the airport"].split("\n")]
S042 = [x.split(": ", 1)[1] for x in _r["04.2 Repeat: linking sounds"].split("\n")]


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
    cover = cover_html(T, "LEVEL B1 · UNIT 04", "People's appearance", "Describing what people look like · <b>look / look like, be / have, modifiers</b>",
                       [("YOU CAN", "understand and give a detailed, polite description of a person's appearance"),
                        ("LANGUAGE", "What does she look like? · She's in her early forties. · She looks a bit like… · long curly red hair"),
                        ("PRONUNCIATION", "linking sounds in descriptions")])
    cats = [("Hair", "bald · curly · dyed · straight · wavy"), ("Body", "overweight · slim · stocky · well-built"),
            ("Skin", "freckles · pale · tanned · wrinkles"), ("Face", "a beard · clean-shaven · oval · round")]
    if T:
        catrows = "".join(f"<tr><td style='width:16mm'><b>{c}</b></td><td>{R(w)}</td></tr>" for c, w in cats)
    else:
        catrows = "".join(f"<tr><td style='width:16mm'><b>{c}</b></td><td style='height:6mm'></td></tr>" for c, w in cats)
    b.page(f"""{sec(1, "Warm-up: first impressions", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 58, 38)}<div style="flex:1">
{sub("A", "Discuss with your teacher.", "3 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0"><li>How often do you go to a hair salon or a barber? What do you usually ask for?</li><li>Have you ever changed your look completely? What did people say?</li><li>Do first impressions about appearance tell us anything true about a person?</li></ol></div></div>
{sub("B", "Key words. Put the words in the box into the correct categories.", "4 min")}
<div class="bank">a beard · bald · clean-shaven · curly · dyed · freckles · oval · overweight · pale · round · slim · stocky · straight · tanned · wavy · well-built · wrinkles</div>
<table style="font-size:8.8pt;margin-top:1mm">{catrows}</table>
{sub("C", "Describe your own hair and face to your teacher. Use four words from B.", "1 min")}""",
    25, """<ol><li>A: keep it light and personal. Question 3 prepares the talking point on page 7.</li>
<li>B: <i>stocky</i> = short, broad and strong; <i>well-built</i> = big and muscular (positive). <i>Freckles</i> are small brown spots on the skin; <i>wrinkles</i> are lines that come with age. Some words can go in two categories (<i>pale</i> face, <i>round</i> body): accept them if the student can explain.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 60 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Discussion · key words: hair, body, skin, face</td><td>1</td></tr>
<tr><td>2 Listening</td><td>12 min</td><td>Phone call: Ana asks Danny to meet her cousin at the airport</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>8 min</td><td>look / look like, be / have, modifiers, word order</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Describing appearance (study at home)</td><td>4</td></tr>
<tr><td>4 Vocabulary lab + pronunciation</td><td>8 min</td><td>Opposites · say it nicely · changing your appearance · linking</td><td>5</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Danny's message about the hostel · how would you change your look?</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Functional language · long turn: a person in my life · role-play at the airport</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>4 min</td><td>Can-do · language notes · writing homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY</h4>The Linguahouse lesson is vocabulary only, with photos of people to describe. We built an original listening: Ana (a doctor) can't leave a 12-hour hospital shift, so she calls Danny and asks him to meet her cousin Carol (Orlando) at Guarulhos airport. Carol is in her early forties, tall, slim and well-built, with an oval face, brown eyes, new shoulder-length curly red hair (it used to be long, straight and dark), a tan and big round glasses. In the Practice, Danny describes Bruno (his roommate) and Mrs. Lima (the hostel owner) to his mom, Rita (B1 Unit 02). In the writing model, Ana describes Danny to Carol.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students say <i>She has forty years</i>, use <i>hairs</i> for the hair on the head, say <i>He is with a beard</i> and <i>She looks like tired</i>, confuse <i>What does she look like?</i> with <i>What's she like?</i>, and look for a single word for <i>moreno</i>. Words like <i>fat</i>, <i>skinny</i> and <i>old</i> can sound rude.</div>
<div class="box"><h4>AUDIO</h4>Track 04.1 Ana calls Danny: a favor at the airport (natural and slow) · Track 04.2 Repeat: linking sounds</div>""")

    # Page 2 - Listening
    gist = ["to invite Danny to dinner", "to ask Danny to meet her cousin at the airport", "to ask Danny for a taxi number"]
    pp = [("a", "A woman in her twenties, with short curly red hair, pale skin and glasses.", False),
          ("b", "A woman in her forties, with long straight dark hair, a tan and glasses.", False),
          ("c", "A woman in her forties, with shoulder-length curly red hair, a tan and big round glasses.", True),
          ("d", "A slim woman in her sixties, with short wavy gray hair and no glasses.", False)]
    ppl = "".join(f'<div class="msg" style="max-width:none;flex:1;padding:1.2mm 2mm;font-size:8.3pt{";border:1.5pt solid #c0392b" if (T and ok) else ""}"><b>{l}</b> {d}</div>' for l, d, ok in pp)
    det = [("Where is Carol flying from?", "Orlando"), ("Why can't Ana go to the airport?", "She has a 12-hour hospital shift."),
           ("How tall is Carol?", "Fairly tall, about Ana's height."), ("Why is she well-built?", "She goes to the gym every day."),
           ("What did her hair use to look like?", "Long, straight and dark."), ("Why is she tanned?", "She lives in Florida and goes to the beach every weekend."),
           ("Why might she look tired?", "It's an overnight flight and she never sleeps on planes."), ("How will Carol recognize Danny?", "Ana will send her his photo; he'll hold a sign.")]
    detl = [f'<li value="{i+1}">{q} {A(a, "min-width:24mm")}</li>' for i, (q, a) in enumerate(det)]
    b.page(f"""{sec(2, "Listening: a favor at the airport", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{audiocard(["04.1 · NATURAL", "04.1 · SLOW"])}
{sub("A", "Listen at natural speed. Why does Ana call Danny? Choose.", "2 min", "04.1")}
<p style="margin:.3mm 0;font-size:8.9pt">{ch(gist, gist[1])}</p></div>{img('B', 46, 31)}</div>
{sub("B", "Listen again. Which woman is Carol? Choose a, b, c or d.", "2 min")}
<div style="display:flex;gap:2mm">{ppl}</div>
{sub("C", "Answer the questions. Use the slow version if you need it.", "4 min")}
<div style="font-size:8.5pt">{twocol(detl, 4)}</div>
{sub("D", "Think about it. Discuss with your teacher.", "4 min")}
<ol style="line-height:1.4;font-size:8.8pt;margin:0"><li>Ana says, "That's the tricky part." Why is Carol's hair a problem? {R("Danny may expect long dark hair like Ana's (or an old photo), but Carol's hair is now red, curly and shorter.") if T else ""}</li>
<li>Ana describes Carol's body as "slim, but quite well-built". Why do you think she chooses her words carefully? {R("Personal: to sound polite and positive about her cousin.") if T else ""}</li></ol>
<div class="box sand" style="margin-top:1mm"><h4>NOTICE: USEFUL CHUNKS</h4><i>I need a big favor. · She's flying in from… · Let me think. · That's the tricky part. · Got it. · Don't be surprised if… · You're a lifesaver!</i></div>""",
    25, """<ol><li>A: play the natural version once with books closed except for A. The slow version is support for C, not the first listening.</li>
<li>B: each wrong option has one or two details from the call (red curls, a tan, glasses, her old hair) so the student must listen for the whole picture. <i>A lifesaver</i> = a person who helps you in a difficult moment.</li></ol>""")

    # Page 3 - Language focus
    qa = [("What does she look like?", "She's tall, with red curly hair.", "appearance"), ("What's she like?", "She's friendly and very funny.", "personality"),
          ("How is she?", "She's fine, but a little tired.", "health / mood"), ("What does she like?", "She likes the gym and the beach.", "interests")]
    ans = ["She likes the gym and the beach.", "She's fine, but a little tired.", "She's tall, with red curly hair.", "She's friendly and very funny."]
    qal = "".join(f"<li>{q} {A(chr(97 + ans.index(a)) + ' ' + ('(' + w + ')' if T else ''), 'min-width:8mm')}</li>" for q, a, w in qa)
    ansl = " &nbsp; ".join(f"<b>{chr(97+i)}</b> {a}" for i, a in enumerate(ans))
    cs = [(["She's in her early forties.", "She has forty years."], "She's in her early forties."),
          (["She looks a bit like a college professor.", "She looks a bit a college professor."], "She looks a bit like a college professor."),
          (["She has an oval face.", "She is with an oval face."], "She has an oval face."),
          (["She looks a little tired.", "She looks like a little tired."], "She looks a little tired."),
          (["She's dyed her hair red.", "She's dyed her hairs red."], "She's dyed her hair red.")]
    csl = "".join(f"<li>{ch(o, a)}</li>" for o, a in cs)
    wo = [("curly / shoulder-length / red", "shoulder-length curly red"), ("dark / straight / long", "long straight dark"), ("gray / wavy / short", "short wavy gray")]
    wol = "".join(f"<li>({w}) {A(a, 'min-width:34mm')} hair</li>" for w, a in wo)
    b.page(f"""{sec(3, "Language focus: describing appearance", "8 min")}
{sub("A", "Match the questions 1–4 to the answers a–d.", "2 min")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.6">{ansl}</p>
<ol style="line-height:1.6;font-size:8.9pt;margin:0;column-count:2">{qal}</ol>
{sub("B", "Which sentence from the call is correct? Choose.", "3 min")}
<ol style="line-height:1.6;font-size:8.9pt;margin:0">{csl}</ol>
{sub("C", "Word order. Write the words in the correct order.", "3 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0">{wol}</ol>
<div class="box sand"><h4>RULE</h4><b>be</b> + age, height, build (<i>She's tall. He's in his thirties.</i>) · <b>have</b> + hair, eyes, a beard (<i>She has curly hair.</i>) · <b>look</b> + adjective (<i>She looks tired.</i>) · <b>look like</b> + noun (<i>She looks like a professor.</i>) · <i>a bit, a little</i> + negative ideas; <i>quite, fairly, pretty</i> = medium · hair: <b>length → style → color</b>. More on the next page: <b>Grammar reference</b>.</div>""",
    24, """<ol><li>A: this is a classic confusion. Ask the four questions about someone the student knows well.</li>
<li>B: all the correct sentences are from the call. Play 04.1 again if the student wants to check.</li></ol>""")

    grammar_ref.describing_appearance(b)

    # Page 5 - Vocabulary lab
    op = [("dark hair", "fair / blond"), ("broad shoulders", "narrow"), ("pale skin", "tanned / dark"), ("full lips", "thin"), ("curly hair", "straight"), ("a slim build", "a muscular / stocky")]
    opl = " &nbsp;·&nbsp; ".join(f"{a} ↔ {A(o, 'min-width:16mm')}" for a, o in op)
    ni = [("fat", "a bit overweight"), ("skinny", "slim"), ("old", "elderly / older"), ("short and fat (a man)", "stocky"), ("ugly", "not very attractive")]
    nil = " &nbsp;·&nbsp; ".join(f"{a} → {A(p, 'min-width:20mm')}" for a, p in ni)
    cg = [("She's", "dyed", "her hair blond."), ("He's growing", "a beard", "to look older."), ("I've", "put on", "five kilos since Christmas."),
          ("You look great! Have you", "lost", "weight?"), ("He", "shaved off", "his mustache last week."), ("I need to", "get", "a haircut.")]
    cgl = [f'<li value="{i+1}">{a} {A(v, "min-width:15mm")} {e}</li>' for i, (a, v, e) in enumerate(cg)]
    b.page(f"""{sec(4, "Vocabulary lab: describing people", "4 min")}
{sub("A", "Opposites. Write the opposite.", "1 min")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.8">{opl}</p>
{sub("B", "Say it nicely. Write a more polite word from the box.", "1 min")}
<div class="bank">a bit overweight · elderly / older · not very attractive · slim · stocky</div>
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.8">{nil}</p>
{sub("C", "Changing your appearance. Complete with the words in the box.", "2 min")}
<div class="bank">a beard · dyed · get · lost · put on · shaved off</div>
<div style="font-size:8.6pt">{twocol(cgl, 3)}</div>
<div class="box sand"><h4>WATCH OUT: WORD CHOICE</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>He's moreno.</td><td><b>He has dark hair. / He's tanned. / He has brown skin.</b></td><td>English needs to say if it's the hair, a tan or the skin.</td></tr>
<tr><td>She's very thin. (as a compliment)</td><td><b>She's slim.</b></td><td><i>slim</i> is positive; <i>thin</i> and <i>skinny</i> can sound negative.</td></tr>
<tr><td>She has a fringe.</td><td><b>She has bangs.</b></td><td><i>fringe</i> is British English.</td></tr>
</table></div>
{sec(5, "Pronunciation lab: linking sounds", "4 min")}
<p class="small" style="margin:.3mm 0">When a word ends in a consonant and the next word starts with a vowel, we say them together: <i>She's_got_an_oval face</i> · <i>He's_in_his forties</i> · <i>What does she look_like?</i></p>
{audiocard(["04.2"])}
{sub("A", "Listen and repeat. Then describe a person in your family in three sentences.", "4 min", "04.2")}
<p style="margin:.3mm 0;font-size:8.8pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S042))}</p>""",
    24, """<ol><li>B: politeness matters in American English; comments about weight, age or attractiveness are usually avoided, especially at work. <i>Elderly</i> is polite for very old people; <i>older</i> is softer.</li>
<li>Pronunciation: students often add a vowel (<i>She's-i got-i an</i>) or stop between words. Model the chunks slowly, then at natural speed.</li></ol>""")

    # Page 6 - Practice
    pr = [(["in his mid-twenties", "with twenty-five years"], "in his mid-twenties"), (["quite", "a bit"], "quite"), (["short curly black", "black short curly"], "short curly black"),
          (["looks", "looks like"], "looks like"), (["a little", "extremely"], "a little"), (["has", "is with"], "has"), (["wears", "uses"], "wears"),
          (["looks", "looks like"], "looks"), (["put on", "lost"], "put on")]
    p = [ch(o, a) for o, a in pr]
    sit = ["You have an important job interview tomorrow.", "You are an actor and you have to play a person ten years older.",
           "You are going to a friend's wedding on the beach.", "You want a completely new look for the new year."]
    b.page(f"""{sec(6, "Practice", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Danny writes to his mom about the people at his hostel. Choose the correct words.", "5 min")}</div>{img('C', 30, 20)}</div>
<div class="box" style="line-height:1.9;font-size:9pt">Hi Mom! You asked about the people here, so here goes. My roommate Bruno is {p[0]}. He's {p[1]} tall and well-built, and he has {p[2]} hair. He's growing a beard at the moment, and honestly, he {p[3]} a pirate! He's {p[4]} messy, but he's a great guy. Mrs. Lima, the owner, is in her sixties. She's short and slim and she {p[5]} gray hair, and she always {p[6]} glasses. She {p[7]} strict, but she's really kind. And me? I think I've {p[8]} a few kilos – the cheese bread here is amazing! Love, Danny</div>
{sub("B", "How would you change your appearance in these situations? Write a sentence with I'd… Then tell your teacher.", "3 min")}
<ol style="line-height:1.35;font-size:8.9pt;margin:0">{"".join(f"<li>{t}<div class='wline'></div></li>" for t in sit)}</ol>""",
    22, """<ol><li>A: ask the student to justify each choice with a rule from page 3 or 4 (<i>look like</i> + noun, <i>look</i> + adjective; <i>a little</i> with a negative idea).</li>
<li>B: encourage <i>I'd</i> + infinitive: <i>I'd get a haircut and shave. I'd dye my hair gray.</i> Ask follow-up questions: <i>Have you ever done that?</i></li></ol>""")

    # Page 7 - Speaking
    b.page(f"""{sec(7, "Speaking: describing people", "12 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>approximate</th><th>compare</th><th>be polite</th><th>check and identify</th></tr>
<tr><td><i>I'd say she's in her fifties. · He's about 1.80 m. · tallish · thirtyish</i></td><td><i>She looks a bit like… · He reminds me of… · She's taller than…</i></td><td><i>He's a bit overweight. · She isn't very tall. · He's quite slim.</i></td><td><i>Is that the man with…? · Which one? The one in the blue jacket?</i></td></tr></table></div>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("A", "Long turn. Prepare for one minute, then talk for two minutes about an important person in your life.", "5 min")}
<ul style="line-height:1.45;font-size:8.9pt;margin:0"><li>what he or she looks like now</li><li>what he or she used to look like</li><li>who he or she looks like in the family</li><li>what he or she is like (personality)</li></ul></div>{img('D', 32, 24)}</div>
{sub("B", "Role-play: at the airport. You have to meet your teacher's relative at the airport. Call your teacher, ask questions and take notes. Then change roles: describe a person you know.", "4 min")}
<div style="display:flex;gap:5mm;font-size:8.6pt"><div style="flex:1"><b>Notes:</b>{lines(2)}</div><div style="flex:1">{R("Teacher's card: Uncle Jorge, in his late fifties, short and stocky, bald, a gray mustache, small glasses, a red soccer shirt, a big black suitcase.") if T else ""}</div></div>
{sub("C", "Talking point. Discuss with your teacher.", "3 min")}
<ol style="line-height:1.5;font-size:8.9pt;margin:0"><li>How does your appearance influence what people think of you, for example at a job interview?</li><li>Is there too much pressure on people to look good today? What about photo filters on social media?</li></ol>""",
    28, """<ol><li>A: don't interrupt; note mistakes for the error log (page 8), especially <i>has… years</i>, <i>hairs</i> and <i>look like</i> + adjective. Fluency option (3-2-1): the same talk in 2 minutes, then in 1 minute.</li>
<li>B: use the card in red; answer only what the student asks, so they need questions like <i>How old is he? Has he got…? What's he wearing?</i></li></ol>""")

    # Page 8 - Wrap-up
    pc = ["I can understand a detailed description of a person in a phone call.", "I can use <i>look / look like</i>, <i>be / have</i> and modifiers correctly.",
          "I can describe a person's appearance politely and in detail."]
    pcr = "".join(f"<tr><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for s in pc)
    b.page(f"""{sec(8, "Wrap-up and homework", "4 min")}
{sub("A", "Can-do check", "1 min")}
<table class="ck" style="font-size:8.6pt"><tr><th>In English…</th><th style="width:16mm">Easy!</th><th style="width:16mm">Sometimes</th><th style="width:16mm">Not yet</th></tr>{pcr}</table>
{sub("B", "My language notes. Write three corrections from today's class.", "2 min")}
<div style="display:flex;gap:5mm;font-size:8.6pt"><div style="flex:1"><b>I said…</b>{lines(3)}</div><div style="flex:1"><b>Better:</b>{lines(3)}</div></div>
{sub("C", "Homework: writing (100–150 words)", "1 min")}
<p style="margin:.3mm 0"><b>Meet my friend.</b> A friend is going to meet someone you know at the airport. Write a message and describe the person. Read Ana's message to Carol first.</p>
<div class="box" style="font-size:8.6pt;line-height:1.4;margin:.5mm 0"><i>Hi Carol! I'm so sorry I can't meet you, but my friend Danny is going to pick you up. He's American, from Chicago, and he's in his early twenties. He's very tall – about 1.90 m – and quite thin, with short wavy blond hair and a lot of freckles. At the moment he's trying to grow a beard, but it isn't very successful! He usually wears jeans, sneakers and a baseball cap, so he looks like a typical tourist. He'll be at the arrivals exit with a sign with your name on it. He's really friendly and funny, so you'll have a great time in the taxi. See you tomorrow night! Love, Ana</i></div>
<p class="small" style="margin:.3mm 0">Checklist: ☐ age and height &nbsp;☐ hair (length → style → color) &nbsp;☐ face, skin or glasses &nbsp;☐ <i>looks / looks like</i> &nbsp;☐ one modifier (<i>quite, a bit</i>) &nbsp;☐ 100–150 words</p>
{lines(7)}""",
    30, """<ol><li>B (error log): during the lesson, note 3–5 real mistakes. Here, the student writes what they said and the better version; guide them to self-correct first.</li>
<li>C: when you correct, check the word order of the hair adjectives and that weight and age are described politely.</li></ol>""")

    script = "".join(f"<p style='margin:.6mm 0'><b>{l.split(': ', 1)[0]}:</b> {l.split(': ', 1)[1]}</p>" for l in S041)
    b.extra("Audio script", f"""
{sub("04.1", "Ana calls Danny: a favor at the airport (natural and slow)")}
<div style="line-height:1.35;font-size:8.8pt">{script}</div>
{sub("04.2", "Repeat: linking sounds")}
<p>{" · ".join(S042)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 04 - People's appearance")
