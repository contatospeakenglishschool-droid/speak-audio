# Speak! Bridge A2 - Unit 04 "Where's my phone?" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 04", audio_json="audio_a2-unit-04.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["a2-unit-04"]
NAMES = {"Host": "Host", "Doctor": "Dr. Brooks", "Lucy": "Lucy"}
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["04.1 Radio show"].split("\n")]
S042 = [x.split(": ", 1)[1] for x in _r["04.2 Repeat phrases"].split("\n")]
S043 = [x.split(": ", 1)[1] for x in _r["04.3 Repeat sentences"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1: one big photo + phone survey (abstract topic)
    cover = cover_html(T, "LEVEL A2 · UNIT 04", "Where's my phone?", "Phones and habits · <b>adjective + preposition, noun + preposition</b>",
                       [("YOU CAN", "listen to a radio show and talk about your phone habits"),
                        ("LANGUAGE", "I'm afraid of losing it. · I'm tired of waiting. · a solution to the problem"),
                        ("PRONUNCIATION", "weak of, to, for: afraid of /əv/ · a solution to /tə/")])
    sv = [("Where is your phone right now?", ["in my hand", "near me", "in another room"]),
          ("Do you check your phone at a restaurant with a friend?", ["always", "sometimes", "never"]),
          ("Do you read work messages on vacation?", ["always", "sometimes", "never"]),
          ("Do you take your phone into the bathroom?", ["always", "sometimes", "never"]),
          ("How do you feel when your battery is dead?", ["very worried", "a little worried", "not worried"])]
    svl = "".join(f"<li>{q}<br><span class='small'>{' &nbsp; ☐ '.join([''] + o)[7:]}</span></li>" for q, o in sv)
    b.page(f"""{sec(1, "Warm-up: you and your phone", "8 min")}
<div style="display:flex;gap:4mm;align-items:flex-start">
<div style="width:62mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo('A')}" style="width:62mm;height:62mm;object-fit:cover;display:block"></div>
<div style="flex:1">{sub("A", "The phone test. Check (✓) your answers.", "5 min")}
<ol style="margin-top:1mm">{svl}</ol></div></div>
{sub("B", "Talk about it.", "3 min")}
<ol><li>Count your answers. Do you think you control your phone, or does your phone control you?</li>
<li>How many hours a day do you think you use your phone? Check the screen time on your phone. Are you surprised?</li></ol>""",
    22, """<ol><li>A: do the test too and compare. Pre-teach <b>check</b> (look quickly), <b>dead</b> battery (no power) and <b>screen time</b>.</li>
<li>B: ask follow-ups with the unit language: <i>Are you worried about it? Are you tired of it?</i> Don't correct yet.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>The phone test</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>A radio call-in show about nomophobia</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Adjective + preposition · noun + preposition · preposition + -ing</td><td>3</td></tr>
<tr><td>4 Pronunciation lab</td><td>5 min</td><td>Weak prepositions · linking</td><td>4</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Lucy's email · preposition + -ing · Word builder: phone verbs</td><td>5</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Are you the same as me? · phone rules</td><td>6</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework (50–75 words)</td><td>7</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Back in Chicago: Lucy (student and weekend barista at City Coffee) calls <i>Chicago Talks</i>, a radio show (invented), where psychologist Dr. Alan Brooks (invented) talks about <b>nomophobia</b>, the fear of being without your phone. She takes her phone everywhere, even into the shower. Dr. Brooks gives her two rules: no phone at dinner, no phone in the bedroom. Facts: about nine in ten American adults (91%) own a smartphone (Pew Research Center, Mobile Fact Sheet, 2025); distracted driving killed 3,275 people in the United States in 2023 (NHTSA, "Distracted Driving in 2023", April 2025).</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Prepositions don't translate one to one: <i>worried with</i> ✗ → <b>worried about</b>; <i>married with</i> ✗ → <b>married to</b>; <i>different of</i> ✗ → <b>different from</b>; <i>good in</i> ✗ → <b>good at</b>. And after a preposition students use the base form: <i>tired of wait</i> ✗ → <b>tired of waiting</b>; <i>afraid of to lose</i> ✗ → <b>afraid of losing</b>.</div>
<div class="box"><h4>AUDIO</h4>Track 04.1 The radio show (slow and natural) · Track 04.2 Phrases · Track 04.3 Sentences · Dr. Brooks uses a new voice (Chirp 3 HD Charon).</div>""")

    # Page 2: listening
    tf = [("Nomophobia is the fear of using a phone.", "F: the fear of being without your phone."), ("About 90% of American adults have a smartphone.", "T: about nine in ten."),
          ("Dr. Brooks sees fewer patients with this problem now.", "F: he sees an increase."), ("Lucy lost her phone on the train.", "F: on the bus."),
          ("Dr. Brooks tells Lucy to stop using her phone.", "F: he tells her to make some rules."), ("Using your phone while you're driving can kill.", "T: 3,275 deaths in 2023.")]
    tfl = [f'<li value="{i+1}">{s} <b>T / F</b> {R(a)}</li>' for i, (s, a) in enumerate(tf)]
    pp = [("familiar", ["with", "to"], "with", "this feeling"), ("the fear", ["of", "from"], "of", "being without your phone"),
          ("an increase", ["in", "of"], "in", "the number of patients"), ("worried", ["for", "about"], "about", "it"),
          ("separation", ["of", "from"], "from", "their phone"), ("in contact", ["with", "to"], "with", "my friends"),
          ("the reasons", ["for", "of"], "for", "this problem"), ("a solution", ["for", "to"], "to", "it"),
          ("tired", ["with", "of"], "of", "feeling this way"), ("responsible", ["for", "of"], "for", "how we use our phones")]
    ppl = [f'<li value="{i+1}">{a} {ch(o, r)} {c}</li>' for i, (a, o, r, c) in enumerate(pp)]
    b.page(f"""{sec(2, "Listening: a radio show", "10 min")}
<p>Lucy listens to <i>Chicago Talks</i>, a radio show. Today's guest is psychologist Dr. Alan Brooks. Lucy decides to call the show.</p>
{audiocard(["04.1 · SLOW", "04.1 · NATURAL"])}
{sub("A", "Listen. True (T) or false (F)? Correct the false sentences.", "4 min", "04.1 · SLOW")}
{twocol(tfl, 4)}
{sub("B", "Listen again. Choose the word you hear.", "4 min", "04.1 · NATURAL")}
{twocol(ppl, 6)}
{sub("C", "What do you think of Dr. Brooks's two rules? Are they easy for you?", "2 min")}""",
    22, """<p>A: before listening, ask <i>What do you think "nomophobia" means?</i> (no + mobile + phobia). Explain <b>FOMO</b> = the fear of missing out. B: the student guesses first, then listens; the words in bold are the patterns of page 3. If there's time, read the script (TB last page): you are Dr. Brooks, the student is Lucy.</p>""")

    # Page 3
    b.page(f"""{sec(3, "Language focus: words + prepositions", "10 min")}
{sub("A", "Read the sentences from the radio show. Then choose the correct option.", "3 min")}
<div class="bank" style="background:#fff;font-weight:600">I'm sure many listeners are <u>familiar with</u> this feeling. · I'm seeing an <u>increase in</u> the number of patients. · They're <u>afraid of losing</u> contact. · I'm <u>tired of feeling</u> this way.</div>
<ol><li>Some adjectives and nouns are followed by a fixed {ch(["preposition", "verb"], "preposition")}.</li>
<li>After a preposition, we use a noun or {ch(["to + verb", "verb + -ing"], "verb + -ing")}.</li></ol>
{sub("B", "Complete the tables with prepositions. Use page 2 to help.", "5 min")}
<div class="two"><div><table style="margin-top:0;font-size:9pt"><tr><th>adjective</th><th>preposition</th></tr>
<tr><td>worried</td><td>{A("about", "min-width:14mm")}</td></tr><tr><td>afraid / tired</td><td>{A("of", "min-width:14mm")}</td></tr>
<tr><td>familiar</td><td>{A("with", "min-width:14mm")}</td></tr><tr><td>responsible</td><td>{A("for", "min-width:14mm")}</td></tr>
<tr><td>interested</td><td>{A("in", "min-width:14mm")}</td></tr></table></div>
<div><table style="margin-top:0;font-size:9pt"><tr><th>noun</th><th>preposition</th></tr>
<tr><td>the fear</td><td>{A("of", "min-width:14mm")}</td></tr><tr><td>an increase</td><td>{A("in", "min-width:14mm")}</td></tr>
<tr><td>separation</td><td>{A("from", "min-width:14mm")}</td></tr><tr><td>the reason / a need</td><td>{A("for", "min-width:14mm")}</td></tr>
<tr><td>a solution</td><td>{A("to", "min-width:14mm")}</td></tr></table></div></div>
{sub("C", "Test yourself. Cover the tables. Your teacher says a word; you say the word + preposition.", "2 min")}
<div class="msg" style="max-width:none;padding:1.5mm 4mm"><b>Teacher:</b> Interested… <b>You:</b> Interested on? <b>Teacher:</b> No, try again! <b>You:</b> Interested in! <b>Teacher:</b> Correct!</div>
<div class="box sand"><h4>MORE USEFUL PAIRS</h4><b>good at</b> (cooking) · <b>excited about</b> · <b>different from</b> · <b>married to</b> · <b>proud of</b> · <b>depend on</b> · <b>in contact with</b><br>Preposition + -ing: I'm afraid <b>of losing</b> it. Thanks <b>for calling</b>. She's good <b>at cooking</b>.</div>""",
    24, """<ol><li>A: elicit the nouns after the prepositions: <i>this feeling, the number, contact, this way</i>; <i>losing / feeling</i> work like nouns (gerunds).</li>
<li>B: these combinations must be memorized. C: do it fast, 10–12 words, then swap roles.</li></ol>""")

    # Page 4
    b.page(f"""{sub("D", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>I'm worried with my exam.</td><td><b>I'm worried about my exam.</b></td><td>worried + about.</td></tr>
<tr><td>I'm tired of wait.</td><td><b>I'm tired of waiting.</b></td><td>preposition + -ing.</td></tr>
<tr><td>She's afraid of to lose it.</td><td><b>She's afraid of losing it.</b></td><td>preposition + -ing.</td></tr>
<tr><td>He's married with a doctor.</td><td><b>He's married to a doctor.</b></td><td>married + to.</td></tr>
<tr><td>My phone is different of yours.</td><td><b>My phone is different from yours.</b></td><td>different + from.</td></tr>
<tr><td>I'm good in math.</td><td><b>I'm good at math.</b></td><td>good + at.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "5 min")}
{audiocard(["04.2", "04.3"])}
{sub("A", "Phrases. Listen and repeat. The prepositions are short and weak.", "2 min", "04.2")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S042)}</div>
{sub("B", "Sentences. Listen and repeat. Link the words.", "2 min", "04.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S043)}</div>
<div class="box" style="margin-top:1mm"><h4>WEAK AND LINKED</h4><b>of</b> = /əv/, <b>to</b> = /tə/, <b>for</b> = /fər/. Link a consonant to the next vowel: <i>afraid_of</i> = "afray-dəv", <i>tired_of</i> = "tire-dəv", <i>interested_in</i> = "interesti-din".</div>""",
    24, """<ol><li>4A: Brazilians often stress the preposition (<i>afraid OF</i>). The stress is on the adjective: a<b>FRAID</b> of, <b>WOR</b>ried about, <b>IN</b>terested in.</li>
<li>4B: <i>interested</i> has three syllables in fast speech: <b>IN</b>-tres-tid.</li></ol>""")

    # Page 5
    em = [("about", "worried"), ("for", "responsible"), ("of", "afraid"), ("with", "familiar"), ("for", "need"), ("of", "tired"), ("to", "solution"), ("in", "interested")]
    g = [A(p, "min-width:11mm") for p, _ in em]
    email = (f"Hi Dr. Brooks, it's Lucy, the caller from last week! I'm writing to tell you about my week. At first I was worried <sup>1</sup>{g[0]} your rules, but they work! "
             f"I'm responsible <sup>2</sup>{g[1]} a real alarm clock now (it was eight dollars). I'm less afraid <sup>3</sup>{g[2]} missing messages, and my friends are familiar "
             f"<sup>4</sup>{g[3]} my new rule: no phone at dinner. I still have a need <sup>5</sup>{g[4]} my phone at work, of course. But I'm not tired <sup>6</sup>{g[5]} my life anymore. "
             f"Thanks for the solution <sup>7</sup>{g[6]} my problem! Are you interested <sup>8</sup>{g[7]} hearing about week two?")
    ing = [("I'm tired of", "wait", "waiting", "for the bus every morning."), ("Thank you for", "help", "helping", "me with my homework."),
           ("Tom is good at", "explain", "explaining", "grammar."), ("Are you interested in", "learn", "learning", "Spanish?"), ("She's afraid of", "fly", "flying", "alone.")]
    ingl = "".join(f"<li>{a} {A(r, 'min-width:20mm')} <span class='small'>({v})</span> {c}</li>" for a, v, r, c in ing)
    wb = [("send", "a text message"), ("make", "a call"), ("take", "a photo"), ("charge", "the battery"), ("check", "your messages"), ("listen to", "your voicemail")]
    nouns = ["the battery", "your messages", "a photo", "a text message", "your voicemail", "a call"]
    wbt = "".join(f"<tr><td>{i+1}. {v}</td><td>{A(n, 'min-width:28mm')}</td></tr>" for i, (v, n) in enumerate(wb))
    b.page(f"""{sec(5, "Practice", "8 min")}
{sub("A", "One week later Lucy writes to Dr. Brooks. Complete with prepositions.", "3 min")}
<p style="line-height:1.85;margin:1mm 0">{email}</p>
{sub("B", "Complete with the -ing form of the verbs.", "2 min")}
<ol>{ingl}</ol>
{sub("C", "Word builder: phone verbs. Match the verbs with the nouns.", "3 min")}
<div class="bank">{" · ".join(nouns)}</div>
<table style="table-layout:fixed;margin-top:0;font-size:9pt;width:70%">{wbt}</table>
<p class="small">Phone problems: <i>My battery is dead.</i> (no power) · <i>There's no signal here.</i> (no connection)</p>""",
    22, """<ol><li>A: then ask the student to find the noun or -ing form after each preposition (<i>your rules, a real alarm clock, missing…</i>).</li>
<li>C: from the bonus lesson <i>Cell phones</i> (Vocabulary to Go).</li></ol>""")

    # Page 6
    st = ["I'm afraid of…", "I'm interested in…", "I'm not very good at…", "I'm tired of…", "I'm worried about…", "In my family, I'm responsible for…",
          "In Brazil, we're seeing an increase in…", "Separation from my phone makes me feel…"]
    rules = ["no phone at dinner", "no phone in the bedroom", "no phone while driving", "no work messages after 8 p.m.", "no phone in class", "one hour without a phone every day"]
    b.page(f"""{sec(6, "Speaking", "12 min")}
{sub("A", "Are you the same as me? Complete the sentences so they are true for you. Then compare with your teacher.", "7 min")}
<div class="two"><div><ol>{"".join(f"<li>{s}<div class='wline'></div></li>" for s in st[:4])}</ol></div><div><ol start="5">{"".join(f"<li>{s}<div class='wline'></div></li>" for s in st[4:])}</ol></div></div>
<div class="msg" style="max-width:none;padding:1.5mm 4mm"><b>You:</b> I'm afraid of flying. <b>Teacher:</b> Really? Me too! / Oh, I'm not. I love flying!</div>
{sub("B", "Phone rules. Which rules are good for you? Which are impossible? Why?", "5 min")}
<div class="bank">{" · ".join(rules)}</div>
<ol><li>Which two rules can you start this week?</li><li>Should schools in Brazil allow phones in the classroom? Why / why not?</li></ol>""",
    26, """<ol><li>A: remind the student that a noun or -ing form comes after the preposition. Complete the sentences too, then compare: <i>We're the same / different because…</i></li>
<li>B: Brazil restricted phone use in schools in 2025 (federal law 15.100/2025); use it as a discussion point. Correct the prepositions.</li></ol>""")

    # Page 7
    pc = [("A1 Unit 35", "I can explain rules with must, mustn't, can and can't."), ("A2 Unit 01", "I can ask about appearance, personality, likes and wishes."),
          ("A2 Unit 02", "I can use verb + to, verb + -ing and verb + person + to."), ("A2 Unit 03", "I can describe a place with my senses and use state verbs correctly."),
          ("A2 Unit 04", "I can use adjectives and nouns with the right preposition.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Many people have a fear", "of", "flying."), ("Who is responsible", "for", "the money in your family?"), ("There's a big increase", "in", "online shopping in Brazil."),
          ("Kate is very good", "at", "baking cakes."), ("Is there a solution", "to", "this problem?"), ("My new phone is different", "from", "my old one.")]
    hl = [f'<li value="{i+1}">{a} {A(p, "min-width:12mm")} {c}</li>' for i, (a, p, c) in enumerate(hw)]
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Complete with a preposition.</b></p>
{twocol(hl, 4)}
<p style="margin-top:2mm"><b>2. Call the show (50–75 words).</b> Write what you would say to Dr. Brooks about you and your phone. Use at least four words + prepositions from page 3 (afraid of, tired of, worried about, a solution to…).</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class: the student reads homework 2 as a radio call and you answer as Dr. Brooks. Check every preposition and the -ing forms.</p>""")

    b.extra("Audio scripts", f"""
{sub("04.1", "The radio show: Chicago Talks (slow and natural)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{NAMES[n]}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("04.2", "Phrases")}
<p>{" · ".join(S042)}</p>
{sub("04.3", "Sentences")}
<p>{" ".join(S043)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 04 - Where's my phone")
