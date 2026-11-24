# Speak! Progress B1 - Unit 43 "Staying with people" (all English) - lean B1 format
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
setup(band="B1 · UNIT 43", audio_json="audio_b1-unit-43.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-43"]
S431 = [l.split(": ", 1) for l in _r["43.1 Carol arrives at Ana's"].split("\n")]
S432 = [x.split(": ", 1)[1] for x in _r["43.2 Repeat: make yourself at home"].split("\n")]


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
    cover = cover_html(T, "LEVEL B1 · UNIT 43", "Staying with people", "Hosts and guests · <b>Make yourself at home · Help yourself</b>",
                       [("YOU CAN", "be a good host or guest: make and answer offers and requests"),
                        ("LANGUAGE", "host · guest · landlord · tenant · roommate · move out · myself · by myself · each other"),
                        ("PRONUNCIATION", "stress on -self / -selves: make yourSELF at home")])
    kw = [("the owner of an apartment or house who receives rent", "landlord"),
          ("a person who stays at your home for a short time", "guest"),
          ("to leave your home and stop living there", "move out"),
          ("a person who pays rent to live in an apartment or house", "tenant"),
          ("a person who receives visitors in their home", "host"),
          ("a person who shares an apartment or a room with you", "roommate")]
    kwl = "".join(f'<li>{A(w, "min-width:24mm")} <span style="color:#6b7377">= {d}</span></li>' for d, w in kw)
    b.page(f"""{sec(1, "Warm-up: hosts and guests", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["When you travel, do you prefer a hotel or staying with friends or family? Why?", "Who was the last person who stayed at your home? How long for?", "What makes a perfect guest room?"], "START TALKING")}</div></div>
{sub("A", "Key words. Write the words from the box next to the definitions.", "3 min")}
<div class="bank">{" · ".join(sorted(w for d, w in kw))}</div>
<ol style="font-size:8.8pt;line-height:1.75;margin:0">{kwl}</ol>
{talk(["Have you ever had a roommate? What was it like?", "Do young people in your city rent or own their homes? Why?", "What makes a good guest? And a good host?"], "USE THE WORDS")}""",
    26, """<ol><li>Top box: 3 minutes.</li>
<li>A: 4 minutes with the questions. Check the difference between <i>live</i> (your home) and <i>stay</i> (a short time, as a guest), and between <i>rent</i> (you pay) and <i>own</i> (it's yours). <i>move in</i> is the opposite of <i>move out</i>. In American English, <i>roommate</i> is used for people who share an apartment or a house.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Carol arrives at Ana's apartment for two weeks · offer or request? yes or no? · questions · Talk about it",
                      "reflexive pronouns: myself… themselves, by myself, make yourself at home, each other; verbs that are not reflexive in English", "Reflexive, each other or nothing · rewrite · Use it (oral)",
                      "make yourself at home (43.2) · host and guest: match · role-play: a guest arrives", "Carol's message to Linda · rewrite · watch out · writing a thank-you email"),
        """The Linguahouse lesson has vocabulary for living and staying (landlord, tenant, host, guest, roommate, move in and out), a dialogue where Simon welcomes his guest Gina, phrases for requests and offers, host and guest small talk, and a role-play. Polite requests were studied in B1 Unit 28 and offers in A2, so the new grammar is reflexive pronouns and <i>each other</i>, which come naturally from the host's phrases (<i>Make yourself at home. Help yourself.</i>). Story: Ana's cousin Carol flies in from Orlando to stay with Ana for two weeks. She didn't sleep on the plane (the man next to her snored); Ana's new kitchen was finished last month (Danny painted most of it, Unit 31); Carol brings chocolates and a T-shirt for Leo; coffee with a little milk, no sugar; no lunch (she ate on the plane) but she tries the cheese breads; Wi-Fi password on the fridge; a shower; she can't borrow the car (Marcos needs it for work), so Ana will take her to the beach on Saturday. Carol has been teaching herself Portuguese with an app for six months, and Leo is learning English at school: they can teach each other.""",
        """Reflexive pronouns with verbs that are reflexive in Portuguese (<i>I relaxed myself, I feel myself tired, I remember myself</i>); <i>themselves</i> for <i>each other</i>; <i>by me</i> for <i>by myself</i>; <i>Help you!</i> for <i>Help yourself!</i> Vocabulary: <i>live</i> vs <i>stay</i>; <i>rent</i> vs <i>own</i>. Pronunciation: the stress falls on <i>-self / -selves</i>.""",
        "Track 43.1 Carol arrives at Ana's (natural and slow; Ana and Carol) · Track 43.2 Repeat: make yourself at home"))

    # Page 2 - Listening
    rows = [("a coffee", "offer", "yes: a little milk, no sugar"), ("lunch", "offer", "no: she ate on the plane"),
            ("a cheese bread", "request", "yes: Help yourself!"), ("the Wi-Fi password", "request", "yes: it's on the fridge"),
            ("a shower", "request", "yes: Go ahead."), ("the car", "request", "no: Marcos needs it")]
    rt = "".join(f'<tr><td><b>{i}</b></td><td>{A(o, "min-width:20mm")}</td><td>{A(y, "min-width:44mm")}</td></tr>' for i, o, y in rows)
    qs = [("Why didn't Carol sleep on the plane?", "The man next to her snored all night."),
          ("Who painted Ana's new kitchen?", "Ana's family, but Danny painted most of it."),
          ("What did Carol bring?", "Chocolates for Ana and a T-shirt for Leo."),
          ("How can Carol and Leo help each other?", "She's teaching herself Portuguese; he's learning English: they can teach each other.")]
    ql = "".join(f"<li>{q} {A(a, 'min-width:50mm')}</li>" for q, a in qs)
    b.page(f"""{sec(2, "Listening: welcome to São Paulo!", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Ana's cousin Carol arrives from Orlando. Listen. Is it an offer (Ana) or a request (Carol)? Is the answer yes or no?", "5 min")}
<table style="font-size:8.6pt;margin:.5mm 0"><tr><th></th><th>offer or request?</th><th>yes or no? why?</th></tr>{rt}</table></div>{img('B', 34, 30)}</div>
{audiocard(["43.1 · NATURAL", "43.1 · SLOW"])}
{sub("B", "Listen again and answer.", "3 min")}
<ol style="line-height:1.5;font-size:8.6pt;margin:0">{ql}</ol>
<p style="margin:.6mm 0;font-size:8.6pt"><b>Think about it:</b> Ana says no to the car. How does she say no politely? {A("I'm afraid + a reason, a joke, and an alternative: I'll take you on Saturday.", "min-width:20mm")}</p>
{talk(["Would you lend your car to a guest? Why or why not?", "What do you usually bring when you stay with someone?", "What do you offer a guest when they arrive?"])}""",
    30, """<ol><li>A: play the natural version; play the slow one if needed. Offers come from the host, requests from the guest.</li>
<li>B: accept short answers. Ask the student to find the reflexive pronouns they heard: <i>make yourself at home, we painted it ourselves, help yourself, teaching myself, each other, enjoy myself</i>. And one verb with no pronoun: <i>Go and relax.</i></li>
<li>Talk about it: 4 minutes.</li></ol>""")

    # Page 3
    lean.grammar_in_class(b, grammar_ref.reflexive_pronouns)

    # Page 4 - Practice
    comp = [("Did you hurt", "yourself", "when you fell?"),
            ("Carol and Leo can teach", "each other", "languages."),
            ("After the long flight, Carol just wanted to relax", "—", "on the sofa."),
            ("Leo made breakfast", "himself", "this morning. Nobody helped him."),
            ("I felt", "—", "really tired after the trip."),
            ("Welcome, both of you! Make", "yourselves", "at home."),
            ("We really enjoyed", "ourselves", "at the beach."),
            ("My grandmother is 90, but she still lives by", "herself", ".")]
    cl = "".join(f"<li>{a} {A(m, 'min-width:20mm')} {z}</li>" for a, m, z in comp)
    rw = [("Nobody helped me paint the room. (by)", "I painted the room by myself."),
          ("Ana helps Carol, and Carol helps Ana. (each other)", "Ana and Carol help each other."),
          ("The kids cooked dinner without any help. (themselves)", "The kids cooked dinner themselves.")]
    rwl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw)
    use = ["What have you taught yourself? How?", "Do you prefer traveling by yourself or with friends?", "When did you last really enjoy yourself?",
           "How often do you and your family see each other?", "Do you ever talk to yourself? When?"]
    b.page(f"""{sec(4, "Practice: myself or each other?", "10 min")}
{sub("A", "Complete with a reflexive pronoun, each other, or — (nothing).", "4 min")}
<ol style="line-height:1.75;font-size:8.8pt;margin:0">{cl}</ol>
{sub("B", "Rewrite the sentences with the words in brackets.", "3 min")}
<ol style="line-height:1.45;font-size:8.7pt;margin:0">{rwl}</ol>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    30, """<ol><li>A: 4 minutes. Items 3 and 5: no pronoun after <i>relax</i> and <i>feel</i>. Item 6: two people → <i>yourselves</i>.</li>
<li>B: in 3, <i>themselves</i> can also go after <i>The kids</i>: <i>The kids themselves cooked dinner.</i></li>
<li>Use it: 3 minutes, all oral. Listen for <i>myself</i> after <i>relax, feel, remember</i> and correct it.</li></ol>""")

    # Page 5 - Speaking
    hq = ["How was the weather in Orlando when you left?", "Dinner's ready!", "How do you like São Paulo so far?", "Did you have any problems finding us?",
          "Is this your first time here?", "Let me give you a ride to the airport.", "Thank you for having me.", "You must come and have dinner with us sometime."]
    ga = ["Hot and humid, as always.", "Mmm, it smells delicious.", "It's huge! But I love it.", "None at all. I took a taxi straight here.",
          "No, actually I've been here twice.", "Thank you. I'd appreciate that.", "It was a pleasure.", "Thank you. I'd love to."]
    order = [6, 0, 4, 1, 7, 3, 5, 2]  # letters a-h show these responses
    letter = {o: "abcdefgh"[k] for k, o in enumerate(order)}
    hl = "".join(f'<li>{q} {A(letter[i], "min-width:6mm")}</li>' for i, q in enumerate(hq))
    gl = "".join(f'<div><b>{"abcdefgh"[k]}</b>&nbsp; {ga[o]}</div>' for k, o in enumerate(order))
    card = f"""<div class="box" style="margin-top:1mm;font-size:8.2pt">{R("<b>Teacher's card (C):</b> you are the host. Welcome the guest and make small talk (the trip, the weather). Offer a drink and food. Say yes to two requests and no to one (with <i>I'm afraid…</i>, a reason and an alternative). Offer a ride to the bus station. Then swap: you are the guest and make three requests.")}</div>""" if T else ""
    b.page(f"""{sec(5, "Speaking: be a good host", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.2pt"><tr><th>requests</th><th>answers</th><th>offers</th><th>answers</th></tr>
<tr><td><i>Could I…? · Is it all right if I…? · Do you mind if I…?</i></td><td><i>Sure, go ahead. · Of course. Help yourself. · I'm afraid… (+ reason)</i></td><td><i>Can I get you…? · Would you like…? · Let me take your coat.</i></td><td><i>Yes, please. That would be great. · No thanks, I'm fine. · That's very kind of you.</i></td></tr></table></div>
{audiocard(["43.2"])}
{sub("A", "Listen and repeat. The stress is on -self / -selves: make yourSELF at home.", "3 min", "43.2")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S432))}</p>
{sub("B", "Match the host and guest sentences. Then say them with your teacher.", "5 min")}
<div style="display:flex;gap:5mm;font-size:8.3pt"><ol style="flex:1.1;margin:0;line-height:1.45">{hl}</ol><div style="flex:1;margin:0;line-height:1.45">{gl}</div></div>
{sub("C", "Role-play. You arrive at your teacher's home. Make small talk and make three requests. Then swap: you are the host.", "7 min")}{card}
{talk(["Are you a better host or a better guest? Why?"], "TALK ABOUT IT")}""",
    30, """<ol><li>A: <i>yourself</i> and <i>ourselves</i> take the stress; <i>each other</i>: stress on <i>OTHer</i>.</li>
<li>B is the Linguahouse matching task with Brazilian places. C is the Linguahouse role-play for 1:1. Last 3 minutes: wrap-up (two corrections, and ask <i>Can you now be a good host or guest in English?</i>).</li></ol>""")

    # Homework
    pc = [(["myself", "me"], "myself"), (["yourself", "you"], "yourself"), (["each other", "ourselves"], "each other"),
          (["by myself", "by me"], "by myself"), (["relaxed", "relaxed myself"], "relaxed"), (["felt", "felt myself"], "felt")]
    p = [ch(o, a) for o, a in pc]
    rw2 = [("Leo taught Carol some words and Carol taught Leo some words. (each other)", "Leo and Carol taught each other some words."),
           ("Nobody helped Ana. She organized the guest room alone. (herself)", "Ana organized the guest room herself. / by herself"),
           ("Please, both of you, take as many cookies as you want. (help)", "Please help yourselves (to the cookies).")]
    rwl2 = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw2)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Carol writes to her friend Linda in Miami. Choose the correct words.", "")}</div>{img('C', 30, 19)}</div>
<div class="box" style="line-height:1.85;font-size:8.8pt;margin:.5mm 0"><b>Hi Linda!</b> I'm at Ana's in São Paulo, and I'm enjoying {p[0]} so much! On the first day Ana said "Make {p[1]} at home", and she really meant it. Leo and I are teaching {p[2]}: he corrects my Portuguese and I help him with his English homework. Yesterday Ana was at work, so I went to a museum {p[3]}. In the evening I just {p[4]} on the balcony with a cheese bread. Ana can't lend me her car, but she's taking me to the beach on Saturday. On Sunday I {p[5]} a bit homesick, but it passed! Love, Carol</div>
{sub("B", "Rewrite the sentences with the words in brackets.", "")}
<ol style="line-height:1.5;font-size:8.7pt;margin:0">{rwl2}</ol>
{lean.watch_out([("I relaxed myself on the balcony.", "I relaxed on the balcony.", "<i>relax, feel, worry, remember</i>: no reflexive pronoun."), ("Carol and Leo help themselves.", "Carol and Leo help each other.", "A → B and B → A = <i>each other</i>."), ("We stayed in this apartment for ten years.", "We lived in this apartment for ten years.", "<i>live</i> = your home; <i>stay</i> = a short time, as a guest.")])}
{lean.writing_task(sub, "You stayed with a friend or relative for a weekend. Write a thank-you email to your host.", "Dear …, Thank you so much for having me last weekend!", ["what you enjoyed most", "something your host did for you", "two reflexive pronouns or each other", "an invitation: You must come and stay with me…", "100–150 words"], "I can be a good host or guest: make and answer offers and requests.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class. In A, <i>relaxed</i> and <i>felt</i> have no pronoun. Read the writing at home and choose two mistakes to discuss in class.</p>""")

    script = "".join(f"<p style='margin:.5mm 0'><b>{s}:</b> {t}</p>" for s, t in S431)
    b.extra("Audio script", f"""
{sub("43.1", "Carol arrives at Ana's (natural and slow; Ana and Carol)")}
<div style="line-height:1.3;font-size:8.4pt">{script}</div>
{sub("43.2", "Repeat: make yourself at home")}
<p>{" · ".join(S432)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 43 - Staying with people")
