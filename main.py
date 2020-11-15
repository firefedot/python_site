# coding: utf-8

from horoscope import generate_prophecies
from datetime import datetime as dt


bootstrap = '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">'


def generate_page(head, body):
    page = f'<html>{head}{body}</html>'
    return page


def generate_head(title):
    head = f'''
    <head>
    {bootstrap}
    <meta charset="UTF-8">
        <title>{title}</title>
    </head>
        '''
    return head


def generate_body(header, paragraphs):
    body = f"<h1>{ header }</h1>"
    for p in paragraphs:
        body += f"<p>{p}</p>"

    return f"<body>{ body }<a href='about.html'>About</a></body>"


# body = generate_body(header='Гороскоп на 15.11.2020', paragraphs=generate_prophecies())


def save_page(title, header, paragraphs, output="index.html"):
    with open(output, "w") as nf:
        today = dt.now().date()
        page = generate_page(head=generate_head(title), body=generate_body(header=header, paragraphs=paragraphs))
        print(page, file=nf)


today = dt.now().date()
save_page(title="Гороскоп на сегодня", header=f"Что день {today} говорит", paragraphs=generate_prophecies())
save_page(title="Гороскоп на сегодня", header=f"page about", paragraphs='any text', output="about.html")
