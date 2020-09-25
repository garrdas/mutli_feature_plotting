import pandas as pd
import seaborn as sns


def generate_plots(df):
    features = list(df.columns.values)
    features.remove('date_time')
    # x_axis = df['date_time']
    # y_axis = features
    sns.set(rc={'figure.figsize': (12, 10)})
    g = sns.catplot(x='date_time', y=features, data=df, ci=False, kind='point')
    g.savefig('plot.png')
    return ax


def generate_plots_2(df):
    features = list(df.columns.values)
    features.remove('date_time')
    x_axis = df['date_time']
    y_axis = features
    sns.set(rc={'figure.figsize': (12, 10)})
    ax = sns.lineplot(x=x_axis, y='cp_idcnorm', data=df, ci=False)
    return ax


def retrieve_data(loc3, cols3):
    # custom_date_parser = lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S %z')

    # tzinfos = {"EST": -14400}  # 4 hours behind UTC in seconds (1 hour behind would be -3600)
    # custom_date_parser = lambda x: parser.parse(x, tzinfos=tzinfos)

    custom_date_parser = lambda x: parser.parse(x, ignoretz=True)
    df = pd.read_csv(loc3, usecols=cols3, parse_dates=[0], date_parser=custom_date_parser)
    return df
