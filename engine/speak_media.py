"""Speak! Essentials - media generator (replaces the old Colab notebook).

Usage:
  python3 speak_media.py audio  roteiro.json keys.json REPO_DIR     -> MP3s into REPO_DIR/<unit-key>/, writes audio_<unit-key>.json
  python3 speak_media.py images roteiro.json keys.json OUT_DIR      -> 3 Pixabay candidates per letter + contact sheet

roteiro.json format (same as the old Colab roteiros):
  {"characters": {"Tom": "en-US-Neural2-D", ...},
   "units": {"a1-unit-21": {"21.1 Dialogue": "Tom: Hi!\\nAna: Hello!", "21.2 Repeat words": "Narrator: ..."}},
   "images": {"a1-unit-21": {"A": "search query", ...}}}

keys.json: {"GOOGLE_TTS_KEY": "...", "PIXABAY_KEY": "...", "GITHUB_REPO": "owner/repo"}
Public audio URL: https://<owner>.github.io/<repo>/<unit-key>/<code>-<slow|natural>.mp3
"""
import base64, io, json, os, sys, requests
from pydub import AudioSegment

SPEEDS = {"natural": 1.0, "slow": 0.85}


def tts(key, text, voice, rate):
    def call(inp):
        return requests.post("https://texttospeech.googleapis.com/v1/text:synthesize", params={"key": key},
                             json={"input": inp, "voice": {"languageCode": "-".join(voice.split("-")[:2]), "name": voice},
                                   "audioConfig": {"audioEncoding": "MP3", "sampleRateHertz": 24000, "speakingRate": rate}},
                             timeout=60)
    r = call({"text": text})
    if not r.ok:
        r = call({"ssml": f"<speak>{text.replace('&', 'and')}</speak>"})
    if not r.ok:
        print("WARNING: TTS failed for", repr(text), r.text[:200])
        return AudioSegment.silent(duration=10, frame_rate=24000)
    return AudioSegment.from_file(io.BytesIO(base64.b64decode(r.json()["audioContent"])), format="mp3")


def parse(script, chars):
    out = []
    for line in script.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        name, sep, txt = line.partition(":")
        out.append((name.strip(), txt.strip()) if sep and name.strip() in chars else ("Narrator", line))
    return out


def audio(rot, keys, repo_dir):
    d = json.load(open(rot)); k = json.load(open(keys))
    chars = {"Narrator": "en-US-Neural2-J", **d.get("characters", {})}
    owner, repo = k["GITHUB_REPO"].split("/")
    base = f"https://{owner}.github.io/{repo}"
    for unit, tracks in d.get("units", {}).items():
        folder = os.path.join(repo_dir, unit); os.makedirs(folder, exist_ok=True)
        ids = {}
        for title, script in tracks.items():
            code = title.split()[0]
            pause = AudioSegment.silent(duration=2000 if any(p in title for p in ("Repeat", "Contractions", "Intonation")) else 600, frame_rate=24000)
            for ver, rate in SPEEDS.items():
                dest = os.path.join(folder, f"{code}-{ver}.mp3")
                if not os.path.exists(dest):
                    seg = AudioSegment.silent(duration=300, frame_rate=24000)
                    for name, txt in parse(script, chars):
                        seg += tts(k["GOOGLE_TTS_KEY"], txt, chars[name], rate) + pause
                    seg.set_channels(1).export(dest, format="mp3", bitrate="64k",
                                               tags={"title": f"Speak! Essentials {unit} {title} ({ver})", "artist": "Speak! English School"})
                    print("new", dest, f"{len(seg)/1000:.0f}s")
            # dialogue tracks (first track) get SLOW + NATURAL keys; the others use the natural version
            if title.split()[1:2] == ["Dialogue"] or code.endswith(".1"):
                ids[f"{code} · SLOW"] = f"{base}/{unit}/{code}-slow.mp3"
                ids[f"{code} · NATURAL"] = f"{base}/{unit}/{code}-natural.mp3"
            else:
                ids[code] = f"{base}/{unit}/{code}-natural.mp3"
        json.dump(ids, open(f"audio_{unit}.json", "w"), ensure_ascii=False, indent=1)
        print("wrote", f"audio_{unit}.json")


def images(rot, keys, out):
    from PIL import Image, ImageDraw
    d = json.load(open(rot)); k = json.load(open(keys))
    os.makedirs(out, exist_ok=True)
    for unit, photos in d.get("images", {}).items():
        for letter, q in photos.items():
            r = requests.get("https://pixabay.com/api/", params={"key": k["PIXABAY_KEY"], "q": q, "image_type": "photo",
                             "orientation": "horizontal", "safesearch": "true", "per_page": 3}, timeout=60)
            hits = r.json().get("hits", [])[:3] if r.ok else []
            if not hits:
                print("NO PHOTO for", letter, q)
            for i, h in enumerate(hits, 1):
                open(os.path.join(out, f"{letter}-{i}.jpg"), "wb").write(requests.get(h["largeImageURL"], timeout=60).content)
            print("photos", letter, q, len(hits))
    fs = sorted(f for f in os.listdir(out) if f.endswith(".jpg"))
    W, H = 300, 200
    rows = (len(fs) + 2) // 3
    sh = Image.new("RGB", (W * 3, H * max(rows, 1)), "white"); dr = ImageDraw.Draw(sh)
    for i, f in enumerate(fs):
        im = Image.open(os.path.join(out, f)).convert("RGB"); im.thumbnail((W - 6, H - 6))
        x, y = (i % 3) * W, (i // 3) * H; sh.paste(im, (x, y)); dr.text((x + 4, y + 4), f, fill="red")
    sh.save(os.path.join(out, "_contact_sheet.jpg")); print("sheet", os.path.join(out, "_contact_sheet.jpg"))


if __name__ == "__main__":
    mode, rot, keys, target = sys.argv[1:5]
    (audio if mode == "audio" else images)(rot, keys, target)
