from flask import Flask, render_template, request
import random
from random import randint
from random import seed




app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def monty_hall():
    if request.method == 'POST':
        #num_doors = int(request.form['num_doors'])
        #num_simulations = int(request.form['num_simulations'])
        doors = int(request.form['doors'])

        win_door = randint(1,doors)
         

        # Perform Monty Hall simulations and calculate statistics
        # You can implement this logic here

        return render_template('index.html', doors=doors, win_door=win_door)

    return render_template('index.html')




if __name__=='__main__':
  app.run('0.0.0.0',debug=True)
