from flask import Flask, session, redirect, url_for, escape, request
import coffee_dict

app = Flask(__name__)
app.secret_key = b'ITMGT25'
app.config['SESSION_TYPE'] = 'filesystem'
app.run(debug=True, port = 5678)

@app.route('/')
def index():
    session.clear()
    html = '<html><h1>Welcome to Coffee Python!</h1></html>'
    menu_title = '<div> <h2> Coffee Python Menu </h2> '
    
    menu_string = ""
    for product in coffee_dict.products_dict:
        menu_string += "<tr><td>{}</td><td>{}</td></tr>".format(coffee_dict.products_dict[product]['name'], coffee_dict.products_dict[product]['price'])
    
    menu = '<table><tr><th>Name</th><th>Price</th></tr>{}</table></div>'.format(menu_string)

    link = '<div> {} | </div>'.format('<a href="orders">Order Here!</a>')

    return html + menu_title + menu + link

#-----------------------------------------------------------------------------------------------------------------------------------
    # Attempt to process 2nd Page
@app.route('/orders', methods = ['GET','POST'])
def orders():
    html = "<html><h1>Coffee Python Order</h1></html>"
    instruc = "<h4>Kindly Input Code and Quantity from Menu</h4>"
    menu_title2 = '<div> <h2> Coffee Python Menu </h2> '
    
    menu_string2 = ""
    for product in coffee_dict.products_dict:
        menu_string2 += "<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(product, coffee_dict.products_dict[product]['name'], coffee_dict.products_dict[product]['price'])
    
    menu2 = '<table><tr><th>Code</th><th>Name</th><th>Price</th></tr>{}</table></div>'.format(menu_string2)

    #form = '''
        #<form method="POST">
        #Enter Code: <input type="text" name="code"/><br/>
        #Enter Quantity: <input type="number" name="qty"/><br/>
        #<input type="submit"/>
        #</form>
        #'''
    instruc2 = "<h4>Please choose a quantity first then click the product.</h4>"
    form = '''
        <form method="POST">
        Enter Quantity: <input type="number" name="qtyAmr"/><br/>
        <input type="submit" name="americano" value="americano"/><br/>
        Enter Quantity: <input type="number" name="qtyBre"/><br/>
        <input type="submit" name="brewed" value="brewed"/><br/>
        Enter Quantity: <input type="number" name="qtyCap"/><br/>
        <input type="submit" name="cappuccino" value="cappuccino"/><br/>
        <input type="submit"/>
        </form>
        '''

    food_tray = []
    if 'food_tray' not in session:
        session['food_tray'] = []
    else:
        food_tray = session['food_tray']
        
        if request.form.get('americano') == 'americano':
            code = "americano"
            qty=request.form.get("qtyAmr")
        elif request.form.get('brewed') == 'brewed':
            code = "brewed"
            qty=request.form.get("qtyBre")
        elif request.form.get('cappuccino') == 'cappuccino':
            code = "cappuccino"
            qty=request.form.get("qtyCap")

        prc=int(qty)*coffee_dict.products_dict[code]["price"]
        food_tray.append({"code":code,"quantity":qty,"price":prc})
        session['food_tray']=food_tray

        #food_tray = session['food_tray']
        #code=request.form.get("code")
        #qty=request.form.get("qty")
        #prc=int(qty)*coffee_dict.products_dict[code]["price"]
        #food_tray.append({"code":code,"qty":qty,"price":prc})
        #session['food_tray']=food_tray
    # print(session)
    print(food_tray)
    # print(models.products[request.form.get("code")]["name"])
    food_tray_string = ["<div>{}-{}-{}</div>".format(i["code"],i["quantity"],i["price"]) for i in food_tray]
    return html + instruc + menu_title2 + menu2 + form + "".join(food_tray_string)

if __name__ == '__main__':
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True, port = 5678)



''''
    food_tray = ""

    code=request.form.get("code")
    qty=request.form.get("qty")
    food_tray += "<tr><td>{}</td><td>{}</td></tr>".format(coffee_dict.products_dict[code]['name'], qty)

    tray = '''
        #<div>
            #<table>
                #<tr><th>Item</th><th>Quantity</th>
                #{}
           # </table>
        #</div>
    #tray.format(food_tray)

    










