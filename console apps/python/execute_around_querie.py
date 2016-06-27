#!/usr/bin/python

import time


def timer(log_info):
    def partial(query, get_description):
        start = time.time()
        result = query()
        stop = time.time()
        duration = stop - start
        log_info("DURATION: {} took {} millseconds".format(get_description(), duration))
        return result

    return partial


