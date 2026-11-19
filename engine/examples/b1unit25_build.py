# Speak! Progress B1 - Unit 25 "Sightseeing" (all English) - lean B1 format
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
setup(band="B1 · UNIT 25", audio_json="audio_b1-unit-25.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-25"]
_yrs = {"fifteen fifty-four": "1554", "nineteen thirteen": "1913", "nineteen sixty-seven": "1967", "nineteen eleven": "1911",
        "nineteen twenty-two": "1922", "nineteen thirty-three": "1933"}
def _num(s):
    for k, v in _yrs.items():
        s = s.replace(k, v)
    return s
S251 = [_num(l) for l in _r["25.1 A walking tour of São Paulo"].split("\n")]
S252 = [_num(x.split(": ", 1)[1]) for x in _r["25.2 Repeat: pauses in relative clauses"].split("\n")]


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
    cover = cover_html(T, "LEVEL B1 · UNIT 25", "Sightseeing", "A walking tour of São Paulo · <b>who, which, where</b> with commas",
                       [("YOU CAN", "describe places of interest, give a short tour of your city and add extra information"),
                        ("LANGUAGE", "touristy · lively · picturesque · take photographs · the cathedral, which is Neo-Gothic, …"),
                        ("PRONUNCIATION", "pauses around extra information")])
    kw = [("having too many tourists", "touristy"), ("full of life and activity", "lively"),
          ("with people from many different countries and cultures", "cosmopolitan"), ("pretty and charming, like a postcard", "picturesque"),
          ("full of people", "crowded"), ("far from other towns and cities, hard to reach", "remote")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:22mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Warm-up: places of interest", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["When you travel, do you visit museums, markets or churches? Why?", "What do you usually do on vacation?", "Which places in your country are popular with tourists?"], "START TALKING")}</div></div>
{sub("A", "Key words. Write the adjectives from the box next to the definitions.", "3 min")}
<div class="bank">cosmopolitan · crowded · lively · picturesque · remote · touristy</div>
<div style="font-size:8.7pt">{twocol(kwl, 3)}</div>
{talk(["Describe the last place you visited as a tourist. Use two of the adjectives.", "Is your city lively, crowded or picturesque? Is it touristy?"], "USE THE WORDS")}""",
    26, """<ol><li>Start with the questions in the top box: this is speaking time, not a test. 4 minutes.</li>
<li>A: quick check (3 minutes), then the two questions with the new words. <i>Touristy</i> is negative; <i>picturesque</i> is positive. Stress: <i>pictur<b>esque</b>, cosmo<b>pol</b>itan</i>.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("A walking tour of downtown São Paulo with Danny · order the stops · match the dates · Talk about it",
                      "non-defining relative clauses: who, which, where, whose (with commas)", "Complete, choose · Use it (oral)",
                      "Giving a tour (25.2 pauses) · the student gives you a tour of their city", "Paulo's blog · join sentences · word choice · writing"),
        """The Linguahouse lesson is vocabulary only (places of interest, tourism phrases, adjectives to describe places). We added non-defining relative clauses, which guides and guidebooks use all the time. Danny, a weekend guide for City Steps Tours (Units 07–08), leads a walking tour downtown. In the homework, Paulo (Unit 15) writes about Belém, Lisbon. Verified facts: São Paulo was founded at Pátio do Colégio on January 25, 1554 (today's building is a reconstruction with a museum); the Neo-Gothic cathedral was begun in 1913, consecrated in 1954, towers finished in 1967, dome inspired by Florence (Wikipedia); the Theatro Municipal opened in 1911, inspired by the Paris Opera, and hosted Modern Art Week in 1922 (theatromunicipal.org.br); the Mercado Municipal opened in 1933, stained glass shows farming and food (gpsmycity, PPS); Belém Tower 1514–1520, Pastéis de Belém since 1837, tram 15E to Belém (Visit Lisboa, Rough Guides).""",
        """Brazilians use <i>that</i> after a comma (<i>the cathedral, that…</i>), repeat the object (<i>which I visited it</i>), use <i>where … there</i>, and say <i>I know Paris</i> for <i>I've been to Paris</i>. Also <i>tourist places</i> → <i>tourist attractions / places of interest</i>.""",
        "Track 25.1 A walking tour of São Paulo (natural and slow) · Track 25.2 Repeat: pauses in relative clauses"))

    # Page 2 - Listening
    gist = [("the cathedral", "2"), ("the market", "4"), ("Pátio do Colégio", "1"), ("the theater", "3")]
    gl = " &nbsp;·&nbsp; ".join(f"{A(n, 'min-width:6mm')} {p}" for p, n in gist)
    dates = [("1554", "the city was founded"), ("1913", "work on the cathedral started"), ("1967", "the cathedral towers were finished"),
             ("1911", "the theater opened"), ("1922", "Modern Art Week"), ("1933", "the market opened")]
    order = ["the cathedral towers were finished", "the city was founded", "the market opened", "Modern Art Week", "the theater opened", "work on the cathedral started"]
    letters = "abcdef"
    dl = "".join(f"<li><b>{y}</b> {A(letters[order.index(e)], 'min-width:7mm')}</li>" for y, e in dates)
    ol = "".join(f"<li>{e}</li>" for e in order)
    b.page(f"""{sec(2, "Listening: a walking tour", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{audiocard(["25.1 · NATURAL", "25.1 · SLOW"])}
{sub("A", "Danny gives a walking tour of downtown São Paulo. Listen and number the stops 1–4.", "2 min", "25.1")}
<p style="margin:.3mm 0;font-size:8.9pt">{gl}</p></div>{img('B', 40, 27)}</div>
{sub("B", "Listen again. Match the years 1–6 with the events a–f.", "4 min")}
<div style="display:flex;gap:6mm;font-size:8.8pt"><ol style="margin:0;line-height:1.6;columns:2;flex:1">{dl}</ol><ol type="a" style="margin:0;line-height:1.6;flex:1.4">{ol}</ol></div>
{talk(["Which stop would you like most? Why?", "Is it important to preserve old buildings? Why?", "Do you prefer a tour with a guide or exploring alone?"])}""",
    29, """<ol><li>A–B: 6 minutes. Play the natural version; use the slow one only if needed. All facts are verified (see the story box). Ask: <i>Is the Mercadão touristy?</i> (Danny: a bit, but locals shop there too).</li>
<li>Talk about it: 7 minutes. If the student knows São Paulo, ask what they would add to the tour. Note sentences you can rephrase with <i>which / who</i> for page 3.</li></ol>""")

    # Page 3 - Grammar reference
    lean.grammar_in_class(b, grammar_ref.non_defining_relative_clauses)

    # Page 4 - Practice
    fs = [("Our walk starts at Pátio do Colégio, ___ the city was founded in 1554.", "where"), ("This is São Paulo Cathedral, ___ is my favorite building in the city.", "which"),
          ("Our next stop is the Theatro Municipal, ___ opened in 1911.", "which"), ("Danny, ___ is from Chicago, works for City Steps Tours.", "who"),
          ("Paulo, ___ photos are amazing, loves markets.", "whose")]
    fsl = "".join(f"<li><i>{s.replace('___', A(a, 'min-width:16mm'))}</i></li>" for s, a in fs)
    use = ["Tell me about your city: <i>My city, which…, is…</i>", "Talk about a friend or relative: <i>My…, who…, …</i>", "Talk about a place you visited: <i>…, where I…, was…</i>",
           "Describe your favorite restaurant: <i>…, which…, …</i>", "Talk about a famous building in your country: <i>…, which was built…, …</i>"]
    b.page(f"""{sec(4, "Practice: who, which, where", "10 min")}
{sub("A", "Complete the sentences with who, which, where or whose.", "3 min")}
<div class="bank">where · which · who · whose</div>
<ol style="line-height:1.85;font-size:8.9pt;margin:0">{fsl}</ol>
{sub("B", "Choose.", "2 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0"><li>In <i>The cathedral, which is Neo-Gothic, …</i> the clause gives {ch(["extra information", "the information we need to know which one"], "extra information")}.</li>
<li>After a comma, you {ch(["can", "can't"], "can't")} use <i>that</i>.</li>
<li><i>The museum, which I visited <u>it</u>, …</i> is {ch(["correct", "wrong"], "wrong")}.</li></ol>
<div class="box sand"><h4>RULE</h4><b>who</b> (people) · <b>which</b> (things) · <b>where</b> (places) · <b>whose</b> (possession) + commas around the extra information · never <i>that</i> after a comma · no extra <i>it / there</i>. See the <b>Grammar reference</b> on page 3.</div>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    24, """<ol><li>A–B: 4 minutes. Point out the commas and the short pause in speech.</li>
<li>Use it: 6 minutes, all oral. Push for real extra information (<i>My city, which has about 300,000 people, is…</i>). Correct <i>that</i> after a comma every time.</li></ol>""")

    # Page 5 - Speaking
    S_tour = [("Is it safe at night?", "", ""), ("How much does it cost to go in?", "", ""), ("Where can I buy souvenirs?", "", ""), ("Where do the locals eat out?", "", ""),
              ("Is it very touristy?", "", ""), ("How do I get there?", "", "")]
    tq = " · ".join(f"<i>{q}</i>" for q, _, _ in S_tour)
    b.page(f"""{sec(5, "Speaking: give a tour", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.3pt"><tr><th>starting</th><th>showing</th><th>giving information</th><th>recommending</th><th>finishing</th></tr>
<tr><td><i>Welcome to… · I'll be your guide today. · Our walk starts here.</i></td><td><i>Here it is! · On your left / right, you can see… · Look up at…</i></td><td><i>It was built in… · It's famous for… · It's the place where…</i></td><td><i>It's worth visiting. · Don't miss… · Feel free to take photographs. · If you're hungry, try…</i></td><td><i>Our next stop is… · Finally, … · Thanks for walking with me!</i></td></tr></table></div>
{audiocard(["25.2"])}
{sub("A", "Listen and repeat. Pause before and after the extra information. Then underline the extra information in each sentence.", "4 min", "25.2")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.55">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S252))}</p>
{sub("B", "Give your teacher a walking tour of your city (or a city you know well). Plan three stops in 2 minutes. For each stop, say what it is, one fact with who / which / where, and one tip. Your teacher is the tourist and asks questions.", "14 min")}
<p class="small" style="margin:.3mm 0">The tourist may ask: {tq}</p>
<div style="display:flex;gap:2mm;margin-top:1mm">{"".join(f'<div class="box" style="flex:1;margin:0;min-height:12mm"><b>Stop {n}</b><br><span class="small">place · fact · tip</span></div>' for n in (1, 2, 3))}</div>
{talk(["What are the good and bad sides of being a tour guide?", "What would you show a foreign friend in your country in one day?"], "TALK ABOUT IT")}""",
    32, """<ol><li>A: the pauses come with the commas. Answers (extra information): 1 which is Neo-Gothic · 2 where the city was founded · 3 which opened in 1911 · 4 who was very funny · 5 which is always crowded · 6 where I lived for a year.</li>
<li>B: 12 minutes. 2 minutes to plan (notes only in the boxes). Be a curious tourist: interrupt with the questions in the list. Then swap: you give a 1-minute tour of a city you know and the student asks. Last 3 minutes: wrap-up (two corrections, and ask <i>Can you now give a short tour in English?</i>).</li></ol>""")

    # Homework
    pc = [(["which", "where"], "which"), (["where", "which"], "where"), (["who", "which"], "who"), (["which", "that"], "which"), (["whose", "who"], "whose")]
    p = [ch(o, a) for o, a in pc]
    rw = [("The Mercadão is in downtown São Paulo. It opened in 1933. (which)", "The Mercadão, which opened in 1933, is in downtown São Paulo."),
          ("My sister loves museums. She lives in Paris. (who)", "My sister, who lives in Paris, loves museums."),
          ("Ouro Preto is very picturesque. I spent a week there. (where)", "Ouro Preto, where I spent a week, is very picturesque.")]
    rwl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Paulo, Ana's brother, writes about Belém, in Lisbon, on his travel blog. Choose the correct words.", "")}</div>{img('C', 28, 18)}</div>
<div class="box" style="line-height:1.85;font-size:8.8pt;margin:.5mm 0"><b>Paulo's travel blog · A morning in Belém</b><br>Take tram 15E, {p[0]} goes along the river, to Belém. Start at Belém Tower, {p[1]} you can take the best photographs early in the morning. The tower was built between 1514 and 1520. Then walk to Pastéis de Belém. The bakers, {p[2]} start very early, have made custard tarts there since 1837. The line, {p[3]} is always long, moves fast. Don't buy souvenirs here: they're cheaper in town. My friend Rui, {p[4]} family is from Lisbon, says the best way to see the city is to meet the locals. He's right!</div>
{sub("B", "Join the sentences with the word in brackets. Use commas.", "")}
<ol style="line-height:1.5;font-size:8.7pt;margin:0">{rwl}</ol>
{lean.watch_out([("I know Paris.", "I've been to Paris.", "<i>know</i> a city = you know it very well; for a visit, say <i>have been to</i>."), ("We visited many tourist places.", "We visited many tourist attractions / places of interest.", "the usual phrases in English."), ("Let's take a walk in the city to know it.", "Let's walk around the city to see it / get to know it.", "<i>get to know</i> = start to know.")])}
{lean.writing_task(sub, "Describe a place you visited as a tourist for a travel blog: where it is, what to see, what to do and one tip.", "Last year I went to…, which is…", ["three places of interest", "who, which, where with commas", "three adjectives from page 1", "a tip", "100–150 words"], "I can describe places of interest and give a short tour.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class. The blog facts are verified (see the story box). Read the writing at home and choose two mistakes to discuss in class.</p>""")

    script = "".join(f"<p style='margin:.5mm 0'><b>{l.split(': ', 1)[0]}:</b> {l.split(': ', 1)[1]}</p>" for l in S251)
    b.extra("Audio script", f"""
{sub("25.1", "A walking tour of São Paulo (natural and slow)")}
<div style="line-height:1.3;font-size:8.6pt">{script}</div>
{sub("25.2", "Repeat: pauses in relative clauses")}
<p>{" · ".join(S252)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 25 - Sightseeing")
