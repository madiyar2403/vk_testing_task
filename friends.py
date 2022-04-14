import json
import csv

from report_format import get_report_format
from api_friends import get_user_friends
from csv_or_tsv_format import get_csv_or_tsv
from json_format import get_json
from report_filename import get_report_filename


def get_report(user, report, report_file):
    """Generates a report in one of 3 formats

    Args:
        user (dict): contains information about the user's friends
        report (string): contains information about the report format
        report_file (string): contains information about filename
    """

    if report == 'TSV':
        tsv_header, tsv_data = get_csv_or_tsv(user)

        with open(f'{report_file}.tsv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f, delimiter="\t")
            writer.writerow(tsv_header)
            writer.writerows(tsv_data)

    elif report == 'JSON':
        json_data = get_json(user)

        with open(f'{report_file}.json', 'w') as f:
            f.write(json.dumps(json_data, indent=4, ensure_ascii=True))

    else:
        csv_header, csv_data = get_csv_or_tsv(user)

        with open(f'{report_file}.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(csv_header)
            writer.writerows(csv_data)

    print('Done!')


if __name__ == '__main__':
    request = get_user_friends()
    report_format = get_report_format()
    report_file = get_report_filename()
    get_report(request, report_format, report_file)
