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

#-------------------------------------------------------------------------------------------------
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
        <input type="submit" name="Remove" value = "Remove"/><input type="number" name="remAmr"/><br/>
        
        Enter Quantity: <input type="number" name="qtyBre"/><br/>
        <input type="submit" name="brewed" value="brewed"/><br/>
        
        Enter Quantity: <input type="number" name="qtyCap"/><br/>
        <input type="submit" name="cappuccino" value="cappuccino"/><br/>
        
        Enter Quantity: <input type="number" name="qtyEsp"/><br/>
        <input type="submit" name="espresso" value="espresso"/><br/>
        
        Enter Quantity: <input type="number" name="qtyLat"/><br/>
        <input type="submit" name="latte" value="latte"/><br/>
        
        Enter Quantity: <input type="number" name="qtyFra"/><br/>
        <input type="submit" name="frappuccino" value="frappuccino"/><br/>
        
        Enter Quantity: <input type="number" name="qtyMoc"/><br/>
        <input type="submit" name="mocha" value="mocha"/><br/>
        
        Enter Quantity: <input type="number" name="qtyMac"/><br/>
        <input type="submit" name="macchiato" value="macchiato"/><br/>
        
        Enter Quantity: <input type="number" name="qtyAff"/><br/>
        <input type="submit" name="affogato" value="affogato"/><br/>
        
        Enter Quantity: <input type="number" name="qtyCor"/><br/>
        <input type="submit" name="cortado" value="cortado"/><br/>
        
        Enter Quantity: <input type="number" name="qtyBla"/><br/>
        <input type="submit" name="black" value="black"/><br/>
        
        Enter Quantity: <input type="number" name="qtyIce"/><br/>
        <input type="submit" name="iced" value="iced"/><br/>
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
            rem=request.form.get("remAmr")
            if request.form.get("Remove") == 'Remove' and int(rem) > 0:
                qty=-(int(rem))
                
        elif request.form.get('brewed') == 'brewed':
            code = "brewed"
            qty=request.form.get("qtyBre")
        elif request.form.get('cappuccino') == 'cappuccino':
            code = "cappuccino"
            qty=request.form.get("qtyCap")
        elif request.form.get('espresso') == 'espresso':
            code = "espresso"
            qty=request.form.get("qtyEsp")
        elif request.form.get('latte') == 'latte':
            code = "latte"
            qty=request.form.get("qtyLat")
        elif request.form.get('frappuccino') == 'frappuccino':
            code = "frappuccino"
            qty=request.form.get("qtyFra")
        elif request.form.get('mocha') == 'mocha':
            code = "mocha"
            qty=request.form.get("qtyMoc")
        elif request.form.get('macchiato') == 'macchiato':
            code = "macchiato"
            qty=request.form.get("qtyMac")
        elif request.form.get('affogato') == 'affogato':
            code = "affogato"
            qty=request.form.get("qtyAff")
        elif request.form.get('cortado') == 'cortado':
            code = "cortado"
            qty=request.form.get("qtyCor")
        elif request.form.get('black') == 'black':
            code = "black"
            qty=request.form.get("qtyBla")
        elif request.form.get('iced') == 'iced':
            code = "iced"
            qty=request.form.get("qtyIce")

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
    
    link2 = '<div> {} | </div>'.format('<a href="cinfo">Proceed to Customer Information</a>')
    
    return html + instruc2 + menu_title2 + menu2 + form + "".join(food_tray_string) + link2

if __name__ == '__main__':
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True, port = 5678)


#-------------------------------------------------------------------------------------------------
    # Attempt to process 3rd Page
@app.route('/cinfo', methods = ['GET','POST'])
def cinfo():
    html = "<html><h1>Customer Information</h1></html>"
    instruc3 = "<h4>Kindly input the following information</h4>"
    required = "<h5>All fields are required</h5>"
    message = "<h4>Thank You for submitting your information!</h4>"

    form = '''
        <form method="POST">
        First Name: <input type="text" name="fname" required="required"/><br/>
        Last Name: <input type="text" name="lname" required="required"/><br/>
        Email: <input type="email" name="email" required="required"/><br/>
        Contact Number: <input type="number" name="cnumber" required="required"/><br/>
        Delivery Address: <input type="text" name="address" required="required"/><br/>
        <input type="submit"/>
        </form>
        '''
        
    customer_info = []
    if 'customer_info' not in session:
        session['customer_info'] = []
    else:
        customer_info = session['customer_info']
        fname=request.form.get("fname")
        lname=request.form.get("lname")
        email=request.form.get("email")
        cnumber=request.form.get("cnumber")
        address=request.form.get("address")
        # message="Thank You for submitting your information!"
        
        customer_info.append({"fname":fname,"lname":lname,"email":email,"cnumber":cnumber,"address":address})
        session['customer_info']=customer_info
    # print(session)
    print(customer_info)
    
    customer_info_string = ["<div>{}&nbsp;{}<br/>{}<br/>{}<br/>{}</div>".format(i["fname"],i["lname"],i["email"],i["cnumber"],i["address"]) for i in customer_info]

    ####
    
    #form2 = '''
    #<form method="POST">
    #<input type="submit" name="address" value="Confirm"/><br/>
    #</form>
    #'''
    
    message_after = []
    if 'message_after' not in session:
        session['message_after'] = []
    else:
        message_after = session['message_after']
        
        address=request.form.get("address")
        # message="Thank You for submitting your information!"
        
        message_after.append({"message":message})
        session['message_after']=message_after
    # print(session)
    print(message_after)
    
    
    message_after_string = ["<div>{}</div>".format(i["message"]) for i in message_after]
    
    return html + instruc3 + required + form + "".join(customer_info_string) + "".join(message_after_string)

if __name__ == '__main__':
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True, port = 5678)
   

'''''
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
