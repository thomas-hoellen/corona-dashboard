import pandas as pd
import plotly.graph_objs as go


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
    df = pd.read_csv("data/corona_numbers_world.csv", delimiter=',')

    x_germany = df[df.country == "Germany"].year_week
    y_germany_positives = df[df.country == "Germany"].new_cases
    y_germany_tests = df[df.country == "Germany"].tests_done

    graph_one.append(
        go.Scatter(
            x=x_germany,
            y=y_germany_tests,
            fill='tozeroy',
            name='Number Tests'
        )
    )
    graph_one.append(
        go.Scatter(
            x=x_germany,
            y=y_germany_positives,
            mode='lines',
            name='Number Positives'
        )
    )

    layout_one = dict(title='<b>Germany:</b> Number of Tests vs. Positives',
                      xaxis=dict(title='Weeks',
                                 autotick=False, dtick=15),
                      yaxis=dict(title='Number of tests/positives'),
                      )

    # Plot different countries
    graph_two = []

    x_sweden = df[df.country == "Sweden"].year_week
    y_sweden_positives = df[df.country == "Sweden"].new_cases
    y_sweden_tests = df[df.country == "Sweden"].tests_done

    graph_two.append(
        go.Scatter(
            x=x_sweden,
            y=y_sweden_tests,
            fill='tozeroy',
            name='Number Tests'
        )
    )
    graph_two.append(
        go.Scatter(
            x=x_sweden,
            y=y_sweden_positives,
            mode='lines',
            name='Number Positives'
        )
    )

    layout_two = dict(title='<b>Sweden:</b> Number of Tests vs. Positives',
                      xaxis=dict(title='Weeks',
                                 autotick=False, dtick=15),
                      yaxis=dict(title='Number of positive tests'),
                      )

    # Comparing Germany and Sweden - Number of positives
    graph_three = []
    normalizer = (df[df.region_name == "Germany"].population.iloc[0]/df[df.region_name == "Sweden"].population.iloc[0])
    x_sweden = df[df.country == "Sweden"].year_week
    y_sweden_positives_equaled = (df[df.country == "Sweden"].new_cases * normalizer).astype(int)

    graph_three.append(
        go.Scatter(
            x=x_sweden,
            y=y_sweden_positives_equaled,
            mode='lines',
            name='Sweden'
        )
    )
    graph_three.append(
        go.Scatter(
            x=x_sweden,
            y=y_germany_positives,
            mode='lines',
            name='Germany'
        )
    )

    layout_three = dict(title='<b> Germany vs. Sweden:</b> Normed comparison of Positives',
                      xaxis=dict(title='Weeks',
                                 autotick=False, dtick=15),
                      yaxis=dict(title='Number of positive tests'),
                      )

    # Comparing Germany and Sweden - Number of deaths
    graph_four = []
    df_2 = pd.read_csv("data/death_numbers.csv", delimiter=',')

    df_deaths_germany = df_2[df_2.country == "Germany"]
    df_deaths_sweden = df_2[df_2.country == "Sweden"]

    y_germany_deaths = df_deaths_germany[df_deaths_germany.indicator == "deaths"].weekly_count
    x_germany_deaths = df_deaths_germany[df_deaths_germany.indicator == "deaths"].year_week

    y_sweden_deaths = (df_deaths_sweden[df_deaths_sweden.indicator == "deaths"].weekly_count * normalizer).astype(int)
    x_sweden_deaths = df_deaths_sweden[df_deaths_sweden.indicator == "deaths"].year_week

    graph_four.append(
        go.Scatter(
            x=x_sweden,
            y=y_sweden_deaths,
            mode='lines',
            name='Sweden'
        )
    )
    graph_four.append(
        go.Scatter(
            x=x_sweden,
            y=y_germany_deaths,
            mode='lines',
            name='Germany'
        )
    )

    layout_four = dict(title='<b>Germany vs. Sweden:</b> Normed comparison of Covid-19 related Deaths',
                        xaxis=dict(title='Weeks',
                                   autotick=False, dtick=15),
                        yaxis=dict(title='Number of Deaths'),
                        )

    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures
