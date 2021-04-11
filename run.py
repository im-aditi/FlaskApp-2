from flask_blog import app


if __name__ == '__main__':
    app.run(debug = True)
# set FLASK_DEBUG=1 in cmd

'''SQL Alchemy lets us represent our database structure as classes which are called models. Each class is a table
in the database. '''