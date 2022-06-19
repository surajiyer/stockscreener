from dotenv import load_dotenv
import logging
import signal
import sys
from src.control.screener import Screener


SIGNUM_MAP = {signal.SIGTERM: "SIGTERM", signal.SIGINT: "SIGINT"}


def service_shutdown(signum, frame):
    logging.info(f"Caught signal {SIGNUM_MAP[signum]}, shutting down")
    sys.exit(1)


logger = logging.getLogger(__name__)


def main():
    signal.signal(signal.SIGTERM, service_shutdown)
    signal.signal(signal.SIGINT, service_shutdown)

    load_dotenv()
    from IPython import embed

    embed()
    logger.info("Done")


if __name__ == "__main__":
    main()
