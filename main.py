from flask import Flask, render_template # type: ignore
  
app = Flask(__name__, template_folder='.')  
  
@app.route("/")  
def web():  
    return render_template('index.html')  
  
if __name__ == "__main__":  
    app.run(debug=True, host="0.0.0.0", port='80')