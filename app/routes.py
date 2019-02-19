#! /usr/bin/env python3

from flask import render_template, flash, redirect, url_for, request, jsonify, send_from_directory, session
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User
from app.model.fightClass import fight
from app.model.fighterClass import fighter
from app.model.AiClass import AIfighter
from app.model.playerClass import fighterPlayer

import json

@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html", title='Home Page', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


# @app.route('/_add_numbers', methods=['GET'])
# def add_numbers():
#     a = request.args.get('a', 0, type=int)
#     b = request.args.get('b', 0, type=int)
#     return jsonify(result=testMe())

@app.route('/fight_init', methods=['GET'])
@login_required
def fight_init():
    FighterAI = AIfighter("Wojak", 1000, 550, 6, 3, 11)
    FighterPlr = fighterPlayer("Gracz", 1000, 550, 6, 3, 11)
    # currFight = fight(FighterPlr, FighterAI)
    currFight = fight(FighterPlr, FighterAI)

    session['FighterAI'] = FighterAI.__dict__
    session['FighterPlr'] = FighterPlr.__dict__
    session['currFight'] = currFight.__dict__
    # print(FighterAI.name)
    # action = request.args.get('action', 0, type=str)
    #
    # FighterPlr.action(action, FighterAI)
    #
    # return json.dumps({
    #     "playerHP": FighterPlr.health,
    #     "playerSTA": FighterPlr.stamina,
    #     "opponentHP": FighterAI.health,
    #     "opponentSTA": FighterAI.stamina
    # })
    return render_template("fight.html", title='Walkaaa')


@app.route('/fight_do', methods=['GET'])
@login_required
def fight_do():
    FighterAI = AIfighter(**session.get("FighterAI"))
    FighterPlr = fighterPlayer(**session.get("FighterPlr"))
    currFight = fight(FighterAI, FighterPlr)
    action = request.args.get('action', 0, type=str)

    B = FighterPlr.action(action, FighterAI, currFight)
    A = FighterAI.action(FighterPlr, currFight)

    currFight.addAction(A)
    currFight.addAction(B)

    if FighterAI.health <= 0 or FighterPlr.health <= 0:
        print("TOOOOOOO JUŻŻŻŻŻŻŻŻŻ KONIEEEEEEEEEEEC!!")
        return redirect("index.html")

    else:
        session['FighterAI'] = FighterAI.__dict__
        session['FighterPlr'] = FighterPlr.__dict__
        session['currFight'] = currFight.__dict__


        return json.dumps({
                "playerHP": FighterPlr.health,
                "playerSTA": FighterPlr.stamina,
                "opponentHP": FighterAI.health,
                "opponentSTA": FighterAI.stamina,
                "playerAction": FighterPlr.actionMemory,
                "opponentAction": FighterAI.actionMemory
                })
    # return json.dumps({'file_id': record.file_id, 'filename': record.filename, 'links_to': record.links_to})

@app.route('/js/<path:path>')
def send_js(path): return send_from_directory('js', path)