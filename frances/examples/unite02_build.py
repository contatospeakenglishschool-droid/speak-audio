# Speak! Essentiel A1 - Unité 02 "Ça va ?" (tout en français, pour vrais débutants) - built with the shared engine + French layer
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_fr import *
setup(band="A1 · UNITÉ 02", audio_json=os.path.join(HERE, "audio_fr-a1-unite-02.json"), img_dir=os.path.join(HERE, "img"), lang="fr-FR")

PHOTOS = [("A", "Super !", "super"), ("B", "Très bien !", "très bien"), ("C", "Bien.", "bien"), ("D", "Ça va.", "ça va"),
          ("E", "Pas mal.", "pas mal"), ("F", "Pas très bien.", "pas très bien"), ("G", "fatigué(e)", "fatigué"), ("H", "malade", "malade")]

SCRIPT = [("Narratrice", "Dialogue un."), ("Camila", "Bonjour, Madame Lefèvre !"), ("Madame Lefèvre", "Bonjour, Camila ! Comment allez-vous ?"),
          ("Camila", "Bien, merci. Et vous ?"), ("Madame Lefèvre", "Très bien, merci."),
          ("Narratrice", "Dialogue deux."), ("Madame Girard", "Bonjour ! Vous êtes madame Souza ?"), ("Camila", "Oui, je suis Camila Souza."),
          ("Madame Girard", "Souza … Comment ça s'écrit ?"), ("Camila", "S – O – U – Z – A."), ("Madame Girard", "Merci !"),
          ("Narratrice", "Dialogue trois."), ("Nadia", "Salut, Camila ! Ça va ?"), ("Camila", "Ça va. Je suis fatiguée. Et toi ?"),
          ("Nadia", "Super, merci ! Camila, c'est Hugo. Il est étudiant."), ("Hugo", "Salut, Camila !"), ("Camila", "Salut, Hugo ! Enchantée !")]
S022 = ["Super !", "Très bien !", "Bien.", "Ça va.", "Pas mal.", "Pas très bien.", "fatigué", "malade"]
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
    cover = cover_html(T, "NIVEAU A1 · UNITÉ 02", "Ça va ?", "Demander et dire comment ça va · l'alphabet",
                       [("VOUS POUVEZ", "demander comment ça va, répondre et épeler votre nom"),
                        ("LANGUE", "Ça va ? / Comment allez-vous ? · je suis, tu es, il / elle est, vous êtes"),
                        ("PRONONCIATION", "l'alphabet · E, G, H, J, R, U")])
    words = ["Bien.", "Ça va.", "fatigué(e)", "malade", "Pas mal.", "Pas très bien.", "Super !", "Très bien !"]
    me = "".join(f'<td style="text-align:center">☐<br><span class="small">{w}</span></td>' for w in ["Super !", "Très bien !", "Bien.", "Ça va.", "Pas mal.", "Pas très bien."])
    b.page(f"""{sec(1, "Échauffement : Ça va ?", "8 min")}
{sub("A", "Écoutez et répétez. Écrivez.", "5 min", "02.2")}
<div class="bank">{" &nbsp;·&nbsp; ".join(words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Et vous ? Ça va aujourd'hui ? Cochez.", "3 min")}
<table class="ck"><tr>{me}</tr></table>""",
    30, """<ol><li>A : piste 02.2. Montrez avec le visage et les gestes : pouce en haut = <b>Super ! / Très bien !</b>, main qui hésite = <b>Ça va. / Pas mal.</b>, pouce en bas = <b>Pas très bien.</b> Révision de l'unité 01 : commencez par <i>Bonjour ! / Salut !</i></li>
<li>B : l'enseignant demande : <i>Ça va ?</i> L'élève montre le mot et le dit. Puis l'élève pose la question à l'enseignant.</li></ol>""", cover=cover)

    b.extra("Déroulement de la leçon · 55 min", """
<table><tr><th>Étape</th><th>Durée</th><th>Objectif</th><th>Page</th></tr>
<tr><td>1 Échauffement</td><td>8 min</td><td>Ça va ? 8 réponses avec photos</td><td>1</td></tr>
<tr><td>2 Écoute</td><td>10 min</td><td>Le deuxième jour de Camila : trois petits dialogues</td><td>2</td></tr>
<tr><td>3 Grammaire</td><td>10 min</td><td><i>être</i> (singulier) · <i>Ça va ? / Comment allez-vous ?</i></td><td>3–4</td></tr>
<tr><td>4 Labo de prononciation</td><td>5 min</td><td>L'alphabet · épeler des noms</td><td>4</td></tr>
<tr><td>5 Pratique</td><td>8 min</td><td>Compléter, mettre en ordre, relier</td><td>5</td></tr>
<tr><td>6 Parler</td><td>12 min</td><td>Quatre personnes : Ça va ? · noms épelés</td><td>6</td></tr>
<tr><td>7 Bilan</td><td>2 min</td><td>Auto-évaluation et devoirs</td><td>7</td></tr></table>
<div class="box"><h4>COMMENT UTILISER CE GUIDE</h4>Chaque page correspond à la page du livre de l'élève avec le même numéro. Vos notes sont dans l'<b>encadré jaune</b>.
<span class="red">Les réponses en rouge</span> ne sont pas dans le livre de l'élève. Les étiquettes <span class="time">5 min</span> indiquent la durée de chaque activité. Les transcriptions sont à la dernière page.</div>
<div class="box"><h4>TOUJOURS LENTEMENT</h4>Il y a seulement trois nouveautés : <i>Ça va ? / Comment allez-vous ?</i> avec les réponses, les quatre formes de <i>être</i> au singulier et l'alphabet. Tout ce qui vient de l'unité 01 (salutations, <i>Je m'appelle …</i>, <i>Tu t'appelles comment ?</i>) revient. Parlez lentement, montrez beaucoup et répétez.</div>
<div class="box sand"><h4>L'HISTOIRE</h4>Le deuxième jour de Camila à Lyon. Le matin, elle revoit Madame Lefèvre (vous). À l'agence, Madame Girard, de l'accueil, demande son nom : Camila épelle <i>Souza</i>. Le soir, au café, elle est fatiguée. Nadia lui présente Hugo, son voisin. Hugo est étudiant.</div>
<div class="box"><h4>LE PROBLÈME POUR LES BRÉSILIENS</h4><i>Je suis bien</i> ✗ (comme « Estou bem ») → <b>Bien, merci.</b> / <b>Ça va bien.</b> Avec <i>Madame / Monsieur</i> : <b>Comment allez-vous ?</b> Pour l'alphabet : <b>E</b> = [ə], <b>G</b> = [ʒe], <b>J</b> = [ʒi] (le contraire du portugais !), <b>H</b> = hache, <b>R</b> = erre, <b>U</b> = [y].</div>
<div class="box"><h4>AUDIO</h4>Piste 02.1 Trois dialogues (lent et naturel) · Piste 02.2 Ça va ? · Piste 02.3 L'alphabet</div>""")

    # Page 2
    gr = [("1", "Madame Lefèvre", ["Très bien.", "Pas très bien."], "Très bien."), ("3", "Camila", ["Super !", "Ça va."], "Ça va."), ("3", "Nadia", ["Super !", "Pas mal."], "Super !")]
    wr = "".join(f'<td style="width:33%"><b>Dialogue {n}</b><br><span class="small">{p}</span><br>{ch(o, a)}</td>' for n, p, o, a in gr)
    gp = [("Comment", "allez", "-vous ?"), ("Oui, je", "suis", " Camila Souza."), ("Comment ça", "s'écrit", " ?"),
          ("Ça va. Je suis", "fatiguée", "."), ("C'est Hugo. Il", "est", " étudiant."), ("Salut, Camila ! Ça", "va", " ?")]
    gl = [f'<li value="{i+1}">{a} {A(x, "min-width:20mm")}{c}</li>' for i, (a, x, c) in enumerate(gp)]
    b.page(f"""{sec(2, "Écoute : le deuxième jour de Camila", "10 min")}
<p>C'est le deuxième jour de Camila à Lyon. Elle voit Madame Lefèvre, Madame Girard, Nadia et Hugo.</p>
{audiocard(["02.1 · SLOW", "02.1 · NATURAL"])}
{sub("A", "Écoutez. Ça va ? Choisissez.", "3 min", "02.1 · SLOW")}
<table class="ck"><tr>{wr}</tr></table>
{sub("B", "Écoutez encore. Complétez.", "5 min", "02.1 · NATURAL")}
<div class="bank">allez · est · fatiguée · s'écrit · suis · va</div>
{twocol(gl, 4)}
{sub("C", "Lisez les dialogues avec l'enseignant.", "2 min")}""",
    30, """<ol><li>A : version <b>lente</b>, deux écoutes. Avant, demandez : <i>C'est qui ?</i> (Madame Lefèvre et Nadia, de l'unité 01). Nouveaux : Madame Girard (accueil de l'agence) et Hugo (voisin).</li>
<li>B : version <b>naturelle</b>, pause après chaque dialogue. Camila épelle <i>Souza</i> : montrez rapidement, l'alphabet est à la page 4.</li>
<li>C : les dialogues sont à la dernière page. L'élève est Camila, puis on change.</li></ol>""")

    # Page 3
    etre = [("je", "suis", "Je suis Camila."), ("tu", "es", "Tu es Hugo ?"), ("il / elle", "est", "Il est étudiant."), ("vous", "êtes", "Vous êtes madame Souza ?")]
    te = "".join(f"<tr><td>{p}</td><td><b>{v}</b></td><td class='small'>{e}</td></tr>" for p, v, e in etre)
    who = [("Thomas", "collègue", "Et toi ?"), ("Madame Lefèvre", "propriétaire", "Et vous ?"), ("Hugo", "voisin", "Et toi ?"), ("Madame Girard", "accueil", "Et vous ?")]
    wt = "".join(f'<td style="width:25%"><b>{n}</b><br><span class="small">{d}</span><br>{ch(["Et toi ?", "Et vous ?"], a)}</td>' for n, d, a in who)
    b.page(f"""{sec(3, "Grammaire : être · Ça va ?", "10 min")}
{sub("A", "Lisez.", "3 min")}
<div class="two"><div><table style="margin:0"><tr><th colspan="3">être</th></tr>{te}</table></div>
<div><table style="margin:0"><tr><th>tu</th><th>vous</th></tr>
<tr><td><b>Ça va</b> ?</td><td><b>Comment allez-vous</b> ?</td></tr>
<tr><td>Bien, merci. Et <b>toi</b> ?</td><td>Bien, merci. Et <b>vous</b> ?</td></tr></table></div></div>
<div class="box"><h4>ATTENTION</h4>Ça va ? → <b>Bien, merci.</b> &nbsp;Pas : <i>Je suis bien.</i> &nbsp;·&nbsp; Mais : Je <b>suis</b> fatigué(e). Je <b>suis</b> malade.</div>
{sub("B", "Toi ou vous ? Choisissez.", "4 min")}
<table class="ck"><tr>{wt}</tr></table>
{sub("C", "Et vous ? Écrivez.", "3 min")}
<div class="two"><div class="wline">Ça va ? – {R("Bien, merci. / Ça va. / …")}</div><div class="wline">Je suis {R("… (nom)")}</div></div>""",
    32, """<ol><li>A : seulement le singulier de <i>être</i> ; le pluriel (nous, ils) vient plus tard. Révision : <i>tu</i> = amis, <i>vous</i> = Madame / Monsieur. <i>es</i> et <i>est</i> ont le même son.</li>
<li>Encadré : l'erreur <i>Je suis bien</i> vient du portugais (« Estou bem »). Avec <i>être</i> : le nom, <i>fatigué(e)</i>, <i>malade</i>. <i>fatigué</i> (homme) et <i>fatiguée</i> (femme) : même son, comme <i>enchanté(e)</i>.</li>
<li>B : comme dans l'unité 01 : collègue / voisin → toi ; Madame / Monsieur → vous.</li></ol>""")

    # Page 4
    abc = "".join(f'<td style="width:10%;text-align:center;padding:1.2mm 0.5mm{";background:#f3ead8" if l in HOT else ""}"><b style="font-size:12pt">{l}</b><br><span class="small">{n}</span></td>' + ("</tr><tr>" if (i + 1) % 10 == 0 and i < len(ABC) - 1 else "") for i, (l, n) in enumerate(ABC))
    names = ["Thomas", "Nadia", "Hugo", "Lyon", "Recife", "votre nom"]
    b.page(f"""{sub("D", "Erreurs fréquentes", "2 min")}
<div class="box sand"><h4>ATTENTION : ERREURS FRÉQUENTES</h4>
<table style="margin:0"><tr><th>Ne dites pas</th><th>Dites</th></tr>
<tr><td>Ça va ? – Je suis bien.</td><td><b>Bien, merci.</b></td></tr>
<tr><td>Vous es madame Souza ?</td><td><b>Vous êtes madame Souza ?</b></td></tr>
<tr><td>Ça va, Madame Lefèvre ?</td><td><b>Comment allez-vous, madame ?</b></td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Labo de prononciation : l'alphabet", "5 min")}
{audiocard(["02.3"])}
{sub("A", "Écoutez et répétez.", "3 min", "02.3")}
<table class="ck" style="table-layout:fixed"><tr>{abc}</tr></table>
<div class="box"><h4>DIFFÉRENT DU PORTUGAIS</h4>Les lettres en couleur : <b>E</b> [ə] &nbsp;·&nbsp; <b>G</b> [ʒe] &nbsp;·&nbsp; <b>H</b> [aʃ] &nbsp;·&nbsp; <b>J</b> [ʒi] &nbsp;·&nbsp; <b>R</b> [ɛʁ] &nbsp;·&nbsp; <b>U</b> [y] &nbsp;·&nbsp; <b>W</b> [dubləve] &nbsp;·&nbsp; <b>Y</b> [igʁɛk]</div>
{sub("B", "Épelez.", "2 min")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(names)}</div>""",
    36, """<ol><li>Erreurs : corrigez tout de suite <i>Je suis bien</i> → <i>Bien, merci.</i> Avec Madame / Monsieur, on apprend d'abord <i>Comment allez-vous ?</i></li>
<li>4A : piste 02.3, deux fois. Pour les Brésiliens : <b>G</b> = « jê », <b>J</b> = « ji » (le contraire du portugais) ; <b>U</b> : lèvres rondes, langue comme pour « i ». Le <b>h</b> est muet : <i>Hugo</i> = « ugo ».</li>
<li>4B : l'élève épelle, l'enseignant écrit. Puis on change. En cas d'erreur : <i>Pardon ?</i></li></ol>""")

    # Page 5
    gw = ["suis", "es", "est", "êtes", "est", "suis"]
    gs = [("Je", " Camila."), ("Tu", " Hugo ?"), ("C'est Hugo. Il", " étudiant."), ("Vous", " madame Girard ?"), ("C'est Nadia. Elle", " au café."), ("Je", " malade.")]
    gl5 = [f'<li value="{i+1}">{a} {A(gw[i], "min-width:16mm")}{c}</li>' for i, (a, c) in enumerate(gs)]
    od = [("allez-vous / comment / ?", "Comment allez-vous ?"), ("merci / bien / ,", "Bien, merci."), ("ça / comment / s'écrit / ?", "Comment ça s'écrit ?")]
    ol5 = "".join(f'<li>{s}<div class="wline">{R(a)}</div></li>' for s, a in od)
    mt = [("Ça va ?", "c", "Oui, je suis Hugo."), ("Comment allez-vous ?", "d", "H – U – G – O."), ("Comment ça s'écrit ?", "b", "Ça va bien, merci. Et toi ?"), ("Tu es Hugo ?", "a", "Très bien, merci. Et vous ?")]
    mr = "".join(f'<tr><td>{i+1}. {l} &nbsp;{A(k, "min-width:9mm")}</td><td>{chr(97+i)}) {r}</td></tr>' for i, (l, k, r) in enumerate(mt))
    b.page(f"""{sec(5, "Pratique", "8 min")}
{sub("A", "Complétez.", "3 min")}
<div class="bank">es · est · est · êtes · suis · suis</div>
{twocol(gl5, 4)}
{sub("B", "Mettez dans l'ordre.", "2 min")}
<ol>{ol5}</ol>
{sub("C", "Reliez.", "3 min")}
<table style="margin:0">{mr}</table>""",
    24, """<ol><li>A : <i>il</i> = Hugo (homme), <i>elle</i> = Nadia (femme). <i>es</i> / <i>est</i> : même son, écriture différente.</li>
<li>C : lisez les paires à voix haute. L'enseignant pose la question, l'élève répond.</li></ol>""")

    # Page 6
    ppl = [("Thomas", "collègue · Super !"), ("Madame Lefèvre", "propriétaire · Bien."), ("Hugo", "voisin · fatigué"), ("Madame Girard", "accueil · Pas mal.")]
    st = "".join(f'<div class="ad" style="flex:1"><b class="t">{n}</b>{d}<br>{R("→ " + ("Comment allez-vous ?" if "Madame" in n else "Ça va ?"))}</div>' for n, d in ppl)
    b.page(f"""{sec(6, "Parler", "12 min")}
{sub("A", "Jouez avec l'enseignant. Saluez la personne. Demandez : Ça va ?", "7 min")}
<div style="display:flex;gap:2.5mm;margin:1mm 0 2mm">{st}</div>
<div class="msg"><b>A :</b> Bonjour, Madame Lefèvre ! Comment allez-vous ?<br><b>B :</b> Bien, merci. Et vous ?<br><b>A :</b> Ça va. Je suis fatigué(e).</div>
{sub("B", "Écoutez et écrivez les noms.", "5 min")}
<ol style="line-height:2"><li>{A("GIRARD", "min-width:55mm")}</li><li>{A("DUBOIS", "min-width:55mm")}</li><li>{A("JOLY", "min-width:55mm")}</li><li>{A("LEROUX", "min-width:55mm")}</li></ol>""",
    30, """<ol><li>A : l'enseignant joue les quatre personnes et répond comme sur la carte. L'élève choisit <i>Ça va ?</i> ou <i>Comment allez-vous ?</i> Puis on change.</li>
<li>B : l'enseignant épelle lentement (deux fois) : G-I-R-A-R-D, D-U-B-O-I-S, J-O-L-Y, L-E-R-O-U-X. L'élève écrit et lit le nom à voix haute. Faites pratiquer : <i>Pardon ? Vous pouvez répéter ?</i></li></ol>""")

    # Page 7
    pc = [("Unité 01", "Je peux saluer et dire mon nom."), ("Unité 02", "Je peux demander : Ça va ? / Comment allez-vous ?"),
          ("Unité 02", "Je peux dire comment je vais."), ("Unité 02", "Je peux épeler mon nom.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    b.page(f"""{sec(7, "Bilan et devoirs", "2 min")}
{sub("A", "Auto-évaluation", "1 min")}
<table class="ck"><tr><th style="width:19mm"></th><th>En français …</th><th style="width:18mm">Facile !</th><th style="width:18mm">Parfois</th><th style="width:18mm">Pas encore</th></tr>{pcr}</table>
{sub("B", "Devoirs", "1 min")}
<p><b>1. Complétez les dialogues.</b></p>
<div class="msg"><b>Hugo :</b> Salut, Camila ! Ça va ?<br><b>Camila :</b> {A("Ça va bien, merci. Et toi ?", "min-width:60mm")}<br><b>Hugo :</b> Super, merci !<br><br>
<b>Camila :</b> Bonjour, Madame Girard ! Comment allez-vous ?<br><b>Madame Girard :</b> {A("Très bien, merci. Et vous ?", "min-width:60mm")}<br><b>Camila :</b> {A("Ça va. Je suis fatiguée.", "min-width:60mm")}</div>
<p style="margin-top:2mm"><b>2. Complétez : suis, es, est ou êtes ?</b> &nbsp; Je {A("suis", "min-width:12mm")} Nadia. · Tu {A("es", "min-width:12mm")} Hugo ? · Il {A("est", "min-width:12mm")} étudiant. · Vous {A("êtes", "min-width:12mm")} madame Lefèvre ?</p>
<p style="margin-top:2mm"><b>3. Écrivez votre nom et votre ville.</b> Épelez-les au prochain cours.</p>
<div class="wline"></div><div class="wline"></div>""",
    22, """<p>Au prochain cours : commencez par <i>Salut ! Ça va ?</i> L'élève épelle son nom et sa ville (devoir 3), l'enseignant écrit. Dans l'unité 03 : les pays, <i>Tu viens d'où ?</i></p>""")

    b.extra("Transcriptions", f"""
{sub("02.1", "Le deuxième jour de Camila (lent et naturel)")}
<p style="line-height:1.6">{"<br>".join(f"<b>{n} :</b> {t}" for n, t in SCRIPT)}</p>
{sub("02.2", "Ça va ?")}
<p>{" · ".join(S022)}</p>
{sub("02.3", "L'alphabet")}
<p>{" · ".join(f"{l} ({n})" for l, n in ABC)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essentiel 02 - Ça va")
