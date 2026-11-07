# Speak! Bridge A2 - Unit 38 "The sights of Hannibal" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 38", audio_json="audio_a2-unit-38.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["a2-unit-38"]
S381 = [x.split(": ", 1)[1] for x in _r["38.1 Visit Hannibal, Missouri"].split("\n")]
S382 = [x.split(": ", 1)[1] for x in _r["38.2 Repeat: a, an and the"].split("\n")]
S383 = [x.split(". ", 1)[1] for x in [y.split(": ", 1)[1] for y in _r["38.3 The: /ðə/ or /ði/?"].split("\n")]]

ART = [
    "Hannibal, on the Mississippi River about 100 miles north of St. Louis, is where Mark Twain <b>grew up</b>. He was born in 1835 in Florida, Missouri, and his family moved to Hannibal when he was four. You'll have a great day exploring the town.",
    "The first place you'll want to visit is the Mark Twain <b>Boyhood</b> Home &amp; Museum. The Clemens family lived in the white house from about 1844 until 1853. Mark Twain's real name was Samuel Clemens. The museum has several <b>historic</b> buildings, including the Huckleberry Finn House.",
    "Outside the house, there's a white <b>fence</b>, just like the fence that Tom paints in <i>The Adventures of Tom Sawyer</i>. Everyone takes a photo there!",
    "If you have children, the best place to spend an afternoon is Mark Twain Cave, the oldest show cave in Missouri. Twain played there as a boy, and the cave is in <i>Tom Sawyer</i> too. Tours last about an hour.",
    "And if your feet hurt after walking around town, try a river <b>cruise</b>. The Mark Twain Riverboat has one-hour sightseeing cruises, and the guide tells stories about the river. There's also a dinner cruise in the evening.",
    "Another way to end your day is a visit to Rockcliffe Mansion, a big house on a hill above the town. It was finished in 1900, and some people say it's <b>haunted</b>! Twain visited Hannibal for the last time in 1902, and there was a <b>reception</b> for him at the mansion.",
    "Hannibal has so much to offer visitors. You'll never forget the day you visited this magical place."]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(n, opts, ans):
        return f"<sup><b>{n}</b></sup><b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 38", "The sights of Hannibal", "Mark Twain's hometown · <b>articles: a/an, the, no article</b>",
                       [("YOU CAN", "read a travel article, describe a place and use a/an, the and no article correctly"),
                        ("LANGUAGE", "a big house on a hill · the oldest cave · the Mississippi · Visitors love the town."),
                        ("PRONUNCIATION", "weak a and the · the /ðə/ or /ði/")])
    wf = [("Mark Twain was an American", "author", "who lived in the 19th and early 20th centuries."), ("\"Mark Twain\" was his", "pen name", "; his real name was Samuel Clemens."),
          ("His most famous", "novels", "are <i>The Adventures of Tom Sawyer</i> and <i>Adventures of Huckleberry Finn</i>."), ("Tom Sawyer and Huck Finn are two of his best-known", "characters", "."),
          ("As a young man, he worked as a", "riverboat", "pilot on the Mississippi River."), ("His name is a river expression: \"mark twain\" means the water is two fathoms (12 feet)", "deep", "."),
          ("People love his books because of their", "humor", ": they're very funny."), ("He traveled a lot and also wrote", "travel books", ".")]
    wfl = "".join(f"<li>{a} {A(w, 'min-width:20mm')}{'' if e[0] in '.;:' else ' '}{e}</li>" for a, w, e in wf)
    b.page(f"""{sec(1, "Warm-up: Mark Twain", "8 min")}
<div style="display:flex;gap:3mm;align-items:center"><p style="flex:1;margin:0">Mark Twain is one of the most famous American writers. Do you know anything about him?</p>{img('A', 38, 22)}</div>
{sub("A", "Complete the sentences with the words in the box.", "5 min")}
<div class="bank">author · characters · deep · humor · novels · pen name · riverboat · travel books</div>
<ol style="line-height:1.55;font-size:9pt;margin:0">{wfl}</ol>
{sub("B", "Talk about it.", "3 min")}
<p style="margin:0">Have you read anything by Mark Twain, or seen a movie of one of his books? Who is a famous writer from Brazil? Is there a town in Brazil connected to a famous writer?</p>""",
    22, """<ol><li>A: Twain (1835–1910) worked as a Mississippi steamboat pilot before he became a writer; <i>mark twain</i> was a call meaning two fathoms (12 feet), safe water for the boat. <i>Pen name</i> = a name a writer uses instead of the real one.</li>
<li>B: accept any answers; the student may mention Brazilian writers and their hometowns.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Mark Twain: author, novels, characters</td><td>1</td></tr>
<tr><td>2 Reading</td><td>10 min</td><td>Paulo's travel article about Hannibal, Missouri (audio 38.1)</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>a/an, the and no article</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Articles</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>4 min</td><td>Weak a and the · the /ðə/ or /ði/?</td><td>5</td></tr>
<tr><td>5 Practice</td><td>9 min</td><td>Choose the article · vocabulary from the article</td><td>6</td></tr>
<tr><td>6 Speaking and writing</td><td>12 min</td><td>Present a play, a historic town or a Brazilian writer</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Paulo (Neural2-I), who works at a travel agency in New York, writes an article about Hannibal, Missouri, for the agency's website, and reads it aloud (38.1). Linguahouse's Stratford-upon-Avon (Shakespeare) becomes Hannibal (Mark Twain's boyhood town). Facts: Twain was born in 1835 in Florida, Missouri, and grew up in Hannibal; the Clemens family lived in the Boyhood Home from about 1844 to 1853, and the museum runs several historic buildings, including the Huckleberry Finn House (Mark Twain Boyhood Home &amp; Museum, marktwainmuseum.org); Mark Twain Cave is Missouri's oldest show cave, Twain explored it as a boy, and guided tours last about 60 minutes; the Mark Twain Riverboat offers one-hour narrated sightseeing cruises and dinner cruises (marktwainriverboat.com); Rockcliffe Mansion was finished in 1900, and a reception was held there for Twain on his last visit to Hannibal in 1902; its "haunted" reputation is local legend.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Portuguese uses the article for things in general and with names and countries, so students say <i>The life is short</i>, <i>the Brazil</i>, <i>the Mark Twain</i>, and drop <i>a</i> with jobs (<i>He is engineer</i>). They also forget <i>the</i> with rivers and superlatives.</div>
<div class="box"><h4>AUDIO</h4>Track 38.1 Visit Hannibal, Missouri (slow and natural) · Track 38.2 Repeat: a, an and the · Track 38.3 The: /ðə/ or /ði/?</div>""")

    # Page 2
    qs = [("Who wrote this article?", "Paulo, a travel agent"), ("How long does the article suggest you spend in the town?", "one day"),
          ("How old was Twain when his family moved to Hannibal?", "four"), ("Where can you take a photo like a scene from Tom Sawyer?", "at the white fence outside the house"),
          ("How long is a cave tour? And a sightseeing cruise?", "about an hour; one hour")]
    ql = "".join(f"<li>{q} {A(a, 'min-width:28mm')}</li>" for q, a in qs)
    art = "".join(f"<p style='margin:0 0 1.2mm'><b>{i+1}</b> {t}</p>" for i, t in enumerate(ART))
    b.page(f"""{sec(2, "Reading: the sights of Hannibal", "10 min")}
<div style="display:flex;gap:2.5mm;align-items:center"><p style="flex:1;margin:0">Paulo writes articles for his travel agency's website. This week, he writes about a small town on the Mississippi River.</p>{img('B', 26, 18)}{img('C', 26, 18)}{img('E', 26, 18)}</div>
{sub("A", "Read the article and answer the questions.", "6 min", "38.1 · SLOW")}
<ol style="margin:0;line-height:1.45;font-size:8.8pt">{ql}</ol>
<div class="box" style="font-size:8.6pt;line-height:1.45;column-count:2;column-gap:5mm"><b style="color:#176074;font-size:10pt">Visit Hannibal, Missouri</b><br><i>A travel agent describes its top attractions</i><br>{art}<p class="small" style="margin:0;color:#666">Sources: marktwainmuseum.org · marktwainriverboat.com</p></div>
{audiocard(["38.1 · SLOW", "38.1 · NATURAL"])}
{sub("B", "Would you enjoy a day in Hannibal? Which place would you visit first?", "4 min")}""",
    22, """<ol><li>A: the audio is Paulo reading his article; use it for a second read-and-listen. Drill <i>cruise</i> /kruːz/, <i>haunted</i> /ˈhɔːntɪd/, <i>historic</i> /hɪˈstɔːrɪk/.</li>
<li>B: the Rockcliffe ghost is a local legend, not a fact; the bold words are practiced on page 6.</li></ol>""")

    # Page 3
    b.page(f"""{sec(3, "Language focus: a/an, the or no article", "10 min")}
{sub("A", "A/an. Match the sentences 1–3 with the uses a–c.", "3 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">1 Paulo is <b>a</b> travel agent. {A("b", "min-width:6mm")} · 2 You'll have <b>a</b> great day exploring the town. {A("a", "min-width:6mm")} · 3 Boats leave three times <b>an</b> hour. {A("c", "min-width:6mm")}<br>
<b>a</b> one of many similar things &nbsp; <b>b</b> a job &nbsp; <b>c</b> how often</div>
<p class="small" style="margin:.3mm 0">We use <b>an</b> before a vowel <b>sound</b>: <i>an hour</i> (the h is silent), <i>an old house</i>.</p>
{sub("B", "The. Match the sentences 1–4 with the uses a–d.", "3 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">1 It's <b>the</b> oldest show cave in Missouri. {A("b", "min-width:6mm")} · 2 Hannibal is on <b>the</b> Mississippi River. {A("d", "min-width:6mm")} · 3 The museum is next to <b>the</b> house. {A("c", "min-width:6mm")} · 4 People come from all over <b>the</b> world. {A("a", "min-width:6mm")}<br>
<b>a</b> there is only one &nbsp; <b>b</b> a superlative &nbsp; <b>c</b> we know which one &nbsp; <b>d</b> a river</div>
<p style="margin:.5mm 0;font-size:9pt">There's <b>a</b> white fence outside the house… Everyone takes a photo at <b>the</b> fence. Why <i>a</i> first and <i>the</i> later? {A("first time = new; second time = we know which one", "min-width:60mm")}</p>
{sub("C", "No article. Match the sentences 1–3 with the uses a–c.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">1 <b>Mark Twain</b> grew up in <b>Hannibal</b>. {A("b", "min-width:6mm")} · 2 <b>Children</b> love caves. {A("a", "min-width:6mm")} · 3 There's a cruise at <b>dinner</b> time. {A("c", "min-width:6mm")}<br>
<b>a</b> things in general &nbsp; <b>b</b> names of people and places &nbsp; <b>c</b> meals</div>
{sub("D", "Portuguese has articles too. Do we use them in the same way? Think about talking about life in general, countries and jobs.", "2 min")}
<div class="box sand"><h4>RULE</h4><b>a/an</b>: one of many, first mention, jobs, how often · <b>the</b>: we know which one, second mention, only one, superlatives, rivers and oceans · <b>no article</b>: general plurals and uncountables, names, most places, meals. More on the next page: <b>Grammar reference</b>.</div>""",
    25, """<ol><li>The main idea of <i>the</i>: speaker and listener know exactly which one.</li>
<li>D: Portuguese uses the article in general statements (<i>Life is short</i> has no article in English) and with countries, but no article with jobs (<i>He's a doctor</i> needs <i>a</i>).</li></ol>""")

    grammar_ref.articles(b)

    # Page 5
    sch = ["ðə", "ði", "ðə", "ði", "ðə", "ði"]
    scl = "".join(f"<li>{w} {A('/' + s + '/', 'min-width:12mm;text-align:center')}</li>" for w, s in zip(["the cave", "the afternoon", "the boat", "the end", "the town", "the oldest"], sch))
    scl_sb = "".join(f"<li>/ðə/ or /ði/? {A('/' + s + '/', 'min-width:12mm;text-align:center')}</li>" for s in sch)
    b.page(f"""{sub("E", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>The life is short.</td><td><b>Life is short.</b></td><td>in general.</td></tr>
<tr><td>I live in the Brazil.</td><td><b>I live in Brazil.</b></td><td>most countries: no article.</td></tr>
<tr><td>She is doctor.</td><td><b>She's a doctor.</b></td><td>jobs: a/an.</td></tr>
<tr><td>Mississippi is very long.</td><td><b>The Mississippi is very long.</b></td><td>rivers: the.</td></tr>
<tr><td>It's oldest cave in Missouri.</td><td><b>It's the oldest cave…</b></td><td>superlatives: the.</td></tr>
<tr><td>a hour · an university</td><td><b>an hour · a university</b></td><td>vowel sound.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "4 min")}
{audiocard(["38.2", "38.3"])}
{sub("A", "Listen and repeat. a and the are short and weak: /ə/, /ðə/.", "2 min", "38.2")}
{twocol([f'<li value="{i+1}">{s}</li>' for i, s in enumerate(S382)], 4)}
{sub("B", "Listen to six phrases. Does the sound like /ðə/ or /ði/? Write ðə or ði.", "2 min", "38.3")}
<ol style="line-height:1.5;column-count:3;column-gap:5mm">{scl if T else scl_sb}</ol>
<p class="small" style="margin:.5mm 0">Rule: <b>/ði/</b> before a vowel sound (<i>the end</i>), <b>/ðə/</b> before a consonant sound (<i>the boat</i>).</p>""",
    26, """<ol><li>A: <i>th</i> /ð/: tongue between the teeth, with voice; Brazilians often say /d/ (<i>da river</i>). <i>a</i> is /ə/, not /eɪ/, in normal speech.</li>
<li>B: script: 1 the cave 2 the afternoon 3 the boat 4 the end 5 the town 6 the oldest. Many Americans also use /ðə/ before vowels in fast speech; /ði/ is the clear, standard form.</li></ol>""")

    # Page 6
    ps = [(1, ["The", "—"], "—"), (2, ["a", "the"], "a"), (3, ["The", "A"], "The"), (4, ["a", "the"], "a"), (5, ["the", "—"], "—"), (6, ["The", "—"], "The"),
          (7, ["an", "a"], "an"), (8, ["A", "The"], "A"), (9, ["the", "a"], "the"), (10, ["the", "—"], "the"), (11, ["the", "—"], "—"), (12, ["a", "the"], "a")]
    c = {n: ch(n, o, a) for n, o, a in ps}
    ptxt = f"""<div class="box" style="font-size:9pt;line-height:1.75">{c[1]} visitors to Hannibal love taking {c[2]} trip on the Mark Twain Riverboat. {c[3]} boat was built in 1964, and it's {c[4]} paddlewheeler, like {c[5]} boats in Twain's time. {c[6]} sightseeing cruise lasts {c[7]} hour. {c[8]} guide tells stories about {c[9]} Mississippi, one of {c[10]} longest rivers in {c[11]} North America. There's also {c[12]} dinner cruise with live music.</div>"""
    vv = [("attractions", "interesting places that make people want to visit"), ("grew up", "spent your childhood somewhere"), ("boyhood", "the time when a man was a boy"),
          ("historic", "important in history, and very old"), ("fence", "a kind of wall made of wood or metal around a yard or garden"), ("cruise", "an enjoyable trip on a boat"),
          ("haunted", "with ghosts appearing often"), ("reception", "a formal party to welcome someone")]
    vs = sorted(vv, key=lambda x: x[1])
    vl = "".join(f"<li>{d} {A(w, 'min-width:20mm')}</li>" for w, d in vs)
    b.page(f"""{sec(5, "Practice", "9 min")}
{sub("A", "Choose the correct article (— = no article). Explain your choice.", "5 min")}
{ptxt}
<p class="small" style="margin:.5mm 0">{R("1 in general · 2 first mention, one of many · 3 we know which boat · 4 one of many · 5 boats in general · 6 we know which cruise · 7 vowel sound · 8 first mention · 9 a river · 10 superlative · 11 continent · 12 first mention") if T else ""}</p>
{sub("B", "Vocabulary. Find the words in bold in the article on page 2. Write them next to the meanings.", "4 min")}
<ol style="line-height:1.55;font-size:9pt;column-count:2;column-gap:5mm">{vl}</ol>""",
    25, """<ol><li>A: do number 1 together. The Mark Twain Riverboat was built in 1964 and offers one-hour sightseeing and dinner cruises (marktwainriverboat.com). The Mississippi is one of the longest rivers in North America.</li>
<li>B: the student uses the context of the article.</li></ol>""")

    # Page 7
    topics = [("a play or show you saw", "its name, when and where you saw it, what it was about, and whether you enjoyed it"),
              ("a historic town in Brazil", "its name and location, its buildings and how old they are, and one place to visit"),
              ("a famous Brazilian writer", "when they lived, what they wrote, why they're famous, and one book to read")]
    tl = "".join(f"<li><b>{t}</b>: say {d}.</li>" for t, d in topics)
    model = ("I want to talk about Ouro Preto, a historic town in Minas Gerais. It's in the mountains, about 100 kilometers from Belo Horizonte. "
             "The town has beautiful old churches and houses from the 18th century. The best place to visit is the main square. "
             "I think it's one of the most beautiful towns in Brazil.")
    b.page(f"""{sec(6, "Speaking and writing: tell me about it", "12 min")}
<div style="display:flex;gap:3mm;align-items:center"><p style="flex:1;margin:0">Choose one topic. You're going to talk about it and then write about it. Be careful with <b>a/an</b>, <b>the</b> and no article.</p>{img('F', 30, 20)}</div>
<ul style="margin:.5mm 0;line-height:1.5;font-size:9pt">{tl}</ul>
{sub("A", "Listen to your teacher's example. Which articles do you hear?", "2 min")}
<p class="small" style="margin:0">{R(model) if T else ''}</p>
{sub("B", "Make notes. Key words only, not full sentences.", "3 min")}
<div class="wline"></div><div class="wline"></div><div class="wline"></div>
{sub("C", "Tell your teacher about your topic. Your teacher asks questions and notes any article mistakes.", "4 min")}
{sub("D", "Start writing (50–75 words). Skip a line after each line, so your teacher has space for corrections.", "3 min")}
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<ol><li>A: the model uses <i>a historic town</i> (one of many), <i>the mountains</i>, <i>the main square</i> (we know which), <i>the most beautiful</i> (superlative) and no article with <i>Minas Gerais, Brazil</i>. Replace it with your own example if you like.</li>
<li>C–D: correct articles first; the student finishes the text at home.</li></ol>""")

    # Page 8
    pc = [("A2 Unit 35", "I can make suggestions and offers when I plan a day out."), ("A2 Unit 36", "I can write a clear, polite work email."),
          ("A2 Unit 37", "I can use -ing forms after verbs like enjoy and avoid, and as subjects."), ("A2 Unit 38", "I can use a/an, the and no article correctly.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hwt = ("Mark Twain's father, John Clemens, was {0} lawyer, but he never had much money. When Sam was eleven, his father died, and {1} family was very poor. "
           "Sam left school and got {2} job at {3} local newspaper. Later, he worked as {4} riverboat pilot on {5} Mississippi. He loved {6} river, and it's in many of his books. "
           "Today, {7} most famous American writer is still Mark Twain for many readers.")
    hwa = ["a", "the", "a", "a", "a", "the", "the", "the"]
    hwx = hwt.format(*[A(f"{a}", "min-width:7mm;text-align:center") if T else "___" for a in hwa])
    hwx = hwt.format(*[R(f"<b>{a}</b>") if T else "<span style='color:#999'>^</span>" for a in hwa])
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p style="margin:.5mm 0"><b>1. Eight articles are missing from this text. The ^ marks show where. Write a, an or the.</b></p>
<div class="box" style="font-size:9pt;line-height:1.8">{hwx}</div>
<p style="margin-top:1.5mm"><b>2. Finish your text from page 7 (50–75 words).</b> Check every article: a/an, the or no article?</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    24, """<p>Answers 1: a lawyer (job) · the family (we know which) · a job, a local newspaper (first mention) · a riverboat pilot (job) · the Mississippi (river) · the river (second mention) · the most famous (superlative). Twain's father died in 1847 and Sam left school to work for a printer and newspaper; he later trained as a Mississippi steamboat pilot.</p>""")

    b.extra("Audio script", f"""
{sub("38.1", "Visit Hannibal, Missouri (slow and natural)")}
<p style="line-height:1.4">{"<br>".join(S381)}</p>
{sub("38.2", "Repeat: a, an and the")}
<p>{" · ".join(S382)}</p>
{sub("38.3", "The: /ðə/ or /ði/? (3-second pause)")}
<p>{" · ".join(S383)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 38 - The sights of Hannibal")
