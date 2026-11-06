# Speak! Bridge A2 - Unit 26 "Housemates" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 26", audio_json="audio_a2-unit-26.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["a2-unit-26"]
S261 = [x.split(": ", 1) for x in _r["26.1 A new roommate"].split("\n")]
S262 = [x.split(": ", 1)[1] for x in _r["26.2 Repeat: adjectives and modifiers"].split("\n")]
S263 = [x.split(": ", 1)[1] for x in _r["26.3 Word stress"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 26", "Housemates", "Personality adjectives · <b>modifiers: a bit, really, so, too</b>",
                       [("YOU CAN", "describe people's personalities and write a short profile about yourself"),
                        ("LANGUAGE", "She's really smart. · He's a bit dishonest. · He's too shy. · She sounds great!"),
                        ("PRONUNCIATION", "word stress: CHEERful · poLITE · CONfident · disHONest")])
    pairs = [("confident", "shy"), ("polite", "rude"), ("smart", "stupid"), ("cheerful", "miserable")]
    pr = "".join(f"<tr><td>{2*i+1} {A(p, 'min-width:30mm')}</td><td>{2*i+2} {A(n, 'min-width:30mm')}</td></tr>" for i, (p, n) in enumerate(pairs))
    b.page(f"""{sec(1, "Warm-up: personality adjectives", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">{sub("A", "These words describe people's personalities. Find four pairs of opposites and write them in the table.", "4 min")}
<div class="bank">cheerful · confident · miserable · polite · rude · shy · smart · stupid</div></div>{img('A', 34, 22)}</div>
<table style="margin:0;table-layout:fixed;width:120mm"><tr><th>positive</th><th>negative</th></tr><tr><td><i>example: interesting</i></td><td><i>boring</i></td></tr>{pr}</table>
{sub("B", "Add a prefix to make the opposites.", "1 min")}
<p style="margin:0">1. honest → {A("dishonest", "min-width:28mm")} &nbsp;&nbsp; 2. friendly → {A("unfriendly", "min-width:28mm")}</p>
{sub("C", "Read the sentences. Which two words in bold are adjectives? Which one is an adverb?", "1 min")}
<ol style="line-height:1.5"><li>My new coworkers are <b>friendly</b>, and I already feel at home at work.</li><li>Come <b>quickly</b>! There's been an accident.</li><li>My neighbor is <b>lovely</b>. She always brings me homemade cookies.</li></ol>
<p class="small" style="margin:0">{A("adjectives: friendly, lovely (they describe people) · adverb: quickly (it describes the verb come)", "min-width:110mm")}</p>
{sub("D", "Talk about it.", "2 min")}
<ol><li>Which three adjectives in A describe you? Which describe your best friend?</li><li>Have you ever shared a house or an apartment? Would you like to?</li></ol>""",
    25, """<ol><li>A: drill the stress (CHEERful, CONfident, poLITE); the <i>h</i> in <i>honest</i> is silent. <i>Stupid</i> is strong and rude about another person; it's OK about yourself (<i>I feel so stupid!</i>).</li>
<li>C: in American English, <i>lovely</i> is used less than in British English and is more common for women; <i>great</i> or <i>wonderful</i> are more frequent. In the US, people usually say <b>roommate</b>; <i>housemate</i> is understood.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Personality adjectives · opposites · prefixes</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Lucy and Ben choose a new roommate</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Modifiers: really, very, so, a bit, a little, too · seem and sound</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Modifiers, very or too, seem and sound, opposites</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>4 min</td><td>Stressing modifiers · word stress in adjectives</td><td>5</td></tr>
<tr><td>5 Practice</td><td>9 min</td><td>Adjectives and modifiers in context · Word builder: -ly adjectives</td><td>6</td></tr>
<tr><td>6 Writing</td><td>12 min</td><td>A roommate profile (80–100 words)</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Lucy (Neural2-C) shares an apartment in Chicago with her friend Ben (Chirp3-HD-Charon). Their roommate Emma has moved out, and three people want her room: Derek (rude and maybe dishonest), Priya, a medical student (smart, cheerful and polite), and Sam, a customer at City Coffee (a little miserable and too shy). They choose Priya. All the applicants are invented, so there are no facts to check.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students translate <i>muito</i> as <i>too</i> (<i>She's too beautiful</i> ✗ when they mean <i>really beautiful</i>), use <i>a bit</i> with positive adjectives (<i>a bit friendly</i> ✗), say <i>seems a nice person</i> without <i>like</i>, and stress <i>polite</i> and <i>dishonest</i> on the first syllable.</div>
<div class="box"><h4>AUDIO</h4>Track 26.1 A new roommate (slow and natural) · Track 26.2 Repeat: adjectives and modifiers · Track 26.3 Word stress</div>""")

    # Page 2
    who = [("Derek", "rude, dishonest"), ("Priya", "smart, cheerful, polite"), ("Sam", "miserable, shy")]
    wl = "".join(f'<li>{n}: {A(a, "min-width:50mm")}</li>' for n, a in who)
    gaps = [("That's", "very", "rude. Emma's room is the smallest one!"), ("Maybe he's a", "bit", "dishonest."),
            ("I guess she's", "really", "smart. That's a difficult course."), ("She does yoga and bakes her own bread. She", "seems", "cheerful!"),
            ("She even says thank you for reading her message. She's", "so", "polite!"), ("He's all right, but he's a", "little", "miserable."),
            ("I'm surprised he wants to share an apartment. I thought he was", "too", "shy."), ("Let's go with Priya, then. She", "sounds", "great!")]
    gl = [f'<li value="{i+1}">{a} {A(g, "min-width:14mm")} {e}</li>' for i, (a, g, e) in enumerate(gaps)]
    b.page(f"""{sec(2, "Listening: a new roommate", "10 min")}
<div style="display:flex;gap:2.5mm;align-items:center"><p style="flex:1;margin:0">Lucy shares an apartment in Chicago with her friend Ben. Their roommate Emma has moved out, and three people want her room. Lucy and Ben read their messages.</p>{img('B', 26, 19)}{img('C', 26, 19)}{img('D', 26, 19)}</div>
{audiocard(["26.1 · SLOW", "26.1 · NATURAL"])}
{sub("A", "Listen and match the people with the adjectives. Some people have more than one.", "3 min", "26.1 · SLOW")}
<div class="bank">cheerful · dishonest · miserable · polite · rude · shy · smart</div>
<ol style="line-height:1.5">{wl}</ol>
<p style="margin:0">Who do they choose? {A("Priya", "min-width:25mm")}</p>
{sub("B", "Listen again and complete the sentences with one word.", "5 min", "26.1 · NATURAL")}
<ol style="line-height:1.55;font-size:9pt">{"".join(gl)}</ol>
{sub("C", "Talk about it: Would you choose Priya too? Why? What's important in a roommate?", "2 min")}""",
    22, """<ol><li>A: the photos are clues: a parking space (Derek), a stethoscope (Priya), drums (Sam).</li>
<li>B: let the student predict the words in pairs or with you first. Then play the track to check. Read the script aloud together if there is time; it prepares the next page.</li></ol>""")

    # Page 3
    b.page(f"""{sec(3, "Language focus: modifiers", "10 min")}
{sub("A", "Read the sentences and answer the questions.", "3 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">That's <b>very</b> rude. · I guess she's <b>really</b> smart. · She even says thank you. She's <b>so</b> polite!</div>
<ol style="line-height:1.7"><li>The words in bold make the adjectives {ch(["stronger", "weaker"], "stronger")}.</li>
<li>Why does Lucy say <i>so polite</i>? What information did she already have? {A("Priya says thank you for reading her message.", "min-width:62mm")}</li></ol>
{sub("B", "Read the sentences and answer the questions.", "3 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">Maybe he's <b>a bit</b> dishonest. · He's all right, but he's <b>a little</b> miserable. · I thought he was <b>too</b> shy.</div>
<ol style="line-height:1.7"><li>Which word means <i>more than we want</i>, so there is a problem? {ch(["a bit", "a little", "too"], "too")}</li>
<li>We use <i>a bit</i> and <i>a little</i> with {ch(["positive", "negative"], "negative")} adjectives. They make them sound {ch(["more polite", "stronger"], "more polite")}.</li></ol>
{sub("C", "Read the sentences and answer the question.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">She <b>seems</b> cheerful! · She <b>sounds</b> great! · He <b>sounds like</b> trouble.</div>
<p style="margin:.5mm 0">How are <i>seem</i> and <i>sound</i> different from <i>be</i>? {A("We use them when we aren't sure. Seem = from what we see or know; sound = from what we hear or read. Before a noun, add like.", "min-width:110mm")}</p>
<div class="box sand"><h4>RULE</h4><b>really / very / so</b> + adjective = stronger · <b>a bit / a little</b> + negative adjective = softer, more polite · <b>too</b> + adjective = a problem. The modifier goes <b>before</b> the adjective. More on the next page: <b>Grammar reference</b>.</div>""",
    22, """<ol><li>A–B: ask concept questions: <i>Is "too shy" a problem for Lucy and Ben? Is "very smart" a problem?</i> Most errors at this level are with <i>too</i>.</li>
<li>Drill the sentences: the modifier and the adjective are both stressed; <i>seems</i> and <i>sounds</i> are usually not.</li></ol>""")

    grammar_ref.adjective_modifiers(b)

    # Page 5
    stress = {"Oo": ["cheerful", "friendly", "honest"], "oO": ["polite", "relaxed"], "Ooo": ["confident", "miserable"], "oOo": ["dishonest", "unfriendly"]}
    def cell(k):
        return R(" · ".join(stress[k])) if T else '<div class="wline"></div><div class="wline"></div>'
    b.page(f"""{sub("D", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>She's too beautiful. I love her photos!</td><td><b>She's really beautiful.</b></td><td>no problem = really / very.</td></tr>
<tr><td>He's a bit friendly.</td><td><b>He's really friendly.</b></td><td>a bit + negative adjectives.</td></tr>
<tr><td>She seems a nice person.</td><td><b>She seems like a nice person.</b></td><td>seem like + noun.</td></tr>
<tr><td>He sounds greatly.</td><td><b>He sounds great.</b></td><td>sound + adjective.</td></tr>
<tr><td>He's a person too shy.</td><td><b>He's too shy.</b></td><td>modifier before the adjective.</td></tr>
<tr><td>She's very honest. /ˈhɑːnəst/ with h</td><td><b>/ˈɑːnəst/</b></td><td>silent h.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "4 min")}
{audiocard(["26.2", "26.3"])}
{sub("A", "Listen and repeat. Stress the modifier and the adjective.", "2 min", "26.2")}
{twocol([f'<li value="{i+1}">{s}</li>' for i, s in enumerate(S262)], 4)}
{sub("B", "Listen to the adjectives. Write each one in the correct stress column. O = stressed syllable.", "2 min", "26.3")}
<p class="small" style="margin:0 0 .5mm">{" · ".join(S263)}</p>
<table style="margin:0;table-layout:fixed"><tr><th>Oo</th><th>oO</th><th>Ooo</th><th>oOo</th></tr><tr><td>{cell("Oo")}</td><td>{cell("oO")}</td><td>{cell("Ooo")}</td><td>{cell("oOo")}</td></tr></table>""",
    22, """<ol><li>B: prefixes (<i>dis-</i>, <i>un-</i>) don't change the stress: HONest → disHONest, FRIENDly → unFRIENDly.</li>
<li>Brazilians often say <i>PO-lite</i> and <i>CON-fi-DENT</i>. Clap the syllables, then say each word in a sentence: <i>She's really poLITE.</i></li></ol>""")

    # Page 6
    gf = [("My sister is always", "confident", "when she meets new people. She talks to everyone."),
          ("The new guy at work seems", "miserable", ". I haven't seen him smile once."),
          ("The people at the store down the street never say hello or thank you. They're", "unfriendly", "."),
          ("Sometimes my best friend is", "honest", ", like when she tells me my new haircut doesn't look good."),
          ("Your doctor sounds like a", "kind", "person: friendly, helpful and patient."),
          ("I left my keys inside the apartment, and now I can't get in. I feel", "stupid", "!"),
          ("Your roommate told me a long story about his bus ride to work. I'm afraid he was", "boring", "."),
          ("You seem", "cheerful", "today! Did you get some good news?")]
    gfl = "".join(f"<li>{a} {A(w, 'min-width:20mm')}{e if e[0] in '.,!' else ' ' + e}</li>" for a, w, e in gf)
    ly = [("I don't have many early", "memories, but I remember the house I lived in when I was four.", "c"),
          ("My big brother gave me some brotherly", "advice: don't let your social life affect your studies.", "a"),
          ("You're lucky to have curly", "hair. You can wear it in so many styles.", "e"),
          ("They studied hard, so the most likely", "result is that the whole class will pass the test.", "f"),
          ("Lots of older people are lonely", "because their families live far away.", "b"),
          ("Please take that smelly", "garbage outside right now. It's disgusting!", "d")]
    left = "".join(f"<li>{a} {A(l, 'min-width:7mm;text-align:center')}</li>" for a, _, l in ly)
    right = "".join(f"<li>{bb}</li>" for l, bb in sorted([(l, bb) for _, bb, l in ly]))
    b.page(f"""{sec(5, "Practice", "9 min")}
{sub("A", "Complete the sentences with the words in the box.", "4 min")}
<div class="bank">boring · cheerful · confident · honest · kind · miserable · stupid · unfriendly</div>
<ol style="line-height:1.6;font-size:9pt">{gfl}</ol>
{sub("B", "Which sentences in A can you add these words to? Where do they go?", "2 min")}
<p style="margin:0;line-height:1.6">1. a bit / a little {A("2 and 7", "min-width:16mm")} &nbsp; 2. really / very {A("1, 5 and 8", "min-width:20mm")} &nbsp; 3. so {A("3 and 6", "min-width:16mm")} &nbsp; 4. too {A("4", "min-width:10mm")}</p>
{sub("C", "Word builder: adjectives ending in -ly. Match 1–6 with a–f.", "3 min")}
<div style="display:flex;gap:4mm;font-size:8.8pt"><ol style="flex:1;line-height:1.5;margin:0">{left}</ol><ol type="a" style="flex:1;line-height:1.5;margin:0">{right}</ol></div>
<p class="small" style="margin:.8mm 0 0">Talk about it: Do you have any early memories? How can we help lonely older people? What's likely to happen to you tomorrow?</p>""",
    22, """<ol><li>B: sentences with the modifiers: 2 a bit miserable · 7 a bit boring · 1 really confident · 5 a really kind person · 8 very cheerful · 3 so unfriendly · 6 so stupid · 4 too honest. Ask the student to read the full sentences with the correct stress.</li>
<li>C: these words end in -ly, but they are adjectives, like <i>friendly</i> and <i>lovely</i>.</li></ol>""")

    # Page 7
    model = ("Hi! I'm Priya, and I'm a second-year medical student. People say I'm really cheerful, and I love meeting new people, so I think I'd be a good roommate. "
             "I'm also very neat: I always wash the dishes right after dinner. In my free time, I do yoga and bake bread, and I'm happy to share it! "
             "I'm a bit shy at first, but not for long. My only problem is that I'm sometimes too busy with my studies, so I often stay at the library until late. "
             "Thank you so much for reading my message!")
    b.page(f"""{sec(6, "Writing: a roommate profile", "12 min")}
<div style="display:flex;gap:3mm;align-items:center"><p style="flex:1;margin:0">Imagine you want to share an apartment with people like Lucy and Ben. You are going to write a short profile about yourself.</p>{img('F', 34, 21)}</div>
{sub("A", "Read Priya's message. Underline the modifiers and the personality adjectives.", "3 min")}
<div class="msg" style="max-width:none;padding:2mm 3mm;font-size:9pt;line-height:1.45">{model}</div>
<p class="small" style="margin:.5mm 0">{A("really cheerful · very neat · a bit shy · too busy (a problem!)", "min-width:100mm")}</p>
{sub("B", "Plan. Choose two positive adjectives and one negative adjective for you. Use a different modifier with each one.", "3 min")}
<table style="margin:0"><tr><th style="width:24mm"></th><th style="width:30mm">adjective</th><th>notes</th><th style="width:40mm">modifier: a bit, a little, really, very, so, too</th></tr>
<tr><td><i>example</i></td><td><i>smart</i></td><td><i>sudoku puzzles, trivia games</i></td><td><i>too</i></td></tr>
<tr><td>positive</td><td></td><td></td><td></td></tr><tr><td>positive</td><td></td><td></td><td></td></tr><tr><td>negative</td><td></td><td></td><td></td></tr></table>
{sub("C", "Tell your teacher about your notes. Then write your profile (80–100 words).", "6 min")}
<p class="small" style="margin:0 0 1mm"><i>Example: I love sudoku puzzles and trivia games, so I'm pretty smart. Maybe some people think I'm too smart, but I like knowing things that other people don't know!</i></p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    28, """<ol><li>A: <i>neat</i> = organized and clean (American English). Point out that Priya uses a negative adjective too, but softens it with <i>a bit</i>.</li>
<li>C: the student can tell the truth or invent. Correct the spoken version first; fewer errors appear in the writing. If there isn't time, the student finishes at home.</li></ol>""")

    # Page 8
    pc = [("A2 Unit 23", "I can imagine a different situation with the second conditional."), ("A2 Unit 24", "I can plan and write a short story with direct speech."),
          ("A2 Unit 25", "I can talk about TV shows with -ed and -ing adjectives."), ("A2 Unit 26", "I can describe people's personalities with modifiers.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    ro = [("a little / but / I think / My cousin is / shy, / you'll like him.", "My cousin is a little shy, but I think you'll like him."),
          ("about her life, / it's / my grandmother / so interesting. / tells me / When", "When my grandmother tells me about her life, it's so interesting."),
          ("a bit / don't say hello / if you / It seems / meet someone. / rude / when you", "It seems a bit rude if you don't say hello when you meet someone."),
          ("is always / polite / The mail carrier / really / to everyone.", "The mail carrier is always really polite to everyone."),
          ("because / good at / her job / She's / she's / so smart.", "She's good at her job because she's so smart."),
          ("friendly, / if you know / is / That guy / too / what I mean.", "That guy is too friendly, if you know what I mean."),
          ("a dishonest / He sounds / like / person, / should avoid him. / so you", "He sounds like a dishonest person, so you should avoid him."),
          ("and I / can't wait / for you / great, / My new roommate / is really / to meet her.", "My new roommate is really great, and I can't wait for you to meet her.")]
    rol = "".join(f'<li><span class="small">{w}</span><br>{A(s, "min-width:120mm")}</li>' for w, s in ro)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Put the words in order to make sentences.</b></p>
<ol style="line-height:1.45">{rol}</ol>
<p style="margin-top:1.5mm"><b>2. Finish your roommate profile.</b> Then write 3–4 sentences about a friend or family member. Use <i>seem</i> or <i>sound</i> and at least two modifiers.</p>""",
    18, """<p>Next class: the student reads the profile aloud. Ask: <i>Would you be a good roommate for Lucy and Ben? Why?</i> Collect the writing to correct.</p>""")

    b.extra("Audio script", f"""
{sub("26.1", "A new roommate (slow and natural)")}
<p style="line-height:1.42">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in S261)}</p>
{sub("26.2", "Repeat: adjectives and modifiers")}
<p>{" · ".join(S262)}</p>
{sub("26.3", "Word stress")}
<p>{" · ".join(S263)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 26 - Housemates")
