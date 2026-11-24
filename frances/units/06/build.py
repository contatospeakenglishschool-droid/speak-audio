# Speak! Essentiel A1 - Unité 06 "On va où ?" (tout en français, pour vrais débutants) - built with the shared engine + French layer
# Plan (Édito A1 unité 2, Alter Ego 1 dossier 1): the city and the neighbourhood; un / une / des vs le / la / les; il y a; à / au / en + cities and countries.
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_fr import *
setup(band="A1 · UNITÉ 06", audio_json=os.path.join(HERE, "audio_fr-a1-unite-06.json"), img_dir=os.path.join(HERE, "img"), lang="fr-FR")

# Warm-up rule (2026-11-23): bank alphabetical (bank_key), photos shuffled (bank order 5,2,6,0,3,7,1,4: no fixed point, no run).
PHOTOS = [('A', 'une pharmacie', 'pharmacie'), ('B', 'une gare', 'gare'), ('C', 'un restaurant', 'restaurant'), ('D', 'une banque', 'banque'),
          ('E', 'un musée', 'musée'), ('F', 'un supermarché', 'supermarché'), ('G', 'une boulangerie', 'boulangerie'), ('H', 'un parc', 'parc')]

SCRIPT = [("Narratrice", "Dialogue un."), ("Camila", "Hugo, il y a une pharmacie dans le quartier ?"),
          ("Hugo", "Oui, il y a une pharmacie, rue d'Austerlitz. Il y a aussi une boulangerie, un marché et des restaurants."),
          ("Camila", "Et un supermarché ?"), ("Hugo", "Oui, il y a un supermarché, rue de Belfort."), ("Camila", "Super ! Le quartier est sympa."),
          ("Narratrice", "Dialogue deux."), ("Madame Lefèvre", "Bonjour, Camila ! Vous allez où ?"),
          ("Camila", "Bonjour, madame ! Je vais à la boulangerie. Et vous ?"), ("Madame Lefèvre", "Moi, je vais à la pharmacie. Bonne journée !"),
          ("Camila", "Bonne journée, madame !"),
          ("Narratrice", "Dialogue trois."), ("Nadia", "Camila, en août, tu vas où ?"), ("Camila", "Je vais au Brésil, à Recife ! Et toi, Nadia ?"),
          ("Nadia", "Moi, je vais en Italie, à Rome."), ("Thomas", "Et moi, je vais à Paris."), ("Nadia", "Et ce soir, on va où ?"), ("Thomas", "Au cinéma !")]
S062 = ["une banque", "une boulangerie", "une gare", "un musée", "un parc", "une pharmacie", "un restaurant … des restaurants", "un supermarché"]
S063 = ["On va où ?", "Il y a une pharmacie dans le quartier ?", "Il y a des restaurants.", "Je vais à la boulangerie.", "Je vais au Brésil, à Recife.", "Je vais en France, à Lyon."]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def tick(yes):
        return R("✓") if (T and yes) else "☐"

    # Page 1
    cover = cover_html(T, "NIVEAU A1 · UNITÉ 06", "On va où ?", "Le quartier et la ville",
                       [("VOUS POUVEZ", "dire ce qu'il y a dans votre quartier et où vous allez"),
                        ("LANGUE", "il y a un / une / des · je vais, tu vas, vous allez · à Lyon, en France, au Brésil"),
                        ("PRONONCIATION", "il y a · au · en, on (sons nasals)")])
    places = sorted((p[1] for p in PHOTOS), key=bank_key)
    mq = "".join(f'<td style="width:25%">☐ {w}</td>' + ("</tr><tr>" if i == 3 else "") for i, w in enumerate(places))
    b.page(f"""{sec(1, "Échauffement : les lieux du quartier", "8 min")}
{sub("A", "Écoutez et répétez. Écrivez.", "5 min", "06.2")}
<div class="bank">{" &nbsp;·&nbsp; ".join(places)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Et votre quartier ? Cochez.", "3 min")}
<table class="ck"><tr>{mq}</tr></table>""",
    30, """<ol><li>A : piste 06.2. Montrez chaque photo et dites le mot avec <i>un</i> ou <i>une</i> ; l'élève répète et écrit le mot avec l'article. Révision de l'unité 05 : <i>Qui travaille ici ? Un serveur, une pharmacienne…</i> (si l'élève connaît le mot).</li>
<li>B : l'élève coche les lieux de son quartier. Posez la question : <i>Il y a une pharmacie ?</i> Réponse simple : <i>Oui. / Non.</i> La règle de <i>il y a</i> est à la page 3.</li></ol>""", cover=cover)

    b.extra("Déroulement de la leçon · 55 min", """
<table><tr><th>Étape</th><th>Durée</th><th>Objectif</th><th>Page</th></tr>
<tr><td>1 Échauffement</td><td>8 min</td><td>8 lieux du quartier avec photos (un / une)</td><td>1</td></tr>
<tr><td>2 Écoute</td><td>10 min</td><td>Le quartier de Camila et les vacances : trois petits dialogues</td><td>2</td></tr>
<tr><td>3 Grammaire</td><td>10 min</td><td><i>il y a</i> + un / une / des · <i>je vais</i> + à / au / en</td><td>3–4</td></tr>
<tr><td>4 Labo de prononciation</td><td>5 min</td><td>Les lieux · phrases utiles</td><td>4</td></tr>
<tr><td>5 Pratique</td><td>8 min</td><td>un / une / des · à / au / en · relier</td><td>5</td></tr>
<tr><td>6 Parler</td><td>12 min</td><td>Votre quartier · Vous allez où en vacances ?</td><td>6</td></tr>
<tr><td>7 Bilan</td><td>2 min</td><td>Auto-évaluation et devoirs</td><td>7</td></tr></table>
<div class="box"><h4>COMMENT UTILISER CE GUIDE</h4>Chaque page correspond à la page du livre de l'élève avec le même numéro. Vos notes sont dans l'<b>encadré jaune</b>.
<span class="red">Les réponses en rouge</span> ne sont pas dans le livre de l'élève. Les étiquettes <span class="time">5 min</span> indiquent la durée de chaque activité. Les transcriptions sont à la dernière page.</div>
<div class="box"><h4>TOUJOURS LENTEMENT</h4>Une seule mission : parler des lieux (le quartier, les vacances). Trois nouveautés : <i>il y a</i> + <i>un / une / des</i> ; trois formes de <i>aller</i> en formule (<i>je vais, tu vas, vous allez</i> ; le verbe complet vient plus tard) ; <i>à</i> + ville, <i>en</i> / <i>au</i> + pays. <i>On va où ?</i> = « a gente vai aonde ? » : <i>on</i> = nous, dans la conversation. Les nationalités de l'unité 03 aident pour les pays.</div>
<div class="box sand"><h4>L'HISTOIRE</h4>Samedi à la Croix-Rousse, le quartier de Camila à Lyon. Hugo, le voisin, présente le quartier : une pharmacie, une boulangerie, un marché, des restaurants, un supermarché. Dans la rue, Madame Lefèvre va à la pharmacie (vous). Le soir, au café de Nadia, on parle des vacances d'août : Camila va au Brésil, Nadia en Italie, Thomas à Paris. Et ce soir ? Au cinéma !</div>
<div class="box"><h4>LE PROBLÈME POUR LES BRÉSILIENS</h4><i>Je vais en Brésil</i> ✗ → <b>au Brésil</b> : en portugais, « no / na » ; en français, <i>en</i> + pays féminin (<i>la France</i>), <i>au</i> + pays masculin (<i>le Brésil</i>). <i>Il y a restaurants</i> ✗ → <b>des restaurants</b> : en français, le pluriel a un article. <i>Je vais à le cinéma</i> ✗ → <b>au cinéma</b> (à + le = au).</div>
<div class="box"><h4>AUDIO</h4>Piste 06.1 Trois dialogues (lent et naturel) · Piste 06.2 Les lieux · Piste 06.3 Les phrases</div>""")

    # Page 2
    heard = [("une pharmacie", True), ("une gare", False), ("une boulangerie", True), ("un musée", False),
             ("un marché", True), ("une banque", False), ("des restaurants", True), ("un supermarché", True)]
    ht = "".join(f'<td style="width:25%">{tick(y)} {w}</td>' + ("</tr><tr>" if i == 3 else "") for i, (w, y) in enumerate(heard))
    gp = [("Il y a", "une", " pharmacie dans le quartier ?"), ("Il y a aussi", "des", " restaurants."), ("Je vais à la", "boulangerie", "."),
          ("Je vais", "au", " Brésil, à Recife."), ("Moi, je vais", "en", " Italie, à Rome."), ("Et ce soir, on va où ? —", "Au", " cinéma !")]
    gl = [f'<li value="{i+1}">{a} {A(x, "min-width:16mm")}{c}</li>' for i, (a, x, c) in enumerate(gp)]
    b.page(f"""{sec(2, "Écoute : le quartier de Camila", "10 min")}
<p>Samedi à Lyon. Camila est dans son quartier, la Croix-Rousse.</p>
{audiocard(["06.1 · SLOW", "06.1 · NATURAL"])}
{sub("A", "Écoutez le dialogue 1. Qu'est-ce qu'il y a dans le quartier ? Cochez.", "3 min", "06.1 · SLOW")}
<table class="ck"><tr>{ht}</tr></table>
{sub("B", "Écoutez les trois dialogues. Complétez.", "5 min", "06.1 · NATURAL")}
<div class="bank">au · Au · boulangerie · des · en · une</div>
{twocol(gl, 4)}
{sub("C", "Lisez les dialogues avec l'enseignant.", "2 min")}""",
    30, """<ol><li>A : version <b>lente</b>, dialogue 1 deux fois. Cinq lieux sont dans le quartier ; pas de gare, pas de musée, pas de banque.</li>
<li>B : version <b>naturelle</b>, les trois dialogues. Madame Lefèvre dit <i>vous</i> ; Nadia et Camila disent <i>tu</i>.</li>
<li>C : les dialogues sont à la dernière page. L'élève est Camila, puis on change.</li></ol>""")

    # Page 3 (explanation first: 3A explanation, 3B check, 3C practice)
    art = [("un", "masculin", "Il y a <b>un</b> parc."), ("une", "féminin", "Il y a <b>une</b> gare."), ("des", "pluriel", "Il y a <b>des</b> restaurants.")]
    ta = "".join(f"<tr><td><b>{a}</b></td><td class='small'>{g}</td><td>{e}</td></tr>" for a, g, e in art)
    go = [("à", "+ ville", "à Lyon · à Recife"), ("en", "+ pays féminin", "en France · en Italie"), ("au", "+ pays masculin", "au Brésil · au Portugal"),
          ("aux", "+ pays pluriel", "aux États-Unis")]
    tg = "".join(f"<tr><td><b>{p}</b></td><td class='small'>{g}</td><td>{e}</td></tr>" for p, g, e in go)
    ck = [("Il y a", ["un", "une"], "une", "gare."), ("Il y a", ["des", "une"], "des", "restaurants."),
          ("Je vais", ["en", "au"], "au", "Brésil."), ("Tu vas", ["à", "en"], "à", "Paris ?")]
    ct = "".join(f'<td style="width:25%">{s} {ch(o, a)} {e}</td>' for s, o, a, e in ck)
    b.page(f"""{sec(3, "Grammaire : il y a · un / une / des · à / en / au", "10 min")}
{sub("A", "Lisez.", "4 min")}
<div class="two"><div><table style="margin:0"><tr><th colspan="3">il y a + un / une / des</th></tr>{ta}</table></div>
<div><table style="margin:0"><tr><th colspan="3">je vais · tu vas · vous allez</th></tr>{tg}</table></div></div>
<div class="box"><h4>LA RÈGLE</h4><b>il y a</b> = « tem / há » : Il y a une pharmacie. &nbsp;·&nbsp; <b>un / une / des</b> : on présente une chose. <b>le / la / les</b> : on connaît la chose : <b>le</b> quartier, <b>le</b> café de Nadia. &nbsp;·&nbsp; Lieux : à <b>la</b> boulangerie, <b>au</b> cinéma (à + le = <b>au</b>). &nbsp;·&nbsp; Pays en <b>-e</b> = féminin : <b>en</b> France, <b>en</b> Italie. Le Brésil, le Portugal, le Canada = masculin : <b>au</b>.</div>
{sub("B", "Choisissez.", "3 min")}
<table class="ck"><tr>{ct}</tr></table>
{sub("C", "Et vous ? Écrivez.", "3 min")}
<p style="line-height:2.2">Dans mon quartier, il y a {A("une boulangerie, des restaurants…", "min-width:70mm")} . <br>En vacances, je vais {A("au … / en … , à …", "min-width:70mm")} .</p>""",
    30, """<ol><li>A : lisez les tableaux avec l'élève. <i>il y a</i> ne change pas (singulier ou pluriel). Le pays a un genre comme les mots : <i>la France</i> → <i>en France</i> ; <i>le Brésil</i> → <i>au Brésil</i>. Exception utile : <i>le Mexique</i> → <i>au Mexique</i>.</li>
<li>B : l'élève lit la phrase complète à voix haute.</li>
<li>C : aidez avec le nom du pays en français si nécessaire (<i>l'Argentine, le Chili, le Japon…</i>).</li></ol>""")

    # Page 4
    b.page(f"""{sub("D", "Erreurs fréquentes", "2 min")}
<div class="box sand"><h4>ATTENTION : ERREURS FRÉQUENTES</h4>
<table style="margin:0"><tr><th>Ne dites pas</th><th>Dites</th></tr>
<tr><td>Je vais en Brésil.</td><td><b>Je vais au Brésil.</b></td></tr>
<tr><td>Il y a restaurants.</td><td><b>Il y a des restaurants.</b></td></tr>
<tr><td>Je vais à le cinéma.</td><td><b>Je vais au cinéma.</b></td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Labo de prononciation", "5 min")}
{audiocard(["06.2", "06.3"])}
{sub("A", "Écoutez et répétez. Les lieux.", "2 min", "06.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S062)}</div>
{sub("B", "Écoutez et répétez. Les phrases.", "3 min", "06.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S063)}</div>
<div class="box"><h4>LES SONS</h4><i>il y a</i> = un seul mot à l'oral : [ilja]. &nbsp;·&nbsp; <i><b>au</b></i> = [o], comme « ô ». &nbsp;·&nbsp; Sons nasals : <i>en</i>, <i>France</i> [ɑ̃] ; <i>on</i> [ɔ̃]. &nbsp;·&nbsp; <i>vais</i> [vɛ] : le <b>s</b> final ne se prononce pas.</div>""",
    36, """<ol><li>Erreurs : <i>en Brésil</i> vient du portugais « no Brasil » ; rappelez la règle du genre des pays.</li>
<li>4A : piste 06.2, l'élève répète avec l'article. 4B : piste 06.3. Faites répéter <i>il y a</i> lentement puis vite : [ilja].</li></ol>""")

    # Page 5
    ar = [("une", "banque"), ("un", "musée"), ("des", "restaurants"), ("une", "gare"), ("un", "parc"), ("des", "pharmacies")]
    al = [f'<li value="{i+1}">Il y a {A(a, "min-width:12mm")} {w}.</li>' for i, (a, w) in enumerate(ar)]
    pr = [("à", "Paris"), ("au", "Portugal"), ("en", "France"), ("au", "Canada"), ("à", "Rome"), ("en", "Espagne")]
    pl = [f'<li value="{i+1}">Je vais {A(p, "min-width:12mm")} {w}.</li>' for i, (p, w) in enumerate(pr)]
    mt = [("Il y a une banque ?", "c", "Je vais à la gare."), ("Vous allez où ?", "a", "En Italie, à Rome."),
          ("Tu vas où en août ?", "b", "Oui, rue de Belfort."), ("On va où ce soir ?", "d", "Au cinéma !")]
    mr = "".join(f'<tr><td>{i+1}. {l} &nbsp;{A(k, "min-width:9mm")}</td><td>{chr(97+i)}) {r}</td></tr>' for i, (l, k, r) in enumerate(mt))
    b.page(f"""{sec(5, "Pratique", "8 min")}
{sub("A", "Complétez : un, une ou des ?", "2 min")}
{twocol(al, 4)}
{sub("B", "Complétez : à, au ou en ?", "3 min")}
{twocol(pl, 4)}
{sub("C", "Reliez.", "3 min")}
<table style="margin:0">{mr}</table>""",
    24, """<ol><li>A : en 6, <i>des pharmacies</i> : le <b>s</b> du pluriel ne s'entend pas, mais <i>des</i> s'entend. B : <i>l'Espagne</i> est féminin → <i>en Espagne</i>.</li>
<li>C : lisez les paires à voix haute : ce sont les questions de la page 6.</li></ol>""")

    # Page 6
    qp = ["une boulangerie", "un parc", "une gare", "un musée", "des restaurants", "un supermarché"]
    qt = "".join(f"<tr><td>{w}</td><td style='width:16mm'>☐ oui</td><td style='width:16mm'>☐ non</td></tr>" for w in qp)
    cards = [("Paul", "le Canada · Montréal", "au Canada, à Montréal"), ("Léa", "l'Espagne · Barcelone", "en Espagne, à Barcelone"),
             ("Kenji", "le Japon · Tokyo", "au Japon, à Tokyo")]
    cd = "".join(f'<div class="ad" style="flex:1"><b class="t">{n}</b>{d}<br><span class="small">Il / Elle va {A(r, "min-width:40mm")}</span></div>' for n, d, r in cards)
    b.page(f"""{sec(6, "Parler", "12 min")}
{sub("A", "Votre quartier. Répondez à l'enseignant. Cochez.", "6 min")}
<table class="ck" style="width:70%">{qt}</table>
<div class="msg"><b>A :</b> Il y a une boulangerie dans votre quartier ?<br><b>B :</b> Oui, il y a une boulangerie, rue … / Non.<br><b>A :</b> Et des restaurants ?<br><b>B :</b> Oui, il y a des restaurants.</div>
{sub("B", "Les vacances. Posez la question : Vous allez où ? Écrivez.", "6 min")}
<div style="display:flex;gap:2.5mm;margin:1mm 0 2mm">{cd}</div>""",
    28, """<ol><li>A : posez les six questions ; l'élève répond avec <i>Oui, il y a…</i> ou <i>Non.</i> (la négation <i>pas de</i> vient à l'unité 07). Puis l'élève vous pose les questions sur votre quartier.</li>
<li>B : l'enseignant joue Paul, Léa et Kenji ; l'élève demande <i>Vous allez où ?</i> et écrit la réponse. Pour finir : <i>Et vous, vous allez où en vacances ?</i></li></ol>""")

    # Page 7
    pc = [("Unité 04", "Je peux dire ce que j'aime."), ("Unité 05", "Je peux dire ma profession et où je travaille."),
          ("Unité 06", "Je peux dire ce qu'il y a dans mon quartier (il y a un / une / des)."), ("Unité 06", "Je peux dire où je vais (à Lyon, en France, au Brésil).")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("au", "Japon"), ("à", "Lyon"), ("en", "Italie"), ("au", "Brésil")]
    hl = [f'<li value="{i+1}">Je vais {A(a, "min-width:12mm")} {w}.</li>' for i, (a, w) in enumerate(hw)]
    b.page(f"""{sec(7, "Bilan et devoirs", "2 min")}
{sub("A", "Auto-évaluation", "1 min")}
<table class="ck"><tr><th style="width:19mm"></th><th>En français …</th><th style="width:18mm">Facile !</th><th style="width:18mm">Parfois</th><th style="width:18mm">Pas encore</th></tr>{pcr}</table>
{sub("B", "Devoirs", "1 min")}
<p><b>1. Complétez : à, au ou en ?</b></p>
{twocol(hl, 3)}
<p style="margin-top:2mm"><b>2. Votre quartier : écrivez trois phrases avec il y a.</b></p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>
<p style="margin-top:2mm"><b>3. Les vacances.</b> En vacances, je vais … (pays), à … (ville). J'aime …</p>
<div class="wline"></div><div class="wline"></div>""",
    22, """<p>Au prochain cours : l'élève lit ses phrases sur son quartier (devoir 2). Dans l'unité 07 : la nourriture et les repas, <i>Qu'est-ce qu'on mange ?</i></p>""")

    b.extra("Transcriptions", f"""
{sub("06.1", "Le quartier de Camila (lent et naturel)")}
<p style="line-height:1.6">{"<br>".join(f"<b>{n} :</b> {t}" for n, t in SCRIPT)}</p>
{sub("06.2", "Les lieux")}
<p>{" · ".join(S062)}</p>
{sub("06.3", "Les phrases")}
<p>{" · ".join(S063)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essentiel 06 - On va où")
