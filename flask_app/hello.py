from flask import Flask, render_template
from flask import request
from flask import make_response
from flask_bootstrap import Bootstrap
from flask.ext.moment import Moment 
from datetime import datetime
from flask.ext.wtf import Form
from wtfforms import StringField, SubmitField
from wtfforms.validators import Required


app = Flask(__name__)
bootstrap =  Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'hard to guess string'

class NameForm(Form):
    name= StringField('What is ur name?', validators= [Required()]
    submit =  SubmitField('Submit')
    
@app.route('/')
def index():
    #user_agent = request.headers.get('User_Agent')
    #response= make_response("This carries a cookie")
    #response.set_cookie('answer', '42')
    #return '<h1>Your browseris %s</h1>'% user_agent
    return render_template('index.html', current_time= datetime.utcnow())

@app.route('/user/<name>')
def  user(name):
    return render_template('user.html', name= name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)