from flask import Flask
app = Flask(__name__)
@app.route('/')

def index():
    html = """
    <head>
        <title>Coffee Python</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
        * {
          box-sizing: border-box;
        }

        /* Style the body */
        body {
          font-family: Arial, Helvetica, sans-serif;
          margin: 0;
        }

        /* Header/logo Title */
        .header {
          padding: 50px;
          text-align: center;
          background: #023246;
          color: #d4d4ce;
        }

        /* Increase the font size of the heading */
        .header h1 {
          font-size: 50px;
        }

        /* Style the top navigation bar */
        .navbar {
          overflow: hidden;
          background-color: #d4d4ce;
        }

        /* Style the navigation bar links */
        .navbar a {
          float: left;
          display: block;
          color: #023246;
          text-align: center;
          padding: 14px 20px;
          text-decoration: none;
        }

        /* Right-aligned link */
        .navbar a.right {
          float: right;
        }

        /* Change color on hover */
        .navbar a:hover {
          background-color: #023246;
          color: #d4d4ce;
        }

        /* Column container */
        .row {  
          display: -ms-flexbox; /* IE10 */
          display: flex;
          -ms-flex-wrap: wrap; /* IE10 */
          flex-wrap: wrap;
        }

        /* Create two unequal columns that sits next to each other */
        /* Sidebar/left column */
        .side {
          -ms-flex: 40%; /* IE10 */
          flex: 40%;
          background-color: #287094;
          padding: 20px;
        }

        /* Main column */
        .main {   
          -ms-flex: 60%; /* IE10 */
          flex: 60%;
          background-color: #f6f6f6;
          padding: 20px;
        }

        /* Fake image, just for this example */
        .fakeimg {
          background-color: #023246;
          width: 100%;
          padding: 20px;
        }

        /* Footer */
        .footer {
          padding: 10px;
          text-align: center;
          background: #f6f6f6;
        }

        /* Responsive layout - when the screen is less than 700px wide, make the two columns stack on top of each other instead of next to each other */
        @media screen and (max-width: 700px) {
          .row {   
            flex-direction: column;
          }
        }

        /* Responsive layout - when the screen is less than 400px wide, make the navigation links stack on top of each other instead of next to each other */
        @media screen and (max-width: 400px) {
          .navbar a {
            float: none;
            width: 100%;
          }
        }
        </style>
    </head>
    <body>

        <div class="header">
          <h1>Coffee Python</h1>
        </div>
        
        <div class="navbar">
          <a href="#">Cart</a>
          <a href="#" class="right">Sign In</a>
          <a href="#" class="right">Create an Account</a>
        </div>

        <div class="row">
          <div class="side">
            <h2>Coffee Python Menu</h2>
            <h5>*Insert Menu Here*</h5>
          </div>
          
          <div class="main">
            <h2>TITLE HEADING</h2>
            <h5>Enter Code: </h5>
            <h5>Enter Quantity: </h5>
          </div>
        </div>

        
        <div class="footer">
          <p>This is a footer if you guys want to put anything here.</p>
        </div>

    </body>"""
    
    return html