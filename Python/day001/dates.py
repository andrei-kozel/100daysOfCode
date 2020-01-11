from datetime import date, timedelta

start_100days = date(2017, 3, 30)
pybites_founded = date(2016, 12, 19)
pycon_date = date(2018, 5, 8)


def get_hundred_days_end_date():
    """Return a string of yyyy-mm-dd"""
    print(str(start_100days + timedelta(100)))
    return(str(start_100days + timedelta(100)))


def get_days_between_pb_start_first_joint_pycon():
    days = (pycon_date - pybites_founded).days
    print(days)
    return(days)


get_days_between_pb_start_first_joint_pycon()
get_hundred_days_end_date()
