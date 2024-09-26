from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/crop_yield')
def crop_yield():
    return render_template('crop_yield_meter.html')

@app.route('/about_crop')
def about_crop():
    return render_template('about_crop.html')

if __name__ == '__main__':
    app.run(debug=True)