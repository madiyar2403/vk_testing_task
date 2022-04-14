from datetime import date


def get_csv_or_tsv(user):
    """Returns a list of friends for further report generation in csv or tsv format

    Args:
        user (dict): contains information about the user's friends

    Returns:
        csv_header: a list containing header names
        csv_data: a list containing a sorted by first_name list about the user's friends with required parameters
    """

    csv_header = ['First Name', 'Last Name', 'Country', 'City', 'Birth Date', 'Sex']
    csv_data = []
    for friend in user:
        first_name = friend.get('first_name')
        last_name = friend.get('last_name')
        sex = friend.get('sex')
        if sex == int(1):
            sex = 'female'
        else:
            sex = 'male'

        country = friend.get('country', {}).get('title')
        city = friend.get('city', {}).get('title')
        bdate = friend.get('bdate')
        try:
            date.isoformat(bdate)
        except TypeError:
            pass

        listing = [first_name, last_name, country, city, bdate, sex]
        csv_data.append(listing)

    return csv_header, sorted(csv_data)
