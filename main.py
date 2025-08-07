from flask import Flask
app2=Flask(_name_)

@app2.route("/")
def hellow():
  return 'Hellow World from GitHub!'
