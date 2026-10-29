# Speak! grammar reference pages (extra SB/TB page at the end of a unit): page(b) adds the page to a Book.

_TIMELINE = """<svg viewBox="0 0 520 70" width="100%" height="17mm" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<line x1="20" y1="38" x2="500" y2="38" stroke="#77acb5" stroke-width="2"/>
<polygon points="500,38 490,33 490,43" fill="#77acb5"/>
<text x="20" y="62" font-size="11" fill="#7d858a">PAST</text><text x="440" y="62" font-size="11" fill="#7d858a">NOW</text>
<line x1="450" y1="22" x2="450" y2="54" stroke="#176074" stroke-width="2"/>
<circle cx="230" cy="38" r="7" fill="#176074"/><text x="200" y="18" font-size="11" fill="#176074" font-weight="700">action / experience</text>
<path d="M237 32 Q340 0 446 30" fill="none" stroke="#cbbca0" stroke-width="2.5" stroke-dasharray="5 4"/>
<text x="300" y="62" font-size="11" fill="#9a7b4f" font-weight="700">connection to now</text></svg>"""


def present_perfect(b):
    """One-page reference for the present perfect at A2 (units 07-09)."""
    b.page(f"""{b.sec("+", "Grammar reference: the present perfect", "")}
<div class="box" style="margin-top:0"><h4>WHAT IS IT?</h4>The present perfect is a <b>bridge between the past and now</b>. Something happened in the past, but we are thinking about it <b>now</b>: the result is important now, or it's part of our life experience. We don't say <i>when</i> it happened.
{_TIMELINE}</div>
<h4 style="color:#0f4a5a;margin:1.5mm 0 .5mm">1. FORM: have / has + past participle</h4>
<table style="table-layout:fixed;margin-top:0;font-size:8.8pt"><tr><th style="width:24mm"></th><th>I / you / we / they</th><th>he / she / it</th></tr>
<tr><td><b>positive</b></td><td>I <b>have</b> (I<b>'ve</b>) cut my finger.</td><td>She <b>has</b> (she<b>'s</b>) cut her finger.</td></tr>
<tr><td><b>negative</b></td><td>I <b>haven't</b> been to Florida.</td><td>He <b>hasn't</b> been to Florida.</td></tr>
<tr><td><b>question</b></td><td><b>Have</b> you ever ridden a horse?</td><td><b>Has</b> she ever ridden a horse?</td></tr>
<tr><td><b>short answers</b></td><td>Yes, I <b>have</b>. / No, I <b>haven't</b>.</td><td>Yes, she <b>has</b>. / No, she <b>hasn't</b>.</td></tr></table>
<p class="small" style="margin:.8mm 0"><b>Past participle:</b> regular verbs = <b>-ed</b>, like the past (climb → climbed → climbed). Irregular verbs have a third form: go → went → <b>gone</b> · see → saw → <b>seen</b> · do → did → <b>done</b> · break → broke → <b>broken</b>. Learn the three forms together!</p>
<h4 style="color:#0f4a5a;margin:1.5mm 0 .5mm">2. TWO USES AT THIS LEVEL</h4>
<div class="two"><div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.8pt"><b>A. Recent news with a result now</b> (Unit 07)<br>with <b>just</b> = a short time ago<br><i>I've just cut my finger.</i> (it's bleeding now)<br><i>She's just fallen off her bike.</i><br><i>What's happened?</i></div>
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.8pt"><b>B. Life experiences</b> (Unit 08)<br>with <b>ever</b> (questions), <b>never</b>, <b>before</b>, <b>twice</b>, <b>many times</b><br><i>Have you ever swum with manatees?</i><br><i>I've never camped. I've been to Orlando twice.</i></div></div>
<h4 style="color:#0f4a5a;margin:1.5mm 0 .5mm">3. PRESENT PERFECT OR PAST SIMPLE?</h4>
<table style="table-layout:fixed;margin-top:0;font-size:8.8pt"><tr><th>present perfect: no finished time</th><th>past simple: a finished time</th></tr>
<tr><td>ever · never · just · before · twice · many times</td><td>yesterday · last year · in 2023 · two days ago · when I was twenty</td></tr>
<tr><td><i>I've ridden a horse.</i> (sometime in my life)</td><td><i>I rode a horse in Minas last summer.</i> (when? last summer)</td></tr></table>
<p class="small" style="margin:.8mm 0">A typical conversation <b>starts</b> with the present perfect and <b>continues</b> with the past simple: <i>Have you ever been to New York? — Yes, I have. — When did you go? — I went in 2022. It was amazing!</i></p>
<div class="two"><div class="box sand" style="margin-top:1mm"><h4>BEEN OR GONE?</h4><i>Carol has <b>been</b> to Miami.</i> (she went and came back)<br><i>Carol has <b>gone</b> to Miami.</i> (she's in Miami now)</div>
<div class="box sand" style="margin-top:1mm"><h4>DON'T SAY</h4><s>I have been in Florida last year.</s> → I <b>went</b> to Florida last year.<br><s>Have you ever went…?</s> → been · <s>Yes, I did.</s> → Yes, I <b>have</b>.</div></div>""",
    16, """<p>Use this page whenever the student hesitates between the present perfect and the past simple. Draw the timeline: the dot is the action, the dotted line connects it to now. The next units add more uses (<i>for / since, already / yet</i>). In American English the past simple is common with <i>just</i> (<i>I just ate</i>); both are correct.</p>""")
