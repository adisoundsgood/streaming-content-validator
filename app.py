from flask import Flask, jsonify

app = Flask(__name__)

# Sample data for streaming content
content = [
    {"id": 1, "title": "The Mandalorian", "genre": "Sci-Fi", "episodes": 16},
    {"id": 2, "title": "WandaVision", "genre": "Superhero", "episodes": 9},
    {"id": 3, "title": "The Last Dance", "genre": "Sports Documentary", "episodes": 10},
]

@app.route('/api/content', methods=['GET'])
def get_content():
    return jsonify(content)

if __name__ == '__main__':
    app.run(debug=True)