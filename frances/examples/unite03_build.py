# Speak! Essentiel A1 - Unité 03 "Et vous ?" (tout en français, pour vrais débutants) - built with the shared engine + French layer
# Plan (Édito A1 unité 1, Alter Ego 1 dossier 0): nationality, age; être; avoir (… ans); nationality adjectives m/f; ne … pas.
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_fr import *
setup(band="A1 · UNITÉ 03", audio_json=os.path.join(HERE, "audio_fr-a1-unite-03.json"), img_dir=os.path.join(HERE, "img"), lang="fr-FR")

PHOTOS = [("A", "brésilien(ne)", "brésilien"), ("B", "français(e)", "français"), ("C", "portugais(e)", "portugais"), ("D", "espagnol(e)", "espagnol"),
          ("E", "italien(ne)", "italien"), ("F", "canadien(ne)", "canadien"), ("G", "belge", "belge"), ("H", "américain(e)", "américain")]

SCRIPT = [("Narratrice", "Dialogue un."), ("Madame Lefèvre", "Bonjour, Camila ! Vous êtes portugaise ?"),
          ("Camila", "Non, madame, je ne suis pas portugaise. Je suis brésilienne."), ("Madame Lefèvre", "Ah, brésilienne ! Bienvenue à Lyon !"),
          ("Camila", "Merci, madame !"),
          ("Narratrice", "Dialogue deux."), ("Hugo", "Nadia, tu es française ?"), ("Nadia", "Oui, je suis française. Et toi, Camila, tu es espagnole ?"),
          ("Camila", "Non, je ne suis pas espagnole. Je suis brésilienne, de Recife."), ("Nadia", "Brésilienne ! Super !"),
          ("Narratrice", "Dialogue trois."), ("Hugo", "Camila, tu as quel âge ?"), ("Camila", "J'ai trente-deux ans. Et toi ?"),
          ("Hugo", "J'ai vingt-deux ans."), ("Camila", "Tu es étudiant ?"), ("Hugo", "Oui, je suis étudiant.")]
S032 = ["brésilien … brésilienne", "français … française", "portugais … portugaise", "espagnol … espagnole",
        "italien … italienne", "canadien … canadienne", "américain … américaine", "belge … belge"]
S033 = ["vingt ans", "vingt-deux ans", "trente ans", "trente-deux ans", "quarante ans", "cinquante ans", "soixante ans",
        "J'ai trente-deux ans.", "Tu as quel âge ?", "Vous avez quel âge ?"]
AGES = [(20, "vingt"), (22, "vingt-deux"), (30, "trente"), (32, "trente-deux"), (40, "quarante"), (50, "cinquante"), (60, "soixante")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "NIVEAU A1 · UNITÉ 03", "Et vous ?", "Dire sa nationalité et son âge",
                       [("VOUS POUVEZ", "dire votre nationalité et votre âge, et poser la question"),
                        ("LANGUE", "je suis, tu es, il / elle est, vous êtes · brésilien / brésilienne · ne … pas · J'ai … ans"),
                        ("PRONONCIATION", "masculin / féminin · les âges · deux ans")])
    b.page(f"""{sec(1, "Échauffement : les nationalités", "8 min")}
{sub("A", "Écoutez et répétez. Écrivez.", "5 min", "03.2")}
<div class="bank">{" &nbsp;·&nbsp; ".join(sorted(p[1] for p in PHOTOS))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Et vous ? Écrivez.", "3 min")}
<p style="line-height:2.2">Je m'appelle {A("…", "min-width:40mm")} . Je suis {A("brésilien / brésilienne", "min-width:50mm")} .</p>""",
    30, """<ol><li>A : piste 03.2. Montrez chaque photo : <i>C'est le Brésil. Il est brésilien, elle est brésilienne.</i> L'élève répète les deux formes et écrit le mot sous la photo. Révision de l'unité 01 : commencez par <i>Bonjour ! Vous vous appelez comment ?</i></li>
<li>B : un homme écrit <i>brésilien</i>, une femme écrit <i>brésilienne</i>. Ne donnez pas encore la règle : elle est à la page 3.</li></ol>""", cover=cover)

    b.extra("Déroulement de la leçon · 55 min", """
<table><tr><th>Étape</th><th>Durée</th><th>Objectif</th><th>Page</th></tr>
<tr><td>1 Échauffement</td><td>8 min</td><td>8 nationalités avec photos</td><td>1</td></tr>
<tr><td>2 Écoute</td><td>10 min</td><td>Camila parle de sa nationalité et de son âge : trois petits dialogues</td><td>2</td></tr>
<tr><td>3 Grammaire</td><td>10 min</td><td><i>être</i> (singulier) · masculin / féminin · <i>ne … pas</i> · <i>J'ai … ans</i></td><td>3–4</td></tr>
<tr><td>4 Labo de prononciation</td><td>5 min</td><td>Masculin / féminin à l'oral · les âges</td><td>4</td></tr>
<tr><td>5 Pratique</td><td>8 min</td><td>Compléter, écrire le féminin, relier</td><td>5</td></tr>
<tr><td>6 Parler</td><td>12 min</td><td>Quatre personnes : nationalité et âge · questions de l'enseignant</td><td>6</td></tr>
<tr><td>7 Bilan</td><td>2 min</td><td>Auto-évaluation et devoirs</td><td>7</td></tr></table>
<div class="box"><h4>COMMENT UTILISER CE GUIDE</h4>Chaque page correspond à la page du livre de l'élève avec le même numéro. Vos notes sont dans l'<b>encadré jaune</b>.
<span class="red">Les réponses en rouge</span> ne sont pas dans le livre de l'élève. Les étiquettes <span class="time">5 min</span> indiquent la durée de chaque activité. Les transcriptions sont à la dernière page.</div>
<div class="box"><h4>TOUJOURS LENTEMENT</h4>Une seule mission : se présenter avec la nationalité et l'âge. Trois nouveautés : <i>être</i> au singulier avec une nationalité (masculin / féminin), la négation <i>ne … pas</i> et l'âge avec <i>avoir</i> (<i>J'ai … ans</i>, seulement comme formule). Pour l'âge, on voit les dizaines (20, 30, 40, 50, 60) et le modèle <i>trente-deux</i> ; les nombres complets viennent plus tard.</div>
<div class="box sand"><h4>L'HISTOIRE</h4>Le troisième jour de Camila à Lyon. Le matin, Madame Lefèvre pense qu'elle est portugaise (vous). Le soir, au café de Nadia, Hugo demande à Nadia si elle est française, et Nadia demande à Camila si elle est espagnole (tu). Puis Hugo et Camila parlent de leur âge : 32 ans et 22 ans.</div>
<div class="box"><h4>LE PROBLÈME POUR LES BRÉSILIENS</h4><i>Je non suis pas</i> ✗ → <b>Je ne suis pas</b> : en français, la négation a deux parties autour du verbe. <i>J'ai 32</i> ✗ → <b>J'ai 32 ans</b> : le mot <i>ans</i> est obligatoire. Et à l'oral, le masculin et le féminin ne sonnent pas pareil : <i>françai(s)</i> / <i>françai<b>se</b></i>, <i>brésili<b>en</b></i> (son nasal) / <i>brésili<b>enne</b></i>.</div>
<div class="box"><h4>AUDIO</h4>Piste 03.1 Trois dialogues (lent et naturel) · Piste 03.2 Masculin, féminin · Piste 03.3 Les âges</div>""")

    # Page 2
    gr = [("1", "Camila est …", ["portugaise", "brésilienne"], "brésilienne"), ("2", "Nadia est …", ["française", "espagnole"], "française"),
          ("3", "Hugo a …", ["22 ans", "32 ans"], "22 ans")]
    wr = "".join(f'<td style="width:33%"><b>Dialogue {n}</b><br><span class="small">{p}</span><br>{ch(o, a)}</td>' for n, p, o, a in gr)
    gp = [("Vous êtes", "portugaise", " ?"), ("Non, madame, je ne suis", "pas", " portugaise."), ("Oui, je", "suis", " française."),
          ("Et toi, Camila, tu", "es", " espagnole ?"), ("Camila, tu", "as", " quel âge ?"), ("J'", "ai", " trente-deux ans.")]
    gl = [f'<li value="{i+1}">{a} {A(x, "min-width:20mm")}{c}</li>' for i, (a, x, c) in enumerate(gp)]
    b.page(f"""{sec(2, "Écoute : tu es espagnole ?", "10 min")}
<p>C'est le troisième jour de Camila à Lyon. Elle parle avec Madame Lefèvre, Nadia et Hugo.</p>
{audiocard(["03.1 · SLOW", "03.1 · NATURAL"])}
{sub("A", "Écoutez. Choisissez.", "3 min", "03.1 · SLOW")}
<table class="ck"><tr>{wr}</tr></table>
{sub("B", "Écoutez encore. Complétez.", "5 min", "03.1 · NATURAL")}
<div class="bank">ai · as · es · pas · portugaise · suis</div>
{twocol(gl, 3)}
{sub("C", "Lisez les dialogues avec l'enseignant.", "2 min")}""",
    30, """<ol><li>A : version <b>lente</b>, deux écoutes. Avant, rappelez qui est qui : Madame Lefèvre (propriétaire, vous), Nadia (café), Hugo (voisin, étudiant).</li>
<li>B : version <b>naturelle</b>, pause après chaque dialogue. Faites remarquer <i>ne … pas</i> dans la phrase 2.</li>
<li>C : les dialogues sont à la dernière page. L'élève est Camila, puis on change.</li></ol>""")

    # Page 3 (explanation first: 3A explanation, 3B check, 3C practice)
    etre = [("je", "suis", "Je suis brésilienne."), ("tu", "es", "Tu es française ?"), ("il / elle", "est", "Il est étudiant. Elle est française."), ("vous", "êtes", "Vous êtes portugaise ?")]
    te = "".join(f"<tr><td>{p}</td><td><b>{v}</b></td><td class='small'>{e}</td></tr>" for p, v, e in etre)
    mf = [("brésilien", "brésili<b>enne</b>"), ("italien", "itali<b>enne</b>"), ("français", "françai<b>se</b>"), ("espagnol", "espagnol<b>e</b>"), ("belge", "belge")]
    tm = "".join(f"<tr><td>{m}</td><td>{f}</td></tr>" for m, f in mf)
    ck = [("Camila est", ["brésilien", "brésilienne"], "brésilienne"), ("Hugo est", ["français", "française"], "français"),
          ("Nadia", ["es", "est"], "est"), ("Je", ["ne suis pas", "suis ne pas"], "ne suis pas")]
    ct = "".join(f'<td style="width:25%">{s}<br>{ch(o, a)}</td>' for s, o, a in ck)
    b.page(f"""{sec(3, "Grammaire : être · masculin / féminin · ne … pas", "10 min")}
{sub("A", "Lisez.", "4 min")}
<div class="two"><div><table style="margin:0"><tr><th colspan="3">être</th></tr>{te}</table></div>
<div><table style="margin:0"><tr><th>homme</th><th>femme</th></tr>{tm}</table></div></div>
<div class="box"><h4>LA RÈGLE</h4><b>Femme</b> → forme féminine : Camila est brésili<b>enne</b>, Nadia est françai<b>se</b>. &nbsp;·&nbsp; <b>Négation</b> : <b>ne</b> + verbe + <b>pas</b> → Je <b>ne</b> suis <b>pas</b> portugaise. &nbsp;·&nbsp; <b>L'âge</b> avec <b>avoir</b> : J'<b>ai</b> 32 <b>ans</b>. Tu <b>as</b> quel âge ?</div>
{sub("B", "Choisissez.", "3 min")}
<table class="ck"><tr>{ct}</tr></table>
{sub("C", "Et vous ? Écrivez.", "3 min")}
<p style="line-height:2.2">Je suis {A("brésilien / brésilienne", "min-width:50mm")} .<br>Je ne suis pas {A("français / française", "min-width:50mm")} .<br>J'ai {A("…", "min-width:20mm")} ans.</p>""",
    30, """<ol><li>A : lisez les tableaux avec l'élève. <i>être</i> seulement au singulier ; le pluriel vient plus tard. Montrez le féminin : <i>-ien → -ienne</i>, <i>+ e</i>, et <i>belge</i> ne change pas. Dans l'encadré, <i>J'ai … ans</i> est une formule : <i>avoir</i> complet vient plus tard.</li>
<li>B : l'élève lit la phrase complète à voix haute.</li>
<li>C : phrases personnelles ; l'élève les dit ensuite à voix haute.</li></ol>""")

    # Page 4
    ages = "".join(f'<td style="width:14.28%;text-align:center;padding:1.2mm 0.5mm"><b style="font-size:12pt">{n}</b><br><span class="small">{w}</span></td>' for n, w in AGES)
    b.page(f"""{sub("D", "Erreurs fréquentes", "2 min")}
<div class="box sand"><h4>ATTENTION : ERREURS FRÉQUENTES</h4>
<table style="margin:0"><tr><th>Ne dites pas</th><th>Dites</th></tr>
<tr><td>Je non suis pas portugaise.</td><td><b>Je ne suis pas portugaise.</b></td></tr>
<tr><td>Camila est brésilien.</td><td><b>Camila est brésilienne.</b></td></tr>
<tr><td>J'ai 32.</td><td><b>J'ai 32 ans.</b></td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Labo de prononciation", "5 min")}
{audiocard(["03.2", "03.3"])}
{sub("A", "Écoutez et répétez. Masculin, féminin.", "2 min", "03.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S032)}</div>
{sub("B", "Écoutez et répétez. Les âges.", "3 min", "03.3")}
<table class="ck" style="table-layout:fixed"><tr>{ages}</tr></table>
<div class="box"><h4>LES SONS</h4>Masculin : la consonne finale est muette → <i>françai(s), portugai(s)</i>. Féminin : on l'entend → <i>françai<b>se</b>, portugai<b>se</b></i>. &nbsp;·&nbsp; <i>brésili<b>en</b></i> = son nasal, <i>brésili<b>enne</b></i> = pas nasal. &nbsp;·&nbsp; <i>deux‿ans</i> = « deu-z-ans ».</div>""",
    36, """<ol><li>Erreurs : <i>Je non suis</i> vient du portugais « não ». <i>J'ai 32</i> : en portugais, on dit souvent « tenho 32 » ; en français, <i>ans</i> est obligatoire.</li>
<li>4A : piste 03.2. L'élève répète chaque paire en exagérant la différence. 4B : piste 03.3. Montrez la liaison <i>deux‿ans</i>. Pour les autres âges : dizaine + chiffre (<i>vingt-huit, trente-cinq</i>) ; <i>vingt et un, trente et un</i> plus tard.</li></ol>""")

    # Page 5
    gw = ["suis", "es", "est", "êtes", "est", "suis"]
    gs = [("Je", " brésilienne."), ("Tu", " française ?"), ("Hugo", " étudiant."), ("Vous", " portugais ?"), ("Nadia", " française."), ("Je ne", " pas espagnol.")]
    gl5 = [f'<li value="{i+1}">{a} {A(gw[i], "min-width:16mm")}{c}</li>' for i, (a, c) in enumerate(gs)]
    fem = [("italien", "italienne"), ("canadien", "canadienne"), ("portugais", "portugaise"), ("américain", "américaine"), ("espagnol", "espagnole"), ("belge", "belge")]
    fl = [f'<li value="{i+1}">{m} → {A(f, "min-width:28mm")}</li>' for i, (m, f) in enumerate(fem)]
    mt = [("Tu es française ?", "d", "J'ai vingt-deux ans."), ("Tu as quel âge ?", "a", "Oui, je suis étudiant."),
          ("Vous êtes portugaise ?", "c", "Non, je suis brésilienne."), ("Tu es étudiant ?", "b", "Oui, je suis française.")]
    mr = "".join(f'<tr><td>{i+1}. {l} &nbsp;{A(k, "min-width:9mm")}</td><td>{chr(97+i)}) {r}</td></tr>' for i, (l, k, r) in enumerate(mt))
    b.page(f"""{sec(5, "Pratique", "8 min")}
{sub("A", "Complétez : suis, es, est ou êtes ?", "3 min")}
{twocol(gl5, 3)}
{sub("B", "Écrivez la forme féminine.", "2 min")}
{twocol(fl, 3)}
{sub("C", "Reliez.", "3 min")}
<table style="margin:0">{mr}</table>""",
    24, """<ol><li>A : <i>Hugo</i> = il, <i>Nadia</i> = elle → <i>est</i>. <i>es</i> et <i>est</i> ont le même son.</li>
<li>B : l'élève lit chaque paire à voix haute : on entend la différence (sauf <i>belge</i>). C : lisez les paires, l'enseignant pose la question.</li></ol>""")

    # Page 6
    ppl = [("Lucas", "brésilien · 28 ans", "vingt-huit"), ("Sofia", "italienne · 35 ans", "trente-cinq"),
           ("Marie", "belge · 40 ans", "quarante"), ("Diego", "espagnol · 23 ans", "vingt-trois")]
    st = "".join(f'<div class="ad" style="flex:1"><b class="t">{n}</b>{d}<br>{R("→ " + a + " ans")}</div>' for n, d, a in ppl)
    b.page(f"""{sec(6, "Parler", "12 min")}
{sub("A", "Jouez avec l'enseignant. Posez les questions.", "7 min")}
<div style="display:flex;gap:2.5mm;margin:1mm 0 2mm">{st}</div>
<div class="msg"><b>A :</b> Bonjour ! Tu t'appelles comment ?<br><b>B :</b> Je m'appelle Sofia.<br><b>A :</b> Tu es espagnole ?<br><b>B :</b> Non, je ne suis pas espagnole. Je suis italienne.<br><b>A :</b> Tu as quel âge ?<br><b>B :</b> J'ai trente-cinq ans.</div>
{sub("B", "Répondez à l'enseignant.", "5 min")}
<ol style="line-height:1.8"><li>Vous vous appelez comment ?</li><li>Vous êtes français(e) ?</li><li>Vous êtes brésilien(ne) ?</li><li>Vous avez quel âge ?</li></ol>""",
    28, """<ol><li>A : l'enseignant est la personne de la carte ; l'élève pose les questions. Puis on change : l'élève choisit une carte, l'enseignant pose les questions (et se trompe exprès de nationalité pour faire dire <i>Non, je ne suis pas …</i>).</li>
<li>B : réponses complètes : <i>Non, je ne suis pas français(e). Je suis brésilien(ne). J'ai … ans.</i> L'âge est une question personnelle : l'élève peut inventer.</li></ol>""")

    # Page 7
    pc = [("Unité 01", "Je peux saluer et dire mon nom."), ("Unité 02", "Je peux épeler mon nom et compter de 0 à 20."),
          ("Unité 03", "Je peux dire ma nationalité (et ne … pas)."), ("Unité 03", "Je peux dire mon âge et demander l'âge.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("français", "française"), ("italien", "italienne"), ("espagnol", "espagnole"), ("canadien", "canadienne")]
    hl = [f'<li value="{i+1}">{m} → {A(f, "min-width:30mm")}</li>' for i, (m, f) in enumerate(hw)]
    b.page(f"""{sec(7, "Bilan et devoirs", "2 min")}
{sub("A", "Auto-évaluation", "1 min")}
<table class="ck"><tr><th style="width:19mm"></th><th>En français …</th><th style="width:18mm">Facile !</th><th style="width:18mm">Parfois</th><th style="width:18mm">Pas encore</th></tr>{pcr}</table>
{sub("B", "Devoirs", "1 min")}
<p><b>1. Écrivez la forme féminine.</b></p>
{twocol(hl, 2)}
<p style="margin-top:2mm"><b>2. Complétez le dialogue.</b></p>
<div class="msg"><b>Hugo :</b> Tu es portugaise ?<br><b>Vous :</b> {A("Non, je ne suis pas portugaise. Je suis …", "min-width:70mm")}<br><b>Hugo :</b> Tu as quel âge ?<br><b>Vous :</b> {A("J'ai … ans.", "min-width:70mm")}</div>
<p style="margin-top:2mm"><b>3. Présentez-vous en trois phrases.</b> Je m'appelle … Je suis … J'ai … ans.</p>
<div class="wline"></div><div class="wline"></div>""",
    22, """<p>Au prochain cours : l'élève lit sa présentation (devoir 3). Posez des questions : <i>Vous êtes italien(ne) ? Vous avez quel âge ?</i> Dans l'unité 04 : les goûts, <i>J'aime le tennis</i>.</p>""")

    b.extra("Transcriptions", f"""
{sub("03.1", "Tu es espagnole ? (lent et naturel)")}
<p style="line-height:1.6">{"<br>".join(f"<b>{n} :</b> {t}" for n, t in SCRIPT)}</p>
{sub("03.2", "Masculin, féminin")}
<p>{" · ".join(S032)}</p>
{sub("03.3", "Les âges")}
<p>{" · ".join(S033)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essentiel 03 - Et vous")
