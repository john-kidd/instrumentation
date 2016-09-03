import time


def timer(log_info):
    def partial(action, get_description):
        start = time.time()
        action()
        stop = time.time()
        duration = stop - start
        log_info("DURATION: {} took {} milliseconds".format(get_description(), duration))

    return partial


def around(log_info):
    def partial(action, get_description):
        log_info("BEGIN: {}".format(get_description()))
        action_time = timer(log_info)
        action_time(action, get_description)
        log_info("END: {}".format(get_description()))

    return partial


def compensate(log_error, log_info):
    def partial(action, get_description):
        try:
            action_around = around(log_info)
            action_around(action, get_description)
        except ValueError as ex:
            log_info("FAILED: {}".format(get_description()))
            log_error(ex.message)
            raise ex

    return partial
