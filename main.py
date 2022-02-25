from flask import Flask, render_template, redirect

from data.users import User
from loginform import LoginForm
from flask_login import LoginManager, login_user
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'el_psy_kongoroo'
login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/<title>')
@app.route('/index/<title>')
def base(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    prof = prof.lower()
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<list>')
def prof_list(list):
    return render_template('prof_list.html', list=list)


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    return render_template('auto_answer.html')


@app.route('/distribution')
def distribution():
    astronauts = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Тедди Сандерс', 'Шон Бин']
    return render_template('distribution.html', astronauts=astronauts)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    db_session.global_init("db/blogs.db")
    app.run(port=8080, host='127.0.0.1')
