from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
        return '''
            <html>
                <head>
                    <title>Flask App</title>
                    <style>
                        body {
                            display: flex;
                            justify-content: center;
                            align-items: center;
                            height: 100vh;
                            margin: 0;
                            font-family: Arial, sans-serif;
                            background-color: #f2f2f2;
                        }
                        h1 {
                            font-size: 48px;
                            color: #333;
                        }
                    </style>
                </head>
                <body>
                    <h1>Welcome to the Flask App!</h1>
                </body>
            </html>
            '''

@app.route('/status')
def status():
    return jsonify({"status": "OK"})

if __name__ == '__main__':
    app.run(debug=True)
    
