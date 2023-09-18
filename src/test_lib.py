# calling the test_script
import polars as pl
from test_script import check_values

from lib import create_summary

data = pl.read_csv('World University Rankings 2023.csv')


def test():
    check_values(data)
    create_summary(data, file_path="../Generated summary report.md")


test()
