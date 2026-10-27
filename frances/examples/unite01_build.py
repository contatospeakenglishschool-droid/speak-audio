# Speak! Essentiel A1 - Unité 01 "Bonjour !" (tout en français, pour vrais débutants) - built with the shared engine + French layer
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_fr import *
setup(band="A1 · UNITÉ 01", audio_json=os.path.join(HERE, "audio_fr-a1-unite-01.json"), img_dir=os.path.join(HERE, "img"), lang="fr-FR")

PHOTOS = [("A", "Bonjour !", "bonjour"), ("B", "Salut !", "salut"), ("C", "Bonsoir !", "bonsoir"), ("D", "Bonne nuit !", "bonne nuit"),
          ("E", "Au revoir !", "au revoir"), ("F", "À demain !", "à demain"), ("G", "À bientôt !", "à bientôt"), ("H", "Enchanté !", "enchanté")]

SCRIPT = [("Narratrice", "Dialogue un."), ("Madame Lefèvre", "Bonjour ! Je suis Madame Lefèvre. Vous vous appelez comment ?"),
          ("Camila", "Bonjour, madame ! Je m'appelle Camila Souza."), ("Madame Lefèvre", "Enchantée, madame Souza."), ("Camila", "Enchantée !"),
          ("Narratrice", "Dialogue deux."), ("Thomas", "Salut ! Je m'appelle Thomas. Tu t'appelles comment ?"), ("Camila", "Salut, Thomas ! Je suis Camila."),
          ("Thomas", "Enchanté, Camila !"), ("Camila", "Enchantée !"),
          ("Narratrice", "Dialogue trois."), ("Nadia", "Bonsoir !"), ("Camila", "Bonsoir ! Je suis Camila."),
          ("Nadia", "Salut, Camila ! Je m'appelle Nadia. Enchantée !"), ("Camila", "Enchantée ! Au revoir, Nadia !"), ("Nadia", "Au revoir ! À demain !")]
S012 = ["Bonjour", "Salut", "Bonsoir", "Bonne nuit", "Au revoir", "À demain", "À bientôt", "Enchanté"]
S013 = ["Je m'appelle Camila.", "Je suis Thomas.", "Tu t'appelles comment ?", "Vous vous appelez comment ?", "Enchanté !", "Enchantée !"]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "NIVEAU A1 · UNITÉ 01", "Bonjour !", "Saluer et dire son nom",
                       [("VOUS POUVEZ", "dire bonjour, dire votre nom et demander le nom"),
                        ("LANGUE", "Je m'appelle … · Je suis … · Tu t'appelles comment ? · Vous vous appelez comment ?"),
                        ("PRONONCIATION", "Les salutations · on · ou · lettres finales muettes")])
    words = ["À bientôt !", "À demain !", "Au revoir !", "Bonjour !", "Bonne nuit !", "Bonsoir !", "Enchanté !", "Salut !"]
    qs = [("09:00", "Bonjour !"), ("15:00", "Bonjour !"), ("20:00", "Bonsoir !"), ("23:00", "Bonne nuit !")]
    cl = "".join(f'<td style="width:25%;text-align:center"><b style="font-size:13pt">{t}</b><br>{A(a, "min-width:30mm")}</td>' for t, a in qs)
    b.page(f"""{sec(1, "Échauffement : Bonjour !", "8 min")}
{sub("A", "Écoutez et répétez. Écrivez.", "5 min", "01.2")}
<div class="bank">{" &nbsp;·&nbsp; ".join(words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Quelle heure est-il ? Écrivez.", "3 min")}
<table class="ck"><tr>{cl}</tr></table>""",
    30, """<ol><li>A : piste 01.2. Montrez chaque photo, faites écouter le mot, l'élève répète et écrit. Lentement, avec des gestes (lever la main, serrer la main). Répétez beaucoup.</li>
<li>B : montrez une horloge. En France, on dit <b>Bonjour</b> toute la journée, le matin et l'après-midi. Le soir (à partir de 18 h environ) : <b>Bonsoir</b>. <b>Bonne nuit</b> seulement avant de dormir. <b>Salut</b> = informel (pour arriver et pour partir), <b>Bonjour / Au revoir</b> = pour tout le monde.</li></ol>""", cover=cover)

    b.extra("Déroulement de la leçon · 55 min", """
<table><tr><th>Étape</th><th>Durée</th><th>Objectif</th><th>Page</th></tr>
<tr><td>1 Échauffement</td><td>8 min</td><td>8 salutations avec photos et heures</td><td>1</td></tr>
<tr><td>2 Écoute</td><td>10 min</td><td>Camila à Lyon : trois petits dialogues</td><td>2</td></tr>
<tr><td>3 Grammaire</td><td>10 min</td><td><i>Je m'appelle … / Je suis …</i> · <i>Tu t'appelles comment ? / Vous vous appelez comment ?</i></td><td>3–4</td></tr>
<tr><td>4 Labo de prononciation</td><td>5 min</td><td>Répéter des phrases · on · ou · lettres muettes</td><td>4</td></tr>
<tr><td>5 Pratique</td><td>8 min</td><td>Compléter, mettre en ordre, relier</td><td>5</td></tr>
<tr><td>6 Parler</td><td>12 min</td><td>Saluer quatre personnes · questions de l'enseignant</td><td>6</td></tr>
<tr><td>7 Bilan</td><td>2 min</td><td>Auto-évaluation et devoirs</td><td>7</td></tr></table>
<div class="box"><h4>COMMENT UTILISER CE GUIDE</h4>Chaque page correspond à la page du livre de l'élève avec le même numéro. Vos notes sont dans l'<b>encadré jaune</b>.
<span class="red">Les réponses en rouge</span> ne sont pas dans le livre de l'élève. Les étiquettes <span class="time">5 min</span> indiquent la durée de chaque activité. Les transcriptions sont à la dernière page.</div>
<div class="box"><h4>PREMIER COURS : LENTEMENT !</h4>L'élève n'a jamais entendu de français. Parlez lentement, montrez beaucoup (photos, gestes, horloge) et répétez souvent chaque structure. Les consignes sont courtes et reviennent toujours : <i>Écoutez. Répétez. Écrivez. Complétez. Reliez.</i> L'enseignant les lit et montre ce qu'il faut faire. Objectif du cours : saluer, dire son nom et demander le nom. Rien de plus.</div>
<div class="box sand"><h4>L'HISTOIRE COMMENCE</h4>Camila Souza est graphiste. Elle vient de Recife et elle habite maintenant à Lyon. Le matin, elle rencontre sa propriétaire, Madame Lefèvre (vous). À l'agence, elle rencontre Thomas, un collègue (tu). Le soir, au café, elle rencontre Nadia.</div>
<div class="box"><h4>LE PROBLÈME POUR LES BRÉSILIENS</h4><i>Suis Camila</i> ✗ → <b>Je suis Camila</b> : en français, le <i>je</i> est toujours là. <i>Me appelle Camila</i> ✗ → <b>Je m'appelle Camila</b>. Il n'y a pas de « boa tarde » : l'après-midi, on dit <b>Bonjour</b>. Et avec <i>Madame / Monsieur</i>, on dit <b>vous</b>.</div>
<div class="box"><h4>AUDIO</h4>Piste 01.1 Trois dialogues (lent et naturel) · Piste 01.2 Les salutations · Piste 01.3 Les phrases</div>""")

    # Page 2
    gr = [("1", "Camila et Madame Lefèvre", ["Salut !", "Bonjour !"], "Bonjour !"), ("2", "Camila et Thomas", ["Salut !", "Bonsoir !"], "Salut !"),
          ("3", "Camila et Nadia", ["Bonjour !", "Bonsoir !"], "Bonsoir !")]
    wr = "".join(f'<td style="width:33%"><b>Dialogue {n}</b><br><span class="small">{p}</span><br>{ch(o, a)}</td>' for n, p, o, a in gr)
    gp = [("Je", "suis", " Madame Lefèvre."), ("Vous vous", "appelez", " comment ?"), ("Je", "m'appelle", " Camila Souza."),
          ("Tu", "t'appelles", " comment ?"), ("", "Enchanté", ", Camila !"), ("", "Au revoir", ", Nadia !")]
    gl = [f'<li value="{i+1}">{a} {A(x, "min-width:20mm")}{c}</li>' for i, (a, x, c) in enumerate(gp)]
    b.page(f"""{sec(2, "Écoute : Camila à Lyon", "10 min")}
<p>Voici Camila. Elle est brésilienne. Elle habite à Lyon.</p>
{audiocard(["01.1 · SLOW", "01.1 · NATURAL"])}
{sub("A", "Écoutez. Choisissez.", "3 min", "01.1 · SLOW")}
<table class="ck"><tr>{wr}</tr></table>
{sub("B", "Écoutez encore. Complétez.", "5 min", "01.1 · NATURAL")}
<div class="bank">appelez · Au revoir · Enchanté · m'appelle · suis · t'appelles</div>
{twocol(gl, 3)}
{sub("C", "Lisez les dialogues avec l'enseignant.", "2 min")}""",
    30, """<ol><li>A : version <b>lente</b>, deux écoutes. Avant l'écoute, montrez trois photos de la page 1 (A, B, C) : le matin, le bureau, le soir.</li>
<li>B : version <b>naturelle</b>. Les mots sont dans l'encadré. Faites une pause après chaque dialogue.</li>
<li>C : les dialogues sont à la dernière page du guide. L'enseignant lit, l'élève est Camila. Puis on change.</li></ol>""")

    # Page 3
    who = [("Thomas", "collègue", "Tu t'appelles comment ?"), ("Madame Lefèvre", "propriétaire", "Vous vous appelez comment ?"),
           ("Hugo", "voisin, 22 ans", "Tu t'appelles comment ?"), ("Monsieur Martin", "médecin", "Vous vous appelez comment ?")]
    wt = "".join(f'<td style="width:25%"><b>{n}</b><br><span class="small">{d}</span><br>{ch(["Tu t'appelles comment ?", "Vous vous appelez comment ?"], a)}</td>' for n, d, a in who)
    b.page(f"""{sec(3, "Grammaire : Je m'appelle … / Tu t'appelles comment ?", "10 min")}
{sub("A", "Lisez.", "3 min")}
<div class="two"><div><table style="margin:0"><tr><th colspan="2">Mon nom</th></tr>
<tr><td>Je <b>m'appelle</b> Camila.</td><td>Je <b>suis</b> Camila.</td></tr>
<tr><td>Je <b>m'appelle</b> Thomas.</td><td>Je <b>suis</b> Thomas.</td></tr></table></div>
<div><table style="margin:0"><tr><th colspan="2">La question</th></tr>
<tr><td><b>tu</b></td><td><b>Tu t'appelles</b> comment ?</td></tr>
<tr><td><b>vous</b></td><td><b>Vous vous appelez</b> comment ?</td></tr></table></div></div>
<div class="box"><h4>TU OU VOUS ?</h4><b>tu</b> = amis, collègues, jeunes. &nbsp; <b>vous</b> = Madame …, Monsieur … &nbsp; <b>Enchanté</b> (homme) · <b>Enchantée</b> (femme) : même son !</div>
{sub("B", "Tu ou vous ? Choisissez la question.", "4 min")}
<table class="ck"><tr>{wt}</tr></table>
{sub("C", "Écrivez votre nom.", "3 min")}
<div class="two"><div class="wline">Je m'appelle {R("…")}</div><div class="wline">Je suis {R("…")}</div></div>""",
    32, """<ol><li>A : <i>Je m'appelle …</i> et <i>Je suis …</i> ont ici le même sens. On travaille seulement ces deux formes et les deux questions, pas toute la conjugaison (elle vient plus tard). L'élève lit à voix haute.</li>
<li>B : montrez avec des gestes : ami = tu, Madame / Monsieur = vous. Hugo : jeune, voisin → tu.</li>
<li>C : l'élève dit son nom à voix haute : <i>Je m'appelle …</i> Si l'élève est une femme : <i>Enchantée</i> à l'écrit.</li></ol>""")

    # Page 4
    b.page(f"""{sub("D", "Erreurs fréquentes", "2 min")}
<div class="box sand"><h4>ATTENTION : ERREURS FRÉQUENTES</h4>
<table style="margin:0"><tr><th>Ne dites pas</th><th>Dites</th></tr>
<tr><td>Suis Camila.</td><td><b>Je suis Camila.</b></td></tr>
<tr><td>Me appelle Camila.</td><td><b>Je m'appelle Camila.</b></td></tr>
<tr><td>Tu t'appelles comment, Monsieur Martin ?</td><td><b>Vous vous appelez comment, Monsieur ?</b></td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Labo de prononciation", "5 min")}
{audiocard(["01.2", "01.3"])}
{sub("A", "Écoutez et répétez.", "2 min", "01.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S012)}</div>
{sub("B", "Écoutez et répétez.", "3 min", "01.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S013)}</div>
<div class="box"><h4>LES SONS</h4><b>on</b> : <i>b<b>on</b>jour, b<b>on</b>soir, comm<b>en</b>t</i> (le son sort par le nez) &nbsp;·&nbsp; <b>ou</b> = [u] : <i>bonj<b>ou</b>r, v<b>ou</b>s</i> &nbsp;·&nbsp; lettres finales muettes : <i>salu<s>t</s>, commen<s>t</s>, vou<s>s</s></i></div>""",
    36, """<ol><li>Erreurs : <i>Suis Camila</i> est l'erreur la plus fréquente (en portugais, on dit « Sou Camila » sans sujet). Corrigez gentiment, la main sur la poitrine : <i>JE suis …</i> <i>Me appelle</i> vient de « Me chamo » : en français, toujours <i>je</i> devant.</li>
<li>4A/4B : chaque mot deux fois. Le <b>on</b> est nasal, comme « bom » en portugais, mais sans fermer la bouche à la fin. <b>ou</b> = le « u » portugais. Les lettres finales barrées ne se prononcent pas : <i>salut</i> = « salu ». Montrez, ne l'expliquez pas en détail.</li></ol>""")

    # Page 5
    gw = ["m'appelle", "suis", "t'appelles", "appelez", "suis", "m'appelle"]
    gs = [("Je", "Thomas."), ("Je", "Camila."), ("Tu", "comment ?"), ("Vous vous", "comment ?"), ("Je", "Madame Lefèvre."), ("Bonsoir ! Je", "Nadia.")]
    gl5 = [f'<li value="{i+1}">{a} {A(gw[i], "min-width:20mm")} {c}</li>' for i, (a, c) in enumerate(gs)]
    od = [("m'appelle / je / Hugo", "Je m'appelle Hugo."), ("comment / t'appelles / tu / ?", "Tu t'appelles comment ?"), ("vous / comment / appelez / vous / ?", "Vous vous appelez comment ?")]
    ol5 = "".join(f'<li>{s}<div class="wline">{R(a)}</div></li>' for s, a in od)
    mt = [("Bonjour !", "c", "Je m'appelle Hugo."), ("Tu t'appelles comment ?", "a", "Enchantée !"), ("Enchanté !", "b", "Bonjour !"), ("Au revoir !", "d", "Au revoir !")]
    mr = "".join(f'<tr><td>{i+1}. {l} &nbsp;{A(k, "min-width:9mm")}</td><td>{chr(97+i)}) {r}</td></tr>' for i, (l, k, r) in enumerate(mt))
    b.page(f"""{sec(5, "Pratique", "8 min")}
{sub("A", "Complétez.", "3 min")}
<div class="bank">appelez · m'appelle · m'appelle · suis · suis · t'appelles</div>
{twocol(gl5, 3)}
{sub("B", "Mettez dans l'ordre.", "2 min")}
<ol>{ol5}</ol>
{sub("C", "Reliez.", "3 min")}
<table style="margin:0">{mr}</table>""",
    24, """<ol><li>A : en 1, 2, 5 et 6, <i>m'appelle</i> et <i>suis</i> sont corrects : acceptez les deux.</li>
<li>B : montrez que la question finit par <i>comment ?</i> C : lisez les paires à voix haute, l'enseignant joue la première personne.</li></ol>""")

    # Page 6
    ppl = [("Thomas", "collègue · 9 h", "tu · Salut ! / Bonjour !"), ("Madame Lefèvre", "propriétaire · 8 h", "vous · Bonjour, madame !"),
           ("Hugo", "voisin · 20 h", "tu · Salut ! / Bonsoir !"), ("Monsieur Martin", "médecin · 15 h", "vous · Bonjour, monsieur !")]
    st = "".join(f'<div class="ad" style="flex:1"><b class="t">{n}</b>{d}<br>{R("→ " + a)}</div>' for n, d, a in ppl)
    b.page(f"""{sec(6, "Parler", "12 min")}
{sub("A", "Jouez avec l'enseignant. Saluez la personne. Dites votre nom. Demandez le nom.", "7 min")}
<div style="display:flex;gap:2.5mm;margin:1mm 0 2mm">{st}</div>
<div class="bank" style="background:#fff">Bonjour ! / Salut ! / Bonsoir ! · Je m'appelle … · Tu t'appelles comment ? / Vous vous appelez comment ? · Enchanté(e) ! · Au revoir ! / À demain !</div>
<div class="msg"><b>A :</b> Bonjour ! Je m'appelle … Vous vous appelez comment ?<br><b>B :</b> Bonjour ! Je suis … <br><b>A :</b> Enchanté(e) !<br><b>B :</b> Enchanté(e) ! … Au revoir !</div>
{sub("B", "Répondez à l'enseignant.", "5 min")}
<ol style="line-height:1.8"><li>Salut ! Tu t'appelles comment ?</li><li>Bonjour ! Vous vous appelez comment ?</li><li>Enchanté !</li><li>Au revoir !</li></ol>""",
    28, """<ol><li>A : l'enseignant joue les quatre personnes (avec une carte ou une photo). L'élève suit le modèle de l'encadré. Puis on change : l'élève est Madame Lefèvre, l'enseignant est Camila.</li>
<li>B : l'enseignant pose la question, l'élève répond librement. Réponses attendues : <i>Je m'appelle … · Enchanté(e) ! · Au revoir !</i> Corrigez tout de suite les erreurs comme <i>Suis …</i></li></ol>""")

    # Page 7
    pc = [("Unité 01", "Je peux dire bonjour (le matin, l'après-midi, le soir)."), ("Unité 01", "Je peux dire mon nom."),
          ("Unité 01", "Je peux demander le nom (tu et vous).")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("08:00", "Bonjour !"), ("16:00", "Bonjour !"), ("21:00", "Bonsoir !"), ("23:30", "Bonne nuit !")]
    hl = [f'<li value="{i+1}"><b>{t}</b> {A(a, "min-width:32mm")}</li>' for i, (t, a) in enumerate(hw)]
    b.page(f"""{sec(7, "Bilan et devoirs", "2 min")}
{sub("A", "Auto-évaluation", "1 min")}
<table class="ck"><tr><th style="width:19mm"></th><th>En français …</th><th style="width:18mm">Facile !</th><th style="width:18mm">Parfois</th><th style="width:18mm">Pas encore</th></tr>{pcr}</table>
{sub("B", "Devoirs", "1 min")}
<p><b>1. Écrivez la salutation.</b></p>
{twocol(hl, 3)}
<p style="margin-top:2mm"><b>2. Complétez le dialogue.</b></p>
<div class="msg"><b>A :</b> Salut ! Je m'appelle Thomas. Tu t'appelles comment ?<br><b>B :</b> {A("Salut ! Je m'appelle …", "min-width:60mm")}<br><b>A :</b> Enchanté !<br><b>B :</b> {A("Enchanté(e) !", "min-width:60mm")}<br><b>A :</b> Au revoir !<br><b>B :</b> {A("Au revoir ! / À demain !", "min-width:60mm")}</div>
<p style="margin-top:2mm"><b>3. Écrivez.</b> Je m'appelle … <div class="wline"></div></p>""",
    22, """<p>Au prochain cours : lisez les devoirs à voix haute. Commencez par une salutation (<i>Bonjour ! / Bonsoir !</i>) et demandez à l'élève : <i>Tu t'appelles comment ?</i> Dans l'unité 02 : l'alphabet, les nombres de 0 à 20 et les phrases utiles de la classe (<i>Pardon ? Je ne comprends pas.</i>).</p>""")

    b.extra("Transcriptions", f"""
{sub("01.1", "Camila à Lyon (lent et naturel)")}
<p style="line-height:1.6">{"<br>".join(f"<b>{n} :</b> {t}" for n, t in SCRIPT)}</p>
{sub("01.2", "Les salutations")}
<p>{" · ".join(S012)}</p>
{sub("01.3", "Les phrases")}
<p>{" · ".join(S013)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essentiel 01 - Bonjour")
