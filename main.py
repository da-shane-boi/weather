import argparse
from api import Api


def create_parser():
    parser = argparse.ArgumentParser(
        prog="Weather App", description="A CLI weather application"
    )

    parser.add_argument(
        "-f",
        "--forecast",
        metavar="days",
        type=int,
        choices=range(1, 5),
        help="Input the amount of days that you would like to forecast, max of 4",
    )
    parser.add_argument(
        "location",
        nargs="?",
        default="Cape Town",
        metavar='"location"',
        type=str,
        help="Put in a location you would like to get the weather for.",
    )

    parser.add_argument(
        "-t", "--tomorrow", action="store_true", help="Get the weather for tomorrow"
    )

    parser.add_argument(
        "-json",
        "--get_json",
        action="store_true",
        default=False,
        help="Get Api request response json",
    )

    parser.add_argument(
        "-a",
        "--all",
        action="store_true",
        default=False,
        help="See all data for forecast"
    )

    return parser


if __name__ == "__main__":

    parser = create_parser()
    args = parser.parse_args()
    api = Api()
    json = True if args.get_json else False
    all = True if args.all else False
    if args.forecast:
        params = {"key": api.KEY, "q": args.location, "days": args.forecast}
        api.get("forecast", params)
        api.print_response_forecast(json, all)
    elif args.tomorrow:
        params = {"key": api.KEY, "q": args.location, "days": 2}
        api.get("forecast", params)
        api.print_response_forecast(json, all)
    else:
        params = {"key": api.KEY, "q": args.location}
        api.get("current", params)
        api.print_response_current(json)
