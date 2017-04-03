from flask import render_template, redirect, request
from draw import app
from .models import User
from .database import db_session
import praw

def add_url_routes(routes_tuple):
    for route, view_func in routes_tuple:
        app.add_url_rule(route, view_func.__name__, view_func, methods=["GET",
            "POST"])

def index():
    return "Users registered: %s" % [u.username for u in
            User.query.all()]

def register(username):
    reddit = praw.Reddit(client_id='',
                         client_secret='',
                         redirect_uri='http://mrkrabs.csh.rit.edu:8080/callback',
                         user_agent='drawbot by /u/csssuf')
    url = reddit.auth.url(['submit', 'identity', 'vote'], username, 'permanent')
    return redirect(url)

def callback():
    code = request.args.get('code')
    if code is None:
        return "Failure"
    reddit = praw.Reddit(client_id='',
                         client_secret='',
                         redirect_uri='http://mrkrabs.csh.rit.edu:8080/callback',
                         user_agent='drawbot by /u/csssuf')
    refresh = reddit.auth.authorize(code)
    old_user = User.query.filter(User.username == str(reddit.user.me())).first()
    if old_user is None:
        new_user = User(str(reddit.user.me()), code, refresh)
        db_session.add(new_user)
    else:
        old_user.code = request.args.get('code')
        old_user.refresh_token = reddit.auth.authorize(code)
    db_session.commit()
    return "Success"

add_url_routes((
    ('/', index),
    ('/register/<username>/', register),
    ('/callback', callback),
    ('/register/', lambda: register("none"))
))
