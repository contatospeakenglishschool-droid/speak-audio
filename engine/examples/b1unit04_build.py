# Speak! Progress B1 - Unit 04 "People's appearance" (all English) - lean B1 format (rebuilt 2026-11-19)
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Progress"
import lean
from lean import talk
setup(band="B1 · UNIT 04", audio_json="audio_b1-unit-04.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-04"]
S041 = [x.replace("twelve-hour", "12-hour") for x in _r["04.1 Ana calls Danny: a favor at the airport"].split("\n")]
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

    # 1 Warm-up
    cover = cover_html(T, "LEVEL B1 · UNIT 04", "People's appearance", "Describing what people look like · <b>look / look like, be / have, modifiers</b>",
                       [("YOU CAN", "understand and give a detailed, polite description of a person's appearance"),
                        ("LANGUAGE", "What does she look like? · She's in her early forties. · She looks a bit like… · long curly red hair"),
                        ("PRONUNCIATION", "linking sounds in descriptions")])
    cats = [("Hair", "bald · curly · straight · wavy"), ("Body", "slim · stocky · well-built"), ("Skin and face", "a beard · freckles · tanned · wrinkles")]
    catrows = "".join(f"<tr><td style='width:22mm'><b>{c}</b></td><td style='height:6mm'>{R(w) if T else ''}</td></tr>" for c, w in cats)
    b.page(f"""{sec(1, "Warm-up: first impressions", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["How often do you go to a hair salon or a barber? What do you ask for?", "Have you ever changed your look completely? What did people say?", "Do first impressions tell us anything true about a person?"], "START TALKING")}</div></div>
{sub("A", "Key words. Put the words in the box into the correct categories.", "3 min")}
<div class="bank">a beard · bald · curly · freckles · slim · stocky · straight · tanned · wavy · well-built · wrinkles</div>
<table style="font-size:8.8pt;margin-top:1mm">{catrows}</table>
{talk(["Describe your own hair and face with three words from A.", "Describe a famous person without saying the name. Can your teacher guess?"], "USE THE WORDS")}""",
    26, """<ol><li>Top box: keep it light and personal (4 minutes).</li>
<li>A: <i>stocky</i> = short, broad and strong; <i>well-built</i> = big and muscular (positive). <i>Freckles</i> are small brown spots; <i>wrinkles</i> are lines that come with age.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Phone call: Ana asks Danny to meet her cousin · which woman is Carol? · Talk about it", "Describing appearance: look / look like, be / have, modifiers, word order",
                      "Questions about people · correct sentences · Use it (oral)", "Functional language · linking (04.2) · role-play at the airport",
                      "Danny's message about the hostel · hair word order · word choice · writing"),
        "The Linguahouse lesson is vocabulary only. Our listening: Ana (a doctor) can't leave a 12-hour hospital shift, so she calls Danny and asks him to meet her cousin Carol (Orlando) at Guarulhos airport. Carol is in her early forties, tall, slim and well-built, with an oval face, brown eyes, new shoulder-length curly red hair (it used to be long, straight and dark), a tan and big round glasses. In the homework, Danny describes Bruno and Mrs. Lima to his mom, Rita (B1 Unit 02).",
        "Students say <i>She has forty years</i>, use <i>hairs</i> for the hair on the head, say <i>He is with a beard</i> and <i>She looks like tired</i>, confuse <i>What does she look like?</i> with <i>What's she like?</i>, and look for a single word for <i>moreno</i>. Words like <i>fat</i>, <i>skinny</i> and <i>old</i> can sound rude.",
        "Track 04.1 Ana calls Danny: a favor at the airport (natural and slow) · Track 04.2 Repeat: linking sounds"))

    # 2 Listening
    gist = ["to invite Danny to dinner", "to ask Danny to meet her cousin at the airport", "to ask Danny for a taxi number"]
    pp = [("a", "A woman in her twenties, with short curly red hair, pale skin and glasses.", False),
          ("b", "A woman in her forties, with long straight dark hair, a tan and glasses.", False),
          ("c", "A woman in her forties, with shoulder-length curly red hair, a tan and big round glasses.", True),
          ("d", "A slim woman in her sixties, with short wavy gray hair and no glasses.", False)]
    ppl = "".join(f'<div class="msg" style="max-width:none;flex:1;padding:1.2mm 2mm;font-size:8.3pt{";border:1.5pt solid #c0392b" if (T and ok) else ""}"><b>{l}</b> {d}</div>' for l, d, ok in pp)
    b.page(f"""{sec(2, "Listening: a favor at the airport", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{audiocard(["04.1 · NATURAL", "04.1 · SLOW"])}
{sub("A", "Listen at natural speed. Why does Ana call Danny? Choose.", "2 min", "04.1")}
<p style="margin:.3mm 0;font-size:8.9pt">{ch(gist, gist[1])}</p></div>{img('B', 46, 31)}</div>
{sub("B", "Listen again. Which woman is Carol? Choose a, b, c or d.", "3 min")}
<div style="display:flex;gap:2mm">{ppl}</div>
{talk(["Ana says, &ldquo;That's the tricky part.&rdquo; Why is Carol's hair a problem?", "Ana says Carol is &ldquo;slim, but quite well-built&rdquo;. Why does she choose her words carefully?", "Have you ever met a stranger at an airport or a station? How did you find them?"])}""",
    26, """<ol><li>A–B: 6 minutes. Each wrong option in B has one or two details from the call, so the student must listen for the whole picture.</li>
<li>Talk about it: 6 minutes. 1: Danny may expect long dark hair; Carol's hair is now red, curly and shorter. 2: to sound polite and positive about her cousin.</li></ol>""")

    # 3 Grammar reference
    lean.grammar_in_class(b, grammar_ref.describing_appearance)

    # 4 Practice
    qa = [("What does she look like?", "c (appearance)"), ("What's she like?", "d (personality)"), ("How is she?", "b (health / mood)"), ("What does she like?", "a (interests)")]
    ans = ["She likes the gym and the beach.", "She's fine, but a little tired.", "She's tall, with red curly hair.", "She's friendly and very funny."]
    qal = "".join(f"<li>{q} {A(a, 'min-width:22mm')}</li>" for q, a in qa)
    ansl = " &nbsp; ".join(f"<b>{chr(97+i)}</b> {a}" for i, a in enumerate(ans))
    cs = [(["She's in her early forties.", "She has forty years."], "She's in her early forties."),
          (["She looks a bit like a college professor.", "She looks a bit a college professor."], "She looks a bit like a college professor."),
          (["She looks a little tired.", "She looks like a little tired."], "She looks a little tired.")]
    csl = "".join(f"<li>{ch(o, a)}</li>" for o, a in cs)
    use = ["What does your best friend look like?", "Who do you look like in your family?", "Describe someone you saw today.",
           "What did you use to look like ten years ago?", "Your teacher describes a person: ask three questions to find out more."]
    b.page(f"""{sec(4, "Practice: describing appearance", "10 min")}
{sub("A", "Match the questions to the answers a–d.", "2 min")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.6">{ansl}</p>
<ol style="line-height:1.6;font-size:8.9pt;margin:0;column-count:2">{qal}</ol>
{sub("B", "Which sentence from the call is correct? Choose.", "2 min")}
<ol style="line-height:1.6;font-size:8.9pt;margin:0">{csl}</ol>
<div class="box sand"><h4>RULE</h4><b>be</b> + age, height, build · <b>have</b> + hair, eyes, a beard · <b>look</b> + adjective · <b>look like</b> + noun · <i>a bit, a little</i> + negative ideas; <i>quite, fairly</i> = medium · hair: <b>length → style → color</b>. See the <b>Grammar reference</b> on page 3.</div>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    24, """<ol><li>A–B: 4 minutes. <i>What does she look like?</i> vs <i>What's she like?</i> is a classic confusion: ask both about someone the student knows.</li>
<li>Use it: 6 minutes, all oral. Correct <i>has… years</i>, <i>hairs</i> and <i>looks like</i> + adjective.</li></ol>""")

    # 5 Speaking
    b.page(f"""{sec(5, "Speaking: describing people", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>approximate</th><th>compare</th><th>be polite</th><th>check and identify</th></tr>
<tr><td><i>I'd say she's in her fifties. · He's about 1.80 m. · tallish · thirtyish</i></td><td><i>She looks a bit like… · He reminds me of… · She's taller than…</i></td><td><i>He's a bit overweight. · She isn't very tall. · He's quite slim.</i></td><td><i>Is that the man with…? · Which one? The one in the blue jacket?</i></td></tr></table></div>
{audiocard(["04.2"])}
{sub("A", "Linking. Listen and repeat: She's_got_an_oval face · He's_in_his forties.", "4 min", "04.2")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.55">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S042))}</p>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("B", "Role-play: at the airport. You have to meet your teacher's relative at the airport. Call your teacher, ask questions and take notes. Then change roles: describe a person you know.", "10 min")}
<div style="font-size:8.6pt"><b>Notes:</b>{lines(2)}</div>
<p style="margin:.3mm 0;font-size:8.6pt">{R("Teacher's card: Uncle Jorge, in his late fifties, short and stocky, bald, a gray mustache, small glasses, a red soccer shirt, a big black suitcase.") if T else ""}</p></div>{img('D', 32, 24)}</div>
{talk(["How does your appearance influence what people think of you, for example at a job interview?", "Is there too much pressure on people to look good today? What about photo filters?"])}""",
    28, """<ol><li>A: students often add a vowel (<i>She's-i got-i an</i>). Model the chunks slowly, then at natural speed.</li>
<li>B: answer only what the student asks, so they need questions like <i>How old is he? What's he wearing?</i> Last 3 minutes: wrap-up (two corrections and <i>Can you describe a person politely?</i>).</li></ol>""")

    # H Homework
    pr = [(["in his mid-twenties", "with twenty-five years"], "in his mid-twenties"), (["short curly black", "black short curly"], "short curly black"),
          (["looks", "looks like"], "looks like"), (["has", "is with"], "has"), (["looks", "looks like"], "looks"), (["put on", "lost"], "put on")]
    p = [ch(o, a) for o, a in pr]
    wo = [("dark / straight / long", "long straight dark"), ("gray / wavy / short", "short wavy gray"), ("red / curly / shoulder-length", "shoulder-length curly red")]
    wol = " &nbsp;·&nbsp; ".join(f"({w}) {A(a, 'min-width:30mm')} hair" for w, a in wo)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Danny writes to his mom about the people at his hostel. Choose the correct words.", "")}</div>{img('C', 28, 18)}</div>
<div class="box" style="line-height:1.8;font-size:8.8pt;margin:.5mm 0">Hi Mom! My roommate Bruno is {p[0]}. He's quite tall and well-built, and he has {p[1]} hair. He's growing a beard at the moment, and honestly, he {p[2]} a pirate! Mrs. Lima, the owner, is in her sixties. She's short and slim and she {p[3]} gray hair. She {p[4]} strict, but she's really kind. And me? I think I've {p[5]} a few kilos – the cheese bread here is amazing! Love, Danny</div>
{sub("B", "Write the words in the correct order.", "")}
<p style="margin:.3mm 0;line-height:1.9;font-size:8.6pt">{wol}</p>
{lean.watch_out([("He's moreno.", "He has dark hair. / He's tanned. / He has brown skin.", "English needs to say if it's the hair, a tan or the skin."), ("She's very thin. (as a compliment)", "She's slim.", "<i>slim</i> is positive; <i>thin</i> and <i>skinny</i> can sound negative."), ("She has a fringe.", "She has bangs.", "<i>fringe</i> is British English.")])}
{lean.writing_task(sub, "A friend is going to meet someone you know at the airport. Write a message and describe the person.", "Hi! My friend… is going to pick you up. He's in his… He's quite… with…", ["age and build", "hair and face", "clothes", "100–150 words"], "I can describe a person's appearance politely and in detail.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class (justify each choice: <i>look like</i> + noun, <i>look</i> + adjective). When you correct the writing, focus on <i>be / have</i> and the order of adjectives.</p>""")

    script = "<br>".join(f"<b>{l.split(': ', 1)[0]}:</b> {l.split(': ', 1)[1]}" if ": " in l else l for l in S041)
    b.extra("Audio script", f"""
{sub("04.1", "Ana calls Danny: a favor at the airport (natural and slow)")}
<p style="line-height:1.4;font-size:9pt">{script}</p>
{sub("04.2", "Repeat: linking sounds")}
<p>{" · ".join(S042)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 04 - People's appearance")
