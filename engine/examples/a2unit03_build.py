# Speak! Bridge A2 - Unit 03 "In the forest" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 03", audio_json="audio_a2-unit-03.json", img_dir="img")

PHOTOS = [("A", "branches", "bare tree branches"), ("B", "a flower", "flower on a branch"), ("C", "a fruit", "apple on a tree"), ("D", "leaves", "leaves"),
          ("E", "roots", "tree roots"), ("F", "a seed", "acorn"), ("G", "a trunk", "tree trunk"), ("H", "bark", "tree bark")]

_r = json.load(open("roteiro.json"))["units"]["a2-unit-03"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["03.1 Podcast"].split("\n")]
S032 = [x.split(": ", 1)[1] for x in _r["03.2 Repeat words"].split("\n")]
S033 = [x.split(": ", 1)[1] for x in _r["03.3 Repeat sentences"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1: 8 photos (concrete vocabulary)
    cover = cover_html(T, "LEVEL A2 · UNIT 03", "In the forest", "Nature and the five senses · <b>action verbs and state verbs</b>",
                       [("YOU CAN", "listen to a podcast and describe a place with your five senses"),
                        ("LANGUAGE", "I'm smelling the leaf. It smells fresh. · I hear the birds. · I love it here."),
                        ("PRONUNCIATION", "leaf / leaves · branch / branches · rough /rʌf/ · It tastes sweet.")])
    grid = photo_grid(T, PHOTOS)
    b.page(f"""{sec(1, "Warm-up: parts of a tree", "8 min")}
{sub("A", "Look at the photos. Write the words under the photos.", "3 min")}
<div class="bank">a flower · a fruit · a seed · a trunk · bark · branches · leaves · roots</div>
{grid}
{sub("B", "Answer the questions.", "5 min")}
<ol><li>Which words are plural? What are the singular forms? {R("branches → branch, leaves → leaf, roots → root")}</li>
<li>Which part of a tree is under the ground? {R("the roots")} Which part feels rough? {R("the bark")}</li>
<li>Do you have a favorite tree? Is there a tree you remember from your childhood?</li></ol>""",
    22, """<ol><li>A: <b>bark</b> is uncountable (the "skin" of the trunk). A small, thin branch is <b>a twig</b>. An acorn is the seed of an oak tree.</li>
<li>B: <b>leaf → leaves</b> (f → ves, like <i>knife → knives</i>); <b>branches</b> has two syllables. For 3, Brazilian trees: ipê, mango tree, jabuticaba tree, cashew tree.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Parts of a tree</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>A podcast: forest bathing in Central Park</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Sense verbs as actions and descriptions · state verbs · present simple and continuous</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Action and state verbs · sense verbs · simple or continuous</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>5 min</td><td>Singular and plural · sense sentences</td><td>5</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Paulo's blog · correct the mistakes · Word builder: sense adjectives</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Guess the place · nature and the senses</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework (50–75 words)</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Paulo, now a photographer and tour guide in New York, takes visitors on slow Saturday walks in the <b>North Woods</b> of Central Park. The host of <i>Green City</i>, a podcast about nature in New York (invented), tries forest bathing with him. Paulo remembers his grandmother Lourdes's mango tree in Brazil. Facts: the North Woods is a 40-acre woodland in the north of Central Park, and the Loch is a stream that runs through it into the Harlem Meer (Central Park Conservancy, centralparknyc.org, "North Woods" and "The Loch"). Forest bathing (<i>shinrin-yoku</i>) comes from Japan, where the term was created in 1982 (The Washington Post, "Forest bathing is great for your health").</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Portuguese often uses the continuous with state verbs, so students say <i>I'm hearing a noise, I'm understanding</i> ✗ → <b>I hear / I can hear a noise, I understand</b>. They also use the continuous for descriptions (<i>The soup is tasting good</i> ✗ → <b>tastes good</b>), adverbs after sense verbs (<i>It smells well</i> ✗ → <b>good</b>) and the calque <i>I feel the smell of coffee</i> ✗ → <b>I can smell coffee</b>.</div>
<div class="box"><h4>AUDIO</h4>Track 03.1 The podcast (slow and natural) · Track 03.2 Words · Track 03.3 Sentences</div>""")

    # Page 2: listening
    gist = [("Where are Paulo and the host?", "In the North Woods, in Central Park, New York."), ("What is forest bathing?", "Time with the trees: you walk slowly, breathe and use your five senses. No rules."),
            ("How does the host feel at the end?", "Much calmer. She wants to do it again.")]
    gl = "".join(f"<li>{q}<div class='wline'>{R(a)}</div></li>" for q, a in gist)
    vf = [(["'m looking", "look"], "'m looking", "I", "at this old oak tree."), (["'s looking", "looks"], "looks", "It", "enormous!"),
          (["'m listening", "listen"], "'m listening", "I", "very carefully…"), (["'m hearing", "hear"], "hear", "I", "water."),
          (["'s sounding", "sounds"], "sounds", "It", "so peaceful."), (["'m smelling", "smell"], "'m smelling", "I", "it now…"),
          (["'s smelling", "smells"], "smells", "It", "fresh, like rain."), (["'m touching", "touch"], "'m touching", "OK, I", "it."),
          (["'s feeling", "feels"], "feels", "It", "rough and cold."), (["'m understanding", "understand"], "understand", "I", "why people come back.")]
    vfl = [f'<li value="{i+1}">{a} {ch(o, r)} {c}</li>' for i, (o, r, a, c) in enumerate(vf)]
    b.page(f"""{sec(2, "Listening: forest bathing in the city", "10 min")}
<p>Paulo lives in New York now. On Saturdays he takes visitors on slow walks in Central Park. Today the host of <i>Green City</i>, a podcast about nature, walks with him.</p>
{audiocard(["03.1 · SLOW", "03.1 · NATURAL"])}
{sub("A", "Listen and answer the questions.", "3 min", "03.1 · SLOW")}
<ol>{gl}</ol>
{sub("B", "Listen again. Choose the verb form you hear.", "5 min", "03.1 · NATURAL")}
{twocol(vfl, 5)}
{sub("C", "Would you like to go on Paulo's walk? Is there a place like the North Woods in your city?", "2 min")}""",
    22, """<p>A: play the slow version first. Explain <b>forest bathing</b> (from Japanese <i>shinrin-yoku</i>; no water!). B: the student guesses first, then listens to check. Elicit the two forms: <b>present continuous</b> and <b>present simple</b>; this leads into page 3. If there's time, read the script together (TB last page): you are the host, the student is Paulo.</p>""")

    # Page 3
    b.page(f"""{sec(3, "Language focus: action verbs and state verbs", "10 min")}
{sub("A", "Read the pairs from the podcast. Then choose the correct option.", "3 min")}
<table style="table-layout:fixed;margin-top:0"><tr><th>doing an action with a sense</th><th>describing what we experience</th></tr>
<tr><td>I'm looking at this oak tree.</td><td>It looks enormous!</td></tr>
<tr><td>I'm smelling the leaf.</td><td>It smells fresh.</td></tr>
<tr><td>I'm touching the bark.</td><td>It feels rough.</td></tr>
<tr><td>I'm listening very carefully.</td><td>It sounds so peaceful. · I hear water.</td></tr></table>
<ol><li>To talk about an action we are doing with our senses now, we use {ch(["present simple", "present continuous"], "present continuous")}.</li>
<li>To describe how something looks, smells, tastes, feels or sounds, we use {ch(["present simple", "present continuous"], "present simple")} + an {ch(["adjective", "adverb"], "adjective")}.</li>
<li><i>See</i> and <i>hear</i> are {ch(["action verbs", "state verbs"], "state verbs")}: <i>I hear water.</i> (or <i>I can hear water.</i>)</li></ol>
{sub("B", "State verbs. Complete the table with these verbs from the podcast.", "4 min")}
<div class="bank">hear · love · need · think · understand · want</div>
<table style="table-layout:fixed;font-size:9pt;margin-top:0"><tr><th>feelings</th><th>thinking</th><th>senses</th></tr>
<tr><td>{A("love, want, need", "min-width:28mm")}<br><span class="small">like, hate, prefer</span></td><td>{A("think, understand", "min-width:28mm")}<br><span class="small">believe, know, remember</span></td><td>{A("hear", "min-width:16mm")}<br><span class="small">see, smell / taste / feel (+ adjective)</span></td></tr></table>
{sub("C", "Action verbs: present simple or present continuous? Match.", "3 min")}
<table style="table-layout:fixed;margin-top:0"><tr><td>1. Every Saturday he <b>takes</b> visitors on a slow walk.</td><td>a. an action happening now</td></tr>
<tr><td>2. Right now we<b>'re walking</b> in the North Woods.</td><td>b. a routine or something always true</td></tr></table>
<p class="small">{R("1 b · 2 a")}</p>
<div class="box sand"><h4>RULE</h4>State verbs are not usually continuous: <i>I love it</i> (not <i>I'm loving it</i>). <b>think</b> has two meanings: <i>I think it's beautiful</i> (opinion, simple) · <i>What are you thinking about?</i> (action, continuous).</div>""",
    24, """<ol><li>A: point out that <b>look / smell / taste / feel / sound</b> + adjective work like <i>be</i>: <i>It smells fresh</i> = it is fresh (to my nose).</li>
<li>B: <i>think</i> here = opinion ("I think the city needs this"). <i>have</i> (= own) is also a state verb: <i>She has a mango tree.</i></li></ol>""")

    # Grammar reference (before Common mistakes)
    grammar_ref.action_state_verbs(b)

    # Page 4
    b.page(f"""{sub("D", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>I'm hearing a strange noise.</td><td><b>I hear / I can hear a strange noise.</b></td><td>hear is a state verb.</td></tr>
<tr><td>This soup is tasting delicious.</td><td><b>This soup tastes delicious.</b></td><td>description = simple.</td></tr>
<tr><td>It smells well.</td><td><b>It smells good.</b></td><td>sense verb + adjective.</td></tr>
<tr><td>She looks like tired.</td><td><b>She looks tired.</b></td><td>look + adjective; look like + noun.</td></tr>
<tr><td>I'm understanding you now.</td><td><b>I understand you now.</b></td><td>understand is a state verb.</td></tr>
<tr><td>I feel the smell of coffee.</td><td><b>I can smell coffee.</b></td><td>smell is the verb.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "5 min")}
{audiocard(["03.2", "03.3"])}
{sub("A", "Singular and plural. Listen and repeat. Which plural has an extra syllable?", "2 min", "03.2")}
<table style="table-layout:fixed;margin-top:0"><tr>{"".join(f"<td style='text-align:center'><b>{w}</b></td>" for w in S032)}</tr></table>
<p class="small">{R("branches /ˈbræntʃɪz/ has two syllables. leaf → leaves: /f/ → /v/. rough = /rʌf/ (gh = f) · smooth = /smuːð/")}</p>
{sub("B", "Sentences. Listen and repeat.", "2 min", "03.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S033)}</div>
<div class="box" style="margin-top:1mm"><h4>NO EXTRA VOWEL</h4>Say <b>tastes</b> /teɪsts/ and <b>smells</b> /smelz/ in one syllable: not <i>tasté-sis</i> or <i>is-mells</i>. <i>sweet</i>, <i>smells</i> and <i>sky</i> start with /s/, not /is/.</div>""",
    24, """<ol><li>4A: Brazilians often add a vowel: <i>branch-i, roots-i</i>. Keep the final consonants short and clean.</li>
<li>4B: stress the adjective: <i>It smells <b>FRESH</b>. It tastes <b>SWEET</b>.</i></li></ol>""")

    # Page 5
    blog = [("take", "take"), ("love", "love"), ("walk", "'m walking"), ("look", "are looking"), ("look", "look"), ("smell", "smells"),
            ("see", "see"), ("want", "want"), ("take", "'m taking"), ("feel", "feel"), ("need", "need")]
    g = [A(v, "min-width:17mm") for _, v in blog]
    blog_txt = (f"Every Saturday I <sup>1</sup>{g[0]} visitors to the North Woods. Today it's raining, but I <sup>2</sup>{g[1]} the woods in the rain! "
                f"Right now I <sup>3</sup>{g[2]} near the Loch with a family from Texas. The kids <sup>4</sup>{g[3]} for squirrels. "
                f"The trees <sup>5</sup>{g[4]} dark and beautiful, and the air <sup>6</sup>{g[5]} clean. Oh, I <sup>7</sup>{g[6]} a red bird on a branch! "
                f"I <sup>8</sup>{g[7]} a photo, so I <sup>9</sup>{g[8]} my camera out of my bag. My hands are wet, but I <sup>10</sup>{g[9]} happy. "
                f"Big cities <sup>11</sup>{g[10]} places like this.")
    cm = [("I'm walking in the Amazon rain forest.", "✓"), ("The trees are looking very tall.", "The trees look very tall."),
          ("I'm hearing a strange noise.", "I hear a strange noise."), ("A big jaguar is watching me!", "✓"),
          ("I'm wanting to run, but I can't.", "I want to run, but I can't."), ("The air is smelling of rain.", "The air smells of rain."),
          ("I'm thinking this is a dream.", "I think this is a dream."), ("I feel very scared.", "✓")]
    cml = [f'<li value="{i+1}">{s} {R(a)}</li>' for i, (s, a) in enumerate(cm)]
    wb = [("A lime tastes", "sour"), ("Jiló tastes", "bitter"), ("Malagueta pepper tastes", "spicy"), ("Brigadeiro tastes", "sweet"),
          ("A churrascaria smells", "smoky"), ("Toothpaste smells", "minty"), ("A cat's fur feels", "soft"), ("A mirror feels", "smooth"),
          ("Tree bark feels", "rough"), ("Honey feels", "sticky")]
    wbl = [f'<li value="{i+1}">{s} {A(w, "min-width:16mm")}.</li>' for i, (s, w) in enumerate(wb)]
    b.page(f"""{sec(5, "Practice", "8 min")}
{sub("A", "Paulo's photo blog. Complete with the present simple or continuous of the verbs.", "3 min")}
<div class="bank">feel · look (×2) · love · need · see · smell · take (×2) · walk · want</div>
<p style="line-height:1.9;margin:1mm 0">{blog_txt}</p>
{sub("B", "A strange dream. Correct the mistakes. Three sentences are correct.", "2 min")}
{twocol(cml, 4)}
{sub("C", "Word builder: sense adjectives. Complete with the words in the box.", "3 min")}
<div class="bank">bitter · minty · rough · smoky · smooth · soft · sour · spicy · sticky · sweet</div>
{twocol(wbl, 5)}""",
    22, """<ol><li>A: 7 <b>see</b> (or <i>can see</i>) is a state verb; 4 and 9 are actions now; 1 is a routine.</li>
<li>C: from the bonus lesson <i>In the forest</i> (Vocabulary to Go). Ask for more examples: <i>What tastes bitter / smells disgusting / feels sticky?</i></li></ol>""")

    # Page 6
    cards = ["a bakery at 7 a.m.", "a beach in Bahia", "Times Square at night", "a churrascaria", "a soccer stadium", "the Amazon after the rain"]
    cg = "".join(f"<td style='text-align:center;height:12mm;font-weight:600'>{c}</td>" + ("</tr><tr>" if i == 2 else "") for i, c in enumerate(cards))
    b.page(f"""{sec(6, "Speaking", "12 min")}
{sub("A", "Guess the place. Choose a place secretly. Describe it with three senses. Your teacher guesses. Then change roles.", "7 min")}
<table style="table-layout:fixed;margin-top:0"><tr>{cg}</tr></table>
<div class="msg" style="max-width:none;padding:2mm 4mm;line-height:1.55"><b>You:</b> I'm standing in a big, busy place. It smells smoky and delicious. I hear knives and loud conversations. The meat tastes amazing!<br><b>Teacher:</b> Is it a churrascaria? <b>You:</b> Yes!</div>
{sub("B", "Nature and the senses.", "5 min")}
<ol><li>Is there a park or a forest near your home? How often do you go there? How does it make you feel?</li>
<li>Do you think forest bathing is a good idea for people in big cities? Why / why not?</li>
<li>Which smell reminds you of your childhood?</li><li>Which sound do you love? Which sound do you hate?</li>
<li>Which food tastes better in Brazil than in other countries?</li></ol>""",
    26, """<ol><li>A: the student must use at least one continuous action (<i>I'm standing…</i>) and three descriptions (<i>It smells…</i>). Then you describe a place and the student guesses (ideas: a hospital, a farm, a subway station in New York).</li>
<li>B: correct <i>I'm loving / I'm hearing</i> and <i>It smells well</i>.</li></ol>""")

    # Page 7
    pc = [("A1 Unit 34", "I can give advice with should, could and imperatives."), ("A1 Unit 35", "I can explain rules with must, mustn't, can and can't."),
          ("A2 Unit 01", "I can ask about appearance, personality, likes and wishes."), ("A2 Unit 02", "I can use verb + to, verb + -ing and verb + person + to."),
          ("A2 Unit 03", "I can describe a place with my senses and use state verbs correctly.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    imgs = "".join(f"<div style='flex:1;text-align:center'><img src='{photo(l)}' style='width:100%;height:22mm;object-fit:cover;border-radius:1.5mm;display:block'><span class='small'><b>{l}</b> {c}</span></div>"
                   for l, c in (("I", "a forest at night"), ("J", "the Amazon rain forest"), ("K", "a forest in winter")))
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework: the Green City writing competition (50–75 words)", "1 min")}
<p style="margin:0 0 1mm">Imagine you are forest bathing in one of these places. Write a short text for the podcast's website.</p>
<div style="display:flex;gap:3mm;margin-bottom:1.5mm">{imgs}</div>
<div class="msg" style="max-width:none;padding:1.5mm 4mm;line-height:1.45;font-size:8.8pt"><b>Model:</b> I'm standing in a forest at night. I'm listening to an owl. It sounds a little scary, but I love it here. The air smells cold and fresh. I'm touching a tree, and its bark feels wet. I can see the moon through the branches. I feel calm, and I think I'm safe. (55 words)</div>
<p class="small" style="margin:1mm 0"><b>Steps:</b> 1. Choose a place. 2. Say what you're doing (present continuous). 3. Describe three senses (look / sound / smell / taste / feel + adjective). 4. Say how you feel and what you think.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class: the student reads the text aloud and you guess the place (night, Amazon or winter). Check every sense verb + adjective and the state verbs.</p>""")

    b.extra("Audio scripts", f"""
{sub("03.1", "The podcast: Green City (slow and natural)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("03.2", "Words")}
<p>{" · ".join(S032)}</p>
{sub("03.3", "Sentences")}
<p>{" ".join(S033)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 03 - In the forest")
