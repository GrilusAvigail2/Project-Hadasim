import argparse
import parser

import module
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from Project.StatisticData import StatisticData

UPLOAD_FOLDER = 'C:\\Users\\USER\\Desktop\\Project Hadasim\\'
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
        filename = uploaded_file.filename
        data = StatisticData()
        stat_data = data.make_statistic_on_file(filename)

    return render_template('index.html', filename=filename, data=stat_data)


@app.route('/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


# @app.route('/show')
# def show():
#     data = StatisticData("dickens.txt")
#     stat_data = data.make_statistic_on_file("dickens.txt")
#     return stat_data


if __name__ == "__main__":
    app.run(debug=True)

