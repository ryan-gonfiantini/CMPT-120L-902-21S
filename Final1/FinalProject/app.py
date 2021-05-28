from flask import Flask, render_template, logging 
app = Flask(__name__)

@app.route('/') 
def home():
    app.logger.info("Moving to the index page"); 
    return render_template ("index.html") 

@app.route('/education')
def school():
    app.logger.info("Moving to the page1 page");  
    return render_template ("page1.html") 

@app.route('/hobbies')
def activites():
    app.logger.info("Moving to the page2 page"); 
    return render_template ("page2.html") 

@app.route('/family')
def myfamily():
    app.logger.info("Moving to the page3 page"); 
    return render_template ("page3.html")  

# Handles 404 errors
@app.errorhandler(404)
def notfound(e): 
    app.logger.error("404 Error. User left website.")
    return render_template("404.html") 

# Runs Flask with file
if __name__ == "__main__":
    app.run()
#End