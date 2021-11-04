from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class AddUserForm(FlaskForm):
    id = StringField('id')
    knownname = StringField('knownname')
    givenname = StringField('givenname')
    familyname = StringField('familyname')
    fullname = StringField('fullname')
    gender = StringField('gender')
    birthdate = StringField('birthdate')
    city = StringField('city')
    country = StringField('country')
    citynow = StringField('citynow')
    countrynow = StringField('countrynow') 
    continent = StringField('continent')
    locationstring = StringField('locationstring')
    prizestatus = StringField('prizestatus')
    submit = SubmitField('submit')

class SearchForm(FlaskForm):
    knownname = StringField('knownname')
    submit = SubmitField('submit')

class AwardSearchForm(FlaskForm):
    awardyear = StringField('Award Year')
    submit = SubmitField('submit')