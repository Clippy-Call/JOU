from flask import Flask, jsonify

app = Flask(__name__, static_folder="static")

@app.route("/")
def home():
    return app.send_static_file("index.html")

@app.route("/api/videos")
def get_videos():
    videos = [
        {
            "title": "Discarded EP 1 Ft.AakashGupta_AnubhavSinghBassi",
            "url": "https://rumble.com/embed/v6bgd64/?pub=y5av6"
        },
        {
            "title": "Ft.SeedheMaut_Madhurvirli",
            "url": "https://rumble.com/embed/v64u80d/?pub=y5av6"
        },
        {
            "title": "Ft.AvikaGor",
            "url": "https://rumble.com/embed/v64ucrm/?pub=y5av6"
        },
        {
            "title": "Ft.ArpitBala BonusContent",
            "url": "https://rumble.com/embed/v64ujhp/?pub=y5av6"
        },
        {
            "title": "Ft.Badshad_SiddhantChaturvedi",
            "url": "https://rumble.com/embed/v64umz4/?pub=y5av6"
        },
        {
            "title": "Ft.Rohanjoshi_SahilShah",
            "url": "https://rumble.com/embed/v64utxj/?pub=y5av6"
        }
    ]
    return jsonify(videos)

