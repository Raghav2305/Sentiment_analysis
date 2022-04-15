from flask import request, redirect, url_for, Flask, render_template
import joblib


app = Flask(__name__)

model = joblib.load("my_obj.pkl")



# def load_model():
#     model = joblib.load("my_obj.pkl")
#     return model

# def run_model():
#     model = load_model()
#     st.sidebar.header('User Input Parametrs')
    




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/render', methods = ["POST"])
def render():
    if request.method == "POST":
        text = request.form.get("url")
        
        return render_template('render.html', text = text)

if __name__ == "__main__":
    app.run(debug=True)