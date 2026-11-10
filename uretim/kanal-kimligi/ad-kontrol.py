#!/usr/bin/env python3
"""Kullanıcı adı müsaitliği: IG (title/og/PolarisErrorRoot), TT (statusCode), YT (Data API forHandle + HTTP)."""
import os, re, subprocess, sys, time, json
KEY = os.environ.get("YOUTUBE_API_KEY", "")
def get(url):
    r = subprocess.run(["curl", "-s", "-o", "-", "-w", "\n__HTTP__%{http_code}", url], capture_output=True, text=True, errors="ignore", timeout=40)
    body, _, code = r.stdout.rpartition("\n__HTTP__")
    return code, body
def ig(u):
    for deneme in range(3):
        code, b = get(f"https://www.instagram.com/{u}/")
        if code == "200":
            if re.search(r'og:title" content="[^"]*\(&#064;' + re.escape(u) + r'\)', b, re.I): return "DOLU"
            if "PolarisErrorRoot" in b and "og:title" not in b: return "BOŞ"
            return "belirsiz(200-tanınmadı)"
        time.sleep(8)
    return f"belirsiz({code})"
def tt(u):
    code, b = get(f"https://www.tiktok.com/@{u}")
    m = re.search(r'"statusCode":(\d+)', b)
    s = m.group(1) if m else None
    if s == "0": return "DOLU"
    if s == "10221": return "BOŞ"
    if s == "10222": return "DOLU(gizli)"
    return f"belirsiz({code},{s})"
def yt(u):
    code, b = get(f"https://www.googleapis.com/youtube/v3/channels?part=id&forHandle=@{u}&key={KEY}")
    try: n = json.loads(b)["pageInfo"]["totalResults"]
    except Exception: return f"belirsiz(api {code})"
    hc, _ = get(f"https://www.youtube.com/@{u}")
    api = "DOLU" if n else "BOŞ"
    web = {"200": "DOLU", "404": "BOŞ"}.get(hc, f"?{hc}")
    return api if api == web else f"belirsiz(api {api}/web {web})"
for u in sys.argv[1:]:
    print(u, "IG=" + ig(u), "YT=" + yt(u), "TT=" + tt(u), sep="\t", flush=True)
    time.sleep(4)
