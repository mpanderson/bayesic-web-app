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



@app.route('/simulate', methods=['POST'])
def simulate():
    data = request.json
    num_doors = int(data['num_doors'])
    num_simulations = int(data['num_simulations'])
    stay_wins = 0
    switch_wins = 0

    for _ in range(num_simulations):
        winner = random.randint(0, num_doors - 1)
        chosen_door = random.randint(0, num_doors - 1)
        if chosen_door == winner:
            stay_wins += 1
        else:
            switch_wins += 1

    stay_percentage = (stay_wins / num_simulations) * 100
    switch_percentage = (switch_wins / num_simulations) * 100

    return jsonify({'stay_percentage': stay_percentage, 'switch_percentage': switch_percentage})

    
if __name__ == '__main__':
    app.run(debug=True)
