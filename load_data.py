import pandas as pd
import datetime
import os


def read_file(filepath):
    '''
    This function read uploaded csv file, save analysis in html and return path to result file.
    '''

    # Open file.
    df = pd.read_csv(filepath)

    # Number of rows and columns.
    n_rows = len(df)
    n_col = len(df.columns)

    # Create empty df (main).
    result = pd.DataFrame([])

    # Describe each column and append to main df.
    for col in list(df.columns):
        result = pd.concat([result, df[f"{col}"].describe(percentiles=[0.1, 0.9])], axis=1)

    # Add column with info about missing values and data type.
    result.loc['missing_values'] = [df[f'{col}'].isnull().sum() for col in list(df.columns)]
    result.loc['%_of_missing_values'] = result.loc['missing_values'] / len(df) * 100
    result.loc['data_type'] = [df[f'{col}'].dtype for col in list(df.columns)]

    # Replace nan.
    result = result.fillna('-')

    # Make results directory if not exist.
    if not os.path.isdir('./templates/results'):
        os.mkdir('./templates/results')

    # Variables to name the result.
    oryg_file_name = filepath[5:-4] # data/google.csv -> google
    creation_time = str(datetime.datetime.now())[0:19].replace(' ', '_') # 2022-04-15_13:15:48
    fn = f'{oryg_file_name}_{n_rows}x{n_col}_{datetime.date.today()}' # google_30x6_2022-04-15

    result_filepath = f"./templates/results/{fn}.html"

    # Set a display option.
    caption = {
        'selector': 'caption',
        'props': 'caption-side: top; text-align: center; background-color: yellow; font-size:1.25em; width: 500px'
    }

    headers = {
        'selector': 'th:not(.index_name)',
        'props': 'background-color: green; color: black; border: 2px solid black'
    }

    cell_hover = {
        'selector': 'td:hover',
        'props': [('background-color', 'yellow')]
    }

    throw = {
            "selector":"th.row_heading",
            "props": [("background-color", "orange"), ("color", "green")]
    }

    table_title = f'''File: "{oryg_file_name}"; number of rows: {n_rows};
                    number of columns: {n_col}; time of execution of the analysis: {creation_time}'''

    result = result.style.set_caption(table_title) \
        .set_table_styles([caption, cell_hover, headers, throw], overwrite=False).set_properties(**{'background-color': 'cyan',
                               'color': 'red',
                               'border': '2px solid black'}).set_precision(2)

    result.to_html(result_filepath)

    return result_filepath



