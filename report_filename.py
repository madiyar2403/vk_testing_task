import os


def get_report_filename():
    """Creates a filename for the report

    Returns:
        output_filename: a string representing the filename
    """

    module_path = os.path.dirname(os.path.realpath(__file__))
    filename = input('Please enter name of the report file (default name - report):')
    invalid = '<>:"/\|?* '

    for char in invalid:
        filename = filename.replace(char, '')
    if not filename:
        filename = 'report'

    output_filename = os.path.join(module_path, filename)

    return output_filename
