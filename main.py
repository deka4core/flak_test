from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def mission_name():
    return "Миссия Колонизация Марса"


@app.route('/index')
def mission_slogan():
    return "И на Марсе будут яблони цвести!"


def promotion(promotion_text):
    return ''.join(['<div class="alert alert-primary" role="alert">' + x + "</div>" for x in promotion_text])


@app.route('/promotion')
@app.route('/promotion_image')
def bootstrap():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Жди нас, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}"
                      alt="здесь должна была быть картинка, но не нашлась">
                    {promotion(["Человечество вырастает из детства.",
                                "Человечеству мала одна планета.",
                                "Мы сделаем обитаемыми безжизненные пока планеты.",
                                "И начнем с Марса!",
                                "Присоединяйся!"])}
                  </body>
                </html>'''


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <div><h1>Анкета претендента<br><h4>на участие в миссии</h4></h1></div>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name"><br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите e-mail" name="email">
                                    <div class="form-group">
                                        <label for="educationSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="educationSelect" name="education">
                                          <option>Среднее</option>
                                          <option>Бакалавриат</option>
                                          <option>Специалитет</option>
                                          <option>Магистратура</option>
                                          <option>Подготовка кадров высшей квалификации</option>
                                        </select>
                                     </div><br>
                                     <div class="form-group">
                                        <label for="profession-check">Какие у Вас есть профессии?</label>
                                        <div class="profession-check">
                                          <input class="form-check-input" type="checkbox" name="profession" value="engineer" id="engineer">
                                          <label class="form-check-label" for="engineer">
                                            Инженер-исследователь
                                          </label>
                                        </div>
                                        <div class="profession-check">
                                          <input class="form-check-input" type="checkbox" name="profession" value="engineer-builder" id="engineer-builder">
                                          <label class="form-check-label" for="engineer-builder">
                                            Инженер-строитель
                                          </label>
                                        </div>
                                        <div class="profession-check">
                                          <input class="form-check-input" type="checkbox" name="profession" value="pilot" id="pilot">
                                          <label class="form-check-label" for="pilot">
                                            Пилот
                                          </label>
                                        </div>
                                        <div class="profession-check">
                                          <input class="form-check-input" type="checkbox" name="profession" value="meteorologist" id="meteorologist">
                                          <label class="form-check-label" for="meteorologist">
                                            Метеоролог
                                          </label>
                                        </div>
                                        <div class="profession-check">
                                          <input class="form-check-input" type="checkbox" name="profession" value="engineer-terra" id="engineer-terra">
                                          <label class="form-check-label" for="engineer-terra">
                                            Инженер по терраформированию
                                          </label>
                                        </div>
                                        <div class="profession-check">
                                          <input class="form-check-input" type="checkbox" name="profession" value="medic" id="medic">
                                          <label class="form-check-label" for="medic">
                                            Врач
                                          </label>
                                        </div>
                                        <div class="profession-check">
                                          <input class="form-check-input" type="checkbox" name="profession" value="biologist" id="biologist">
                                          <label class="form-check-label" for="biologist">
                                            Экзобиолог
                                          </label>
                                        </div>
                                     </div><br>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div><br>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите участвовать в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form.get('name'))
        print(request.form.get('surname'))
        print(request.form.get('email'))
        print(request.form.get('education'))
        print(request.form.get('profession'))
        print(request.form.get('sex'))
        print(request.form.get('about'))
        print(request.form.get('file'))
        print(request.form.get('accept'))
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def planets_choice(planet_name):
    mars_poem = [
        "Марс пустынная планета", "Никого на Марсе нет.", "Не растут деревья тут", "И цветы холодным летом"
        , "Не распустятся с рассветом.", "Очень мало здесь, воды,", "Но у полюса есть льды."]
    venera_poem = ["Венера прекрасна! За тонкой вуалью",
                   "Богиню любви различите едва ли!",
                   "Закрыта она пеленой облаков.",
                   "А что же под ними? Климат каков?",
                   "Климат имеет огромный дефект.",
                   "Причиной тому парниковый эффект.",
                   "Газ ядовит в атмосфере Венеры.",
                   "Дышать невозможно! Жарища без меры!",
                   "Солнца не видно сквозь облака.",
                   "Жизнь невозможна! Но, может, пока?"]
    planets = {"Марс": mars_poem, "Венера": venera_poem}
    return f'''<!doctype html>
                   <html lang="en">
                     <head>
                       <meta charset="utf-8">
                       <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                       <link rel="stylesheet" 
                       href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                       integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                       crossorigin="anonymous">
                       <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                       <title>Жди нас, {planet_name}!</title>
                     </head>
                     <body>
                       <h1>Жди нас, {planet_name}!</h1>
                       {promotion(planets[planet_name])}
                     </body>
                   </html>'''


@app.route("/results/<nickname>/<int:level>/<float:rating>")
def results_page(nickname, level: int, rating: float):
    return f'''<!doctype html>
                   <html lang="en">
                     <head>
                       <meta charset="utf-8">
                       <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                       <link rel="stylesheet" 
                       href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                       integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                       crossorigin="anonymous">
                       <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                       <title>Результаты!</title>
                     </head>
                     <body>
                       <h1>Результаты отбора!</h1><br>
                       <h4>Претендента {nickname} на участие в миссии Akuranpu:</h4><br>
                       {promotion([f'Ваш рейтинг после {level} этапа отбора',
                                   f'составляет {rating}!', 'Желаем удачи!'])}
                     </body>
                   </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
