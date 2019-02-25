
import logging
from datetime import timedelta
from requests import exceptions
from pytrends.request import TrendReq
from pytrends.exceptions import ResponseError
import time


API_DATE_FORMAT = '%Y-%m-%dT%H'


def get_trends_data(timeframe=None, *keywords):

    # Build timeframe string
    # if not timeframe:
    #     timeframe = __get_timeframe_string(start_date, end_date)

    print(keywords)

    return do_request(keywords, timeframe)



def get_hourly_trends(date, *keywords):

    # Query for a range of several dates, then filter, to get the correct hourly split
    start = date - timedelta(days=1)
    end = date + timedelta(days=2)

    timeframe = '%s %s' % (start.strftime(API_DATE_FORMAT), end.strftime(API_DATE_FORMAT))

    data_frame = do_request(keywords, timeframe)

    # if not data_frame is None:
    #     data_frame = data_frame.loc[date.strftime('%Y-%m-%d')]

    return data_frame


# Make a request, multiple times if required
def do_request(keywords, timeframe):

    request_count = 0
    max_requests = 10

    while request_count < max_requests:

        try:
            return get_trends_over_time(keywords, timeframe)
        except exceptions.SSLError:
            logging.error('SSL Error!  Retrying...')
            time.sleep(1)
        except ResponseError:
            logging.error('Pytrends Request Failed.')
            time.sleep(360)

        request_count += 1

    return None


def get_trends_over_time(keywords, timeframe, cat = 0, geo = 'GB', gprop = ''):
    print("Attempt made")

    # PyTrends client
    pytrends = TrendReq(hl='en-US', tz=-60)

    # Create the payload
    pytrends.build_payload(keywords, cat = cat, timeframe = timeframe, geo = geo, gprop = gprop)

    # Interest over time
    trends = pytrends.interest_over_time()

    time.sleep(5)
    # Return results (dataframe)
    return trends


def __get_timeframe_string(start_date, end_date):
    return '{} {}'.format(__timeframe_string(start_date), __timeframe_string(end_date))


def __timeframe_string(_datetime):
    return _datetime.strftime(API_DATE_FORMAT)

