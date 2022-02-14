from flask import Flask, render_template, redirect
from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'el_psy_kongoroo'


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/distribution')
def distribution():
    astronauts = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Тедди Сандерс', 'Шон Бин']
    return render_template('distribution.html', astronauts=astronauts)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
