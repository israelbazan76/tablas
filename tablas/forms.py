from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,BooleanField,IntegerField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, Email, Length, NumberRange,InputRequired
from wtforms.widgets.core import TextArea


class SignupForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=64)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Registrar')
class PostForm(FlaskForm):
    title = StringField('Titulo', validators=[DataRequired(),Length(max=128)])
    title_slug = StringField('Titulo slug', validators=[Length(max=128)])
    content = TextAreaField('Contenido')
    submit = SubmitField('Guardar')
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Recuérdame')
    submit = SubmitField('Login')
class TablasForm(FlaskForm):
    number = IntegerField('Tabla del', validators=[InputRequired( message='*Requerido'),NumberRange(min=1,message='Ingrese un número igual o mayor a %(min)d')])
    submit = SubmitField('Ir')