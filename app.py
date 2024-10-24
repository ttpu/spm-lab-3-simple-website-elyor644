from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Index Page</title>
    </head>
    <body>
        <h1><marquee>Welcome to the Index Page!</marquee></h1>
        <a href="/content"><centre>Go to Content Page</centre></a>
    </body>
    </html>
    """

@app.route('/content')
def content():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Content Page</title>
    </head>
    <body>
        <h1>This is the Content Page!</h1>
        <a href="/">Go back to Index Page</a>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
