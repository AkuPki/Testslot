from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Default settings for win probability (admin can adjust)
settings = {
    "win_chance": 50  # Percentage chance to win
}

@app.route('/spin', methods=['GET'])
def spin():
    reels = ['🍒', '🍋', '🍉', '⭐', '🍇']
    result = [random.choice(reels) for _ in range(3)]

    # Determine win/loss based on win_chance
    win = random.randint(1, 100) <= settings["win_chance"]
    if win:
        result = [random.choice(reels)] * 3  # Set all reels to the same for a win

    return jsonify({
        "reels": result,
        "win": win
    })

@app.route('/settings', methods=['POST'])
def update_settings():
    global settings
    data = request.json

    # Update win chance if provided
    if "win_chance" in data:
        win_chance = data["win_chance"]
        if 0 <= win_chance <= 100:
            settings["win_chance"] = win_chance
            return jsonify({"message": "Settings updated successfully!"})
        else:
            return jsonify({"error": "Win chance must be between 0 and 100."}), 400

    return jsonify({"error": "No valid data provided."}), 400

@app.route('/settings', methods=['GET'])
def get_settings():
    return jsonify(settings)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
