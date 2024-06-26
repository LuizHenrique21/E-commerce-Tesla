from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, EqualTo

class ShowPassword(PasswordField):
    def __init__(self, *args, **kwargs):
        super(ShowPassword, self).__init__(*args, **kwargs)
        self.hide_password = True

    def toggle(self):
        self.hide_password = not self.hide_password

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = valuelist[0]
        else:
            self.data = ''

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = ShowPassword('password')
    exibir_senha = BooleanField('exibir_senha')
    remember_me = BooleanField("remember_me")
    submit = SubmitField('Submit')

    def validate_password(form, field):
        
        print("password field is {}".format(field))
