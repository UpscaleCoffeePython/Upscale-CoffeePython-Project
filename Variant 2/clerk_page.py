from flask import Flask, session, redirect, url_for, escape, request
import coffee_dict, clerk_dict

app = Flask(__name__)
app.secret_key = b'ITMGT25'
app.config['SESSION_TYPE'] = 'filesystem'
app.run(debug=True, port = 5678)

@app.route('/')
def index():
    session.clear()
    html = '''<html><style>
    body {background-color: #f5edda; text-align:center}
    h1, h2 { font-family: Quicksand; text-align: center }
    table {border-collapse: collapse; font-family: Quicksand} table, th, td { border: 1px solid black; padding: 5px; text-align: center}
    a:link, a:visited {display: inline-block; border-radius: 4px; background-color: #66462f; border: none; color: #f5edda; text-align: center; font-size: 20px; padding: 10px; width: 200px; transition: all 0.5s; cursor: pointer; margin: 5px; font-family: Quicksand;}
    a:link span {cursor: pointer; display: inline-block; position: relative; transition: 0.5s;}
    a:link span:after {font-size: 10px; content: '>>'; position: absolute; opacity: 0; top: 5px;right: -40px; transition: 0.5s;}
    a:hover span {padding-right: 25px;}
    a:hover span:after {opacity: 1;right: -10px;}
   
    </style>
    <br/>
    <h1>Welcome to Coffee Python!</h1></html>'''
    menu_title = '<div> <h2> Coffee Python Menu </h2> '
    
    menu_string = ""
    for product in coffee_dict.products_dict:
        menu_string += "<tr><td>{}</td><td>{}</td></tr>".format(coffee_dict.products_dict[product]['name'], coffee_dict.products_dict[product]['price'])
    
    menu = '<table align="center"><tr><th>Name</th><th>Price</th></tr>{}</table></div></br>'.format(menu_string)

    link = '<div> {} </div>'.format('<a href="login" style="vertical-align:middle"><span>Order Here!</span></a>')

    return html + menu_title + menu + link
#-------------------------------------------------------------------------------------------------
    # Attempt to process Login Page
@app.route('/login', methods = ['GET','POST'])
def login():
    html = html = """<html><style>
    body {background-color: #66462f; text-align:center}
    div {font-family: Quicksand; text-align: center; font-weight: 12px; color: #f5edda}
    h1, h2, h3, h4, h5 { font-family: Quicksand; text-align: center; color:#f5edda }
    
    input[type=text], input[type=email], input[type=number] {
  width: 200px;
  box-sizing: border-box;
  border: 2px solid #f5edda;
  border-radius: 25px;
  background-color: #66462f;
  background-repeat: no-repeat;
  padding: 12px 20px 12px 30px;
  -webkit-transition: width 0.4s ease-in-out;
  transition: width 0.4s ease-in-out;
}

    input[type=submit] {align: middle; background-color: #f5edda; color: #66462f; border: none; padding: 5px; margin: 4px 2px; font-family: Quicksand; border-radius: 25px;} 
    input[type=submit]:hover {background-color: #66462f; color: #f5edda; border-radius: 25px;} 

    input[type=text]::placeholder, input[type=email]::placeholder, input[type=number]::placeholder {
    color: #f5edda;
    font-family: Quicksand;}

    input[type=text]:focus, input[type=email]:focus, input[type=number]:focus {
  width: 50%;
}
    
    a:link, a:visited {display: inline-block; border-radius: 4px; background-color: #f5edda; border: none; color: #66462f; text-align: center; font-size: 15px; padding: 10px; width: 250px; transition: all 0.5s; cursor: pointer; margin: 5px; font-family: Quicksand;}
    a:link span {cursor: pointer; display: inline-block; position: relative; transition: 0.5s;}
    a:link span:after {font-size: 10px; content: '>>'; position: absolute; opacity: 0; top: 2px;right: -40px; transition: 0.5s;}
    a:hover span {padding-right: 25px;}
    a:hover span:after {opacity: 1;right: -10px;}
    
    </style><br/><h1>Log In</h1><br/></html>"""

    form = '''
        <form method="POST">
        <input type="text" name="password" required="required" placeholder="Clerk Code"/><br/>
        <input type="submit"/>
        </form>
        '''
    #messagee = "<h4>You are logged in</h4>"
    logged_in = []
    if 'logged_in' not in session:
        session['logged_in'] = []
    else:
        logged_in = session['logged_in']
        password = request.form.get("password")
        name = clerk_dict.clerk_dict[password]["Clerk Name"]
        sales = clerk_dict.clerk_dict[password]["Total Sales"]
        comm = clerk_dict.clerk_dict[password]["Total Commission"]
        logged_in.append({"Name":name, "Total Sales":sales, "Total Commission":comm})

    session['logged_in']=logged_in
    logged_in_string = ["<div>Welcome, <b>{}</b>!<br/><br/> Please proceed to the <br/>{}</div><br/>".format(i["Name"],'<a href="interface" style="vertical-align:middle"><span>Interface Page.</span></a><br/>') for i in logged_in]   
    
    #message_after_string = ["<div>{}</div>".format(i["message"]) for i in message_after]
    #logged_in_string = ["<div>Clerk Name: <b>{}</b> | Total Sales: <b>{}</b> | Total Commission: <b>{}</b></div><br/>".format(i["Name"],i["Total Sales"],i["Total Commission"]) for i in logged_in]
    #linkk = '<div> {} </div>'.format('<a href="interface" style="vertical-align:middle"><span>Proceed to Order Page</span></a><br/>')
    return html + form + "".join(logged_in_string)
#-------------------------------------------------------------------------------------------------
    # Attempt to process Interface Page

@app.route('/interface', methods = ['GET','POST'])
def interface():
    html = """<html><style>
    body {background-color: #66462f; text-align:center}
    h1, h2, h3, h4 { font-family: Quicksand; text-align: center ; color:#f5edda}
   
    a:link, a:visited {display: inline-block; border-radius: 4px; background-color: #f5edda; border: none; color: #66462f; text-align: center; font-size: 15px; padding: 10px; width: 250px; transition: all 0.5s; cursor: pointer; margin: 5px; font-family: Quicksand;}
    a:link span {cursor: pointer; display: inline-block; position: relative; transition: 0.5s;}
    a:link span:after {font-size: 10px; content: '>>'; position: absolute; opacity: 0; top: 5px;right: -40px; transition: 0.5s;}
    a:hover span {padding-right: 25px;}
    a:hover span:after {opacity: 1;right: -10px;}
   
    </style><br/><h1>Clerk Interface</h1><br/></html>"""

    logged_in = session['logged_in']
    name = ["<div><h3>Let's get to Work {}</h3></div>".format(i["Name"]) for i in logged_in]
    sales = ["<div><h4>Your Current Sales for the day is <b>{}</b></h4></div>".format(i["Total Sales"]) for i in logged_in]
    commission = ["<div><h4>Your Current Commission for the day is <b>{}</b></h4><br/></div>".format(i["Total Commission"]) for i in logged_in]
    session['logged_in']=logged_in

    message = "<div><h2>Let's take more orders to raise our Commission!</h2></div>"
    linkkk = '<div> {} </div>'.format('<a href="orders" style="vertical-align:middle"><span>Proceed to Orders Page</span></a><br/>')
    return html + "".join(name) + "".join(sales) + "".join(commission) + message + linkkk
#-------------------------------------------------------------------------------------------------
    # Attempt to process 2nd Page
@app.route('/orders', methods = ['GET','POST'])
def orders():
    html = """<html><style>
    body {background-color: #f5edda; text-align:center}
    div {font-family: Quicksand; text-align: center; font-weight: 12px}
    h1, h2, h3, h4 { font-family: Quicksand; text-align: center }
    table {border-collapse: collapse; font-family: Quicksand} table, th, td { border: 1px solid black; padding: 5px; text-align: center}
    
    input[type=submit] {align: middle; background-color: #CA9E7B; color: #F5EDDA; border: none; padding: 5px; margin: 4px 2px; font-family: Quicksand; border-radius: 25px; font-size: 16px} 
    input[type=submit]:hover {background-color: #F5EDDA; color: #363636; border-radius: 25px; font-size: 16px} 
    
    input[type=number] {
  width: 100px;
  box-sizing: border-box;
  border: 2px solid #98694f;
  border-radius: 25px;
  background-color: #f5edda;
  background-repeat: no-repeat;
  padding: 5px 20px 5px 20px;
  -webkit-transition: width 0.4s ease-in-out;
  transition: width 0.4s ease-in-out;}
  
    a:link, a:visited {display: inline-block; border-radius: 4px; background-color: #66462f; border: none; color: #f5edda; text-align: center; font-size: 12px; padding: 10px; width: 250px; transition: all 0.5s; cursor: pointer; margin: 5px; font-family: Quicksand;}
    a:link span {cursor: pointer; display: inline-block; position: relative; transition: 0.5s;}
    a:link span:after {font-size: 8px; content: '>>'; position: absolute; opacity: 0; top: 2px;right: -40px; transition: 0.5s;}
    a:hover span {padding-right: 25px;}
    a:hover span:after {opacity: 1;right: -10px;}


    input[type=number]::placeholder {
color: #98694f;
font-family: Quicksand}

    </style>
    <br/>
    <h1>Coffee Python Order</h1></html>"""
    
    instruc = "<h4>Kindly Input Code and Quantity from Menu</h4>"
    menu_title2 = '<div> <h2> Coffee Python Menu </h2> '
    
    menu_string2 = ""
    for product in coffee_dict.products_dict:
        menu_string2 += "<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(product, coffee_dict.products_dict[product]['name'], coffee_dict.products_dict[product]['price'])
    
    menu2 = '<table align="center"><tr><th>Code</th><th>Name</th><th>Price</th></tr>{}</table></div><br/>'.format(menu_string2)

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
        <input type="number" name="qty" min="1" placeholder="Qty"/>
        <input type="number" name="rem" min="1" placeholder="Rmv"/><br/>
        <br/>
        <input type="submit" name="americano" value="americano"/>
        <input type="submit" name="brewed" value="brewed"/>
        <input type="submit" name="cappuccino" value="cappuccino"/>
        <input type="submit" name="espresso" value="espresso"/><br/>
        <br/>
        <input type="submit" name="latte" value="latte"/>
        <input type="submit" name="frappuccino" value="frappuccino"/>
        <input type="submit" name="mocha" value="mocha"/>
        <input type="submit" name="macchiato" value="macchiato"/><br/>
        <br/>
        <input type="submit" name="affogato" value="affogato"/>
        <input type="submit" name="cortado" value="cortado"/>
        <input type="submit" name="black" value="black"/>
        <input type="submit" name="iced" value="iced"/><br/>
        </form>
        '''

    food_tray = []
    code = "brewed"
    qty = 0
    if 'food_tray' not in session:
        session['food_tray'] = []
    else:
        food_tray = session['food_tray']
        
        #qty=request.form.get("qty")
        
        if request.form.get('americano') == 'americano':
            code = "americano"
            #qty=request.form.get("qty")
            if request.form.get("qty") != '':
                qty=int(request.form.get("qty"))
            elif request.form.get("rem") != '':
                qty=-int(request.form.get("rem"))
        elif request.form.get('brewed') == 'brewed':
            code = "brewed"
            if request.form.get("qty") != '':
                qty=int(request.form.get("qty"))
            elif request.form.get("rem") != '':
                qty=-int(request.form.get("rem"))
        elif request.form.get('cappuccino') == 'cappuccino':
            code = "cappuccino"
            if request.form.get("qty") != '':
                qty=int(request.form.get("qty"))
            elif request.form.get("rem") != '':
                qty=-int(request.form.get("rem"))
        elif request.form.get('espresso') == 'espresso':
            code = "espresso"
            if request.form.get("qty") != '':
                qty=int(request.form.get("qty"))
            elif request.form.get("rem") != '':
                qty=-int(request.form.get("rem"))
        elif request.form.get('latte') == 'latte':
            code = "latte"
            if request.form.get("qty") != '':
                qty=int(request.form.get("qty"))
            elif request.form.get("rem") != '':
                qty=-int(request.form.get("rem"))
        elif request.form.get('frappuccino') == 'frappuccino':
            code = "frappuccino"
            if request.form.get("qty") != '':
                qty=int(request.form.get("qty"))
            elif request.form.get("rem") != '':
                qty=-int(request.form.get("rem"))
        elif request.form.get('mocha') == 'mocha':
            code = "mocha"
            if request.form.get("qty") != '':
                qty=int(request.form.get("qty"))
            elif request.form.get("rem") != '':
                qty=-int(request.form.get("rem"))
        elif request.form.get('macchiato') == 'macchiato':
            code = "macchiato"
            if request.form.get("qty") != '':
                qty=int(request.form.get("qty"))
            elif request.form.get("rem") != '':
                qty=-int(request.form.get("rem"))
        elif request.form.get('affogato') == 'affogato':
            code = "affogato"
            if request.form.get("qty") != '':
                qty=int(request.form.get("qty"))
            elif request.form.get("rem") != '':
                qty=-int(request.form.get("rem"))
        elif request.form.get('cortado') == 'cortado':
            code = "cortado"
            if request.form.get("qty") != '':
                qty=int(request.form.get("qty"))
            elif request.form.get("rem") != '':
                qty=-int(request.form.get("rem"))
        elif request.form.get('black') == 'black':
            code = "black"
            if request.form.get("qty") != '':
                qty=int(request.form.get("qty"))
            elif request.form.get("rem") != '':
                qty=-int(request.form.get("rem"))
        elif request.form.get('iced') == 'iced':
            code = "iced"
            if request.form.get("qty") != '':
                qty=int(request.form.get("qty"))
            elif request.form.get("rem") != '':
                qty=-int(request.form.get("rem"))
        sub_total=0
        prc=int(qty)*coffee_dict.products_dict[code]["price"]
        
        checker=next((item.get('code') for item in session['food_tray'] if item["code"] == coffee_dict.products_dict[code]["name"]), False)
        checker_quan=next((item.get('quantity') for item in session['food_tray'] if item["code"] == coffee_dict.products_dict[code]["name"]), False)
        #if checker == code:
            #sub_total=qty+int(checker_quan)
            #new_prc=int(sub_total)*coffee_dict.products_dict[code]["price"]
            #for i in range(len(food_tray)):
                #if food_tray[i]['code'] == checker:
                    #del food_tray[i]
                    #break
        if checker == coffee_dict.products_dict[code]["name"]:
            if qty < 0 and -qty > int(checker_quan):
                sub_total=0+int(checker_quan)
                new_prc=int(sub_total)*coffee_dict.products_dict[code]["price"]
                for i in range(len(food_tray)):
                    if food_tray[i]['code'] == checker:
                        del food_tray[i]
                        break
            else:
                sub_total=qty+int(checker_quan)
                new_prc=int(sub_total)*coffee_dict.products_dict[code]["price"]
                for i in range(len(food_tray)):
                    if food_tray[i]['code'] == checker:
                        del food_tray[i]
                        break
            #session['food_tray'].remove({"code":checker,"quantity":checker_quan,"price":prc})
            #for d in session['food_tray']:
            food_tray.append({"code":coffee_dict.products_dict[code]["name"],"quantity":sub_total,"price":new_prc})
            session['food_tray']=food_tray
        
        elif checker != coffee_dict.products_dict[code]["name"]:
            if qty < 0:
                qty = 0
                prc = 0
            else:
                qty = qty
            food_tray.append({"code":coffee_dict.products_dict[code]["name"],"quantity":qty,"price":prc})
            session['food_tray']=food_tray
        
        for i in range(len(food_tray)):
                    if food_tray[i]['quantity'] == 0:
                        del food_tray[i]
                        break
        
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
    food_tray_string = ["<div>Product: <b>{}</b> | Quantity: <b>{}</b> | Price: <b>{}</b></div><br/>".format(i["code"],i["quantity"],i["price"]) for i in food_tray]
    
    link7 = '<div> {} </div>'.format('<a href="summary" style="vertical-align:middle"><span>Proceed to Summary</span></a>')
    return html + instruc2 + menu_title2 + menu2 + form + "".join(food_tray_string) + link7
#-------------------------------------------------------------------------------------------------
    # Attempt to process 4th Page
    
@app.route('/summary', methods = ['GET','POST'])
def summary():
    html = """<html><style>
    body {background-color: #f5edda; text-align:center}
    div {font-family: Quicksand; text-align: center; font-weight: 12px}
    h1, h2, h3, h4 { font-family: Quicksand; text-align: center }
    table {border-collapse: collapse; font-family: Quicksand} table, th, td { border: 1px solid black; padding: 5px; text-align: center}
    
    
    input[type=text], input[type=email], input[type=number] {
  width: 150px;
  box-sizing: border-box;
  border: 2px solid #98694f;
  border-radius: 25px;
  background-color: #f5edda;
  background-repeat: no-repeat;
  padding: 5px 20px 5px 30px;
  -webkit-transition: width 0.4s ease-in-out;
  transition: width 0.4s ease-in-out;
}
    
    input[type=submit] {align: middle; background-color: #CA9E7B; color: #F5EDDA; border: none; padding: 5px; margin: 4px 2px; font-family: Quicksand; border-radius: 25px; font-size: 16px} 
    input[type=submit]:hover {background-color: #F5EDDA; color: #363636; border-radius: 25px; font-size: 16px} 
    
    input[type=text]::placeholder, input[type=email]::placeholder, input[type=number]::placeholder {
    color: #98694f;
    font-family: Quicksand;}

    input[type=text]:focus, input[type=number]:focus, input[type=number]:focus {
  width: 50%;}
    
    input[type=number] {
  width: 200px;
  box-sizing: border-box;
  border: 2px solid #98694f;
  border-radius: 25px;
  background-color: #f5edda;
  background-repeat: no-repeat;
  padding: 5px 20px 5px 30px;
  -webkit-transition: width 0.4s ease-in-out;
  transition: width 0.4s ease-in-out;}
  
    a:link, a:visited {display: inline-block; border-radius: 4px; background-color: #66462f; border: none; color: #f5edda; text-align: center; font-size: 12px; padding: 10px; width: 250px; transition: all 0.5s; cursor: pointer; margin: 5px; font-family: Quicksand;}
    a:link span {cursor: pointer; display: inline-block; position: relative; transition: 0.5s;}
    a:link span:after {font-size: 8px; content: '>>'; position: absolute; opacity: 0; top: 2px;right: -40px; transition: 0.5s;}
    a:hover span {padding-right: 25px;}
    a:hover span:after {opacity: 1;right: -10px;}


    input[type=number]::placeholder {
color: #98694f;
font-family: Quicksand}
    
    </style>
    <br/>
    <h1>Order Summary</h1></html>"""
    instruc4 = "<h4>Kindly check the following information</h4>"
        
    logged_in = session['logged_in']
    clerk_info_string = ["<br/><div>Clerk Name: {}<br/>Total Sales: {}<br/>Total Commission {}</div><br/>".format(i["Name"],i["Total Sales"],i["Total Commission"]) for i in logged_in]
        
    food_tray = session['food_tray']
    food_tray_string = ["<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(i["code"],i["quantity"],i["price"]) for i in food_tray]
    food_tray_final = '<table align="center"><tr><th>Code</th><th>Quantity</th><th>Price</th></tr>{}</table><br/>'.format(food_tray_string)

    total_cart = 0
    for i in food_tray:
        total_cart += i["price"]

    total_string = "<div> Total Amount for your Order is: <b>{}</b></div><br/>".format(total_cart)

    wallet_form = '''
        <form method="POST">
        <input type="number" name="amount" required="required" placeholder="Payment Amount"/><br/><br/>
        <input type="text" name="method" required="required" placeholder="Method"/><br/><br/>
        <input type="submit"/>
        </form>
        '''
        
    customer_wallet = []
    if 'customer_wallet' not in session:
        session['customer_wallet'] = []
    else:
        customer_wallet = session['customer_wallet']
        amount=request.form.get("amount")
        method=request.form.get("method")
        
        customer_wallet.append({"Amount":amount,"Method":method})
        session['customer_wallet']=customer_wallet
    # print(session)
    print(customer_wallet)
    
    customer_wallet_string = ["<div>Your Cash Amount is: <b>{}</b> paid through <b>{}</b></div><br/>".format(i["Amount"],i["Method"]) for i in customer_wallet]

    if bool(customer_wallet) == False:
        change_string = "<div> Allow us to calculate for your change by inputting your amount</div><br/>"
    else:
        change = int(customer_wallet[0]["Amount"]) - total_cart
        change_string = "<div> Your Change for the Order is: <b>{}</b> </div></br>".format(change)
    
    link4 = '<div> {} </div>'.format('<a href="orders">Go back to Orders</a>')
    link6 = '<div> {} </div>'.format('<a href="checkout" style="vertical-align:middle"><span>Proceed to Checkout</span></a>')
    
    return html + instruc4 + "".join(clerk_info_string) + "".join(food_tray_final) + total_string + wallet_form + "".join(customer_wallet_string) + "".join(change_string) + link4 + link6
#-------------------------------------------------------------------------------------------------
    # Attempt to process 5th Page
    
@app.route('/checkout', methods = ['GET','POST'])
def checkout():
    html = """<html><style>
    body {background-color: #4A2615; text-align:center}
    div {font-family: Quicksand; text-align: center; font-weight: 12px; color:#f5edda}
    h1, h2, h3, h4, h5 { font-family: Quicksand; text-align: center; color:#f5edda }
    table {border-collapse: collapse; font-family: Quicksand} 
    table, th, td,tr {border: 1px solid #f5edda; padding: 5px; text-align: center; color: #f5edda}
    </style>
    <br/>
    <h1>Coffee Python</h1></html>"""
    final_message = "<h2>Order Receipt</h2>"    
    
    
    logged_in = session['logged_in']
    clerk_info_string = ["<br/><div>Clerk Name: {}<br/>Total Sales: {}<br/>Total Commission {}</div><br/>".format(i["Name"],i["Total Sales"],i["Total Commission"]) for i in logged_in]
    
    
    food_tray = session['food_tray']
    food_tray_string = ["<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(i["code"],i["quantity"],i["price"]) for i in food_tray]
  
    total_cart = 0
    for i in food_tray:
        total_cart += i["price"]
   
    
    food_tray_final = '<table align="center"><tr><th>Code</th><th>Quantity</th><th>Price</th></tr>{}<tr><td><b>Total</b></td> <td></td><td><b>{}</b></td></tr></table><br/>'.format(food_tray_string,total_cart)
   
    customer_wallet_string = ["<div>Amount Paid: <b>{}</b> through <b>{}</b></div><br/>".format(i["Amount"],i["Method"]) for i in session['customer_wallet']]

    if bool(session['customer_wallet']) == False:
        change_string = "<div> Allow us to calculate for your change by inputting your amount</div>"
    else:
        change = int(session['customer_wallet'][0]["Amount"]) - total_cart
        change_string = "<div> Total Change: <b>{}</b> </div><br/>".format(change)
    
    return html + final_message + "".join(food_tray_final) + "".join(customer_wallet_string) + "".join(change_string) + "".join(clerk_info_string) 

if __name__ == '__main__':
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True, port = 5678)