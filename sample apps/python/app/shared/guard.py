def validate_input(log_info, action_or_query, input_value):
    if input_value is None:
        raise ValueError("Invalid input")

    log_info("INPUT {}\n{}".format(action_or_query, input_value))


def validate_output(log_info, action_or_query, output_value):
    if output_value is None:
        raise ValueError("Invalid output")

    log_info("OUTPUT {}\n{}".format(action_or_query, output_value))
