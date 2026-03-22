from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def dashboard():
    data = {
        "status": "SUCCESS",
        "last_build": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "vulnerabilities": "0 CRITICAL",
        "app_status": "Running"
    }
    return render_template("dashboard.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
