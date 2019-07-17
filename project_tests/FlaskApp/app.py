from flask import Flask, session
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

@app.route('/orders', methods = ['GET','POST'])
def orders():
    html = "<html><h1>Orders</h1>{}<br/>{}</html>"
    form = '''
        <form method="POST">
        Enter Code: <input type="text" name="code"/><br/>
        Enter Qty: <input type="text" name="qty"/><br/>
        <input type="submit"/>
        </form>
    '''
    if 'food_tray' not in session:
        session['food_tray'] = []

    food_tray = session['food_tray']
    code=request.form.get("code")
    qty=request.form.get("qty")
    food_tray.append({"code":code,"qty":qty})
    session['food_tray']=food_tray
    # print(session)
    print(food_tray)
    print(models.products["cappuccino"]["name"])
    # print(models.products[request.form.get("code")]["name"])
    food_tray_string = ["<div>{}-{}</div>".format(i["code"],i["qty"]) for i in food_tray]
    return html.format(form,"".join(food_tray_string))
