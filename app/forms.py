#! /usr/bin/env python3

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, RadioField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    avatarId = IntegerField('Avatar', validators=[DataRequired()])
    strength = IntegerField('Strength', validators=[DataRequired()])
    agility = IntegerField('Agility', validators=[DataRequired()])
    stamina = IntegerField('Stamina', validators=[DataRequired()])

    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class WinForm(FlaskForm):
    levelup = RadioField('Avatar', validators=[DataRequired()])
    submit = SubmitField('LevelUp')


class PrepareHotseat(FlaskForm):
    avatarId = IntegerField('Avatar', validators=[DataRequired()])
    submit = SubmitField('Walcz')

class PrepareWeb(FlaskForm):
    roomName = StringField('Nazwa pokoju', validators=[DataRequired()])
    submit = SubmitField('Załóż')

    def validate_roomName(self, roomName):
        user = User.query.filter_by(roomName=roomName.data).first()
        if user is not None:
            raise ValidationError('Please use a different roomName.')
