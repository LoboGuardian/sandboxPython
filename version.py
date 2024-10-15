import datetime

def get_iso_week_number(date):
    """Calculate the ISO week number."""
    return date.isocalendar()[1]

def get_quarter(date):
    """Determine the quarter of the year based on the month."""
    month = date.month
    if month < 4:
        return 'Q1'
    elif month < 7:
        return 'Q2'
    elif month < 10:
        return 'Q3'
    else:
        return 'Q4'

def calculate_patch_version(date):
    """Calculate the patch version based on the day of the week."""
    day_of_week = date.weekday()  # Monday is 0, Sunday is 6
    return (day_of_week + 1) * 3  # Adjust for patch version (Mon=3, ..., Sun=21)

def generate_current_week_version():
    """Generate the version string for the current week."""
    today = datetime.datetime.now()
    year = today.year
    week_number = get_iso_week_number(today)
    quarter = get_quarter(today)
    patch_version = calculate_patch_version(today)
    
    return f"K{year}.{quarter}.{week_number}.{patch_version}"

if __name__ == "__main__":
    version = generate_current_week_version()
    print(version)
