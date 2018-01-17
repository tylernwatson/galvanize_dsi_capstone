from flask import Flask, request, render_template, jsonify
import numpy as np
import pandas as pd
import sys

import constants as C

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
    return render_template(
        'index.html', data=df.to_html(index=False), locations=np.sort(df["name"].unique()),
        months=df["month"].unique(), revenue="${:,}".format(int(df[df["prediction"] == 0]["price"].sum())),
        total_count="{:,}".format(total_count), cancel_count="{:,}".format(cancel_count),
        percent_cancelled="{:,.0f}%".format(100 * cancel_count / total_count)
    )

@app.route('/graph/')
def new_reservation():
    """
    Renders graph.html.
    """
    return render_template('graph.html')


@app.route('/graph_minus_node/')
def new_reservation():
    """
    Renders graph_minus_node.html.
    """
    return render_template('graph_minus_node.html')

@app.route('/graph_minus_two_nodes/')
def new_reservation():
    """
    Renders graph_minus_two_nodes.html.
    """
    return render_template('graph_minus_two_nodes.html')


if __name__ == '__main__':
    app.run(debug=True)