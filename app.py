# app.py
from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_doors', methods=['POST'])
def generate_doors():
    num_doors = int(request.form['num_doors'])
    winner = random.randint(0, num_doors - 1)
    return jsonify({'num_doors': num_doors, 'winner': winner})

@app.route('/reveal_goat', methods=['POST'])
def reveal_goat():
    data = request.get_json()
    num_doors = data['num_doors']
    chosen_door = data['chosen_door']
    winner = data['winner']

    if chosen_door == winner:
        goat_doors = [i for i in range(num_doors) if i != winner]
        revealed_goats = random.sample(goat_doors, num_doors - 2)
    else:
        goat_doors = [i for i in range(num_doors) if i != winner and i != chosen_door]
        revealed_goats = goat_doors

    return jsonify({'revealed_goats': revealed_goats})

if __name__ == '__main__':
    app.run(debug=True)
