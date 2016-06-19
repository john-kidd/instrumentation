from model import ValueObject

def validate_input(log_info, input):
    """ expects a ValueObject """

    if (input == None or input.is_valid() == False):
        raise ValueError("Invalid input")

    log_info("INPUT: {0}".format(input))


def validate_output(log_info, output):
    """ expects a ValueObject """

    if (input == None or input.is_valid() == False):
        raise ValueError("Invalid ouput")

    log_info("OUTPUT: {0}".format(output))
