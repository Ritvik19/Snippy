from flask import Flask, render_template, request
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SECRET_KEY"] = "secretkey"
db = SQLAlchemy(app)
admin = Admin(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Post('{self.id}', '{self.title}')"


admin.add_view(ModelView(Post, db.session))


@app.route("/")
def home():
    pnum = request.args.get("page", 1, int)
    return render_template("index.html", posts=Post.query.paginate(pnum, 2))


if __name__ == "__main__":
    app.run(debug=True)
