def validate_input(log_info, input_value):
    """ expects a ValueObject """

    if input_value is None:
        raise ValueError("Invalid input")

    log_info("INPUT: {0}".format(input_value))


def validate_output(log_info, output_value):
    """ expects a ValueObject """

    if input is None:
        raise ValueError("Invalid output")

    log_info("OUTPUT: {0}".format(output_value))
