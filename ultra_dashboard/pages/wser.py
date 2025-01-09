import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

from figures import finishers_per_year_line_chart

dash.register_page(__name__, path="/WSER", name="UltraDashboard: WSER")

layout = dbc.Container(
    [
        html.H2("Western States Endurance Run"),
            dbc.Row(
                dcc.Graph(
                    id="finishers-per-year",
                    figure=finishers_per_year_line_chart("WSER")
                ),
            )
    ],
    fluid=True
)
