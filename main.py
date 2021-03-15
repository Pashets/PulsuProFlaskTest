from app import app, db
from books.blueprint import books

import view

app.register_blueprint(books, url_prefix='/library')

if __name__ == '__main__':
    app.run()
