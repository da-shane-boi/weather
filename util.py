from datetime import datetime
import calendar

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
    if 0 < index < 3:
        return "Low"
    elif 2 < index < 6:
        return "Moderate"
    elif 5 < index < 8:
        return "High"
    elif 7 < index < 11:
        return "Very High"
    elif index > 10: 
        return "Extreme"

if __name__ == "__main__":
    print(get_month("2024-11-15"))