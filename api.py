from pathlib import Path
import requests
import os
import util


class Api:
    def __init__(self) -> None:
        self.base_url = "https://api.weatherapi.com/v1"
        self.path = Path.home() / ".config" / "weather"
        self.KEY = self.configure()

        self.response = None

    def configure(self) -> str:
        """Configures the Api, acquiring the key and saving it to a local file.

        Returns:
            str: Api key
        """
        if self.path.exists():
            key_path = self.path / ".key.txt"
            if key_path.exists():
                with open(key_path) as key_file:
                    key = key_file.readline()
            else:
                print("[App] Key not found")
                key = self.get_key()
                self.save_key(key)
        else:
            print("[App] Configuration not found.")
            print("[App] Starting configuration.")
            Path.mkdir(self.path)
            key = self.get_key()
            self.save_key(key)
        return key

    def save_key(self, key):
        """Saves the key in a hidden file in the home directory

        Args:
            key (_type_): _description_
        """
        os.system(f"echo '{key}' > {self.path}/.key.txt")

    def get_key(self) -> str:
        while True:
            key = input("Input your Api Key: ")
            if self.validate_key(key):
                return key

    def validate_key(self, key: str):
        paramaters = {"key": key, "q": "Cape Town"}
        response = requests.get(f"{self.base_url}/current.json", params=paramaters)
        return str(response.status_code)[0] != "4"

    def get(self, type: str, paramaters: dict):
        self.response = requests.get(
            f"{self.base_url}/{type}.json", params=paramaters
        ).json()

    def print_response_current(self, json:bool):
        if json:
            print(self.response)
        else:
            print("_________________________________________________________________")
            print()
            print(f"Location:          {self.response['location']['name']}")
            print(f"Condition:         {self.response['current']['condition']['text']}")
            print(f"Temperature:       {self.response['current']['temp_c']}°C")
            if self.response['current']['temp_c'] != self.response['current']["feelslike_c"]:
                print(f"    Feels like:    {self.response['current']['feelslike_c']}°C")
            print(f"Humidity:          {self.response['current']['humidity']}%")
            if self.response["current"]["precip_mm"] > 0.1:
                print(f"Rain:              {self.response['current']['precip_mm']}mm")
            print(
                f"Wind:              {self.response['current']['wind_kph']}Km {self.response['current']['wind_dir']}"
            )
            print(f"UV Index:          {util.get_uv_index_rate(self.response['current']['uv'])}")
            print("_________________________________________________________________")

    def print_response_forecast(self, json:bool, all:bool):
        fore_day = self.response["forecast"]["forecastday"][-1]
        if json:
            print(self.response)
        else:
            print("_________________________________________________________________")
            print()
            print(f"Location:          {self.response['location']['name']}")
            print(
                f"Date:              {util.get_day(fore_day['date'])}, {fore_day['date'].split('-')[2]} {util.get_month(fore_day['date'])}"
            )
            print(f"Condition:         {fore_day['day']['condition']['text']}")
            print(
                f"Temperature:       {fore_day['day']['mintemp_c']}°C/{fore_day['day']['maxtemp_c']}°C"
            )
            print(f"Humidity:          {fore_day['day']['avghumidity']}%")
            print(f"Chance of rain:    {fore_day['day']['daily_chance_of_rain']}%")
            print(f"Chance of snow:    {fore_day['day']['daily_chance_of_snow']}%")
            print(f"Wind:              {fore_day['day']['maxwind_kph']}Km")
            print(f"UV Index:          {util.get_uv_index_rate(fore_day['day']['uv'])}")
            print("_________________________________________________________________")
            if all:
                print()
                print(f"Sunrise:           {fore_day['astro']['sunrise']}")
                print(f"Sunset:            {fore_day['astro']['sunset']}")
                print(f"Moonrise:          {fore_day['astro']['moonrise']}")
                print(f"Moonset:           {fore_day['astro']['moonset']}")
                print(f"Moon Phase:        {fore_day['astro']['moon_phase']}")
                print(f"Moon Light:        {fore_day['astro']['moon_illumination']}")
                print("_________________________________________________________________")


            
