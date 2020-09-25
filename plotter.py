import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os


def id_files(path, suffix):
    filenames = os.listdir(path)
    return [path+os.sep+filename for filename in filenames if filename.endswith(suffix)]


def format_input_features(cols1):
    new_cols = list(map(str.lower, cols1))
    print(new_cols)
    return new_cols


def format_data_headers(loc1):
    df = pd.read_csv(loc1, delimiter='\s+')
    df.columns = map(str.lower, df.columns)
    new_filename = loc1.replace('.txt', '') + '.csv'
    df.to_csv(new_filename, index=False)
    return new_filename


def prove_usecols(loc2, cols2):
    df = pd.read_csv(loc2)
    df_headers = list(df.columns.values)
    return all(col in df_headers for col in cols2)


def retrieve_data(loc3, cols3):
    df = pd.read_csv(loc3, parse_dates=[[0, 1]], usecols=cols3)
    return df


def generate_plots(df):
    # credit to Randal Olson for this multi-line plot method:
    # http://www.randalolson.com/2014/06/28/how-to-make-beautiful-data-visualizations-in-python-with-matplotlib/
    features = list(df.columns.values)
    features.remove('date_time')

    # These are the "Tableau 20" colors as RGB.
    tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
                 (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
                 (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
                 (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
                 (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]

    # Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.
    for i in range(len(tableau20)):
        r, g, b = tableau20[i]
        tableau20[i] = (r / 255., g / 255., b / 255.)

    plt.figure(figsize=(18, 12))

    ax = plt.subplot(111)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

    for num, feature in enumerate(features):
        plt.plot(df['date_time'].values,
                 df[feature].values,
                 label=feature,
                 lw=2.5,
                 color=tableau20[num])

    plt.legend(loc='best')

    current_date = str(datetime.now().date().strftime("%d-%m-%Y"))
    current_time = str(datetime.now().time().strftime("%H.%M.%S"))
    plt.savefig('plot-name-' + current_date + '-' + current_time + '.png', bbox_inches="tight")
    return


def multi_feature_plot(data_location, feature_list, suffix='.txt'):
    filenames = id_files(data_location, suffix)
    features = format_input_features(feature_list)
    for filename in filenames:
        file = format_data_headers(filename)
        if not prove_usecols(file, features):
            raise ValueError('All column names passed are not found in data headers')
        else:
            data = retrieve_data(file, features)
            generate_plots(data)


if __name__ == '__main__':
    col_headers = ['date', 'time']
    location = str(os.getcwd())
    multi_feature_plot(location, col_headers)
