
from datetime import datetime, timedelta
from itertools import repeat

import _trends
import pandas
import _output

import time

INPUT_DATE_FORMAT = '%Y-%m-%d %H'


def __parse_date(date_string):
    date = datetime.strptime(date_string, INPUT_DATE_FORMAT)
    return date


def get_hours(datetime_diff):
    return datetime_diff.total_seconds() / 3600


def get_trends_dataframe(keywords, start_date, end_date):
    return (
        _trends.do_request(
            keywords = keywords,
            timeframe = _trends.__get_timeframe_string(
                start_date = start_date,
                end_date = end_date
            )
        )
    )


def get_full_trends(start_date, end_date, keywords):
    _start_date = __parse_date(start_date)
    _end_date = __parse_date(end_date) - timedelta(hours = 1)

    hours = get_hours(datetime_diff = _end_date - _start_date)

    for i in range(0, int(hours)):
        runtime = get_time_now()

        first_date = _start_date + timedelta(hours = i)
        second_date = _start_date + timedelta(hours = i + 2)

        print("Checking {} and {}".format(_trends.__timeframe_string(first_date), _trends.__timeframe_string(second_date)))

        trends_frame = get_trends_dataframe(keywords = keywords, start_date = first_date, end_date = second_date)

        try:
            trends_frame = clean_trends_frame(
                trends_frame = trends_frame,
                column_length = len(trends_frame[keywords[0]]),
                runtime = runtime
            )

            _output.output_trends_frame(trends_frame = trends_frame, filename = "trends {}.csv".format(runtime))
        except KeyError:
            print("No Data")
            continue

        time.sleep(2)

    filepath = _output.merge_trends()
    _output.clear_temp_folder()

    return filepath


def clean_trends_frame(trends_frame, column_length, runtime):
    time = [runtime]
    timestamp_col = time * column_length

    trends_frame.drop("isPartial", axis = 1, inplace = True)

    trends_frame = trends_frame.assign(Runtime = timestamp_col)

    return trends_frame


def get_time_now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

