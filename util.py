from datetime import datetime
import calendar
from colour import Colour as col

def get_day(given_date: str) -> str:
    """Get the day of the week from a given date

    Args:
        given_date (str): date -> format: yyyy-mm-dd

    Returns:
        str: Day of the week
    """    
    given_datetime = datetime.strptime(given_date, "%Y-%m-%d")
    days = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday",
    }
    return days[given_datetime.weekday()]

def get_month(given_date:str) -> str:
    given_datetime = datetime.strptime(given_date, "%Y-%m-%d")
    months = {
        1: "January",
        2:"February",
        3:"March",
        4:"April",
        5:"May",
        6:"June",
        7:"July",
        8:"August",
        9:"September",
        10:"October",
        11:"November",
        12:"December"
    }     
    return months[given_datetime.month]

def get_uv_index_rate(index:float):
    colour = col()
    if 0 < index < 3:
        return colour.string("Low", "blue")
    elif 2 < index < 6:
        return colour.string("Moderate", 'green')
    elif 5 < index < 8:
        return colour.string("High", 'yellow')
    elif 7 < index < 11:
        return colour.string("Very High", 'red')
    elif index > 10: 
        return colour.string("Extreme", 'red', bold=True)

def get_heading(location:str, date:str, time="", center=True, heading_colour='cyan'):
    colour = col()
    year, month, day = date.split('-')
    heading = ""

    heading += f"{location}, "
    heading += f"{get_day(date)}, "
    if time:
        heading += f"{time}, "
    heading += f"{day} "
    heading += f"{get_month(date)} "
    heading += f"{year}"
    if center:
        heading = heading.center(70, ' ' )
    heading = colour.string(heading, heading_colour, bold=True)
    return heading

def get_break():
    breakline = "-" * 70
    colour = col()
    return colour.string(breakline, 'green', bold=True)

def colour_temp(temp):
    colour = col()
    if 16 > temp:
        return colour.string(str(temp), 'blue')
    elif 15 < temp < 20:
        return colour.string(str(temp), 'green')
    elif 19 < temp < 27 :
        return colour.string(str(temp), 'yellow')
    elif 26 < temp:
        return colour.string(str(temp), 'red')

if __name__ == "__main__":
    print(get_month("2024-11-15"))