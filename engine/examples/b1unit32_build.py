# Speak! Progress B1 - Unit 32 "Land and sea" (all English) - lean B1 format
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
setup(band="B1 · UNIT 32", audio_json="audio_b1-unit-32.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-32"]
_n = [("almost seven thousand meters", "almost 7,000 meters"), ("nine hundred and seventy-nine meters", "979 meters"), ("about three thousand meters", "about 3,000 meters")]
def _num(s):
    for k, v in _n:
        s = s.replace(k, v)
    return s
S321 = [_num(l) for l in _r["32.1 A geography quiz"].split("\n")]
S322 = [x.split(": ", 1)[1] for x in _r["32.2 Repeat: superlatives"].split("\n")]


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
    cover = cover_html(T, "LEVEL B1 · UNIT 32", "Land and sea", "A South America quiz · <b>the Amazon, Mount Everest · the highest… in the world</b>",
                       [("YOU CAN", "describe landscapes, talk about natural records and use the with place names"),
                        ("LANGUAGE", "a valley · a cliff · a wetland · the tip of the iceberg · the driest desert in the world"),
                        ("PRONUNCIATION", "weak the and in the in superlatives")])
    kw = [("low land between hills or mountains", "a valley"), ("a very high, steep rock face, often by the sea", "a cliff"),
          ("the land next to the sea", "the coast"), ("a line between two countries", "a border"),
          ("land that is wet most of the year, with lots of birds and animals", "a wetland"), ("a small river", "a stream")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:19mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Warm-up: landscapes", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["Describe the photo. What can you see: mountains, a lake, a river, a valley?", "Do you prefer the mountains or the sea? Why?", "What's the most beautiful landscape you've ever seen?"], "START TALKING")}</div></div>
{sub("A", "Key words. Write the words from the box next to the definitions.", "3 min")}
<div class="bank">a border · a cliff · the coast · a stream · a valley · a wetland</div>
<div style="font-size:8.7pt">{twocol(kwl, 3)}</div>
{talk(["Describe the different landscapes in your country: coast, mountains, wetlands, deserts…", "Have you ever crossed a border by land? Where?"], "USE THE WORDS")}""",
    26, """<ol><li>Start with the questions in the top box: 4 minutes. Teach <i>a hill</i> (small mountain), <i>a pond</i> (small lake), <i>a wood</i> (small forest) if they come up.</li>
<li>A: quick check (3 minutes), then the two questions. For Brazil: the coast, the Pantanal, the Amazon rainforest, the Serra do Mar, the Lençóis Maranhenses dunes.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Podcast quiz: South America, land and sea · answer the quiz · who won? · Talk about it",
                      "the with geographical names; superlatives with in / of / one of / ever", "Complete, choose · Use it (oral)",
                      "Weak forms (32.2) · describe Brazil and make your own quiz", "Bruno's message (idioms) · rewrite · word choice · writing"),
        """The Linguahouse lesson is vocabulary (land and water words, a world-records quiz with audio, landscape sizes, idioms). Our listening is a quiz on Danny's podcast <i>Gap Year Diaries</i> with Ana and Bruno, about South America. Danny saw Aconcagua from the bus on his trip (Unit 21); Bruno's uncle took him to the Pantanal as a child (invented). Verified facts: Aconcagua, Argentina, about 6,960 m, is the highest mountain in South America; the Amazon carries more water than any other river (the Nile is usually called the longest); Angel Falls, Venezuela, 979 m, is the highest waterfall (higher than the 828 m Burj Khalifa, the tallest building); Pico da Neblina, about 2,995 m, on the border with Venezuela, is Brazil's highest mountain; the Pantanal (Brazil, Bolivia, Paraguay) is the world's largest tropical wetland; the Atacama, Chile, is the driest non-polar desert (Wikipedia; IBGE; Britannica). In the homework, Bruno writes to Danny after his date with Paula (Unit 11) ended badly.""",
        """<i>the Brazil, the Mount Everest</i>, no article with rivers (<i>Amazon is…</i>), <i>the highest … of Brazil</i>, <i>one of the biggest city</i>, <i>the best place I ever saw</i>. Pronunciation: <i>the</i> and <i>in the</i> are weak and linked: /ðə/, /ɪnðə/.""",
        "Track 32.1 A geography quiz (natural and slow) · Track 32.2 Repeat: superlatives"))

    # Page 2 - Listening
    qz = [("The highest mountain in South America is…", ["Aconcagua", "Pico da Neblina", "Huascarán"], "Aconcagua"),
          ("The river that carries the most water is…", ["the Nile", "the Amazon", "the Paraná"], "the Amazon"),
          ("The highest waterfall in the world is…", ["Iguazu Falls", "Niagara Falls", "Angel Falls"], "Angel Falls"),
          ("The highest mountain in Brazil is…", ["Pico da Bandeira", "Pico da Neblina", "Pão de Açúcar"], "Pico da Neblina"),
          ("The largest tropical wetland in the world is…", ["the Pantanal", "the Everglades", "the Okavango"], "the Pantanal"),
          ("The driest non-polar desert in the world is…", ["the Sahara", "the Gobi", "the Atacama"], "the Atacama")]
    qzl = "".join(f"<li>{q} {ch(o, a)}</li>" for q, o, a in qz)
    b.page(f"""{sec(2, "Listening: a geography quiz", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{audiocard(["32.1 · NATURAL", "32.1 · SLOW"])}
{sub("A", "Before you listen, do the quiz. Then listen to Danny's podcast and check.", "5 min", "32.1")}</div>{img('B', 40, 27)}</div>
<ol style="line-height:1.65;font-size:8.7pt;margin:0">{qzl}</ol>
{sub("B", "Listen again. Who won: Ana or Bruno? What's the score?", "1 min")}
<p style="margin:.3mm 0;font-size:8.9pt">{A("Bruno, 3–2", "min-width:30mm")}</p>
{talk(["How many quiz answers did you get right? Which fact surprised you?", "Which of these places would you most like to visit? Why?", "Should more be done to protect places like the Pantanal and the Amazon?"])}""",
    30, """<ol><li>A–B: 6 minutes. All quiz facts are verified (see the story box). Bruno answered 1, 2 and 5; Ana answered 3 and 4. The photo shows the Atacama.</li>
<li>Talk about it: 6 minutes. Collect sentences with <i>the highest… / the most… I've ever…</i> for page 3.</li></ol>""")

    # Page 3
    lean.grammar_in_class(b, grammar_ref.geography_the_superlatives)

    # Page 4 - Practice
    fs = [("What's ___ (high) mountain in South America?", "the highest"), ("___ Amazon carries more water than any other river.", "The"),
          ("Iguazu is ___ (beautiful) waterfall I've ever seen.", "the most beautiful"), ("___ Pico da Neblina is on the border with Venezuela.", "–"),
          ("The Atacama is ___ (dry) non-polar desert in the world.", "the driest")]
    fsl = "".join(f"<li><i>{s.replace('___', A(a, 'min-width:24mm'))}</i></li>" for s, a in fs)
    use = ["What's the most beautiful place you've ever been to?", "What's the biggest city in your state? Is it one of the biggest in Brazil?", "Name a river, a mountain and a lake you know (with or without the).",
           "What's the hottest or coldest place you've ever been to?", "What's the second most popular tourist place in your city?"]
    b.page(f"""{sec(4, "Practice: the and superlatives", "10 min")}
{sub("A", "Complete the sentences from the quiz. Use the superlative, or write the or – (no article).", "3 min")}
<ol style="line-height:1.85;font-size:8.9pt;margin:0">{fsl}</ol>
{sub("B", "Choose.", "2 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0"><li>We flew over {ch(["Andes", "the Andes"], "the Andes")} on the way to Chile.</li>
<li>São Paulo is one of the biggest {ch(["city", "cities"], "cities")} in the world.</li>
<li>It's the highest mountain {ch(["in", "of"], "in")} Brazil.</li></ol>
<div class="box sand"><h4>RULE</h4><b>the</b> + rivers, oceans, deserts, mountain ranges, plural countries · <b>no article</b> + single mountains, lakes, continents, most countries · <b>the -est / the most… in</b> + place · <b>one of the</b> + plural · <b>I've ever</b> + participle. See the <b>Grammar reference</b> on page 3.</div>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    24, """<ol><li>A–B: 4 minutes. In A4, <i>Pico da Neblina</i> is a single mountain, so no article.</li>
<li>Use it: 6 minutes, all oral. Correct <i>the Brazil</i> and <i>of</i> after superlatives every time.</li></ol>""")

    # Page 5 - Speaking
    b.page(f"""{sec(5, "Speaking: describe your country", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.3pt"><tr><th>describing landscape</th><th>locating</th><th>records</th><th>quiz language</th></tr>
<tr><td><i>It's famous for its… · There are miles of… · It's full of… · It's flat / hilly / rocky.</i></td><td><i>in the north / south of… · on the coast · near the border with…</i></td><td><i>It's one of the… in the world. · It's the second… · the most… I've ever seen</i></td><td><i>Question one… · Is it A, B or C? · Correct! · Sorry, it's… · Final score…</i></td></tr></table></div>
{audiocard(["32.2"])}
{sub("A", "Listen and repeat. Say &ldquo;the&rdquo; and &ldquo;in the&rdquo; quickly and softly.", "4 min", "32.2")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S322))}</p>
{sub("B", "Long turn. Your teacher is a foreign visitor. Describe the landscapes of your country or state: where they are, what they are like and one record or special fact. Talk for 2–3 minutes.", "7 min")}
{sub("C", "Make your own quiz. Write three questions about Brazil with three options each. Ask your teacher. Then answer your teacher's quiz.", "7 min")}
<div style="display:flex;gap:2mm;margin-top:1mm">{"".join(f'<div class="box" style="flex:1;margin:0;min-height:13mm"><b>Question {n}</b><br><span class="small">a… · b… · c…</span></div>' for n in (1, 2, 3))}</div>
{talk(["What's the most interesting trip you've made? Describe the landscape.", "Which landscape would you never get tired of: mountains, beach, forest or desert?"], "TALK ABOUT IT")}""",
    32, """<ol><li>A: the stress is on the superlative and the noun: <i>the HIGHest MOUNtain in the WORLD</i>.</li>
<li>B–C: 14 minutes. Ask follow-up questions in B. Your quiz (answers in red): <span class="red">Brazil borders every South American country except Chile and Ecuador · the Amazon flows into the Atlantic · Lake Titicaca is on the border between Peru and Bolivia</span>. Last 3 minutes: wrap-up (two corrections, and ask <i>Can you now describe the landscapes of your country?</i>).</li></ol>""")

    # Homework
    idi = [("a drop in the ocean", "a drop in the ocean"), ("plenty more fish in the sea", "plenty more fish in the sea"), ("the tip of the iceberg", "the tip of the iceberg"),
           ("a jungle out there", "a jungle out there"), ("over the hill", "over the hill")]
    p = [A(a, "min-width:30mm") for _, a in idi]
    rw = [("Aconcagua / high / mountain / South America", "Aconcagua is the highest mountain in South America."), ("The Amazon / long / river / the world (one of)", "The Amazon is one of the longest rivers in the world."),
          ("This beach / beautiful / place / I / ever / see", "This beach is the most beautiful place I've ever seen.")]
    rwl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Bruno writes to Danny after a bad date. Complete it with the idioms from the box.", "")}</div>{img('C', 28, 18)}</div>
<div class="bank">a drop in the ocean · a jungle out there · over the hill · plenty more fish in the sea · the tip of the iceberg</div>
<div class="box" style="line-height:1.85;font-size:8.8pt;margin:.5mm 0">Hey Danny, Paula and I went out again, and it was a disaster. She said I'm {p[4]} because I'm 26 and I don't like clubs! And that was just {p[2]}: she also hates running and chess. I spent R$200 on dinner, but I know that's {p[0]} compared to what you spent in Buenos Aires. Anyway, Mrs. Lima says there are {p[1]}. Dating in São Paulo… it's {p[3]}! Bruno</div>
{sub("B", "Write superlative sentences.", "")}
<ol style="line-height:1.5;font-size:8.7pt;margin:0">{rwl}</ol>
{lean.watch_out([("I love the nature.", "I love nature.", "nature in general: no <i>the</i>."), ("We went to the beach of Copacabana.", "We went to Copacabana Beach.", "name + Beach / Lake / Mountain."), ("The Brazil has a big coast.", "Brazil has a long coastline.", "no <i>the</i> with most countries; a <i>long</i> coast.")])}
{lean.writing_task(sub, "Describe an interesting trip you made. What were the landscapes like? Include at least one record or superlative.", "Last year I went to…, which has one of the most beautiful…", ["four landscape words", "the / no article with place names", "two superlatives", "one idiom (optional)", "100–150 words"], "I can describe landscapes and talk about natural records.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class. The idioms come from the Linguahouse lesson: ask the student to use two of them in a personal story. The writing task is the Linguahouse talking point.</p>""")

    script = "".join(f"<p style='margin:.4mm 0'><b>{l.split(': ', 1)[0]}:</b> {l.split(': ', 1)[1]}</p>" for l in S321)
    b.extra("Audio script", f"""
{sub("32.1", "A geography quiz (natural and slow)")}
<div style="line-height:1.28;font-size:8.5pt">{script}</div>
{sub("32.2", "Repeat: superlatives")}
<p>{" · ".join(S322)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 32 - Land and sea")
