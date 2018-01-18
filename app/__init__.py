from flask import Flask, request, render_template, jsonify
# import numpy as np
# import pandas as pd
# import sys
#
# import constants as C
import json

app = Flask(__name__)

# # Load model from pickle file and then retrieve the booked data
# with open('../model/model.pkl', 'rb') as f:
#     model = pickle.load(f)
# engine = create_engine(C.ENGINE)
# df = pd.read_sql_query("SELECT * FROM booked", con=engine)


@app.route('/')
def index():
    """
    Renders index.html template for the main page of the app.
    """
    return render_template('index.html')

@app.route('/graph/')
def graph():
    """
    Renders graph.html.
    """
    return render_template('graph.html')


@app.route('/graph_minus_node/')
def graph_minus_node():
    """
    Renders graph_minus_node.html.
    """
    return render_template('graph_minus_node.html')

@app.route('/graph_minus_two_nodes/')
def graph_minus_two_nodes():
    """
    Renders graph_minus_two_nodes.html.
    """
    return render_template('graph_minus_two_nodes.html')

@app.route('/get_graph/', methods=['GET'])
def get_graph():
    filename = "../{}".format(request.args["json"])
    with open(filename, 'r') as f:
        datastore = json.load(f)
    return jsonify(datastore)

if __name__ == '__main__':
    app.run(debug=True)