"""Simple arguments parser"""

import argparse
from dataclasses import dataclass

from src.version import VERSION


@dataclass
class ArgumentData:
    """Holding the parsed arguments or its default values"""
    # TODO: your args
    # debug logging
    debug: bool


def init_args_parser() -> argparse.ArgumentParser:
    """Initializes the argument parser

    Returns:
        argparse.ArgumentParser: Initialized argument parser
    """
    parser = argparse.ArgumentParser(
        prog=f"YOUR PROJECT v{VERSION}",
        description="""
        Your project description.
        """
    )
    # debug logging
    parser.add_argument('--debug', required=False,
                        action='store_true',  # on-off switch
                        help=argparse.SUPPRESS)
    return parser


def try_get_args(parser: argparse.ArgumentParser) -> ArgumentData | None:
    """Tries to parse the defined arguments.
    May print errors and return None.

    Args:
        parser (argparse.ArgumentParser): The initialized parser

    Returns:
        ArgumentData | None: Your defined argument data if successful
    """
    args = parser.parse_args()
    # TODO: check values and handle errors

    return ArgumentData(bool(args.debug))
