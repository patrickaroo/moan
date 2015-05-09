from flask import Flask, make_response, render_template, request, url_for, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
try:
    import cPickle as pickle
except:
    import pickle

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'guest'

toolbar = DebugToolbarExtension(app)

@app.after_request
def gnu_terry_pratchett(resp):
  resp.headers.add("X-Clacks-Overhead", "GNU Terry Pratchett")
  return resp

@app.route('/', methods = ['GET', 'POST'])
def index():
    return "Hello world!"#render_template('index.html', form=form)

if __name__ == "__main__":
    app.run()