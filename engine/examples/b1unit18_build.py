# Speak! Progress B1 - Unit 18 "Sustainable fashion" (all English) - B1 format (2026-11-09)
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Progress"
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
    def lines(n):
        return '<div class="wline"></div>' * n

    # Page 1 - Warm-up
    cover = cover_html(T, "LEVEL B1 · UNIT 18", "Sustainable fashion", "Fast fashion and its real cost · <b>the passive: is being made, has been signed, can be repaired</b>",
                       [("YOU CAN", "understand an article about the fashion industry and discuss solutions"),
                        ("LANGUAGE", "a garment · synthetic · a consumer · a landfill · sustainable · wear out · hand down · swap"),
                        ("PRONUNCIATION", "word stress: sustainable, environment, synthetic")])
    kw = [("an item of clothing", "a garment"), ("made with chemicals, not natural", "synthetic"), ("a person who buys things for personal use", "a consumer"),
          ("to use someone unfairly for your own advantage", "exploit"), ("a place where garbage is buried", "a landfill"),
          ("the lowest salary you can legally receive", "the minimum wage"), ("not damaging to the environment, so it can continue for a long time", "sustainable")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:22mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Warm-up: what's in your closet?", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 35)}<div style="flex:1">
{sub("A", "Discuss with your teacher.", "3 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0"><li>How often do you buy new clothes? Where?</li><li>What do you do with clothes you don't wear anymore?</li><li>Do you check where your clothes are made?</li></ol></div></div>
{sub("B", "Key words. Write the words from the box next to the definitions.", "4 min")}
<div class="bank">a consumer · exploit · a garment · a landfill · the minimum wage · sustainable · synthetic</div>
<div style="font-size:8.6pt">{twocol(kwl, 4)}</div>
{sub("C", "Look at the label of something you're wearing. What's it made of? Where was it made?", "1 min")}""",
    30, """<ol><li>A: <i>closet</i> is American English (British: <i>wardrobe</i>). <i>Fast fashion</i> = cheap clothes made quickly to follow trends.</li>
<li>B: <i>exploit</i> /ɪkˈsplɔɪt/ is a verb; the noun is <i>exploitation</i>. <i>Landfill</i> can be countable (<i>a landfill</i>) or uncountable (<i>sent to landfill</i>).</li>
<li>C: model the passive: <i>It's made of cotton. It was made in Vietnam.</i></li></ol>""", cover=cover)

    b.extra("Lesson overview · 60 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Discussion · key words</td><td>1</td></tr>
<tr><td>2 Reading</td><td>12 min</td><td>Article: the real cost of cheap clothes (verified facts)</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>8 min</td><td>The passive: present continuous, present perfect, future, modals</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>The passive in other tenses and with modals (study at home)</td><td>4</td></tr>
<tr><td>4 Vocabulary lab + pronunciation</td><td>8 min</td><td>The life of clothes: wear out, hand down, swap · word families · word stress</td><td>5</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Lucy's campus clothes swap · active to passive</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Rank the solutions · long turn · talking point</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>4 min</td><td>Can-do · language notes · writing homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY</h4>The Linguahouse lesson uses a 2019 UK opinion article on fashion waste. We wrote an original article, read by the Host (track 18.1), with facts checked in current sources. Verified facts: clothing production about doubled between 2000 and 2015, while each item was worn fewer times; the equivalent of one garbage truck of textiles is landfilled or burned every second; less than 1% of the material used for clothing is recycled into new clothing (Ellen MacArthur Foundation, <i>A New Textiles Economy</i>, 2017; <i>Circular Business Models</i>, 2021). Polyester is a synthetic fabric made from oil. The Rana Plaza building collapsed on April 24, 2013, in Savar, near Dhaka (Bangladesh); 1,134 people died and about 2,000–2,500 were injured; afterward, an agreement on fire and building safety was signed by international brands and factories were inspected. The "30 times" test is presented as advice, not a statistic. In the Practice, Lucy (Chicago) writes about a clothes swap at her university. The writing model is Danny's forum post about buying second-hand clothes in São Paulo.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students confuse <i>been</i> and <i>being</i> (<i>are been made</i>), forget <i>be</i> after modals (<i>it can recycled</i>), and say <i>fabric</i> for <i>factory</i>, <i>reform</i> for <i>alter / fix</i>, and <i>costume</i> for <i>clothes</i>. Word stress: <i>susTAINable, enVIronment, synTHEtic</i>.</div>
<div class="box"><h4>AUDIO</h4>Track 18.1 The real cost of cheap clothes (natural and slow) · Track 18.2 Repeat: word stress</div>""")

    # Page 2 - Reading
    bq = [("Between 2000 and 2015, clothing production…", ["fell", "about doubled", "grew ten times"], "about doubled"),
          ("Polyester is made from…", ["oil", "rubber", "leaves"], "oil"),
          ("How many people died in the Rana Plaza collapse?", ["about 400", "about 1,100", "about 2,100"], "about 1,100"),
          ("How much of the material used for clothes is recycled into new clothes?", ["less than 1%", "about 15%", "about half"], "less than 1%")]
    bql = "".join(f'<li>{q} {ch(o, a)}</li>' for q, o, a in bq)
    qs = [("What is the real cost of cheap clothes?", "damage to the planet and to workers"), ("What happens every second?", "one garbage truck of textiles is burned or sent to landfill"),
          ("What happened after Rana Plaza?", "a safety agreement was signed; factories were inspected"), ("What can be done with old clothes?", "repaired, swapped, sold, given away, upcycled"),
          ("What is the simple test?", "Will it be worn at least 30 times?")]
    qsl = [f'<li value="{i+1}">{q} {A(a, "min-width:20mm")}</li>' for i, (q, a) in enumerate(qs)]
    art = "".join(f'<p style="margin:0 0 .8mm"><b style="color:#176074">{i+1}</b> {p}</p>' for i, p in enumerate(PARAS))
    b.page(f"""{sec(2, "Reading: the real cost of cheap clothes", "12 min")}
{sub("A", "Before you read. Guess the answers. Then read the article and check.", "3 min")}
<ol style="line-height:1.5;font-size:8.5pt;margin:0">{bql}</ol>
<div class="box" style="margin:.5mm 0 0;font-size:8pt;line-height:1.33;column-count:2;column-gap:4mm"><b style="font-size:9.5pt">The real cost of cheap clothes</b><br>{art}</div>
<div style="display:flex;gap:3mm;align-items:center;margin-top:1mm"><div style="flex:1">{audiocard(["18.1 · NATURAL", "18.1 · SLOW"])}</div>{img('B', 36, 20)}</div>
{sub("B", "Read again and answer the questions.", "4 min")}
<div style="font-size:8.5pt">{twocol(qsl, 3)}</div>
{sub("C", "Think about it. Discuss with your teacher.", "3 min")}
<ol style="line-height:1.4;font-size:8.7pt;margin:0"><li>"The most sustainable clothes are the ones that are already in your closet." What does the writer mean? {R("The best option is to wear what we already have, not to buy new 'green' clothes.") if T else ""}</li>
<li>Would the "30 times" test change the way you shop?</li></ol>""",
    24, """<ol><li>A: let the student guess first; the reading then has a purpose. They can read and listen (18.1) at the same time.</li>
<li>All figures are real (see the story box). Treat Rana Plaza with care: it is a tragedy, not a curiosity. <i>Upcycle</i> = turn old things into something new and better.</li></ol>""")

    # Page 3 - Language focus
    fs = [("It ___ at the checkout. (not pay)", "isn't paid"), ("Every second, one garbage truck of textiles ___ or sent to landfill. (burn)", "is burned"),
          ("An agreement on factory safety ___ by many brands. (sign)", "has been signed"), ("Clothes ___, swapped, sold or given away. (can / repair)", "can be repaired"),
          ("Will it ___ at least 30 times? (wear)", "be worn")]
    fsl = "".join(f"<li><i>{s.replace('___', A(a, 'min-width:24mm'))}</i></li>" for s, a in fs)
    b.page(f"""{sec(3, "Language focus: the passive", "8 min")}
{sub("A", "Complete the sentences from the article with the passive form of the verbs. Then check in the text.", "3 min")}
<ol style="line-height:1.85;font-size:8.9pt;margin:0">{fsl}</ol>
{sub("B", "Complete the rules. Choose.", "3 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0"><li>The passive is always {ch(["be + past participle", "have + past participle"], "be + past participle")}.</li>
<li>Present continuous passive: <i>New clothes are {ch(["been", "being"], "being")} produced all the time.</i></li>
<li>Present perfect passive: <i>Many factories have {ch(["been", "being"], "been")} inspected.</i></li>
<li>After a modal, we use {ch(["be", "to be"], "be")} + participle: <i>It can be recycled.</i></li>
<li>We use the passive when {ch(["the action is more important than who does it", "we want to say who does it"], "the action is more important than who does it")}.</li></ol>
{sub("C", "Correct or incorrect? Choose.", "2 min")}
<ol style="line-height:1.6;font-size:8.9pt;margin:0"><li>These jeans have been worn by three people. {ch(["correct", "incorrect"], "correct")}</li><li>Old clothes should recycled. {ch(["correct", "incorrect"], "incorrect")} {R("→ should be recycled") if T else ""}</li><li>A new store is been built downtown. {ch(["correct", "incorrect"], "incorrect")} {R("→ is being built") if T else ""}</li></ol>
<div class="box sand"><h4>RULE</h4>Passive = <b>be + past participle</b>; only <b>be</b> changes: <i>is made · is <b>being</b> made · was made · has <b>been</b> made · will <b>be</b> made · can / should / must <b>be</b> made</i>. <b>being</b> = in progress now; <b>been</b> = after <i>have / has</i>. More on the next page: <b>Grammar reference</b>.</div>""",
    26, """<ol><li>A: ask the student to underline every passive in the article (there are more than ten).</li>
<li>B: write <i>be / being / been</i> on the board and ask which word comes after <i>is</i>, after <i>has</i> and after <i>can</i>.</li></ol>""")

    grammar_ref.passive_tenses_modals(b)

    # Page 5 - Vocabulary lab
    lv = [("We can't afford new uniforms, so my younger brother wears my old ones. I ___ them ___ to him.", "hand / down"),
          ("I wore these sneakers every day for three years, and now they're completely ___.", "worn out"),
          ("At the party, we ___ clothes: I took a dress and gave a jacket.", "swapped"),
          ("Don't ___ that shirt! It just needs a new button.", "throw away"),
          ("I ___ all my baby clothes to a charity.", "gave away"),
          ("My grandmother can ___ anything with a needle and thread.", "mend")]
    lvl = "".join(f"<li>{s.replace(' ___ them ___ ', ' ' + A('hand them down', 'min-width:22mm') + ' ') if 'them ___' in s else s.replace('___', A(a, 'min-width:18mm'))}</li>" for s, a in lv)
    wf = [("sustain", "sustainable"), ("consume", "consumer / consumption"), ("produce", "production / producer"), ("recycle", "recycling"), ("environment", "environmental")]
    wfl = "".join(f"<li>{v} → {A(n, 'min-width:30mm')}</li>" for v, n in wf)
    b.page(f"""{sec(4, "Vocabulary lab: the life of clothes", "4 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Complete the sentences with the verbs in the box. Use the correct form.", "2 min")}
<div class="bank">give away · hand down · mend · swap · throw away · wear out</div></div>{img('C', 30, 20)}</div>
<ol style="line-height:1.55;font-size:8.6pt;margin:0">{lvl}</ol>
<div style="display:flex;gap:4mm;align-items:flex-start"><div style="flex:1">
{sub("B", "Word families. Write a noun or adjective from the article.", "2 min")}
<ul style="line-height:1.5;font-size:8.6pt;margin:0;padding-left:4mm">{wfl}</ul></div></div>
<div class="box sand"><h4>WATCH OUT: FALSE FRIENDS AND WORD CHOICE</h4>
<table style="margin:0;font-size:8.2pt"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>The jeans are made in a fabric.</td><td><b>The jeans are made in a factory.</b></td><td><i>fabric</i> = the material clothes are made of, like cotton.</td></tr>
<tr><td>I need to reform my pants.</td><td><b>I need to alter / fix my pants.</b></td><td>we <i>reform</i> systems and laws; we <i>alter</i> clothes.</td></tr>
<tr><td>I bought a new costume for work.</td><td><b>I bought new clothes / an outfit for work.</b></td><td>a <i>costume</i> is for a party or a play.</td></tr>
<tr><td>The prices are very expensive.</td><td><b>The prices are very high.</b></td><td>things are <i>expensive</i>; prices are <i>high</i>.</td></tr></table></div>
{sec(5, "Pronunciation lab: word stress", "4 min")}
{audiocard(["18.2"])}
{sub("A", "Listen and repeat. Underline the stressed syllable. Then use three words in a sentence about your clothes.", "4 min", "18.2")}
<p style="margin:.3mm 0;font-size:8.8pt;line-height:1.55">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {R(y) if T else x}" for i, (x, y) in enumerate(zip(S182, ["susTAINable", "enVIronment", "conSUMer", "synTHEtic", "polyESter", "reCYcle", "GARment", "LANDfill", "UPcycle", "MInimum WAGE"])))}</p>""",
    23, """<ol><li>A: <i>wear out</i> = use something until it can't be used anymore; <i>hand down</i> = give to a younger person in the family; <i>mend</i> = repair (clothes).</li>
<li>B: <i>consumption</i> = how much we use or buy; <i>environmental</i> adds <i>-al</i> to the noun.</li></ol>""")

    # Page 6 - Practice
    pc = [(["is being organized", "is been organized"], "is being organized"), (["were brought", "brought"], "were brought"), (["have been swapped", "have swapped"], "have been swapped"),
          (["be", "been"], "be"), (["will be given", "will give"], "will be given"), (["can be fixed", "can fixed"], "can be fixed")]
    p = [ch(o, a) for o, a in pc]
    ap = [("They make most of our clothes in Asia.", "Most of our clothes are made in Asia."), ("They are building a new mall downtown.", "A new mall is being built downtown."),
          ("Someone has stolen my bike!", "My bike has been stolen!"), ("They will open the store next week.", "The store will be opened next week."),
          ("You should wash this sweater by hand.", "This sweater should be washed by hand.")]
    apl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in ap)
    b.page(f"""{sec(6, "Practice", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Lucy (Chicago) writes to Danny about a clothes swap at her university. Choose the correct words.", "4 min")}</div>{img('D', 30, 20)}</div>
<div class="box" style="line-height:1.95;font-size:9pt"><b>From: Lucy · To: Danny</b><br>Hi Danny! Big news: a clothes swap {p[0]} by our student club this month, and I'm helping! Last Saturday, over 300 items {p[1]} to the campus center. So far, more than 200 garments {p[2]}, and nothing has been paid for! The rules are simple: everything must {p[3]} clean, and you can take one item for each item you bring. Anything that isn't swapped {p[4]} to a local charity. We also have a repair table: holes {p[5]} in ten minutes. Maybe you can do one at the hostel! Love, Lucy</div>
{sub("B", "Make the sentences passive. Don't use by.", "4 min")}
<ol style="line-height:1.55;font-size:8.8pt;margin:0">{apl}</ol>""",
    24, """<ol><li>A: ask for the tense of each passive: <i>is being organized</i> (present continuous), <i>have been swapped</i> (present perfect)…</li>
<li>B: we don't use <i>by</i> because the agent (<i>they, someone, you</i>) is not important.</li></ol>""")

    # Page 7 - Speaking
    sol = ["Clothes repair services should be made cheaper by the government.", "A small tax should be paid on every new garment.", "Repairing clothes should be taught at school.",
           "Second-hand clothes should be bought before new ones.", "Unsold clothes should never be destroyed.", "Every garment should be worn at least 30 times."]
    soll = "".join(f"<li>{x} <span style='color:#999'>___</span></li>" for x in sol)
    b.page(f"""{sec(7, "Speaking: what should be done?", "12 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>giving opinions</th><th>agreeing / disagreeing</th><th>comparing ideas</th><th>conceding</th></tr>
<tr><td><i>In my opinion… · I'm convinced that… · As I see it…</i></td><td><i>I couldn't agree more. · I'm not so sure. · I see your point, but…</i></td><td><i>The most effective idea is… · …would work better than…</i></td><td><i>That's true, but… · On the other hand… · Even so…</i></td></tr></table></div>
{sub("A", "Rank the solutions from 1 (most effective) to 6 (least effective). Then compare with your teacher and try to agree on the top three.", "6 min")}
<ol style="line-height:1.5;font-size:8.9pt;margin:0">{soll}</ol>
{sub("B", "Long turn. Prepare for one minute, then talk for two minutes about an item of clothing you've had for a long time.", "4 min")}
<ul style="line-height:1.45;font-size:8.9pt;margin:0"><li>what it is, and where and when it was bought (or who it was given by)</li><li>what it's made of and how it's been looked after</li><li>why it hasn't been thrown away</li></ul>
{sub("C", "Talking point. Discuss with your teacher.", "2 min")}
<ol style="line-height:1.5;font-size:8.9pt;margin:0"><li>How does fashion culture in your country compare with what you read in the article?</li><li>Should people buy fewer clothes? Would you?</li></ol>""",
    30, """<ol><li>A: all the solutions are passive with <i>should</i>; encourage the student to use the passive in their arguments. Play devil's advocate to push for <i>I see your point, but…</i></li>
<li>B: don't interrupt; note mistakes for the error log (page 8), especially <i>been / being</i> and missing <i>be</i> after modals.</li></ol>""")

    # Page 8 - Wrap-up
    cd = ["I can understand an article about the fashion industry.", "I can use the passive in different tenses and with modals.", "I can discuss solutions and give my opinion."]
    cdr = "".join(f"<tr><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for s in cd)
    b.page(f"""{sec(8, "Wrap-up and homework", "4 min")}
{sub("A", "Can-do check", "1 min")}
<table class="ck" style="font-size:8.6pt"><tr><th>In English…</th><th style="width:16mm">Easy!</th><th style="width:16mm">Sometimes</th><th style="width:16mm">Not yet</th></tr>{cdr}</table>
{sub("B", "My language notes. Write three corrections from today's class.", "2 min")}
<div style="display:flex;gap:5mm;font-size:8.6pt"><div style="flex:1"><b>I said…</b>{lines(3)}</div><div style="flex:1"><b>Better:</b>{lines(3)}</div></div>
{sub("C", "Homework: writing (100–150 words)", "1 min")}
<p style="margin:.3mm 0"><b>A forum post: Should we buy fewer clothes?</b> Give your opinion, with reasons and one personal example. Read Danny's post first.</p>
<div class="box" style="font-size:8.6pt;line-height:1.4;margin:.5mm 0"><b>Danny · Gap year forum · Why I stopped buying new clothes</b><br><i>When I left the US, I brought one backpack, so I can't buy much anyway! But I've also changed my mind about fashion. I recently read that less than one percent of the material used to make clothes is recycled into new clothes. That shocked me. Since then, all my clothes have been bought second-hand. There's a great second-hand store near my hostel in São Paulo, and my favorite jacket was found there for the price of a sandwich. When my jeans were torn, they were mended by a tailor around the corner. In my opinion, we should all buy fewer clothes, and better ones. Not everything can be fixed, of course, but much more can be repaired than we think. What about you?</i></div>
<p class="small" style="margin:.3mm 0">Checklist: ☐ your opinion in the first sentence &nbsp;☐ two reasons &nbsp;☐ a personal example &nbsp;☐ three passives &nbsp;☐ 100–150 words</p>
{lines(5)}""",
    30, """<ol><li>B (error log): during the lesson, note 3–5 real mistakes. Here, the student writes what they said and the better version; guide them to self-correct first.</li>
<li>C: check the passives and the opinion language (<i>In my opinion, As I see it</i>). A <i>tailor</i> repairs and alters clothes.</li></ol>""")

    b.extra("Audio script", f"""
{sub("18.1", "The real cost of cheap clothes (natural and slow)")}
<p style="margin:.5mm 0"><b>{_L[0]}</b></p>
<div style="line-height:1.3;font-size:8.6pt">{"".join(f"<p style='margin:.5mm 0'>{x}</p>" for x in PARAS)}</div>
{sub("18.2", "Repeat: word stress")}
<p>{" · ".join(S182)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 18 - Sustainable fashion")
