import time
import uuid


def log_time(log_info):
    def partial(query, get_description):
        start = time.time()
        result = query()
        stop = time.time()
        duration = stop - start
        log_info("DURATION {} took {} milliseconds".format(get_description(), duration))
        return result

    return partial


def log_wrap(log_info):
    def partial(query, get_description):
        log_info("BEGIN {}".format(get_description()))
        query_time = log_time(log_info)
        result = query_time(query, get_description)
        log_info("END {}\n".format(get_description()))
        return result

    return partial


def handle_error(log_error, log_info):
    def partial(query, get_description):
        try:
            query_around = log_wrap(log_info)
            return query_around(query, get_description)
        except ValueError as ex:
            correlation_id = str(uuid.uuid4())
            log_info("Correlation Id {}".format(correlation_id))
            log_info("FAILED {}\n".format(get_description()))
            log_error(ex)
            raise ValueError(
                "An error has occurred. Please contact support with correlation Id {}".format(correlation_id))

    return partial
