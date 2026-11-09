# Speak! Bridge A2 - Unit 46 "Food for thought" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 46", audio_json="audio_a2-unit-46.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["a2-unit-46"]
S461 = [x.split(": ", 1)[1] for x in _r["46.1 Food for thought"].split("\n")]
S462 = [x.split(": ", 1)[1] for x in _r["46.2 Repeat: phrasal verbs"].split("\n")]
S463 = [x.split(". ", 1)[1] for x in [y.split(": ", 1)[1] for y in _r["46.3 Which particle?"].split("\n")]]

ART = [
    "Reality TV has never been more popular. We've seen people on dates, at the doctor's office, and moving to a new house. But for me, the best topic for reality TV is food. And when food and cooking are combined with a <b>competition</b> for prizes, it's a <b>winning formula</b>. In one popular type of show, different people take turns cooking dinner for each other. Each meal gets a score, and the <b>host</b> with the highest score wins some money at the end of the week.",
    "So why do we enjoy these shows so much? First of all, we all think we can do better. When we watch a host <u>cutting up</u> vegetables or <u>mixing in</u> the egg whites, we like to think, \"That's not the right way to do it!\"",
    "We also enjoy watching the guests eating… or not eating. Some of the food is amazing, and the guests <u>pig out</u> happily. Others <u>pick at</u> their salad and say, \"I don't really like vegetables.\" Sometimes guests are <b>on special diets</b>: \"I <u>gave up</u> meat ten years ago,\" or \"I'm trying to <u>cut down on</u> sugar.\" This is a big <b>challenge</b> for the hosts, who may have to make two different dishes.",
    "Some of the more \"creative\" hosts don't even <b>bother</b> to cook! They just <u>pick up</u> takeout and <u>heat</u> it <u>up</u> for their guests. They don't usually win the prize money, though.",
    "And what about the arguments? The TV producers like to <u>turn up</u> the heat by putting together people with very different ideas about life. We love watching the \"discussions\" that follow.",
    "Will we ever get tired of these shows? I don't think so, because there are so many <b>variations</b> of food, people and homes. In my opinion, a good dinner party show is even better than <u>eating out</u> at a fancy restaurant!"]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 46", "Food for thought", "Food and TV · <b>phrasal verbs</b>",
                       [("YOU CAN", "read an informal article and use food phrasal verbs with the correct grammar"),
                        ("LANGUAGE", "eat out · pick up · pig out · pick at · cut down on · give up · heat it up · cut them up"),
                        ("PRONUNCIATION", "linking in phrasal verbs: pick‿it‿up · which particle?")])
    groups = [("We always <b>eat out</b> on special occasions. But if we're too tired to cook, we <b>pick up</b> some takeout.", [("have a meal in a restaurant", "eat out"), ("quickly go to get something", "pick up")]),
              ("As a child, I used to <b>pick at</b> my food. Now I love to <b>pig out</b>!", [("eat a lot", "pig out"), ("eat very little, without enjoying it", "pick at")]),
              ("My dad is trying to <b>cut down on</b> sugar. He's also going to <b>give up</b> coffee.", [("stop doing something completely", "give up"), ("use less of something", "cut down on")]),
              ("Let's <b>heat up</b> some soup. It's taking ages: <b>turn up</b> the heat!", [("make something hot", "heat up"), ("make something stronger", "turn up")]),
              ("I <b>cut up</b> the strawberries. Can you <b>mix</b> them <b>in</b> with the other fruit?", [("make small pieces with a knife", "cut up"), ("add something and stir it", "mix in")])]
    gh = "".join(f"<li style='margin-bottom:.8mm'>{t}<br><span class='small'>{' · '.join(d + ' ' + A(a, 'min-width:16mm') for d, a in ds)}</span></li>" for t, ds in groups)
    b.page(f"""{sec(1, "Warm-up: food phrasal verbs", "8 min")}
<div style="display:flex;gap:2mm;margin-bottom:1mm">{"".join(img(l, 34, 20) for l in "ABCD")}</div>
{sub("A", "Read the sentences. Write the phrases in bold next to the meanings.", "6 min")}
<ol style="line-height:1.45;font-size:8.8pt;margin:0">{gh}</ol>
{sub("B", "What do you notice about the phrases in bold?", "2 min")}
<p class="small" style="margin:0">{A("They're all verb + a small word (up, out, at, in, down on): phrasal verbs.", "min-width:80mm")}</p>""",
    22, """<ol><li>A: lots of linking: <i>eat‿out, pick‿up, pig‿out, cut‿up</i>. <i>Takeout</i> (British: <i>takeaway</i>). <i>Pig out</i> is informal.</li>
<li>B: these are phrasal verbs; ask if the student knows others (wake up, get up, turn off).</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Ten food phrasal verbs</td><td>1</td></tr>
<tr><td>2 Reading</td><td>10 min</td><td>Kate's blog post about dinner party TV shows (audio 46.1)</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Phrasal verbs: form, meaning, grammar</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Phrasal verbs</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>4 min</td><td>Linking · which particle?</td><td>5</td></tr>
<tr><td>5 Practice</td><td>9 min</td><td>Correct the mistakes · gifts for a host</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Dinner party role-play with a word card</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Kate (Neural2-G), Tom's sister and the owner of Sweet Kate Bakery, writes a post for the bakery's blog about why people love dinner party reality shows, and reads it aloud (46.1). The blog is invented, and the show is described in general terms (no real show is named). This is a reading lesson, as in Linguahouse.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students put pronouns after the particle (<i>heat up it, cut up them</i>), confuse particles (<i>eat up</i> for <i>eat out</i>), forget the third part (<i>cut down sugar</i>), and avoid phrasal verbs completely, which sounds very formal.</div>
<div class="box"><h4>AUDIO</h4>Track 46.1 Food for thought (slow and natural) · Track 46.2 Repeat: phrasal verbs · Track 46.3 Which particle?</div>""")

    # Page 2
    qs = [("Why do we enjoy watching people cook?", "Because we think we can do better."), ("Do the guests always enjoy the food?", "No: some pick at their food or don't like it."),
          ("What happens if hosts don't cook the food themselves?", "They don't usually win the prize."), ("How do the producers make the shows interesting?", "They put together people with very different ideas."),
          ("How does Kate feel about these shows?", "She loves them: better than eating out.")]
    ql = "".join(f"<li>{q} {A(a, 'min-width:28mm')}</li>" for q, a in qs)
    art = "".join(f"<p style='margin:0 0 1.1mm'><b>{i+1}</b> {t}</p>" for i, t in enumerate(ART))
    b.page(f"""{sec(2, "Reading: food for thought", "10 min")}
<div style="display:flex;gap:2.5mm;align-items:center"><p style="flex:1;margin:0">Kate, Tom's sister, writes a blog for her bakery. This week, she writes about TV shows where people cook dinner for each other.</p>{img('E', 30, 18)}</div>
{sub("A", "Read the post and answer the questions.", "5 min", "46.1 · SLOW")}
<ol style="margin:0;line-height:1.4;font-size:8.8pt">{ql}</ol>
<div class="box" style="font-size:8.4pt;line-height:1.42;column-count:2;column-gap:5mm"><b style="color:#176074;font-size:10pt">Food for thought</b><br><i>Why we love watching dinner party shows</i><br>{art}</div>
{audiocard(["46.1 · SLOW", "46.1 · NATURAL"])}
{sub("B", "Find the words in bold that mean:", "4 min")}
<p class="small" style="margin:0;line-height:1.6">a situation where people try to be the best {A("competition", "min-width:16mm")} · things that work very well together {A("a winning formula", "min-width:20mm")} · a difficult situation {A("challenge", "min-width:14mm")} · a person who invites guests {A("host", "min-width:10mm")} · eating plans for health reasons {A("special diets", "min-width:16mm")} · take the time to do something {A("bother", "min-width:10mm")} · different versions {A("variations", "min-width:14mm")}</p>
{sub("C", "Kate uses quotation marks (\" \") for what people say and for jokes. Find two jokes.", "1 min")}
<p class="small" style="margin:0">{A("\"creative\" hosts (they don't cook!) · \"discussions\" (really arguments)", "min-width:70mm")}</p>""",
    22, """<ol><li>A: the underlined phrasal verbs come from the Warm-up; the bold words are new vocabulary. Play the audio as a second read-and-listen.</li>
<li>C: American English uses double quotation marks (British English often uses single ones).</li></ol>""")

    # Page 3
    col = [("cut up", "vegetables"), ("mix in", "the egg whites"), ("pig out", "happily"), ("pick at", "their salad"), ("give up", "meat"), ("cut down on", "sugar"), ("pick up", "takeout"), ("turn up", "the heat"), ("eat out", "at a fancy restaurant")]
    cs = sorted(c for _, c in col)
    cl = "".join(f"<li>{v} {A('abcdefghi'[cs.index(c)], 'min-width:6mm;text-align:center')}</li>" for v, c in col)
    csl = "".join(f"<li>{c}</li>" for c in cs)
    types = [("1 no object", "eat out · pig out"), ("2 object, can't separate", "pick at something"), ("3 object, can separate", "cut something up · give something up · heat something up · pick something up · turn something up"), ("4 three parts", "cut down on something")]
    tt = "".join(f"<tr><td style='width:40mm'><b>{a}</b></td><td>{b_}</td></tr>" for a, b_ in types)
    b.page(f"""{sec(3, "Language focus: phrasal verbs", "10 min")}
<div class="box" style="margin-top:0;font-size:9pt">A phrasal verb = verb + particle (<i>up, out, at, in, down, on</i>). Learn the <b>form</b>, the <b>meaning</b> and the <b>grammar</b>.</div>
{sub("A", "Collocations. Match the phrasal verbs with the words they go with in the post.", "3 min")}
<div style="display:flex;gap:4mm;font-size:8.8pt"><ol style="flex:1;line-height:1.45;margin:0;column-count:2">{cl}</ol><ol type="a" style="flex:1;line-height:1.45;margin:0;column-count:2">{csl}</ol></div>
{sub("B", "Grammar. Look at the four types. What's the difference between type 2 and type 3?", "4 min")}
<table style="margin:0;font-size:8.6pt">{tt}</table>
<p style="margin:.5mm 0">{A("Type 2: the object always comes after the particle. Type 3: the object can go between the verb and the particle.", "min-width:100mm")}</p>
{sub("C", "Type 3 and pronouns. Which sentences are correct?", "3 min")}
<p style="margin:.5mm 0;line-height:1.7">I cut up the vegetables. {A("✓", "min-width:6mm")} · I cut the vegetables up. {A("✓", "min-width:6mm")} · I cut them up. {A("✓", "min-width:6mm")} · I cut up them. {A("✗", "min-width:6mm")}</p>
<div class="box sand"><h4>RULE</h4>With a <b>noun</b>, type 3 can go either way: <i>cut up the onions / cut the onions up</i>. With a <b>pronoun</b> (<i>it, them</i>), you must separate: <i>cut them up</i>. Not sure of the type? Put the noun after the particle. More on the next page: <b>Grammar reference</b>.</div>""",
    20, """<ol><li>B: a learner's dictionary shows the type: <i>pick at sth</i> (no separation) vs <i>cut sth up</i> (separable).</li>
<li>C: the noun-after-particle order is always safe; with pronouns the student must separate.</li></ol>""")

    grammar_ref.phrasal_verbs(b)

    # Page 5
    pp = ["up", "in", "at", "out", "up", "down on"]
    ppl = "".join(f"<li>{A(x, 'min-width:14mm;text-align:center')}</li>" for x in pp)
    b.page(f"""{sub("D", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>Heat up it in the microwave.</td><td><b>Heat it up in the microwave.</b></td><td>pronoun in the middle.</td></tr>
<tr><td>Cut up them.</td><td><b>Cut them up.</b></td><td>pronoun in the middle.</td></tr>
<tr><td>Let's eat up tonight.</td><td><b>Let's eat out tonight.</b></td><td>eat out = restaurant.</td></tr>
<tr><td>I'm cutting down sugar.</td><td><b>I'm cutting down on sugar.</b></td><td>three parts.</td></tr>
<tr><td>Stop picking your food at.</td><td><b>Stop picking at your food.</b></td><td>type 2: can't separate.</td></tr>
<tr><td>Please diminish the sugar. (spoken)</td><td><b>Cut down on the sugar.</b></td><td>phrasal verbs sound natural.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "4 min")}
{audiocard(["46.2", "46.3"])}
{sub("A", "Listen and repeat. Link the words: pick‿it‿up, heat‿it‿up.", "2 min", "46.2")}
{twocol([f'<li value="{i+1}">{s}</li>' for i, s in enumerate(S462)], 4)}
{sub("B", "Listen to six sentences. Which particle do you hear? Write it.", "2 min", "46.3")}
<ol style="line-height:1.5;column-count:3;column-gap:5mm">{ppl}</ol>""",
    30, """<ol><li>A: consonant + vowel links: <i>pick‿it‿up</i> sounds like "pi-ki-tup". The particle is usually stressed: <i>eat OUT, pick UP</i>.</li>
<li>B: script: 1 Can you pick it up on your way home? 2 Mix the fruit in now. 3 Please stop picking at your food. 4 We're eating out on Friday. 5 She gave it up last year. 6 I'm trying to cut down on snacks.</li></ol>""")

    # Page 6
    pm = [("Are you going to eat that cold, or are you going to heat up it?", "heat it up"), ("Do you have any bananas? Mix in them with the other fruit.", "Mix them in"),
          ("I'm just going to pick up a pizza for dinner.", "✓"), ("I'm really cold. Could we turn the up heat?", "turn up the heat / turn the heat up"),
          ("Sorry, I can't eat this dessert. I gave up chocolate.", "✓"), ("I'm too tired to cook. Do you want to eat up tonight?", "eat out"),
          ("If you don't like it, leave it. Don't pick it at.", "pick at it"), ("Maybe you should cut on down sweets.", "cut down on"),
          ("We always pig out at my grandmother's house.", "✓"), ("Please cut this tomato out for the salad.", "cut this tomato up")]
    pml = "".join(f"<li>{s} {A(c, 'min-width:24mm')}</li>" for s, c in pm)
    gf = [("F", "potted", "plant"), ("G", "scented", "candle"), ("H", "box of", "chocolates"), ("I", "bouquet of", "flowers")]
    gfh = "".join(f'<div style="text-align:center;font-size:8.6pt">{img(l, 26, 18)}{A(w, "min-width:16mm")} {n}</div>' for l, w, n in gf)
    b.page(f"""{sec(5, "Practice", "9 min")}
{sub("A", "Correct the mistakes. If a sentence is correct, write ✓.", "5 min")}
<ol style="line-height:1.5;font-size:9pt;margin:0">{pml}</ol>
{sub("B", "Word builder: gifts for a host. In the US, guests often bring a small gift to a dinner party. Complete with: bouquet of · box of · potted · scented.", "4 min")}
<div style="display:flex;gap:3mm;justify-content:space-between">{gfh}</div>
<p class="small" style="margin:.8mm 0">Which gift is the best? What do people bring to a dinner in Brazil?</p>""",
    26, """<ol><li>A: ask for the rule each time: pronoun position, type 2 or 3, the right particle.</li>
<li>B: from the Linguahouse extension. Other common host gifts: a bottle of wine, flavored olive oil, cookies, a coffee table book (a big picture book).</li></ol>""")

    # Page 7
    words = ["eat out", "pick up", "pig out", "pick at", "cut down on", "give up", "heat up", "turn up", "cut up", "mix in", "host", "challenge", "special diet", "competition", "bother", "variation"]
    b.page(f"""{sec(6, "Speaking: a dinner party", "12 min")}
<div style="display:flex;gap:3mm;align-items:center"><p style="flex:1;margin:0">Role-play a dinner party with your teacher. The meal has soup, a main course and dessert. First, write these 16 words in your card in any order.</p>{img('E', 30, 20)}</div>
<div class="bank">{" · ".join(words)}</div>
<table style="table-layout:fixed;width:100%;margin:1mm 0">{"".join("<tr>" + "".join("<td style='height:10mm;border:.8pt solid #c9dfe3'></td>" for _ in range(4)) + "</tr>" for _ in range(4))}</table>
{sub("A", "Your teacher is the host. You are a guest. Use the words on your card and cross them out. Can you make a line of four?", "5 min")}
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:9pt"><b>Teacher (host):</b> I hope everyone likes soup! I heated it up just before you arrived. <b>You:</b> It smells great! I'm trying to cut down on salt, but it looks delicious…</div>
{sub("B", "Change roles: you are the host.", "4 min")}
{sub("C", "How many words did you use? Any lines? Which sentences do you want to check with your teacher?", "3 min")}""",
    26, """<ol><li>This is a 1:1 version of the Linguahouse group dinner party. As the host, invent problems: the soup is cold (heat it up), a guest is on a special diet, the dessert is store-bought (picked it up).</li>
<li>C: write two or three "perfect" sentences together at the end.</li></ol>""")

    # Page 8
    pc = [("A2 Unit 43", "I can explain the rules of a game."), ("A2 Unit 44", "I can explain how to solve a problem and why a solution works."),
          ("A2 Unit 45", "I can describe a process with the present simple passive."), ("A2 Unit 46", "I can use food phrasal verbs with the correct word order.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    wo = [("you / on your way home? / up / pick / it / Can", "Can you pick it up on your way home?"), ("the fruit / I / in / mix / need to / now.", "I need to mix in the fruit / mix the fruit in now."),
          ("heat / I'll / it / the microwave / to / up. / use", "I'll use the microwave to heat it up."), ("down / I'm / on / snacks. / trying to / cut", "I'm trying to cut down on snacks."),
          ("at / food. / picking / Please / stop / your", "Please stop picking at your food."), ("given / for health reasons. / She's / them / up", "She's given them up for health reasons."),
          ("eating / this weekend. / out / We're", "We're eating out this weekend."), ("can / by / cutting / help / them / up. / You", "You can help by cutting them up.")]
    wol = "".join(f"<li>{w}<br>{A(s, 'min-width:80mm')}</li>" for w, s in wo)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p style="margin:.5mm 0"><b>1. Put the words in order. If two orders are possible, write both.</b></p>
<ol style="line-height:1.38;font-size:8.8pt;margin:0">{wol}</ol>
<p style="margin-top:1.5mm"><b>2. A memorable meal (50–75 words).</b> Write about a meal you had at home or when you ate out. Use at least four phrasal verbs from this unit.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class: the student reads the text aloud; ask follow-up questions with phrasal verbs: <i>Did you pig out? Who picked it up?</i> Unit 47 is about asking questions; Unit 49 is Review 5.</p>""")

    b.extra("Audio script", f"""
{sub("46.1", "Food for thought (slow and natural)")}
<p style="line-height:1.4">{"<br>".join(S461)}</p>
{sub("46.2", "Repeat: phrasal verbs")}
<p>{" · ".join(S462)}</p>
{sub("46.3", "Which particle? (3-second pause)")}
<p>{" · ".join(S463)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 46 - Food for thought")
