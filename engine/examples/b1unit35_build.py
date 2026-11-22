# Speak! Progress B1 - Unit 35 "Ecotourism" (all English) - lean B1 format
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
setup(band="B1 · UNIT 35", audio_json="audio_b1-unit-35.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-35"]
_n = [("six hundred billion dollars", "$600 billion"), ("two thousand fifteen", "2015"), ("eight billion", "8 billion")]
def _num(s):
    for k, v in _n:
        s = s.replace(k, v)
    return s
S351 = [_num(l.split(": ", 1)[1]) for l in _r["35.1 Can tourists be too friendly"].split("\n")]
S352 = [x.split(": ", 1)[1] for x in _r["35.2 Repeat: as a result, because of"].split("\n")]


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
    cover = cover_html(T, "LEVEL B1 · UNIT 35", "Ecotourism", "Can tourists be too friendly? · <b>because of · as a result · lead to · cause… to</b>",
                       [("YOU CAN", "talk about the effects of tourism on nature, and explain causes and results"),
                        ("LANGUAGE", "wildlife · a predator · a safe haven · because of · as a result · lead to"),
                        ("PRONUNCIATION", "linking: as a result, because of")])
    kw = [("wild animals and plants in nature", "wildlife"), ("the protection of nature", "conservation"),
          ("an animal that kills and eats other animals", "a predator"), ("afraid of something", "fearful"),
          ("a place where people or animals are free from danger", "a safe haven"), ("to make a wild animal used to living with people", "domesticate")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:21mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Warm-up: close to nature", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["Ecotourism is travel to natural places to enjoy and protect nature. Give some examples.", "Have you ever been on a trip like this? Where?", "Look at the photo. Would you like to do this? Why or why not?"], "START TALKING")}</div></div>
{sub("A", "Key words. Write the words from the box next to the definitions.", "3 min")}
<div class="bank">conservation · domesticate · fearful · a predator · a safe haven · wildlife</div>
<div style="font-size:8.7pt">{twocol(kwl, 3)}</div>
{talk(["What wildlife can you see near your city? Is there a safe haven for animals there?", "Which animals are you fearful of? Why?"], "USE THE WORDS")}""",
    26, """<ol><li>Start with the questions in the top box: 4 minutes. Examples: national parks, whale watching, snorkeling in clear rivers, jungle lodges.</li>
<li>A: quick check (3 minutes), then the two questions. <i>Wildlife</i> is uncountable (no <i>wildlifes</i>).</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Article: can tourists be too friendly? · predict, read and check · find the information · Talk about it",
                      "cause and result: because (of), due to, so, as a result, which means; cause… to, lead to, make", "Complete, choose · Use it (oral)",
                      "Linking (35.2) · role-play: rules for a nature park", "Paulo's blog · rewrite · word choice · writing", "Reading"),
        """The Linguahouse lesson uses an article from The Independent (2015) on a review by Geffroy, Samia, Bessa and Blumstein in Trends in Ecology &amp; Evolution (2015), and teaches <i>be / get used to</i>, which we already covered in Unit 26. We wrote an original article on the same research, read by the Host, and chose a new B1 point that fits the topic: cause and result. Verified facts: protected areas receive about 8 billion visits a year, with about US$600 billion of direct spending (Balmford et al., PLOS Biology, 2015; University of Cambridge). The 2015 review (Cell Press release, Blumstein, UCLA) says animals that relax with tourists may also relax around predators; it compares tourism with domestication and urbanization (less fearful domesticated foxes, bolder urban birds); elk and pronghorn in busier areas of Grand Teton National Park spend less time on alert; vervet monkeys have fewer run-ins with leopards when people are around; the release photo shows tourists snorkeling among piraputanga fish in Nobres, Mato Grosso; the authors ask for more research. In the homework, Paulo (travel photographer) blogs about photographing fish in a clear river in Mato Grosso (fictional trip, no new facts).""",
        """<i>because of</i> + a clause (<i>Because of animals relax…</i>), <i>It caused that…</i> for <i>It caused… to</i>, <i>makes them to relax</i>, <i>due the rain</i>; word choice: <i>educated</i> for <i>polite</i>, <i>the nature</i>, <i>make a trail</i> for <i>go hiking</i>. Pronunciation: linking in <i>as a result</i> /əzəˈrɪzʌlt/ and <i>because of</i> /bɪˈkʌzəv/.""",
        "Track 35.1 Can tourists be too friendly? (natural and slow; read by the Host) · Track 35.2 Repeat: as a result, because of"))

    # Page 2 - Reading
    tf = [("Protected areas get about 8 billion visits a year.", "T"), ("Ecotourism money never helps local communities.", "F"),
          ("Animals that relax with tourists may relax with predators too.", "T"), ("Urban birds escape from danger very quickly.", "F"),
          ("Human presence can keep some predators away.", "T"), ("The scientists say ecotourism is bad and should stop.", "F")]
    tfl = "".join(f"<li>{s} {A(w, 'min-width:6mm')}</li>" for s, w in tf)
    fi = [("how much visitors spend a year", "about $600 billion"), ("the park where elk spent less time watching for danger", "Grand Teton"),
          ("the fish tourists swim with in Mato Grosso", "piraputanga"), ("the animals that meet fewer leopards when people are around", "vervet monkeys")]
    fil = "".join(f"<li>{q} {A(a, 'min-width:24mm')}</li>" for q, a in fi)
    title = S351[0]
    art = "".join(f"<p style='margin:0 0 1mm'>{p}</p>" for p in S351[1:])
    b.page(f"""{sec(2, "Reading: can tourists be too friendly?", "12 min")}
{sub("A", "Before you read, guess: T (true) or F (false)? Then read the article and check.", "4 min")}
<ol style="line-height:1.45;font-size:8.5pt;margin:0;columns:2">{tfl}</ol>
<div class="box" style="margin:1mm 0 0;font-size:7.9pt;line-height:1.32;column-count:2;column-gap:4mm"><b style="font-size:9.5pt">{title}</b><br>{art}</div>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("B", "Find the information.", "3 min")}
<ol style="line-height:1.5;font-size:8.5pt;margin:0">{fil}</ol></div>{img('B', 34, 24)}</div>
{audiocard(["35.1 · NATURAL", "35.1 · SLOW"])}
{talk(["Were your guesses right? What surprised you?", "Should tourists be allowed to swim with or feed wild animals?", "Is ecotourism a good or a bad thing? Why?"])}""",
    30, """<ol><li>A: 1 minute to guess, then read (or listen) and check: 5 minutes. B: 2 minutes. All facts are verified (see the story box). Point out that the scientists present an idea that needs more research, not a final answer.</li>
<li>Talk about it: 5 minutes. Note sentences with <i>because, so, as a result</i> for page 3.</li></ol>""")

    # Page 3
    lean.grammar_in_class(b, grammar_ref.cause_result)

    # Page 4 - Practice
    fs = [("Animals relax with tourists, ___ they may relax with predators too.", "so"), ("Many birds in cities are bold ___ regular contact with people.", "because of"),
          ("Feeding wild animals can ___ them to depend on humans.", "cause"), ("Too many visitors can ___ more pollution in the park.", "lead to"),
          ("The park closed for three months. ___, the animals came back to the trails.", "As a result")]
    fsl = "".join(f'<li>{d.replace("___", A(a, "min-width:22mm"))}</li>' for d, a in fs)
    use = ["What are the effects of tourism on your city or a place you know?", "What causes the most traffic in your city?",
           "Tell me about something that led to a big change in your life.", "What makes you stressed? What makes you relax?",
           "Name a problem in Brazil and explain its main cause."]
    b.page(f"""{sec(4, "Practice: cause and result", "10 min")}
{sub("A", "Complete the sentences with the words from the box.", "4 min")}
<div class="bank">as a result · because of · cause · lead to · so</div>
<ol style="line-height:1.75;font-size:8.9pt;margin:0">{fsl}</ol>
{sub("B", "Choose.", "2 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0"><li>The trail was closed {ch(["due to", "because"], "due to")} the rain.</li>
<li>Tourists make the animals {ch(["relax", "to relax"], "relax")}.</li>
<li>Noise from boats can cause fish {ch(["to swim", "swim"], "to swim")} away.</li></ol>
<div class="box sand"><h4>RULE</h4><b>because</b> + clause · <b>because of / due to</b> + noun · <b>so</b> in the middle · <b>As a result,</b> at the start of a sentence · <b>cause</b> sb <b>to</b> do · <b>lead to</b> + noun · <b>make</b> sb do. See the <b>Grammar reference</b> on page 3.</div>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    24, """<ol><li>A–B: 6 minutes. In A1, <i>which means</i> is also possible; in A5, <i>Because of this,</i> is also possible.</li>
<li>Use it: 4 minutes, all oral. Ask <i>And what was the result?</i> to get a second linker.</li></ol>""")

    # Page 5 - Speaking
    ru = ["a maximum number of visitors per day", "no feeding the animals", "visits only with a local guide", "an entrance fee that pays for conservation",
          "no sunscreen or insect spray in the river", "the park closes when animals have their young", "stay at least 10 meters from the animals", "no drones"]
    rl = "".join(f"<li>{x}</li>" for x in ru)
    b.page(f"""{sec(5, "Speaking: rules for a nature park", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.3pt"><tr><th>giving reasons</th><th>cause and result</th><th>conceding</th><th>compromising</th></tr>
<tr><td><i>The main reason is… · This is because… · That's why…</i></td><td><i>This would lead to… · As a result, … · That could cause animals to…</i></td><td><i>That's a fair point, but… · I see what you mean. However, …</i></td><td><i>What if we…? · How about a compromise: …? · Let's meet halfway.</i></td></tr></table></div>
{audiocard(["35.2"])}
{sub("A", "Listen and repeat. Link the words in “as a result” and “because of”.", "4 min", "35.2")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S352))}</p>
{sub("B", "You manage a nature park with a clear river and lots of wildlife. Choose four rules from the list and explain the reasons and results. Your teacher owns a tour company and wants more visitors. Agree on a final plan.", "14 min")}
<ol style="line-height:1.4;font-size:8.8pt;margin:0;columns:2">{rl}</ol>
{talk(["Would you swim with dolphins or feed wild animals on a trip? Why or why not?", "Who should pay for conservation: tourists, companies or the government?"], "TALK ABOUT IT")}""",
    32, """<ol><li>A: link the final consonant to the next vowel: <i>as a result</i> /əzəˈrɪzʌlt/, <i>because of</i> /bɪˈkʌzəv/, <i>lead to a</i>.</li>
<li>B: 1 minute to choose and plan. As the tour company owner, object (<i>A fee will cause tourists to go somewhere else.</i>) and push the student to give reasons and results, concede and compromise. Last 3 minutes: wrap-up (two corrections, and ask <i>Can you now explain the causes and results of a problem?</i>).</li></ol>""")

    # Homework
    pc = [(["so", "because"], "so"), (["because of", "because"], "because"), (["which means", "due to"], "which means"),
          (["cause", "lead"], "cause"), (["lead to", "cause to"], "lead to"), (["As a result", "Because of"], "As a result")]
    p = [ch(o, a) for o, a in pc]
    rw = [("Tourists fed the monkeys, so the monkeys became aggressive. (As a result)", "Tourists fed the monkeys. As a result, the monkeys became aggressive."),
          ("The beach was closed because there was pollution. (because of)", "The beach was closed because of pollution."),
          ("The dolphins left because of the noise from the boats. (caused … to)", "The noise from the boats caused the dolphins to leave.")]
    rwl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Paulo writes on his travel blog about a trip to Mato Grosso. Choose the correct words.", "")}</div>{img('C', 28, 18)}</div>
<div class="box" style="line-height:1.85;font-size:8.8pt;margin:.5mm 0"><b>Swimming with fish</b><br>Last month I photographed fish in a clear river in Mato Grosso. You can only go in the water with a local guide, {p[0]} the river stays very clean. Our guide asked us not to wear sunscreen {p[1]} it makes the water dirty. The fish weren't fearful at all, {p[2]} they're used to people. The guide told us that feeding them can {p[3]} them to depend on tourists, and it can also {p[4]} fights between them. {p[5]}, feeding is not allowed. Best photos of my year! Paulo</div>
{sub("B", "Rewrite the sentences with the words in brackets.", "")}
<ol style="line-height:1.5;font-size:8.7pt;margin:0">{rwl}</ol>
{lean.watch_out([("I love the nature.", "I love nature.", "no <i>the</i> with <i>nature</i> in general; <i>wildlife</i> is uncountable."), ("The tourists were very educated with the animals.", "The tourists were very respectful to the animals.", "<i>educated</i> = with a good education; use <i>polite</i> or <i>respectful</i>."), ("We made a trail in the forest.", "We went hiking in the forest. / We hiked a trail.", "<i>make a trail</i> = build a new path.")])}
{lean.writing_task(sub, "Is ecotourism a good or a bad thing? Give your opinion with reasons and examples (a place you know or would like to visit).", "Many people think ecotourism is…", ["two advantages", "two disadvantages", "three cause and result linkers", "your opinion", "100–150 words"], "I can talk about the effects of tourism on nature and explain causes and results.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class. The writing task is the Linguahouse talking point. Read it at home and choose two mistakes to discuss in class.</p>""")

    script = "".join(f"<p style='margin:.5mm 0'>{l}</p>" for l in S351)
    b.extra("Audio script", f"""
{sub("35.1", "Can tourists be too friendly? (natural and slow; read by the Host)")}
<div style="line-height:1.3;font-size:8.6pt">{script}</div>
{sub("35.2", "Repeat: as a result, because of")}
<p>{" · ".join(S352)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 35 - Ecotourism")
