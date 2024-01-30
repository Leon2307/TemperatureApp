from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.get('/test')
def test():
    return "{'hallo': 123}"

if __name__ == '__main__':
    app.run('0.0.0.0')