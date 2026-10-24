# Speak! Essentials A1 - Unit 21 "Where Is It?" (all English) - built with the shared engine
import sys
sys.path.insert(0, "/home/claude/speak-audio/engine")
from speak_engine import *
setup(band="A1 · UNIT 21", audio_json="audio_a1-unit-21.json", img_dir="img")

PHOTOS = [("A", "a bakery", "bakery"), ("B", "a bank", "bank"), ("C", "a movie theater", "movie theater"), ("D", "a museum", "museum"),
          ("E", "a pharmacy", "pharmacy"), ("F", "a post office", "post office"), ("G", "a supermarket", "supermarket"), ("H", "traffic lights", "traffic lights")]
MAP = open("townmap.svg").read()
def themap(h):
    return MAP.replace('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 260">',
                       f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 260" style="width:{h*400/260:.0f}mm;height:{h}mm;display:block;margin:0 auto;border-radius:2mm">')

SCRIPT = [("Narrator", "Dialogue one."), ("Paulo", "Excuse me, is there a bank near here?"),
          ("Woman", "Yes. Go straight. The bank is on the corner, at the traffic lights."), ("Paulo", "Thank you."), ("Woman", "You're welcome."),
          ("Narrator", "Dialogue two."), ("Paulo", "Excuse me, is there a supermarket near here?"), ("Man", "Yes, it's on Lake Street."),
          ("Paulo", "How do I get there?"), ("Man", "Go straight. Go past the movie theater and the park. Turn right at the second traffic lights. It's on the right."),
          ("Narrator", "Dialogue three."), ("Paulo", "Excuse me, I'm looking for the museum."),
          ("Woman", "Go straight ahead, past the café. Cross Lake Street. The museum is on the left."), ("Paulo", "Is it far?"),
          ("Woman", "No, it's close. About five minutes on foot."), ("Paulo", "Thank you!"),
          ("Narrator", "Dialogue four."), ("Paulo", "Excuse me, can you tell me the way to the post office?"),
          ("Man", "I'm sorry, I'm not from here."), ("Paulo", "Oh, no problem. Thanks anyway!")]
S212 = ["Excuse me.", "Excuse me, is there a bank near here?", "Excuse me, I'm looking for the museum.", "Excuse me, can you tell me the way to the post office?", "How do I get there?", "Is it far?"]
S213 = ["Sorry, can you repeat that?", "Can you say it again more slowly, please?", "Sorry, I didn't catch that.", "Is it on the right or the left?", "Let me check: I go past the bank, and it's on the corner?"]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    cover = cover_html(T, "LEVEL A1 · UNIT 21", "Where Is It?", "Places in town · <b>asking for and giving directions</b>",
                       [("YOU CAN", "ask for directions and help someone find a place"), ("LANGUAGE", "Is there a… near here? · Go straight. · Turn left. · It's on the corner."),
                        ("PRONUNCIATION", "Excuse me · polite questions ↗ · Sorry, can you repeat that?")])
    words = ["a bakery", "a bank", "a movie theater", "a museum", "a pharmacy", "a post office", "a supermarket", "traffic lights"]
    qs = [("are sick?", "a pharmacy"), ("have free time?", "a movie theater, a museum"), ("want to send a letter?", "a post office"),
          ("are hungry?", "a bakery, a supermarket"), ("need money?", "a bank")]
    ql = [f'<li value="{i+1}">… you <b>{q}</b> {R("→ " + a) if T else ""}</li>' for i, (q, a) in enumerate(qs)]
    b.page(f"""{sec(1, "Warm-up: places in town", "8 min")}
{sub("A", "Look, listen and repeat. Then write the place under the photo.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Where do you go if you…", "4 min")}
{twocol(ql, 4)}""",
    24, """<ol><li>A: <b>movie theater</b> (AmE) = <i>cinema</i> (BrE). <b>pharmacy</b> /ˈfɑrməsi/: the PH sounds like F.</li>
<li>B: accept any logical answer and ask: <i>Is there a pharmacy near your home?</i></li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>8 places in town with photos</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Paulo is lost in Chicago: four short dialogues</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Asking for directions · giving directions (imperatives) · prepositions</td><td>3–4</td></tr>
<tr><td>4 Pronunciation lab</td><td>5 min</td><td>Excuse me · polite questions · when you don't understand</td><td>4</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Follow the map · complete the dialogues</td><td>5</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Map role-play · directions in your own town</td><td>6</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>7</td></tr></table>
<div class="box"><h4>HOW THIS GUIDE WORKS</h4>Every page looks like the Student Book page with the same number. Your notes are in the <b>yellow box</b>.
<span class="red">Answers in red</span> are not in the Student Book. The <span class="time">5 min</span> chips show the time for each activity. Audio scripts are on the last page.</div>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Paulo (the travel photographer) is in Chicago again. His phone battery is dead, so he asks people on Main Street for directions. In the last dialogue, the man is a tourist too… and the post office is right behind Paulo!</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4><i>It's at the left</i> ✗ → <b>It's on the left</b>. <i>Turn right in the traffic lights</i> ✗ → <b>at the traffic lights</b>. And always start with <b>Excuse me</b>.</div>
<div class="box"><h4>AUDIO</h4>Track 21.1 Four dialogues (slow and natural) · Track 21.2 Asking politely · Track 21.3 When you don't understand</div>""")

    # Page 2
    places = [("1", "a bank"), ("2", "a supermarket"), ("3", "the museum"), ("4", "the post office")]
    pr = "".join(f'<td style="width:25%"><b>Dialogue {n}</b><br>{A(p, "min-width:30mm")}</td>' for n, p in places)
    gp = [("The bank is on the", "corner", ", at the traffic lights."), ("Go", "past", "the movie theater and the park."),
          ("Turn right at the second", "traffic lights", "."), ("The museum is on the", "left", "."), ("It's close. About five minutes", "on foot", ".")]
    gl = [f'<li value="{i+1}">{a} {A(x, "min-width:24mm")}{c}</li>' for i, (a, x, c) in enumerate(gp)]
    b.page(f"""{sec(2, "Listening: Paulo is lost", "10 min")}
<p>Paulo is in Chicago. He's on Main Street, his phone battery is dead, and he needs some places. He asks people for help.</p>
{audiocard(["21.1 · SLOW", "21.1 · NATURAL"])}
{sub("A", "Listen. What place does Paulo ask about in each dialogue?", "3 min", "21.1 · SLOW")}
<table class="ck"><tr>{pr}</tr></table>
{sub("B", "Listen again and complete the directions.", "5 min", "21.1 · NATURAL")}
{twocol(gl, 4)}
{sub("C", "Why is dialogue 4 different? Look at the map on page 5. Where is the post office?", "2 min")}
<div class="wline">{R("The man is not from here, so he can't help. And the post office is right next to Paulo, on the left!")}</div>""",
    26, """<ol><li>A: <b>slow</b> version. <i>near here</i> = close to this place.</li>
<li>B: <b>natural</b> version. Then the student follows the routes with a finger on the map (page 5): Paulo is at the red star.</li>
<li>C: a nice surprise for the student. <i>Thanks anyway</i> = thank you, even if you can't help.</li></ol>""")

    # Page 3
    ask = ["Excuse me, is there a bank near here?", "Excuse me, I'm looking for the museum.", "Excuse me, can you tell me the way to the post office?", "How do I get there?", "Is it far?"]
    give = [("↑", "Go straight (ahead)."), ("←", "Turn left."), ("→", "Turn right."), ("⤳", "Go past the park."), ("✚", "Cross the street."),
            ("🚦", "at the traffic lights")]
    give = [("↑", "Go straight (ahead)."), ("←", "Turn left."), ("→", "Turn right."), ("↗", "Go past the park."), ("⇵", "Cross Lake Street."), ("●", "at the traffic lights")]
    where = ["It's <b>on the left</b>.", "It's <b>on the right</b>.", "It's <b>on the corner</b>.", "It's <b>next to</b> the bank.", "It's <b>on</b> Lake Street."]
    rules = [("We start with", "Excuse me", "Excuse"), ("Directions use the verb without <i>you</i>:", "Turn left.", "You turn left."),
             ("A place on a side of the street is", "on the left", "at the left"), ("We stop or turn", "at the traffic lights", "in the traffic lights")]
    def rule(i, s, right, wrong):
        o = [right, wrong] if i % 2 == 0 else [wrong, right]
        o = [R(f"<u>{x}</u>") if (T and x == right) else x for x in o]
        return f"<li>{s} <b><i>{o[0]}</i></b> / <b><i>{o[1]}</i></b></li>"
    gt = "".join(f'<tr><td style="width:10mm;text-align:center;font-size:12pt;color:{TEAL}">{a}</td><td>{t}</td></tr>' for a, t in give)
    b.page(f"""{sec(3, "Language focus: asking for and giving directions", "10 min")}
{sub("A", "Asking for directions. Read the questions from the dialogues.", "2 min")}
<div class="bank" style="background:#fff;font-weight:600">{" &nbsp;·&nbsp; ".join(ask)}</div>
{sub("B", "Giving directions and saying where it is.", "4 min")}
<div class="two"><div><table style="margin:0"><tr><th colspan="2">Directions</th></tr>{gt}</table></div>
<div><table style="margin:0"><tr><th>Where is it?</th></tr>{"".join(f"<tr><td>{w}</td></tr>" for w in where)}</table></div></div>
{sub("C", "Choose the correct option.", "4 min")}
<ol>{"".join(rule(i, *r) for i, r in enumerate(rules))}</ol>
<div class="box"><h4>IMPERATIVE</h4>To give directions, we use the base verb with no subject: <b>Go</b> straight. <b>Turn</b> right. <b>Cross</b> the street. Negative: <b>Don't</b> turn left.</div>""",
    24, """<ol><li>A: three ways to ask. <i>Is there a…?</i> = Unit 14. All of them start with <b>Excuse me</b>.</li>
<li>B: act it out: the student gives you directions and you walk with your fingers on the map.</li></ol>""")

    # Page 4
    b.page(f"""{sub("D", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>Excuse, where is the bank?</td><td><b>Excuse me, where is the bank?</b></td><td>Always <i>Excuse me</i>.</td></tr>
<tr><td>How I get there?</td><td><b>How do I get there?</b></td><td>Question: <i>do</i> before the subject.</td></tr>
<tr><td>It's at the left.</td><td><b>It's on the left.</b></td><td>Side of the street = <i>on</i>.</td></tr>
<tr><td>Turn right in the traffic lights.</td><td><b>Turn right at the traffic lights.</b></td><td>A point = <i>at</i> (Unit 15).</td></tr>
<tr><td>Is it long?</td><td><b>Is it far?</b></td><td>Distance = <i>far</i>.</td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Pronunciation lab", "5 min")}
{audiocard(["21.2", "21.3"])}
{sub("A", "Asking politely. Listen and repeat. Start with a friendly Excuse me /ɪkˈskjuːz mi/.", "2 min", "21.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S212)}</div>
{sub("B", "When you don't understand. Listen and repeat.", "3 min", "21.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S213)}</div>""",
    40, """<ol><li>Mistakes: <i>at / on</i> is the most common problem. Use the map: <i>on</i> the left / right / corner / Lake Street, <i>at</i> the traffic lights.</li>
<li>4A: <i>Excuse me</i> has the stress on <b>-CUSE</b>. The voice goes up a little at the end of yes/no questions: <i>near here? ↗</i></li>
<li>4B: very useful in real life. Practice in the speaking: give fast directions so the student needs these phrases.</li></ol>""")

    # Page 5
    gw = ["Excuse", "straight", "looking", "ahead", "at", "on", "far", "tell", "past", "corner"]
    def g(i): return f"({i+1}) {A(gw[i], 'min-width:18mm')}"
    dls = [("Location 1: the bank", [("A", f"{g(0)} me, is there a bank near here?"), ("B", f"Yes. Go {g(1)}. It's on the left, at the traffic lights.")]),
           ("Location 2: the café", [("A", f"Excuse me, I'm {g(2)} for the café."), ("B", f"Go straight {g(3)} and cross Oak Street. Go past the movie theater. The café is {g(4)} the traffic lights, {g(5)} the left."), ("A", f"Is it {g(6)}?"), ("B", "No, it's about three minutes on foot.")]),
           ("Location 3: the supermarket", [("A", f"Excuse me, can you {g(7)} me the way to the supermarket?"), ("B", f"Sure. Go {g(8)} the park and turn right on Lake Street. The supermarket is on the {g(9)}.")])]
    dh = "".join(f'<p style="margin:1.5mm 0 .5mm;font-weight:800;color:{TEAL}">{t}</p>' + "".join(f"<div style='line-height:2'><b>{n}:</b> {x}</div>" for n, x in rows) for t, rows in dls)
    b.page(f"""{sec(5, "Practice", "8 min")}
{sub("A", "Look at the map. You are at the red star. Complete the dialogues with the words.", "8 min")}
<div style="margin:1mm 0 2mm">{themap(78)}</div>
<div class="bank">ahead · at · corner · Excuse · far · looking · on · past · straight · tell</div>
<div class="msg" style="max-width:none;padding:1mm 4mm 2mm">{dh}</div>""",
    18, """<p>Then read the dialogues together and check each route on the map with your finger. Location 3: the supermarket is on the corner of Main Street and Lake Street.</p>""")

    # Page 6
    tasks = ["the pharmacy", "the hotel", "the café", "the museum", "the post office", "the park"]
    b.page(f"""{sec(6, "Speaking", "12 min")}
{sub("A", "Role-play. You are at the red star. Ask your teacher for directions to a place. Then change roles.", "7 min")}
<div style="margin:1mm 0 2mm">{themap(70)}</div>
<div class="bank">{" &nbsp;·&nbsp; ".join(tasks)}</div>
<div class="bank" style="background:#fff">Excuse me, is there a… near here? · I'm looking for… · How do I get there? · Is it far? · Sorry, can you repeat that?</div>
{sub("B", "Your town. Talk about it.", "5 min")}
<ol style="line-height:1.65"><li>Is there a pharmacy near your home? How do you get there?</li><li>What's your favorite place in your city? Give directions from your home.</li><li>Do you use your phone or ask people when you are lost?</li></ol>""",
    22, """<ol><li>A: first the student asks and you give directions (speak naturally, so the student needs <i>Can you repeat that?</i>). Then swap: you ask, the student gives directions.</li>
<li>B: real places in the student's city. Correct <i>at / on</i> and <i>How do I get there?</i></li></ol>""")

    # Page 7
    pc = [("Unit 17", "I can use superlatives: the biggest, the best."), ("Unit 19", "I can talk about the weather and actions now."),
          ("Unit 20", "I can ask wh- questions: What are you doing?"), ("Unit 21", "I can name places in town."),
          ("Unit 21", "I can ask for and give simple directions.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Excuse, can you tell me where the bakery is?", "Excuse me, can you tell me where the bakery is?"), ("How I get there?", "How do I get there?"),
          ("Turn right on the traffic lights.", "Turn right at the traffic lights."), ("It's at the left.", "It's on the left."),
          ("Is it long?", "Is it far?"), ("It's about ten minutes if you're walk.", "It's about ten minutes on foot. / …if you're walking.")]
    hl = "".join(f'<li>{s} {R("→ " + a) if T else ""}</li>' for s, a in hw)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:15mm"></th><th>In English…</th><th style="width:20mm">Easy!</th><th style="width:20mm">Sometimes</th><th style="width:20mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Correct the mistakes.</b> There is one mistake in each sentence.</p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. From your home.</b> Write directions from your home to a bakery or a supermarket near you (3–4 sentences).</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Next class: check the corrections, then the student reads the directions and you "walk" them: <i>OK, I go straight… and then?</i></p>""")

    b.extra("Audio scripts", f"""
{sub("21.1", "Paulo is lost (slow and natural)")}
<p style="line-height:1.5">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("21.2", "Asking politely")}
<p>{" ".join(S212)}</p>
{sub("21.3", "When you don't understand")}
<p>{" ".join(S213)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essentials 21 - Where is it")
