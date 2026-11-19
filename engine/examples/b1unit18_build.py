# Speak! Progress B1 - Unit 18 "Sustainable fashion" (all English) - lean B1 format (rebuilt 2026-11-19)
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
setup(band="B1 · UNIT 18", audio_json="audio_b1-unit-18.json", img_dir="img")
_r = json.load(open("roteiro.json"))["units"]["b1-unit-18"]
_L = [l.split(": ", 1)[1] for l in _r["18.1 The real cost of cheap clothes"].split("\n")]
PARAS = _L[1:]
S182 = [x.split(": ", 1)[1] for x in _r["18.2 Repeat: word stress"].split("\n")]
for k, v in {"two thousand fifteen": "2015", "two thousand thirteen": "2013", "two thousand": "2000", "April twenty-fourth": "April 24", "One thousand one hundred thirty-four": "1,134", "one percent": "1%", "thirty times": "30 times"}.items():
    PARAS = [p.replace(k, v) for p in PARAS]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'

    # 1 Warm-up
    cover = cover_html(T, "LEVEL B1 · UNIT 18", "Sustainable fashion", "Fast fashion and its real cost · <b>the passive: is being made, has been signed, can be repaired</b>",
                       [("YOU CAN", "understand an article about the fashion industry and discuss solutions"),
                        ("LANGUAGE", "a garment · synthetic · a consumer · a landfill · sustainable · wear out · hand down · swap"),
                        ("PRONUNCIATION", "word stress: sustainable, environment, synthetic")])
    kw = [("an item of clothing", "a garment"), ("made with chemicals, not natural", "synthetic"), ("a person who buys things for personal use", "a consumer"),
          ("a place where garbage is buried", "a landfill"), ("the lowest salary you can legally receive", "the minimum wage"),
          ("not damaging to the environment, so it can continue for a long time", "sustainable")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:22mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Warm-up: what's in your closet?", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["How often do you buy new clothes? Where?", "What do you do with clothes you don't wear anymore?", "Do you check where your clothes are made?"], "START TALKING")}</div></div>
{sub("A", "Key words. Write the words from the box next to the definitions.", "3 min")}
<div class="bank">a consumer · a garment · a landfill · the minimum wage · sustainable · synthetic</div>
<div style="font-size:8.6pt">{twocol(kwl, 3)}</div>
{talk(["Look at the label of something you're wearing. What's it made of? Where was it made?", "Are you a careful consumer? Why or why not?"], "USE THE WORDS")}""",
    26, """<ol><li>Top box: <i>closet</i> is American English (British: <i>wardrobe</i>). <i>Fast fashion</i> = cheap clothes made quickly to follow trends.</li>
<li>Last box: model the passive: <i>It's made of cotton. It was made in Vietnam.</i></li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Article: the real cost of cheap clothes (verified facts) · guess the numbers · Talk about it", "The passive: other tenses and modals",
                      "Complete from the article · choose the rule · Use it (oral)", "Functional language · word stress (18.2) · rank the solutions",
                      "Lucy's campus clothes swap · the life of clothes · word choice · writing", "Reading"),
        'The Linguahouse lesson uses a 2019 UK opinion article on fashion waste. We wrote an original article, read by the Host (track 18.1), with facts checked in current sources. Verified facts: clothing production about doubled between 2000 and 2015, while each item was worn fewer times; the equivalent of one garbage truck of textiles is landfilled or burned every second; less than 1% of the material used for clothing is recycled into new clothing (Ellen MacArthur Foundation, <i>A New Textiles Economy</i>, 2017; <i>Circular Business Models</i>, 2021). Polyester is a synthetic fabric made from oil. The Rana Plaza building collapsed on April 24, 2013, in Savar, near Dhaka (Bangladesh); 1,134 people died and about 2,000–2,500 were injured; afterward, an agreement on fire and building safety was signed by international brands and factories were inspected. The "30 times" test is presented as advice, not a statistic. In the homework, Lucy (Chicago) writes about a clothes swap at her university.', 'Students confuse <i>been</i> and <i>being</i> (<i>are been made</i>), forget <i>be</i> after modals (<i>it can recycled</i>), and say <i>fabric</i> for <i>factory</i>, <i>reform</i> for <i>alter / fix</i>, and <i>costume</i> for <i>clothes</i>. Word stress: <i>susTAINable, enVIronment, synTHEtic</i>.',
        "Track 18.1 The real cost of cheap clothes (natural and slow) · Track 18.2 Repeat: word stress"))

    # 2 Reading
    bq = [("Between 2000 and 2015, clothing production…", ["fell", "about doubled", "grew ten times"], "about doubled"),
          ("Polyester is made from…", ["oil", "rubber", "leaves"], "oil"),
          ("How many people died in the Rana Plaza collapse?", ["about 400", "about 1,100", "about 2,100"], "about 1,100"),
          ("How much of the material used for clothes is recycled into new clothes?", ["less than 1%", "about 15%", "about half"], "less than 1%")]
    bql = "".join(f'<li>{q} {ch(o, a)}</li>' for q, o, a in bq)
    art = "".join(f'<p style="margin:0 0 .8mm"><b style="color:#176074">{i+1}</b> {p}</p>' for i, p in enumerate(PARAS))
    b.page(f"""{sec(2, "Reading: the real cost of cheap clothes", "12 min")}
{sub("A", "Before you read. Guess the answers. Then read the article and check.", "4 min")}
<ol style="line-height:1.45;font-size:8.4pt;margin:0">{bql}</ol>
<div class="box" style="margin:.5mm 0 0;font-size:7.9pt;line-height:1.32;column-count:2;column-gap:4mm"><b style="font-size:9.5pt">The real cost of cheap clothes</b><br>{art}</div>
<div style="display:flex;gap:3mm;align-items:center;margin-top:1mm"><div style="flex:1">{audiocard(["18.1 · NATURAL", "18.1 · SLOW"])}</div>{img('B', 36, 20)}</div>
{talk(["&ldquo;The most sustainable clothes are the ones that are already in your closet.&rdquo; What does the writer mean?", "Would the &ldquo;30 times&rdquo; test change the way you shop?", "Which fact in the article surprised you most?"])}""",
    26, """<ol><li>A: 6 minutes. Let the student guess first; they can read and listen (18.1). All figures are real (see the story box). Treat Rana Plaza with care: it is a tragedy, not a curiosity.</li>
<li>Talk about it: 6 minutes. 1: the best option is to wear what we already have. <i>Upcycle</i> = turn old things into something new and better.</li></ol>""")

    # 3 Grammar reference
    lean.grammar_in_class(b, grammar_ref.passive_tenses_modals)

    # 4 Practice
    fs = [("Every second, one garbage truck of textiles ___ or sent to landfill. (burn)", "is burned"),
          ("An agreement on factory safety ___ by many brands. (sign)", "has been signed"), ("Clothes ___, swapped, sold or given away. (can / repair)", "can be repaired"),
          ("Will it ___ at least 30 times? (wear)", "be worn")]
    fsl = "".join(f"<li><i>{s.replace('___', A(a, 'min-width:24mm'))}</i></li>" for s, a in fs)
    use = ["Where was the shirt you're wearing made?", "What is being built or changed in your neighborhood right now?", "What has been done in your city to help the environment?",
           "What should be done about fast fashion?", "Name something in your home that can be repaired, not thrown away."]
    b.page(f"""{sec(4, "Practice: the passive", "10 min")}
{sub("A", "Complete the sentences from the article with the passive form of the verbs.", "3 min")}
<ol style="line-height:1.85;font-size:8.9pt;margin:0">{fsl}</ol>
{sub("B", "Choose.", "1 min")}
<p style="margin:.3mm 0;font-size:8.9pt;line-height:1.7">New clothes are {ch(["been", "being"], "being")} produced. &nbsp;·&nbsp; Factories have {ch(["been", "being"], "been")} inspected. &nbsp;·&nbsp; It can {ch(["be", "to be"], "be")} recycled.</p>
<div class="box sand"><h4>RULE</h4>Passive = <b>be + past participle</b>; only <b>be</b> changes: <i>is made · is <b>being</b> made · was made · has <b>been</b> made · will <b>be</b> made · can / should / must <b>be</b> made</i>. See the <b>Grammar reference</b> on page 3.</div>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    24, """<ol><li>A–B: 4 minutes. Write <i>be / being / been</i> on the board: which comes after <i>is</i>, after <i>has</i>, after <i>can</i>?</li>
<li>Use it: 6 minutes, all oral. Correct <i>are been made</i> and <i>it can recycled</i> every time.</li></ol>""")

    # 5 Speaking
    sol = ["Clothes repair services should be made cheaper by the government.", "A small tax should be paid on every new garment.", "Repairing clothes should be taught at school.",
           "Second-hand clothes should be bought before new ones.", "Unsold clothes should never be destroyed.", "Every garment should be worn at least 30 times."]
    soll = "".join(f"<li>{x} <span style='color:#999'>___</span></li>" for x in sol)
    sl = " &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {R(y) if T else x}" for i, (x, y) in enumerate(zip(S182, ["susTAINable", "enVIronment", "conSUMer", "synTHEtic", "polyESter", "reCYcle", "GARment", "LANDfill", "UPcycle", "MInimum WAGE"])))
    b.page(f"""{sec(5, "Speaking: what should be done?", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>giving opinions</th><th>agreeing / disagreeing</th><th>comparing ideas</th><th>conceding</th></tr>
<tr><td><i>In my opinion… · I'm convinced that… · As I see it…</i></td><td><i>I couldn't agree more. · I'm not so sure. · I see your point, but…</i></td><td><i>The most effective idea is… · …would work better than…</i></td><td><i>That's true, but… · On the other hand… · Even so…</i></td></tr></table></div>
{audiocard(["18.2"])}
{sub("A", "Word stress. Listen, repeat and underline the stressed syllable.", "4 min", "18.2")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.55">{sl}</p>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("B", "Rank the solutions from 1 (most effective) to 6 (least effective). Then compare with your teacher and try to agree on the top three.", "10 min")}
<ol style="line-height:1.45;font-size:8.8pt;margin:0">{soll}</ol></div>{img('D', 28, 28)}</div>
{talk(["Tell me about an item of clothing you've had for a long time. Why hasn't it been thrown away?", "Should people buy fewer clothes? Would you?"])}""",
    28, """<ol><li>B: all the solutions are passive with <i>should</i>; encourage the passive in the student's arguments. Play devil's advocate to push for <i>I see your point, but…</i></li>
<li>Last 3 minutes: wrap-up (two corrections and <i>Can you use the passive in different tenses?</i>).</li></ol>""")

    # H Homework
    pc = [(["is being organized", "is been organized"], "is being organized"), (["were brought", "brought"], "were brought"), (["have been swapped", "have swapped"], "have been swapped"),
          (["be", "been"], "be"), (["will be given", "will give"], "will be given")]
    p = [ch(o, a) for o, a in pc]
    lv = [("I wore these sneakers every day for three years. Now they're completely ___.", "worn out"), ("Don't ___ that shirt! It just needs a new button.", "throw away"),
          ("My grandmother can ___ anything with a needle and thread.", "mend")]
    lvl = "".join(f"<li>{s.replace('___', A(a, 'min-width:16mm'))}</li>" for s, a in lv)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Lucy (Chicago) writes to Danny about a clothes swap at her university. Choose the correct words.", "")}</div>{img('C', 28, 18)}</div>
<div class="box" style="line-height:1.8;font-size:8.8pt;margin:.5mm 0"><b>From: Lucy · To: Danny</b><br>Hi Danny! Big news: a clothes swap {p[0]} by our student club this month, and I'm helping! Last Saturday, over 300 items {p[1]} to the campus center. So far, more than 200 garments {p[2]}. The rules are simple: everything must {p[3]} clean, and anything that isn't swapped {p[4]} to a local charity. Love, Lucy</div>
{sub("B", "Complete with mend, throw away or worn out.", "")}
<ol style="line-height:1.5;font-size:8.6pt;margin:0">{lvl}</ol>
{lean.watch_out([("The jeans are made in a fabric.", "The jeans are made in a factory.", "<i>fabric</i> = the material, like cotton."), ("I need to reform my pants.", "I need to alter / fix my pants.", "we <i>alter</i> clothes."), ("The prices are very expensive.", "The prices are very high.", "things are <i>expensive</i>; prices are <i>high</i>.")])}
{lean.writing_task(sub, "A forum post: Should we buy fewer clothes? Give your opinion, with reasons and one personal example.", "In my opinion, we should… My favorite jacket was bought… Clothes can be…", ["your opinion", "two reasons", "three passives", "100–150 words"], "I can understand an article about fashion and use the passive.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class (ask for the tense of each passive). When you correct the writing, check <i>been / being</i> and <i>be</i> after modals.</p>""")

    b.extra("Audio script", f"""
{sub("18.1", "The real cost of cheap clothes (natural and slow)")}
<p style="margin:.5mm 0"><b>{_L[0]}</b></p>
<div style="line-height:1.3;font-size:8.6pt">{"".join(f"<p style='margin:.5mm 0'>{x}</p>" for x in PARAS)}</div>
{sub("18.2", "Repeat: word stress")}
<p>{" · ".join(S182)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 18 - Sustainable fashion")
