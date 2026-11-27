# Speak! Progress B1 - Unit 62 "Bucket list" (all English) - lean B1 format
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
setup(band="B1 · UNIT 62", audio_json="audio_b1-unit-62.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-62"]
S621 = [l.split(": ", 1) for l in _r["62.1 Gap Year Diaries: our bucket lists"].split("\n")]
S622 = [x.split(": ", 1)[1] for x in _r["62.2 Repeat: dreams and plans"].split("\n")]




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
    cover = cover_html(T, "LEVEL B1 · UNIT 62", "Bucket list", "Dreams, plans and things to do one day · <b>I've always dreamed of… · I hope I get to…</b>",
                       [("YOU CAN", "talk about your dreams and plans, and react to other people's dreams"),
                        ("LANGUAGE", "bucket list · go for it · not my thing · dream of -ing · hope I get to · can't wait to · be dying to"),
                        ("PRONUNCIATION", "enthusiastic intonation: That would be amazing!")])
    items = ["drive across a country", "go up in a hot air balloon", "learn a new language", "run a marathon", "see the Northern Lights",
             "swim with dolphins", "volunteer for a good cause", "write a book"]
    rows = "".join(f"<tr><td>{x}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for x in items)
    b.page(f"""{sec(1, "Warm-up: one day…", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["Look at the photo. Would you like to do this? Why or why not?", "What is a bucket list? Have you ever made one?", "Why do you think people make bucket lists?"], "START TALKING")}</div></div>
{sub("A", "Popular bucket list items. Check one box for each. Then tell your teacher about two of them.", "4 min")}
<table class="ck" style="font-size:8.5pt;margin:.5mm 0"><tr><th>item</th><th style="width:24mm">I've done it!</th><th style="width:24mm">I'd love to</th><th style="width:24mm">Not for me</th></tr>{rows}</table>
{talk(["Which item would be the most exciting? The most difficult?", "What would you add to this list?", "Do you know anyone who has done one of these?"], "USE THE LIST")}""",
    30, """<ol><li>Top box: a bucket list is a list of things you want to do before you die. The expression comes from <i>kick the bucket</i>, an informal idiom for <i>die</i>.</li>
<li>A replaces the Linguahouse popular items pictures. Push <i>I've (never)…, I'd love to…, It's not for me</i>, and ask one follow-up question each time.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Gap Year Diaries: our bucket lists · who wants to do it? · positive or negative reactions · Talk about it",
                      "dreams and ambitions: would love to, hope to / I hope I get to, dream of -ing, can't wait to, be dying to, be determined to; hope vs wish", "Choose the correct words · rewrite · Use it (oral)",
                      "intonation (62.2) · reacting to dreams · the bucket list game · long turn: a dream that came true", "hope or wish · watch out · writing: my bucket list"),
        """The Linguahouse lesson has no listening or reading: statements about bucket lists matched with responses, pictures of popular items in another country, a grammar box on hope and wish + could, a bucket list game for groups and a homework list. We turned the statements and responses into a Gap Year Diaries episode: Danny, Bruno and Rafa share their bucket lists. Bruno has always dreamed of running a marathon abroad (maybe Chicago, with Danny as his guide) and would love to go up in a hot air balloon (Rafa is scared of heights). Rafa's dream is to record an album with the band, and he hopes he gets to play at a jazz festival. Danny is determined to go to the Amazon before he leaves Brazil (he's been saving for months) and is dying to sleep in a hammock in the rainforest; he wishes he could cook like Mrs. Lima, and he wants to learn to surf (not Bruno's thing). Wish + could was taught in Unit 38, so the new B1 grammar point is the language of dreams and ambitions, with hope vs wish as a review. The game is adapted for 1:1.""",
        """<i>I dream to travel</i> (→ <i>dream of traveling</i>); <i>I hope to can go</i> (→ <i>to be able to go / I hope I can go</i>); <i>I wish you have a great trip</i> (→ <i>I hope you have</i>); <i>I can't wait for see it</i> (→ <i>to see</i>).""",
        "Track 62.1 Gap Year Diaries: our bucket lists (natural and slow; Danny, Bruno and Rafa) · Track 62.2 Repeat: dreams and plans"))

    # Page 2 - Listening
    who = [("learn to surf", "Danny"), ("record an album", "Rafa"), ("run a marathon in another country", "Bruno"), ("sleep in a hammock in the Amazon", "Danny"),
           ("play at a jazz festival", "Rafa"), ("cook like Mrs. Lima", "Danny"), ("go up in a hot air balloon", "Bruno")]
    whol = "".join(f'<li>{d} {A(n, "min-width:16mm")}</li>' for d, n in who)
    reac = [("Cool. But I think that might be too dangerous for me.", "N · the Amazon"), ("Don't let that stop you!", "P · cooking"), ("Go for it!", "P · the jazz festival"),
            ("Hmm, that's not really my thing.", "N · surfing"), ("I wouldn't do that. I'm scared of heights.", "N · the balloon"), ("I'm sure you will!", "P · the marathon"),
            ("That would be amazing!", "P · the album")]
    rl = "".join(f'<li><i>{s}</i> {A(a, "min-width:26mm")}</li>' for s, a in reac)
    b.page(f"""{sec(2, "Listening: our bucket lists", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
<p style="margin:0 0 1mm;font-size:8.8pt">On this episode of Gap Year Diaries, Danny, Bruno and Rafa talk about their bucket lists: the things they want to do one day.</p>
{sub("A", "Listen. Who wants to do these things? Write Danny, Bruno or Rafa.", "3 min")}
<ol style="line-height:1.5;font-size:8.5pt;margin:0;columns:2;column-gap:4mm">{whol}</ol></div>{img('B', 36, 30)}</div>
{audiocard(["62.1 · NATURAL", "62.1 · SLOW"])}
{sub("B", "Reactions. Listen again. Is each reaction positive (P) or negative (N)? Which dream is it about?", "5 min")}
<ol style="line-height:1.55;font-size:8.5pt;margin:0">{rl}</ol>
<p style="margin:.6mm 0;font-size:8.6pt"><b>Think about it:</b> Danny says "I'm determined to go before I leave Brazil." What has he been doing? {A("saving money for months", "min-width:30mm")}</p>
{talk(["Whose bucket list is the most interesting? Why?", "Which of their dreams would you like to do? Which wouldn't you do?", "Do you think Danny will learn to surf? Why or why not?"])}""",
    35, """<ol><li>A: play the natural version; play the slow one if needed.</li>
<li>B comes from the Linguahouse statements and responses. Then ask the student to find how they talk about dreams: <i>I've always dreamed of running, I'd love to go up, One of my dreams is to record, I can't wait to hear, I hope I get to play, I'm determined to go, I'm dying to sleep, I wish I could cook</i>. They come back on page 3.</li></ol>""")

    # Page 3
    lean.grammar_in_class(b, grammar_ref.dreams_ambitions)

    # Page 4 - Practice
    pc = [("I've always dreamed", ["to run", "of running"], "of running", "a marathon."), ("I'd love", ["to go", "going"], "to go", "up in a balloon."),
          ("I hope I", ["will get", "get to"], "get to", "play at a festival."), ("I can't wait", ["to hear", "hearing"], "to hear", "your album!"),
          ("I'm looking forward", ["to see", "to seeing"], "to seeing", "the Amazon."), ("I'm determined", ["to go", "going"], "to go", "before I leave."),
          ("I", ["wish", "hope"], "hope", "you have a great trip!"), ("I wish I", ["could", "can"], "could", "cook like Mrs. Lima.")]
    cl = "".join(f"<li>{a} {ch(o, r)} {z}</li>" for a, o, r, z in pc)
    rw = [("You want a cat, but you're allergic to them. (wish)", "I wish I could have a cat."),
          ("You really want to see the Northern Lights, and you're saving for the trip. (hope I get to)", "I hope I get to see the Northern Lights."),
          ("You want to drive, but you haven't passed your test yet. (wish)", "I wish I could drive.")]
    rwl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw)
    use = ["What have you always dreamed of doing?", "What are you dying to do this year?", "What can't you wait to do on your next vacation?",
           "Is there something you wish you could do, but can't? Why not?", "What do you hope you get to do in the next ten years?"]
    b.page(f"""{sec(4, "Practice: I'd love to…, I hope I get to…", "10 min")}
{sub("A", "Choose the correct words.", "3 min")}
<ol style="line-height:1.7;font-size:8.6pt;margin:0;columns:2;column-gap:6mm">{cl}</ol>
{sub("B", "Hope or wish? Write a sentence with the words in brackets.", "4 min")}
<ol style="line-height:1.45;font-size:8.7pt;margin:0">{rwl}</ol>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    30, """<ol><li>A: 3 minutes. Items 1 and 5: <i>of</i> and <i>to</i> are prepositions here, so the verb takes <i>-ing</i>.</li>
<li>B comes from the Linguahouse wish + could exercise: ask <i>Is it possible?</i> before the student chooses <i>hope</i> or <i>wish</i>.</li>
<li>Use it: 3 minutes, all oral. React to each answer with the phrases from page 2.</li></ol>""")

    # Page 5 - Speaking
    card = f"""<div class="box" style="margin-top:1mm;font-size:8.2pt">{R("<b>Teacher's card:</b> write your own six items secretly at the same time. Then take turns reading one item. If the other person has the same (or a very similar) item, nobody gets a point; if not, the reader gets one point. React to every item with the functional language, and ask one question: <i>Why? When? Who with?</i>")}</div>""" if T else ""
    b.page(f"""{sec(5, "Speaking: the bucket list game", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE: SHARING DREAMS AND REACTING</h4>
<table style="margin:0;font-size:8.2pt"><tr><th>sharing a dream</th><th>positive</th><th>negative</th><th>encouraging</th></tr>
<tr><td><i>I've always dreamed of… · One of my dreams is to… · I'm dying to…</i></td><td><i>That would be amazing! · Sounds incredible! · Me too!</i></td><td><i>That's not really my thing. · I wouldn't do that. · That might be too… for me.</i></td><td><i>Go for it! · Don't let that stop you! · I'm sure you will!</i></td></tr></table></div>
{audiocard(["62.2"])}
{sub("A", "Listen and repeat. Sound excited: the voice goes up on the important word.", "2 min", "62.2")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S622))}</p>
{sub("B", "The bucket list game. You have 3 minutes to write six things on your bucket list. Don't show your teacher! Then listen to the rules.", "8 min")}
<ol style="line-height:1.4;font-size:8.6pt;margin:0;columns:2;column-gap:6mm">{"".join(f"<li>{lines(1)}</li>" for _ in range(6))}</ol>{card}
{sub("C", "Discuss. Is it a good idea to have a bucket list? Which dreams are popular in Brazil? Have your dreams changed since you were younger?", "3 min")}
{sub("D", "Long turn. Tell your teacher about a dream that came true for you (or for someone you know). What was it? How did it feel?", "3 min")}""",
    30, """<ol><li>B comes from the Linguahouse bucket list game, adapted for 1:1. Explain the rules only after the student has written the list, so they write their real dreams.</li>
<li>Last 3 minutes: wrap-up (two corrections, and ask <i>Can you now talk about your dreams and react to other people's?</i>).</li></ol>""")

    # Homework
    hw = [("You want to visit your cousin in Lisbon, but the tickets are too expensive.", "I wish I could visit my cousin in Lisbon."),
          ("You're going to Rio next month, and you really want to see a samba school rehearsal.", "I hope I get to see a samba school rehearsal."),
          ("Your friend invites you to a party, but you have to work.", "I wish I could go to the party."),
          ("Your friend is flying to Japan tomorrow.", "I hope you have a great trip!")]
    hwl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in hw)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Hope or wish? Write a sentence for each situation.", "")}</div>{img('C', 30, 19)}</div>
<ol style="line-height:1.45;font-size:8.7pt;margin:0">{hwl}</ol>
{lean.watch_out([("I dream to travel around the world.", "I dream of traveling around the world.", "<i>dream of</i> + -ing."), ("I hope to can go next year.", "I hope to be able to go / I hope I can go next year.", "no <i>to can</i>: use <i>to be able to</i>."), ("I wish you have a great trip!", "I hope you have a great trip!", "good wishes about the future: <i>hope</i>.")])}
{lean.writing_task(sub, "Write your bucket list for Danny's blog: six things you want to do one day, and why you want to do each one.", "One of my biggest dreams is to…", ["six items", "a reason for each one", "at least four different phrases (dream of, I'd love to, I hope I get to, I'm dying to…)", "100–150 words"], "I can talk about my dreams and plans, and react to other people's dreams.")}""",
    25, """<p>Check A in 3 minutes at the start of the next class. It comes from the Linguahouse wish + could situations, with hope added. The writing is the Linguahouse homework (a list with reasons). Read it at home and choose two mistakes to discuss in class.</p>""")

    def scr(lst):
        return "".join(f"<p style='margin:.4mm 0'><b>{n}:</b> {t}</p>" for n, t in lst)
    b.extra("Audio script", f"""
{sub("62.1", "Gap Year Diaries: our bucket lists (natural and slow; Danny, Bruno and Rafa)")}
<div style="line-height:1.28;font-size:8.2pt">{scr(S621)}</div>
{sub("62.2", "Repeat: dreams and plans")}
<p>{" · ".join(S622)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 62 - Bucket list")
