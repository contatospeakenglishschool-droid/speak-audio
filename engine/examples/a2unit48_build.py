# Speak! Bridge A2 - Unit 48 "On my plate" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 48", audio_json="audio_a2-unit-48.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["a2-unit-48"]
S481 = [x.split(": ", 1)[1] for x in _r["48.1 Ana's essay"].split("\n")]
S482 = [x.split(": ", 1)[1] for x in _r["48.2 Repeat: opinions"].split("\n")]
S483 = [x.split(". ", 1)[1] for x in [y.split(": ", 1)[1] for y in _r["48.3 Contrast, addition or example?"].split("\n")]]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans, l=""):
        return (f"<sup><b>{l}</b></sup>" if l else "") + "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 48", "On my plate", "Food choices · <b>writing an opinion essay</b>",
                       [("YOU CAN", "plan and write a short essay with an introduction, two sides and a conclusion, and give your opinion"),
                        ("LANGUAGE", "In my opinion, · From my point of view, · However, · In addition, · For example, · In conclusion,"),
                        ("PRONUNCIATION", "opinion phrases · contrast, addition or example?")])
    st = [("In my opinion, <b>organic</b> food is a <b>luxury</b>.", ""), ("Personally, I think all schools should teach people how to cook.", ""),
          ("From my point of view, supermarkets use too much plastic <b>packaging</b>.", ""), ("As far as I'm concerned, <b>reducing food miles</b> helps fight climate change.", ""),
          ("If you ask me, a <b>vegetarian diet</b> has lots of <b>benefits</b>.", "")]
    stl = "".join(f"<li>☐ {s}</li>" for s, _ in st)
    mm = [("positive effects", "benefits"), ("the food someone usually eats", "diet"), ("how far food travels from the farm to you", "food miles"), ("an expensive thing that is nice but not necessary", "luxury"),
          ("produced in a natural way, without artificial chemicals", "organic"), ("the bags, boxes or plastic that food is sold in", "packaging"), ("making something smaller", "reducing"), ("not eating meat", "vegetarian")]
    mml = "".join(f"<li>{d} {A(w, 'min-width:16mm')}</li>" for d, w in mm)
    b.page(f"""{sec(1, "Warm-up: food opinions", "8 min")}
<div style="display:flex;gap:2mm;margin-bottom:1mm">{"".join(img(l, 34, 20) for l in "ABCE")}</div>
<ol style="line-height:1.5;font-size:9pt;margin:0;list-style:none;padding-left:1mm">{stl}</ol>
{sub("A", "Find the words in bold. Write them next to the meanings.", "4 min")}
<ol style="line-height:1.45;font-size:8.8pt;margin:0;column-count:2;column-gap:5mm">{mml}</ol>
{sub("B", "Check (☐) one statement you agree with. Explain your opinion to your teacher.", "4 min")}""",
    22, """<ol><li>A: drill <i>luxury</i> /ˈlʌkʃəri/, <i>organic</i> /ɔːrˈɡænɪk/. The phrases at the start of each sentence (In my opinion…) are opinion phrases for the essay.</li>
<li>B: in Brazil, ask about weekly street markets, which usually use less packaging than supermarkets.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Food and environment vocabulary · opinion phrases</td><td>1</td></tr>
<tr><td>2 Reading</td><td>10 min</td><td>Ana's practice essay on organic food (audio 48.1) · A2 grammar review</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>How to write a good essay</td><td>3</td></tr>
<tr><td>+ Language reference</td><td>–</td><td>Writing an opinion essay</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>4 min</td><td>Opinion phrases · contrast, addition or example?</td><td>5</td></tr>
<tr><td>5 Practice</td><td>9 min</td><td>Complete an essay about vegetarian diets</td><td>6</td></tr>
<tr><td>6 Speaking and writing</td><td>12 min</td><td>Plan an essay: should schools teach cooking? · a food memory</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Ana (Neural2-F) is preparing for the TOEIC test (Units 31 and 34). The TOEIC Writing test includes an opinion essay, so Tom asks her to practice, and she writes about organic food and reads it aloud (48.1). This is a reading and writing lesson, as in Linguahouse. The essay avoids specific statistics: "organic food often costs much more" and "it may travel thousands of kilometers".</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students write one very long paragraph, use <i>In my opinion I think</i>, forget the comma after linking words (<i>However it is…</i>), ask several rhetorical questions, and use contractions and <i>gonna</i> in formal essays.</div>
<div class="box"><h4>AUDIO</h4>Track 48.1 Ana's essay (slow and natural) · Track 48.2 Repeat: opinions · Track 48.3 Contrast, addition or example?</div>""")

    # Page 2
    qq = [("This text is", ["a story", "a magazine article", "an essay"], "an essay"), ("Ana gives", ["one", "two", "three"], "two", "reasons for eating organic food."),
          ("She gives", ["one", "two", "three"], "three", "reasons why it's difficult."), ("Ana", ["gives", "doesn't give"], "gives", "her own opinion.")]
    qql = "".join(f"<li>{q[0]} {ch(q[1], q[2])} {q[3] if len(q) > 3 else ''}</li>" for q in qq)
    essay = f"""<div class="box" style="font-size:8.8pt;line-height:1.6;background:#fff"><b style="color:#176074">Should we buy organic food?</b><br>
{ch(["The", "—"], "—", "A")} organic food is becoming more and more popular these days. However, it can be expensive, and some people are asking: {ch(["Do", "Are"], "Do", "B")} we really need to eat organic food?<br>
Organic food has several benefits. Many people think it is better for our bodies and for the environment because it is {ch(["producing", "produced"], "produced", "C")} without artificial chemicals. In addition, many people are worried about how animals are treated on farms. Farmers who produce organic meat, milk and eggs believe it is important that their animals live in good conditions.<br>
However, {ch(["to find", "finding"], "finding", "D")} organic food at the supermarket can be difficult. In addition, organic fruit and vegetables often cost much more. Many people do not want to spend so much money {ch(["for", "to"], "to", "E")} be healthy. Another problem is that some organic food comes from very far away. For example, it may travel thousands of kilometers to reach the store. From my point of view, it is important {ch(["to", "that"], "that", "F")} we cut down {ch(["on", "for"], "on", "G")} food miles.<br>
In conclusion, you should buy organic food if you have {ch(["too much", "enough"], "enough", "H")} money, but you {ch(["must not", "do not have to"], "do not have to", "I")} put it on your {ch(["dinner plate", "plate of dinner"], "dinner plate", "J")} at every meal.</div>"""
    lp = [("a gerund as the subject (Unit 37)", "D"), ("no article: something in general (Unit 38)", "A"), ("noun + noun for an everyday thing (Unit 39)", "J"), ("a quantifier: no problem with the amount (Unit 41)", "H"),
          ("something necessary (Unit 42)", "F"), ("you can choose: not necessary (Unit 43)", "I"), ("to + verb for the result you want (Unit 44)", "E"), ("a passive (Unit 45)", "C"),
          ("a phrasal verb (Unit 46)", "G"), ("a question that introduces the topic (Unit 47)", "B")]
    lpl = [f'<li value="{i+1}">{s} {A(l, "min-width:6mm;text-align:center")}</li>' for i, (s, l) in enumerate(lp)]
    b.page(f"""{sec(2, "Reading: Ana's essay", "10 min")}
<div style="display:flex;gap:2.5mm;align-items:center"><p style="flex:1;margin:0">The TOEIC Writing test has an opinion essay, so Ana writes a practice essay for Tom. Read it quickly.</p>{img('D', 28, 18)}</div>
{sub("A", "Read quickly and choose.", "2 min", "48.1 · SLOW")}
<ol style="margin:0;line-height:1.6;font-size:9pt">{qql}</ol>
{sub("B", "Read again and choose the correct options A–J. Then listen and check.", "4 min", "48.1 · NATURAL")}
{essay}
{audiocard(["48.1 · SLOW", "48.1 · NATURAL"])}
{sub("C", "Grammar review: match A–J with the language points.", "4 min")}
<div style="font-size:8.4pt">{twocol(lpl, 6)}</div>""",
    27, """<ol><li>C reviews Units 37–47; these points also make an essay stronger in an exam. Skip C if time is short.</li>
<li>The TOEIC Writing test includes an opinion essay task (ETS); the student should aim for clear structure rather than long sentences.</li></ol>""")

    # Page 3
    fn = [("From my point of view, it is important that we cut down on food miles.", "opinion"), ("It is better for the environment because it is produced without chemicals.", "reason"),
          ("For example, it may travel thousands of kilometers to reach the store.", "example")]
    fnl = "".join(f"<li>{s} {A(f, 'min-width:16mm')}</li>" for s, f in fn)
    b.page(f"""{sec(3, "Language focus: how to write a good essay", "10 min")}
{sub("A", "Start with a short introduction.", "2 min")}
<p style="margin:.3mm 0;line-height:1.7">The general topic of Ana's essay is {ch(["being vegetarian", "staying healthy", "organic food"], "organic food")}. The specific question is {ch(["Should we buy organic food?", "Will we live longer?", "Why is it better?"], "Should we buy organic food?")}</p>
<p class="small" style="margin:0">Tip: a question in the introduction focuses the essay, but don't ask more questions later.</p>
{sub("B", "Organize your ideas.", "2 min")}
<p style="margin:.3mm 0;line-height:1.7">Paragraphs {ch(["make the essay look longer", "help the reader follow your ideas"], "help the reader follow your ideas")}. Paragraph 3 starts with <i>However</i>. It shows {ch(["contrast", "a similar idea", "cause and effect"], "contrast")}.</p>
{sub("C", "Explain your ideas. Is each sentence a reason, an example or an opinion?", "3 min")}
<ol style="margin:0;line-height:1.5;font-size:9pt">{fnl}</ol>
{sub("D", "Make a strong finish.", "3 min")}
<p style="margin:.3mm 0;line-height:1.7">How does Ana feel? {A("She agrees in some ways and disagrees in others.", "min-width:60mm")} How does she give advice? {A("with should and do not have to", "min-width:44mm")}</p>
<div class="box sand"><h4>RULE</h4>A good essay has: an <b>introduction</b> (topic + one question) · <b>paragraphs</b> with one idea each and <b>linking words</b> (In addition, However, For example) · <b>reasons, examples and opinions</b> · a <b>conclusion</b> with your opinion or advice · a good <b>range of language</b>. Leave time to check! More on the next page: <b>Language reference</b>.</div>""",
    25, """<ol><li>Go through A–D with the essay on page 2 open. A rhetorical question in the introduction is fine at this level, but only one.</li>
<li>Tell the student examiners look for organization first, then a range of grammar and vocabulary.</li></ol>""")

    grammar_ref.opinion_essay(b)

    # Page 5
    cae = ["contrast", "addition", "example", "contrast", "addition", "example"]
    cael = "".join(f"<li>{A(x, 'min-width:16mm')}</li>" for x in cae)
    b.page(f"""{sub("E", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't write</th><th>Write</th><th>Why?</th></tr>
<tr><td>In my opinion I think it's good.</td><td><b>In my opinion, it is good.</b></td><td>don't repeat.</td></tr>
<tr><td>However organic food is expensive.</td><td><b>However, organic food is expensive.</b></td><td>comma after linkers.</td></tr>
<tr><td>Is it good? Is it bad? Why?</td><td><b>Do we really need organic food?</b></td><td>only one question.</td></tr>
<tr><td>It's gonna be better.</td><td><b>It is going to be better.</b></td><td>formal: no gonna.</td></tr>
<tr><td>(one long paragraph)</td><td><b>four paragraphs</b></td><td>one idea each.</td></tr>
<tr><td>The organic food is expensive.</td><td><b>Organic food is expensive.</b></td><td>in general: no the.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "4 min")}
{audiocard(["48.2", "48.3"])}
{sub("A", "Listen and repeat. Pause after the opinion phrase.", "2 min", "48.2")}
{twocol([f'<li value="{i+1}">{s}</li>' for i, s in enumerate(S482)], 4)}
{sub("B", "Listen to six sentences. Does the linking word show contrast, addition or an example?", "2 min", "48.3")}
<ol style="line-height:1.5;column-count:3;column-gap:5mm">{cael}</ol>""",
    30, """<ol><li>A: a short pause after the opinion phrase = the comma in writing: <i>From my point of view, | it's important.</i></li>
<li>B: script: 1 However, it can be expensive. 2 In addition, it's better for animals. 3 For example, apples can travel very far. 4 On the other hand, it's difficult to find. 5 Also, it uses less plastic. 6 For instance, my local market sells it.</li></ol>""")

    # Page 6
    gaps = ["are giving up", "advantages and disadvantages", "animals are treated", "don't have to", "eating beans instead", "to make space", "not enough choice", "they eat out", "It's important that", "I am concerned"]
    g = {i + 1: A(w, "min-width:30mm") for i, w in enumerate(gaps)}
    vtxt = f"""<div class="box" style="font-size:8.8pt;line-height:1.85;background:#fff">It used to be unusual to meet a vegetarian. However, nowadays many people <sup>1</sup>{g[1]} meat and even other animal products like milk and eggs. What are the <sup>2</sup>{g[2]} of a vegetarian diet?<br>
Most vegetarians made their decision because they are worried about how <sup>3</sup>{g[3]}. They think it is wrong to take a life when they <sup>4</sup>{g[4]}. For example, <sup>5</sup>{g[5]} of meat can give you a healthy diet. Other vegetarians want to help the planet. They think it is wrong to cut down forests <sup>6</sup>{g[6]} for farm animals.<br>
However, there are some difficulties. Vegetarians may find that there is <sup>7</sup>{g[7]} on the menu when <sup>8</sup>{g[8]}. Also, some say their families do not understand their choice.<br>
To conclude, giving up meat is a difficult decision. <sup>9</sup>{g[9]} vegetarians have the right to choose how they eat. As far as <sup>10</sup>{g[10]}, if other people don't want to make this choice, they don't have to.</div>"""
    b.page(f"""{sec(5, "Practice", "9 min")}
{sub("A", "Read this essay quickly. Then complete it with the phrases in the box.", "7 min")}
<div class="bank">advantages and disadvantages · animals are treated · are giving up · don't have to · eating beans instead · I am concerned · It's important that · not enough choice · they eat out · to make space</div>
{vtxt}
{sub("B", "Can you think of another point for this essay? Are there many vegetarians in Brazil?", "2 min")}""",
    22, """<ol><li>A: after checking, ask the student to find the paragraphs, the linking words, and one reason, one example and one opinion.</li>
<li>The phrases review gerunds (eating beans), passives (are treated), phrasal verbs (giving up, eat out) and <i>don't have to</i>.</li></ol>""")

    # Page 7
    pro = ["It's fun.", "Children who learn to cook will be healthier adults.", "Cooking teaches other things, like math.", "your idea:"]
    con = ["Ingredients are expensive.", "It can be dangerous.", "Schools don't have time; other subjects are more important.", "your idea:"]
    tbl = "".join(f"<tr><td>{p}</td><td style='width:12mm'></td><td>{c}</td><td style='width:12mm'></td></tr>" for p, c in zip(pro, con))
    model = "In my opinion, all schools in Brazil should teach basic cooking. First of all, children who can cook will eat better as adults. For example, they can make a simple, healthy lunch instead of buying fast food. However, ingredients are expensive for many schools. In conclusion, I think schools should start with one easy class a month."
    b.page(f"""{sec(6, "Speaking and writing: plan an essay", "12 min")}
<div class="box" style="margin:0;font-size:9pt"><b>Essay task:</b> In the past, people learned to cook at home. Nowadays, some schools teach children to cook basic healthy meals. <b>Should all schools in Brazil teach cooking?</b></div>
{sub("A", "Number the ideas in each column in order of importance (1 = most important).", "3 min")}
<table style="margin:0;font-size:8.8pt"><tr><th>reasons for</th><th>#</th><th>difficulties</th><th>#</th></tr>{tbl}</table>
{sub("B", "Discuss with your teacher: which two ideas from each column will you use? What reasons or examples can you give? What's your opinion?", "4 min")}
<p class="small" style="margin:0">{R("Teacher's model opinion: " + model) if T else ""}</p>
{sub("C", "Write your introduction (2–3 sentences). Include one question.", "3 min")}
<div class="wline"></div><div class="wline"></div>
{sub("D", "A food memory. Talk for one minute: a food you learned to cook, or a special meal someone cooked for you.", "2 min")}""",
    22, """<ol><li>B: share the model in red only after the student gives their own ideas; point out the linkers and the opinion phrase.</li>
<li>D: this is like the IELTS speaking long turn; time one minute and give one positive comment and one correction.</li></ol>""")

    # Page 8
    pc = [("A2 Unit 45", "I can describe a process with the present simple passive."), ("A2 Unit 46", "I can use food phrasal verbs with the correct word order."),
          ("A2 Unit 47", "I can ask correct questions in different tenses."), ("A2 Unit 48", "I can plan and write a short opinion essay.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = ["However", "For example", "Another", "In addition", "In conclusion", "Personally"]
    h = {i + 1: A(w, "min-width:20mm") for i, w in enumerate(hw)}
    htxt = f"""<div class="box" style="font-size:8.8pt;line-height:1.85;background:#fff">How can we make better shopping choices for the planet? One important thing is packaging. Supermarkets use a lot of plastic, especially for fruit and vegetables. <sup>1</sup>{h[1]}, street markets usually use much less. <sup>2</sup>{h[2]} problem is food that is out of season. <sup>3</sup>{h[3]}, strawberries in winter may travel very far to reach us. Local markets often sell food from nearby farms. <sup>4</sup>{h[4]}, they help local farmers. <sup>5</sup>{h[5]}, our shopping choices are important. <sup>6</sup>{h[6]}, I buy fresh food at the market and the rest at the supermarket.</div>"""
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p style="margin:.5mm 0"><b>1. Complete the short essay with: Another · For example · However · In addition · In conclusion · Personally.</b></p>
{htxt}
<p style="margin-top:1.5mm"><b>2. Your essay (50–75 words).</b> Write the introduction and the conclusion of your essay from page 7 (schools and cooking). Use one question in the introduction and an opinion phrase in the conclusion.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class: correct the introduction and conclusion for structure first, then grammar; the student can write the full essay (two body paragraphs) as an extra challenge. Unit 49 is Review 5, the last unit of A2 Bridge.</p>""")

    b.extra("Audio script", f"""
{sub("48.1", "Ana's essay (slow and natural)")}
<p style="line-height:1.4">{"<br>".join(S481)}</p>
{sub("48.2", "Repeat: opinions")}
<p>{" · ".join(S482)}</p>
{sub("48.3", "Contrast, addition or example? (3-second pause)")}
<p>{" · ".join(S483)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 48 - On my plate")
