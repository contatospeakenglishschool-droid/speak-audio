# Speak! Essentials A1 - Unit 24 "Hit makers" (all English) - built with the shared engine
import sys
sys.path.insert(0, "/home/claude/speak-audio/engine")
from speak_engine import *
setup(band="A1 · UNIT 24", audio_json="audio_a1-unit-24.json", img_dir="img")

PHOTOS = [("A", "a band", "band"), ("B", "a concert", "concert"), ("C", "the drums", "drums"), ("D", "a guitar", "guitar"),
          ("E", "a microphone", "microphone"), ("F", "a piano", "piano"), ("G", "a record", "record"), ("H", "a studio", "studio")]

SCRIPT = [("Host", "Hello and welcome to Music Lives! Today's star is Rita Lee, the Queen of Brazilian Rock."),
          ("Host", "She was born in São Paulo on December 31, 1947. Her full name was Rita Lee Jones, but everybody called her Rita Lee. Her father was a dentist, and her mother was a pianist."),
          ("Host", "Rita started her career in 1966 with the band Os Mutantes. Their music was rock with a lot of Brazilian sounds, and it attracted a lot of attention."),
          ("Host", "In 1972 her time with Os Mutantes ended, and she started a solo career. Her red hair and her crazy stage clothes attracted a lot of attention too!"),
          ("Host", "In 1976 she started to work with the musician Roberto de Carvalho. They worked together for many years, and they married in 1996."),
          ("Host", "Rita recorded a lot of albums, and people all over Brazil listened to her songs. She is still the best-selling female singer in the history of Brazil."),
          ("Host", "Rita Lee died in São Paulo in 2023, but millions of fans still love her music. That's all for today. See you next week on Music Lives!")]
S242 = [("/d/", "moved · played · listened · changed"), ("/t/", "worked · watched · danced · stopped"), ("/ɪd/", "started · attracted · ended · recorded")]
S243 = ["She started her career in 1966.", "The band attracted a lot of attention.", "She worked with Roberto de Carvalho.", "People listened to her songs.", "I watched a concert last night.", "We danced all night."]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LEVEL A1 · UNIT 24", "Hit Makers", "Music and careers · <b>past simple: regular verbs</b> · -ed endings",
                       [("YOU CAN", "tell the story of a music star and talk about your past"),
                        ("LANGUAGE", "She started her career in 1966. · They married in 1996. · I watched a concert."),
                        ("PRONUNCIATION", "-ed: /d/ played · /t/ worked · /ɪd/ started")])
    words = ["a band", "a concert", "the drums", "a guitar", "a microphone", "a piano", "a record", "a studio"]
    phr = [("start a career", "c"), ("release an album", "e"), ("attract attention", "a"), ("record a song", "f"), ("perform live", "b"), ("play a character", "d")]
    means = ["make people look at you and talk about you", "sing or play in front of people", "begin your work life",
             "be a different person in a movie", "start to sell a new collection of songs", "put your music on a file in a studio"]
    pl = [f'<li value="{i+1}"><b>{p}</b> {A(k, "min-width:8mm")}</li>' for i, (p, k) in enumerate(phr)]
    mb = "".join(f"<div>{chr(97+i)}. {m}</div>" for i, m in enumerate(means))
    b.page(f"""{sec(1, "Warm-up: music words", "8 min")}
{sub("A", "Look, listen and repeat. Then write the word under the photo.", "3 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Music careers. Match the phrases 1–6 with the meanings a–f.", "5 min")}
<div class="two"><div><ol style="line-height:1.6">{"".join(pl)}</ol></div><div class="small" style="line-height:1.55">{mb}</div></div>""",
    18, """<ol><li>A: <b>a record</b> /ˈrekərd/ (noun) ≠ <b>to record</b> /rɪˈkɔrd/ (verb). Ask: <i>Do you play an instrument?</i></li>
<li>B: <b>live</b> /laɪv/ here, like <i>five</i>. <b>release</b> = <i>lançar</i> an album.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>8 music words with photos · phrases about music careers</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>A podcast about Rita Lee</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Past simple of regular verbs: use and spelling (-d, -ed, double consonant, -ied)</td><td>3</td></tr>
<tr><td>4 Pronunciation lab</td><td>5 min</td><td>Three sounds of -ed: /d/, /t/, /ɪd/</td><td>4</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Tim Maia's timeline: present → past</td><td>5</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Tom and Ana as teenagers (but / and) · your past · <i>play</i></td><td>6</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>7</td></tr></table>
<div class="box"><h4>HOW THIS GUIDE WORKS</h4>Every page looks like the Student Book page with the same number. Your notes are in the <b>yellow box</b>.
<span class="red">Answers in red</span> are not in the Student Book. The <span class="time">5 min</span> chips show the time for each activity. Audio scripts are on the last page.</div>
<div class="box sand"><h4>THE STORY CONTINUES</h4>After the exhibition (Unit 23), Tom wants to know more about Brazilian music. Ana sends him an episode of the podcast <i>Music Lives</i> about Rita Lee. On page 6, the student compares Tom and Ana when they were teenagers: Tom played the guitar and listened to rock; Ana played the piano and listened to bossa nova.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Brazilians often say every -ed as an extra syllable: <i>work-ED</i> ✗ → <b>workt</b> /wɜrkt/, <i>play-ED</i> ✗ → <b>playd</b>. Only verbs ending in /t/ or /d/ get the extra syllable: <b>start-ed</b>, <b>end-ed</b>. Also: <i>I listened music</i> ✗ → <b>listened to music</b>.</div>
<div class="box"><h4>AUDIO</h4>Track 24.1 Podcast: Rita Lee (slow and natural) · Track 24.2 -ed endings · Track 24.3 Sentences</div>""")

    # Page 2
    ch1 = [(["Rio", "São Paulo"], "São Paulo", "Rita Lee was from"), (["Rita Lee Jones", "Rita Lee Smith"], "Rita Lee Jones", "Her full name was"),
           (["a singer", "a pianist"], "a pianist", "Her mother was"), (["1966", "1976"], "1966", "She started her career in"),
           (["Os Mutantes", "Os Paralamas"], "Os Mutantes", "Her first band was"), (["red", "blue"], "red", "Her famous hair was"),
           (["1976", "1996"], "1996", "She married Roberto de Carvalho in"), (["2003", "2023"], "2023", "She died in")]
    cl = [f'<li value="{i+1}">{s} {ch(o, r)}.</li>' for i, (o, r, s) in enumerate(ch1)]
    gp = [("She started her", "career", "in 1966 with the band Os Mutantes."), ("The band's music attracted a lot of", "attention", "."),
          ("In 1972, she started a", "solo", "career."), ("She worked with the", "musician", "Roberto de Carvalho."),
          ("She recorded a lot of", "albums", "."), ("Millions of", "fans", "still love her music.")]
    gl = [f'<li value="{i+1}">{a} {A(x, "min-width:22mm")}{c if c == "." else " " + c}</li>' for i, (a, x, c) in enumerate(gp)]
    b.page(f"""{sec(2, "Listening: a music podcast", "10 min")}
<p>Tom loves Brazilian music now. Ana sends him an episode of the podcast <i>Music Lives</i>. Today's star is Rita Lee.</p>
{audiocard(["24.1 · SLOW", "24.1 · NATURAL"])}
{sub("A", "Guess first. Then listen and choose the correct words.", "4 min", "24.1 · SLOW")}
{twocol(cl, 5)}
{sub("B", "Listen again and complete. One word is extra.", "4 min", "24.1 · NATURAL")}
<div class="bank">albums · attention · career · character · fans · musician · solo</div>
{twocol(gl, 4)}
{sub("C", "Do you know any songs by Rita Lee? Who is a famous Brazilian singer for you?", "2 min")}
<div class="wline"></div>""",
    22, """<ol><li>A: let the student guess before listening; it's fine to be wrong. <i>Queen of Brazilian Rock</i> = her nickname.</li>
<li>B: extra word: <span class="red">character</span>. Ask: <i>Is this about now or the past?</i> (the past: <i>started, attracted, ended…</i>)</li></ol>""")

    # Page 3
    rules = [("Verbs ending in <i>-e</i> (move, change, release): add", "-d", "-ed"),
             ("Most verbs (start, play, attract): add", "-ed", "-d"),
             ("Short verbs with consonant + vowel + consonant (stop, plan):", "double the last letter + -ed", "add -ed"),
             ("Verbs ending in consonant + <i>-y</i> (marry, study):", "change -y to -ied", "add -ed")]
    def rule(i, s, right, wrong):
        o = [right, wrong] if i % 2 == 0 else [wrong, right]
        o = [R(f"<u>{x}</u>") if (T and x == right) else x for x in o]
        return f"<li>{s} <b><i>{o[0]}</i></b> / <b><i>{o[1]}</i></b>.</li>"
    vb = [("dance", "danced"), ("stop", "stopped"), ("study", "studied"), ("play", "played"), ("plan", "planned"), ("try", "tried"), ("listen", "listened"), ("love", "loved")]
    vl = [f'<li value="{i+1}">{v} → {A(p, "min-width:22mm")}</li>' for i, (v, p) in enumerate(vb)]
    b.page(f"""{sec(3, "Language focus: past simple (regular verbs)", "10 min")}
{sub("A", "Read the sentences from the podcast.", "2 min")}
<div class="bank" style="background:#fff;font-weight:600">Rita <u>started</u> her career in 1966. · Her time with Os Mutantes <u>ended</u> in 1972. · They <u>married</u> in 1996. · People <u>listened</u> to her songs.</div>
<div class="box" style="margin-top:0"><h4>PAST SIMPLE</h4>We use the past simple for <b>finished actions in the past</b>, often with a time: <i>in 1966, last night, yesterday, two years ago</i>.<br>
The form is the <b>same for all people</b>: I / you / he / she / we / they <b>worked</b>. (No <i>-s</i>, no <i>was</i>: <s>She was worked</s> ✗)</div>
{sub("B", "Spelling. Choose the correct option.", "4 min")}
<ol>{"".join(rule(i, *r) for i, r in enumerate(rules))}</ol>
<table style="table-layout:fixed;margin-top:1mm"><tr><th>+ -d</th><th>+ -ed</th><th>double + -ed</th><th>-y → -ied</th></tr>
<tr><td>move → moved<br>release → released</td><td>start → started<br>play → played</td><td>stop → stopped<br>plan → planned</td><td>marry → married<br>study → studied</td></tr></table>
{sub("C", "Write the past simple.", "3 min")}
{twocol(vl, 5)}""",
    27, """<ol><li>A: point at the time words. <i>She is worked</i> and <i>She was worked</i> are common mistakes: the past simple is <b>one word</b>.</li>
<li>B–C: <i>play → played</i> (vowel + y: just -ed). <i>try → tried</i> (consonant + y). Spelling first; pronunciation on the next page.</li></ol>""")

    # Page 4
    sort = ["acted", "continued", "died", "listened", "played", "released", "stopped", "watched"]
    ans = {"acted": "/ɪd/", "continued": "/d/", "died": "/d/", "listened": "/d/", "played": "/d/", "released": "/t/", "stopped": "/t/", "watched": "/t/"}
    sl = " &nbsp;·&nbsp; ".join(f"{w} {R(ans[w]) if T else ''}" for w in sort)
    rows = "".join(f'<td style="width:33%"><b style="font-size:12pt;color:{TEAL}">{s}</b><br>{w}</td>' for s, w in S242)
    b.page(f"""{sub("D", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>Yesterday I watch a movie.</td><td><b>Yesterday I watched a movie.</b></td><td>Finished action: past.</td></tr>
<tr><td>She was started her career.</td><td><b>She started her career.</b></td><td>No <i>was</i> with past verbs.</td></tr>
<tr><td>I studyed English.</td><td><b>I studied English.</b></td><td>consonant + y → <i>-ied</i>.</td></tr>
<tr><td>The music stoped.</td><td><b>The music stopped.</b></td><td>Double the <i>p</i>.</td></tr>
<tr><td>I listened music all day.</td><td><b>I listened to music all day.</b></td><td>listen <i>to</i>.</td></tr>
<tr><td>I work-ED. /ˈwɜrkɪd/</td><td><b>I worked. /wɜrkt/</b></td><td>One syllable!</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "5 min")}
{audiocard(["24.2", "24.3"])}
{sub("A", "Three sounds of -ed. Listen and repeat.", "2 min", "24.2")}
<table style="table-layout:fixed;margin-top:0"><tr>{rows}</tr>
<tr><td class="small">most verbs</td><td class="small">after the sounds /p/, /k/, /s/, /ʃ/, /tʃ/</td><td class="small">only after /t/ or /d/: an extra syllable</td></tr></table>
{sub("B", "Where do these verbs go: /d/, /t/ or /ɪd/? Say them.", "1 min")}
<div class="bank" style="background:#fff">{sl}</div>
{sub("C", "Listen and repeat the sentences.", "2 min", "24.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S243)}</div>""",
    24, """<ol><li>4A: the big rule: the extra syllable /ɪd/ is <b>only</b> after <i>t</i> or <i>d</i>. Most verbs are /d/. Put a hand on the throat: /d/ vibrates, /t/ doesn't.</li>
<li>4B: <i>released</i> ends in the sound /s/, so it is /t/ (spelling <i>-sed</i>, sound /st/).</li></ol>""")

    # Page 5
    tl = [("1959", [("He", "travel", "traveled", "to the USA. He"), ("", "live", "lived", "in New York State, and he"), ("", "learn", "learned", "English.")]),
          ("1961", [("He", "move", "moved", "to New York City. He"), ("", "join", "joined", "a vocal group called The Ideals.")]),
          ("1964", [("He", "return", "returned", "to Brazil.")]),
          ("1970", [("He", "release", "released", "his first album. People"), ("", "love", "loved", "his soul music.")]),
          ("1970s–1990s", [("He", "record", "recorded", "a lot of albums. He"), ("", "mix", "mixed", "soul music with samba.")]),
          ("1998", [("He", "die", "died", "in Niterói, near Rio.")])]
    n = 0; rows = ""
    for yr, parts in tl:
        cells = ""
        for a, v, p, c in parts:
            n += 1
            cells += f'{a} <span class="small">({n})</span> {A(p, "min-width:22mm")} <span class="small">({v})</span> {c} '
        rows += f'<tr><td style="width:24mm"><b>{yr}</b></td><td style="line-height:1.9">{cells}</td></tr>'
    b.page(f"""{sec(5, "Practice", "8 min")}
{sub("A", "Read about Tim Maia. Write the verbs in the past simple. Then read the story aloud with the correct -ed sounds.", "8 min")}
<div class="msg" style="max-width:none;padding:2mm 4mm;margin-bottom:2mm">Tim Maia was a famous Brazilian singer. He was born in Rio de Janeiro in 1942. His real name was Sebastião Rodrigues Maia. He was famous for soul music and for songs like <i>Azul da Cor do Mar</i>.</div>
<table>{rows}</table>
<div class="box"><h4>READ IT ALOUD</h4>Say the story to your teacher. Be careful with <b>learned</b> /lɜrnd/, <b>mixed</b> /mɪkst/ and <b>recorded</b> /rɪˈkɔrdɪd/.</div>""",
    24, """<p>Sounds: traveled /d/, lived /d/, learned /d/, moved /d/, joined /d/, returned /d/, released /t/, loved /d/, <b>recorded /ɪd/</b>, mixed /t/, died /d/. Ask: <i>Where was Tim Maia in 1961?</i> Then extra: <i>Do you know other Brazilian singers who lived in another country?</i></p>""")

    # Page 6
    cmp = [("listen to", "rock music", "bossa nova"), ("play", "the guitar", "the piano"), ("watch", "music videos on TV", "telenovelas with her mom"),
           ("collect", "CDs", "posters of singers"), ("dance", "never!", "every weekend"), ("travel", "to concerts in Chicago", "to Rio with her family")]
    ct = "".join(f"<tr><td><b>{i+1}. {v}</b></td><td>{t}</td><td>{a}</td></tr>" for i, (v, t, a) in enumerate(cmp))
    play = [("an instrument", "He plays the guitar."), ("with other people", "She plays in a band."), ("on the radio", "They play her songs on the radio."), ("in front of people", "The band played live in São Paulo.")]
    pt = "".join(f"<tr><td class='small'>{a}</td><td>{x}</td></tr>" for a, x in play)
    b.page(f"""{sec(6, "Speaking", "12 min")}
{sub("A", "Tom and Ana in the 1990s. They were teenagers. Make sentences with but or and.", "5 min")}
<table><tr><th style="width:30mm"></th><th>Tom (Chicago)</th><th>Ana (São Paulo)</th></tr>{ct}</table>
<p class="small"><b>Example:</b> Tom listened to rock music, but Ana listened to bossa nova.</p>
{sub("B", "Your past. Tell your teacher. Use the verbs.", "4 min")}
<div class="bank" style="background:#fff">listen to · watch · play · dance · travel · cook · study · visit · work · stay at home</div>
<ol><li>Last weekend, I…</li><li>When I was a teenager, I…</li><li>Last year, I…</li></ol>
{sub("C", "Music and you. Talk about it.", "3 min")}
<table style="margin-top:0;table-layout:fixed"><tr><th style="width:40mm">play…</th><th>Example</th></tr>{pt}</table>
<ol><li>Do you play an instrument? Do you want to learn one?</li><li>What music do they play on the radio in your city?</li><li>Who is your favorite singer or band? Do you know where they started their career?</li></ol>""",
    26, """<ol><li>A: possible answers: <i>Tom played the guitar, and Ana played the piano. Tom watched music videos, but Ana watched telenovelas. Tom never danced, but Ana danced every weekend.</i> Correct the -ed sounds.</li>
<li>B–C: questions with <i>did</i> come later; the student tells, you react: <i>Really? Nice!</i></li></ol>""")

    # Page 7
    pc = [("Unit 21", "I can ask for and give simple directions."), ("Unit 22", "I can talk about transportation and my plans."),
          ("Unit 23", "I can use was / were and say when I was born."), ("Unit 24", "I can spell regular past verbs: stopped, studied."),
          ("Unit 24", "I can say -ed correctly: played, worked, started.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hv = [("travel", "traveled", "/d/"), ("arrive", "arrived", "/d/"), ("stay", "stayed", "/d/"), ("rain", "rained", "/d/"), ("visit", "visited", "/ɪd/"),
          ("photograph", "photographed", "/t/"), ("listen", "listened", "/d/"), ("dance", "danced", "/t/"), ("want", "wanted", "/ɪd/")]
    def h(i):
        v, p, s = hv[i]
        return f"({i+1}) {A(p + (' ' + s if T else ''), 'min-width:24mm')}"
    msg = (f"Last weekend I {h(0)} to Rio for a music festival. I {h(1)} on Friday night and {h(2)} in a small hotel near the beach. "
           f"On Saturday morning it {h(3)}, so I {h(4)} a museum. In the afternoon I {h(5)} the bands, and at night I {h(6)} to a great samba group. "
           f"Everybody {h(7)} until two in the morning. I {h(8)} to stay one more day!")
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:15mm"></th><th>In English…</th><th style="width:20mm">Easy!</th><th style="width:20mm">Sometimes</th><th style="width:20mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Paulo's blog.</b> Complete with the past simple. Then write /d/, /t/ or /ɪd/ next to each verb.</p>
<div class="bank">arrive · dance · listen · photograph · rain · stay · travel · visit · want</div>
<div class="msg" style="max-width:none;line-height:1.95">{msg}</div>
<p style="margin-top:3mm"><b>2. Your weekend.</b> Write 5 sentences about last weekend. Use regular verbs (watched, cooked, played…).</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Paulo is Ana's brother, the travel photographer. Next class: the student reads the blog aloud (check the -ed sounds) and then the 5 sentences.</p>""")

    b.extra("Audio scripts", f"""
{sub("24.1", "Podcast: Rita Lee (slow and natural)")}
<p style="line-height:1.5">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("24.2", "-ed endings")}
<p>{" · ".join(f"{s} {w}" for s, w in S242)}</p>
{sub("24.3", "Sentences")}
<p>{" ".join(S243)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essentials 24 - Hit makers")
