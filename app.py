from flask import Flask, render_template, request
import os
import datetime
from load_data import read_file


app = Flask(__name__)


@app.route('/test', methods=['GET'])
def test():
    return f'test OK - {str(datetime.datetime.now())[:-7]}'


@app.route('/postcsv', methods = ['GET', 'POST'])
def index():
    '''
    This function shows the home page where you can upload a new csv file for analysis.
    It also shows a list of analysis if exists.
    '''
    # Check and download a file.
    if request.method == 'POST':
        file = request.files['csvfile']
        if file.filename.endswith('.csv'):
            if not os.path.isdir('data'):
                os.mkdir('data')
            filepath = os.path.join('data', file.filename)
            file.save(filepath)
            # Calls functions for analysis after successful file download.
            if os.path.isfile(filepath):
                result_html_path = read_file(filepath)
                if 'example_file.csv' not in filepath:
                    os.remove(filepath)
                # Display result
                return render_template(result_html_path[11:])
        else:
            return 'Only the csv file can be uploaded'

    # Creating list of results to display.
    results = []
    directory = 'templates/results'
    if os.path.isdir('templates/results'):
        for filename in os.listdir(directory):
            results.append(filename[:-5])
    # Display the home page with existing analyzes
    return render_template('index.html', content=results)


@app.route(f'/results/<filename>', methods = ['GET'])
def show_result(filename):
    '''
    This function shows the file analysis.
    '''
    return render_template(f'./results/{filename}.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)