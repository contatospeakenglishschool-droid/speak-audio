# Speak! Bridge A2 - Unit 43 "Word games" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 43", audio_json="audio_a2-unit-43.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["a2-unit-43"]
S431 = [x.split(": ", 1) for x in _r["43.1 A game of GHOST"].split("\n")]
S432 = [x.split(": ", 1)[1] for x in _r["43.2 Repeat: rules"].split("\n")]
S433 = [x.split(". ", 1)[1] for x in [y.split(": ", 1)[1] for y in _r["43.3 Necessary or not necessary?"].split("\n")]]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 43", "Word games", "Explaining games · <b>rules: have to, can't, don't have to, allowed to, supposed to</b>",
                       [("YOU CAN", "explain the rules of a game and talk about what is necessary, not allowed or your choice"),
                        ("LANGUAGE", "We have to take turns. · You can't say that. · You don't have to wait. · You're not allowed to give a clue."),
                        ("PRONUNCIATION", "have to /hæftə/, supposed to · necessary or not?")])
    wm = [("I'll just explain", "the rules of the game to you."), ("The aim of the game is to", "make the longest word."), ("You need a good strategy", "to win this game."),
          ("I almost always beat", "my brother at this game."), ("Wake up!", "It's your turn!"), ("The score is 3–3, so", "it's a tie."),
          ("I hope you're not going to get angry", "if you lose the game."), ("I can't believe I won the game.", "I've never played before!")]
    we = sorted(e for _, e in wm)
    lt = "abcdefgh"
    wml = "".join(f"<li>{s} {A(lt[we.index(e)], 'min-width:6mm;text-align:center')}</li>" for s, e in wm)
    wel = "".join(f"<li>{e}</li>" for e in we)
    b.page(f"""{sec(1, "Warm-up: playing games", "8 min")}
<div style="display:flex;gap:2mm;margin-bottom:1mm">{"".join(img(l, 34, 22) for l in "ABCE")}</div>
{sub("A", "Match the halves to make sentences about playing games.", "5 min")}
<div style="display:flex;gap:4mm;font-size:9pt"><ol style="flex:1;line-height:1.55;margin:0">{wml}</ol><ol type="a" style="flex:1;line-height:1.55;margin:0">{wel}</ol></div>
{sub("B", "Do you like card games, board games, sports or word games? Which games are popular in Brazil?", "3 min")}""",
    22, """<ol><li>A: <i>win</i> a game, but <i>beat</i> a person: <i>I beat my brother. I won the game.</i> A <i>tie</i> = the same score (British: <i>a draw</i>). <i>Your turn</i> = your time to play.</li>
<li>B: possible Brazilian games: truco, dominoes, Stop (a categories game), board games and soccer, of course.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Game vocabulary: rules, turn, beat, win, tie</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Tom teaches Kate a word game called GHOST</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Rules: necessary, not allowed, your choice, advice</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>have to, must, can't, don't have to, can, should, allowed to, supposed to</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>4 min</td><td>Rules in fast speech · necessary or not?</td><td>5</td></tr>
<tr><td>5 Practice</td><td>9 min</td><td>The rules of Categories</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Teach and play a word game</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Tom (Neural2-D), the English teacher, and his sister Kate (Neural2-G) are waiting for a train in Chicago, so Tom teaches her GHOST, a classic spelling game. Kate wins the first round with C-A-T-C-H. No new facts.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students think <i>don't have to</i> means "not allowed" (it means "not necessary"), put <i>to</i> after <i>must</i> and <i>can</i>, say <i>She have to</i>, and drop the -ed in <i>allowed</i> and <i>supposed</i>.</div>
<div class="box"><h4>AUDIO</h4>Track 43.1 A game of GHOST (slow and natural) · Track 43.2 Repeat: rules · Track 43.3 Necessary or not necessary?</div>""")

    # Page 2
    tf = [("GHOST is a spelling game.", "T"), ("The aim is to make the longest word you can.", "F: to make the other player finish the word."),
          ("Tom explains one rule in the middle of the game.", "T: three-letter words don't count."), ("They make a four-letter word.", "F: catch has five letters."),
          ("Kate wins the whole game.", "F: she only wins the first round.")]
    tfl = "".join(f"<li>{s} <b>T / F</b> {A(a, 'min-width:12mm')}</li>" for s, a in tf)
    op = [("We", ["have to", "can"], "have to", "take turns saying a letter."), ("In your turn, you", ["don't have to", "shouldn't"], "shouldn't", "say a letter that can end a word."),
          ("C K? You can't", ["to say", "say"], "say", "that."), ("It", ["must", "can"], "must", "be a real word."),
          ("But you're not supposed", ["to tell", "telling"], "to tell", "me the word."), ("So it's C A.", ["Should", "Can"], "Can", "I say that?"),
          ("You", ["should", "would"], "should", "explain that rule at the beginning!"), ("You can't", ["said", "say"], "say", "it if you don't know the word."),
          ("", ["You're", "You've"], "You're", "not allowed to give me a clue."), ("You", ["can't", "don't have to"], "don't have to", "be so annoying!")]
    opl = [f'<li value="{i+1}">{(a + " ") if a else ""}{ch(o, r)} {e}</li>' for i, (a, o, r, e) in enumerate(op)]
    b.page(f"""{sec(2, "Listening: a game of GHOST", "10 min")}
<div style="display:flex;gap:2.5mm;align-items:center"><p style="flex:1;margin:0">Tom and his sister Kate are waiting for a train in Chicago. Tom teaches Kate a word game.</p>{img('D', 30, 20)}</div>
{audiocard(["43.1 · SLOW", "43.1 · NATURAL"])}
{sub("A", "Listen. True (T) or false (F)?", "3 min", "43.1 · SLOW")}
<ol style="font-size:9pt;line-height:1.45;margin:0">{tfl}</ol>
<p class="small" style="margin:.5mm 0">Why is it important to say the aim of the game at the beginning? {A("It makes the rules much easier to understand.", "min-width:50mm")}</p>
{sub("B", "Listen again and choose the correct option.", "6 min", "43.1 · NATURAL")}
<div style="font-size:8.8pt">{twocol(opl, 6)}</div>
{sub("C", "Would you like to play GHOST? Why or why not?", "1 min")}""",
    22, """<ol><li>A: <i>a clue</i> = a piece of information that helps you find the answer. <i>A round</i> = one part of a game.</li>
<li>B: let the student predict first; most options are the grammar of the next page.</li></ol>""")

    # Page 3
    b.page(f"""{sec(3, "Language focus: talking about rules", "10 min")}
{sub("A", "Necessary or not allowed? Read and choose.", "3 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">1 We <b>have to</b> take turns. · 2 It <b>must</b> be a real word. · 3 You <b>can't</b> say that.</div>
<p style="margin:.5mm 0;line-height:1.7">In 1 and 2, it {ch(["is", "isn't"], "is")} necessary to do something. In 3, it's necessary {ch(["to do", "not to do"], "not to do")} something. Which form has <i>to</i> after it? {A("have to", "min-width:16mm")}</p>
{sub("B", "Your choice. Read and choose.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">1 So it's C A. <b>Can</b> I say that? · 2 You <b>don't have to</b> be so annoying!</div>
<p style="margin:.5mm 0">Here it {ch(["is", "isn't"], "is")} possible to choose what to do. <i>Don't have to</i> means {ch(["not allowed", "not necessary"], "not necessary")}.</p>
{sub("C", "Advice. Read and choose.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">1 You <b>shouldn't</b> say any letter that can end a word. · 2 You <b>should</b> explain that rule at the beginning.</div>
<p style="margin:.5mm 0">These are {ch(["rules", "advice"], "advice")}: it's {ch(["possible", "not possible"], "possible")} to choose.</p>
{sub("D", "Allowed and supposed. Read and answer.", "3 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">1 You're <b>not supposed to</b> tell me the word. You're <b>supposed to</b> keep it a secret. · 2 You're <b>not allowed to</b> give me a clue. You're only <b>allowed to</b> say the letter.</div>
<p style="margin:.5mm 0;line-height:1.7">Is there a choice? {A("No: these are rules.", "min-width:30mm")} Grammar: {A("be + supposed / allowed + to + base form", "min-width:56mm")} Stress: {A("supPOSED, alLOWED (second syllable)", "min-width:50mm")}</p>
<div class="box sand"><h4>RULE</h4><b>necessary:</b> have to, must · <b>not allowed:</b> can't, not allowed to, not supposed to · <b>not necessary:</b> don't have to · <b>allowed:</b> can, allowed to · <b>advice:</b> should. No <i>to</i> after <i>must, can, can't, should</i>. More on the next page: <b>Grammar reference</b>.</div>""",
    25, """<ol><li><i>must</i> is always about obligation; <i>can / can't</i> and <i>have to / don't have to</i> cover both rules and choice. Insist on the difference between <i>can't</i> and <i>don't have to</i>.</li>
<li>Drill all the examples, then let the student read the script aloud with you.</li></ol>""")

    grammar_ref.rules_modals(b)

    # Page 5
    nn = ["necessary", "not necessary", "necessary", "not necessary", "necessary", "not necessary"]
    nnl = "".join(f"<li>{A(x, 'min-width:22mm')}</li>" for x in nn)
    b.page(f"""{sub("E", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>You don't have to use your phone. (it's a rule)</td><td><b>You can't use your phone.</b></td><td>not allowed = can't.</td></tr>
<tr><td>You must to say a letter.</td><td><b>You must say a letter.</b></td><td>no to after must.</td></tr>
<tr><td>She have to choose a word.</td><td><b>She has to choose a word.</b></td><td>he / she / it: has to.</td></tr>
<tr><td>You're not allow to look.</td><td><b>You're not allowed to look.</b></td><td>allowed with -ed.</td></tr>
<tr><td>You're suppose to listen.</td><td><b>You're supposed to listen.</b></td><td>supposed with -ed.</td></tr>
<tr><td>I won my brother.</td><td><b>I beat my brother.</b></td><td>win a game, beat a person.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "4 min")}
{audiocard(["43.2", "43.3"])}
{sub("A", "Listen and repeat. have to = /hæftə/, has to = /hæstə/, supposed to = /səˈpoʊstə/.", "2 min", "43.2")}
{twocol([f'<li value="{i+1}">{s}</li>' for i, s in enumerate(S432)], 4)}
{sub("B", "Listen to six rules. Is it necessary or not necessary? Write it.", "2 min", "43.3")}
<ol style="line-height:1.5;column-count:3;column-gap:5mm">{nnl}</ol>""",
    30, """<ol><li>A: in fast speech, <i>have to</i> sounds like "hafta" and <i>has to</i> like "hasta"; the d in <i>supposed to</i> and <i>allowed to</i> almost disappears.</li>
<li>B: script: 1 You have to say a letter. 2 You don't have to start with A. 3 You must use real words. 4 You don't have to write anything. 5 You have to wait for your turn. 6 You don't have to answer quickly. Listen for <i>don't</i>.</li></ol>""")

    # Page 6
    gaps = [("The", "aim", "of the game is to write one word for each category, for example a fruit, a country and a name."),
            ("First, all the players", "have to", "write the categories at the top of a piece of paper."),
            ("One player says the alphabet quietly, and another player says \"Stop!\" The players", "are supposed", "to use the letter where the alphabet stopped."),
            ("All the words", "must / (should)", "start with that letter. For B: banana, Brazil, Bruno…"),
            ("You", "can't", "use a word that starts with a different letter."),
            ("You're not", "allowed", "to look at the other players' papers."),
            ("You", "don't have to", "finish all the categories, but you get more points if you do."),
            ("When one player finishes, they", "can", "say \"Stop!\" and everybody stops writing."),
            ("You", "should / (must)", "check the other players' words: are they real?")]
    gl = "".join(f"<li>{a} {A(w, 'min-width:24mm')} {e}</li>" for a, w, e in gaps)
    b.page(f"""{sec(5, "Practice", "9 min")}
<div style="display:flex;gap:3mm;align-items:center"><p style="flex:1;margin:0">This game is popular all over the world, and in Brazil many people know it as <b>Stop</b>. In English it's often called <b>Categories</b>.</p>{img('C', 30, 20)}</div>
{sub("A", "Complete the rules with the words in the box. Sometimes more than one answer is possible.", "7 min")}
<div class="bank">aim · allowed · are supposed · can · can't · don't have to · have to · must · should</div>
<ol style="line-height:1.55;font-size:9pt;margin:0">{gl}</ol>
{sub("B", "Do you play this game? Are your rules the same?", "2 min")}""",
    26, """<ol><li>This replaces Linguahouse's Hangman text (the host draws a man) with a game every Brazilian student knows. Where two answers are possible, the better one is first.</li>
<li>B: let the student explain their family's version with the new forms; then play one quick round together if there's time.</li></ol>""")

    # Page 7
    ispy = ["One person has to think of a thing that everyone knows, for example a door.", "In an online class, they say: \"I'm thinking of something that starts with the letter D.\"",
            "The aim of the game is for the other person to guess the thing.", "The other player has to guess. They're not supposed to ask other questions,",
            "but if it's too difficult, they're allowed to ask for a little help."]
    alpha = ["The first player says: \"I went to the store and I bought an apple.\" It must start with A.", "The next player has to repeat it and add something with B: \"…an apple and a bag.\"",
             "Players are supposed to add one thing each time, in alphabetical order.", "The things don't have to be real store items: a cat is OK!",
             "You can take a few seconds, but you're not allowed to take too long. The aim is to be the last player who remembers everything."]
    b.page(f"""{sec(6, "Speaking: teach and play a game", "12 min")}
<div class="two"><div class="box" style="margin:0;font-size:8.8pt;line-height:1.45"><h4>YOUR GAME: I SPY (ONLINE VERSION)</h4>{"<br>".join(ispy)}</div>
<div class="box sand" style="margin:0;font-size:8.8pt;line-height:1.45"><h4>YOUR TEACHER'S GAME: THE ALPHABET GAME</h4>{"<br>".join(alpha) if T else "Your teacher is going to explain this game. Listen and ask questions: <i>Do I have to…? Can I…? Am I allowed to…?</i>"}</div></div>
{sub("A", "Read your game for one minute. Then close the book and explain the rules to your teacher. Use the forms from this lesson.", "4 min")}
{sub("B", "Play I Spy with your teacher. Use the Warm-up phrases: It's your turn! You beat me! It's a tie!", "3 min")}
{sub("C", "Listen to your teacher's game, ask questions, and play.", "4 min")}
{sub("D", "Which game is more fun? How could you explain your game better?", "1 min")}""",
    24, """<ol><li>A: the student must not read the rules aloud: the aim is to remember and explain with <i>have to, can't, don't have to, supposed to</i>.</li>
<li>C: explain the Alphabet Game from the red text without reading it; play until someone forgets an item.</li></ol>""")

    # Page 8
    pc = [("A2 Unit 39", "I can put nouns together: a coffee cup, Leo's ideas, the end of the story."), ("A2 Unit 41", "I can talk about quantities with some, any, much, many, enough and plenty of."),
          ("A2 Unit 42", "I can understand and give advice and instructions at a pharmacy."), ("A2 Unit 43", "I can explain the rules of a game.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    ow = [("2–5 people / You need / to play.", "You need 2–5 people to play."), ("has to / Player 1 / choose a person, place or thing.", "Player 1 has to choose a person, place or thing."),
          ("of the game / The aim / is to guess it.", "The aim of the game is to guess it."), ("have to / The other players / ask yes/no questions.", "The other players have to ask yes/no questions."),
          ("not allowed / They're / to ask \"When…?\" or \"Where…?\"", "They're not allowed to ask \"When…?\" or \"Where…?\""), ("can't / Players / use their phones.", "Players can't use their phones."),
          ("is twenty, / The maximum / but you / don't have to / wait to guess.", "The maximum is twenty, but you don't have to wait to guess.")]
    owl = "".join(f"<li>{w}<br>{A(s, 'min-width:90mm')}</li>" for w, s in ow)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p style="margin:.5mm 0"><b>1. Twenty Questions. Put the words in order to make the rules.</b></p>
<ol style="line-height:1.4;font-size:8.8pt;margin:0">{owl}</ol>
<p style="margin-top:1.5mm"><b>2. A game I know (50–75 words).</b> Write the rules of a game you know (a card game, a board game or a Brazilian game). Say the aim and use <i>have to, can't, don't have to</i> and <i>allowed to</i>.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class: play Twenty Questions to start the lesson; then the student explains their game from the homework and you play it.</p>""")

    b.extra("Audio script", f"""
{sub("43.1", "A game of GHOST (slow and natural)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in S431)}</p>
{sub("43.2", "Repeat: rules")}
<p>{" · ".join(S432)}</p>
{sub("43.3", "Necessary or not necessary? (3-second pause)")}
<p>{" · ".join(S433)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 43 - Word games")
