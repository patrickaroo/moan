from flask import Flask, Response, render_template, request, url_for, redirect, flash, session, jsonify, send_from_directory
from flask_debugtoolbar import DebugToolbarExtension
from flask import request
import requests
import ast
from models import session, Moan
from forms import MoanForm

try:
    import cPickle as pickle
except:
    import pickle

#from syllables import is_haiku

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__, static_folder='static')
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'guest'

toolbar = DebugToolbarExtension(app)

@app.after_request
def gnu_terry_pratchett(resp):
  resp.headers.add("X-Clacks-Overhead", "GNU Terry Pratchett")
  return resp

@app.route('/', methods = ['GET', 'POST'])
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/posts', methods = ['GET'])
def get_posts():
    posts = session.query(Moan).all()
    response = [post.as_dict() for post in posts]
    return jsonify(results=response)

@app.route('/post/<postId>', methods=['GET'])
def get_post(postId = None):
    post = session.query(Moan).get(postId)
    return jsonify(post.as_dict())

@app.route('/post/', methods=['POST'])
def make_post():
    newPost = Moan()
    data = ast.literal_eval(request.data)

    newPost.text = data['text']
    newPost.user = data['user']
    session.add(newPost)
    session.commit()

    return "I don't know what I'm doing"

@app.route('/test_post/', methods=['POST'])
def test_post():
    # Number of words first
    if len(request.data.split()) > 139:
            return True
    else:
            return False
    '''
    elif is_haiku(request.data):
            return True
    else:
            return False
    '''

if __name__ == "__main__":
    app.run()
