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

# print(cars)

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
                id='data',
                children=[],
                # style={'display': 'none'}
            ),
            html.Div(
                className='five columns',
                children=[
                    dcc.Graph(
                        id='bar_graph',
                        figure={
                            'data': [
                                {
                                    'x': cars,
                                    'y': [1 for i in range(32)],
                                    'type': 'bar',
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
                                    'labels': cars,
                                    'values': [1 for i in range(32)],
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


# Data
# ---------------------------------------------------------------------------------------------------------
@app.callback(
    Output(component_id='data', component_property='children'),
    [Input(component_id='dropdown', component_property='value')]
)
def update_data(prop):
    return [df[prop][i] for i in range(len(df[prop]))]


# Graph
# ---------------------------------------------------------------------------------------------------------
@app.callback(
    Output(component_id='bar_graph', component_property='figure'),
    [Input(component_id='data', component_property='children')],
    [State(component_id='bar_graph', component_property='figure')]
)
def update_bar(data, figure):
    new_figure = figure
    new_figure['data'][0]['values'] = data
    return new_figure


if __name__ == '__main__':
    app.run_server(debug=True)
