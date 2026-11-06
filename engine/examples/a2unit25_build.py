# Speak! Bridge A2 - Unit 25 "Last night's TV" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 25", audio_json="audio_a2-unit-25.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["a2-unit-25"]
S251 = [x.split(": ", 1) for x in _r["25.1 Coffee break"].split("\n")]
S252 = [x.split(": ", 1)[1] for x in _r["25.2 Repeat: -ed and -ing"].split("\n")]
S253 = [x.split(": ", 1)[1] for x in _r["25.3 Three -ed sounds"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 25", "Last night's TV", "TV shows and feelings · <b>-ed and -ing adjectives</b>",
                       [("YOU CAN", "talk about TV shows and say how they make you feel"),
                        ("LANGUAGE", "I thought it was a bit boring. · I got annoyed after five minutes. · I'm interested in history."),
                        ("PRONUNCIATION", "-ed: /d/ bored · /t/ shocked · /ɪd/ excited")])
    shows = [("Family Dinner: dinner at the Hobbs home is always full of surprises. This week, Grandma loses her glasses.", "sitcom"),
             ("Kingdom of Fire: the prince finds out that his best friend is really his sister, and the dragons are coming.", "drama"),
             ("Killer Dinosaurs: how dinosaurs used teeth, claws and speed to catch their food.", "documentary"),
             ("Tonight at Six: the latest political news, a report on crime and the weather.", "the news"),
             ("Sing My Song: five singers perform for famous judges, but only one can win.", "talent show"),
             ("On the Sofa with Jess: tonight's guests are a movie star, a tennis player and a chef.", "talk show"),
             ("Fix My House: can the team make a family's small house bigger and better in one week?", "makeover show"),
             ("Know-It-All: four people answer questions about history, art and sports to win a million dollars.", "game show")]
    sl = "".join(f'<li>{A(t, "min-width:22mm")} {d}</li>' for d, t in shows)
    b.page(f"""{sec(1, "Warm-up: types of TV shows", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">{sub("A", "Match the types of shows with the descriptions.", "5 min")}
<div class="bank">documentary · drama · game show · makeover show · sitcom · talent show · talk show · the news</div></div>{img('A', 34, 20)}</div>
<ol style="line-height:1.45;font-size:8.8pt">{sl}</ol>
{sub("B", "Talk about it.", "3 min")}
<ol><li>Which types of shows are popular in Brazil? Do you watch telenovelas (Brazilian soap operas)?</li><li>Which of the shows in A would you like to watch the most? Why?</li></ol>""",
    25, """<ol><li>A: a <b>sitcom</b> = situation comedy. In the US, people say <i>TV show</i> (British: <i>programme</i>) and <i>commercials</i> (British: <i>adverts</i>).</li>
<li>B: Brazilian telenovelas are a good topic; many students also watch series on streaming services. Drill <i>documentary</i> /ˌdɑːkjəˈmentəri/.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Types of TV shows</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Lucy and Rita talk about last night's TV</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>-ed and -ing adjectives · be / get / feel · prepositions</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>-ed and -ing adjectives: form, verbs, prepositions, pairs</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>4 min</td><td>-ed and -ing · three -ed sounds</td><td>5</td></tr>
<tr><td>5 Practice</td><td>9 min</td><td>Adjectives in context · Word builder: watching TV together</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>A 45-second mini-presentation about a TV show</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>On their coffee break at City Coffee, Lucy (Neural2-C) and Rita, the manager (Chirp3-HD-Aoede), talk about two shows they watched last night: <i>Kingdom of Fire</i>, a fantasy drama (Lucy loves it, Rita thinks it's boring), and <i>Fix My House</i>, a makeover show (they both enjoy it). All the shows in this unit are invented, so there are no facts to check.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students say <i>I'm boring</i> ✗ when they mean <i>I'm bored</i>, use <i>interesting in</i> / <i>excited for</i> instead of <i>interested in</i> / <i>excited about</i>, say <i>scaring</i> for <i>scary</i>, and pronounce every -ed as an extra syllable (<i>shock-ed</i> ✗).</div>
<div class="box"><h4>AUDIO</h4>Track 25.1 Coffee break (slow and natural) · Track 25.2 Repeat: -ed and -ing · Track 25.3 Three -ed sounds</div>""")

    # Page 2
    adj = [(["bored", "boring"], "boring", "Well, to be honest, I thought it was a bit", "."),
           (["excited", "exciting"], "excited", "Weren't you", "when the dragons flew in?"),
           (["surprised", "surprising"], "surprising", "That was a bit", ", I guess."),
           (["annoyed", "annoying"], "annoyed", "I got", "after about five minutes."),
           (["interested", "interesting"], "interesting", "It's always", "…"),
           (["shocked", "shocking"], "shocked", "…although I often feel", "by the changes they make."),
           (["amazed", "amazing"], "amazed", "I was", "by the color they painted the kitchen."),
           (["confused", "confusing"], "confusing", "What's really", "is how they can do so much in one week.")]
    al = [f'<li value="{i+1}">{a} {ch(o, r)}{e if e[0] in ".,…" else " " + e}</li>' for i, (o, r, a, e) in enumerate(adj)]
    b.page(f"""{sec(2, "Listening: last night's TV", "10 min")}
<div style="display:flex;gap:3mm;align-items:center"><p style="flex:1;margin:0">Lucy and Rita work together at City Coffee. On their coffee break, they talk about the TV shows they watched last night.</p>{img('C', 30, 21)}{img('D', 30, 21)}</div>
{audiocard(["25.1 · SLOW", "25.1 · NATURAL"])}
{sub("A", "Listen and answer the questions.", "3 min", "25.1 · SLOW")}
<ol style="line-height:1.55"><li>Which two shows did they watch last night? {A("Kingdom of Fire (a drama) and Fix My House (a makeover show)", "min-width:60mm")}</li>
<li>Do they agree about the first show? {A("No. Lucy loves it, but Rita thought it was boring.", "min-width:60mm")}</li>
<li>Do they agree about the second show? {A("Yes, they both enjoy it.", "min-width:40mm")}</li></ol>
{sub("B", "Choose the correct adjective. Then listen again and check.", "5 min", "25.1 · NATURAL")}
{twocol(al, 5)}
{sub("C", "Which adjectives in B are positive? Which are negative?", "2 min")}
<p class="small" style="margin:0">{A("positive: excited, surprising, interesting, amazed · negative: boring, annoyed, shocked, confusing", "min-width:110mm")}</p>""",
    22, """<ol><li>B: let the student guess first, then listen. Don't explain the rule yet; that's the next page.</li>
<li>C: <i>surprising</i> and <i>shocked</i> can be positive or negative; accept good reasons.</li></ol>""")

    # Page 3
    b.page(f"""{sec(3, "Language focus: -ed and -ing adjectives", "10 min")}
{sub("A", "Study the sentences from the conversation.", "2 min")}
<div style="display:flex;gap:3mm"><div class="box" style="flex:1;margin-top:1mm;font-size:9pt;line-height:1.55"><h4>-ING ADJECTIVES</h4>I thought <b>it</b> was a bit <b>boring</b>.<br><b>That</b> was a bit <b>surprising</b>.<br><b>It</b>'s always <b>interesting</b>.<br><b>What</b>'s really <b>confusing</b> is…</div>
<div class="box" style="flex:1;margin-top:1mm;font-size:9pt;line-height:1.55"><h4>-ED ADJECTIVES</h4>Weren't <b>you</b> <b>excited</b>…?<br><b>I</b> got <b>annoyed</b> after five minutes.<br><b>I</b> often feel <b>shocked</b> by the changes.<br><b>I</b> was <b>amazed</b> by the color.</div></div>
{sub("B", "Choose the best option to complete the rules.", "5 min")}
<ol style="line-height:1.75"><li>-ing adjectives describe {ch(["our feelings", "the thing that makes us feel"], "the thing that makes us feel")}. Their subjects are {ch(["people", "it, that, what or things"], "it, that, what or things")}.</li>
<li>-ed adjectives describe {ch(["our feelings", "the thing that makes us feel"], "our feelings")}. Their subjects are usually {ch(["people", "things"], "people")}.</li>
<li>With -ed adjectives, we use <b>be</b>, <b>feel</b> and <b>get</b>. {ch(["get", "feel"], "get")} shows a change in our feelings.</li>
<li>bore → boring: we {ch(["keep", "drop"], "drop")} the final <b>e</b> before -ing.</li></ol>
{sub("C", "-ed adjectives + preposition. Complete the table with about, by, in or of.", "3 min")}
<table style="margin:0;table-layout:fixed"><tr><td><b>+</b> {A("about", "min-width:14mm")}</td><td><b>+</b> {A("by", "min-width:14mm")}</td><td><b>+</b> {A("in", "min-width:14mm")}</td><td><b>+</b> {A("of", "min-width:14mm")}</td></tr>
<tr><td>annoyed · confused · excited · worried</td><td>amazed · shocked · surprised</td><td>interested</td><td>bored · frightened · scared</td></tr></table>
<div class="box sand"><h4>RULE</h4><b>-ed</b> = how a person feels: <i>I was bored.</i> · <b>-ing</b> = what causes the feeling: <i>The show was boring.</i> <i>I'm bored</i> = I feel bored; <i>I'm boring</i> = people feel bored with me! More on the next page: <b>Grammar reference</b>.</div>""",
    22, """<ol><li>B: ask: <i>Who was bored, Rita or the show?</i> Use concept questions with every pair.</li>
<li>C: also <i>bored with</i>; <i>scared</i> → <i>scary</i> (not <i>scaring</i>).</li></ol>""")

    grammar_ref.ed_ing_adjectives(b)

    # Page 5
    snd = {"amazed": "d", "annoyed": "d", "bored": "d", "worried": "d", "depressed": "t", "relaxed": "t", "shocked": "t", "disappointed": "id", "excited": "id", "interested": "id"}
    cols = {"d": [w for w in S253 if snd[w] == "d"], "t": [w for w in S253 if snd[w] == "t"], "id": [w for w in S253 if snd[w] == "id"]}
    def cell(k):
        return R(" · ".join(cols[k])) if T else '<div class="wline"></div><div class="wline"></div>'
    b.page(f"""{sub("D", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>I'm boring. Let's go out!</td><td><b>I'm bored. Let's go out!</b></td><td>feeling = -ed.</td></tr>
<tr><td>The movie was bored.</td><td><b>The movie was boring.</b></td><td>the cause = -ing.</td></tr>
<tr><td>I'm interesting in music.</td><td><b>I'm interested in music.</b></td><td>feeling = -ed + in.</td></tr>
<tr><td>I'm excited for the trip.</td><td><b>I'm excited about the trip.</b></td><td>excited about.</td></tr>
<tr><td>It was a scaring movie.</td><td><b>It was a scary movie.</b></td><td>special form: scary.</td></tr>
<tr><td>I was shock-ed. /ˈʃɑːkɪd/</td><td><b>I was shocked. /ʃɑːkt/</b></td><td>-ed is /t/ here.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "4 min")}
{audiocard(["25.2", "25.3"])}
{sub("A", "Listen and repeat. Stress the adjectives.", "2 min", "25.2")}
{twocol([f'<li value="{i+1}">{s}</li>' for i, s in enumerate(S252)], 5)}
{sub("B", "Listen to the adjectives in alphabetical order. Write each one in the correct column.", "2 min", "25.3")}
<p class="small" style="margin:0 0 .5mm">{" · ".join(S253)}</p>
<table style="margin:0;table-layout:fixed"><tr><th>/d/ bored</th><th>/t/ shocked</th><th>/ɪd/ excited</th></tr><tr><td>{cell("d")}</td><td>{cell("t")}</td><td>{cell("id")}</td></tr></table>""",
    22, """<ol><li>B: same rule as past simple endings (Unit 19): /ɪd/ only after <i>t</i> or <i>d</i> (excited, interested, disappointed).</li>
<li>Brazilians add a vowel at the end: <i>shocked-i</i>. Practice the final consonants slowly.</li></ol>""")

    # Page 6
    pr = [("I'm really", "in this artist. The colors in her paintings are", "interested", "amazing", "interest", "amaze"),
          ("I'm", "of snakes. The way they move is", "scared", "frightening", "scare", "frighten"),
          ("He's getting", "about finding a new job. Applying for jobs day after day is", "worried", "depressing", "worry", "depress"),
          ("She was", "by the price of her meal at the new restaurant. It wasn't cheap, and that was", "shocked", "surprising", "shock", "surprise"),
          ("Don't you feel", "with the same exercise class every week? Trying new activities is more", "bored", "exciting", "bore", "excite"),
          ("I'm really", "about this recipe. It's so", "confused", "confusing", "confuse", "confuse")]
    prl = "".join(f"<li>{a} {A(x, 'min-width:18mm')} ({v1}) {m} {A(y, 'min-width:18mm')} ({v2}).</li>" for a, m, x, y, v1, v2 in pr)
    wb = [("Commercials are so boring.", "I'm going to check my phone while they're on.", "f"),
          ("This is a terrible show.", "Change the channel, please.", "d"),
          ("We've seen this part already.", "Can you fast-forward five minutes?", "b"),
          ("It's time for my favorite show.", "Where's the remote control?", "h"),
          ("I think we missed something.", "We need to rewind a bit.", "g"),
          ("I can't understand what they're saying.", "Can we watch with the subtitles on?", "a"),
          ("I can't hear anything!", "Can you turn up the volume?", "c"),
          ("I haven't seen the last episode yet.", "Please, no spoilers!", "e")]
    left = "".join(f"<li>{a} {A(l, 'min-width:7mm;text-align:center')}</li>" for a, _, l in wb)
    right_sorted = sorted([(l, bb) for _, bb, l in wb])
    right = "".join(f"<li>{bb}</li>" for l, bb in right_sorted)
    b.page(f"""{sec(5, "Practice", "9 min")}
{sub("A", "Complete the sentences with the -ed or -ing adjective of the verbs.", "5 min")}
<ol style="line-height:1.7">{prl}</ol>
<p class="small" style="margin:.5mm 0">Sometimes more than one answer is possible.</p>
{sub("B", "Word builder: watching TV together. Match the sentences 1–8 with the replies a–h.", "4 min")}
<div style="display:flex;gap:4mm;font-size:9pt"><ol style="flex:1;line-height:1.55;margin:0">{left}</ol><ol type="a" style="flex:1;line-height:1.55;margin:0">{right}</ol></div>
<p class="small">What do the words <b>commercials, fast-forward, rewind, subtitles, volume, spoilers</b> mean? Which phrases do you use at home?</p>""",
    22, """<ol><li>A: alternatives: 2 frightened / scary · 3 depressed / depressing or worrying · 4 surprised / shocking · 6 annoyed / annoying. 6: the recipe doesn't say how long to bake the cake.</li>
<li>B: American English: <i>commercials</i> (British: <i>adverts</i>), <i>remote control</i> or just <i>the remote</i>.</li></ol>""")

    # Page 7
    model = ("My favorite show at the moment is Fix My House. It's a makeover show, and I watch it on Sunday nights. In every episode, the team has only one week to change a family's home. "
             "The results are always amazing, and sometimes a little shocking! I get really excited at the end, when the family sees their new house for the first time. "
             "I think people love it because it's relaxing, and you get great ideas for your own home.")
    fb = ["I included all the information", "I spoke for 45 seconds", "I spoke clearly, without stopping a lot", "I used -ed and -ing adjectives correctly"]
    fbl = "".join(f"<tr><td>{f}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for f in fb)
    b.page(f"""{sec(6, "Speaking: a mini-presentation", "12 min")}
<div style="display:flex;gap:3mm;align-items:center"><p style="flex:1;margin:0">You are going to speak for <b>45 seconds</b> about a TV show or series. Choose one topic: <b>my favorite show</b> · <b>the last show I watched</b> · <b>a show that everyone is talking about</b>.</p>{img('B', 32, 21)}</div>
{sub("A", "Listen to your teacher's presentation. What type of show is it? Why do people like it?", "2 min")}
<p class="small" style="margin:0">{R(model) if T else ''}</p>
{sub("B", "Plan. Write key words only, not sentences.", "3 min")}
<table style="margin:0"><tr><td style="width:62mm">what type of show it is, and when or where you watch it</td><td></td></tr>
<tr><td>what happens (use at least one <b>-ing</b> adjective)</td><td></td></tr>
<tr><td>how it makes you feel (use an <b>-ed</b> adjective + preposition)</td><td></td></tr>
<tr><td>why you or other people watch it</td><td></td></tr></table>
{sub("C", "Give your presentation. Your teacher listens and asks you one question. Then rate yourself.", "5 min")}
<table class="ck"><tr><th>My speaking</th><th style="width:18mm">0 not yet</th><th style="width:18mm">1 OK</th><th style="width:18mm">2 very good</th></tr>{fbl}</table>
{sub("D", "Talk about it: Do you prefer to watch shows alone or with other people? Do you watch with subtitles?", "2 min")}""",
    22, """<ol><li>A: read the red model at natural speed; ask the student to count the -ed and -ing adjectives (amazing, shocking, excited, relaxing).</li>
<li>C: time the student, give feedback, and let them repeat it once; the second time is usually much better.</li></ol>""")

    # Page 8
    pc = [("A2 Unit 22", "I can compare my life then and now with used to."), ("A2 Unit 23", "I can imagine a different situation with the second conditional."),
          ("A2 Unit 24", "I can plan and write a short story with direct speech."), ("A2 Unit 25", "I can talk about TV shows with -ed and -ing adjectives.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Listen! Did you hear that", ["scared", "scary"], "scary", "sound?", ""),
          ("I'm getting", ["bored", "boring"], "bored", "housework! Can you help me?", "with / of"),
          ("For me, soccer is the most", ["excited", "exciting"], "exciting", "sport to watch.", ""),
          ("My brother is", ["annoyed", "annoying"], "annoyed", "his team losing again.", "about"),
          ("She's", ["frightened", "frightening"], "frightened", "the dark.", "of"),
          ("The students are", ["interested", "interesting"], "interested", "American culture.", "in"),
          ("These instructions are really", ["confused", "confusing"], "confusing", ". I don't know what to do.", ""),
          ("Were you", ["surprised", "surprising"], "surprised", "my new haircut?", "by")]
    hwl = "".join(f"<li>{a} {ch(o, r)} {A(p or '—', 'min-width:12mm')} {e}</li>" for a, o, r, e, p in hw)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Choose the correct adjective. Add a preposition if you need to.</b></p>
<ol style="line-height:1.65">{hwl}</ol>
<p style="margin-top:2mm"><b>2. A TV review (50–75 words).</b> Write about the last show or movie you watched. What was it about? Was it exciting, boring, scary…? How did you feel? Would you recommend it?</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class: the student reads the review aloud; ask follow-up questions with <i>Were you surprised by…? Was it scary?</i></p>""")

    b.extra("Audio script", f"""
{sub("25.1", "Coffee break (slow and natural)")}
<p style="line-height:1.42">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in S251)}</p>
{sub("25.2", "Repeat: -ed and -ing")}
<p>{" · ".join(S252)}</p>
{sub("25.3", "Three -ed sounds")}
<p>{" · ".join(S253)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 25 - Last night's TV")
