from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.modelos import User


class Register_Form(FlaskForm):

	def validate_username(self, username_to_check):

		user = User.query.filter_by(username=username_to_check.data).first()

		if user is not None:
			raise ValidationError("El usuario ya existe")

	def validate_email_address(self, email_to_check):
		email_address = User.query.filter_by(email_address=email_to_check.data).first()

		if email_address is not None:
			raise ValidationError("Email ya existe")

	username = StringField(label="Usuario: ", validators=[Length(min=2, max=30), DataRequired()])
	email_address = StringField(label="Correo electrónico:", validators=[Email(), DataRequired()])
	password1 =	PasswordField(label="Contraseña:", validators=[Length(min=6), DataRequired()])
	password2 = PasswordField(label="Confirmar Contraseña:", validators=[EqualTo("password1"), DataRequired()])
	submit = SubmitField(label="Crear Cuenta")

class Login_Form(FlaskForm):
	username = StringField(label="Usuario:", validators=[DataRequired()])
	password = StringField(label="Contraseña:", validators=[DataRequired()])
	submit = SubmitField(label="Iniciar Sesión")