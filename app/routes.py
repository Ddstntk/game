#! /usr/bin/env python3
import random
from random import randint
from flask import render_template, flash, redirect, url_for, request, jsonify, send_from_directory, session
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm, WinForm, PrepareHotseat, PrepareWeb
from app.models import User
from app.model.fightClass import fight
from app.model.fighterClass import fighter
from app.model.AiClass import AIfighter
from app.model.playerClass import fighterPlayer
from sqlalchemy import text, update
import json
import gc

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template("index.html", title='Home Page', image=url_for('static', filename='images/Char_'+str(current_user.avatarId)+'.png'))


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
        user = User(username=form.username.data,
                    email=form.email.data,
                    avatarId=form.avatarId.data,
                    strength=form.strength.data,
                    agility=form.agility.data,
                    stamina=form.stamina.data,)
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

def decompose(number):
    sub = number - randint(0, int(number / 2))
    return number - sub

@app.route('/fight_init', methods=['GET', 'POST'])
@login_required
def fight_init():
    PlayerStr = current_user.strength
    PlayerAgi = current_user.agility
    PlayerSta = current_user.stamina
    statsSum = PlayerAgi + PlayerAgi + PlayerSta

    OpponentStr = decompose(statsSum)
    OpponentAgi = decompose(statsSum)
    OpponentSta = decompose(statsSum)

    if PlayerStr >= OpponentStr:
        playerStronger = "silniejszy"
    else:
        playerStronger = "słabszy"

    if PlayerAgi >= OpponentAgi:
        playerAgiliter = "zwinniejszy"
    else:
        playerAgiliter = "mniej zwinny"

    if PlayerSta >= OpponentSta:
        playerStaminer = "wytrzymalszy"
    else:
        playerStaminer = "mniej wytrzymały"

    FighterPlr = fighterPlayer("Gracz", 1000, 550, PlayerStr, PlayerAgi, PlayerSta)
    FighterAI = AIfighter("Wojak", 1000, 550, OpponentStr, OpponentAgi, OpponentSta)
    # print("ai st:", FighterAI.strg)
    # print("plr st:", FighterPlr.strg)
    # print("ai ag:", FighterAI.agi)
    # print("plr ag:", FighterPlr.agi)
    # print("ai s:", FighterAI.sta)
    # print("plr s:", FighterPlr.sta)
    # currFight = fight(FighterPlr, FighterAI)
    currFight = fight(FighterPlr, FighterAI)

    # print(current_user.avatarId)

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
    form = WinForm(request.form)
    print("no to formularzyk 1")

    if request.method == 'POST':
        print("no to formularzyk 2")
        print(current_user.id)
        param = form.levelup.data
        id = str(current_user.id)
        print(param)
        print(id)

        setattr(current_user, param, getattr(current_user, param) + 1)
        db.session.commit()
        # query = "UPDATE user SET param: = param: +1 WHERE id=userid"
        # db.session.execute("UPDATE user SET "+ param + "=" + param + "+1 WHERE id=" + id + ";")

        flash('Congratulations, you leveled up!')
        return redirect(url_for('login'))

    return render_template("fight.html",
                           title='Walkaaa',
                           form=form,
                           image =url_for('static', filename='images/Char_'+str(current_user.avatarId)+'.png'),
                           op_image=url_for('static', filename='images/Char_'+str(randint(1, 7))+'.png'),
                           stronger=playerStronger,
                           agiliter=playerAgiliter,
                           staminer=playerStaminer
                           )


@app.route('/fight_do', methods=['GET'])
@login_required
def fight_do():
    FighterAI = AIfighter(**session.get("FighterAI"))
    FighterPlr = fighterPlayer(**session.get("FighterPlr"))
    currFight = fight(FighterPlr, FighterAI)
    action = request.args.get('action', 0, type=str)

    B = FighterPlr.action(action, FighterAI, currFight)
    A = FighterAI.action(FighterPlr, currFight)

    currFight.addAction(B)
    currFight.addAction(A)

    if FighterAI.health <= 0 or FighterPlr.health <= 0:
        print("TOOOOOOO JUŻŻŻŻŻŻŻŻŻ KONIEEEEEEEEEEEC!!")
        return json.dumps({
            "playerHP": FighterPlr.health,
            "playerSTA": FighterPlr.stamina,
            "opponentHP": FighterAI.health,
            "opponentSTA": FighterAI.stamina,
            "playerAction": "win" if FighterPlr.health > FighterAI.health else "die",
            "opponentAction": "die" if FighterPlr.health > FighterAI.health else "win"
        })

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


@app.route('/fight_hotseat_init', methods=['GET'])
@login_required
def fight_hotseat_init():
    opponentAvatar = session.get("opponentAvatar", None)
    PlayerStr = current_user.strength
    PlayerAgi = current_user.agility
    PlayerSta = current_user.stamina
    statsSum = PlayerAgi + PlayerAgi + PlayerSta

    OpponentStr = decompose(statsSum)
    OpponentAgi = decompose(statsSum)
    OpponentSta = decompose(statsSum)

    FighterPlr = fighterPlayer("Gracz", 1000, 550, PlayerStr, PlayerAgi, PlayerSta)
    FighterOpponent = fighterPlayer("Wojak", 1000, 550, OpponentStr, OpponentAgi, OpponentSta)

    currFight = fight(FighterPlr, FighterOpponent)

    session['FighterOpponent'] = FighterOpponent.__dict__
    session['FighterPlr'] = FighterPlr.__dict__
    session['currFight'] = currFight.__dict__

    return render_template("fight_hotseat.html",
                           title='Walkaaa - hotseat',
                           # form=form,
                           image =url_for('static', filename='images/Char_'+str(current_user.avatarId)+'.png'),
                           op_image=url_for('static', filename='images/Char_'+str(opponentAvatar)+'.png'),
                           )


@app.route('/prepare_hotseat_init', methods=['GET', 'POST'])
@login_required
def prepare_hotseat_init():
    form = PrepareHotseat(request.form)
    if request.method == 'POST':
        session["opponentAvatar"] = form.avatarId.data
        print("przypisano avatarid do sesji")
        return redirect(url_for('fight_hotseat_init'))
    return render_template("prepare_hotseat.html",
                           title='Walkaaa - hotseat',
                           form=form,
                           )


@app.route('/fight_hotseat_do', methods=['GET'])
@login_required
def fight_hotseat_do():
    FighterOpponent = fighterPlayer(**session.get("FighterOpponent"))
    FighterPlr = fighterPlayer(**session.get("FighterPlr"))
    currFight = fight(FighterPlr, FighterOpponent)
    action = request.args.get('action', 0, type=str)
    actionOpponent = request.args.get('actionOpponent', 0, type=str)
    print(action)
    print(actionOpponent)
    print("xd")
    B = FighterPlr.action(action.replace("Hs",""), FighterOpponent, currFight)
    A = FighterOpponent.action(actionOpponent.replace("HsO",""), FighterPlr, currFight)

    currFight.addAction(B)
    currFight.addAction(A)
    #
    # for obj in gc.get_objects():
    #     if isinstance(obj, fighter):
    #         print(obj.name)

    if FighterOpponent.health <= 0 or FighterPlr.health <= 0:
        print("TOOOOOOO JUŻŻŻŻŻŻŻŻŻ KONIEEEEEEEEEEEC!!")
        return json.dumps({
            "playerHP": FighterPlr.health,
            "playerSTA": FighterPlr.stamina,
            "opponentHP": FighterOpponent.health,
            "opponentSTA": FighterOpponent.stamina,
            "playerAction": "win" if FighterPlr.health > FighterOpponent.health else "die",
            "opponentAction": "die" if FighterPlr.health > FighterOpponent.health else "win"
        })

    else:
        session['FighterOpponent'] = FighterOpponent.__dict__
        session['FighterPlr'] = FighterPlr.__dict__
        session['currFight'] = currFight.__dict__


        return json.dumps({
                "playerHP": FighterPlr.health,
                "playerSTA": FighterPlr.stamina,
                "opponentHP": FighterOpponent.health,
                "opponentSTA": FighterOpponent.stamina,
                "playerAction": FighterPlr.actionMemory,
                "opponentAction": FighterOpponent.actionMemory
                })
    # return json.dumps({'file_id': record.file_id, 'filename': record.filename, 'links_to': record.links_to})

@app.route('/fight_web_init', methods=['GET'])
@login_required
def fight_web_init():
    opponentAvatar = session.get("opponentAvatar", None)
    PlayerStr = current_user.strength
    PlayerAgi = current_user.agility
    PlayerSta = current_user.stamina
    statsSum = PlayerAgi + PlayerAgi + PlayerSta

    OpponentStr = decompose(statsSum)
    OpponentAgi = decompose(statsSum)
    OpponentSta = decompose(statsSum)

    FighterPlr = fighterPlayer("Gracz", 1000, 550, PlayerStr, PlayerAgi, PlayerSta)
    FighterOpponent = fighterPlayer("Wojak", 1000, 550, OpponentStr, OpponentAgi, OpponentSta)

    currFight = fight(FighterPlr, FighterOpponent)

    session['FighterOpponent'] = FighterOpponent.__dict__
    session['FighterPlr'] = FighterPlr.__dict__
    session['currFight'] = currFight.__dict__

    return render_template("fight_hotseat.html",
                           title='Walkaaa - hotseat',
                           # form=form,
                           image =url_for('static', filename='images/Char_'+str(current_user.avatarId)+'.png'),
                           op_image=url_for('static', filename='images/Char_'+str(opponentAvatar)+'.png'),
                           )


@app.route('/prepare_web_init', methods=['GET', 'POST'])
@login_required
def prepare_web_init():
    form = PrepareWeb(request.form)
    if request.method == 'POST':
        roomName = form.roomName.data

        return redirect(url_for('fight_web_init'))
    return render_template("prepare_web.html",
                           title='Walkaaa - hotseat',
                           form=form,
                           )


@app.route('/fight_web_do', methods=['GET'])
@login_required
def fight_web_do():
    FighterOpponent = fighterPlayer(**session.get("FighterOpponent"))
    FighterPlr = fighterPlayer(**session.get("FighterPlr"))
    currFight = fight(FighterPlr, FighterOpponent)
    action = request.args.get('action', 0, type=str)
    actionOpponent = request.args.get('actionOpponent', 0, type=str)
    print(action)
    print(actionOpponent)
    print("xd")
    B = FighterPlr.action(action.replace("Hs",""), FighterOpponent, currFight)
    A = FighterOpponent.action(actionOpponent.replace("HsO",""), FighterPlr, currFight)

    currFight.addAction(B)
    currFight.addAction(A)
    #
    # for obj in gc.get_objects():
    #     if isinstance(obj, fighter):
    #         print(obj.name)

    if FighterOpponent.health <= 0 or FighterPlr.health <= 0:
        print("TOOOOOOO JUŻŻŻŻŻŻŻŻŻ KONIEEEEEEEEEEEC!!")
        return json.dumps({
            "playerHP": FighterPlr.health,
            "playerSTA": FighterPlr.stamina,
            "opponentHP": FighterOpponent.health,
            "opponentSTA": FighterOpponent.stamina,
            "playerAction": "win" if FighterPlr.health > FighterOpponent.health else "die",
            "opponentAction": "die" if FighterPlr.health > FighterOpponent.health else "win"
        })

    else:
        session['FighterOpponent'] = FighterOpponent.__dict__
        session['FighterPlr'] = FighterPlr.__dict__
        session['currFight'] = currFight.__dict__


        return json.dumps({
                "playerHP": FighterPlr.health,
                "playerSTA": FighterPlr.stamina,
                "opponentHP": FighterOpponent.health,
                "opponentSTA": FighterOpponent.stamina,
                "playerAction": FighterPlr.actionMemory,
                "opponentAction": FighterOpponent.actionMemory
                })
    # return json.dumps({'file_id': record.file_id, 'filename': record.filename, 'links_to': record.links_to})



@app.route('/js/<path:path>')
def send_js(path): return send_from_directory('js', path)

#
# if __name__ == '__app__':
#     app.run(debug = False, host = '0.0.0.0', port = 5050)