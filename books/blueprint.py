from flask import Blueprint, render_template, request
from models import Book, Author
from flask_security import login_required

books = Blueprint('books', __name__, template_folder='templates')


# books = Blueprint('books', __name__)


@books.route('/')
def index():
    q = request.args.get('q')
    if q:
        books_from_db = set(Book.query.filter(Book.title.contains(q)).all())
        authors_from_db = Author.query.filter(Author.name.contains(q)).all()
        for author in authors_from_db:
            books_from_db.update(set(author.books))
    else:
        books_from_db = Book.query.all()
    return render_template('books/index.html', books=books_from_db)
