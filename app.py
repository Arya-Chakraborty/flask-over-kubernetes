from flask import Flask, render_template, redirect, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def view_landing_page():
    if request.method == "GET":
        return render_template("index.html")
    # post request section
    input_json = request.get_json(force=True)
    print("request: ", input_json["question"])
    return_json = {'name':'arya'}
    return jsonify(return_json)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
