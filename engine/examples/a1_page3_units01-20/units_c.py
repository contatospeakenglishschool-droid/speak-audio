from p3old import unit, rules_ol

Q = chr(39)


def std(b, title, a_title, a_pt, table, box, b_title, b_pt, bank, rules, c_title, c_pt, c_html, notes, nh, ta="4 min", tb="3 min", tc="3 min"):
    sub = b.sub
    kw = (lambda p: {"pt": p} if p else {})
    return f"""{b.sec(3, title, "10 min")}
{sub("A", a_title, ta, **kw(a_pt))}
{table}{box}
{sub("B", b_title, tb, **kw(b_pt))}
<div class="bank" style="background:#fff">{bank}</div>
{rules_ol(b, rules)}
{sub("C", c_title, tc, **kw(c_pt))}
{c_html}""", nh, notes


def box(h, t, mt="1.5mm"):
    return f'<div class="box" style="margin-top:{mt}"><h4>{h}</h4>{t}</div>'


@unit(14)
def u14(b):
    A = b.A
    t = ('<table style="table-layout:fixed"><tr><th style="width:18mm"></th><th>Singular</th><th>Plural</th></tr>'
         "<tr><td><b>+</b></td><td><b>There's</b> a lamp. (There is)</td><td><b>There are</b> two chairs. <span class='small'>(no contraction)</span></td></tr>"
         "<tr><td><b>–</b></td><td><b>There isn't</b> a sofa.</td><td><b>There aren't any</b> shelves.</td></tr>"
         "<tr><td><b>?</b></td><td><b>Is there</b> a mirror?</td><td><b>Are there any</b> chairs?</td></tr>"
         "<tr><td><b>Short</b></td><td>Yes, there is. / No, there isn't.</td><td>Yes, there are. / No, there aren't.</td></tr></table>")
    bx = box("WHERE IS IT? PREPOSITIONS", "<b>next to</b> (ao lado de) · <b>behind</b> (atrás de) · <b>in front of</b> (na frente de) · <b>between</b> (entre) · <b>on the left / on the right</b> · <b>on</b> the wall · <b>in</b> the room")
    c = f"""<ol><li>{A("There's", "min-width:18mm")} a TV in my living room.</li><li>{A("There are", "min-width:18mm")} three bedrooms in the apartment.</li><li>{A("Is there", "min-width:18mm")} a balcony? — Yes, there is.</li></ol>"""
    return std(b, "Language focus: there is / there are", "Grammar table", "Tabela de gramática", t, bx,
               "Look at the sentences from Lucy's tour. Choose the correct option.", "Olhe as frases do tour da Lucy. Escolha a opção correta.",
               "<b>There are</b> two armchairs in the living room. · <b>There's</b> a lamp next to the armchair.",
               [("We use <b>there is</b> with", "singular", "plural", " nouns.", True), ("We use <b>there are</b> with", "plural", "singular", " nouns.", False),
                ("The short answer is", "Yes, there is.", "Yes, there" + Q + "s.", "", True), ("\"Tem uma mesa\" in English is", "There" + Q + "s a table.", "Have a table.", "", False)],
               "Complete with there's, there are or is there.", "Complete com there's, there are ou is there.", c,
               """<ol><li>A: show your own room on camera and describe it: <i>There's a lamp on my desk. There are books behind me.</i> <i>any</i> with plural negatives and questions: present it, don't drill it hard.</li>
<li>B: the student checks the rules. C: then the student describes their own home.</li></ol>""", 28)


@unit(15)
def u15(b):
    A = b.A
    rows = [("<b>in</b> + room / area", "I'm <b>in</b> Room 504. · The gym is <b>in</b> the basement.", "no quarto 504 · no subsolo"), ("<b>on</b> + floor", "My room is <b>on</b> the fifth floor.", "no quinto andar"),
            ("<b>at</b> + point", "The stairs are <b>at</b> the end of the corridor. · Coffee is free <b>at</b> reception.", "no fim do corredor · na recepção"),
            ("upstairs / downstairs", "The bar is <b>upstairs</b>. · The gym is <b>downstairs</b>.", "lá em cima / lá embaixo"), ("through · outside", "Go <b>through</b> those doors. · Leave the bag <b>outside</b> your door.", "pelas portas · do lado de fora")]
    t = '<table style="table-layout:fixed;font-size:9pt"><tr><th style="width:34mm"></th><th>Example</th><th style="width:40mm">Em português</th></tr>' + "".join(f"<tr><td>{a}</td><td>{e}</td><td>{p}</td></tr>" for a, e, p in rows) + "</table>"
    bx = box("QUESTIONS", "<b>Where's</b> the gym? → <b>It's</b> downstairs. · <b>Where are</b> the stairs? → <b>They're</b> next to the elevator. · <b>Is there</b> a pool? → No, there isn't. (Unit 14)")
    c = f"""<ol><li>The pool is {A("on", "min-width:12mm")} the top floor.</li><li>The gym is {A("in", "min-width:12mm")} the basement.</li><li>Meet me {A("at", "min-width:12mm")} reception at nine.</li></ol>"""
    return std(b, "Language focus: where is it?", "Grammar table", "Tabela de gramática", t, bx,
               "Look at the sentences from Ana's check-in. Choose the correct option.", "Olhe as frases do check-in da Ana. Escolha a opção correta.",
               "You're <u>in</u> Room 504, <u>on</u> the fifth floor. · The elevator is <u>at</u> the end of the corridor, <u>through</u> those doors.",
               [("Use", "in", "on", " with rooms: <i>in Room 504</i>.", True), ("Use", "on", "in", " with floors: <i>on the fifth floor</i>.", False),
                ("Use", "at", "on", " with a point / place: <i>at the end of the corridor, at reception</i>.", True)],
               "Complete with in, on or at.", "Complete com in, on ou at.", c,
               """<ol><li>A: rule of thumb: <b>in</b> = inside a space, <b>on</b> = a floor/level, <b>at</b> = a specific point. Prepositions don't translate 1:1, so teach them as chunks: <i>on the fifth floor</i>.</li>
<li><b>through</b> /θruː/: one syllable; the spelling is strange. Drill it.</li></ol>""", 26)


@unit(16)
def u16(b):
    A = b.A
    rows = [("short (1 syllable)", "+ <b>-er</b>", "fast → fast<b>er</b> · slow → slow<b>er</b>"), ("ends in <b>-e</b>", "+ <b>-r</b>", "nice → nice<b>r</b> · large → large<b>r</b>"),
            ("vowel + consonant (big, hot)", "double the consonant + <b>-er</b>", "big → bi<b>gger</b> · hot → ho<b>tter</b>"), ("ends in <b>-y</b>", "<b>-y → -ier</b>", "heavy → heav<b>ier</b> · funny → funn<b>ier</b>"),
            ("long (2+ syllables)", "<b>more</b> + adjective", "<b>more</b> dangerous · <b>more</b> intelligent"), ("irregular", "new word", "good → <b>better</b> · bad → <b>worse</b> · far → <b>farther</b>")]
    t = '<table style="table-layout:fixed;font-size:9pt"><tr><th>Adjective</th><th>Rule</th><th>Examples</th></tr>' + "".join(f"<tr><td>{a}</td><td>{r}</td><td>{e}</td></tr>" for a, r, e in rows) + "</table>"
    bx = box("THE FORMULA", "A <b>is / are</b> + comparative + <b>than</b> + B → <i>The desert <b>is</b> hotter <b>than</b> the forest.</i>")
    c = f"""<ol><li>A horse is {A("bigger than", "min-width:24mm")} a dog. (big)</li><li>Sharks are {A("more dangerous than", "min-width:34mm")} dolphins. (dangerous)</li><li>My cat is {A("better than", "min-width:24mm")} your cat! (good)</li></ol>"""
    return std(b, "Language focus: comparatives", "Grammar table", "Tabela de gramática", t, bx,
               "Look at the sentences from Tom's quiz. Choose the correct option.", "Olhe as frases do quiz do Tom. Escolha a opção correta.",
               "Camels are <u>faster than</u> elephants. · Tigers are <u>heavier than</u> lions. · Snakes are <u>more dangerous than</u> sharks. · Dolphins have a <u>better</u> memory.",
               [("After a comparative, we use", "than", "that", ".", True), ("For short adjectives (fast, big), we add", "-er", "more", ".", False),
                ("For long adjectives (dangerous), we use", "more", "-er", ".", True), ("The comparative of <i>good</i> is", "better", "gooder", ".", False)],
               "Complete with the comparative.", "Complete com o comparativo.", c,
               """<ol><li>A: common A1 problem: no verb (<i>Camels faster than…</i>) or no <i>than</i>. Use the formula box.</li>
<li><i>interesting</i> /ˈɪntrəstɪŋ/ has 3 syllables, so: <i>more interesting</i>. C: then compare two cities the student knows.</li></ol>""", 24)


@unit(17)
def u17(b):
    A = b.A
    rows = [("short: small, cheap", "smaller, cheaper", "<b>the</b> small<b>est</b>, <b>the</b> cheap<b>est</b>"), ("ends in -e: safe, nice", "safer, nicer", "<b>the</b> saf<b>est</b>, <b>the</b> nic<b>est</b>"),
            ("vowel + consonant: big, hot", "bigger, hotter", "<b>the</b> bigg<b>est</b>, <b>the</b> hott<b>est</b>"), ("ends in -y: pretty, easy", "prettier, easier", "<b>the</b> pretti<b>est</b>, <b>the</b> easi<b>est</b>"),
            ("long: expensive, beautiful", "more expensive", "<b>the most</b> expensive, <b>the most</b> beautiful"), ("irregular: good, bad, far", "better, worse, farther", "<b>the best</b>, <b>the worst</b>, <b>the farthest</b>")]
    t = '<table style="table-layout:fixed;font-size:9pt"><tr><th>Adjective</th><th>Comparative</th><th>Superlative</th></tr>' + "".join(f"<tr><td>{a}</td><td>{c}</td><td>{s}</td></tr>" for a, c, s in rows) + "</table>"
    bx = box("USEFUL CHUNKS", "<b>in the world</b> · <b>in Brazil</b> · <b>in my city</b> &nbsp;|&nbsp; <b>one of the</b> + superlative + plural: <i>one of the safest countries</i>")
    c = f"""<ol><li>Brazil is {A("the biggest", "min-width:24mm")} country in South America. (big)</li><li>It's {A("the most beautiful", "min-width:34mm")} beach in my city. (beautiful)</li><li>This is {A("the best", "min-width:20mm")} restaurant in town. (good)</li></ol>"""
    return std(b, "Language focus: superlatives", "Grammar table: comparative (Unit 16) and superlative", "Tabela de gramática: comparativo (Unit 16) e superlativo", t, bx,
               "Look at the sentences from the podcast. Choose the correct option.", "Olhe as frases do podcast. Escolha a opção correta.",
               "It's one of <u>the safest</u> countries in the world. · Switzerland is <u>the most expensive</u> country. · The Vatican is <u>the smallest</u> country in the world. · It has <u>the best</u> food!",
               [("To compare three or more things, we use", "the", "a", ".", True), ("Short adjectives (small) take", "-est", "most", ".", False),
                ("Long adjectives (expensive) take", "the most", "the more", ".", True), ("We say the best", "in the world", "of the world", ".", False)],
               "Complete with the superlative.", "Complete com o superlativo.", c,
               """<ol><li>A: review Unit 16 quickly: ask for the comparative first, then the superlative (<i>small → smaller → the smallest</i>).</li>
<li><i>one of the</i> + plural noun is very useful and very natural: <i>one of the best restaurants</i>. C: then the student talks about their city.</li></ol>""", 24)


@unit(19)
def u19(b):
    A = b.A
    t = ('<table style="table-layout:fixed"><tr><th style="width:18mm"></th><th>I</th><th>he / she / it</th><th>you / we / they</th></tr>'
         "<tr><td><b>+</b></td><td>I<b>'m working</b>.</td><td>It<b>'s raining</b>.</td><td>They<b>'re walking</b>.</td></tr>"
         "<tr><td><b>–</b></td><td>I<b>'m not working</b>.</td><td>It <b>isn't raining</b>.</td><td>They <b>aren't walking</b>.</td></tr>"
         "<tr><td><b>?</b></td><td><b>Am</b> I <b>working</b>?</td><td><b>Is</b> it <b>raining</b>?</td><td><b>Are</b> they <b>walking</b>?</td></tr>"
         "<tr><td><b>Short</b></td><td>Yes, I am. / No, I'm not.</td><td>Yes, it is. / No, it isn't.</td><td>Yes, they are. / No, they aren't.</td></tr></table>")
    bx = ('<div class="two">' + box("WHEN?", "We use the present continuous for actions <b>now</b>, at this moment: <i>right now, at the moment, today, look!</i>")
          + box("SPELLING: -ING", "rain → rain<b>ing</b> · shin<s>e</s> → shin<b>ing</b>, wear → wear<b>ing</b> · sit → si<b>tting</b>, swim → swi<b>mming</b> (vowel + consonant: double it)") + "</div>")
    c = f"""<ol><li>Look! It {A("'s snowing", "min-width:22mm")}. (snow)</li><li>{A("Are", "min-width:12mm")} you {A("watching", "min-width:18mm")} TV right now? (watch)</li><li>We {A("aren't working", "min-width:24mm")} today. (not work)</li></ol>"""
    return std(b, "Language focus: present continuous", "Grammar table", "", t, bx,
               "Look at the sentences from the call. Choose the correct option.", "",
               "I'<u>m sitting</u> in my garden. · The sun <u>is shining</u>. · <u>Are</u> people <u>walking</u> in the snow? Yes, they <u>are</u>. · They'<u>re wearing</u> big coats.",
               [("For the present continuous, we use", "be + verb-ing", "verb-ing only", ".", True), ("In questions, <i>be</i> goes", "before the subject", "after the subject", ".", False),
                ("In short answers, we", "don" + Q + "t say the -ing verb", "say the -ing verb", ".", True), ("For the weather, the subject is", "it", "he", ".", False),
                ("<i>shine</i> + -ing =", "shining", "shineing", ".", True)],
               "Complete with the present continuous.", "", c,
               """<ol><li>A: the student knows both parts already: <i>be</i> (Unit 1) and verb-ing (Unit 8). Present continuous = the two together.</li>
<li>Contrast with the present simple (Unit 6): <i>It usually rains in December</i> (normally) vs <i>It's raining now</i> (at this moment).</li></ol>""", 22)


@unit(20)
def u20(b):
    A, sub = b.A, b.sub
    qs = [("What", "are", "you", "doing?"), ("Where", "is", "Marcos", "swimming?"), ("Why", "are", "they", "buying souvenirs?"), ("What", "is", "Leo", "eating?")]
    qt = '<table style="table-layout:fixed;font-size:9pt"><tr><th>question word</th><th>be</th><th>subject</th><th>verb + -ing</th></tr>' + "".join(f"<tr><td><b>{a}</b></td><td>{c}</td><td>{d}</td><td>{e}</td></tr>" for a, c, d, e in qs) + "</table>"
    nt = ('<table style="table-layout:fixed;font-size:9pt;margin-top:1mm"><tr><th>Present continuous: NOW</th><th>Present simple: ALWAYS / USUALLY</th></tr>'
          '<tr><td>right now · at the moment · today · look!</td><td>always · usually · every day · on vacation</td></tr>'
          '<tr><td><i>Marcos <b>is swimming</b> now.</i></td><td><i>Marcos <b>swims</b> every morning.</i></td></tr></table>')
    sv = box("STATE VERBS: NO -ING!", "Some verbs are about feelings and thoughts, not actions. We don't use them in the continuous form: <b>like · love · hate · prefer · want · know · need</b><br>"
             "<i>I want ice cream.</i> (not <s>I'm wanting</s>) · <i>Leo loves chocolate.</i> (not <s>is loving</s>) · <i>I know!</i> (not <s>I'm knowing</s>)")
    body = f"""{b.sec(3, "Language focus: questions, now or always?", "10 min")}
{sub("A", "Study the questions from the call and the table.", "4 min")}
{qt}{nt}{sv}
{sub("B", "Now or always? Choose.", "3 min")}
<ol><li>Paulo <b>is taking</b> photos now. → present continuous = {b.R("<u>at this moment</u>") if b.T else "always / every day / at this moment"}{"" if not b.T else ""}</li>
<li>Paulo <b>takes</b> a lot of photos. It's his job. → present simple = {b.R("<u>always / every day</u>") if b.T else "always / every day / at this moment"}</li></ol>
{sub("C", "Correct the mistakes.", "3 min")}
<ol><li>I'm wanting a coffee. → {A("I want a coffee.", "min-width:40mm")}</li><li>Where you are going? → {A("Where are you going?", "min-width:40mm")}</li><li>She is knowing the answer. → {A("She knows the answer.", "min-width:40mm")}</li></ol>"""
    notes = """<ol><li>A: the question order is the same as yes/no questions (Unit 19) + a question word at the start. <i>I'm loving it</i> is a famous slogan, but it's informal and special. At A1: <i>I love it.</i></li>
<li>B: contrast with the student's life: <i>What do you do every Saturday? What are you doing now?</i> C: state verbs and question order.</li></ol>"""
    return body, 28, notes
