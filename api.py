from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('temperature_page.html')

@app.get('/content')
def test():
    return "{'content': 'Wow' }"


if __name__ == '__main__':
    app.run()