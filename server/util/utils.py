from datetime import datetime


def convert_to_date(srt_date):
    date_str = str(srt_date).replace("-", "/")
    return datetime.strptime(date_str, '%Y/%m/%d').date()
