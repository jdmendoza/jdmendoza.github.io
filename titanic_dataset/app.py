from flask import Flask, render_template, session, redirect, url_for, session
import numpy as np
from flask_wtf import FlaskForm
from wtforms import (StringField, RadioField, DecimalField, SubmitField)
from wtforms.validators import DataRequired
import pickle

loaded_model = pickle.load(open('model.sav', 'rb'))
X_predict = []

app=Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):
    '''
    This general class gets a lot of form about a person on the Titanic.
    Mainly a way to go through many of the WTForms Fields.
    '''
    pclass = StringField('What class was the person in?',validators=[DataRequired()])
    sibsp  = StringField("Have many siblings were on board?")
    sex = RadioField('Please choose gender:', choices=[('female','Female'),('male','Male')])
    parch = StringField('How many parents/siblings on board')
    fare = StringField('How much was the ticket?')

    submit = SubmitField('Submit')



@app.route("/about")
def about():
	return render_template('about.html')


@app.route('/', methods=['GET','POST'])
def index():
	form = InfoForm()

	#del X_predict
	X_predict.clear()

	if form.validate_on_submit():
        # Grab the data from the breed on the form.

		session['Sex'] = form.sex.data
		if form.sex.data == 'female':
			X_predict.append(0)
		else:
			X_predict.append(1)
		session['Pclass'] = form.pclass.data
		X_predict.append(int(form.pclass.data))
		session['SibSp'] = form.sibsp.data
		X_predict.append(int(form.sibsp.data))
		session['Parch'] = form.parch.data
		X_predict.append(int(form.parch.data))
		session['Fare'] = form.fare.data
		X_predict.append(float(form.fare.data))

		return (redirect(url_for("predict")))
	return (render_template('home.html', form=form))

@app.route('/predict')
def predict():
	print(X_predict)
	bin_pred = loaded_model.predict([X_predict])
	if bin_pred == 0:
		prediction = 'Did not survived'
	else:
		prediction = 'Survived'
	return (render_template('predict.html', prediction=prediction))


if __name__ == "__main__":
    app.run(debug=True)
