from datetime import datetime, date

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, EmailField, IntegerField, TextAreaField
from wtforms.validators import DataRequired
from models import db, Post

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very secretive and difficult to figure out key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)
bootstrap = Bootstrap(app)

# Create the tables in the database
with app.app_context():
    db.create_all()


class MessageForm(FlaskForm):
    title = StringField('Title:', validators=[DataRequired()])
    message = TextAreaField("Share your story: ", validators=[DataRequired()])

    submit = SubmitField('Post')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/posts')
def submitted():
    posts = Post.query.order_by(Post.date_created.desc()).all()
    return render_template('posts.html', posts=posts)


@app.route('/create', methods=['GET', 'POST'])
def create_post():
    form = MessageForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.message.data
        post = Post(title=title, content=content, date_time_created=datetime.utcnow(), date_created=date.today())
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('submitted'))
    return render_template('create.html', form=form)


@app.route('/about')
def about_us():  # put application's code here
    return render_template('about.html')


@app.route('/resources')
def get_resources():  # put application's code here
    return render_template('resources.html')


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
