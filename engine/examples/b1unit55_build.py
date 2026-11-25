# Speak! Progress B1 - Unit 55 "Strange sports" (all English) - lean B1 format
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
setup(band="B1 · UNIT 55", audio_json="audio_b1-unit-55.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-55"]
S551 = [l.split(": ", 1)[1] for l in _r["55.1 Danny's blog: the Strange Games"].split("\n")]
S552 = [x.split(": ", 1)[1] for x in _r["55.2 Repeat: participle clauses"].split("\n")]


TITLE = "The Strange Games"
PARAS = [S551[0].replace(TITLE + ". ", "", 1)] + S551[1:]


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
    cover = cover_html(T, "LEVEL B1 · UNIT 55", "Strange sports", "Unusual games and competitions · <b>players wearing… · a game played…</b>",
                       [("YOU CAN", "describe unusual sports and explain the rules of a game"),
                        ("LANGUAGE", "pointless · eccentric · steep · barefoot · obstacle course · agility · participle clauses"),
                        ("PRONUNCIATION", "linking in short phrases: players_wearing, tied_between")])
    words = ["alternate", "barefoot", "eccentric", "opponent", "pointless", "shin", "steep", "upside down"]
    defs = {"alternate": "happening one after the other in a regular pattern", "barefoot": "not wearing shoes or socks",
            "eccentric": "strange or unusual (about a person)", "opponent": "a person or team you compete against",
            "pointless": "with no purpose or reason", "shin": "the front part of your leg between the knee and the ankle",
            "steep": "rising or falling at a sharp angle (a hill, a street)", "upside down": "with the top where the bottom should be"}
    order = [4, 7, 0, 6, 1, 3, 5, 2]
    kwl = "".join(f'<li>{A(words[i], "min-width:24mm")} <span style="color:#6b7377">= {defs[words[i]]}</span></li>' for i in order)
    b.page(f"""{sec(1, "Warm-up: crazy sports", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["Look at the photo. What kind of race do you think it is?", "Are there any sports you think are ridiculous or crazy? Why?", "What unusual games did you play as a child?"], "START TALKING")}</div></div>
{sub("A", "Key words. Write the words from the box next to their meanings.", "3 min")}
<div class="bank">{" · ".join(words)}</div>
<ol style="font-size:8.6pt;line-height:1.7;margin:0">{kwl}</ol>
{talk(["Have you ever walked up a very steep street? Where?", "Do you like walking barefoot? Where?", "Do you know anyone eccentric? What do they do?"], "USE THE WORDS")}""",
    30, """<ol><li>Top box: 3 minutes. The photo shows a rubber duck race in a small water channel: people bet on or sponsor a duck. Accept any guess.</li>
<li>A: 4 minutes with the questions. <i>Alternate</i> as an adjective is stressed on the first syllable: /ˈɔːltərnət/.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Danny's blog: the Strange Games festival · true or false · find the words · Talk about it",
                      "participle clauses: -ing (active) and past participle (passive) instead of a relative clause; Inspired by…, …", "Choose the correct form · make it shorter · Use it (oral)",
                      "linking (55.2) · explaining the rules of a game · invent a strange sport · long turn: which sport would you try?", "Dora's festival poster · verbs · watch out · writing: describe a strange sport",
                      listen_label="Reading"),
        """The Linguahouse lesson is an article about real unusual sports from different countries, with dates, places, inventors, speeds and a game from a famous book series. We did not use the article, because we cannot check all those facts, and we avoid brands. Instead, the student reads a post from Danny's blog (also recorded as audio) about a fictional festival, the Strange Games, in a small town in the mountains. Mrs. Lima's cousin Dora, a retired teacher, started it fifteen years ago, inspired by her students' crazy ideas. Events (all invented): suitcase racing through an obstacle course built to look like an airport (Bruno came second); silent soccer, played without words (the referee wore headphones; Rafa lasted six minutes); the hammock relay (teams in hammocks pass a watermelon; Danny's favorite); umbrella fencing, with firefighters spraying water (Danny lost to Lucia, seventy). We kept the Linguahouse key words, the find-the-words phrases, the verbs exercise and the talking points, and added a new B1 grammar point: participle clauses.""",
        """<i>a game playing without words</i> (→ <i>played</i>); <i>Players wear helmets must…</i>; <i>Inspiring by</i> (→ <i>Inspired by</i>). Vocabulary: <i>win the opponents</i> (→ <i>beat</i>); <i>hurted</i> (→ <i>hurt</i>); <i>happens every year since</i> (→ <i>has taken place</i>).""",
        "Track 55.1 Danny's blog: the Strange Games (natural and slow; read by Danny) · Track 55.2 Repeat: participle clauses"))

    # Page 2 - Reading
    text = "".join(f"<p style='margin:0 0 1mm'>{p}</p>" for p in PARAS)
    tf = [("Dora invented the games because she loves extreme sports.", "F: she was inspired by her students' crazy ideas; anyone can play."),
          ("In silent soccer, players who laugh must leave the field.", "T"),
          ("In the hammock relay, teams pass a watermelon.", "T"),
          ("Danny won the umbrella fencing.", "F: he lost to a seventy-year-old woman.")]
    tfl = "".join(f"<li>{s} <b>T / F</b> {R(a)}</li>" for s, a in tf)
    fw = [("got the idea from (P1)", "inspired by"), ("very tiring for the body (P2)", "physically demanding"),
          ("the ability to move quickly and easily (P5)", "agility"), ("with no purpose (P4)", "pointless")]
    fwl = "".join(f"<li>{d} {A(w, 'min-width:26mm')}</li>" for d, w in fw)
    b.page(f"""{sec(2, "Reading: the Strange Games", "12 min")}
{sub("A", "Read Danny's blog post. Which event did Danny like most? Would you go to this festival?", "5 min")}
<div class="box" style="margin:.5mm 0;font-size:8.2pt;line-height:1.36"><div style="float:right;margin:0 0 1mm 2.5mm">{img('B', 34, 23)}</div><b style="font-size:9.4pt;color:#176074">{TITLE}</b><br>{text}</div>
{audiocard(["55.1 · NATURAL", "55.1 · SLOW"])}
<div style="display:flex;gap:4mm"><div style="flex:1.2">
{sub("B", "True (T) or false (F)?", "3 min")}
<ol style="line-height:1.4;font-size:8.3pt;margin:0">{tfl}</ol></div><div style="flex:1">
{sub("C", "Find the words.", "3 min")}
<ol style="line-height:1.5;font-size:8.3pt;margin:0">{fwl}</ol></div></div>""",
    35, """<ol><li>A: the hammock relay. Students can read and listen at the same time.</li>
<li>B and C: then ask the student to find shorter descriptions with <i>-ing</i> or a past participle: <i>competitors carrying, built to look like, a game played, the referee wearing, teams lying, hammocks tied, competitors fighting, Inspired by</i>. They come back on page 3.</li>
<li>Also from the Linguahouse lesson: <i>an obstacle course, a high tolerance for…, spectators, high hopes</i>.</li></ol>""")

    # Page 3
    lean.grammar_in_class(b, grammar_ref.participle_clauses)

    # Page 4 - Practice
    pc = [("Silent soccer is a game", ["played", "playing"], "played", "without words."), ("The woman", ["holding", "held"], "holding", "the umbrella is seventy."),
          ("Players", ["wearing", "wear"], "wearing", "headphones can't hear the crowd."), ("It's a festival", ["organizing", "organized"], "organized", "by a retired teacher."),
          ("", ["Inspired", "Inspiring"], "Inspired", "by her students, Dora invented the games."), ("The man", ["carrying", "carried"], "carrying", "a suitcase came first."),
          ("Hammocks", ["tied", "tying"], "tied", "between trees are used in the relay."), ("Anyone", ["living", "lived"], "living", "in the town can enter.")]
    cl = "".join(f"<li>{a + ' ' if a else ''}{ch(o, r)} {z}</li>" for a, o, r, z in pc)
    rw = [("The players who are lying in the hammocks pass the watermelon.", "The players lying in the hammocks pass the watermelon."),
          ("It's an obstacle course that was designed by teenagers.", "It's an obstacle course designed by teenagers."),
          ("People who watch the games laugh all afternoon.", "People watching the games laugh all afternoon.")]
    rwl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw)
    use = ["Describe someone in this room or in a photo on your phone: the person wearing… / holding…", "Name a dish made with ingredients from your region.",
           "Name a sport played with a ball and a net. And one played on ice.", "Do you know a game invented by children in your family?",
           "Describe a place in your city loved by tourists."]
    b.page(f"""{sec(4, "Practice: players wearing, a game played", "10 min")}
{sub("A", "Choose the correct words.", "3 min")}
<ol style="line-height:1.7;font-size:8.6pt;margin:0;columns:2;column-gap:6mm">{cl}</ol>
{sub("B", "Make the sentences shorter with a participle clause.", "4 min")}
<ol style="line-height:1.45;font-size:8.7pt;margin:0">{rwl}</ol>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    30, """<ol><li>A: 3 minutes. Ask each time: <i>Does the noun do the action (-ing) or is it done to it (past participle)?</i></li>
<li>B: in item 3, <i>People who watch</i> → <i>People watching</i>: a present simple relative clause also becomes -ing.</li>
<li>Use it: 3 minutes, all oral. Accept full relative clauses, then ask for the shorter version.</li></ol>""")

    # Page 5 - Speaking
    card = f"""<div class="box" style="margin-top:1mm;font-size:8.2pt">{R("<b>Teacher's card (B):</b> explain a strange sport first as a model. Example: <i>Backwards cooking: two teams wearing blindfolds make a sandwich, but one person gives the instructions and the other one cooks. You lose a point if you drop something. The winner is the team that finishes first.</i> Then the student invents a sport and explains it. Ask questions: <i>What equipment do you need? How do you win? Is it dangerous?</i>")}</div>""" if T else ""
    b.page(f"""{sec(5, "Speaking: how do you play it?", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE: EXPLAINING THE RULES</h4>
<table style="margin:0;font-size:8.2pt"><tr><th>the aim</th><th>rules</th><th>points and winning</th><th>describing</th></tr>
<tr><td><i>The aim of the game is to… · You play it with…</i></td><td><i>You have to… · You're (not) allowed to… · If you…, you have to…</i></td><td><i>You get a point if… · You lose if… · The winner is the first person to…</i></td><td><i>It's played on / in… · Players wearing… · It was invented by…</i></td></tr></table></div>
{audiocard(["55.2"])}
{sub("A", "Listen and repeat. Link the words: players_wearing, tied_between.", "2 min", "55.2")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S552))}</p>
{sub("B", "Invent a strange sport. Give it a name, then explain the aim, the rules and how to win. Your teacher asks questions.", "6 min")}{card}
<p style="margin:.3mm 0;font-size:8.5pt">Name: {lines(1)}</p>
{sub("C", "Discuss. Which of the Strange Games would you like to try? Which wouldn't you try? Why?", "3 min")}
{sub("D", "Long turn. Tell your teacher about an unusual sport, game or competition from your country or your childhood (real or from a local festival). Use participle clauses.", "4 min")}""",
    30, """<ol><li>B replaces the Linguahouse real-sports matching: the student invents the sport, so there are no facts to check. Push for <i>players wearing…, a game played…</i></li>
<li>C and D come from the Linguahouse talking point. Last 3 minutes: wrap-up (two corrections, and ask <i>Can you now describe an unusual sport and explain its rules?</i>).</li></ol>""")

    # Homework
    pc2 = [(["organized", "organizing"], "organized"), (["Inspired", "Inspiring"], "Inspired"), (["carrying", "carried"], "carrying"),
           (["played", "playing"], "played"), (["lying", "lain"], "lying"), (["wearing", "worn"], "wearing")]
    p = [ch(o, a) for o, a in pc2]
    vb = [("Two people", "were injured", "(injure) in the suitcase race last year."), ("Dora", "invented", "(invent) the hammock relay fifteen years ago."),
          ("The organizers", "switched", "(switch) the festival from Saturday to Sunday because of the rain."), ("Silent soccer", "combines", "(combine) soccer and silence."),
          ("They", "estimated", "(estimate) that two thousand people came last weekend.")]
    vbl = "".join(f'<li>{a} {A(v, "min-width:22mm")} {z}</li>' for a, v, z in vb)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Dora writes the poster for next year's festival. Choose the correct words.", "")}</div>{img('C', 30, 19)}</div>
<div class="box" style="line-height:1.85;font-size:8.8pt;margin:.5mm 0"><b>THE STRANGE GAMES ARE BACK!</b> A festival {p[0]} by people who love to laugh. {p[1]} by my students fifteen years ago, the games are for everyone. Try suitcase racing: competitors {p[2]} heavy suitcases race against the clock. Watch silent soccer, a game {p[3]} without a single word. Join a team {p[4]} in hammocks for the watermelon relay. And don't forget the umbrella fencing: people {p[5]} raincoats are welcome! See you on the first Sunday of June. Dora</div>
{sub("B", "Complete the sentences with the verbs in the correct tense.", "")}
<ol style="line-height:1.55;font-size:8.6pt;margin:0">{vbl}</ol>
{lean.watch_out([("We won the opponents 3–1.", "We beat the opponents 3–1.", "<i>win</i> a game or a prize; <i>beat</i> a person or a team."), ("I fell and I hurted my leg.", "I fell and hurt my leg.", "<i>hurt – hurt – hurt</i> (irregular)."), ("The festival happens every year since 2011.", "The festival has taken place every year since 2011.", "<i>since</i> + a past point → present perfect.")])}
{lean.writing_task(sub, "Write a post for Danny's blog: describe a strange sport (real or invented) and explain how to play it.", "One of the strangest sports I know is…", ["what it is and where it's played", "the aim and the rules", "why it's strange or fun", "at least three participle clauses", "100–150 words"], "I can describe unusual sports and explain the rules of a game.")}""",
    25, """<p>Check A and B in 3 minutes at the start of the next class. B comes from the Linguahouse verbs exercise, with new sentences about the festival. Read the writing at home and choose two mistakes to discuss in class.</p>""")

    script = "".join(f"<p style='margin:.5mm 0'>{t}</p>" for t in S551)
    b.extra("Audio script", f"""
{sub("55.1", "Danny's blog: the Strange Games (natural and slow; read by Danny)")}
<p style="font-size:8.4pt">The audio is the text on page 2, read in full.</p>
{sub("55.2", "Repeat: participle clauses")}
<p>{" · ".join(S552)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 55 - Strange sports")
