import pandas as pd
import plotly.graph_objs as go
import plotly.express as px


def cleandata(dataset):
    """Clean world bank data for a visualizaiton dashboard

    Keeps data range of dates in keep_columns variable and data for the top 10 economies
    Reorients the columns into a year, country and value
    Saves the results to a csv file

    Args:
        dataset (str): name of the csv data file

    Returns:
        None

    """
    df = pd.read_csv(dataset, delimiter=',')

    df['Positiv getestet'] = pd.to_numeric(df['Positiv getestet'], errors='coerce')
    df['Anzahl Testungen'] = pd.to_numeric(df['Anzahl Testungen'], errors='coerce')

    # output clean csv file
    return df


def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

    # first chart plots arable land from 1990 to 2015 in top 10 economies
    # as a line chart

    graph_one = []
    df = cleandata('data/testnumbers_combined.csv')

    y_number_positives = df['Positiv getestet'].iloc[:-1]  # Leave last value out because it is the sum of all
    x_val = list(range(0, y_number_positives.shape[0]))
    y_number_tests = df['Anzahl Testungen'].iloc[:-1]  # Leave last value out because it is the sum of all


    graph_one.append(
        go.Scatter(
            x=x_val,
            y=y_number_tests,
            fill='tozeroy',
            name='Number Tests'
        )
    )
    graph_one.append(
        go.Scatter(
            x=x_val,
            y=y_number_positives,
            mode='lines',
            name='Number Positives'
        )
    )

    layout_one = dict(title='Number of Corona tests vs. positively tested people',
                      xaxis=dict(title='Weeks',
                                 autotick=False, dtick=10),
                      yaxis=dict(title='Number of tests/positives'),
                      )


    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))

    return figures