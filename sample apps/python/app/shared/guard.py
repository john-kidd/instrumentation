def validate_input(log_info, description, input_value):
    if input_value is None:
        raise ValueError("Invalid input")

    log_info("INPUT {}\n{}".format(description, input_value))


def validate_output(log_info, description, output_value):
    if output_value is None:
        raise ValueError("Invalid output")

    log_info("OUTPUT {}\n{}".format(description, output_value))
