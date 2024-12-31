import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)
app.title = "UltraDashboard Race Statistics"
server = app.server

app.layout = html.Div([
    html.H1("UltraDashboard Race Statistics", style={"text-align": "center"}),
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="/"))
        ]),
    dash.page_container
])

if __name__ == '__main__':
    app.run_server()
