from flask import Flask, request
import json
import subprocess

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handleHook():
    pull = request.get_json()

    merged = pull["pull_request"]["merged"]
    branch = pull["pull_request"]["base"]["ref"]

    with open ("pull.txt", "w") as f:
        json.dump(pull, f)

    if merged and branch=="master":
        subprocess.call(["touch", "any_command"])

    return "THIS LITERALLY DOESN'T MATTER. Flask just hates when you don't return"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)
