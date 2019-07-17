from flask import Flask, redirect, url_for, escape, request

import models
app = Flask(__name__)


@app.route('/')
def index():

    html = '<html><h1>Welcome to Coffee Python! {}</h1></html>'

    menu = '<div> {} | </div>'.format('<a href="orders">Orders</a>')

    return html.format("")+menu

if __name__ == '__main__':
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)

@app.route('/orders')
def index():

    html = '<html><h1>Welcome to Coffee Python! {}</h1></html>'

    menu = '<div> {} | </div>'.format('<a href="orders">Orders</a>')

    return html.format("")+menu

if __name__ == '__main__':
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)


@app.route('/products')
def index():

    html = '<html><h1>Welcome to Coffee Python! {}</h1></html>'

    menu = '<div> {} | </div>'.format('<a href="orders">Orders</a>')

    return html.format("")+menu

if __name__ == '__main__':
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)
