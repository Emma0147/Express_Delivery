#!/usr/bin/python
""" main file that allows us run our file"""

from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
