# Speak! Bridge A2 - Unit 11 "Party time" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 11", audio_json="audio_a2-unit-11.json", img_dir="img")

PHOTOS = [("A", "blow up the balloons", "balloons"), ("B", "wrap the presents", "wrapping"), ("C", "make the cake", "baking"), ("D", "send the invitations", "card"),
          ("E", "decorate the room", "streamers"), ("F", "order pizza", "pizza"), ("G", "light the candles", "candles"), ("H", "buy a present", "present")]

_r = json.load(open("roteiro.json"))["units"]["a2-unit-11"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["11.1 Surprise party"].split("\n")]
S112 = [x.split(": ", 1)[1] for x in _r["11.2 Repeat words"].split("\n")]
S113 = [x.split(": ", 1)[1] for x in _r["11.3 Repeat sentences"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 11", "Party time", "Planning a party · <b>present perfect with already, yet and still</b>",
                       [("YOU CAN", "check what's done and what's not done yet when you plan an event"),
                        ("LANGUAGE", "Have you made the cake yet? · We've already ordered the pizzas. · I still haven't made it!"),
                        ("PRONUNCIATION", "alREADy · yet /jet/ · surPRISE · balLOONS")])
    when = ["a week before", "the day before", "on the day", "a few minutes before"]
    b.page(f"""{sec(1, "Warm-up: party preparations", "8 min")}
{sub("A", "Look at the photos. Write the phrases under the photos.", "3 min")}
<div class="bank">blow up the balloons · buy a present · decorate the room · light the candles · make the cake · order pizza · send the invitations · wrap the presents</div>
{photo_grid(T, PHOTOS)}
{sub("B", "When is the best time to do each thing? Tell your teacher.", "5 min")}
<div class="bank" style="background:#fff">{" · ".join(when)}</div>
<p class="small">{R("Suggested: a week before: send the invitations, buy a present · the day before: wrap the presents, make the cake · on the day: decorate the room, order pizza, blow up the balloons · a few minutes before: light the candles")}</p>
<p>Have you ever had a surprise party? Have you ever organized one?</p>""",
    22, """<p>A: <b>wrap</b> = cover with gift paper; <b>blow up</b> balloons; <b>light</b> the candles. B: accept any reasonable order.</p>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Party preparations</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Kate and Lucy plan a surprise party for Tom</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Present perfect with already, yet, still (and just)</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>already, yet, still, just · the four uses of the present perfect</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>5 min</td><td>Word stress · checklist questions and answers</td><td>5</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Questions and answers with yet / already · Word builder: birthday phrases</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>A party for your teacher · birthdays in Brazil and the US</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework (50–75 words)</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>It's Tom's birthday. <b>Kate</b> and <b>Lucy</b> are planning a surprise party for him at Sweet Kate. Lucy has bought running shoes (Tom ran the Chicago Marathon, Unit 06), Kate invited the guests and Megan has sent a card from Seattle (Unit 09). The pizzas haven't arrived yet, Kate still hasn't made the cake (a Brazilian carrot cake with chocolate frosting, from Ana's recipe) and they've forgotten the balloons. Lucy's arm is fine now (Unit 07). Fun fact for page 7: the "Happy Birthday" melody comes from "Good Morning to All" (1893) by sisters Mildred and Patty Hill from Kentucky; in 2015 a federal judge in Los Angeles ruled that the copyright claim was not valid, so anyone can sing it for free (NPR, September 2015).</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Word position: students translate word by word and say <i>I haven't yet finished</i> ✗ → <b>I haven't finished yet</b>; <i>I already have done it</i> ✗ → <b>I've already done it</b>; <i>I still not have…</i> ✗ → <b>I still haven't…</b>. They also use <i>still</i> in questions where English uses <i>yet</i>: <i>Have you finished still?</i> ✗ → <b>yet</b>. Note: Americans often use the past simple (<i>Did you eat yet?</i>); accept it, but practice the present perfect.</div>
<div class="box"><h4>AUDIO</h4>Track 11.1 The surprise party (slow and natural) · Track 11.2 Words · Track 11.3 Sentences</div>""")

    # Page 2
    todo = [("buy a present", True), ("invite the guests", True), ("order the pizzas", True), ("make the cake", False), ("clean the tables", True),
            ("move the chairs", True), ("buy the balloons", False), ("blow up the balloons", False)]
    tl = "".join(f"<td style='text-align:center;font-size:8.8pt'>{t}<br>{'☐' if not T else ('<span class=red>✓</span>' if ok else '<span class=red>✗</span>')}</td>" + ("</tr><tr>" if i == 3 else "") for i, (t, ok) in enumerate(todo))
    gaps = [("He's been at school", "since", "eight."), ("I've", "never", "organized a surprise party before."), ("I", "bought", "him a new pair of running shoes last weekend."),
            ("I invited the guests two weeks", "ago", "."), ("She's", "already", "sent a card from Seattle."), ("They haven't arrived", "yet", "."),
            ("No, I", "still", "haven't made it."), ("I've", "just", "cleaned the tables and moved the chairs.")]
    gl = [f'<li value="{i+1}">{a} {A(w, "min-width:16mm")} {c}</li>' for i, (a, w, c) in enumerate(gaps)]
    b.page(f"""{sec(2, "Listening: the surprise party", "10 min")}
<p>It's Tom's birthday, and he doesn't know about the party! Kate and Lucy are at Sweet Kate, checking their list.</p>
{audiocard(["11.1 · SLOW", "11.1 · NATURAL"])}
{sub("A", "Listen. What have they done (✓)? What haven't they done yet (✗)?", "3 min", "11.1 · SLOW")}
<table style="table-layout:fixed;margin-top:0"><tr>{tl}</tr></table>
<p>What's the problem at the end? How will they solve it? {R("They've forgotten to buy the balloons. Lucy will go to the store.")}</p>
{sub("B", "Listen again. Complete with one word.", "5 min", "11.1 · NATURAL")}
{twocol(gl, 5)}
<p class="small">Sentences 3 and 4 use the past simple. Why? {R("They have a finished time: last weekend, two weeks ago.")}</p>""",
    22, """<p>A: ask for full answers: <i>They've already bought the present. They haven't made the cake yet.</i> B: the student predicts first. The Brazilian carrot cake with chocolate frosting is a nice cultural link: ask if the student knows how to make it.</p>""")

    # Page 3
    b.page(f"""{sec(3, "Language focus: already, yet, still", "10 min")}
{sub("A", "Read the sentences from the conversation. Then choose the correct word.", "4 min")}
<div class="bank" style="background:#fff;font-weight:600">We've already ordered the pizzas. · They haven't arrived yet. · Have you made the cake yet? · I still haven't made it! · I've just cleaned the tables.</div>
<ol><li>We use {ch(["already", "yet", "still"], "already")} in positive sentences when something is done.</li>
<li>We use {ch(["already", "yet", "still"], "yet")} in questions and negatives when something isn't done, but we expect it.</li>
<li>We use {ch(["already", "yet", "still"], "still")} in negatives to show it's a problem or a surprise.</li></ol>
{sub("B", "Word position. Write already, yet, still or just.", "3 min")}
<table style="table-layout:fixed;margin-top:0;font-size:9pt"><tr><td>1. goes at the end of the sentence</td><td>{A("yet", "min-width:16mm")}</td></tr>
<tr><td>2. goes between have / has and the participle (two words)</td><td>{A("already, just", "min-width:26mm")}</td></tr>
<tr><td>3. goes before haven't / hasn't</td><td>{A("still", "min-width:16mm")}</td></tr></table>
{sub("C", "Put the word in the correct place.", "3 min")}
<ol><li>I've invited the guests. (already) {R("I've already invited the guests.")}<div class="wline"></div></li>
<li>Has Kate made the cake? (yet) {R("Has Kate made the cake yet?")}<div class="wline"></div></li>
<li>They haven't bought the balloons. (still) {R("They still haven't bought the balloons.")}<div class="wline"></div></li></ol>
<p class="small">More on the next page: <b>Grammar reference</b>.</p>""",
    24, """<ol><li>A: <i>already</i> can also appear in surprised questions: <i>Have you finished already?</i> (so fast!).</li>
<li>B–C: practice position orally with real things: <i>Have you had lunch yet? Have you paid your bills yet?</i></li></ol>""")

    grammar_ref.present_perfect_already_yet(b)

    # Page 4 (now 5)
    b.page(f"""{sub("D", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>I haven't yet finished.</td><td><b>I haven't finished yet.</b></td><td>yet at the end.</td></tr>
<tr><td>I already have done it.</td><td><b>I've already done it.</b></td><td>have + already + participle.</td></tr>
<tr><td>I still not have called her.</td><td><b>I still haven't called her.</b></td><td>still + haven't.</td></tr>
<tr><td>Have you made the cake still?</td><td><b>Have you made the cake yet?</b></td><td>questions = yet.</td></tr>
<tr><td>I've already sent it last week.</td><td><b>I sent it last week.</b></td><td>finished time = past simple.</td></tr>
<tr><td>Congratulations! (on a birthday)</td><td><b>Happy birthday!</b></td><td>remember Unit 06.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "5 min")}
{audiocard(["11.2", "11.3"])}
{sub("A", "Words. Listen and repeat. Underline the stressed syllable.", "2 min", "11.2")}
<table style="table-layout:fixed;margin-top:0"><tr>{"".join(f"<td style='text-align:center'><b>{w}</b></td>" for w in S112)}</tr></table>
<p class="small">{R("alREADy · yet · still · just · surPRISE · balLOONS · decoRAtions · inviTAtions")}</p>
{sub("B", "Sentences. Listen and repeat.", "2 min", "11.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S113)}</div>
<div class="box" style="margin-top:1mm"><h4>YET OR JET?</h4><b>yet</b> = /jet/, like <i>yes</i>. Don't say "jet" /dʒet/ (a plane!). Words ending in <b>-tion</b> are stressed on the syllable before: invi<b>TA</b>tion, decor<b>A</b>tion.</div>""",
    24, """<ol><li>4A: Brazilians often say <i>SURprise</i> and <i>BAlloons</i>: the stress is on the second syllable.</li>
<li>4B: <i>Have you bought his present yet?</i> goes up at the end (yes/no question).</li></ol>""")

    # Page 5 (now 6)
    qa = [("buy the drinks", True), ("wrap the present", False), ("send the invitations", True), ("decorate the room", False), ("choose the music", True), ("make the cake", False)]
    def q(v):
        base = v.split()[0]
        part = {"buy": "bought", "wrap": "wrapped", "send": "sent", "decorate": "decorated", "choose": "chosen", "make": "made"}[base]
        return part + " " + " ".join(v.split()[1:])
    qal = [f'<li value="{i+1}">{v} {"(✓)" if ok else "(✗)"}<div class="wline">{R(f"Have you {q(v)} yet? — " + (f"Yes, we\'ve already {q(v)}." if ok else f"No, we haven\'t {q(v)} yet."))}</div></li>' for i, (v, ok) in enumerate(qa)]
    bp = [("throw", "a party"), ("send", "the invitations"), ("blow out", "the candles"), ("make", "a wish"), ("sing", "Happy Birthday"), ("open", "the presents")]
    bpl = [f'<li value="{i+1}">{A(v, "min-width:16mm")} {n}</li>' for i, (v, n) in enumerate(bp)]
    b.page(f"""{sec(5, "Practice", "8 min")}
{sub("A", "Kate asks Lucy about another party. Write the questions with yet and the answers with already or not… yet.", "5 min")}
{twocol(qal, 4)}
<p class="small">Now say three of them with <b>still</b>: <i>Lucy still hasn't wrapped the present!</i></p>
{sub("B", "Word builder: birthday phrases. Complete with the verbs.", "3 min")}
<div class="bank">blow out · make · open · send · sing · throw</div>
{twocol(bpl, 4)}""",
    22, """<ol><li>A: <i>choose → chosen</i>, <i>send → sent</i> (irregular). The ✓ items use <i>already</i>; the ✗ items use <i>not… yet</i>.</li>
<li>B: <b>throw a party</b> = organize a party. In Brazil and the US: <i>make a wish and blow out the candles</i>.</li></ol>""")

    # Page 6 (now 7)
    items = ["invite the guests", "buy a present", "wrap the present", "buy food and drinks", "make or buy a cake", "decorate the room", "blow up the balloons", "choose the music"]
    it = "".join(f"<tr><td>{x}</td><td style='width:16mm'>☐</td><td></td><td style='width:16mm'>☐</td></tr>" for x in items)
    b.page(f"""{sec(6, "Speaking", "12 min")}
{sub("A", "A party for a friend. You and your teacher are organizing a party. Secretly check (✓) four things you've already done and add a detail (price, color, place). Then ask and answer.", "7 min")}
<table style="table-layout:fixed;margin-top:0;font-size:9pt"><tr><th></th><th>I've done it</th><th>details</th><th>teacher has</th></tr>{it}</table>
<div class="msg" style="max-width:none;padding:1.5mm 4mm;line-height:1.5"><b>Teacher:</b> Have you bought a present yet? <b>You:</b> Yes, I've already bought it. It was 80 reais. <b>Teacher:</b> Oh no, I've just bought one too!</div>
{sub("B", "Birthdays in Brazil and the US.", "5 min")}
<ol><li>What do people eat at birthday parties in Brazil? Have you ever been to a party in another country?</li>
<li>Do you prefer surprise parties or small dinners? Why?</li></ol>
<div class="box sand" style="margin-top:1mm"><h4>DID YOU KNOW?</h4>The melody of "Happy Birthday to You" comes from "Good Morning to All", a song written in 1893 by two sisters from Kentucky, Mildred and Patty Hill. For many years, a company said it owned the song, but in 2015 a US judge decided that the claim was not valid. Today, anyone can sing it for free!</div>""",
    26, """<ol><li>A: compare the two lists and decide what is still missing: <i>We still haven't bought the drinks! Who's going to do it?</i></li>
<li>B: Brazilian parties often have brigadeiros and a big cake; the birthday song has an extra part after the main song. Source for the fun fact: NPR, September 2015.</li></ol>""")

    # Page 7 (now 8)
    pc = [("A2 Unit 06", "I can praise, compliment and congratulate people, and respond politely."), ("A2 Unit 07", "I can talk about accidents that just happened with the present perfect."),
          ("A2 Unit 08", "I can ask about life experiences and give details with the past simple."), ("A2 Unit 09", "I can say how long things have been true with for and since."),
          ("A2 Unit 11", "I can check what's done and not done with already, yet and still.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    ow = [("you / Have / sung / yet / Happy Birthday / ?", "Have you sung Happy Birthday yet?"), ("already / I've / the / up / balloons / blown", "I've already blown up the balloons."),
          ("just / finished / I've / the cake", "I've just finished the cake."), ("haven't / still / They / us / answered", "They still haven't answered us."),
          ("any photos / We / yet / taken / haven't", "We haven't taken any photos yet.")]
    owl = "".join(f"<li><i>{p}</i><div class='wline'>{R(s)}</div></li>" for p, s in ow)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Put the words in order.</b></p>
<ol>{owl}</ol>
<p style="margin-top:2mm"><b>2. A message to a friend (50–75 words).</b> You're organizing a party (or a trip). Tell your friend what you've already done, what you haven't done yet and what you still need help with.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class: ask follow-up questions about the student's message (<i>Have you… yet?</i>). Check word position of <i>already / yet / still</i>.</p>""")

    b.extra("Audio scripts", f"""
{sub("11.1", "The surprise party (slow and natural)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("11.2", "Words")}
<p>{" · ".join(S112)}</p>
{sub("11.3", "Sentences")}
<p>{" ".join(S113)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 11 - Party time")
