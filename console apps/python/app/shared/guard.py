def validate_input(log_info, input_value):
    if input_value is None:
        raise ValueError("Invalid input")

    log_info("INPUT: {0}".format(input_value))


def validate_output(log_info, output_value):
    if output_value is None:
        raise ValueError("Invalid output")

    log_info("OUTPUT: {0}".format(output_value))