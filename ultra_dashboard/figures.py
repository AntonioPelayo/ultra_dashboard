import plotly.express as px

from ultra_dashboard.data_fetcher import (
    get_finishers_per_year,
    get_winners_per_year,
)

def finishers_per_year_line_chart(race):
    df = get_finishers_per_year(race)
    return px.line(
        df,
        x="year",
        y="finishers",
        title=f"{race} Finishers per Year",
        labels={"year": "Year", "finishers": "Number of Finishers"},
    )

def winning_time_per_year_line_chart(race):
    df = get_winners_per_year(race)
    return px.line(
        df,
        x="year",
        y="time",
        title=f"{race} 1st Place Finisher Times"
    )
