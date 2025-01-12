
from flask import Flask, request, jsonify
from services.url_shortner import UrlShortner

app = Flask(__name__)

@app.route('/shortner', methods=['POST'])
def url_shortner():
    data = request.get_json()
    original_url = data.get("original_url")

    url_shortner = UrlShortner()

    short_url = url_shortner.url_shortner(original_url)
    return jsonify({"short_url": short_url}), 201

if __name__ == '__main__':
    app.run(debug=True)