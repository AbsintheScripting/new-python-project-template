"""YOUR PROJECT"""

from logging import Logger

from src.args_parser import init_args_parser, try_get_args, ArgumentData
from src.logger import logger_instance


class App():
    """defining your project"""

    _logger: Logger | None

    def __init__(self, args: ArgumentData) -> None:
        if args.debug:
            self._logger = logger_instance(__name__, "debug.log")

    def run(self) -> None:
        """Start the script"""
        print("script starting...")
        if self._logger:
            self._logger.debug("run script completed")


if __name__ == "__main__":
    parser = init_args_parser()
    parsed_args = try_get_args(parser)
    if parsed_args is not None:
        app = App(parsed_args)
        app.run()
