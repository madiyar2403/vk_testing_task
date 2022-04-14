def get_report_format():
    """Returns in what format the report should be

    Returns:
        report_format: a string representing the report format
    """

    while True:
        try:
            user_input = int(input(
                "Please, enter the format in which you would like to receive the report (by default CSV):"
                "\n 1. CSV\n 2. TSV\n 3. JSON\n"
            ))
            if user_input == 2:
                report_format = "TSV"
                break
            elif user_input == 3:
                report_format = "JSON"
                break
            else:
                report_format = "CSV"
                break
        except ValueError:
            print("Please, enter the correct format")
    return report_format
