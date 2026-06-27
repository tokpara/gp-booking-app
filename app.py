from flask import Flask #imports flask tool
app = Flask(__name__) # create me a flask application called app

@app.route('/') # / homepage URL, the root it is called an decorator
def home():
    return 'My GP Booking App is working!'

if __name__ == '__main__':
    app.run(debug=True) #shows a detailed error msg when something goes wrong in browser and auto restarts the server everytime you save a change to the code 
    