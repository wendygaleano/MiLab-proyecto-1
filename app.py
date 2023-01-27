from flask import Flask, render_template

app = Flask(__name__)

# pagina principal


@app.route('/')
def index1():
    return render_template("index1.html")
# pag secundaria


@app.route('/4enralla')
def index():
    return render_template("4enralla.py")
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
app=Flask(__name__,template_folder='index.html')

