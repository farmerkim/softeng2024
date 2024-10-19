from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

def get_blog_posts():
    df = pd.read_csv('blog_posts.csv')
    return df.to_dict(orient='records')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/blog')
def blog():
    posts = get_blog_posts()
    return render_template('blog.html', posts=posts)

@app.route('/crop_yield_meter')
def crop_yield():
    return render_template('crop_yield_meter.html')

@app.route('/about_crop')
def about_crop():
    return render_template('about_crop.html')

if __name__ == '__main__':
    app.run(debug=True)