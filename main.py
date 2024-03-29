#! /usr/bin/python3

def create_parser(sys_args):
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

    parser.add_argument(
        "-H",
        "--hour",
        metavar="military hour",
        type=int,
        help="Get the weather for an exact hour, eg; 16 -> 4pm"
    )

    parser.add_argument(
        #TODO
        '-b',
        '--breakdown',
        action="store_true",
        help="Get an hourly breakdown of the day."
    )

    parser.add_argument(
        "-I",
        "--install",
        action="store_true",
        help="Install script as a binary to path"
    )

    parser.add_argument(
        "-U",
        "--uninstall",
        action="store_true",
        help="Uninstall script and remove data."
    )

    return parser.parse_args(sys_args)


if __name__ == "__main__":
    import argparse
    from api import Api
    import sys
    from handler import handle_commands, generate_command_paramaters

    args = create_parser(sys.argv[1:])
    api = Api()
    try:
        param_args = generate_command_paramaters(args)
    except UserWarning:
        print("[Error] Cannot call --hour and --breakdown at the same time.")
        sys.exit()
    except SyntaxError:
        print("[Error] Hour must be called using military time, eg; 0 -> 12 am, 12 -> 12pm, 23 -> 11pm")
        sys.exit()
    handle_commands(api, param_args)

