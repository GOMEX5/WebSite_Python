from flask import Flask, render_template

app = Flask(__name__)
PORT = 5000
DEBUG = False

@app.errorhandler(404)
def not_found(error):
    return "Not Found."

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html',title='WebSite with Python3',logo='WebSite with Python3')

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html',title='Contact',logo='WebSite with Python3')

if __name__ == '__main__':
    app.run(port=PORT,debug=DEBUG)