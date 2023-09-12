from flask import Flask, render_template
import os
# Import Wallet class


STATIC_DIR = os.path.abspath('static')

app = Flask(__name__, static_folder=STATIC_DIR)
app.use_static_for_root = True

# Create a new Wallet object named myWallet


@app.route("/", methods= ["GET", "POST"])
def home():
    # Access myWallet as global
    

    # Call checkConnection() method from myWallet and store result in isConnected variable
    

    # Pass isConnected as isConnected Parameter
    return render_template('index.html',  account=None, balance="No Balance")


if __name__ == '__main__':
    app.run(debug = True, port=4000)
