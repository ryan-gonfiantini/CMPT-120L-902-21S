from flask import Flask, render_template, logging 
app = Flask(__name__)

@app.route('/index') 
def page():
    app.logger.info("Moving to the index page"); 
    return render_template ("index.html") 

@app.route('/page1')
def page1():
    app.logger.info("Moving to the page1 page");  
    return render_template ("page1.html") 

@app.route('/page2')
def page2():
    app.logger.info("Moving to the page2 page"); 
    return render_template ("page2.html") 

@app.route('/page3')
def page3():
    app.logger.info("Moving to the page3 page"); 
    return render_template ("page3.html")  

@app.route('/page4')
def page4():
    app.logger.info("Moving to the page4 page");  
    return render_template ("page4.html") 
