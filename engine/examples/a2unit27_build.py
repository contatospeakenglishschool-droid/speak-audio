# Speak! Bridge A2 - Unit 27 "Coffee psychology" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 27", audio_json="audio_a2-unit-27.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["a2-unit-27"]
S271 = [x.split(": ", 1)[1] for x in _r["27.1 What does your coffee say about you?"].split("\n")]
S272 = [x.split(": ", 1)[1] for x in _r["27.2 Repeat: build it up"].split("\n")]
S273 = [x.split(": ", 1)[1] for x in _r["27.3 Repeat: word families"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 27", "Coffee psychology", "Personality and coffee · <b>comparatives and superlatives</b>",
                       [("YOU CAN", "compare people and things, and say how big the difference is"),
                        ("LANGUAGE", "Black coffee is much stronger than a latte. · I'm a bit more patient than you. · the most generous"),
                        ("PRONUNCIATION", "weak than /ðən/ · word families: ANxious → anXIety")])
    wu = [("You're happy to give your money or your time to help other people.", "generous"),
          ("Your feelings change quickly, and you can get angry in just one minute.", "moody"),
          ("You don't mind waiting for something to happen.", "patient"),
          ("You go running every morning, and you never eat fast food.", "health-conscious"),
          ("You have a lot of new and unusual ideas.", "creative"),
          ("You never get stressed or worried.", "relaxed"),
          ("You want a lot from other people, and everything has to be perfect.", "demanding"),
          ("You worry a lot about the future.", "anxious")]
    wl = "".join(f'<li>{d} {A(a, "min-width:28mm")}</li>' for d, a in wu)
    b.page(f"""{sec(1, "Warm-up: personality adjectives", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">{sub("A", "Match the adjectives with the descriptions.", "4 min")}
<div class="bank">anxious · creative · demanding · generous · health-conscious · moody · patient · relaxed</div></div>{img('A', 34, 22)}</div>
<ol style="line-height:1.5;font-size:9pt">{wl}</ol>
{sub("B", "Answer the questions.", "2 min")}
<ol><li>Which three adjectives are negative? {A("moody, demanding, anxious", "min-width:50mm")}</li>
<li>Which adjective makes its opposite with the prefix <b>im-</b>? {A("patient → impatient", "min-width:40mm")}</li></ol>
{sub("C", "Choose two positive adjectives and one negative adjective that describe you.", "2 min")}
<p style="margin:0">positive: {A("", "min-width:30mm")} &nbsp; positive: {A("", "min-width:30mm")} &nbsp; negative: {A("", "min-width:30mm")}</p>""",
    25, """<ol><li>A: drill the pronunciation: <i>relaxed</i> has two syllables /rɪˈlækst/; <i>anxious</i> /ˈæŋkʃəs/ is tricky. <i>Health-conscious</i>: stress on <i>health</i>.</li>
<li>C: don't check; keep the student's answers for the reading (does your coffee match your personality?).</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Personality adjectives</td><td>1</td></tr>
<tr><td>2 Reading</td><td>10 min</td><td>What does your coffee say about you? · noun forms</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Comparatives, superlatives and modifiers</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Form, spelling, irregular forms, how big is the difference</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>4 min</td><td>Build it up (weak than and the) · word families</td><td>5</td></tr>
<tr><td>5 Practice</td><td>9 min</td><td>Comparing three coffees · Word builder: words from the article</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Personality quiz: compare your answers</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Rita puts an article on the wall at City Coffee: what does your coffee say about you? Read by the Reporter (Studio-O). Facts: in the National Coffee Association's Spring 2025 National Coffee Data Trends report, 66% of American adults had coffee in the past day, more than bottled water (64%) (NCA, ncausa.org, April 2025). The coffee and personality findings come from a 2014 survey of 1,000 coffee drinkers by American psychologist Dr. Ramani Durvasula (Psych Central, "What Does Your Coffee Reveal About You?"). Psych Central notes it was a survey, not a scientific experiment, and different outlets report the results slightly differently; the article says this in its last paragraph. The original lesson used a British statistic; we replaced it with an American one.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students say <i>more better</i> and <i>more rude</i>, use <i>very</i> with comparatives (<i>very stronger</i> ✗), write <i>then</i> for <i>than</i>, forget <i>the</i> with superlatives, and pronounce <i>than</i> and <i>the</i> too strongly.</div>
<div class="box"><h4>AUDIO</h4>Track 27.1 What does your coffee say about you? (article, slow and natural) · Track 27.2 Repeat: build it up · Track 27.3 Repeat: word families</div>""")

    # Page 2
    drinks = ["black coffee (no milk)", "latte", "cappuccino", "instant coffee", "decaf (no caffeine)", "cold, sweet coffee drinks"]
    dl = " &nbsp; ".join(f"☐ {d}" for d in drinks)
    paras = "".join(f"<p style='margin:0 0 .9mm'>{p}</p>" for p in S271[1:])
    nf = [("anxious", "anxiety"), ("creative", "creativity"), ("generous", "generosity"), ("moody", "moodiness"), ("patient", "patience")]
    nft = "<tr><th>adjective</th>" + "".join(f"<td>{a}</td>" for a, _ in nf) + "</tr><tr><th>noun</th>" + "".join(f"<td>{A(n, 'min-width:16mm')}</td>" for _, n in nf) + "</tr>"
    b.page(f"""{sec(2, "Reading: coffee and personality", "10 min")}
{sub("A", "Before you read: which coffee do you usually drink? Tick ✓.", "1 min")}
<p class="small" style="margin:0">{dl}</p>
<div style="display:flex;gap:2mm;align-items:center;margin-top:1mm"><div style="flex:1">{audiocard(["27.1 · SLOW", "27.1 · NATURAL"])}</div>{img('B', 19, 17)}{img('L', 19, 17)}{img('C', 19, 17)}{img('D', 19, 17)}</div>
<div class="box" style="margin-top:1mm;font-size:8.6pt;line-height:1.38"><h4 style="font-size:11pt;margin:0 0 .5mm">{S271[0]}</h4><div style="column-count:2;column-gap:5mm">{paras}</div></div>
{sub("B", "Read quickly. Does your coffee match the adjectives you chose in the Warm-up?", "3 min", "27.1 · SLOW")}
{sub("C", "Find the noun forms of these adjectives in the article.", "3 min")}
<table style="margin:0;table-layout:fixed;font-size:8.8pt">{nft}</table>""",
    30, """<ol><li>B: give about two minutes; the student doesn't need every word. Then play the natural version.</li>
<li>C: the stress moves in three pairs: ANxious → anXIety, creAtive → creaTIvity, GENerous → geneROsity (Pronunciation lab, Track 27.3). The last paragraph is a good moment for critical thinking: can a coffee really show your personality?</li></ol>""")

    # Page 3
    b.page(f"""{sec(3, "Language focus: comparatives and superlatives", "10 min")}
{sub("A", "Study the sentences. Then choose the correct option.", "3 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">1 Black coffee drinkers can be both <b>ruder</b> and <b>moodier</b> than latte drinkers.<br>2 Instant coffee drinkers tend to be <b>more relaxed</b> than cappuccino drinkers.</div>
<ol style="line-height:1.7"><li>When we compare two things, we use {ch(["the", "then", "than"], "than")}.</li>
<li><i>Relaxed</i> uses <b>more</b> because it {ch(["is an -ed adjective", "is irregular", "is a new word"], "is an -ed adjective")}.</li></ol>
{sub("B", "Look at the underlined words. Then choose the correct option.", "3 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">3 They can feel <u>slightly</u> more anxious than black coffee drinkers.<br>4 People who drink decaf are <u>a bit</u> more health-conscious than latte drinkers.<br>5 These trendsetters are <u>a lot</u> more relaxed about their health than cappuccino drinkers.</div>
<ol style="line-height:1.7"><li><i>slightly / a bit / a little</i> = a {ch(["big", "small"], "small")} difference.</li>
<li><i>a lot / much</i> = a {ch(["big", "small"], "big")} difference.</li></ol>
{sub("C", "These sentences compare one group with all the others. Choose the correct option.", "4 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">6 Latte drinkers are <b>the most generous</b> with their time.<br>7 Cappuccino drinkers seem to have <b>the most demanding</b> personalities.<br>8 People who prefer cold, sweet coffee drinks had <b>the highest</b> score for creativity.</div>
<ol style="line-height:1.7"><li>With superlatives, we use {ch(["a", "the", "than"], "the")}.</li>
<li>We add <b>-est</b> to adjectives with {ch(["one syllable", "three syllables"], "one syllable")}.</li>
<li>With <b>the most</b>, we {ch(["add", "don't add"], "don't add")} -est to the adjective.</li></ol>
<div class="box sand"><h4>RULE</h4>2 things: <b>-er than</b> / <b>more … than</b> · the whole group: <b>the -est</b> / <b>the most …</b> · irregular: <b>better / the best, worse / the worst</b>. More on the next page: <b>Grammar reference</b>.</div>""",
    20, """<ol><li>A: <i>moody → moodier</i>: y → i. Elicit more examples from the student's life: <i>my sister is ruder than me</i>.</li>
<li>B: draw two lines of different lengths on paper to show <i>slightly</i> vs <i>much</i>.</li></ol>""")

    grammar_ref.comparatives_superlatives(b)

    # Page 5
    stress = ["ANxious → anXIety", "creAtive → creaTIvity", "GENerous → geneROsity", "MOOdy → MOOdiness", "PAtient → PAtience"]
    wf = "".join(f"<li>{w} {A(s, 'min-width:44mm')}</li>" for w, s in zip(S273, stress))
    b.page(f"""{sub("D", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>This coffee is more better.</td><td><b>This coffee is better.</b></td><td>better = more good.</td></tr>
<tr><td>He's more rude than me.</td><td><b>He's ruder than me.</b></td><td>one syllable: -er.</td></tr>
<tr><td>It's very stronger than tea.</td><td><b>It's much stronger than tea.</b></td><td>much / a lot + comparative.</td></tr>
<tr><td>Lattes are sweeter then black coffee.</td><td><b>…sweeter than black coffee.</b></td><td>than, not then.</td></tr>
<tr><td>She's most generous person I know.</td><td><b>She's the most generous person I know.</b></td><td>superlative + the.</td></tr>
<tr><td>I'm the more patient in my family.</td><td><b>I'm the most patient in my family.</b></td><td>the whole group = most.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "4 min")}
{audiocard(["27.2", "27.3"])}
{sub("A", "Build it up. Listen and repeat. Stress the adjectives; than and the are weak.", "2 min", "27.2")}
<ol style="line-height:1.45;font-size:9pt">{"".join(f"<li>{s}</li>" for s in S272)}</ol>
{sub("B", "Listen and repeat the word families. Write the stressed syllable in CAPITALS.", "2 min", "27.3")}
<ol style="line-height:1.55">{wf}</ol>""",
    20, """<ol><li>A: weak forms: <i>than</i> /ðən/, <i>the</i> /ðə/. Let the student tap the table on the stressed words.</li>
<li>B: <i>anxious</i> /ˈæŋkʃəs/ → <i>anxiety</i> /æŋˈzaɪəti/: the sound changes too.</li></ol>""")

    # Page 6
    rows = [("strong", "2/5", "3/5", "5/5"), ("frothy (with lots of bubbles)", "3/5", "5/5", "0/5"), ("bitter (with a strong taste)", "3/5", "2/5", "4/5"), ("good / bad", "your ideas", "your ideas", "your ideas")]
    rt = "".join(f"<tr><td>{a}</td><td>{x}</td><td>{y}</td><td>{z}</td></tr>" for a, x, y, z in rows)
    cq = [("Compare black coffees and lattes (strong).", "Black coffees are much / a lot stronger than lattes."),
          ("Compare cappuccinos and black coffees (frothy).", "Cappuccinos are much / a lot frothier than black coffees."),
          ("Compare black coffees and lattes (bitter).", "Black coffees are slightly / a bit more bitter than lattes."),
          ("Compare lattes and cappuccinos (good).", "Your own answer with better than."),
          ("Compare all three (strong).", "Black coffees are the strongest."),
          ("Compare all three (frothy).", "Cappuccinos are the frothiest."),
          ("Compare all three (bitter).", "Black coffees are the most bitter."),
          ("Compare all three (bad).", "Your own answer with the worst.")]
    cql = "".join(f"<li>{q}<br>{A(a, 'min-width:110mm')}</li>" for q, a in cq)
    wb = [("Latte drinkers <b>typically</b> want to please other people.", ["most of them", "a few of them", "all of them"], "most of them"),
          ("<b>Perfectionist</b> cappuccino drinkers…", ["want some things to be perfect", "want everything to be perfect", "don't care about details"], "want everything to be perfect"),
          ("Instant coffee drinkers <b>tend to be</b> more relaxed.", ["all of them are", "most of them are", "a few of them are"], "most of them are"),
          ("These <b>trendsetters</b>…", ["don't care what people think", "show us new ways to do things", "follow old ways of doing things"], "show us new ways to do things")]
    wbl = "".join(f"<li>{s} = {ch(o, a)}</li>" for s, o, a in wb)
    b.page(f"""{sec(5, "Practice", "9 min")}
{sub("A", "Use the table to compare the coffees. Add slightly, a bit, a little, much or a lot.", "6 min")}
<table style="margin:0;font-size:8.6pt;table-layout:fixed"><tr><th style="width:56mm"></th><th>lattes</th><th>cappuccinos</th><th>black coffees</th></tr>{rt}</table>
<p class="small" style="margin:.5mm 0"><i>Example: Compare lattes and cappuccinos (strong). → Cappuccinos are slightly stronger than lattes.</i></p>
<ol style="line-height:1.3;font-size:8.8pt">{cql}</ol>
{sub("B", "Word builder: words from the article. Choose the best meaning.", "3 min")}
<ol style="line-height:1.6;font-size:8.8pt">{wbl}</ol>""",
    24, """<ol><li>A: <i>coffee</i> is usually uncountable, but for cups or types we say <i>lattes, cappuccinos</i>. Check that the student uses a modifier in 1–3: 2/5 vs 5/5 is a big difference; 3/5 vs 4/5 is small.</li>
<li>B: <i>typically</i> and <i>tend to</i> are useful for generalizations: <i>Brazilians tend to drink small, strong coffees.</i></li></ol>""")

    # Page 7
    quiz = [("If someone needs my help,", "I always say yes.", "I sometimes say yes.", "I rarely say yes.", "generous"),
            ("When there's a problem,", "I like to find a new solution.", "I usually ask someone for advice.", "I don't know what to do.", "creative"),
            ("Exercise?", "I make time for it every day.", "I usually exercise twice a week.", "What's that?", "health-conscious"),
            ("My home is messy, and I'm behind with my work.", "I feel fine about it.", "I feel a bit stressed.", "This never happens. I hate it!", "relaxed"),
            ("My coffee order is wrong, so I say:", "\"Make it again right now, and I'm not paying.\"", "\"Could you change it, please?\"", "\"That's OK. Everyone makes mistakes.\"", "demanding"),
            ("Yesterday I felt…", "happy, sad, angry and tired.", "a bit happy and a bit sad.", "mostly happy.", "moody"),
            ("My bus is late.", "No problem: I have a coffee and a good book.", "That's OK if it's only ten minutes.", "I'm not happy! Where is it?", "patient"),
            ("When I think about the future,", "I worry about money, my job, my health…", "I feel good about most things.", "I wonder what's for lunch.", "anxious")]
    qt = "".join(f"<tr><td><b>{i+1}</b> {q}<br>{A(adj, 'min-width:20mm')}</td><td>☐ {h}</td><td>☐ {m}</td><td>☐ {l}</td></tr>" for i, (q, h, m, l, adj) in enumerate(quiz))
    b.page(f"""{sec(6, "Speaking: personality quiz", "12 min")}
{sub("A", "Choose the best answer for you. Then write the adjective for each question.", "4 min")}
<div class="bank">anxious · creative · demanding · generous · health-conscious · moody · patient · relaxed</div>
<table style="margin:0;font-size:8.2pt;line-height:1.3"><tr><th style="width:44mm"></th><th>high score</th><th>middle score</th><th>low score</th></tr>{qt}</table>
{sub("B", "Compare your answers with your teacher. Use comparatives and slightly, a bit, much or a lot.", "5 min")}
<p class="small" style="margin:0"><i>A: What did you say for number 3? I said "What's that?", so I think you're a lot more health-conscious than me.<br>B: Yes, I go to the gym every day. But you're a bit more patient than me!</i></p>
{sub("C", "Talk about your family and friends. Who's the most generous? The most relaxed? The moodiest?", "3 min")}""",
    24, """<ol><li>A: the teacher answers the quiz too, so the comparison in B is real. Answers: 1 generous · 2 creative · 3 health-conscious · 4 relaxed · 5 demanding · 6 moody · 7 patient · 8 anxious.</li>
<li>C: in 1:1 classes, superlatives work best with family, friends or coworkers. Ask a follow-up question each time: <i>Why do you say that?</i></li></ol>""")

    # Page 8
    pc = [("A2 Unit 24", "I can plan and write a short story with direct speech."), ("A2 Unit 25", "I can talk about TV shows with -ed and -ing adjectives."),
          ("A2 Unit 26", "I can describe people's personalities with modifiers."), ("A2 Unit 27", "I can compare people and things with comparatives and superlatives.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Coffee", "is", "better than tea."), ("He's happy one minute and angry the next. He's definitely the", "moodiest", "person I know."),
          ("I feel more relaxed today", "than", "I did yesterday."), ("I'm feeling", "more", "anxious than you about the test."),
          ("In my opinion, lattes", "are", "the best type of coffee."), ("My mom is very busy at work, but my dad is retired. My dad is", "much / a lot", "more generous with his time than my mom."),
          ("That server is", "ruder", "than the other one. I never sit at his table."), ("There are seven people on our team, and the", "most", "creative one is Jean."),
          ("This is", "the", "worst coffee I've ever had!"), ("You go to the gym every day? I only go once a week. You're", "much / a lot", "more health-conscious than I am.")]
    hwl = "".join(f"<li>{a} {A(w, 'min-width:16mm')} {e}</li>" for a, w, e in hw)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Write one word in each gap.</b></p>
<ol style="line-height:1.6;font-size:9pt">{hwl}</ol>
<p style="margin-top:1.5mm"><b>2. My family (50–75 words).</b> Compare three people in your family or three friends. Who's the most patient, the most creative, the moodiest? Use <i>a bit, much</i> or <i>a lot</i> at least twice.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    24, """<p>Extra idea for early finishers: compare ways of making coffee at home (a French press, a pour-over, a moka pot, instant coffee): which is the easiest, the fastest, the cheapest, the best? Brazilian students often have strong opinions about coffee!</p>""")

    b.extra("Audio script", f"""
{sub("27.1", "What does your coffee say about you? (slow and natural)")}
<p style="line-height:1.42">{"<br>".join(S271)}</p>
{sub("27.2", "Repeat: build it up")}
<p>{" · ".join(S272)}</p>
{sub("27.3", "Repeat: word families")}
<p>{" · ".join(S273)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 27 - Coffee psychology")
