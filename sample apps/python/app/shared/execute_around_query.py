import time


def timer(log_info):
    def partial(query, get_description):
        start = time.time()
        result = query()
        stop = time.time()
        duration = stop - start
        log_info("DURATION: {} took {} milliseconds".format(get_description(), duration))
        return result

    return partial


def around(log_info):
    def partial(query, get_description):
        log_info("BEGIN: {}".format(get_description()))
        query_time = timer(log_info)
        result = query_time(query, get_description)
        log_info("END {}".format(get_description()))
        return result

    return partial


def compensate(log_error, log_info):
    def partial(query, get_description):
        try:
            query_around = around(log_info)
            return query_around(query, get_description)
        except ValueError as ex:
            log_info("FAILED: {}".format(get_description()))
            log_error(ex.message)
            raise ex

    return partial
