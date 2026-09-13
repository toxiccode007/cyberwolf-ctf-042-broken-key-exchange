from flask import Flask, Response, abort, send_from_directory
import os

app = Flask(__name__)
FLAG = os.environ.get("CTF_FLAG", "CYBERWOLF{dh_small_subgroup_exposed}")

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>CTF 042 - The Broken Key Exchange</title>
<style>
body{margin:0;background:#070b12;color:#dce8f5;font-family:Arial,sans-serif}.wrap{max-width:900px;margin:70px auto;padding:0 24px}.badge{color:#35c7ff;font-weight:700;letter-spacing:2px}.panel{margin:28px 0;padding:24px;background:#0d1420;border:1px solid #1e3a52;border-radius:12px}.downloads{display:grid;gap:12px}.downloads a{display:block;padding:15px 18px;background:#101c2b;border:1px solid #24506d;border-radius:8px;color:#6ed7ff;text-decoration:none}.downloads a:hover{border-color:#6ed7ff}.note{color:#9db0c2}footer{margin-top:35px;color:#71869a}
</style>
</head>
<body><main class="wrap">
<div class="badge">CYBERWOLF LABS - CTF 042</div>
<h1>The Broken Key Exchange</h1>
<p>A legacy Diffie-Hellman service was captured during an internal security review.</p>
<section class="panel"><h2>Mission</h2>
<p>The exchange claims to use large-group Diffie-Hellman, but the implementation accepts peer public values without validating their subgroup. Analyze the supplied transcript, recover the secret exponent, and decrypt the protected message.</p>
<p class="note">No brute force of the full private key is required. The weakness is mathematical.</p></section>
<section class="downloads">
<a href="/download/exchange_capture.txt">Download exchange_capture.txt</a>
<a href="/download/protected_message.bin">Download protected_message.bin</a>
<a href="/download/README.txt">Download README.txt</a>
</section>
<footer>Category: CRYPTO - Difficulty: HARD - 400 points</footer>
</main></body></html>"""

@app.get("/")
def index():
    return Response(PAGE, mimetype="text/html")

@app.get("/download/<path:name>")
def download(name):
    allowed = {"exchange_capture.txt", "protected_message.bin", "README.txt"}
    if name not in allowed:
        abort(404)
    return send_from_directory(os.path.join(app.root_path, "challenge_files"), name, as_attachment=True)

@app.get("/health")
def health():
    return {"status": "online", "challenge": "042"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")))
