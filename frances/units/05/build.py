# Speak! Essentiel A1 - Unité 05 "Qu'est-ce que vous faites ?" (tout en français, pour vrais débutants) - built with the shared engine + French layer
# Plan (Édito A1 unité 2, Alter Ego 1 dossiers 1-2): jobs, personal information; -er verbs in the présent; masculine/feminine of jobs; quel / quelle.
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_fr import *
setup(band="A1 · UNITÉ 05", audio_json=os.path.join(HERE, "audio_fr-a1-unite-05.json"), img_dir=os.path.join(HERE, "img"), lang="fr-FR")

PHOTOS = [('A', 'infirmier / infirmière', 'infirmier'), ('B', 'serveur / serveuse', 'serveur'), ('C', 'avocat(e)', 'avocat'), ('D', 'professeur(e)', 'professeur'),
          ('E', 'étudiant(e)', 'étudiant'), ('F', 'vendeur / vendeuse', 'vendeur'), ('G', 'graphiste', 'graphiste'), ('H', 'médecin', 'médecin')]

SCRIPT = [("Narratrice", "Dialogue un."), ("Homme", "Bonjour, madame ! Quel est votre nom ?"), ("Camila", "Souza. Camila Souza."),
          ("Homme", "Quelle est votre profession ?"), ("Camila", "Je suis graphiste."), ("Homme", "Vous travaillez où ?"),
          ("Camila", "Je travaille dans une agence, à Lyon."), ("Homme", "Et quel est votre numéro de téléphone ?"),
          ("Camila", "06 12 15 08 20."), ("Homme", "Merci, madame. Bienvenue au club !"),
          ("Narratrice", "Dialogue deux."), ("Sophie", "Salut ! Je m'appelle Sophie. Qu'est-ce que tu fais, Camila ?"),
          ("Camila", "Je suis graphiste. Et toi ?"), ("Sophie", "Moi, je suis médecin. Je travaille à l'hôpital."), ("Camila", "Médecin ! Super !"),
          ("Narratrice", "Dialogue trois."), ("Thomas", "Camila, Hugo est étudiant ? Il travaille ?"),
          ("Camila", "Oui, il est étudiant. Et il travaille dans un café, le week-end."), ("Thomas", "Dans le café de Nadia ?"), ("Camila", "Oui ! Il est serveur.")]
S052 = ["graphiste … graphiste", "médecin … médecin", "professeur … professeure", "serveur … serveuse", "vendeur … vendeuse",
        "étudiant … étudiante", "avocat … avocate", "infirmier … infirmière"]
S053 = ["Qu'est-ce que vous faites ?", "Je suis graphiste.", "Quelle est votre profession ?", "Quel est votre nom ?", "Vous travaillez où ?", "Je travaille dans une agence."]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "NIVEAU A1 · UNITÉ 05", "Qu'est-ce que vous faites ?", "Parler de sa profession",
                       [("VOUS POUVEZ", "dire votre profession et où vous travaillez, et remplir une fiche"),
                        ("LANGUE", "Je suis graphiste · serveur / serveuse · je travaille, vous travaillez · quel / quelle"),
                        ("PRONONCIATION", "masculin / féminin des professions · travaille")])
    me = "".join(f'<td style="width:33%" class="small">{q}<br>{A(a, "min-width:40mm")}</td>' for q, a in
                 [("Vous êtes …", "graphiste / étudiant(e) / …"), ("Le professeur est …", "professeur(e)"), ("Un ami / une amie est …", "médecin / …")])
    b.page(f"""{sec(1, "Échauffement : les professions", "8 min")}
{sub("A", "Écoutez et répétez. Écrivez.", "5 min", "05.2")}
<div class="bank">{" &nbsp;·&nbsp; ".join(sorted((p[1] for p in PHOTOS), key=bank_key))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Et vous ? Écrivez une profession.", "3 min")}
<table class="ck"><tr>{me}</tr></table>""",
    30, """<ol><li>A : piste 05.2. Montrez chaque photo : <i>Il est serveur. Elle est serveuse.</i> L'élève répète les deux formes et écrit le mot. Révision de l'unité 04 : <i>Vous aimez le cinéma ? Et le tennis ?</i></li>
<li>B : si la profession de l'élève n'est pas dans la liste, donnez le mot et écrivez-le avec lui. La règle du féminin est à la page 3.</li></ol>""", cover=cover)

    b.extra("Déroulement de la leçon · 55 min", """
<table><tr><th>Étape</th><th>Durée</th><th>Objectif</th><th>Page</th></tr>
<tr><td>1 Échauffement</td><td>8 min</td><td>8 professions avec photos (masculin / féminin)</td><td>1</td></tr>
<tr><td>2 Écoute</td><td>10 min</td><td>Camila au club de tennis : trois petits dialogues</td><td>2</td></tr>
<tr><td>3 Grammaire</td><td>10 min</td><td>Professions m / f · <i>travailler</i> · <i>quel / quelle</i></td><td>3–4</td></tr>
<tr><td>4 Labo de prononciation</td><td>5 min</td><td>Masculin / féminin · phrases utiles</td><td>4</td></tr>
<tr><td>5 Pratique</td><td>8 min</td><td>Féminin, <i>travailler</i>, relier</td><td>5</td></tr>
<tr><td>6 Parler</td><td>12 min</td><td>La fiche d'inscription · questions personnelles</td><td>6</td></tr>
<tr><td>7 Bilan</td><td>2 min</td><td>Auto-évaluation et devoirs</td><td>7</td></tr></table>
<div class="box"><h4>COMMENT UTILISER CE GUIDE</h4>Chaque page correspond à la page du livre de l'élève avec le même numéro. Vos notes sont dans l'<b>encadré jaune</b>.
<span class="red">Les réponses en rouge</span> ne sont pas dans le livre de l'élève. Les étiquettes <span class="time">5 min</span> indiquent la durée de chaque activité. Les transcriptions sont à la dernière page.</div>
<div class="box"><h4>TOUJOURS LENTEMENT</h4>Une seule mission : parler de sa profession. Trois nouveautés : les professions au masculin et au féminin (<i>Je suis graphiste</i>, sans article), le verbe <i>travailler</i> (même modèle que <i>aimer</i> de l'unité 04) et <i>quel / quelle</i> pour les questions d'une fiche. <i>Qu'est-ce que vous faites ?</i> est une formule : <i>faire</i> complet vient plus tard. Le numéro de téléphone de l'unité 02 revient.</div>
<div class="box sand"><h4>L'HISTOIRE</h4>Camila adore le tennis (unité 04) : elle s'inscrit dans un club de tennis à Lyon. À l'accueil, un homme remplit sa fiche : nom, profession, lieu de travail, téléphone. Au club, elle rencontre Sophie, médecin. Au bureau, Thomas demande si Hugo travaille : oui, il est serveur le week-end, au café de Nadia.</div>
<div class="box"><h4>LE PROBLÈME POUR LES BRÉSILIENS</h4><i>Quel est votre profession ?</i> ✗ → <b>Quelle est votre profession ?</b> : en portugais, « qual » ne change pas ; en français, <i>quel</i> (masculin) / <i>quelle</i> (féminin). <i>Je travaille en une agence</i> ✗ (« em ») → <b>dans une agence</b>. <i>Elle est serveur</i> ✗ → <b>serveuse</b>. Et après <i>Je suis</i>, pas d'article : <b>Je suis graphiste.</b></div>
<div class="box"><h4>AUDIO</h4>Piste 05.1 Trois dialogues (lent et naturel) · Piste 05.2 Les professions · Piste 05.3 Les phrases</div>""")

    # Page 2
    form = [("Nom", "Souza"), ("Prénom", "Camila"), ("Profession", "graphiste"), ("Lieu de travail", "une agence, à Lyon"), ("Téléphone", "06 12 15 08 20")]
    ft = "".join(f'<tr><td style="width:35%"><b>{k}</b></td><td>{A(v, "min-width:50mm")}</td></tr>' for k, v in form)
    gp = [("", "Quelle", " est votre profession ?"), ("Je", "travaille", " dans une agence, à Lyon."), ("Moi, je suis", "médecin", "."),
          ("Je travaille à", "l'hôpital", "."), ("Hugo est étudiant ? Il", "travaille", " ?"), ("Oui ! Il est", "serveur", ".")]
    gl = [f'<li value="{i+1}">{a} {A(x, "min-width:18mm")}{c}</li>' for i, (a, x, c) in enumerate(gp)]
    b.page(f"""{sec(2, "Écoute : au club de tennis", "10 min")}
<p>Camila adore le tennis. Elle va au club de tennis de Lyon.</p>
{audiocard(["05.1 · SLOW", "05.1 · NATURAL"])}
{sub("A", "Écoutez le dialogue 1. Complétez la fiche.", "3 min", "05.1 · SLOW")}
<table class="ck" style="width:75%">{ft}</table>
{sub("B", "Écoutez encore. Complétez.", "5 min", "05.1 · NATURAL")}
<div class="bank">l'hôpital · médecin · Quelle · serveur · travaille · travaille</div>
{twocol(gl, 3)}
{sub("C", "Lisez les dialogues avec l'enseignant.", "2 min")}""",
    30, """<ol><li>A : version <b>lente</b>, dialogue 1 deux fois. Le numéro de téléphone est celui de l'unité 02 : l'élève peut vérifier.</li>
<li>B : version <b>naturelle</b>, les trois dialogues. Nouveaux : Sophie (médecin, au club) et l'homme de l'accueil.</li>
<li>C : les dialogues sont à la dernière page. L'élève est Camila, puis on change.</li></ol>""")

    # Page 3 (explanation first: 3A explanation, 3B check, 3C practice)
    mf = [("=", "graphiste · médecin", "graphiste · médecin"), ("+ e", "étudiant · avocat", "étudiant<b>e</b> · avocat<b>e</b>"),
          ("-eur → -euse", "serveur · vendeur", "serv<b>euse</b> · vend<b>euse</b>"), ("-ier → -ière", "infirmier", "infirm<b>ière</b>")]
    tm = "".join(f"<tr><td class='small'>{r}</td><td>{m}</td><td>{f}</td></tr>" for r, m, f in mf)
    tr = [("je", "travaille"), ("tu", "travailles"), ("il / elle", "travaille"), ("vous", "travaillez")]
    tv = "".join(f"<tr><td>{p}</td><td><b>{v}</b></td></tr>" for p, v in tr)
    ck = [("Elle est", ["serveur", "serveuse"], "serveuse", ""), ("Je suis", ["graphiste", "une graphiste"], "graphiste", ""),
          ("", ["Quel", "Quelle"], "Quelle", "est votre profession ?"), ("Vous", ["travaillez", "travaille"], "travaillez", "où ?")]
    ct = "".join(f'<td style="width:25%">{s}<br>{ch(o, a)} {e}</td>' for s, o, a, e in ck)
    b.page(f"""{sec(3, "Grammaire : les professions · travailler · quel / quelle", "10 min")}
{sub("A", "Lisez.", "4 min")}
<div class="two"><div><table style="margin:0"><tr><th></th><th>homme</th><th>femme</th></tr>{tm}</table></div>
<div><table style="margin:0"><tr><th colspan="2">travailler (comme aimer)</th></tr>{tv}</table></div></div>
<div class="box"><h4>LA RÈGLE</h4>Profession sans article : Je suis <b>graphiste</b>. Il est <b>serveur</b>. &nbsp;·&nbsp; <b>quel</b> + nom masculin : <b>Quel</b> est votre nom ? / votre numéro ? &nbsp;·&nbsp; <b>quelle</b> + nom féminin : <b>Quelle</b> est votre profession ? &nbsp;·&nbsp; Travailler <b>dans</b> une agence, <b>à</b> l'hôpital, <b>à</b> Lyon.</div>
{sub("B", "Choisissez.", "3 min")}
<table class="ck"><tr>{ct}</tr></table>
{sub("C", "Et vous ? Écrivez.", "3 min")}
<p style="line-height:2.2">Je suis {A("…", "min-width:50mm")} . &nbsp; Je travaille {A("dans … / à …", "min-width:55mm")} .</p>""",
    30, """<ol><li>A : lisez les tableaux avec l'élève. <i>travailler</i> fonctionne comme <i>aimer</i> (unité 04) : <i>je travaille, tu travailles, il travaille</i> = même son. <i>quel / quelle</i> : même son, écriture différente.</li>
<li>B : l'élève lit la phrase complète à voix haute.</li>
<li>C : si l'élève ne travaille pas : <i>Je suis étudiant(e)</i> ou <i>Je ne travaille pas</i>.</li></ol>""")

    # Page 4
    b.page(f"""{sub("D", "Erreurs fréquentes", "2 min")}
<div class="box sand"><h4>ATTENTION : ERREURS FRÉQUENTES</h4>
<table style="margin:0"><tr><th>Ne dites pas</th><th>Dites</th></tr>
<tr><td>Quel est votre profession ?</td><td><b>Quelle est votre profession ?</b></td></tr>
<tr><td>Je travaille en une agence.</td><td><b>Je travaille dans une agence.</b></td></tr>
<tr><td>Elle est serveur.</td><td><b>Elle est serveuse.</b></td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Labo de prononciation", "5 min")}
{audiocard(["05.2", "05.3"])}
{sub("A", "Écoutez et répétez. Masculin, féminin.", "2 min", "05.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S052)}</div>
{sub("B", "Écoutez et répétez. Les phrases.", "3 min", "05.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S053)}</div>
<div class="box"><h4>LES SONS</h4><i>étudian(t)</i> / <i>étudian<b>te</b></i> : on entend le <b>t</b> au féminin. &nbsp;·&nbsp; <i>serv<b>eur</b></i> [œʁ] / <i>serv<b>euse</b></i> [øz]. &nbsp;·&nbsp; <i>travai<b>lle</b></i> : <b>ill</b> = « i » (comme dans « praia ») → [tʁavaj].</div>""",
    36, """<ol><li>Erreurs : <i>quel / quelle</i> se prononcent pareil ; l'erreur est à l'écrit. <i>en une agence</i> vient du portugais « em ». </li>
<li>4A : piste 05.2, l'élève répète chaque paire. 4B : piste 05.3. Pour <i>travaille</i>, faites répéter <i>je travaille, tu travailles, vous travaillez</i>.</li></ol>""")

    # Page 5
    fem = [("vendeur", "vendeuse"), ("avocat", "avocate"), ("infirmier", "infirmière"), ("médecin", "médecin"), ("étudiant", "étudiante"), ("serveur", "serveuse")]
    fl = [f'<li value="{i+1}">{m} → {A(f, "min-width:28mm")}</li>' for i, (m, f) in enumerate(fem)]
    gw = ["travaille", "travailles", "travaille", "travaillez", "travaille", "travaille"]
    gs = [("Je", " dans une agence."), ("Tu", " où ?"), ("Sophie", " à l'hôpital."), ("Vous", " à Lyon ?"), ("Hugo", " dans un café."), ("Je ne", " pas le dimanche.")]
    gl5 = [f'<li value="{i+1}">{a} {A(gw[i], "min-width:20mm")}{c}</li>' for i, (a, c) in enumerate(gs)]
    mt = [("Quel est votre nom ?", "c", "Je suis médecin."), ("Quelle est votre profession ?", "a", "Dans un café."),
          ("Vous travaillez où ?", "b", "Souza."), ("Quel est votre numéro ?", "d", "06 12 15 08 20.")]
    mr = "".join(f'<tr><td>{i+1}. {l} &nbsp;{A(k, "min-width:9mm")}</td><td>{chr(97+i)}) {r}</td></tr>' for i, (l, k, r) in enumerate(mt))
    b.page(f"""{sec(5, "Pratique", "8 min")}
{sub("A", "Écrivez la forme féminine.", "2 min")}
{twocol(fl, 3)}
{sub("B", "Complétez avec travailler.", "3 min")}
{twocol(gl5, 3)}
{sub("C", "Reliez.", "3 min")}
<table style="margin:0">{mr}</table>""",
    24, """<ol><li>A : l'élève lit chaque paire à voix haute (on entend la différence, sauf <i>médecin</i>).</li>
<li>B : en 6, <i>ne … pas</i> autour du verbe (unité 03). C : lisez les paires : ce sont les questions de la fiche de la page 6.</li></ol>""")

    # Page 6
    fiche = "".join(f'<tr><td style="width:35%"><b>{k}</b></td><td><div class="wline"></div></td></tr>' for k in ["Nom", "Prénom", "Profession", "Lieu de travail", "Téléphone"])
    cards = [("Lucas", "serveur · un café · 06 14 03 19 11"), ("Marie", "avocate · Lyon · 07 20 16 02 13")]
    cd = "".join(f'<div class="ad" style="flex:1"><b class="t">{n}</b>{d}</div>' for n, d in cards)
    b.page(f"""{sec(6, "Parler", "12 min")}
{sub("A", "Au club de tennis. Répondez à l'enseignant. Complétez votre fiche.", "6 min")}
<table class="ck" style="width:75%">{fiche}</table>
<div class="msg"><b>A :</b> Quel est votre nom ?<br><b>B :</b> …<br><b>A :</b> Quelle est votre profession ?<br><b>B :</b> Je suis …<br><b>A :</b> Vous travaillez où ?<br><b>B :</b> Je travaille …</div>
{sub("B", "Changez de rôle. Vous êtes à l'accueil. Posez les questions.", "6 min")}
<div style="display:flex;gap:2.5mm;margin:1mm 0 2mm">{cd}</div>""",
    28, """<ol><li>A : l'enseignant est à l'accueil et pose les questions ; l'élève répond et complète sa fiche (vraies informations ou inventées). Corrigez <i>Quelle est votre profession ?</i></li>
<li>B : l'enseignant joue Lucas, puis Marie ; l'élève pose les quatre questions et écrit les réponses. Pour finir : <i>Vous aimez votre travail ?</i> (révision de l'unité 04).</li></ol>""")

    # Page 7
    pc = [("Unité 03", "Je peux dire ma nationalité et mon âge."), ("Unité 04", "Je peux dire ce que j'aime."),
          ("Unité 05", "Je peux dire ma profession et où je travaille."), ("Unité 05", "Je peux poser les questions d'une fiche (quel / quelle).")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Quelle", "est votre profession ?"), ("Quel", "est votre nom ?"), ("Quel", "est votre numéro ?"), ("Quelle", "est votre nationalité ?")]
    hl = [f'<li value="{i+1}">{A(a, "min-width:16mm")} {w}</li>' for i, (a, w) in enumerate(hw)]
    b.page(f"""{sec(7, "Bilan et devoirs", "2 min")}
{sub("A", "Auto-évaluation", "1 min")}
<table class="ck"><tr><th style="width:19mm"></th><th>En français …</th><th style="width:18mm">Facile !</th><th style="width:18mm">Parfois</th><th style="width:18mm">Pas encore</th></tr>{pcr}</table>
{sub("B", "Devoirs", "1 min")}
<p><b>1. Complétez : quel ou quelle ?</b></p>
{twocol(hl, 2)}
<p style="margin-top:2mm"><b>2. Écrivez la profession de trois personnes (vous, un ami, une amie).</b></p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>
<p style="margin-top:2mm"><b>3. Présentez-vous.</b> Je m'appelle … Je suis … (nationalité). Je suis … (profession). Je travaille … J'aime …</p>
<div class="wline"></div><div class="wline"></div>""",
    22, """<p>Au prochain cours : l'élève lit sa présentation (devoir 3), qui réunit les unités 01 à 05. Dans l'unité 06 : la ville et le quartier, <i>On va où ?</i></p>""")

    b.extra("Transcriptions", f"""
{sub("05.1", "Au club de tennis (lent et naturel)")}
<p style="line-height:1.6">{"<br>".join(f"<b>{n} :</b> {t}" for n, t in SCRIPT)}</p>
{sub("05.2", "Les professions")}
<p>{" · ".join(S052)}</p>
{sub("05.3", "Les phrases")}
<p>{" · ".join(S053)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essentiel 05 - Qu'est-ce que vous faites")
