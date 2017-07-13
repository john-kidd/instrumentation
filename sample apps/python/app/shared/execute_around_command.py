import time
import uuid


def log_time(log_info):
    def partial(action, get_description):
        start = time.time()
        action()
        stop = time.time()
        duration = stop - start
        log_info("DURATION {} took {} milliseconds".format(get_description(), duration))

    return partial


def log_wrap(log_info):
    def partial(action, get_description):
        log_info("BEGIN {}".format(get_description()))
        action_time = log_time(log_info)
        action_time(action, get_description)
        log_info("END {}\n".format(get_description()))

    return partial


def handle_error(log_error, log_info):
    def partial(action, get_description):
        try:
            action_around = log_wrap(log_info)
            action_around(action, get_description)
        except ValueError as ex:
            correlation_id = str(uuid.uuid4())
            log_info("Correlation Id {}".format(correlation_id))
            log_info("FAILED {}\n".format(get_description()))
            log_error(ex)
            raise ValueError(
                "An error has occurred. Please contact support with correlation Id {}".format(correlation_id))

    return partial
