# Speak! Essentiel A1 - Unité 02 "Ça s'écrit comment ?" (tout en français, pour vrais débutants) - built with the shared engine + French layer
# Plan 2026-10-27 (Édito A1 unité 0, Alter Ego 1 dossier 0): alphabet, spelling, numbers 0-20, classroom phrases.
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_fr import *
setup(band="A1 · UNITÉ 02", audio_json=os.path.join(HERE, "audio_fr-a1-unite-02.json"), img_dir=os.path.join(HERE, "img"), lang="fr-FR")

PHOTOS = [("A", "Pardon ?", "pardon"), ("B", "Je ne comprends pas.", "je ne comprends pas"), ("C", "Vous pouvez répéter ?", "vous pouvez répéter"),
          ("D", "Plus lentement, s'il vous plaît.", "plus lentement"), ("E", "Ça s'écrit comment ?", "ça s'écrit comment"), ("F", "Merci !", "merci"),
          ("G", "D'accord !", "d'accord"), ("H", "Je ne sais pas.", "je ne sais pas")]

SCRIPT = [("Narratrice", "Dialogue un."), ("Madame Girard", "Bonjour, madame ! Vous vous appelez comment ?"), ("Camila", "Bonjour ! Je m'appelle Camila Souza."),
          ("Madame Girard", "Souza … Ça s'écrit comment ?"), ("Camila", "S – O – U – Z – A."), ("Madame Girard", "Merci. Et votre numéro de téléphone ?"),
          ("Camila", "06 12 15 08 20."), ("Madame Girard", "Pardon ? Vous pouvez répéter, s'il vous plaît ?"), ("Camila", "Zéro six … douze … quinze … zéro huit … vingt."),
          ("Madame Girard", "Merci, madame !"),
          ("Narratrice", "Dialogue deux."), ("Hugo", "Salut ! Je m'appelle Hugo. Appartement 16."), ("Camila", "Salut, Hugo ! Je suis Camila, appartement 14. Hugo … ça s'écrit comment ?"),
          ("Hugo", "H – U – G – O."), ("Camila", "Merci ! À bientôt, Hugo !"),
          ("Narratrice", "Dialogue trois."), ("Thomas", "Camila, le code wifi, c'est LYON19."), ("Camila", "Pardon ? Je ne comprends pas."),
          ("Thomas", "L – Y – O – N … dix-neuf."), ("Camila", "D'accord ! Merci, Thomas !")]
S022 = ["Pardon ?", "Je ne comprends pas.", "Vous pouvez répéter ?", "Plus lentement, s'il vous plaît.", "Ça s'écrit comment ?", "D'accord !", "Merci !", "Je ne sais pas."]
NUM = [(0, "zéro"), (1, "un"), (2, "deux"), (3, "trois"), (4, "quatre"), (5, "cinq"), (6, "six"), (7, "sept"), (8, "huit"), (9, "neuf"), (10, "dix"),
       (11, "onze"), (12, "douze"), (13, "treize"), (14, "quatorze"), (15, "quinze"), (16, "seize"), (17, "dix-sept"), (18, "dix-huit"), (19, "dix-neuf"), (20, "vingt")]
ABC = [("A", "a"), ("B", "bé"), ("C", "cé"), ("D", "dé"), ("E", "e"), ("F", "effe"), ("G", "gé"), ("H", "hache"), ("I", "i"), ("J", "ji"),
       ("K", "ka"), ("L", "elle"), ("M", "emme"), ("N", "enne"), ("O", "o"), ("P", "pé"), ("Q", "ku"), ("R", "erre"), ("S", "esse"), ("T", "té"),
       ("U", "u"), ("V", "vé"), ("W", "double vé"), ("X", "ixe"), ("Y", "i grec"), ("Z", "zède")]
HOT = {"E", "G", "H", "J", "R", "U", "W", "Y"}


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "NIVEAU A1 · UNITÉ 02", "Ça s'écrit comment ?", "L'alphabet, les nombres et les phrases de la classe",
                       [("VOUS POUVEZ", "épeler votre nom, dire un numéro de téléphone et demander de répéter"),
                        ("LANGUE", "Ça s'écrit comment ? · les nombres de 0 à 20 · Pardon ? Je ne comprends pas."),
                        ("PRONONCIATION", "l'alphabet · E, G, J, U · six / seize")])
    sit = [("L'enseignant parle vite.", ["Plus lentement, s'il vous plaît.", "Merci !"], "Plus lentement, s'il vous plaît."),
           ("Vous ne comprenez pas.", ["D'accord !", "Je ne comprends pas."], "Je ne comprends pas."),
           ("Un nom difficile : Lefèvre.", ["Ça s'écrit comment ?", "Je ne sais pas."], "Ça s'écrit comment ?")]
    sr = "".join(f'<td style="width:33%"><span class="small">{s}</span><br>{ch(o, a)}</td>' for s, o, a in sit)
    b.page(f"""{sec(1, "Échauffement : les phrases de la classe", "8 min")}
{sub("A", "Écoutez et répétez. Écrivez.", "5 min", "02.2")}
<div class="bank">{" &nbsp;·&nbsp; ".join(sorted(S022))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Qu'est-ce que vous dites ? Choisissez.", "3 min")}
<table class="ck"><tr>{sr}</tr></table>""",
    30, """<ol><li>A : piste 02.2. Montrez chaque photo et mimez la phrase (main derrière l'oreille = <b>Pardon ?</b>, geste lent de la main = <b>Plus lentement</b>, épaules levées = <b>Je ne sais pas</b>). Révision de l'unité 01 : commencez par <i>Bonjour ! Vous vous appelez comment ?</i></li>
<li>B : lisez chaque situation et mimez-la (parlez très vite, montrez un nom difficile). Ces phrases servent dans tous les cours : l'élève peut les utiliser à partir d'aujourd'hui.</li></ol>""", cover=cover)

    b.extra("Déroulement de la leçon · 55 min", """
<table><tr><th>Étape</th><th>Durée</th><th>Objectif</th><th>Page</th></tr>
<tr><td>1 Échauffement</td><td>8 min</td><td>8 phrases utiles de la classe avec photos</td><td>1</td></tr>
<tr><td>2 Écoute</td><td>10 min</td><td>Le deuxième jour de Camila : trois petits dialogues</td><td>2</td></tr>
<tr><td>3 Grammaire</td><td>10 min</td><td>Les nombres de 0 à 20 · <i>Ça s'écrit comment ?</i></td><td>3–4</td></tr>
<tr><td>4 Labo de prononciation</td><td>5 min</td><td>L'alphabet · épeler des noms</td><td>4</td></tr>
<tr><td>5 Pratique</td><td>8 min</td><td>Compléter, mettre en ordre, relier</td><td>5</td></tr>
<tr><td>6 Parler</td><td>12 min</td><td>À l'accueil : nom, épellation, téléphone</td><td>6</td></tr>
<tr><td>7 Bilan</td><td>2 min</td><td>Auto-évaluation et devoirs</td><td>7</td></tr></table>
<div class="box"><h4>COMMENT UTILISER CE GUIDE</h4>Chaque page correspond à la page du livre de l'élève avec le même numéro. Vos notes sont dans l'<b>encadré jaune</b>.
<span class="red">Les réponses en rouge</span> ne sont pas dans le livre de l'élève. Les étiquettes <span class="time">5 min</span> indiquent la durée de chaque activité. Les transcriptions sont à la dernière page.</div>
<div class="box"><h4>TOUJOURS LENTEMENT</h4>Trois nouveautés seulement : les phrases utiles de la classe (<i>Pardon ? Je ne comprends pas.</i>), les nombres de 0 à 20 et l'alphabet pour épeler. La grammaire de l'unité 01 (<i>Je m'appelle …</i>, <i>tu / vous</i>) revient dans chaque activité. Le verbe <i>être</i> complet arrive dans l'unité 03.</div>
<div class="box sand"><h4>L'HISTOIRE</h4>Le deuxième jour de Camila à Lyon. À l'agence, Madame Girard, de l'accueil, prépare son badge : Camila épelle <i>Souza</i> et donne son numéro de téléphone. Dans l'immeuble, elle rencontre Hugo, son voisin (appartement 16). Au bureau, Thomas lui donne le code wifi.</div>
<div class="box"><h4>LE PROBLÈME POUR LES BRÉSILIENS</h4><b>six</b> (6) ≠ « seis », <b>seize</b> (16) ≠ « seis » : attention ! <b>deux</b> (2) ≠ « dois », <b>douze</b> (12) ≠ « doze ». Pour l'alphabet : <b>G</b> = [ʒe] et <b>J</b> = [ʒi] (le contraire du portugais), <b>E</b> = [ə], <b>U</b> = [y]. Et en France, on dit le téléphone deux par deux : <i>06 12 15 08 20</i> = zéro six, douze, quinze …</div>
<div class="box"><h4>AUDIO</h4>Piste 02.1 Trois dialogues (lent et naturel) · Piste 02.2 Phrases utiles · Piste 02.3 Les nombres · Piste 02.4 L'alphabet</div>""")

    # Page 2
    gr = [("1", "Le téléphone de Camila", ["06 12 15 08 20", "06 02 05 08 12"], "06 12 15 08 20"), ("2", "L'appartement de Hugo", ["6", "16"], "16"),
          ("3", "Le code wifi", ["LYON19", "LYON9"], "LYON19")]
    wr = "".join(f'<td style="width:33%"><b>Dialogue {n}</b><br><span class="small">{p}</span><br>{ch(o, a)}</td>' for n, p, o, a in gr)
    gp = [("Souza … Ça", "s'écrit", " comment ?"), ("Vous pouvez", "répéter", ", s'il vous plaît ?"), ("Je suis Camila, appartement", "quatorze", "."),
          ("Pardon ? Je ne", "comprends", " pas."), ("", "D'accord", " ! Merci, Thomas !"), ("Merci ! À", "bientôt", ", Hugo !")]
    gl = [f'<li value="{i+1}">{a} {A(x, "min-width:20mm")}{c}</li>' for i, (a, x, c) in enumerate(gp)]
    b.page(f"""{sec(2, "Écoute : le deuxième jour de Camila", "10 min")}
<p>C'est le deuxième jour de Camila à Lyon. Elle parle avec Madame Girard, Hugo et Thomas.</p>
{audiocard(["02.1 · SLOW", "02.1 · NATURAL"])}
{sub("A", "Écoutez. Choisissez.", "3 min", "02.1 · SLOW")}
<table class="ck"><tr>{wr}</tr></table>
{sub("B", "Écoutez encore. Complétez.", "5 min", "02.1 · NATURAL")}
<div class="bank">bientôt · comprends · D'accord · quatorze · répéter · s'écrit</div>
{twocol(gl, 3)}
{sub("C", "Lisez les dialogues avec l'enseignant.", "2 min")}""",
    30, """<ol><li>A : version <b>lente</b>, deux écoutes. Avant, présentez les personnes : Madame Girard (accueil de l'agence), Hugo (voisin), Thomas (collègue, unité 01).</li>
<li>B : version <b>naturelle</b>, pause après chaque dialogue. Montrez que Camila épelle <i>Souza</i> lettre par lettre : l'alphabet est à la page 4.</li>
<li>C : les dialogues sont à la dernière page. L'élève est Camila, puis on change.</li></ol>""")

    # Page 3
    nt = "".join(f'<td style="width:14.28%;text-align:center;padding:1.2mm 0.5mm{";background:#f3ead8" if n in (2, 6, 12, 16) else ""}"><b style="font-size:12pt">{n}</b><br><span class="small">{w}</span></td>' + ("</tr><tr>" if (i + 1) % 7 == 0 and i < len(NUM) - 1 else "") for i, (n, w) in enumerate(NUM))
    lis = [("2", "12"), ("6", "16"), ("3", "13"), ("4", "14")]
    lr = "".join(f'<td style="width:25%;text-align:center">{ch(o, o[1] if i % 2 == 0 else o[0])}</td>' for i, o in enumerate(lis))
    wn = [(5, "cinq"), (11, "onze"), (17, "dix-sept"), (20, "vingt")]
    wl = "".join(f'<td style="width:25%;text-align:center"><b style="font-size:13pt">{n}</b><br>{A(w, "min-width:28mm")}</td>' for n, w in wn)
    b.page(f"""{sec(3, "Grammaire : les nombres de 0 à 20", "10 min")}
{audiocard(["02.3"])}
{sub("A", "Écoutez et répétez.", "4 min", "02.3")}
<table class="ck" style="table-layout:fixed"><tr>{nt}</tr></table>
<div class="box"><h4>ÇA S'ÉCRIT COMMENT ?</h4>– Ça s'écrit comment ? &nbsp;– <b>S – O – U – Z – A.</b> &nbsp;·&nbsp; – Votre numéro de téléphone ? &nbsp;– <b>06 12 15 08 20</b> (zéro six, douze, quinze, zéro huit, vingt)</div>
{sub("B", "Écoutez l'enseignant. Choisissez.", "3 min")}
<table class="ck"><tr>{lr}</tr></table>
{sub("C", "Écrivez le nombre en lettres.", "3 min")}
<table class="ck"><tr>{wl}</tr></table>""",
    32, """<ol><li>A : piste 02.3, deux fois. Les nombres en couleur sont difficiles pour les Brésiliens : <i>deux / douze</i>, <i>six / seize</i>. Montrez avec les doigts.</li>
<li>B : l'enseignant lit : <b>douze, six, treize, quatre</b>. L'élève choisit. Puis l'élève lit un nombre, l'enseignant choisit.</li>
<li>C : l'orthographe exacte n'est pas le plus important aujourd'hui ; acceptez les petites erreurs et corrigez ensemble.</li></ol>""")

    # Page 4
    abc = "".join(f'<td style="width:10%;text-align:center;padding:1.2mm 0.5mm{";background:#f3ead8" if l in HOT else ""}"><b style="font-size:12pt">{l}</b><br><span class="small">{n}</span></td>' + ("</tr><tr>" if (i + 1) % 10 == 0 and i < len(ABC) - 1 else "") for i, (l, n) in enumerate(ABC))
    names = ["Thomas", "Nadia", "Hugo", "Lyon", "Recife", "votre prénom"]
    b.page(f"""{sub("D", "Erreurs fréquentes", "2 min")}
<div class="box sand"><h4>ATTENTION : ERREURS FRÉQUENTES</h4>
<table style="margin:0"><tr><th>Ne dites pas</th><th>Dites</th></tr>
<tr><td>Comment s'écrit ?</td><td><b>Ça s'écrit comment ?</b></td></tr>
<tr><td>Je ne comprendre pas.</td><td><b>Je ne comprends pas.</b></td></tr>
<tr><td>seize = 6</td><td><b>six = 6 · seize = 16</b></td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Labo de prononciation : l'alphabet", "5 min")}
{audiocard(["02.4"])}
{sub("A", "Écoutez et répétez.", "3 min", "02.4")}
<table class="ck" style="table-layout:fixed"><tr>{abc}</tr></table>
<div class="box"><h4>DIFFÉRENT DU PORTUGAIS</h4>Les lettres en couleur : <b>E</b> [ə] &nbsp;·&nbsp; <b>G</b> [ʒe] &nbsp;·&nbsp; <b>H</b> [aʃ] &nbsp;·&nbsp; <b>J</b> [ʒi] &nbsp;·&nbsp; <b>R</b> [ɛʁ] &nbsp;·&nbsp; <b>U</b> [y] &nbsp;·&nbsp; <b>W</b> [dubləve] &nbsp;·&nbsp; <b>Y</b> [igʁɛk]</div>
{sub("B", "Épelez.", "2 min")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(names)}</div>""",
    36, """<ol><li>Erreurs : la question complète est <i>Ça s'écrit comment ?</i> (ou <i>Comment ça s'écrit ?</i>). Corrigez <i>seize = 6</i> avec les doigts.</li>
<li>4A : piste 02.4, deux fois. <b>G</b> = « jê », <b>J</b> = « ji » (le contraire du portugais) ; <b>U</b> : lèvres rondes, langue comme pour « i ». Le <b>h</b> est muet : <i>Hugo</i> = « ugo ».</li>
<li>4B : l'élève épelle, l'enseignant écrit. Puis on change. En cas de doute : <i>Pardon ? Vous pouvez répéter ?</i></li></ol>""")

    # Page 5
    seq = [("dix, onze,", "douze", ", treize"), ("cinq, six,", "sept", ", huit"), ("quinze,", "seize", ", dix-sept"), ("dix-huit, dix-neuf,", "vingt", ""),
           ("zéro, un,", "deux", ", trois"), ("huit,", "neuf", ", dix")]
    gl5 = [f'<li value="{i+1}">{a} {A(x, "min-width:16mm")}{c}</li>' for i, (a, x, c) in enumerate(seq)]
    od = [("s'écrit / ça / comment / ?", "Ça s'écrit comment ?"), ("répéter / pouvez / vous / ?", "Vous pouvez répéter ?"), ("comprends / je / pas / ne", "Je ne comprends pas.")]
    ol5 = "".join(f'<li>{s}<div class="wline">{R(a)}</div></li>' for s, a in od)
    mt = [("7", "c", "seize"), ("12", "d", "dix-neuf"), ("16", "a", "sept"), ("19", "b", "douze")]
    mr = "".join(f'<tr><td>{i+1}. <b>{l}</b> &nbsp;{A(k, "min-width:9mm")}</td><td>{chr(97+i)}) {r}</td></tr>' for i, (l, k, r) in enumerate(mt))
    b.page(f"""{sec(5, "Pratique", "8 min")}
{sub("A", "Complétez.", "3 min")}
{twocol(gl5, 3)}
{sub("B", "Mettez dans l'ordre.", "2 min")}
<ol>{ol5}</ol>
{sub("C", "Reliez.", "3 min")}
<table style="margin:0">{mr}</table>""",
    24, """<ol><li>A : l'élève lit la suite à voix haute et écrit le nombre qui manque.</li>
<li>B : ces trois phrases sont des « phrases de survie » : l'élève peut les dire dans tous les cours. C : lisez les nombres à voix haute après.</li></ol>""")

    # Page 6
    b.page(f"""{sec(6, "Parler", "12 min")}
{sub("A", "À l'accueil. Jouez avec l'enseignant.", "6 min")}
<div class="msg"><b>A :</b> Bonjour ! Vous vous appelez comment ?<br><b>B :</b> Je m'appelle …<br><b>A :</b> Ça s'écrit comment ?<br><b>B :</b> … – … – … – …<br><b>A :</b> Et votre numéro de téléphone ?<br><b>B :</b> 0 …  … … … …<br><b>A :</b> Merci !</div>
<div class="bank" style="background:#fff">Pardon ? · Vous pouvez répéter ? · Plus lentement, s'il vous plaît. · D'accord ! · Merci !</div>
{sub("B", "Écoutez et écrivez les noms.", "3 min")}
<ol style="line-height:2"><li>{A("GIRARD", "min-width:55mm")}</li><li>{A("DUBOIS", "min-width:55mm")}</li><li>{A("JOLY", "min-width:55mm")}</li></ol>
{sub("C", "Écoutez et écrivez les numéros.", "3 min")}
<ol style="line-height:2"><li>{A("06 14 03 19 11", "min-width:55mm")}</li><li>{A("07 20 16 02 13", "min-width:55mm")}</li></ol>""",
    30, """<ol><li>A : l'enseignant est Madame Girard, l'élève donne son vrai nom (ou un nom inventé) et un numéro (nombres de 0 à 20 seulement). Puis on change : l'élève est à l'accueil.</li>
<li>B : épelez lentement, deux fois : G-I-R-A-R-D, D-U-B-O-I-S, J-O-L-Y. C : dites les numéros deux par deux : <i>zéro six, quatorze, zéro trois, dix-neuf, onze</i> · <i>zéro sept, vingt, seize, zéro deux, treize</i>. L'élève doit utiliser <i>Pardon ? / Plus lentement, s'il vous plaît.</i></li></ol>""")

    # Page 7
    pc = [("Unité 01", "Je peux saluer et dire mon nom."), ("Unité 02", "Je peux épeler mon nom."),
          ("Unité 02", "Je peux compter de 0 à 20 et dire un numéro de téléphone."), ("Unité 02", "Je peux dire : Pardon ? Je ne comprends pas.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [(3, "trois"), (8, "huit"), (13, "treize"), (18, "dix-huit")]
    hl = [f'<li value="{i+1}"><b>{n}</b> {A(w, "min-width:32mm")}</li>' for i, (n, w) in enumerate(hw)]
    b.page(f"""{sec(7, "Bilan et devoirs", "2 min")}
{sub("A", "Auto-évaluation", "1 min")}
<table class="ck"><tr><th style="width:19mm"></th><th>En français …</th><th style="width:18mm">Facile !</th><th style="width:18mm">Parfois</th><th style="width:18mm">Pas encore</th></tr>{pcr}</table>
{sub("B", "Devoirs", "1 min")}
<p><b>1. Écrivez le nombre en lettres.</b></p>
{twocol(hl, 2)}
<p style="margin-top:2mm"><b>2. Complétez le dialogue.</b></p>
<div class="msg"><b>Madame Girard :</b> Bonjour ! Vous vous appelez comment ?<br><b>Vous :</b> {A("Je m'appelle …", "min-width:60mm")}<br><b>Madame Girard :</b> Ça s'écrit comment ?<br><b>Vous :</b> {A("(épellation)", "min-width:60mm")}<br><b>Madame Girard :</b> Merci !</div>
<p style="margin-top:2mm"><b>3. Écrivez votre prénom, votre nom et votre numéro de téléphone.</b> Épelez-les au prochain cours.</p>
<div class="wline"></div><div class="wline"></div>""",
    22, """<p>Au prochain cours : commencez par <i>Bonjour ! Ça s'écrit comment ?</i> L'élève épelle son nom et dit son numéro (devoir 3), l'enseignant écrit. Dans l'unité 03 : se présenter, la nationalité et l'âge, <i>Et vous ?</i></p>""")

    b.extra("Transcriptions", f"""
{sub("02.1", "Le deuxième jour de Camila (lent et naturel)")}
<p style="line-height:1.6">{"<br>".join(f"<b>{n} :</b> {t}" for n, t in SCRIPT)}</p>
{sub("02.2", "Phrases utiles")}
<p>{" · ".join(S022)}</p>
{sub("02.3", "Les nombres")}
<p>{" · ".join(f"{n} {w}" for n, w in NUM)}</p>
{sub("02.4", "L'alphabet")}
<p>{" · ".join(f"{l} ({n})" for l, n in ABC)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essentiel 02 - Ça s'écrit comment")
