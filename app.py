import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__)

server = app.server

app.layout = html.Div([
    html.H1("Hello World!")
])

if __name__=="__main__":
    app.run_server('localhost', debug=True)

