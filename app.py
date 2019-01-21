import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

# from auth import auth

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Optionally display a log in screen.                                                                   #
# If `REQUIRE_LOGIN = True` in `config.py`, then auth_instance allows you to programatically access the #
# username of the currently logged in user.                                                             #
# If `REQUIRE_LOGIN = False`, then no login screen will be displayed and `auth_instance` will be `None` #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# auth_instance = auth(app)

server = app.server  # Expose the server variable for deployments

# Standard Dash app code below
df = pd.read_csv('./mtcars.csv')
cars = [df['model'][x] for x in range(len(df))]

app.layout = html.Div(children=[
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'Miles/Gallon', 'value': 'mpg'},
            {'label': ' Number of cylinders', 'value': 'cyl'},
            {'label': 'Displacement', 'value': 'disp'},
            {'label': ' Gross horsepower', 'value': 'hp'},
            {'label': ' Rear axle ratio', 'value': 'drat'}
        ],
        value='mpg'),
    html.Div(
        id='graphs',
        className='row',
        children=[
            html.Div(
                id='test_1_data',
                children=[0, 5, 10, 11, 4, 2, 0, 1, 0, 1],
                style={'display': 'none'}
            ),
            html.Div(
                className='five columns',
                children=[
                    dcc.Graph(
                        id='bar_graph',
                        figure={
                            'data': [
                                {
                                    'x': [i for i in range(1, 11)],
                                    'y': [],
                                    'type': 'bar',
                                    'marker': {
                                        'color': ['rgba(30,144,255,0.8)', 'rgba(255,140,0,0.8)'] +
                                                 ['rgba(30,144,255,0.8)' for i in range(8)]
                                    },
                                },
                            ],
                            'layout': {
                                'title': 'Number Of Clicks Used In Test 1',
                                'xaxis': {
                                    'dtick': 1
                                },
                                'yaxis': {
                                    'dtick': 1
                                },
                                'autosize': True,
                            }
                        },
                        config={
                            'displayModeBar': False
                        }
                    )]),
            html.Div(
                className='five columns',
                children=[
                    dcc.Graph(
                        id='pie_graph',
                        figure={
                            'data': [
                                {
                                    'labels': [str(i) + ' clicks' for i in range(1, 11)],
                                    'values': [],
                                    'type': 'pie',
                                },
                            ],
                            'layout': {
                                'title': 'Distribution Of Performances In Test 1',
                                'autosize': True,
                            }
                        },
                        config={
                            'displayModeBar': False
                        }
                    )
                ]
            )
        ]
    )
])

# State Management
# -------------------------------------------------------------------------------------------------`-------

if __name__ == '__main__':
    app.run_server(debug=True)
