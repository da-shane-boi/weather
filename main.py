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
        help="Input the amount of days that you would like to forecast, max of 3",
    )
    parser.add_argument(
        "location",
        nargs="?",
        # const="Cape Town",
        default="Cape Town",
        metavar='"location"',
        type=str,
        help="Put in a location you would like to get the weather for.",
    )
    return parser


if __name__ == "__main__":

    parser = create_parser()
    args = parser.parse_args()
    api = Api()

    if args.forecast:
        params = {"key": api.KEY, "q": args.location, "days": args.forecast}
        api.get("forecast", params)
        api.print_response_forecast()
    else:
        params = {"key": api.KEY, "q": args.location}
        api.get("current", params)
        api.print_response_current()

    # api.get("current")
    # api.print_response()
