# pip install flask
from flask import Flask, render_template, request, send_file
from main import search_news
from file import save_to_file

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    articles = search_news(keyword)
    return render_template(
        "search.html",
        keyword=keyword,
        articles=enumerate(articles)
    )

@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    articles = search_news(keyword)
    save_to_file(articles)
    return send_file("./ajin_news.csv", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)