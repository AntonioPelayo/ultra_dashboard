from dash import html, register_page

register_page(__name__, path="/")

layout = html.Div([
    html.P([
        "Developer: Antonio Pelayo",
        html.Br(),
        "Contact: aPelayo.py@gmail.com"
    ]),
    html.P([
        "Github sources: ",
        html.Br(),
        "- Web scraping library: ",
        html.A(
            "ultrasignup_tools",
            href="https://github.com/AntonioPelayo/ultrasignup_tools"
        ),
        html.Br(),
        "- Dashboard source: ",
        html.A(
            "ultra_dashboard",
            href="https://github.com/AntonioPelayo/ultra_dashboard"
        ),
    ]),
])
