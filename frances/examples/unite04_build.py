# Speak! Essentiel A1 - Unité 04 "J'aime le tennis" (tout en français, pour vrais débutants) - built with the shared engine + French layer
# Plan (Édito A1 unité 1, Alter Ego 1 dossiers 2-3): likes and hobbies; definite articles le, la, l', les; aimer / adorer / détester + noun.
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_fr import *
setup(band="A1 · UNITÉ 04", audio_json=os.path.join(HERE, "audio_fr-a1-unite-04.json"), img_dir=os.path.join(HERE, "img"), lang="fr-FR")

PHOTOS = [('A', 'le football', 'football'), ('B', 'le tennis', 'tennis'), ('C', 'le café', 'café'), ('D', "l'opéra", 'opéra'),
          ('E', 'le cinéma', 'cinéma'), ('F', 'les voyages', 'voyages'), ('G', 'la danse', 'danse'), ('H', 'la musique', 'musique')]

SCRIPT = [("Narratrice", "Dialogue un."), ("Thomas", "Camila, tu aimes le football ?"),
          ("Camila", "Non, je n'aime pas le football. J'adore le tennis !"), ("Thomas", "Le tennis ? Super ! J'aime le tennis."),
          ("Narratrice", "Dialogue deux."), ("Hugo", "Tu aimes le cinéma, Camila ?"), ("Camila", "Oui, j'aime le cinéma. Et toi ?"),
          ("Hugo", "J'adore le cinéma ! Mais je déteste les films d'horreur."),
          ("Narratrice", "Dialogue trois."), ("Madame Lefèvre", "Camila, vous aimez l'opéra ?"),
          ("Camila", "Euh … non, madame, je n'aime pas l'opéra."), ("Madame Lefèvre", "Ah ! Moi, j'adore l'opéra !")]
S042 = [p[1] for p in PHOTOS]
S043 = ["J'adore le tennis.", "J'aime le cinéma.", "Je n'aime pas le football.", "Je déteste les films d'horreur.", "Tu aimes la musique ?", "Vous aimez l'opéra ?"]
SCALE = [("♥♥", "J'adore"), ("♥", "J'aime"), ("✗", "Je n'aime pas"), ("✗✗", "Je déteste")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "NIVEAU A1 · UNITÉ 04", "J'aime le tennis", "Parler de ses goûts et de ses loisirs",
                       [("VOUS POUVEZ", "dire ce que vous aimez et ce que vous n'aimez pas, et poser la question"),
                        ("LANGUE", "le, la, l', les · j'aime, tu aimes, il / elle aime, vous aimez · j'adore, je déteste"),
                        ("PRONONCIATION", "le / les · l', n' · j'aime, vous aimez")])
    rows = "".join(f'<td style="width:25%;text-align:center"><b>{x}</b><br>♥♥ ☐ &nbsp;♥ ☐ &nbsp;✗ ☐ &nbsp;✗✗ ☐</td>' for x in ["le tennis", "la musique", "les voyages", "le café"])
    key = " &nbsp;·&nbsp; ".join(f"{s} = {w}" for s, w in SCALE)
    b.page(f"""{sec(1, "Échauffement : les loisirs", "8 min")}
{sub("A", "Écoutez et répétez. Écrivez.", "5 min", "04.2")}
<div class="bank">{" &nbsp;·&nbsp; ".join(sorted(S042, key=bank_key))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Et vous ? Cochez.", "3 min")}
<p class="small" style="margin:0 0 1mm">{key}</p>
<table class="ck"><tr>{rows}</tr></table>""",
    30, """<ol><li>A : piste 04.2. Montrez chaque photo et dites le mot <b>avec l'article</b> : l'élève répète et écrit le mot sous la photo. Révision de l'unité 03 : <i>Vous êtes brésilien(ne) ? Vous avez quel âge ?</i></li>
<li>B : mimez l'échelle (deux cœurs = <i>J'adore</i>, une croix = <i>Je n'aime pas</i>). L'élève coche, puis dit une phrase : <i>J'adore le café !</i> La règle complète est à la page 3.</li></ol>""", cover=cover)

    b.extra("Déroulement de la leçon · 55 min", """
<table><tr><th>Étape</th><th>Durée</th><th>Objectif</th><th>Page</th></tr>
<tr><td>1 Échauffement</td><td>8 min</td><td>8 loisirs avec photos · l'échelle des goûts</td><td>1</td></tr>
<tr><td>2 Écoute</td><td>10 min</td><td>Camila parle de ses goûts : trois petits dialogues</td><td>2</td></tr>
<tr><td>3 Grammaire</td><td>10 min</td><td><i>le, la, l', les</i> · <i>aimer</i> (singulier) · <i>adorer, détester</i></td><td>3–4</td></tr>
<tr><td>4 Labo de prononciation</td><td>5 min</td><td><i>le / les</i> · élision <i>l', n'</i> · phrases</td><td>4</td></tr>
<tr><td>5 Pratique</td><td>8 min</td><td>Articles, <i>aimer</i>, relier</td><td>5</td></tr>
<tr><td>6 Parler</td><td>12 min</td><td>Interview : vous aimez … ? · présenter ses goûts</td><td>6</td></tr>
<tr><td>7 Bilan</td><td>2 min</td><td>Auto-évaluation et devoirs</td><td>7</td></tr></table>
<div class="box"><h4>COMMENT UTILISER CE GUIDE</h4>Chaque page correspond à la page du livre de l'élève avec le même numéro. Vos notes sont dans l'<b>encadré jaune</b>.
<span class="red">Les réponses en rouge</span> ne sont pas dans le livre de l'élève. Les étiquettes <span class="time">5 min</span> indiquent la durée de chaque activité. Les transcriptions sont à la dernière page.</div>
<div class="box"><h4>TOUJOURS LENTEMENT</h4>Une seule mission : dire ses goûts. Trois nouveautés : les articles définis <i>le, la, l', les</i>, le verbe <i>aimer</i> au singulier (+ <i>vous aimez</i>) et l'échelle <i>j'adore / j'aime / je n'aime pas / je déteste</i>. La négation <i>ne … pas</i> de l'unité 03 revient avec l'élision : <i>je n'aime pas</i>.</div>
<div class="box sand"><h4>L'HISTOIRE</h4>Une semaine de Camila à Lyon. Au bureau, Thomas demande si elle aime le football : non, elle adore le tennis, comme lui. Dans l'immeuble, Hugo parle de cinéma : il adore le cinéma mais déteste les films d'horreur. Le soir, Madame Lefèvre adore l'opéra … Camila, pas du tout.</div>
<div class="box"><h4>LE PROBLÈME POUR LES BRÉSILIENS</h4><i>J'aime de café</i> ✗ (comme « gosto de café ») → <b>J'aime le café</b> : pas de <i>de</i>, mais toujours l'article. <i>Je ne aime pas</i> ✗ → <b>Je n'aime pas</b> ; <i>le opéra</i> ✗ → <b>l'opéra</b> (élision devant une voyelle). À l'oral, <i>le</i> [lə] et <i>les</i> [le] : c'est l'article qui dit si c'est un pluriel.</div>
<div class="box"><h4>AUDIO</h4>Piste 04.1 Trois dialogues (lent et naturel) · Piste 04.2 Les loisirs · Piste 04.3 J'aime, je n'aime pas</div>""")

    # Page 2
    gr = [("1", "Camila aime …", ["le football", "le tennis"], "le tennis"), ("2", "Hugo déteste …", ["le cinéma", "les films d'horreur"], "les films d'horreur"),
          ("3", "Madame Lefèvre adore …", ["l'opéra", "la danse"], "l'opéra")]
    wr = "".join(f'<td style="width:33%"><b>Dialogue {n}</b><br><span class="small">{p}</span><br>{ch(o, a)}</td>' for n, p, o, a in gr)
    gp = [("Camila, tu", "aimes", " le football ?"), ("Non, je n'aime pas le football. J'", "adore", " le tennis !"), ("Tu aimes", "le", " cinéma, Camila ?"),
          ("Mais je", "déteste", " les films d'horreur."), ("Camila, vous aimez", "l'", "opéra ?"), ("Non, madame, je", "n'aime", " pas l'opéra.")]
    gl = [f'<li value="{i+1}">{a} {A(x, "min-width:18mm")}{c}</li>' for i, (a, x, c) in enumerate(gp)]
    b.page(f"""{sec(2, "Écoute : tu aimes le football ?", "10 min")}
<p>Camila est à Lyon depuis une semaine. Elle parle avec Thomas, Hugo et Madame Lefèvre.</p>
{audiocard(["04.1 · SLOW", "04.1 · NATURAL"])}
{sub("A", "Écoutez. Choisissez.", "3 min", "04.1 · SLOW")}
<table class="ck"><tr>{wr}</tr></table>
{sub("B", "Écoutez encore. Complétez.", "5 min", "04.1 · NATURAL")}
<div class="bank">adore · aimes · déteste · l' · le · n'aime</div>
{twocol(gl, 3)}
{sub("C", "Lisez les dialogues avec l'enseignant.", "2 min")}""",
    30, """<ol><li>A : version <b>lente</b>, deux écoutes. Avant, montrez les photos B, E et D de la page 1 : le tennis, le cinéma, l'opéra.</li>
<li>B : version <b>naturelle</b>, pause après chaque dialogue. Faites remarquer l'article après <i>aimer</i> : <i>aimes <b>le</b> football</i>.</li>
<li>C : les dialogues sont à la dernière page. L'élève est Camila, puis on change.</li></ol>""")

    # Page 3 (explanation first: 3A explanation, 3B check, 3C practice)
    art = [("le", "masculin", "le tennis · le café"), ("la", "féminin", "la musique · la danse"), ("l'", "devant a, e, i, o, u, h", "l'opéra · l'art"), ("les", "pluriel", "les voyages · les films")]
    ta = "".join(f"<tr><td><b>{a}</b></td><td class='small'>{u}</td><td>{e}</td></tr>" for a, u, e in art)
    aim = [("j'", "aime"), ("tu", "aimes"), ("il / elle", "aime"), ("vous", "aimez")]
    tv = "".join(f"<tr><td>{p}</td><td><b>{v}</b></td></tr>" for p, v in aim)
    sc = " &nbsp;·&nbsp; ".join(f"{s} <b>{w}</b>" for s, w in SCALE)
    ck = [("J'aime", ["le", "la"], "la", "musique."), ("Tu aimes", ["le", "l'"], "l'", "opéra ?"), ("J'adore", ["le", "les"], "les", "voyages."),
          ("Je", ["n'aime pas", "ne aime pas"], "n'aime pas", "le football.")]
    ct = "".join(f'<td style="width:25%">{s}<br>{ch(o, a)} {e}</td>' for s, o, a, e in ck)
    b.page(f"""{sec(3, "Grammaire : le, la, l', les · aimer", "10 min")}
{sub("A", "Lisez.", "4 min")}
<div class="two"><div><table style="margin:0"><tr><th colspan="3">l'article</th></tr>{ta}</table></div>
<div><table style="margin:0"><tr><th colspan="2">aimer</th></tr>{tv}</table></div></div>
<div class="box"><h4>LA RÈGLE</h4>{sc}<br>Après <b>aimer, adorer, détester</b> → toujours l'article : J'aime <b>le</b> café. (pas : <i>J'aime de café.</i>) &nbsp;·&nbsp; <b>ne</b> devient <b>n'</b> devant une voyelle : Je <b>n'</b>aime pas l'opéra.</div>
{sub("B", "Choisissez.", "3 min")}
<table class="ck"><tr>{ct}</tr></table>
{sub("C", "Et vous ? Écrivez.", "3 min")}
<p style="line-height:2.2">♥♥ J'adore {A("…", "min-width:45mm")} . &nbsp; ♥ J'aime {A("…", "min-width:45mm")} .<br>✗ Je n'aime pas {A("…", "min-width:40mm")} . &nbsp; ✗✗ Je déteste {A("…", "min-width:40mm")} .</p>""",
    30, """<ol><li>A : lisez les deux tableaux avec l'élève. <i>j'aime, tu aimes, il aime</i> : même son [ɛm] ; <i>vous aimez</i> : son différent. L'échelle des goûts est dans l'encadré.</li>
<li>B : l'élève lit la phrase complète à voix haute.</li>
<li>C : phrases personnelles avec l'article ; l'élève les dit ensuite à voix haute.</li></ol>""")

    # Page 4
    b.page(f"""{sub("D", "Erreurs fréquentes", "2 min")}
<div class="box sand"><h4>ATTENTION : ERREURS FRÉQUENTES</h4>
<table style="margin:0"><tr><th>Ne dites pas</th><th>Dites</th></tr>
<tr><td>J'aime de café.</td><td><b>J'aime le café.</b></td></tr>
<tr><td>Je ne aime pas le football.</td><td><b>Je n'aime pas le football.</b></td></tr>
<tr><td>J'adore le opéra.</td><td><b>J'adore l'opéra.</b></td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Labo de prononciation", "5 min")}
{audiocard(["04.2", "04.3"])}
{sub("A", "Écoutez et répétez. Les loisirs.", "2 min", "04.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S042)}</div>
{sub("B", "Écoutez et répétez. Les phrases.", "3 min", "04.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S043)}</div>
<div class="box"><h4>LES SONS</h4><b>le</b> [lə] ≠ <b>les</b> [le] : <i>le voyage / les voyages</i> (même son pour <i>voyage</i> et <i>voyages</i> !) &nbsp;·&nbsp; <b>l'</b>, <b>n'</b>, <b>j'</b> : on ne prononce pas le <i>e</i> → <i>l'opéra, je n'aime pas, j'adore</i></div>""",
    36, """<ol><li>Erreurs : <i>J'aime de café</i> vient de « gosto de café ». <i>Je ne aime pas</i> et <i>le opéra</i> : en français, deux voyelles se rencontrent → élision.</li>
<li>4A : piste 04.2. Insistez sur <i>le</i> [lə] (bouche ronde) et <i>les</i> [le] (sourire). 4B : piste 04.3, chaque phrase deux fois, avec l'intonation montante pour les questions.</li></ol>""")

    # Page 5
    ar = [("tennis", "le"), ("musique", "la"), ("opéra", "l'"), ("voyages", "les"), ("cinéma", "le"), ("danse", "la"), ("art", "l'"), ("films", "les")]
    al = [f'<li value="{i+1}">{A(a, "min-width:12mm")} {w}</li>' for i, (w, a) in enumerate(ar)]
    gw = ["aime", "aimes", "aime", "aimez", "adore", "aime"]
    gs = [("J'", " le café."), ("Tu", " le cinéma ?"), ("Hugo", " le cinéma."), ("Vous", " l'opéra ?"), ("Madame Lefèvre", " l'opéra."), ("Je n'", " pas le football.")]
    gl5 = [f'<li value="{i+1}">{a} {A(gw[i], "min-width:16mm")}{c}</li>' for i, (a, c) in enumerate(gs)]
    mt = [("Tu aimes le football ?", "c", "Oui, j'adore l'opéra !"), ("Vous aimez l'opéra ?", "a", "Oui, j'aime le cinéma."),
          ("Tu aimes le cinéma ?", "b", "Non, je n'aime pas le football."), ("Tu aimes les voyages ?", "d", "Oui, j'adore les voyages !")]
    mr = "".join(f'<tr><td>{i+1}. {l} &nbsp;{A(k, "min-width:9mm")}</td><td>{chr(97+i)}) {r}</td></tr>' for i, (l, k, r) in enumerate(mt))
    b.page(f"""{sec(5, "Pratique", "8 min")}
{sub("A", "Complétez : le, la, l' ou les ?", "2 min")}
{twocol(al, 4)}
{sub("B", "Complétez avec aimer ou adorer.", "3 min")}
{twocol(gl5, 3)}
{sub("C", "Reliez.", "3 min")}
<table style="margin:0">{mr}</table>""",
    24, """<ol><li>A : <i>l'</i> devant une voyelle (<i>opéra, art</i>). Pour <i>la danse, la musique</i> : on apprend l'article avec le mot.</li>
<li>B : en 5, <i>adore</i> (Madame Lefèvre <i>adore</i> l'opéra) ; <i>aime</i> est aussi accepté. C : lisez les paires à voix haute.</li></ol>""")

    # Page 6
    items = ["le tennis", "la musique", "le cinéma", "la danse", "les voyages", "le café"]
    it = "".join(f'<tr><td>Vous aimez <b>{x}</b> ?</td><td style="text-align:center">♥♥ ☐</td><td style="text-align:center">♥ ☐</td><td style="text-align:center">✗ ☐</td><td style="text-align:center">✗✗ ☐</td></tr>' for x in items)
    b.page(f"""{sec(6, "Parler", "12 min")}
{sub("A", "Interview. Posez les questions à l'enseignant. Cochez.", "6 min")}
<table class="ck">{it}</table>
<div class="msg"><b>A :</b> Vous aimez le tennis ?<br><b>B :</b> Oui, j'adore le tennis ! Et vous ?<br><b>A :</b> Moi, je n'aime pas le tennis.</div>
{sub("B", "Parlez de vos goûts.", "6 min")}
<ol style="line-height:1.8"><li>Vous aimez le football ?</li><li>Vous aimez la musique brésilienne ?</li><li>Vous aimez les films d'horreur ?</li><li>Qu'est-ce que vous adorez ?</li></ol>""",
    28, """<ol><li>A : l'élève pose les six questions, l'enseignant répond avec des goûts variés, et l'élève coche. Puis on change : l'enseignant pose les questions avec <i>tu</i> (<i>Tu aimes … ?</i>).</li>
<li>B : réponses complètes avec l'article. Question 4 : <i>Qu'est-ce que …</i> est nouveau, montrez-le seulement comme formule ; l'élève répond <i>J'adore …</i>.</li></ol>""")

    # Page 7
    pc = [("Unité 02", "Je peux épeler mon nom et compter de 0 à 20."), ("Unité 03", "Je peux dire ma nationalité et mon âge."),
          ("Unité 04", "Je peux dire ce que j'aime et ce que je n'aime pas."), ("Unité 04", "Je peux utiliser le, la, l', les.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("musique", "la"), ("café", "le"), ("opéra", "l'"), ("voyages", "les")]
    hl = [f'<li value="{i+1}">{A(a, "min-width:12mm")} {w}</li>' for i, (w, a) in enumerate(hw)]
    b.page(f"""{sec(7, "Bilan et devoirs", "2 min")}
{sub("A", "Auto-évaluation", "1 min")}
<table class="ck"><tr><th style="width:19mm"></th><th>En français …</th><th style="width:18mm">Facile !</th><th style="width:18mm">Parfois</th><th style="width:18mm">Pas encore</th></tr>{pcr}</table>
{sub("B", "Devoirs", "1 min")}
<p><b>1. Complétez : le, la, l' ou les ?</b></p>
{twocol(hl, 2)}
<p style="margin-top:2mm"><b>2. Complétez le dialogue.</b></p>
<div class="msg"><b>Thomas :</b> Tu aimes le football ?<br><b>Vous :</b> {A("Oui, j'aime le football. / Non, je n'aime pas le football.", "min-width:75mm")}<br><b>Thomas :</b> Et le cinéma ?<br><b>Vous :</b> {A("J'adore le cinéma ! / …", "min-width:75mm")}</div>
<p style="margin-top:2mm"><b>3. Écrivez quatre phrases sur vos goûts.</b> J'adore … J'aime … Je n'aime pas … Je déteste …</p>
<div class="wline"></div><div class="wline"></div>""",
    22, """<p>Au prochain cours : l'élève lit ses quatre phrases (devoir 3) ; demandez <i>Et le football ? Et la danse ?</i> Dans l'unité 05 : les professions, <i>Qu'est-ce que vous faites ?</i></p>""")

    b.extra("Transcriptions", f"""
{sub("04.1", "Tu aimes le football ? (lent et naturel)")}
<p style="line-height:1.6">{"<br>".join(f"<b>{n} :</b> {t}" for n, t in SCRIPT)}</p>
{sub("04.2", "Les loisirs")}
<p>{" · ".join(S042)}</p>
{sub("04.3", "J'aime, je n'aime pas")}
<p>{" · ".join(S043)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essentiel 04 - J'aime le tennis")
