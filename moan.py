from flask import Flask, make_response, render_template, request, url_for, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from flask import request
import requests
from models import session, Moan
from forms import MoanForm

try:
    import cPickle as pickle
except:
    import pickle

from syllables import is_haiku

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
    return render_template('index.html', moans = session.query(Moan).all())

@app.route('/test_post/', methods=['POST'])
def test_post():
	# Number of words first
	if len(request.data.split()) > 139:
		return True
	'''
	elif is_haiku(request.data):
		return True
	else:
		return False
	'''

@app.route('/make_post/', methods=['GET', 'POST'])
def make_post():
	form = MoanForm(csrf_enabled = False)
	if form.validate_on_submit():
		newPost = Moan()
		newPost.text = form.moan.data
		newPost.user = form.user.data
		session.add(newPost)
		session.commit()
	return render_template('make_post.html', form = form)


if __name__ == "__main__":
    app.run()