from flask import (render_template,
                   url_for, request)
from models import db, Pet, app





@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add-pet', methods=['GET', 'POST'])
def add_pet():
    print(request.form)
    print(request.form['name'])
    return render_template('addpet.html')


@app.route('/pet')
def pet():
    return render_template('pet.html')


@app.route('/arthas')
def arthas():
    return 'Arthas the golden retriever wants a Tennis Ball'


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')

