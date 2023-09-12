from flask import Flask, render_template, request, redirect
import os
from time import time
from wallet import Wallet
from wallet import Account

STATIC_DIR = os.path.abspath('static')

app = Flask(__name__, static_folder=STATIC_DIR)
app.use_static_for_root = True

myWallet =  Wallet()
# Define account variable and set it ot None


@app.route("/", methods= ["GET", "POST"])
def home():
    # Access account as global
    global myWallet

    isConnected = myWallet.checkConnection()
    # Create balance variable and set it to "No Balance"
    

    # Check if account exits 
    
        # Set the balance to 0
        
   
    # Pass account and balance in respective attributes
    return render_template('index.html', isConnected=isConnected,  account= None, balance = None)
   
# Create a rout "/createAccount"

# Define createAccount() function

    # Access myWallet and account a global
    
    # Create a new object using Account class and store it in global account variable
    
    # redirect to home i.e. "/" path
    

if __name__ == '__main__':
    app.run(debug = True, port=4000)
