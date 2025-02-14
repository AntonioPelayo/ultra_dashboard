def format_seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds // 60) % 60
    secs = seconds % 60
    return f"{hours}:{minutes:02}:{secs:02}"
