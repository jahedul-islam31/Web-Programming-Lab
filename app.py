from flask import Flask, send_from_directory

app = Flask(__name__, static_folder=".", static_url_path="")

# Serve index.html
@app.route("/")
def home():
    return send_from_directory(".", "index5_e251031.html")

if __name__ == "__main__":
    # '0.0.0.0' makes server visible to others in sam LAN.
    app.run(host="0.0.0.0", port=5031, debug=False)