mkdir my_flask_app
cd my_flask_app
# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/content')
def content():
    return render_template('content.html')

if __name__ == '__main__':
    app.run(debug=True)
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Index Page</title>
</head>
<body>
    <h1>Welcome to the Index Page!</h1>
    <a href="/content">Go to Content Page</a>
</body>
</html>

