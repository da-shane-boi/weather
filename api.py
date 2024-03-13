from pathlib import Path
import requests
import os
import json

class Api:
    def __init__(self) -> None:
        self.base_url = "https://api.weatherapi.com/v1"
        self.path = Path.home() / ".weather"
        self.KEY = self.configure()

        self.current_response = None

    def configure(self) -> str:
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

    # def create_config(self):
    #     config_path = self.path/"config.json"
    #     if not config_path.exists:
    #         Path.touch(self.path/"config.json")
    #         # default location,

    def get(self, type: str, paramaters:dict):
        # paramaters = {"key": self.KEY, "q": location}
        self.response = requests.get(f"{self.base_url}/{type}.json", params=paramaters).json()

    def print_response_current(self):
        print("_________________________________________________________________")
        print()
        print(f"Location:          {self.response['location']['name']}")
        print(f"Condition:         {self.response['current']['condition']['text']}")
        print(f"Temperature:       {self.response['current']['temp_c']}°C")
        print(f"    Feels like:    {self.response['current']['feelslike_c']}°C")
        print(f"Humidity:          {self.response['current']['humidity']}%")
        if self.response['current']['precip_mm'] > 0.1:
            print(f"Rain:              {self.response['current']['precip_mm']}mm")
        print(f"Wind:              {self.response['current']['wind_kph']}Km {self.response['current']['wind_dir']}")
        # print(f"Wind Direction: {self.response['current']['wind_dir']}")
        print("_________________________________________________________________")

    def print_response_forecast(self):
        fore_day = self.response['forecast']['forecastday'][-1]
        # print(fore_day)
        print("_________________________________________________________________")
        print()
        print(f"Location:          {self.response['location']['name']}")
        print(f"Date:              {'-'.join(fore_day['date'].split('-')[::-1])}")
        print(f"Condition:         {fore_day['day']['condition']['text']}")
        print(f"Temperature:       {fore_day['day']['mintemp_c']}°C/{fore_day['day']['maxtemp_c']}°C")
        print(f"Humidity:          {fore_day['day']['avghumidity']}%")
        print(f"Chance of rain:    {fore_day['day']['daily_chance_of_rain']}%")
        print(f"Wind:              {fore_day['day']['maxwind_kph']}Km")
        print(f"UV Index:          {fore_day['day']['uv']}")
        # # print(f"Wind Direction: {self.response['current']['wind_dir']}")
        print("_________________________________________________________________")


