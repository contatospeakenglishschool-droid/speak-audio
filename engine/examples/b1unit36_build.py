# Speak! Progress B1 - Unit 36 "Suggesting ideas" (all English) - lean B1 format
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
setup(band="B1 · UNIT 36", audio_json="audio_b1-unit-36.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-36"]
S361 = [l.split(": ", 1) for l in _r["36.1 Planning a long weekend"].split("\n")]
S362 = [x.split(": ", 1)[1] for x in _r["36.2 Repeat: suggestions"].split("\n")]


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
    cover = cover_html(T, "LEVEL B1 · UNIT 36", "Suggesting ideas", "Planning a long weekend · <b>How about going…? · I suggest we go…</b>",
                       [("YOU CAN", "ask for, make, accept and reject suggestions, and plan a short trip with a friend"),
                        ("LANGUAGE", "touristy · stunning · a good deal · Why don't we…? · How about -ing? · I suggest we…"),
                        ("PRONUNCIATION", "intonation in suggestions")])
    kw = [("full of tourists (often negative)", "touristy"), ("full of energy, fun and people", "lively"),
          ("extremely beautiful", "stunning"), ("a price that is lower than usual", "a good deal"),
          ("to reserve a room, a seat or a ticket", "book"), ("to not go to work for a period", "take time off")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:21mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Warm-up: a weekend away", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["Where do people from your city go for a long weekend?", "Do you like planning trips, or do you prefer when someone else plans them?", "Who do you usually travel with? Do you always agree?"], "START TALKING")}</div></div>
{sub("A", "Key words. Write the words from the box next to the definitions.", "3 min")}
<div class="bank">book · a good deal · lively · stunning · take time off · touristy</div>
<div style="font-size:8.7pt">{twocol(kwl, 3)}</div>
{talk(["Name a place in Brazil that is too touristy. Where would you go instead?", "When did you last take time off? What did you do?"], "USE THE WORDS")}""",
    26, """<ol><li>Start with the questions in the top box: 4 minutes.</li>
<li>A: quick check (3 minutes), then the two questions. <i>Touristy</i> is usually negative; <i>touristic</i> is rare in American English.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Danny and Bruno plan a long weekend · answer the questions · classify the phrases · Talk about it",
                      "How about / What about + -ing; Why don't we / Let's / Shall we + verb; suggest + -ing / suggest we + verb; it's worth + -ing",
                      "Complete, choose · Use it: react and suggest (oral)", "Intonation (36.2) · role-play: ask for and give suggestions",
                      "Danny's message to Rafa · rewrite · word choice · writing"),
        """The Linguahouse lesson is a functional lesson: two friends plan a weekend break (Prague or Krakow, hotel or hostel, book flights early), with phrases for asking for, making, accepting and rejecting suggestions. We kept the structure and the phrases, and moved the story to Brazil: Danny wants time off after his tours, Bruno suggests Rio, Danny says it's too crowded and touristy on long weekends (Mrs. Lima's opinion), Bruno suggests Paraty (he went there with his parents as a kid), they invite Rafa (Danny's fellow guide, Unit 8), who needs to check if he can take Monday off, Danny rejects a hostel because he already lives in one, and they decide to rent a small house and book the bus early. The dialogue gives opinions and memories only; it states no real-world facts. The grammar point is the verb patterns after suggestion phrases.""",
        """<i>I suggest to go</i>, <i>How about to take…?</i>, <i>Why we don't go…?</i>, <i>Let's to meet</i>, <i>It's worth to book</i>; word choice: <i>make a trip</i>, <i>mark a hotel</i> for <i>book</i>, <i>turistic</i>. Pronunciation: suggestions with a friendly rising-falling tone; a flat tone sounds bored or rude.""",
        "Track 36.1 Planning a long weekend (natural and slow; Danny and Bruno) · Track 36.2 Repeat: suggestions"))

    # Page 2 - Listening
    qs = [("Why doesn't Danny want to go to Rio?", "It's crowded and touristy on long weekends."), ("Why does Bruno suggest Paraty?", "The old town is stunning and lively at night."),
          ("What does Rafa need to check?", "if he can take Monday off"), ("Why doesn't Danny want a hostel?", "He already lives in a hostel."),
          ("Why should they book the bus early?", "to get a good deal; long weekends sell out")]
    ql = "".join(f"<li>{q} {A(a, 'min-width:44mm')}</li>" for q, a in qs)
    ph = [("Where shall we go?", "ask"), ("Why don't we go to Rio?", "make"), ("I'm not sure about that, to be honest.", "reject"),
          ("Where else do you have in mind?", "ask"), ("What about Paraty?", "make"), ("That sounds like a good idea!", "accept"),
          ("You must be joking!", "reject"), ("I suppose we could do that.", "accept"), ("I suggest we stay at a hostel.", "make"), ("Right, that makes sense.", "accept")]
    phl = "".join(f"<li style='list-style:none'>{A(c, 'min-width:11mm')} <i>{s}</i></li>" for s, c in ph)
    b.page(f"""{sec(2, "Listening: planning a long weekend", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Danny and Bruno are planning a long weekend. Listen and answer.", "4 min")}
<ol style="line-height:1.5;font-size:8.6pt;margin:0">{ql}</ol></div>{img('B', 36, 26)}</div>
{audiocard(["36.1 · NATURAL", "36.1 · SLOW"])}
{sub("B", "Are the phrases asking for, making, accepting or rejecting a suggestion? Write ask, make, accept or reject.", "3 min")}
<ul style="line-height:1.5;font-size:8.7pt;margin:0;padding-left:2mm;columns:2">{phl}</ul>
{talk(["Which phrase is a strong no? Which one is a yes, but not very happy?", "Would you choose Rio, Paraty, a hotel, a hostel or a house? Why?", "Where would you go on your ideal weekend break? Why?"])}""",
    30, """<ol><li>A: play the natural version; play the slow one if needed. 6 minutes.</li>
<li>B: the student can check with the audio script. Strong no: <i>You must be joking!</i> Unenthusiastic yes: <i>I suppose we could do that.</i></li>
<li>Talk about it: 5 minutes (the Linguahouse talking point). Note the forms after each phrase for page 3.</li></ol>""")

    # Page 3
    lean.grammar_in_class(b, grammar_ref.suggestion_patterns)

    # Page 4 - Practice
    fs = [("How about", "take", "the bus at night?", "taking"), ("Why don't we", "ask", "Rafa?", "ask"), ("I suggest we", "stay", "in a small house.", "stay"),
          ("It might be worth", "book", "early.", "booking"), ("Bruno suggested", "rent", "a house.", "renting")]
    fsl = "".join(f'<li>{a} {A(ans, "min-width:18mm")} ({v}) {c}</li>' for a, v, c, ans in fs)
    use = ["&ldquo;I want to learn English faster, so I'll only study the night before class.&rdquo;", "&ldquo;I need money, so I'm going to try my luck at a casino.&rdquo;",
           "&ldquo;I'm exhausted, so I'll drink five coffees and work all night.&rdquo;", "&ldquo;It's going to rain, so I'll take an umbrella.&rdquo;",
           "&ldquo;I want to get fit, so I'll run a marathon next week.&rdquo;"]
    b.page(f"""{sec(4, "Practice: suggestions and verb patterns", "10 min")}
{sub("A", "Complete with the correct form of the verb in brackets.", "4 min")}
<ol style="line-height:1.75;font-size:8.9pt;margin:0">{fsl}</ol>
{sub("B", "Choose.", "2 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0"><li>I suggest {ch(["to go", "going"], "going")} to Paraty.</li>
<li>Let's {ch(["to meet", "meet"], "meet")} at the bus station.</li>
<li>What about {ch(["to call", "calling"], "calling")} Rafa?</li></ol>
<div class="box sand"><h4>RULE</h4><b>Why don't we / Let's / Shall we / could</b> + base form · <b>How about / What about / It's worth</b> + -ing · <b>suggest</b> + -ing or <b>suggest we</b> + base form · never <i>suggest to</i>. See the <b>Grammar reference</b> on page 3.</div>
<p style="margin:1mm 0 0;font-size:8.6pt">Describe each idea (<i>a bright / sensible / original / crazy / dumb / terrible idea</i>) and suggest something better.</p>
{talk(use, "USE IT: REACT AND SUGGEST")}""",
    24, """<ol><li>A–B: 6 minutes.</li>
<li>Use it: 4 minutes, all oral. Model: <i>That's a crazy idea! Why don't you study a little every day?</i> Item 4 is a sensible idea; the student agrees and adds a suggestion. The idea adjectives come from the Linguahouse lesson.</li></ol>""")

    # Page 5 - Speaking
    si = ["a birthday present for a friend", "which new phone to buy", "what to do with R$50,000", "where to take an old friend you haven't seen in years",
          "a series to watch this weekend", "what to do on a free day tomorrow", "how to get up earlier for a new job", "you aren't happy with your job"]
    sl = "".join(f"<li>{x}</li>" for x in si)
    b.page(f"""{sec(5, "Speaking: I need some ideas!", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.3pt"><tr><th>asking</th><th>making</th><th>accepting</th><th>rejecting</th></tr>
<tr><td><i>What do you suggest? · What shall I…? · What do you have in mind?</i></td><td><i>Why don't you…? · How about -ing? · I was thinking about… · I suggest you…</i></td><td><i>That sounds like a good idea. · That makes sense. · It might be worth trying. · I suppose I could.</i></td><td><i>I'm not sure about that. · I don't really think that's a good idea. · You must be joking!</i></td></tr></table></div>
{audiocard(["36.2"])}
{sub("A", "Listen and repeat. Sound friendly: your voice goes up and then down.", "4 min", "36.2")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S362))}</p>
{sub("B", "Choose a situation and ask your teacher for suggestions. Reject two ideas with a reason and accept one. Then change roles: your teacher chooses a situation and you make suggestions.", "14 min")}
<ol style="line-height:1.4;font-size:8.8pt;margin:0;columns:2">{sl}</ol>
{talk(["Who do you ask for advice when you need ideas? Why that person?", "What's the best suggestion anyone has ever given you?"], "TALK ABOUT IT")}""",
    32, """<ol><li>A: a friendly rising-falling tone on the main word (<i>Why don't we go to PAraty?</i>); a flat tone sounds bored or rude.</li>
<li>B: do three or four rounds, changing roles. When you make suggestions, use a mix of forms; when the student rejects, ask <i>Why not?</i> Last 3 minutes: wrap-up (two corrections, and ask <i>Can you now ask for, make, accept and reject suggestions?</i>).</li></ol>""")

    # Homework
    pc = [(["come", "coming"], "come"), (["to rent", "renting"], "renting"), (["meet", "meeting"], "meeting"),
          (["buy", "to buy"], "buy"), (["asking", "to ask"], "asking")]
    p = [ch(o, a) for o, a in pc]
    rw = [("Let's take the night bus. (How about)", "How about taking the night bus?"),
          ("We should book a table. (I suggest we)", "I suggest we book a table."),
          ("Asking Mrs. Lima for ideas is a good idea. (It's worth)", "It's worth asking Mrs. Lima for ideas.")]
    rwl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Danny writes to Rafa about the long weekend. Choose the correct words.", "")}</div>{img('C', 28, 18)}</div>
<div class="box" style="line-height:1.85;font-size:8.8pt;margin:.5mm 0"><b>Hey Rafa!</b><br>Bruno and I are planning a trip to Paraty for the long weekend. Why don't you {p[0]} with us? Bruno suggested {p[1]} a small house, so it won't be expensive. How about {p[2]} at the bus station on Friday night? I suggest we {p[3]} the tickets this week, because they sell out fast. And it's worth {p[4]} the boss about Monday today! Let me know. Danny</div>
{sub("B", "Rewrite the sentences with the words in brackets.", "")}
<ol style="line-height:1.5;font-size:8.7pt;margin:0">{rwl}</ol>
{lean.watch_out([("We're going to make a trip to Paraty.", "We're going to take a trip / go on a trip to Paraty.", "<i>take</i> or <i>go on</i> a trip, not <i>make</i>."), ("I'll mark the hotel today.", "I'll book the hotel today.", "<i>book</i> = reserve; <i>mark</i> = put a sign on something."), ("The town is very turistic.", "The town is very touristy.", "<i>touristy</i> = full of tourists (often negative).")])}
{lean.writing_task(sub, "Write a message to a friend and suggest a weekend break. Where? How will you get there? Where will you stay? What will you do?", "Hi …! I have an idea for the long weekend.", ["a place and why", "transport and accommodation", "three different suggestion phrases", "a plan B if your friend says no", "100–150 words"], "I can ask for, make, accept and reject suggestions.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class. Read the writing at home and choose two mistakes to discuss in class.</p>""")

    script = "".join(f"<p style='margin:.5mm 0'><b>{n}:</b> {l}</p>" for n, l in S361)
    b.extra("Audio script", f"""
{sub("36.1", "Planning a long weekend (natural and slow; Danny and Bruno)")}
<div style="line-height:1.3;font-size:8.6pt">{script}</div>
{sub("36.2", "Repeat: suggestions")}
<p>{" · ".join(S362)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 36 - Suggesting ideas")
