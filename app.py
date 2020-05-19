from flask import Flask, render_template

meu_web_app = Flask('my_web_app')

me = {
    'nome': 'Denis M. Sousa',
    'descricao': 'Programador, geek, músico e fã do Chelsea.',
    'url': '#',
    'nome_url': 'Me siga no Instagram',
    'foto': 'https://avatars2.githubusercontent.com/u/29387875?s=400&u=b101886329eeff72d675feb6d979bb06b76ae6d6&v=4'
}

my_friend = {
    'nome': 'Adrilene Fonseca',
    'descricao': 'Love cats, programming, rihanna and my church.',
    'url': '#',
    'nome_url': 'Me siga no Instagram',
    'foto': 'https://avatars1.githubusercontent.com/u/19615841?s=400&u=f01d8ffdf7a697e3f9e927d6fe9276a908ebb7e3&v=4'
}

all_data = {
    "denis": me,
    "drica": my_friend
}


@meu_web_app.route('/')
def start_page():
    return '<h1>Go to /denis or /drica :)</h1>'

@meu_web_app.route('/<perfil>')
def person_perfil(perfil):
    return render_template('index.html', perfil=all_data[perfil])

if __name__ == "__main__":
    meu_web_app.run()