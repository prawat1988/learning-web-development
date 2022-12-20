from flask import Flask

app = Flask(__name__) 

@app.route("/")
def hello_world():
  return "hello,jovian!"

print(__name__)
if __name__ == "__main__":
  print("i am inside if")
  app.run(host='0.0.0.0',debug=True)