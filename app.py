from flask import Flask, render_template, send_from_directory, abort, request
import os

app = Flask(__name__)
FLAG = os.environ.get("CTF_FLAG", "CYBERWOLF{dh_small_subgroup_exposed}")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download/<path:name>")
def download(name):
    allowed = {"exchange_capture.txt", "protected_message.bin", "README.txt"}
    if name not in allowed:
        abort(404)
    return send_from_directory("challenge_files", name, as_attachment=True)

@app.route("/health")
def health():
    return {"status": "online", "challenge": "042"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
