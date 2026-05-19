import logging


def get_logger(name):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    logging.getLogger("google.auth._default").setLevel(logging.ERROR)

    return logging.getLogger(name)
