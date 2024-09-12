from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
df = pd.read_csv("dictionary.csv")


@app.route("/")
def home():
    return render_template("test.html")


@app.route("/api/v1/<word>")
def about(word):
    for index, row in df.iterrows():
        if row['word'] == word:
            return {
                "definition": row['definition'].title(),
                "word": word
            }


if __name__ == "__main__":
    app.run(debug=True)
