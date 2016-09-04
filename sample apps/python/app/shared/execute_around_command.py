import time
import uuid


def timer(log_info):
    def partial(action, get_description):
        start = time.time()
        action()
        stop = time.time()
        duration = stop - start
        log_info("DURATION {} took {} milliseconds".format(get_description(), duration))

    return partial


def around(log_info):
    def partial(action, get_description):
        log_info("\nBEGIN {}".format(get_description()))
        action_time = timer(log_info)
        action_time(action, get_description)
        log_info("END {}\n".format(get_description()))

    return partial


def compensate(log_error, log_info):
    def partial(action, get_description):
        try:
            action_around = around(log_info)
            action_around(action, get_description)
        except ValueError as ex:
            correlation_id = str(uuid.uuid4())
            log_info("Correlation Id {}".format(correlation_id))
            log_info("FAILED {}\n".format(get_description()))
            log_error(ex.message)
            raise ValueError("An error has occurred. Please contact support with correlation Id {}".format(correlation_id))

    return partial
