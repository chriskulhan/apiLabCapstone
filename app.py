#import Flask - framework we are using for our website
from flask import Flask, render_template

#create a new Flask app 
app = Flask(__name__)

#create rout for the home page (index.html)
@app.route('/')

#create the index method - this will assign the API key for 
#the map on the home page
def index():
    #Using Dr. Mary's API key (never really do this!)
    api_key = "AIzaSyCdtcEmCii8bNySWzGtpwwWmwBDjp2nKi4"
    return render_template('index.html', api_key=api_key)   

#add the main method method - this method is called when the app runs
if __name__ == '__main__':
    #run the app in debug mode
    app.run(debug=True)
    #debug mode will show errors in the browser

#run the app
