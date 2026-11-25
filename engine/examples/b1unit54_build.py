# Speak! Progress B1 - Unit 54 "Sport" (all English) - lean B1 format
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
setup(band="B1 · UNIT 54", audio_json="audio_b1-unit-54.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-54"]
S541 = [l.split(": ", 1) for l in _r["54.1 Gap Year Diaries: my first soccer game"].split("\n")]
S542 = [x.split(": ", 1)[1] for x in _r["54.2 Repeat: the more, the better"].split("\n")]




def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'
    def lines(n):
        return '<div class="wline"></div>' * n
    def g(x):
        return A(x, "min-width:24mm")

    # Page 1 - Warm-up
    cover = cover_html(T, "LEVEL B1 · UNIT 54", "Sport", "Sports, people and places · <b>The more you train, the fitter you get</b>",
                       [("YOU CAN", "talk about sports and compare them in detail"),
                        ("LANGUAGE", "court · field · rink · referee · coach · spectator · foul · draw · the more…, the… · twice as … as"),
                        ("PRONUNCIATION", "rhythm: the MORE, the MERrier · weak as /əz/")])
    rows = [("football (American)", g("ball, helmet, pads"), "field"), ("soccer", "ball", g("field")), ("tennis", g("racket"), "court"),
            (g("golf"), "clubs", "course"), ("swimming", "cap, goggles", g("pool")), ("boxing", g("gloves"), "ring"),
            ("basketball", "ball", g("court")), (g("ice-skating"), "skates", "rink"), ("baseball", g("bat"), "field"), ("skiing", "skis", g("ski slope"))]
    rt = "".join(f"<tr><td>{a}</td><td>{e}</td><td>{p}</td></tr>" for a, e, p in rows)
    bank = ["ball, helmet, pads", "bat", "court", "field", "gloves", "golf", "ice-skating", "pool", "racket", "ski slope"]
    b.page(f"""{sec(1, "Warm-up: sports, equipment and places", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 46, 30)}<div style="flex:1">
{talk(["Are you into sports? Which sports do you play or watch?", "Did you play a sport at school? Which one?"], "START TALKING")}</div></div>
{sub("A", "Complete the table with the words from the box.", "4 min")}
<div class="bank">{" · ".join(bank)}</div>
<table style="font-size:8.5pt;margin:.6mm 0"><tr><th>sport</th><th>equipment</th><th>place</th></tr>{rt}</table>
<p class="small" style="margin:.5mm 0"><b>play</b> + ball games (<i>play soccer</i>) · <b>go</b> + -ing activities (<i>go swimming, go skiing</i>) · <b>do</b> + other activities (<i>do yoga, do judo</i>)</p>""",
    30, """<ol><li>Top box: 2 minutes. Check <i>Are you into sports?</i> (= Do you like sports?).</li>
<li>A: in American English, <i>football</i> is American football and <i>soccer</i> is football; British English uses <i>pitch</i> for a soccer field and <i>ski run</i> for a ski slope. Then quiz: <i>Where do you play basketball? What do you need for boxing?</i> Drill <i>play / go / do</i>.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Gap Year Diaries: Danny's first soccer game in Brazil, with Bruno · true or false · questions · Talk about it",
                      "the more…, the…; faster and faster; just as / twice as / not nearly as … as; much / far / a bit + comparative", "Choose the correct words · complete · Use it (oral)",
                      "the more, the merrier (54.2) · people in sports · which sport? · long turn: a sports event you'll never forget", "Bruno's message to Rafa · rewrite · watch out · writing about a sports event"),
        """The Linguahouse lesson is vocabulary only: sports, equipment and places, people in sports, spectator comments (Which sport?) and a talking point. It has no listening and no grammar, so we added a Gap Year Diaries episode and a new B1 grammar point: advanced comparisons (the more…, the…; faster and faster; twice as … as; not nearly as … as). Story: Danny goes to his first soccer game in Brazil with Bruno (the team is not named). 40,000 spectators; twice as loud as the baseball games Danny went to with his dad. Everyone shouted at the referee (no penalty for a foul); the other team scored first; Bruno's team's captain scored before halftime (one all); the coach changed the tactics; a goal in the last minute (two to one). Danny ate popcorn and bought food three times. He prefers soccer to American football now and wants a team shirt; next time Rafa is coming too. No real clubs, players or statistics are named.""",
        """<i>More you train, more fit you get</i> (→ <i>The more…, the fitter…</i>); <i>two times louder</i> (→ <i>twice as loud as</i>); <i>very more</i> (→ <i>much more</i>). Vocabulary: <i>assist a game</i> (→ <i>watch</i>, a false friend); <i>practice soccer</i> (→ <i>play</i>); <i>the judge</i> (→ <i>the referee</i>). Rhythm: <i>the MORE, the MERrier</i>.""",
        "Track 54.1 Gap Year Diaries: my first soccer game (natural and slow; Danny and Bruno) · Track 54.2 Repeat: the more, the better"))

    # Page 2 - Listening
    tf = [("There were forty thousand spectators.", "T"), ("Danny thinks the game was quieter than baseball.", "F: twice as loud as baseball."),
          ("The referee gave Bruno's team a penalty.", "F: he didn't; Bruno says it was a foul."), ("At halftime the score was one all.", "T"),
          ("Bruno's team scored the winning goal in the last minute.", "T"), ("Danny prefers American football to soccer.", "F: soccer is much more exciting for him.")]
    tfl = "".join(f"<li>{s} <b>T / F</b> {R(a)}</li>" for s, a in tf)
    qs = [("Why was everyone shouting at the referee?", "He didn't give them a penalty for a foul."),
          ("What did the coach do at halftime?", "He changed the tactics."),
          ("What happened when Danny got nervous?", "He ate more and more popcorn; he bought food three times."),
          ("What does Danny want now?", "A team shirt.")]
    ql = "".join(f"<li>{q} {A(a, 'min-width:46mm')}</li>" for q, a in qs)
    b.page(f"""{sec(2, "Listening: my first soccer game", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
<p style="margin:0 0 1mm;font-size:8.8pt">Danny records his podcast in the stadium, right after his first soccer game in Brazil.</p>
{sub("A", "Listen. True (T) or false (F)? Correct the false sentences.", "4 min")}
<ol style="line-height:1.5;font-size:8.6pt;margin:0">{tfl}</ol></div>{img('B', 36, 30)}</div>
{audiocard(["54.1 · NATURAL", "54.1 · SLOW"])}
{sub("B", "Listen again and answer.", "4 min")}
<ol style="line-height:1.5;font-size:8.6pt;margin:0">{ql}</ol>
<p style="margin:.6mm 0;font-size:8.6pt"><b>Think about it:</b> Bruno says "The referee must be blind!" Does he really mean it? {A("no: it's an angry joke; fans often say it when they disagree with a decision", "min-width:20mm")}</p>
<div class="box sand" style="margin:.8mm 0;font-size:8.3pt"><h4>NOTICE: TALKING ABOUT A GAME</h4>score a goal · a foul · a penalty · halftime · one all (= 1–1) · a draw · the winning goal · beat the other team</div>
{talk(["Have you ever been to a game in a stadium? What was it like?", "Which is more exciting for you to watch: soccer or another sport?", "Do you shout at the referee?"])}""",
    35, """<ol><li>A: play the natural version; play the slow one if needed.</li>
<li>B: ask the student to find the comparisons: <i>The more our team wins, the louder…; twice as loud as; faster and faster; the more nervous I got, the more popcorn I ate; as loud as that; weren't nearly as strong; much more exciting; The sooner…, the better; The more, the merrier</i>. They come back on page 3.</li>
<li>In American English, scores are often said <i>two to one</i>; <i>one all</i> or <i>tied at one</i> for 1–1.</li></ol>""")

    # Page 3
    lean.grammar_in_class(b, grammar_ref.comparisons_advanced)

    # Page 4 - Practice
    pc = [("", ["The more", "More"], "The more", "you practice, the better you play."), ("The game got", ["faster and faster", "more fast and fast"], "faster and faster", "."),
          ("It's", ["twice as loud as", "two times louder as"], "twice as loud as", "a baseball game."), ("Soccer is", ["much", "very"], "much", "more exciting than golf for me."),
          ("The second half was just", ["as", "than"], "as", "good as the first."), ("They weren't", ["nearly", "near"], "nearly", "as strong as last year."),
          ("The sooner we leave,", ["the better", "better"], "the better", "."), ("Tickets are getting", ["more and more expensive", "expensiver and expensiver"], "more and more expensive", ".")]
    cl = "".join(f"<li>{a + ' ' if a else ''}{ch(o, r)}{'' if z.startswith('.') else ' '}{z}</li>" for a, o, r, z in pc)
    cp = [("you sleep / well / you feel", "The more you sleep, the better you feel."), ("the game is / long / I get / tired", "The longer the game is, the more tired I get."),
          ("you start / early / you finish", "The earlier you start, the earlier you finish.")]
    cpl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in cp)
    use = ["Compare two sports: which is more exciting to watch? How much more?", "Finish the sentence: The more I…, the more I…",
           "Is anything in your life getting better and better? Worse and worse?", "Is soccer in Brazil just as popular as it was twenty years ago?",
           "Is your city twice as expensive as it was ten years ago?"]
    b.page(f"""{sec(4, "Practice: the more, the better", "10 min")}
{sub("A", "Choose the correct words.", "3 min")}
<ol style="line-height:1.7;font-size:8.6pt;margin:0;columns:2;column-gap:6mm">{cl}</ol>
{sub("B", "Write double comparatives with the words.", "4 min")}
<ol style="line-height:1.45;font-size:8.7pt;margin:0">{cpl}</ol>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    30, """<ol><li>A: 3 minutes. <i>Expensiver</i> doesn't exist: long adjectives use <i>more and more</i>.</li>
<li>B: item 2 can also be <i>the more tired I feel</i>. Point out the word order: <i>the</i> + comparative + subject + verb.</li>
<li>Use it: 3 minutes, all oral. Opinions, not facts: there are no right answers.</li></ol>""")

    # Page 5 - Speaking
    people = ["captain", "coach", "competitor", "manager", "opponent", "referee", "spectator"]
    pdef = {"captain": "leads the team on the field", "coach": "trains a team (fitness and skills)", "competitor": "takes part in a race or competition",
            "manager": "organizes a team and decides on tactics", "opponent": "plays against you or your team", "referee": "controls a game and makes decisions",
            "spectator": "watches a sports event"}
    order = [5, 3, 6, 0, 2, 4, 1]
    pl = "".join(f'<li>{A("a " + people[i], "min-width:22mm")} {pdef[people[i]]}</li>' for i in order)
    com = [("That was definitely a foul! The referee must be blind!", "soccer, basketball, hockey"), ("Another brilliant serve! She's going to win the match.", "tennis, volleyball"),
           ("He's going to get knocked out in the next round.", "boxing, martial arts"), ("Another amazing touchdown!", "American football"),
           ("Come on! One more home run!", "baseball"), ("What a slam dunk!", "basketball")]
    coml = "".join(f'<li>{s} {A(a, "min-width:20mm")}</li>' for s, a in com)
    b.page(f"""{sec(5, "Speaking: talking about sports", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE: TALKING ABOUT SPORTS</h4>
<table style="margin:0;font-size:8.2pt"><tr><th>likes</th><th>teams</th><th>results</th><th>comparing</th></tr>
<tr><td><i>I'm really into… · I'm a big fan of… · I can't stand watching…</i></td><td><i>I root for… · Who do you root for? · We're playing … on Sunday.</i></td><td><i>We won / lost two to one. · It was a draw. · They beat us.</i></td><td><i>It's twice as… · It's not nearly as… · The more…, the…</i></td></tr></table></div>
{audiocard(["54.2"])}
{sub("A", "Listen and repeat. Stress the comparatives: the MORE, the MERrier.", "2 min", "54.2")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S542))}</p>
{sub("B", "People in sports. Write the person.", "3 min")}
<div class="bank" style="font-size:8.6pt;background:#fff">{" · ".join(people)}</div>
<ol style="font-size:8.5pt;line-height:1.5;margin:0;columns:2;column-gap:6mm">{pl}</ol>
{sub("C", "Which sport? A spectator says these things. Which sport is it?", "4 min")}
<ol style="font-size:8.5pt;line-height:1.5;margin:0">{coml}</ol>
{sub("D", "Long turn. Which sports are popular in Brazil? Why? Then tell your teacher about a sports event you'll never forget (live or on TV).", "5 min")}""",
    30, """<ol><li>B: <i>coach</i> and <i>manager</i> overlap in American English; in pro sports, the head coach often decides tactics. C: more than one answer is possible; teach <i>serve, knock out, touchdown, home run, slam dunk</i>.</li>
<li>D comes from the Linguahouse talking point. Opinions only: no statistics needed. Last 3 minutes: wrap-up (two corrections, and ask <i>Can you now talk about sports and compare them?</i>).</li></ol>""")

    # Homework
    pc2 = [(["the better", "better"], "the better"), (["twice as", "two times"], "twice as"), (["nearly", "near"], "nearly"),
           (["louder and louder", "more loud and loud"], "louder and louder"), (["much", "very"], "much"), (["The more", "More"], "The more")]
    p = [ch(o, a) for o, a in pc2]
    rw2 = [("If you eat a lot of popcorn, you feel sick. (The more…)", "The more popcorn you eat, the sicker you feel."),
           ("The tickets cost 100 reais. The shirt costs 200 reais. (twice as … as)", "The shirt is twice as expensive as the tickets."),
           ("The first half was exciting. The second half was exciting too. (just as … as)", "The second half was just as exciting as the first.")]
    rwl2 = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw2)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Bruno invites Rafa to the next game. Choose the correct words.", "")}</div>{img('C', 30, 19)}</div>
<div class="box" style="line-height:1.85;font-size:8.8pt;margin:.5mm 0"><b>Hey Rafa!</b> Are you coming to the game on Sunday? Buy your ticket soon: the sooner, {p[0]}! Danny loved his first game. He says it was {p[1]} loud as baseball. The other team wasn't {p[2]} as good as us, but they scored first. In the second half the fans sang {p[3]}, and we won in the last minute! Watching it in the stadium is {p[4]} more exciting than on TV. {p[5]} we sing, the better we play. See you there! Bruno</div>
{sub("B", "Rewrite the sentences with the words in brackets.", "")}
<ol style="line-height:1.5;font-size:8.7pt;margin:0">{rwl2}</ol>
{lean.watch_out([("I assisted the game on TV.", "I watched the game on TV.", "<i>assist</i> = help; <i>watch</i> a game."), ("I practice soccer on Saturdays.", "I play soccer on Saturdays.", "<i>play</i> ball games; <i>practice</i> = train for something."), ("The judge didn't see the foul.", "The referee didn't see the foul.", "a <i>judge</i> works in a court of law (and in gymnastics or diving).")])}
{lean.writing_task(sub, "Write a post for Danny's podcast page: a sports event you'll never forget.", "I'll never forget the day…", ["where, when and who with", "what happened (score, key moments)", "how you felt", "two comparisons: the more…, twice as…, not nearly as…", "100–150 words"], "I can talk about sports and compare them in detail.")}""",
    25, """<p>Check A and B in 3 minutes at the start of the next class. In B, <i>sicker</i> is correct (or <i>the worse you feel</i>). Read the writing at home and choose two mistakes to discuss in class.</p>""")

    script = "".join(f"<p style='margin:.5mm 0'><b>{s}:</b> {t}</p>" for s, t in S541)
    b.extra("Audio script", f"""
{sub("54.1", "Gap Year Diaries: my first soccer game (natural and slow; Danny and Bruno)")}
<div style="line-height:1.3;font-size:8.3pt">{script}</div>
{sub("54.2", "Repeat: the more, the better")}
<p>{" · ".join(S542)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 54 - Sport")
