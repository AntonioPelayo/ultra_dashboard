import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

from ultra_dashboard.figures import (
    finishers_per_year_line_chart,
    winning_time_per_year_line_chart
)

dash.register_page(__name__, path="/WSER", name="UltraDashboard: WSER")
race = "WSER"

layout = dbc.Container(
    [
        html.H2("Western States Endurance Run"),
            dbc.Row(
                dcc.Graph(
                    id="finishers-per-year",
                    figure=finishers_per_year_line_chart(race)
                ),
            ),
            dbc.Row(
                dcc.Graph(
                    id="winning-time-per-year",
                    figure=winning_time_per_year_line_chart(race)
                ),
            )
    ],
    fluid=True
)
