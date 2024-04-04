from flask import Flask
print( "Testing the flask app")
app = Flask(__name__)
@app.route("/")
def helloworld():
    return "Hello World!"
if __name__ == "__main__":
    app.run()