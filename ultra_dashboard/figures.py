import plotly.express as px

from ultra_dashboard.data_fetcher import (
    get_finishers_per_year,
    get_winners_per_year,
)
import ultra_dashboard.utils

def generate_y_axis_time_ticks(df):
    max_time_seconds = df['time_seconds'].max()
    df['time_seconds'] = df['time_seconds'].astype(int)

    if max_time_seconds >= 86400: # 24 hours
        rounder = 86400
        frequency = 3600  # 1-hour intervals
    elif max_time_seconds >= 3600:
        rounder = 3600
        frequency = 1800  # 30-minute intervals
    elif max_time_seconds >= 1800:
        rounder = 1800
        frequency = 900 # 15-minute intervals
    else:
        rounder = 300
        frequency = 300 # 5-minute intervals

    tickvals = list(range(
        (df['time_seconds'].min() // rounder) * rounder,
        ((df['time_seconds'].max() // rounder)+1) * rounder + frequency,
        frequency
    ))

    ticktext = [
        ultra_dashboard.utils.format_seconds_to_hms(seconds)
        for seconds in tickvals
    ]

    return tickvals, ticktext

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
    tickvals, ticktext  = generate_y_axis_time_ticks(df)

    fig = px.line(
        df,
        x="year",
        y="time_seconds",
        title=f"{race} 1st Place Finisher Times",
        labels={"year": "Year"},
        hover_data={"Time": df["time"], 'time_seconds': False}
    )

    fig.update_yaxes(
        tickvals=tickvals,
        ticktext=ticktext
    )

    return fig
