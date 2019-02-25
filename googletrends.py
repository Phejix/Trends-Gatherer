from datetime import datetime
import os

import click

import launch_trends

INPUT_DATE_FORMAT = '%Y-%m-%d %H'


"""
Inputs: Date Range,
        Granularity (minute/hour),
        Keywords

Example:
        Date Range: October 1 - October 31 (00:00 - 00:00)
        Granularity: Minute
        Keywords: "Dinosaur"
"""


def __parse_date(date_string):

    # TODO: check string format
    # TODO: should we take a date as a parameter then split it into hour windows elsewhere?

    date = datetime.strptime(date_string, INPUT_DATE_FORMAT)

    return date


@click.command()
@click.argument('keywords', nargs = -1)
def main(keywords):
    if len(keywords) > 5:
        click.echo("Trends only allows a max of 5 keywords at once. Currently have {}".format(len(keywords)))
        #click.echo("Current Version only allows 1 keyword at a time. Currently have {}".format(len(keywords)))
        return ""

    start_date = click.prompt('Enter the start date/time (YYYY-MM-DD HH)')
    end_date = click.prompt('Enter the end date/time (YYYY-MM-DD HH)')

    output_path = launch_trends.get_full_trends(
        start_date = start_date,
        end_date = end_date,
        keywords = keywords
    )

    os.remove(output_path)

    click.echo("File Available at {}".format(output_path))
    


if __name__ == "__main__":
    main()

