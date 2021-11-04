from flask import Flask,render_template,flash,redirect
from flask import Flask, render_template,request
from json import dumps
from bson import json_util
from flask.helpers import url_for
#from application import db
from flask_pymongo import PyMongo
from form import AddUserForm, AwardSearchForm, SearchForm
################################################################################################################################
app = Flask(__name__)
#################################################################################################################################
#mongodb url
#app.confimongo_dbname"] = "nobel"
app.config["MONGO_URI"] = "mongodb+srv://deep:deep@cluster0.85mlz.mongodb.net/nobel_prize"
#"mongodb://localhost:27017/nobel"

mongo = PyMongo(app)
db = mongo.db
##############################################################################################################################
#to not allow change of cookies 
app.config['SECRET_KEY'] = 'abcd'
###############################################################################################################################
@app.route("/")
@app.route("/")
#home functio passed with custom title
def home():
    return render_template('home.html',title = 'custom title')
####################################################################################################################
#about function returns ansewr for search by laureate name
@app.route("/about",methods=['POST','GET'])
def about():
    knownname = request.args.get('knownname')
    print(knownname)
    laureates = db.laureates.find_one({"knownName":{"en":knownname,"se":knownname}})
    Table = []
   
    for key, value in laureates.items():    
        temp = []
        temp.extend([key,value]) 
        Table.append(temp)
    return render_template('about.html',result=Table)

###################################################################################################################
@app.route("/add",methods=['get','post'])
def add():
    form = AddUserForm()
    if request.method == "POST":
        id = form.id.data
        knownname = form.knownname.data
        givenname = form.givenname.data
        familyname = form.familyname.data
        fullname = form.fullname.data
        gender = form.gender.data
        birthdate = form.birthdate.data
        city = form.city.data
        country = form.country.data
        citynow = form.citynow.data
        countrynow = form.countrynow.data
        continent = form.continent.data
        locationstring = form.locationstring.data
        prizestatus = form.prizestatus.data
        db.laureates.insert_one({
            "id" : id,
            "knownname":{"en":knownname,"se":knownname},
            "givenname":{"en":givenname,"se":givenname},
            "familyname":{"en":familyname,"se":familyname},
            "fullname":{"en":fullname,"se":fullname},
            "gender":gender,
            "birthdate":birthdate,
            "city":{"en":city,"no":city,"se":city},
            "country":country,
            "citynow":citynow,
            "countrynow":countrynow,
            "continent":continent,
            "locationstring":locationstring,
            "prizestatus":prizestatus})
    if form.validate_on_submit():
        flash(f'document created for {form.fullname.data}!','success')
        return redirect(url_for('home'))
    return render_template('addlaureate.html',title='laureate', form=form)
###################################################################################################################
#search function
@app.route("/search",methods=['GET','POST'])
def search():
    form = SearchForm()
    return render_template('searchlaureate.html', title='searchlaureate', form=form)
#################################################################################################################################################
@app.route("/searchawardbyyear",methods=['GET','POST'])
def searchawardbyyear():
    form = AwardSearchForm()
    return render_template('searchaward.html', title='searchaward', form=form)
########################################################################################################################################
@app.route("/awardbyyearanswer",methods=['POST','GET'])
def awardbyyearanswer():
    awardyear = request.args.get('awardyear')
    awards = db.award.find({"awardYear":awardyear}).limit(1)
    Table= []
    for data in awards:   
        for key, value in data.items():    # or .items() in Python 3
            temp = []
            temp.extend([key,value])  #Note that this will change depending on the structure of your dictionary
            Table.append(temp)
    return render_template('award_year_answer.html',result=Table)

##############################################################################################################################


###################################################################################################################################################

if __name__ == '__main__':
    app.run(debug=True)

#############################################################################################################################################3
