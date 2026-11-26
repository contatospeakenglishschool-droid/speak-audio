# Speak! Progresso B1 (italiano) - FORMATO RIDOTTO (approvato 2026-11-19): 5 pagine in classe + 1 a casa.
# Modello: engine/examples/b1unit24_build.py (inglese). Ogni unità passa un dizionario C con i contenuti.
# Pagine: 1 Riscaldamento 7' · 2 Ascolto 12' · 3 Riferimento grammaticale (in classe) 8' · 4 Pratica 10' · 5 Parlare 18' · H Compiti (a casa).
import json, os
from engine_it import *
import grammar_ref_it


def load_script(here, key, t1, t2):
    r = json.load(open(os.path.join(here, "roteiro.json")))["units"][key]
    script = [tuple(x.split(": ", 1)) for x in r[t1].split("\n")]
    script = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in script]
    s2 = [x.split(": ", 1)[1] for x in r[t2].split("\n")]
    return script, s2


def make_build(C, SCRIPT, S2):
    nn = C["nn"]
    lv = C.get("level", "B1")          # B2 Indipendenza reuses this layout (2026-11-25)
    wn = C.get("words", "100–150")
    RD = C.get("reading")              # B2: pagina 2 come LETTURA (articolo con audio), dict(head, kicker, body, page_title)
    p2 = "Lettura" if RD else "Ascolto"

    def build(teacher):
        b = Book(teacher)
        T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec

        def ch(opts, ans):
            return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

        def img(l, w, h):
            return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'

        def lines(n):
            return '<div class="wline"></div>' * n

        def talk(qs, title="PARLIAMONE"):
            return f'<div class="box sand" style="margin-top:1.5mm"><h4>{title}</h4><ol style="margin:0;line-height:1.5;font-size:8.9pt">' + "".join(f"<li>{q}</li>" for q in qs) + "</ol></div>"

        def notes(items):
            return "<ol>" + "".join(f"<li>{x}</li>" for x in items) + "</ol>"

        # ---------- IN CLASSE ----------
        # Pagina 1 - Riscaldamento
        cover = cover_html(T, f"LIVELLO {lv} · UNITÀ {nn}", C["title"], C["subtitle"], C["cover"])
        kw = C["kw"]
        kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:22mm")}</li>' for i, (d, w) in enumerate(kw)]
        bank = " · ".join(sorted((w for _, w in kw), key=lambda w: w.lower().lstrip("l'").replace("un ", "").replace("una ", "").replace("il ", "").replace("la ", "")))
        b.page(f"""{sec(1, "Riscaldamento: " + C["t1"], "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(C["start"], "PER COMINCIARE")}</div></div>
{sub("A", "Parole chiave. Scrivi le parole del riquadro accanto alle definizioni.", "3 min")}
<div class="bank">{bank}</div>
<div style="font-size:8.7pt">{twocol(kwl, 3)}</div>
{talk(C["use_words"], "USA LE PAROLE")}""",
        26, notes(["Per cominciare: 4 minuti di conversazione libera, non è un test. Annotare gli errori per la conclusione orale."] + C["n1"]), cover=cover)

        rows = [("1 Riscaldamento", "classe", "7 min", "Conversazione · 6 parole chiave · domande con le parole", "1"),
                (f"2 {p2}", "classe", "12 min", C["aims"][0], "2"),
                ("3 Riferimento grammaticale", "classe", "8 min", C["aims"][1] + " (spiegare con gli esempi del dialogo)", "3"),
                ("4 Pratica", "classe", "10 min", "Completa, scegli · Usalo (a voce)", "4"),
                ("5 Parlare", "classe", "18 min", C["aims"][2], "5"),
                ("Conclusione", "classe", "3 min", "Due correzioni dagli appunti · domanda «So fare»", "–"),
                ("Compiti", "casa", "–", C["aims"][3], "6")]
        rws = "".join(f"<tr><td>{a}</td><td>{d}</td><td>{t}</td><td>{o}</td><td>{p}</td></tr>" for a, d, t, o, p in rows)
        b.extra("Panoramica della lezione · 55–60 min", f"""
<table><tr><th>Fase</th><th>Dove</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>{rws}</table>
<div class="box"><h4>IL FORMATO {lv}</h4>Le lezioni {lv} hanno <b>5 pagine per la classe</b> (riscaldamento, {p2.lower()}, riferimento grammaticale, pratica, parlare) e <b>1 pagina per casa</b> (compiti). Ogni pagina della classe finisce con un riquadro di domande: lo studente parla per la maggior parte del tempo. La pratica in più, la scelta delle parole e la scrittura sono a casa. All'inizio della lezione successiva si controllano i compiti in 3–5 minuti.</div>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>{C["story"]}</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>{C["prob"]}</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>{C["real"]}</div>
<div class="box"><h4>AUDIO</h4>Traccia {nn}.1 {C["tr"][0]} ({"il testo della lettura, " if RD else ""}naturale e lenta) · Traccia {nn}.2 {C["tr"][1]}</div>""")

        # Pagina 2 - Ascolto
        gq, gopts = C["gist"]
        kind, dinstr, ditems = C["detail"]
        if kind == "vf":
            det = "<table style='margin:0;font-size:8.8pt'>" + "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(ditems)) + "</table>"
        else:
            det = "<ol style='line-height:1.55;font-size:8.8pt;margin:0'>" + "".join(f"<li>{s} {A(a, 'min-width:16mm')}</li>" for s, a in ditems) + "</ol>"
        if RD:
            b.page(f"""{sec(2, "Lettura: " + C["tr"][0], "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", gq, "2 min", f"{nn}.1")}
<p style="margin:.3mm 0;font-size:8.9pt">{ch(gopts, gopts[0])}</p>
{audiocard([f"{nn}.1 · NATURAL", f"{nn}.1 · SLOW"])}</div>{img('B', 40, 27)}</div>
<div class="box" style="background:#fbfaf6;border-left:3px solid #176074;margin:1mm 0;padding:2mm 3mm">
<p style="margin:0;font-size:7pt;letter-spacing:.08em;color:#176074"><b>{RD["kicker"]}</b></p>
<p style="margin:.3mm 0 1mm;font-size:12pt;line-height:1.15"><b>{RD["head"]}</b></p>
<div style="columns:2;column-gap:5mm;font-size:8.5pt;line-height:1.38;text-align:justify">{RD["body"]}</div></div>
{sub("B", dinstr, "4 min")}
{det}
{talk(C["talk2"])}""",
            29, notes(["A: 2 minuti di lettura veloce, solo per l'idea generale. B: 5 minuti; poi l'audio come modello (naturale; la lenta per la pronuncia). " + C["n2"][0]] + C["n2"][1:] + ["Parliamone: 5 minuti; prendere il punto di vista opposto per far parlare di più lo studente."]))
        else:
            b.page(f"""{sec(2, "Ascolto: " + C["tr"][0], "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{audiocard([f"{nn}.1 · NATURAL", f"{nn}.1 · SLOW"])}
{sub("A", gq, "2 min", f"{nn}.1")}
<p style="margin:.3mm 0;font-size:8.9pt">{ch(gopts, gopts[0])}</p></div>{img('B', 40, 27)}</div>
{sub("B", dinstr, "4 min")}
{det}
{talk(C["talk2"])}""",
            29, notes(["A–B: 6 minuti. Prima la versione naturale; la lenta solo se serve. " + C["n2"][0]] + C["n2"][1:] + ["Parliamone: 6 minuti; prendere il punto di vista opposto per far parlare di più lo studente."]))

        # Pagina 3 - Riferimento grammaticale (in classe)
        _sec = b.sec
        b.sec = lambda n, t, tm="": _sec(3, t, "8 min") if n == "+" else _sec(n, t, tm)
        getattr(grammar_ref_it, C["gref"])(b)
        b.sec = _sec

        # Pagina 4 - Pratica
        pinstr, pitems = C["pA"]
        pal = "".join(f"<li><i>{s.replace('___', A(a, 'min-width:' + C.get('pAw', '22mm')))}</i></li>" for s, a in pitems)
        pbl = "".join(f"<li>{a}{ch(o, r)}{z}</li>" for a, o, r, z in C["pB"])
        b.page(f"""{sec(4, "Pratica: " + C["t4"], "10 min")}
{sub("A", pinstr, "3 min")}
<ol style="line-height:1.85;font-size:8.9pt;margin:0">{pal}</ol>
{sub("B", "Scegli.", "2 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0">{pbl}</ol>
<div class="box sand"><h4>REGOLA</h4>{C["rule"]} Vedi il <b>Riferimento grammaticale</b> alla pagina 3.</div>
{talk(C["use"], "USALO: RISPONDI A VOCE")}""",
        29, notes(["A–B: 4 minuti. Lo studente ha appena visto il riferimento grammaticale (pagina 3): controllare la forma dopo ogni frase. " + C["n4"],
                   "Usalo: 6 minuti, tutto a voce. Accettare ogni idea logica; correggere solo la struttura e chiedere sempre una seconda frase."]))

        # Pagina 5 - Parlare
        heads, cells = C["fl"]
        th = "".join(f"<th>{h}</th>" for h in heads)
        td = "".join(f"<td><i>{c}</i></td>" for c in cells)
        tinstr, tbody, tred = C["task"]
        b.page(f"""{sec(5, "Parlare: " + C["t5"], "18 min")}
<div class="box sand" style="margin-top:0"><h4>LINGUA PER COMUNICARE</h4>
<table style="margin:0;font-size:8.3pt"><tr>{th}</tr><tr>{td}</tr></table></div>
<p class="small" style="margin:.8mm 0 .3mm">{C["pron"][0]}</p>
{audiocard([f"{nn}.2"])}
{sub("A", C["pron"][1], "4 min", f"{nn}.2")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S2))}</p>
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("B", tinstr, "12 min")}
{tbody}
<p style="margin:.5mm 0;font-size:8.6pt">{R(tred) if T else ""}</p></div>{img('D', 34, 24)}</div>
{talk(C["talk5"])}""",
        32, notes(["A: " + C["n5"][0], "B: 10 minuti. " + C["n5"][1] + " Ultimi 3 minuti: conclusione orale (due correzioni dagli appunti e la domanda «So fare»)."]))

        # ---------- A CASA ----------
        hinstr, htext, hgaps = C["hA"]
        p = [ch(o, a) for o, a in hgaps]
        rwl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in C["hB"][1])
        wl = "".join(f"<tr><td>{a}</td><td><b>{d}</b></td><td>{w}</td></tr>" for a, d, w in C["watch"])
        winstr, wstart, wcheck = C["write"]
        b.page(f"""{sec("H", "Compiti", "a casa")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", hinstr, "")}</div>{img('C', 28, 18)}</div>
<div class="box" style="line-height:1.8;font-size:8.7pt;margin:.5mm 0">{htext.format(*p)}</div>
{sub("B", C["hB"][0], "")}
<ol style="line-height:1.45;font-size:8.7pt;margin:0">{rwl}</ol>
<div class="box sand" style="margin:1mm 0"><h4>ATTENZIONE: SCELTA DELLE PAROLE</h4>
<table style="margin:0;font-size:8.1pt"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>{wl}</table></div>
{sub("C", f"Scrittura ({wn} parole, sul quaderno). " + winstr, "")}
<p class="small" style="margin:.3mm 0"><b>Comincia così:</b> <i>{wstart}</i> &nbsp;{" &nbsp;".join("☐ " + x for x in wcheck)} &nbsp;☐ {wn} parole</p>
<p class="small" style="margin:.3mm 0"><b>So fare:</b> {C["cando"]} ☐ Facile! ☐ A volte ☐ Non ancora</p>""",
        20, f"<p>Controllare A e B in 3 minuti all'inizio della lezione successiva. Leggere la scrittura a casa e scegliere due errori da discutere in classe. {C.get('nH', '')}</p>")

        b.extra("Trascrizioni audio", f"""
{sub(f"{nn}.1", C["tr"][0] + " (naturale e lenta)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub(f"{nn}.2", C["tr"][1])}
<p>{" · ".join(S2)}</p>""")
        return b.html()

    return build
