from flask import Flask, render_template, jsonify, request
import random
from bdd import *

app = Flask(__name__)

# Liste des items possibles dans la loot box
items_commun = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
items_rare = ["Item 6", "Item 7", "Item 8", "Item 9", "Item 10"]
items_epic = ["Item 11", "Item 12", "Item 13", "Item 14", "Item 15"]
items_legendaire = ["Item 16", "Item 17", "Item 18", "Item 19", "Item 20"]

chance = 0


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/response', methods=['GET', 'POST'])
def response():
    uname = request.form['username']
    pword = request.form['password']
    add_user(uname, pword)
    return render_template('index.html')
    


@app.route('/open_box_commun')
def open_box_commun():     
    # Sélection aléatoire d'un item

    chance = random.randint(1, 1000000)
    if chance <= 1000 : 
        selected_item = random.choice(items_legendaire)
        return jsonify({"item": selected_item, 'type' : "legendary", "chance" : chance})
    elif chance <= 100000 and chance > 1000:
        selected_item = random.choice(items_epic)
        return jsonify({"item": selected_item, 'type' : "epic", "chance" : chance})
    elif chance <= 500000 and chance > 100000:
        selected_item = random.choice(items_rare)
        return jsonify({"item": selected_item, 'type' : "rare", "chance" : chance})
    else : 
        return jsonify({"item": random.choice(items_commun), 'type' : "commun", "chance" : chance})
    
@app.route('/open_box_rare')
def open_box_rare():     
    # Sélection aléatoire d'un item

    chance = random.randint(1, 1000000)
    if chance <= 2000 : 
        selected_item = random.choice(items_legendaire)
        return jsonify({"item": selected_item, 'type' : "legendary", "chance" : chance})
    elif chance <= 175000 and chance > 2000:
        selected_item = random.choice(items_epic)
        return jsonify({"item": selected_item, 'type' : "epic", "chance" : chance})
    elif chance <= 700000 and chance > 175000:
        selected_item = random.choice(items_rare)
        return jsonify({"item": selected_item, 'type' : "rare", "chance" : chance})
    else : 
        return jsonify({"item": random.choice(items_commun), 'type' : "commun", "chance" : chance})
    
@app.route('/open_box_epic')
def open_box_epic():     
    # Sélection aléatoire d'un item

    chance = random.randint(1, 1000000)
    if chance <= 5000 : 
        selected_item = random.choice(items_legendaire)
        return jsonify({"item": selected_item, 'type' : "legendary", "chance" : chance})
    elif chance <= 500000 and chance > 5000:
        selected_item = random.choice(items_epic)
        return jsonify({"item": selected_item, 'type' : "epic", "chance" : chance})
    elif chance <= 900000 and chance > 500000:
        selected_item = random.choice(items_rare)
        return jsonify({"item": selected_item, 'type' : "rare", "chance" : chance})
    else : 
        return jsonify({"item": random.choice(items_commun), 'type' : "commun", "chance" : chance})
    
@app.route('/open_box_legendary')
def open_box_legendary():     
    # Sélection aléatoire d'un item

    chance = random.randint(1, 1000000)
    if chance <= 200000 : 
        selected_item = random.choice(items_legendaire)
        return jsonify({"item": selected_item, 'type' : "legendary", "chance" : chance})
    elif chance <= 900000 and chance > 200000:
        selected_item = random.choice(items_epic)
        return jsonify({"item": selected_item, 'type' : "epic", "chance" : chance})
    elif chance <= 100000000 and chance > 900000:
        selected_item = random.choice(items_rare)
        return jsonify({"item": selected_item, 'type' : "rare", "chance" : chance})
    else : 
        return jsonify({"item": random.choice(items_commun), 'type' : "commun", "chance" : chance})
    

if __name__ == '__main__':
    app.run(debug=True)
