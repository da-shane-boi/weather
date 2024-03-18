from api import Api


def generate_command_paramaters(args):
    if args.breakdown and args.hour:
        raise UserWarning()
    params = {}
    params["location"] = args.location
    params["forecast"] = True if args.forecast else False
    if params["forecast"]:
        params["forecast_days"] = args.forecast
    params["tmr"] = True if args.tomorrow else False
    params["json"] = True if args.get_json else False
    params["all"] = True if args.all else False
    params["hour"] = True if type(args.hour) == int else False
    if params["hour"]:
        validate_hour(args.hour)
        params["hour_value"] = args.hour
    params["breakdown"] = True if args.breakdown else False

    return params


def handle_commands(api: Api, c_params: dict):
    if c_params["forecast"]:
        params = {
            "key": api.KEY,
            "q": c_params["location"],
            "days": c_params["forecast_days"],
        }
        api.get("forecast", params)
        if c_params["hour"]:
            api.print_hour(c_params)
        else:
            api.print_response_forecast(c_params)
    elif c_params["tmr"]:
        params = {"key": api.KEY, "q": c_params["location"], "days": 2}
        api.get("forecast", params)
        
        if c_params["hour"]:
            api.print_hour(c_params)
        else:
            api.print_response_forecast(c_params)
    else:
        params = {"key": api.KEY, "q": c_params["location"]}
        if c_params["all"] or c_params["hour"]:
            # Get all data for current day
            params["days"] = 1
            api.get("forecast", params)
            if c_params["hour"]:
                api.print_hour(c_params)
            else:
                api.print_response_forecast(c_params)
        else:
            api.get("current", params)
            api.print_response_current(c_params)

def validate_hour(hour_value:str):
    if hour_value < 0 or hour_value > 23:
        raise SyntaxError