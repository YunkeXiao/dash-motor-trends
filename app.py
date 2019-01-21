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

print(cars)

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
])


# State Management
# -------------------------------------------------------------------------------------------------`-------

if __name__ == '__main__':
    app.run_server(debug=True)
