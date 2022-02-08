from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def mission_name():
    return "Миссия Колонизация Марса"


@app.route('/index')
def mission_slogan():
    return "И на Марсе будут яблони цвести!"


def promotion():
    promotion_text = ["Человечество вырастает из детства.",
                      "Человечеству мала одна планета.",
                      "Мы сделаем обитаемыми безжизненные пока планеты.",
                      "И начнем с Марса!",
                      "Присоединяйся!"]
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
                    {promotion()}
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
