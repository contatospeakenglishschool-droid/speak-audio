# Speak! Essentials A1 - Unit 22 "Wheels" (all English) - built with the shared engine
import sys
sys.path.insert(0, "/home/claude/speak-audio/engine")
from speak_engine import *
setup(band="A1 · UNIT 22", audio_json="audio_a1-unit-22.json", img_dir="img")

PHOTOS = [("A", "a bus", "bus"), ("B", "a taxi", "taxi"), ("C", "the subway", "subway"), ("D", "a bike", "bike"),
          ("E", "a train", "train"), ("F", "a scooter", "scooter"), ("G", "a car", "car"), ("H", "a motorcycle", "motorcycle")]

SCRIPT = [("Narrator", "Message one. Ana sends Tom a voice message."),
          ("Ana", "Hi Tom, it's Ana! I'm so happy you're coming to São Paulo next week! Thanks for sending me your flight details."),
          ("Ana", "I'm sorry, I can't meet you at the airport. I work at the hospital on Fridays. But it's easy to get to my house."),
          ("Ana", "There's a train from the airport. It's very cheap, and it takes about an hour."),
          ("Ana", "You can also take a taxi or an Uber, but it's expensive. It costs about a hundred and fifty reais! And the traffic is often terrible."),
          ("Ana", "There's also a bus. It's comfortable, but it's slow."),
          ("Ana", "So, to confirm: we're meeting at the café near my house at seven o'clock on Friday. Marcos and Leo are coming too!"),
          ("Ana", "Right now I'm on the subway. I usually drive to work, but today I'm trying something different. Oh, this is my stop. I need to go! See you soon!"),
          ("Narrator", "Message two. A week later, Tom answers."),
          ("Tom", "Hi Ana! I'm at the airport in Chicago. I'm waiting for my flight. It leaves at ten o'clock tonight, and it takes about ten hours."),
          ("Tom", "I'm taking the train from the airport. It's cheap, and I love trains! See you at the café on Friday at seven!")]
S222 = ["I'm meeting my friends tonight.", "You're coming next week.", "We're meeting at seven.", "She's taking the train.", "They're coming too.", "The bus is leaving now."]
S223 = ["How do you get to work?", "I take the bus.", "I go by subway.", "I go by car.", "I walk. I go on foot.", "It takes about twenty minutes."]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LEVEL A1 · UNIT 22", "Wheels", "Transportation · <b>present simple and present continuous</b> · future plans",
                       [("YOU CAN", "talk about how you travel, what you're doing now and your plans"),
                        ("LANGUAGE", "I usually take the bus. · I'm waiting now. · We're meeting on Friday."),
                        ("PRONUNCIATION", "I'm · you're · we're · they're · by bus · on foot")])
    words = ["a bike", "a bus", "a car", "a motorcycle", "a scooter", "the subway", "a taxi", "a train"]
    qs = [("Which ones need rails?", "a train, the subway"), ("Which ones can you rent in many cities?", "a bike, a scooter, a car"),
          ("Which one do you use most?", "personal answer")]
    ql = "".join(f'<li>{q} {R("→ " + a) if T else ""}</li>' for q, a in qs)
    b.page(f"""{sec(1, "Warm-up: getting around", "8 min")}
{sub("A", "Look, listen and repeat. Then write the word under the photo.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Answer the questions.", "4 min")}
<ol>{ql}</ol>""",
    22, """<ol><li>A: <b>the subway</b> (AmE) = <i>the underground / the metro</i>. <b>a bike</b> = a bicycle. A <b>scooter</b> here is an electric scooter (<i>patinete</i> in Brazil).</li>
<li>B: also ask: <i>Do you use Uber? Is it cheaper than a taxi?</i> An Uber = a car you call with an app.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>8 kinds of transportation with photos</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Ana's voice message to Tom and Tom's answer</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Present simple × present continuous (now) × present continuous (future plans) · state verbs</td><td>3</td></tr>
<tr><td>4 Pronunciation lab</td><td>5 min</td><td>Contractions in plans · how you get to work (by / on foot)</td><td>4</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Choose the form and say why · expressions with <i>take</i></td><td>5</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Information gap: Tom's week in São Paulo · your week · your transportation</td><td>6</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>7</td></tr></table>
<div class="box"><h4>HOW THIS GUIDE WORKS</h4>Every page looks like the Student Book page with the same number. Your notes are in the <b>yellow box</b>.
<span class="red">Answers in red</span> are not in the Student Book. The <span class="time">5 min</span> chips show the time for each activity. Audio scripts are on the last page.</div>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Tom is visiting Ana's family in São Paulo. Ana can't meet him at the airport (she works at the hospital on Fridays), so she sends a voice message from the subway: the train, a taxi or Uber, or the bus? A week later Tom answers from the airport in Chicago: he's taking the train. They're meeting at the café near Ana's house on Friday at seven.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4><i>I go with the bus</i> ✗ → <b>I go by bus / I take the bus</b>. <i>It spends one hour</i> ✗ → <b>It takes an hour</b>. <i>Tomorrow I meet my friend at 7</i> → <b>I'm meeting</b> (a plan with another person). <i>I'm needing</i> ✗ → <b>I need</b>.</div>
<div class="box"><h4>AUDIO</h4>Track 22.1 Two voice messages (slow and natural) · Track 22.2 Plans: contractions · Track 22.3 Getting around</div>""")

    # Page 2
    gist = [("What three ways from the airport to her house does Ana talk about?", "the train, a taxi or an Uber, the bus"),
            ("Where is Ana now?", "on the subway"), ("How is Tom going from the airport to Ana's house?", "by train")]
    gl = "".join(f'<li>{q}<div class="wline">{R(a)}</div></li>' for q, a in gist)
    items = [(["you're coming", "you come"], "you're coming", "I'm so happy", "to São Paulo next week!"),
             (["I work", "I'm working"], "I work", "", "at the hospital on Fridays."),
             (["It takes", "It's taking"], "It takes", "", "about an hour."),
             (["It costs", "It's costing"], "It costs", "", "about a hundred and fifty reais!"),
             (["we meet", "we're meeting"], "we're meeting", "So, to confirm:", "at the café on Friday."),
             (["come", "are coming"], "are coming", "Marcos and Leo", "too!"),
             (["I usually drive", "I'm usually driving"], "I usually drive", "", "to work."),
             (["I try", "I'm trying"], "I'm trying", "But today", "something different."),
             (["I need", "I'm needing"], "I need", "", "to go!"),
             (["I wait", "I'm waiting"], "I'm waiting", "TOM:", "for my flight.")]
    il = [f'<li value="{i+1}">{a} {ch(o, r)} {c}</li>' for i, (o, r, a, c) in enumerate(items)]
    b.page(f"""{sec(2, "Listening: see you on Friday!", "10 min")}
<p>Tom is visiting Ana and her family in São Paulo. Ana can't meet him at the airport, so she sends him a voice message. A week later, Tom answers.</p>
{audiocard(["22.1 · SLOW", "22.1 · NATURAL"])}
{sub("A", "Listen and answer.", "3 min", "22.1 · SLOW")}
<ol>{gl}</ol>
{sub("B", "Listen again. Choose the words you hear.", "5 min", "22.1 · NATURAL")}
{twocol(il, 6)}
{sub("C", "Where and when are Ana and Tom meeting?", "2 min")}
<div class="wline">{R("At the café near Ana's house, at seven o'clock on Friday.")}</div>""",
    24, """<ol><li>A: <b>slow</b> version. Taxi and Uber are one option. <i>reais</i> /reˈaɪs/ = Brazilian money.</li>
<li>B: <b>natural</b> version. Don't explain the grammar yet: just check what they hear. Page 3 explains why.</li>
<li>C: a <b>plan with a time and a place</b>: <i>we're meeting</i>. Ask: <i>Who is coming too?</i> (Marcos and Leo)</li></ol>""")

    # Page 3
    uses = [("Present simple", "habits and things that are always true", "I <b>usually drive</b> to work.<br>It <b>takes</b> about an hour.<br>The flight <b>leaves</b> at ten.", "always · usually · often · sometimes · never · every day · on Fridays"),
            ("Present continuous", "now, at this moment", "I'<b>m waiting</b> for my flight.<br>Today I'<b>m trying</b> something different.", "now · right now · today · at the moment"),
            ("Present continuous", "future plans with a day or time", "We'<b>re meeting</b> at seven on Friday.<br>You'<b>re coming</b> next week.", "tonight · tomorrow · on Friday · next week")]
    ut = "".join(f"<tr><td><b>{a}</b><br><span class='small'>{u}</span></td><td>{e}</td><td class='small'>{s}</td></tr>" for a, u, e, s in uses)
    rules = [("For habits (every day, usually), we use the", "present simple", "present continuous"),
             ("For actions at this moment, we use the", "present continuous", "present simple"),
             ("For plans with a day and time, we use the", "present continuous", "present simple"),
             ("With <i>need, want, love, know</i>, we", "don't use -ing", "use -ing")]
    def rule(i, s, right, wrong):
        o = [right, wrong] if i % 2 == 0 else [wrong, right]
        o = [R(f"<u>{x}</u>") if (T and x == right) else x for x in o]
        return f"<li>{s} <b><i>{o[0]}</i></b> / <b><i>{o[1]}</i></b>.</li>"
    np = ["I'm seeing the dentist on Monday.", "I'm having dinner with my parents tomorrow.", "I'm sitting on the bus and reading a book.", "I'm flying to Rio next month."]
    npl = "".join(f'<li>{x} {R("← NOT a plan: it is happening now") if (T and i == 2) else ""}</li>' for i, x in enumerate(np))
    b.page(f"""{sec(3, "Language focus: now, usually or a plan?", "10 min")}
{sub("A", "Read the sentences from the messages.", "3 min")}
<table style="table-layout:fixed"><tr><th style="width:42mm">Form and use</th><th>Examples</th><th style="width:44mm">Time words</th></tr>{ut}</table>
{sub("B", "Choose the correct option.", "3 min")}
<ol>{"".join(rule(i, *r) for i, r in enumerate(rules))}</ol>
{sub("C", "Which sentence is NOT a future plan?", "2 min")}
<ol type="a">{npl}</ol>
<div class="box"><h4>STATE VERBS</h4>Some verbs are about feelings and the mind, not actions: <b>need, want, love, like, hate, know</b>. We don't use them with -ing.
I <b>need</b> to go. ✓ &nbsp; <s>I'm needing to go.</s> ✗ &nbsp;·&nbsp; I <b>love</b> trains. ✓ &nbsp; <s>I'm loving trains.</s> ✗</div>""",
    24, """<ol><li>A: simple × continuous is a review of Units 19–20. The <b>new</b> use is the third line: present continuous for plans. A plan usually has a <b>time</b> (on Friday) and <b>other people</b> (we, my parents).</li>
<li>Drill: say a time word, the student makes a sentence: <i>right now → I'm sitting at home.</i></li></ol>""")

    # Page 4
    gw = [("by bus", "I take the bus. / I go by bus."), ("by car", "I drive. / I go by car."), ("by subway", "I take the subway."),
          ("by bike", "I ride my bike."), ("on foot", "I walk.")]
    gt = "".join(f"<tr><td><b>I go {a}.</b></td><td>{x}</td></tr>" for a, x in gw)
    b.page(f"""{sub("D", "Getting around", "2 min")}
<table style="margin-top:0"><tr><th style="width:55mm">by + transportation</th><th>Other ways to say it</th></tr>{gt}</table>
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>I go to work with the bus.</td><td><b>I go to work by bus.</b></td><td>Transportation: <i>by</i>, not <i>with</i>.</td></tr>
<tr><td>I go by foot.</td><td><b>I go on foot. / I walk.</b></td><td>Walking is different: <i>on foot</i>.</td></tr>
<tr><td>It spends one hour.</td><td><b>It takes an hour.</b></td><td>Time for a trip: <i>take</i>.</td></tr>
<tr><td>I'm usually taking the bus.</td><td><b>I usually take the bus.</b></td><td>A habit: present simple.</td></tr>
<tr><td>Tomorrow I meet my friend at 7.</td><td><b>Tomorrow I'm meeting my friend at 7.</b></td><td>A plan: present continuous.</td></tr>
<tr><td>I'm needing a taxi.</td><td><b>I need a taxi.</b></td><td>State verb: no -ing.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "5 min")}
{audiocard(["22.2", "22.3"])}
{sub("A", "Plans. Listen and repeat. Say the short forms: I'm, you're, we're, she's, they're.", "2 min", "22.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S222)}</div>
{sub("B", "Getting around. Listen and repeat.", "3 min", "22.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S223)}</div>""",
    27, """<ol><li>D: Brazilians translate <i>de ônibus</i> as <i>with the bus</i>. Fix it every time. <i>by</i> + no article: <b>by bus</b>, not <i>by the bus</i>. But: <b>take the bus</b>.</li>
<li>4A: <i>you're</i> sounds like <b>your</b> /jʊr/. <i>we're</i> /wɪr/. Don't say the full form (<i>we are meeting</i>) in natural speech.</li>
<li>4B: then ask the student: <i>How do you get to work? How long does it take?</i></li></ol>""")

    # Page 5
    pr = [("I", "my friends for a pizza tonight.", "meet", "'m meeting", "a plan"),
          ("Many tourists", "bikes in Rio.", "rent", "rent", "always true"),
          ("It", "about twenty minutes by bike.", "take", "takes", "always true"),
          ("We often", "the bus to the beach.", "take", "take", "a habit"),
          ("I", "motorcycles.", "love", "love", "state verb"),
          ("Look! Leo", "his bike in the park.", "ride", "'s riding", "now"),
          ("Tom", "a map. He's lost!", "need", "needs", "state verb"),
          ("Ana's parents", "her on Sunday.", "visit", "are visiting", "a plan"),
          ("Be quiet! Marcos", "on the phone.", "talk", "'s talking", "now"),
          ("Trains", "every ten minutes from this station.", "leave", "leave", "always true")]
    pl = "".join(f'<li>{a} {A(ans, "min-width:27mm")} {c} ({v}) {R("· " + why) if T else ""}</li>' for a, c, v, ans, why in pr)
    tk = [("I usually take", "to work. It's fast.", "the train"), ("It takes", "to get to the city center from my house.", "an hour"),
          ("I always take a lot of", "on vacation.", "photos"), ("I take", "every morning before work.", "a shower"),
          ("It's important to take", "from work every hour.", "a break")]
    tl = "".join(f'<li>{a} {A(x, "min-width:22mm")} {c}</li>' for a, c, x in tk)
    b.page(f"""{sec(5, "Practice", "8 min")}
{sub("A", "Complete with the verb in the correct form. Then say why: now, a habit, always true, a plan or a state verb?", "5 min")}
<ol style="line-height:1.85">{pl}</ol>
{sub("B", "Expressions with TAKE. Complete the sentences. Are they true for you? Tell your teacher.", "3 min")}
<div class="bank">a break · a shower · an hour · photos · the train</div>
<ol style="line-height:1.85">{tl}</ol>""",
    22, """<ol><li>A: do number 1 together. The student must say <b>why</b>: this is the real goal of the lesson. Contractions are fine: <i>I'm meeting</i>.</li>
<li>B: then make them true: <i>I don't take the train. I take the bus. It takes forty minutes.</i></li></ol>""")

    # Page 6
    plan = [("Friday", "7:00 p.m.", "meeting Ana's family at the café", True),
            ("Saturday", "morning", "taking the subway to Paulista Avenue", False),
            ("Saturday", "afternoon", "visiting a museum", True),
            ("Sunday", "morning", "riding a bike in Ibirapuera Park", False),
            ("Sunday", "1:00 p.m.", "having lunch with Ana's parents", True),
            ("Monday", "all day", "taking a bus to the beach in Santos", False),
            ("Tuesday", "10:30 p.m.", "flying back to Chicago", True)]
    def cell(x, shown):
        if shown:
            return x
        return R(x) if T else '<span style="color:#9aa;font-weight:800">?</span>'
    pt = "".join(f"<tr><td><b>{d}</b></td><td>{t}</td><td>{cell(x, s)}</td></tr>" for d, t, x, s in plan)
    b.page(f"""{sec(6, "Speaking", "12 min")}
{sub("A", "Tom's week in São Paulo. Ask your teacher about the ? and complete the planner. Then answer your teacher's questions.", "5 min")}
<table><tr><th style="width:26mm">Day</th><th style="width:26mm">Time</th><th>Tom's plans</th></tr>{pt}</table>
<div class="bank" style="background:#fff">What is Tom doing on Saturday morning? · He's taking the subway to… · Who is he having lunch with? · When is he flying back?</div>
{sub("B", "Your week. Answer your teacher's questions.", "3 min")}
<ol><li>What are you doing tonight?</li><li>What are you doing this weekend?</li><li>Are you meeting anyone next week? Who? Where?</li></ol>
{sub("C", "Getting around in your city. Talk about it.", "4 min")}
<ol><li>How do you usually get to work? How long does it take?</li><li>Do you take taxis or Uber? Is it expensive in your city?</li><li>Is public transportation good where you live? Why or why not?</li><li>A friend is coming to your city. What's the best way from the airport or bus station to your house?</li></ol>""",
    20, """<ol><li>A: you have the full planner (answers in red). The student asks about the <b>?</b> lines; then you ask about the others: <i>What is Tom doing on Friday at seven?</i> Insist on full answers: <i>He's meeting…</i></li>
<li>B–C: correct <b>by bus / on foot</b> and <b>It takes…</b>. In C4, help the student plan a real message (it's the homework).</li></ol>""")

    # Page 7
    pc = [("Unit 19", "I can talk about the weather and actions now."), ("Unit 20", "I can ask wh- questions: What are you doing?"),
          ("Unit 21", "I can ask for and give simple directions."), ("Unit 22", "I can say how I get to places (by bus, on foot)."),
          ("Unit 22", "I can talk about my plans: I'm meeting… on Friday.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [(["come", "'re coming"], "'re coming"), (["have", "'re having"], "'re having"), (["picks", "is picking"], "is picking"),
          (["takes", "is taking"], "takes"), (["eat", "are eating"], "eat"), (["make", "'m making"], "'m making"), (["know", "'m knowing"], "know")]
    def h(i): return f"({i+1}) {ch(*hw[i])}"
    msg = (f"Hi Tom! It's Rosa, Ana's mother. We're so happy that you {h(0)} to São Paulo! On Sunday, you {h(1)} lunch with us. "
           f"Carlos {h(2)} you up at Ana's house at noon. Our house is far, and the drive {h(3)} about forty minutes. "
           f"On Sundays, we always {h(4)} feijoada. I {h(5)} the beans right now! I {h(6)} you love coffee, so we have great Brazilian coffee for you. See you on Sunday!")
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:15mm"></th><th>In English…</th><th style="width:20mm">Easy!</th><th style="width:20mm">Sometimes</th><th style="width:20mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. A message from Rosa.</b> Choose the correct form.</p>
<div class="msg" style="max-width:none;line-height:1.7">{msg}</div>
<p style="margin-top:3mm"><b>2. Your message.</b> A friend is coming to your city. You can't meet them at the airport or bus station. Write a message (50–70 words): when they are coming, the best way to your house, the price, the time, and where and when you are meeting.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>1: <i>picks you up</i> = goes to get you by car. 2: the student can use Ana's message as a model. Next class: the student reads the message and you ask: <i>How much does it cost? Where are we meeting?</i></p>""")

    b.extra("Audio scripts", f"""
{sub("22.1", "Two voice messages (slow and natural)")}
<p style="line-height:1.5">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("22.2", "Plans: contractions")}
<p>{" ".join(S222)}</p>
{sub("22.3", "Getting around")}
<p>{" ".join(S223)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essentials 22 - Wheels")
