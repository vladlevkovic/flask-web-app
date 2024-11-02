from flask import Blueprint, render_template, redirect
from werkzeug.security import check_password_hash, generate_password_hash
from project.app.forms.register import RegisterForm
from project.app.models.base import session
from project.app.models.user import User


user_bp = Blueprint('user', __name__)


@user_bp.route('/', methods=['GET'])
def main():
    return render_template('index.html')


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        with session() as db:
            password = generate_password_hash(form.password.data)
            user = User(
                email=form.email.data,
                password=password
            )
            db.add(user)
            db.commit()
            print('user register')
            return redirect('/')
    return render_template('user/register.html', form=form)
