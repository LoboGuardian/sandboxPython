# -*- CODING: UTF-8 -*-

# Without the line above, you cannot use emojis
import pytz
import datetime

# This is the local time to assume:
local_tz = pytz.timezone('America/Caracas')

# YYYY-MM-DD
# Enter the actual date or it won't understand timezone changes (like when Mexico and Colombia change 1 hour)
date_to_convert = "2024-10-23 12:15:00"

# Convert the string to a datetime object
date_to_convert = datetime.datetime.strptime(date_to_convert, "%Y-%m-%d %H:%M:%S")

# Localize the datetime object to the specified timezone
localized_date = local_tz.localize(date_to_convert)

# print(date_to_convert)

# print("Generating flag block:\n")

# In order of priority
zones = [
    # Los Angeles, USA, UTC -8
    ["🇺🇸", "US/Pacific"],
    # Denver, USA, UTC -7
    ["🇺🇸", "US/Mountain"],
    # Chicago, USA, UTC -6
    ["🇺🇸", "US/Central"],
    # New York, USA, UTC -5
    ["🇺🇸", "US/Eastern"],
    # Miami, USA, UTC -5
    ["🇺🇸", "US/Eastern"],
    # Houston, USA, UTC -6
    ["🇺🇸", "US/Central"],
    # El Salvador, UTC -6
    ["🇸🇻", "America/El_Salvador"],
    # Guatemala, UTC -6
    ["🇬🇹", "America/Guatemala"],
    # Tegucigalpa, Honduras, UTC -6
    ["🇭🇳", "America/Tegucigalpa"],
    # La Paz, Bolivia, UTC -4
    ["🇧🇴", "America/La_Paz"],
    # Bogota, Colombia, UTC -5
    ["🇨🇴", "America/Bogota"],
    # Panama City, Panama, UTC -5
    ["🇵🇦", "America/Panama"],
    # Mexico City, Mexico, UTC -6
    ["🇲🇽", "America/Mexico_City"],
    # Caracas, Venezuela, UTC -4
    ["🇻🇪", "America/Caracas"],
    # Lima, Peru, UTC -5
    ["🇵🇪", "America/Lima"],
    # Guayaquil, Ecuador, UTC -5
    ["🇪🇨", "America/Guayaquil"],
    # Santiago, Chile, UTC -3
    ["🇨🇱", "America/Santiago"],
    # Buenos Aires, Argentina, UTC -3
    ["🇦🇷", "America/Argentina/Buenos_Aires"],
    # Montevideo, Uruguay, UTC -3
    ["🇺🇾", "America/Montevideo"],
    # São Paulo, Brazil, UTC -3
    ["🇧🇷", "America/Sao_Paulo"],
    # Santo Domingo, Dominican Republic, UTC -4
    ["🇩🇴", "America/Santo_Domingo"],
    # Managua, Nicaragua, UTC -6
    ["🇳🇮", "America/Managua"],
    # Havana, Cuba, UTC -5
    ["🇨🇺", "America/Havana"],
    # New York, UTC -5
    ["🇺🇸", "US/Eastern"],
    # Madrid, Spain, UTC +1
    ["🇪🇸", "Europe/Madrid"],
    # London, UK, UTC +0
    ["🇬🇧", "Europe/London"],
    # Berlin, Germany, UTC +1
    ["🇩🇪", "Europe/Berlin"],
    # Paris, France, UTC +1
    ["🇫🇷", "Europe/Paris"],
    # Rome, Italy, UTC +1
    ["🇮🇹", "Europe/Rome"],
    # Cairo, Egypt, UTC +2
    ["🇪🇬", "Africa/Cairo"],
    # Moscow, Russia, UTC +3
    ["🇷🇺", "Europe/Moscow"],
    # Istanbul, Turkey, UTC +3
    ["🇹🇷", "Europe/Istanbul"],
    # New Delhi, India, UTC +5:30
    ["🇮🇳", "Asia/Kolkata"],
    # Kuala Lumpur, Malaysia, UTC +8
    ["🇲🇾", "Asia/Kuala_Lumpur"],
    # Beijing, China, UTC +8
    ["🇨🇳", "Asia/Shanghai"],
    # Seoul, South Korea, UTC +9
    ["🇰🇷", "Asia/Seoul"],
    # Tokyo, Japan, UTC +9
    ["🇯🇵", "Asia/Tokyo"],
    # Sydney, Australia, UTC +11
    ["🇦🇺", "Australia/Sydney"],
]

# Initialize the dictionary
times = {}
# times = {"00pm": "X"}


#  Time zones are not derived from countries, but from cities
# Although the priority is by country

for country in zones:
    dtc = localized_date.astimezone(pytz.timezone(country[1]))

    # Format the time based on the timezone
    if country[1] == "Europe/Madrid":
        # Print the time in 24-hour format and an "H" at the end
        formatted_time = dtc.strftime("%-H:%MH")  # Using 24-hour format
    else:
        # Format the time correctly considering if DST is in effect
        if dtc.utcoffset().total_seconds() == dtc.dst().total_seconds():
            # If we're in DST, we may need to subtract that from the standard offset
            formatted_time = dtc.strftime("%-I:%M %p (DST)").replace(" PM", "PM").replace(" AM", "AM")
        else:
            # Print the time in 12-hour format AM/PM
            # formatted_time = dtc.strftime("%-I%p")
            formatted_time = dtc.strftime("%I:%M %p").replace(" PM", "PM").replace(" AM", "AM")

    if formatted_time in times:
        times[formatted_time] += country[0]
    else:
        times[formatted_time] = country[0]

    # If the country is USA in Pacific, add "PT" in front of US flags
    if country[1] == "US/Pacific":
        times[formatted_time] += " PT"  # Pacific Time
    elif country[1] == "US/Mountain":
        times[formatted_time] += " MT"  # Mountain Time
    elif country[1] == "US/Central":
        times[formatted_time] += " CT"  # Central Time
    elif country[1] == "US/Eastern":
        times[formatted_time] += " ET"  # Eastern Time

    times[formatted_time] += " "

for time, flag in times.items():
    if flag.strip() != "":
        # For Spain, print in specified format
        if "🇪🇸" in flag:
            print(f"{time} {flag.strip()}")
        else:
            # Format '5PM' as '05:00'
            if "PM" in time:
                hour, minute = time.split(":")
                formatted_output = f"{int(hour):02d}:{minute}"
                print(f"{formatted_output} {flag.strip()}")
            else:
                print(f"{time} {flag.strip()}")