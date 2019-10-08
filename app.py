from flask import Flask, jsonify , render_template, request
import os, optparse,sys
import yaml

developer = os.getenv("DEVELOPER", "Me")
environment=os.getenv("ENVIRONMENT","development")

app = Flask(__name__)
with open("links.yaml", 'r',encoding='utf-8') as stream:
    try:
        data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)


@app.route('/')
def inf():
        return render_template("index.html" , data=data)



if __name__ == "__main__":
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    app.run(host="0.0.0.0",debug=debug)
