from flask import Flask

print(__name__)
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello, World guys!"

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5050)
