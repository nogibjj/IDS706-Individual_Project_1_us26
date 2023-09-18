import polars as pl
from lib import stats_mean
from lib import stats_median
from lib import stats_mode
from lib import stats_std
# Calculating values for "No of student per staff"
data = pl.read_csv("World University Rankings 2023.csv")


def check_values(dataset):
    assert (stats_mean(dataset)) == 16.72500000000001
    assert (stats_median(dataset)) == 13.5
    assert (stats_mode(dataset)[0]) == 10.3
    assert (stats_std(dataset)) == 10.557828968365255


check_values(data)
