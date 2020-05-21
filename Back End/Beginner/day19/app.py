from flask import Flask, request, render_template, flash, jsonify
import json

app = Flask(__name__)
app.config['SECRET_KEY']='1211c68d6a62babed7aef99e1fd0e339'

def load_db():
    with open('db.json') as f:
       return json.load(f)

data = load_db()

def save_db(data):
    with open('db.json', 'w') as f:
       return json.dump(data, f)

@app.route('/')
def home():
    # users=[d['name'] for d in data]
    return jsonify(data)
    # return render_template('home.html', id=len(data), users=users)

@app.route('/populate/', methods=['POST', 'GET'])
def form():
    id = len(data)
    if request.method == 'POST':
        obj = {
            "id": len(data)+1,
            "name" : request.form['name'],
            "username" : request.form['username'],
            "email" : request.form['email'],
            "address":{
                "street" : request.form['street'],
                "suite" : request.form['suite'],
                "city" : request.form['city'],
                "zipcode" : request.form['zipcode'],
                "geo":{
                    "lat" : request.form['latitude'],
                    "lng" : request.form['longitude']
                }
            },
            "phone" : request.form['phone'],
            "website" : request.form['website'],
            "company":{
                "name" : request.form['company name'],
                "catchPhrase" : request.form['catchPhrase'],
                "bs" : request.form['business']
            }
        }
        data.append(obj)
        save_db(data)
        flash('Added successfully')
        users=[d['name'] for d in data]
        return render_template('home.html', id=len(data), users=users)
    return render_template('form.html', id=id)

@app.route('/delete/', methods=['POST', 'GET'])
def delete():
    if request.method == 'POST':
        try:
            ind = int(request.form['index'])-1
            data.remove(data[ind])
        except :
            return 'Business Id not in data base'
        else:
            save_db(data)
            return 'Business successfully removed'
    return render_template('delete.html')




if __name__ == "__main__":
    app.run(debug=True)