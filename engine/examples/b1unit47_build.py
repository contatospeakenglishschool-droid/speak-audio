# Speak! Progress B1 - Unit 47 "Musical connections" (all English) - lean B1 format
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
setup(band="B1 · UNIT 47", audio_json="audio_b1-unit-47.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-47"]
S471 = [l.split(": ", 1) for l in _r["47.1 Gap Year Diaries: what's on your playlist?"].split("\n")]
S472 = [x.split(": ", 1)[1] for x in _r["47.2 Repeat: both, either, neither"].split("\n")]


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
    cover = cover_html(T, "LEVEL B1 · UNIT 47", "Musical connections", "Music in your life · <b>Both of us… · Neither of us… · either … or</b>",
                       [("YOU CAN", "talk about your musical tastes and compare them with someone else's"),
                        ("LANGUAGE", "record an album · perform live · get a record deal · upbeat · melancholic · both · either · neither"),
                        ("PRONUNCIATION", "stress on BOTH, EIther, NEIther")])
    kw = [("to make a new album available for people to buy or stream", "release", "an album"),
          ("to play or sing in front of an audience", "perform", "live"),
          ("to be the most popular song or album of the week", "be", "number one in the charts"),
          ("to make music in a studio so people can listen to it later", "record", "an album"),
          ("to pay a person to organize your concerts and your career", "hire", "a manager"),
          ("to sign a contract with a music company", "get", "a record deal")]
    kwl = "".join(f'<li>{A(v, "min-width:18mm")} <b>{n}</b> <span style="color:#6b7377">= {d}</span></li>' for d, v, n in kw)
    b.page(f"""{sec(1, "Warm-up: music everywhere", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["Where do you hear music in a normal day? Think of five places.", "How do you usually listen to music: phone, computer, radio, at concerts, on a record player?", "What music did you listen to as a teenager?"], "START TALKING")}</div></div>
{sub("A", "The music industry. Complete the phrases with the verbs from the box.", "3 min")}
<div class="bank">{" · ".join(sorted(v for d, v, n in kw))}</div>
<ol style="font-size:8.7pt;line-height:1.75;margin:0">{kwl}</ol>
{talk(["Which artists perform live in your city often? Have you seen any of them?", "If you had a band, would you rather record an album or perform live? Why?", "Would you like to be a singer or a musician? Why or why not?"], "USE THE PHRASES")}""",
    28, """<ol><li>Top box: 3 minutes. Possible places: on the radio, in a supermarket, in a mall, on hold with a call center, on TV, in the street, at the gym.</li>
<li>A: 4 minutes with the questions. <i>a record deal</i> = a contract with a record company. In American English <i>the charts</i> are often called <i>the Billboard charts</i>.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Gap Year Diaries: Danny and Bruno compare their musical tastes · Danny or Bruno? · questions · Talk about it",
                      "both … and, either … or, neither … nor; both / either / neither (of us) + verb agreement; one negative only", "Choose the correct words · rewrite · Use it (oral)",
                      "both, either, neither (47.2) · describe music with adjectives · types of music: name an artist · long turn: your musical life", "Danny's message to Rafa · rewrite · watch out · writing a post about your music"),
        """The Linguahouse lesson is vocabulary only: places where you hear music, twelve instruments and their families, adjectives to describe music (calm, dramatic, energetic, heavy, melancholic, upbeat), matching famous foreign artists with types of music, ways of listening, and music-industry verbs. It has no listening text and no grammar, so we added a Gap Year Diaries episode and a new B1 grammar point: both, either, neither. We did not use the list of foreign artists: the student names artists they know for each type of music, so we don't state facts about real people. Story: Danny and Bruno share a room at the hostel. Bruno likes rock and metal (for running) and old samba from his grandfather; he played the drums in a school band (no record deal; they performed live once, at his cousin's wedding). Danny likes calm music: jazz and classical for work, and country because his mom plays it in the car; he can play neither the piano nor the guitar (he tried the trumpet as a kid, and the neighbors complained); he listens on his phone or laptop and dreams of a record player; Bruno's dad has an old record player and hundreds of records. Rafa plays the saxophone in a jazz band; they perform live at a bar near the hostel next Friday, and both Danny and Bruno are going.""",
        """Double negatives (<i>I don't like neither</i>); <i>neither … or</i>; <i>both of rock and jazz</i>; <i>the both</i>. Vocabulary: <i>play the guitar</i>; <i>a song</i> vs <i>a music</i> (<i>music</i> is uncountable: <i>a piece of music</i>). Pronunciation: stress on <i>BOTH, EIther, NEIther</i>; <i>either</i> /ˈiːðər/ or /ˈaɪðər/.""",
        "Track 47.1 Gap Year Diaries: what's on your playlist? (natural and slow; Danny and Bruno) · Track 47.2 Repeat: both, either, neither"))

    # Page 2 - Listening
    rows = [("type of music", "calm: jazz, classical, country", "rock, metal, old samba"),
            ("why?", "for work; his mom plays country in the car", "energetic music for running; his grandfather's samba"),
            ("instrument", "neither piano nor guitar; tried the trumpet as a kid", "the drums, in a band at school"),
            ("how he listens", "on his phone or laptop (dream: a record player)", "— (his dad has a record player)")]
    rt = "".join(f'<tr><td><b>{r}</b></td><td>{A(d, "min-width:36mm")}</td><td>{A(bb, "min-width:36mm")}</td></tr>' for r, d, bb in rows)
    qs = [("What happened with Bruno's band?", "They never got a record deal; they performed live only once, at his cousin's wedding."),
          ("Why did Danny stop playing the trumpet?", "The neighbors complained."),
          ("What does Bruno's dad have?", "An old record player and hundreds of records."),
          ("What are they doing next Friday?", "Going to see Rafa's jazz band perform live at a bar near the hostel.")]
    ql = "".join(f"<li>{q} {A(a, 'min-width:50mm')}</li>" for q, a in qs)
    b.page(f"""{sec(2, "Listening: what's on your playlist?", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Listen to Danny's podcast. Complete the table for Danny and Bruno.", "5 min")}
<table style="font-size:8.4pt;margin:.5mm 0"><tr><th></th><th>Danny</th><th>Bruno</th></tr>{rt}</table></div>{img('B', 32, 30)}</div>
{audiocard(["47.1 · NATURAL", "47.1 · SLOW"])}
{sub("B", "Listen again and answer.", "3 min")}
<ol style="line-height:1.5;font-size:8.6pt;margin:0">{ql}</ol>
<p style="margin:.6mm 0;font-size:8.6pt"><b>Think about it:</b> Danny and Bruno share a room, and their tastes are very different. How do you think they manage? {A("open answer: headphones; they find music both of them like; they joke about it", "min-width:20mm")}</p>
{talk(["Is your taste in music closer to Danny's or to Bruno's?", "Do you play an instrument, or did you try one as a kid?", "Would you like to have a record player? Why or why not?"])}""",
    30, """<ol><li>A: play the natural version; play the slow one if needed. Accept short notes.</li>
<li>B: ask the student to find <i>both, either, neither</i> in what they heard: <i>both of us listen, both jazz and classical, neither of us likes, neither the piano nor the guitar, either on my phone or on my laptop</i>. They come back on page 3.</li>
<li>Talk about it: 4 minutes.</li></ol>""")

    # Page 3
    lean.grammar_in_class(b, grammar_ref.both_either_neither)

    # Page 4 - Practice
    pc = [("", ["Both", "Either"], "Both", "my sister and my brother play the guitar."), ("Neither Danny", ["or", "nor"], "nor", "Bruno can play the piano."),
          ("We can", ["either", "neither"], "either", "go to the concert or watch it online."), ("I don't like", ["neither", "either"], "either", "of these songs."),
          ("", ["Neither", "Either"], "Neither", "of us has a record player."), ("She speaks both English", ["and", "or"], "and", "Spanish."),
          ("You can pay", ["either", "both"], "either", "by card or in cash."), ("", ["The both", "Both"], "Both", "albums were number one in the charts.")]
    cl = "".join(f"<li>{a} {ch(o, r)} {z}</li>" for a, o, r, z in pc)
    rw = [("Danny doesn't play the piano. Bruno doesn't play the piano. (neither … nor)", "Neither Danny nor Bruno plays the piano."),
          ("Bruno likes rock. He also likes metal. (both … and)", "Bruno likes both rock and metal."),
          ("We'll go to the concert, or we'll watch it online. (either … or)", "We'll either go to the concert or watch it online.")]
    rwl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw)
    use = ["Do you play an instrument? Do I? So… both of us / neither of us…?", "Which do you prefer: concerts or listening at home? Or both?",
           "Name two artists you like. Is either of them performing in Brazil this year?", "Would you rather listen to music while you work or while you exercise? Either? Neither?",
           "Find two things you and your teacher have in common about music."]
    b.page(f"""{sec(4, "Practice: both, either or neither?", "10 min")}
{sub("A", "Choose the correct words.", "3 min")}
<ol style="line-height:1.7;font-size:8.7pt;margin:0;columns:2;column-gap:6mm">{cl}</ol>
{sub("B", "Rewrite the sentences with the words in brackets.", "4 min")}
<ol style="line-height:1.45;font-size:8.7pt;margin:0">{rwl}</ol>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    30, """<ol><li>A: 3 minutes. Item 4: one negative only, so <i>either</i>. Item 5: <i>Neither of us has</i> (singular; <i>have</i> is also common in speech).</li>
<li>B: item 1: the verb agrees with <i>Bruno</i>: <i>plays</i>.</li>
<li>Use it: 3 minutes, all oral. Answer the questions about yourself too, so the student can say <i>Both of us… / Neither of us…</i>.</li></ol>""")

    # Page 5 - Speaking
    gen = ["classical", "country", "jazz", "MPB", "pop", "rap", "rock", "samba", "sertanejo"]
    card = f"""<div class="box" style="margin-top:1mm;font-size:8.2pt">{R("<b>Teacher's card (B):</b> play 20 seconds of three different pieces of music from your phone (for example something calm, something heavy and something upbeat). The student describes each one with an adjective and says how it makes them feel. (C) Then name an artist for three types of music and compare: <i>Both of us like… / Neither of us listens to…</i>")}</div>""" if T else ""
    b.page(f"""{sec(5, "Speaking: your musical life", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.2pt"><tr><th>describing music</th><th>likes</th><th>dislikes</th><th>comparing</th></tr>
<tr><td><i>It's calm / dramatic / energetic / heavy / melancholic / upbeat. · It makes me feel…</i></td><td><i>I'm really into… · I listen to it when… · It reminds me of…</i></td><td><i>I can't stand… · It's too … for me. · It's not my thing.</i></td><td><i>Both of us… · Neither of us… · I like either, I don't mind.</i></td></tr></table></div>
{audiocard(["47.2"])}
{sub("A", "Listen and repeat. Stress BOTH, EIther, NEIther.", "3 min", "47.2")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S472))}</p>
{sub("B", "Your teacher plays three short pieces of music. Describe each one: which adjective? How does it make you feel?", "4 min")}
{sub("C", "Types of music. Name an artist you know for each type. Which do you like? Compare with your teacher.", "4 min")}
<div class="bank" style="font-size:8.6pt;background:#fff">{" · ".join(gen)}</div>{card}
{sub("D", "Long turn. Talk about your musical life: what you listened to as a teenager, what you listen to now, a concert you'll never forget, a song that reminds you of someone.", "5 min")}
<p style="margin:.3mm 0;font-size:8.5pt">Plan (1 min): {lines(1)}</p>""",
    30, """<ol><li>B replaces the Linguahouse audio samples: use any music from your phone. There are no right or wrong answers.</li>
<li>C replaces the Linguahouse matching with famous foreign artists: the student chooses the artists. D: 1 minute to plan, 2 minutes to talk. Last 3 minutes: wrap-up (two corrections, and ask <i>Can you now talk about your musical tastes and compare them?</i>).</li></ol>""")

    # Homework
    pc2 = [(["Both", "Neither"], "Both"), (["Neither", "Either"], "Neither"), (["either", "neither"], "either"), (["both", "either"], "both"),
           (["neither", "either"], "neither"), (["nor", "or"], "nor")]
    p = [ch(o, a) for o, a in pc2]
    rw2 = [("My mom doesn't like metal. My dad doesn't like it either. (neither … nor)", "Neither my mom nor my dad likes metal."),
           ("I listen to music on my phone or on the radio. (either … or)", "I listen to music either on my phone or on the radio."),
           ("My sister plays the piano, and my brother plays the piano too. (both)", "Both my sister and my brother play the piano.")]
    rwl2 = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw2)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Danny writes to Rafa before the concert. Choose the correct words.", "")}</div>{img('C', 30, 19)}</div>
<div class="box" style="line-height:1.85;font-size:8.8pt;margin:.5mm 0"><b>Hi Rafa!</b> {p[0]} Bruno and I are coming to your concert on Friday! {p[1]} of us has heard your band live, so we're really excited. We can {p[2]} take the bus or walk: the bar is only fifteen minutes from the hostel. Bruno wants to know if your band plays {p[3]} jazz and samba. And just so you know: {p[4]} Bruno {p[5]} I can dance, so please don't ask us to! See you on Friday! Danny</div>
{sub("B", "Rewrite the sentences with the words in brackets.", "")}
<ol style="line-height:1.5;font-size:8.7pt;margin:0">{rwl2}</ol>
{lean.watch_out([("I don't like neither of them.", "I don't like either of them. / I like neither of them.", "only one negative in English."), ("I like both of rock and jazz.", "I like both rock and jazz.", "<i>both A and B</i>: no <i>of</i>."), ("I listened to a beautiful music.", "I listened to a beautiful song / piece of music.", "<i>music</i> is uncountable.")])}
{lean.writing_task(sub, "Write a post for Danny's podcast page: your playlist and your musical life.", "Hi Danny! Here's my playlist…", ["types of music you love and can't stand", "an instrument you play (or don't)", "how you listen to music", "both … and, either … or, neither … nor", "100–150 words"], "I can talk about my musical tastes and compare them with someone else's.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class. In A, <i>Neither of us has heard</i>: singular verb after <i>neither of</i>. Read the writing at home and choose two mistakes to discuss in class.</p>""")

    script = "".join(f"<p style='margin:.5mm 0'><b>{s}:</b> {t}</p>" for s, t in S471)
    b.extra("Audio script", f"""
{sub("47.1", "Gap Year Diaries: what's on your playlist? (natural and slow; Danny and Bruno)")}
<div style="line-height:1.3;font-size:8.4pt">{script}</div>
{sub("47.2", "Repeat: both, either, neither")}
<p>{" · ".join(S472)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 47 - Musical connections")
