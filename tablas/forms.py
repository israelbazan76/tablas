from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,BooleanField,IntegerField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange,InputRequired
from wtforms.widgets.core import TextArea



class TablasForm(FlaskForm):
    number = IntegerField('Tabla del', validators=[InputRequired( message='*Requerido'),NumberRange(min=1,message='Ingrese un número igual o mayor a %(min)d')])
    submit = SubmitField('Ir')