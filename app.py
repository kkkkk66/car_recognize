from flask import Flask, render_template

app = Flask(__name__)

app.config['DEBUG']=True;

@app.route('/')
def car_recognize():  # put application's code here
    return render_template("car_recognize.html")

@app.route('/car/search')
def car_search():  # put application's code here
    return render_template("car_search.html")

@app.route('/group/introduction')
def group_introduction():  # put application's code here
    return render_template("group_introduction.html")

@app.route('/number/search')
def number_search():  # put application's code here
    return render_template("number_search.html")

@app.route('/mysql')
def my_sql():  # put application's code here
    return render_template("mysql.html")

@app.route('/take/poto')
def po():  # put application's code here
    return render_template("take_poto.html")

if __name__ == '__main__':
    app.run()
