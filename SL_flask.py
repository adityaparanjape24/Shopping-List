import re
from flask import Flask , redirect , url_for 
from flask.templating import render_template 
from flask import request

final_list = []


def new_item(item_list, item=None): 
    if item is not None and item != "":
        item_list.append(item)


app = Flask(__name__)


@app.route('/')
def shopping_list_application():
    message = request.args.get("message","")
    return render_template("shopping_list_application.html",content={"list":final_list,"message":message})


@app.route('/add_item', methods =["POST"])
def add_item():
    new = request.form["T1"]
    if len(final_list) == 0:
        create_new_list()
    products = final_list[len(final_list)-1]    
    new_item(products, new)
    
    print(f" this is final list {final_list}")
    print(f"this is the length of final list {len(final_list)}")
    return redirect(url_for("shopping_list_application",message="Item Created"))


@app.route('/new_list' , methods = ["POST"])
def new_list():
    create_new_list()
    return redirect(url_for("shopping_list_application",message="New list created"))


def create_new_list():
    new_list = []
    final_list.append(new_list)


if __name__ == '__main__':  
    app.run() 
