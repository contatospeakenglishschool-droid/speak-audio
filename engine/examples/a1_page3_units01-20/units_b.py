from p3old import unit, rules_ol, two_boxes
from speak_engine import twocol

Q = chr(39)


def items(b, lst):
    return [f'<li value="{i+1}">{x}</li>' for i, x in enumerate(lst)]


@unit(7)
def u07(b):
    A, sub = b.A, b.sub
    qs = [("What", "do", "you", "do", "on the weekends?", "I watch TV."), ("How often", "do", "you", "go", "jogging?", "Once a year!"), ("When", "does", "Tom", "go", "to the gym?", "On Saturday morning.")]
    qt = "".join(f"<tr><td><b>{a}</b></td><td>{c}</td><td>{d}</td><td>{e}</td><td>{f}</td><td>{g}</td></tr>" for a, c, d, e, f, g in qs)
    sc = ["always", "usually", "often", "sometimes", "rarely", "hardly ever", "never"]
    sct = "".join(f"<td style='text-align:center'><b>{w}</b></td>" for w in sc)
    body = f"""{b.sec(3, "Language focus", "10 min")}
{sub("A", "Questions with question words. Read and repeat.", "2 min", pt="Perguntas com palavras interrogativas. Leia e repita.")}
<table style="table-layout:fixed;font-size:9pt"><tr><th>Question word</th><th>do / does</th><th>subject</th><th>verb</th><th></th><th>Answer</th></tr>{qt}</table>
<p class="small" style="margin:.5mm 0">What = o quê · When = quando · How often = com que frequência · Where = onde</p>
{sub("B", "Adverbs of frequency. Study the scale and the position.", "4 min", pt="Advérbios de frequência. Estude a escala e a posição.")}
<table style="table-layout:fixed;margin-top:0"><tr><td class="small">100%</td><td colspan="5"></td><td class="small" style="text-align:right">0%</td></tr><tr>{sct}</tr></table>
{two_boxes("<h4>POSITION: MAIN VERB</h4>before the main verb:<br>I <b>always</b> watch TV.<br>She <b>never</b> cooks.", "<h4>POSITION: BE</h4>after <i>am / is / are</i>:<br>I'm <b>always</b> tired on Monday.<br>He's <b>never</b> late.")}
<div class="box" style="margin-top:1.5mm"><h4>MORE WAYS TO SAY HOW OFTEN</h4>every day · every morning · on Saturdays · once a week · <b>twice</b> a year · three times a month → at the <b>end</b>: <i>I cook every day.</i></div>
{sub("C", "Look at A and B. Choose the correct option.", "4 min", pt="Olhe A e B. Escolha a opção correta.")}
{rules_ol(b, [("With <b>he / she</b>, the auxiliary is", "does", "do", ".", True), ("In questions, the main verb", "doesn" + Q + "t change", "changes", ".", False),
              ("<i>always / never</i> go", "before", "after", " the main verb.", True), ("With the verb <i>be</i>, <i>always / never</i> go", "after", "before", " am / is / are.", False)])}"""
    notes = """<ol><li>A: point at the columns: question word + do/does + subject + verb. The same as Unit 6, with a word at the start.</li>
<li>B: draw a line on the board 0–100% and ask: <i>Lucy, cook?</i> (never) <i>Tom, cook?</i> (every day = always). <i>hardly ever</i> = quase nunca. <i>Twice</i> = duas vezes. C: the student checks the rules.</li></ol>"""
    return body, 26, notes


@unit(8)
def u08(b):
    A, sub = b.A, b.sub
    l1 = items(b, [f"What do you like {A('doing', 'min-width:16mm')} on the weekends?", f"I {A('love', 'min-width:14mm')} going shopping.", f"Do you like taking the bus? No, I {A('don' + Q + 't', 'min-width:14mm')}.",
                   f"I really {A('hate', 'min-width:14mm')} it.", f"I {A('prefer', 'min-width:16mm')} taking the train.", f"I don't like {A('doing', 'min-width:16mm')} homework."])
    body = f"""{b.sec(3, "Language focus: love, like, hate + -ing", "10 min")}
{sub("A", "Grammar table: verb + -ing", "4 min", pt="Tabela de gramática: verbo + -ing")}
<div class="box" style="margin-top:0"><h4>LOVE, LIKE, HATE, PREFER + -ING</h4>After <b>love, like, hate, prefer</b>, we use the <b>-ing form</b>: I love <b>going</b> shopping. · I prefer <b>taking</b> the train.<br>
Short answers: Do you like cooking? <b>Yes, I do.</b> / <b>No, I don't.</b> (not <i>Yes, I like</i>) · <b>really</b> goes before the verb: I <b>really</b> hate it.</div>
<table style="table-layout:fixed;margin-top:1mm;font-size:9pt"><tr><th>Most verbs: + -ing</th><th>Verb ends in -e: – e + -ing</th><th>Short verb, 1 vowel + 1 consonant: double!</th></tr>
<tr><td>go → going · read → reading<br>play → playing · do → doing</td><td>bake → baking · take → taking<br>dance → dancing · ride → riding</td><td>shop → shopping · run → running<br>swim → swimming · get → getting</td></tr></table>
{two_boxes("<h4>HOW MUCH?</h4>++ I <b>love</b> it. &nbsp; + I <b>like</b> it.<br>– I <b>don't like</b> it. &nbsp; – – I <b>hate</b> it.<br>I <b>really</b> like it! (stronger)", "<h4>HE / SHE</h4>She <b>loves</b> baking. He <b>hates</b> running.<br>She <b>doesn't like</b> doing homework.<br><b>Does</b> she <b>like</b> cooking?")}
{sub("B", "Look at A. Choose the correct option.", "3 min", pt="Olhe A. Escolha a opção correta.")}
{rules_ol(b, [("After <b>love / like / hate / prefer</b>, we use", "the -ing form", "the infinitive", ".", True), ("The short answer is", "Yes, I do. / No, I don" + Q + "t.", "Yes, I like. / No, I don" + Q + "t like.", "", False),
              ("<b>really</b> goes", "before", "after", " the verb: <i>I ___ hate it.</i>", True), ("<b>prefer</b> means", "like more", "like less", ".", False)])}
{sub("C", "Complete the sentences. Then listen and check.", "3 min", "8.1 · NATURAL", pt="Complete as frases das entrevistas. Depois, ouça e confira.")}
{twocol(l1, 4)}"""
    notes = """<ol><li>A: in Portuguese we say <i>Eu gosto de ir</i>; in English, <i>like going</i>. Think of -ing as the "noun form" of the verb. Write <i>shopping</i> and <i>taking</i> on the board and show the spelling rules.</li>
<li>B: a very common short answer mistake is <i>Yes, I like.</i> Correct it every time: <i>Yes, I do.</i> C uses the audio.</li></ol>"""
    return body, 24, notes


def pron_page(b, n, title, table_title, table_pt, table_html, boxes, b_rules, c_title, c_pt, audio, citems, split, bank, notes, nh):
    A, sub = b.A, b.sub
    body = f"""{b.sec(3, title, "10 min")}
{sub("A", table_title, "4 min", pt=table_pt)}
{table_html}{boxes}
{sub("B", "Look at the table. Choose the correct option.", "3 min", pt="Olhe a tabela. Escolha a opção correta.")}
{rules_ol(b, b_rules)}
{sub("C", c_title, "3 min", audio, pt=c_pt)}
{twocol(items(b, citems), split)}
<div class="bank">{bank}</div>"""
    return body, nh, notes


@unit(10)
def u10(b):
    A = b.A
    rows = [("I", "me", "Can you help <b>me</b>?"), ("you", "you", "I love <b>you</b>."), ("he", "him", "Tom? I know <b>him</b>."), ("she", "her", "This cake is for <b>her</b>."),
            ("it", "it", "Chocolate? I love <b>it</b>!"), ("we", "us", "Come with <b>us</b>!"), ("they", "them", "Cookies? She loves <b>them</b>.")]
    th = '<table style="table-layout:fixed"><tr><th>Subject</th><th>Object</th><th>Example</th></tr>' + "".join(f"<tr><td>{a}</td><td><b>{o}</b></td><td>{e}</td></tr>" for a, o, e in rows) + "</table>"
    return pron_page(b, 10, "Language focus: object pronouns", "Grammar table", "Tabela de gramática: pronome sujeito (antes do verbo) e objeto (depois do verbo ou de for, with, to…)", th, "",
                     [("In <i>Teenagers buy pancakes</i>, <i>Teenagers</i> is the", "subject", "object", ".", True), ("In <i>They love them</i>, <i>them</i> is the", "object", "subject", ".", False),
                      ("The subject comes", "before", "after", " the verb.", True), ("Two pronouns don" + Q + "t change:", "you and it", "he and she", ".", False)],
                     "Complete the sentences from Kate's story. Then listen and check.", "Complete as frases da Kate. Depois, ouça e confira.", "9.1 · NATURAL",
                     [f"Children ask for candy. They love {A('it', 'min-width:14mm')}.", f"An old man visits {A('me', 'min-width:14mm')} at ten.", f"Teenagers buy pancakes and share {A('them', 'min-width:14mm')}.",
                      f"Chocolate helps {A('them', 'min-width:14mm')} work.", f"Tom buys cookies. His students love {A('them', 'min-width:14mm')}!"], 4, "it · me · them",
                     """<ol><li>A: key idea: <b>subject</b> = who does (before the verb); <b>object</b> = who receives (after the verb or after <i>for, with, to</i>). Portuguese: <i>Eu a amo / Eu amo ela</i>. English is always verb + object pronoun → <i>I love her</i>.</li>
<li>C: singular thing → <i>it</i> (chocolate, cake). Plural → <i>them</i> (cookies, pancakes). Check every time!</li></ol>""", 26)


@unit(11)
def u11(b):
    A = b.A
    rows = [("I", "my phone", "mine", "It's my phone. It's <b>mine</b>."), ("you", "your phone", "yours", "Is it <b>yours</b>?"), ("he", "his phone", "his", "It's <b>his</b>. (no change!)"),
            ("she", "her phone", "hers", "They're <b>hers</b>."), ("we", "our phones", "ours", "These bags are <b>ours</b>."), ("they", "their phones", "theirs", "The car is <b>theirs</b>."), ("Tom", "Tom's phone", "Tom's", "Whose is it? It's <b>Tom's</b>.")]
    th = '<table style="table-layout:fixed;font-size:9pt"><tr><th style="width:18mm">Subject</th><th>Possessive + noun</th><th>Possessive alone</th><th>Example</th></tr>' + "".join(f"<tr><td>{a}</td><td>{p}</td><td><b>{o}</b></td><td>{e}</td></tr>" for a, p, o, e in rows) + "</table>"
    return pron_page(b, 11, "Language focus: mine, yours, hers…", "Grammar table", "Tabela de gramática", th, "",
                     [("<b>my, your, his, her</b> go", "before a noun", "alone", ".", True), ("<b>mine, yours, hers</b> go", "alone (no noun after)", "before a noun", ".", False),
                      ("To ask about the owner, we say", "Whose is this?", "Who is this?", "", True), ("<i>It's</i> = it is. The possessive is", "its", "it" + Q + "s", ".", False)],
                     "Complete the sentences from the dialogue. Then listen and check.", "Complete as frases do diálogo. Depois, ouça e confira.", "11.1 · NATURAL",
                     [f"Tom, is this {A('your', 'min-width:14mm')} phone?", f"Lucy, is it {A('yours', 'min-width:14mm')}? Yes, it's {A('mine', 'min-width:14mm')}!", f"These are Rita's glasses. They're {A('hers', 'min-width:14mm')}.",
                      f"{A('Whose', 'min-width:14mm')} keys are these?", f"They're {A('Kate' + Q + 's', 'min-width:14mm')}.", f"The backpack is {A('yours', 'min-width:14mm')}, Tom!"], 4, "your · yours (×2) · mine · hers · Whose · Kate's",
                     """<ol><li>A: key idea: <i>mine, yours, hers…</i> replace "possessive + noun": <i>It's my phone = It's mine.</i> Never <i>mine phone</i>. Portuguese uses <i>meu</i> for both; English has two forms. Most pronouns add -s: <i>yours, hers, ours, theirs</i>; <i>mine</i> is the exception.</li>
<li>C uses the audio.</li></ol>""", 22)


@unit(12)
def u12(b):
    A = b.A
    th = ('<table style="table-layout:fixed"><tr><th style="width:24mm"></th><th>Near (here)</th><th>Far (over there)</th></tr>'
          '<tr><td><b>Singular</b></td><td><b>this</b> bench · <b>This</b> is my garden.</td><td><b>that</b> tree · <b>That\'s</b> a gate.</td></tr>'
          '<tr><td><b>Plural</b></td><td><b>these</b> flowers · <b>These</b> are my plants.</td><td><b>those</b> trees · <b>Those</b> are my neighbors.</td></tr></table>')
    box = ('<div class="box" style="margin-top:1.5mm"><h4>PORTUGUÊS × INGLÊS</h4>Português: <i>este, esse, aquele</i> (3). Inglês: só 2. <b>this</b> = este/esse (perto) · <b>that</b> = esse/aquele (longe).<br>'
           '<b>Also:</b> <i>That\'s</i> = That is (very common!). There is no contraction for <i>this is</i>.</div>')
    return pron_page(b, 12, "Language focus: this, that, these, those", "Grammar table", "Tabela de gramática", th, box,
                     [("We use <b>this</b> and <b>that</b> with", "singular", "plural", " nouns.", True), ("We use <b>these</b> and <b>those</b> with", "plural", "singular", " nouns.", False),
                      ("Near me (here):", "this / these", "that / those", ".", True), ("Far from me (over there):", "that / those", "this / these", ".", False)],
                     "Complete the sentences. Then listen and check.", "Complete as frases da chamada. Depois, ouça e confira.", "12.1 · NATURAL",
                     [f"Look! {A('This', 'min-width:14mm')} is my favorite place.", f"{A('These', 'min-width:14mm')} flowers are from my mother.", f"{A('That', 'min-width:14mm')} tree is very tall!",
                      f"Is {A('that', 'min-width:14mm')} a gate over there?", f"Show me {A('those', 'min-width:14mm')} plants next time!"], 4, "this · that (×2) · these · those",
                     """<ol><li>A: use real objects: pick up your pen (<i>this pen</i>), point at the door (<i>that door</i>). Then the student does the same.</li>
<li>Pronouns: <i>This is my favorite place</i>; no noun after <i>this</i>. On the phone: <i>Hi, this is Ana.</i> C uses the audio.</li></ol>""", 24)
