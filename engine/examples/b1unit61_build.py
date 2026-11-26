# Speak! Progress B1 - Unit 61 "Habits" (all English) - lean B1 format
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
setup(band="B1 · UNIT 61", audio_json="audio_b1-unit-61.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-61"]
S611 = [l.split(": ", 1)[1] for l in _r["61.1 Danny's blog: eight habits I picked up in Brazil"].split("\n")]
S612 = [x.split(": ", 1)[1] for x in _r["61.2 Repeat: habits"].split("\n")]


TITLE = "Eight habits I picked up in Brazil"
INTRO = S611[0].replace(TITLE + ". ", "", 1)
PARAS = S611[1:]


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
    cover = cover_html(T, "LEVEL B1 · UNIT 61", "Habits", "Good habits, bad habits · <b>she'll always ask… · I'd buy… · I keep checking…</b>",
                       [("YOU CAN", "talk about good and bad habits, now and in the past, and plan to change one"),
                        ("LANGUAGE", "binge-watch · snack · put off · early riser · give up · will / would for habits · always + -ing · keep + -ing"),
                        ("PRONUNCIATION", "contractions: she'll, I'd, he's always")])
    bad = ["binge-watching TV series", "biting your nails", "buying things you don't need", "checking your phone all the time", "eating too fast",
           "interrupting people", "putting things off", "snacking on junk food", "staying up too late", "swearing"]
    b.page(f"""{sec(1, "Warm-up: bad habits", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["Look at the photo. What is she doing? Why do people do this?", "Do you think you have any bad habits? Which ones?", "Is it easier to start a good habit or to stop a bad one?"], "START TALKING")}</div></div>
{sub("A", "Rank these bad habits from 1 (the worst) to 10 (not so bad). Then compare with your teacher and explain your top three.", "4 min")}
<ol style="font-size:8.7pt;line-height:1.75;margin:0;columns:2;column-gap:6mm;list-style:none;padding-left:0">{"".join(f"<li>☐ {h}</li>" for h in bad)}</ol>
{talk(["Which of these habits do you have? Be honest!", "Which habit annoys you most in other people?", "Can you think of two more bad habits?"], "USE THE WORDS")}""",
    30, """<ol><li>Top box: 3 minutes. The photo shows a woman biting a pencil while she works.</li>
<li>A comes from the Linguahouse bad habits ranking. There is no right answer. Point out that every habit is in the -ing form: an -ing form can be the subject of a sentence (<i>Biting your nails is a bad habit.</i>). <i>Binge-watch</i> = watch many episodes one after another; <i>put off</i> = delay.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Danny's blog: eight habits I picked up in Brazil · match the headings · true or false · find the words",
                      "habits: will / won't (typical behavior), be always + -ing, keep + -ing, used to vs would for past habits", "Choose the correct form · rewrite · Use it (oral)",
                      "contractions (61.2) · talking about habits and changes · a 30-day habit plan · long turn: a habit you changed", "verb + -ing or to (avoid, risk, promise…) · watch out · writing: habits I'd like to change",
                      listen_label="Reading"),
        """The Linguahouse lesson is a general article with ten good habits (wake up early, set goals, exercise, live within your means…) and a grammar focus on verb + -ing or to, which the student already studied (A2 and B1 verb patterns). We replaced the article with a post from Danny's blog (also recorded as audio): eight good habits he picked up in Brazil from the people around him. Ana calls him at 6:01 for his 7 a.m. classes; back home he'd buy things on sale, now he saves for the Amazon trip; Mrs. Lima will put rice, beans and salad on the table and won't accept no; Bruno is always telling him to get out of the city (the Pantanal); Bruno kept inviting him to run with Pipoca; Grandma Lourdes (97) does a crossword every morning; Rafa's music evening (Danny now reads on Thursday evenings); his grandfather would say "Stop worrying about tomorrow". Worst habit: he keeps checking his phone at dinner. We kept the Linguahouse ranking of bad habits, the heading matching, the verb + -ing or to exercise (homework) and the talking points, and added a new B1 grammar point: habits with will, would, always + -ing and keep + -ing.""",
        """<i>I use to wake up at six</i> (now; → <i>I usually wake up</i>); <i>I'm used to drink coffee</i> (→ <i>I usually drink</i>); <i>I would live in Chicago</i> (→ <i>used to live</i>); <i>He always is complaining</i> (→ <i>is always</i>). Vocabulary: <i>stop to smoke</i> (→ <i>stop smoking</i>); <i>quit of sugar</i> (→ <i>quit / give up sugar</i>).""",
        "Track 61.1 Danny's blog: eight habits I picked up in Brazil (natural and slow; read by Danny) · Track 61.2 Repeat: habits"))

    # Page 2 - Reading
    heads = ["Eat healthily", "Exercise", "Live in the present", "Live to learn", "Live within your means", "Make time for yourself", "Reconnect with nature", "Wake up early"]
    order = [7, 4, 0, 6, 1, 3, 5, 2]
    text = "".join(f"<p style='margin:0 0 .8mm'><b>{i+1}</b> {A(heads[order[i]], 'min-width:30mm')} {p}</p>" for i, p in enumerate(PARAS))
    tf = [("Danny used to have an extra hour in the morning.", "F: he never used to have it."),
          ("Mrs. Lima lets guests skip meals if they aren't hungry.", "F: she won't accept \"I'm not hungry.\""),
          ("Danny didn't miss his phone in the Pantanal.", "T"),
          ("Danny has stopped checking his phone at dinner.", "F: it's still his worst habit.")]
    tfl = "".join(f"<li>{s} <b>T / F</b> {R(a)}</li>" for s, a in tf)
    fw = [("a person who gets up early (P1)", "an early riser"), ("cheaper than usual (P2)", "on sale"),
          ("eating small amounts between meals (P3)", "snacking"), ("turn off (P7)", "switch off")]
    fwl = "".join(f"<li>{d} {A(w, 'min-width:22mm')}</li>" for d, w in fw)
    b.page(f"""{sec(2, "Reading: eight good habits", "12 min")}
{sub("A", "Read Danny's blog post. Write a heading for each paragraph.", "5 min")}
<div class="bank" style="font-size:8.3pt">{" · ".join(heads)}</div>
<div class="box" style="margin:.5mm 0;font-size:8pt;line-height:1.33"><div style="float:right;margin:0 0 1mm 2.5mm">{img('B', 34, 23)}</div><b style="font-size:9.4pt;color:#176074">{TITLE}</b><br><i>{INTRO}</i>{text}</div>
{audiocard(["61.1 · NATURAL", "61.1 · SLOW"])}
<div style="display:flex;gap:4mm"><div style="flex:1.2">
{sub("B", "True (T) or false (F)?", "3 min")}
<ol style="line-height:1.4;font-size:8.3pt;margin:0">{tfl}</ol></div><div style="flex:1">
{sub("C", "Find the words.", "3 min")}
<ol style="line-height:1.5;font-size:8.3pt;margin:0">{fwl}</ol></div></div>""",
    30, """<ol><li>A comes from the Linguahouse heading matching (8 of its 10 headings). Students can read and listen at the same time.</li>
<li>After C, ask the student to find how Danny talks about habits: <i>she'll always ask, I never used to have, I'd buy, will put / won't accept, is always telling, kept inviting, would always say, I keep checking, is always complaining</i>. They come back on page 3.</li></ol>""")

    # Page 3
    lean.grammar_in_class(b, grammar_ref.habits_will_would)

    # Page 4 - Practice
    pc = [("When I was a child, I", ["will", "would"], "would", "spend hours at my grandmother's."), ("I", ["used to have", "would have"], "used to have", "a dog called Max."),
          ("Bruno", ["always is", "is always"], "is always", "telling me to run."), ("My phone", ["keeps ringing", "keeps to ring"], "keeps ringing", "!"),
          ("These days, Ana", ["would", "will"], "will", "always call at 6:01."), ("I", ["use to", "usually"], "usually", "drink coffee in the morning."),
          ("She", ["is constantly", "constantly is"], "is constantly", "checking her messages."), ("We", ["didn't used to", "didn't use to"], "didn't use to", "eat breakfast.")]
    cl = "".join(f"<li>{a} {ch(o, r)}{'' if z == '!' else ' '}{z}</li>" for a, o, r, z in pc)
    rw = [("My brother interrupts me all the time. It's so annoying! (always)", "My brother is always interrupting me."),
          ("When I was a teenager, I played video games every night. (would)", "When I was a teenager, I would play video games every night."),
          ("I check my phone again and again. I can't stop! (keep)", "I keep checking my phone.")]
    rwl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw)
    use = ["What would you do on Sundays when you were a child?", "Is anyone you know always doing something annoying? What?",
           "What will you typically do when you get home in the evening?", "What do you keep forgetting?",
           "What did you use to do that you don't do anymore?"]
    b.page(f"""{sec(4, "Practice: she'll always…, I'd…, I keep…", "10 min")}
{sub("A", "Choose the correct words.", "3 min")}
<ol style="line-height:1.7;font-size:8.6pt;margin:0;columns:2;column-gap:6mm">{cl}</ol>
{sub("B", "Rewrite the sentences with the word in brackets.", "4 min")}
<ol style="line-height:1.45;font-size:8.7pt;margin:0">{rwl}</ol>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    30, """<ol><li>A: 3 minutes. Item 2: <i>have</i> a dog is a state, so <i>would</i> is not possible. Item 5: <i>will</i> for a present habit, <i>would</i> for a past one.</li>
<li>B: in item 2, <i>I'd play</i> is the natural contraction.</li>
<li>Use it: 3 minutes, all oral. Listen for <i>I use to</i> about the present and correct it.</li></ol>""")

    # Page 5 - Speaking
    b.page(f"""{sec(5, "Speaking: change one habit", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE: TALKING ABOUT HABITS AND CHANGES</h4>
<table style="margin:0;font-size:8.2pt"><tr><th>habits</th><th>changes</th><th>plans</th><th>encouraging</th></tr>
<tr><td><i>I tend to… · I've got into the habit of -ing · I can't help -ing</i></td><td><i>I've given up… · I've cut down on… · I've taken up…</i></td><td><i>I've decided to… · I'm going to try -ing · I'll avoid -ing</i></td><td><i>Why don't you…? · Start small. · Don't give up!</i></td></tr></table></div>
{audiocard(["61.2"])}
{sub("A", "Listen and repeat. Use the contractions: she'll, I'd, he's always.", "2 min", "61.2")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S612))}</p>
{sub("B", "A 30-day plan. Choose one bad habit to stop and one good habit to start. Plan it with your teacher: what exactly will you do, when, and what will you avoid?", "6 min")}
<table style="font-size:8.4pt;margin:.5mm 0"><tr><th style="width:38mm"></th><th>bad habit to stop</th><th>good habit to start</th></tr>
<tr><td>the habit</td><td></td><td></td></tr><tr><td>when / where it happens</td><td></td><td></td></tr><tr><td>my plan (I'll… / I'll avoid…)</td><td></td><td></td></tr><tr><td>who can help me</td><td></td><td></td></tr></table>
{sub("C", "Discuss. Which of Danny's eight habits do you have? Which is the hardest? Do goals help you achieve things?", "3 min")}
{sub("D", "Long turn. Tell your teacher about a habit you changed (or tried to change). What would you do before? What happened? Did you succeed?", "4 min")}""",
    30, """<ol><li>B: model first with a habit of your own. Push for <i>I'll avoid -ing, I've decided to, I'm going to try -ing</i>. In the next classes, ask how the plan is going.</li>
<li>C and D come from the Linguahouse talking points. Last 3 minutes: wrap-up (two corrections, and ask <i>Can you now talk about habits, now and in the past?</i>).</li></ol>""")

    # Homework
    vb = ["avoid", "decide", "miss", "promise", "risk", "suggest"]
    vs = [("Rafa has", "promised", "to check every message before he shares it."), ("Doctors", "suggest", "cutting down on sugar."),
          ("If you", "decide", "to stop a bad habit, start small."), ("If you don't wear sunscreen, you", "risk", "getting a bad sunburn."),
          ("Many people", "avoid", "going to the dentist because they're scared."), ("Danny", "misses", "eating his mom's pancakes on Sundays.")]
    vsl = "".join(f'<li>{a} {A(v, "min-width:22mm")} {z}</li>' for a, v, z in vs)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Verb + -ing or to. Complete with the verbs from the box in the correct form. Then underline the -ing form or to + verb that follows.", "")}</div>{img('C', 30, 19)}</div>
<div class="bank">{" · ".join(vb)}</div>
<ol style="line-height:1.6;font-size:8.6pt;margin:0">{vsl}</ol>
<div class="box sand" style="margin:1mm 0;font-size:8.3pt"><b>Remember:</b> <b>to</b> + verb usually after <i>decide, promise, want, plan</i> (the action comes after); <b>-ing</b> after <i>avoid, risk, miss, suggest, enjoy, give up, put off</i>, after prepositions (<i>before trying</i>) and as a subject (<i>Smoking is bad for you</i>).</div>
{lean.watch_out([("I use to wake up at six.", "I usually wake up at six.", "<i>used to</i> is only for the past; for now use <i>usually</i>."), ("I need to stop to smoke.", "I need to stop smoking.", "<i>stop -ing</i> = quit; <i>stop to</i> = stop in order to do something."), ("I quit of sugar.", "I quit sugar. / I gave up sugar.", "<i>quit</i> and <i>give up</i> take no <i>of</i>.")])}
{lean.writing_task(sub, "Write a post for Danny's blog: two habits you'd like to change and how you'll do it.", "I'm always -ing, and it drives everyone crazy…", ["one bad habit and one good habit", "what you would do in the past", "your plan (I've decided to… / I'll avoid…)", "100–150 words"], "I can talk about good and bad habits, now and in the past, and plan to change one.")}""",
    25, """<p>Check A in 3 minutes at the start of the next class. It comes from the Linguahouse verb + -ing or to exercise, with new sentences. Read the writing at home and choose two mistakes to discuss in class.</p>""")

    b.extra("Audio script", f"""
{sub("61.1", "Danny's blog: eight habits I picked up in Brazil (natural and slow; read by Danny)")}
<p style="font-size:8.4pt">The audio is the text on page 2, read in full.</p>
{sub("61.2", "Repeat: habits")}
<p>{" · ".join(S612)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 61 - Habits")
