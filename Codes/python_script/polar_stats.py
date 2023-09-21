import sys

sys.path.insert(0, "./Codes/src")
from lib import column_name  # noqa: E402


def stats_mean(dataset):
    return dataset[column_name(dataset)].mean()


def stats_median(dataset):
    return dataset[column_name(dataset)].median()


def stats_mode(dataset):
    return dataset[column_name(dataset)].mode()


def stats_std(dataset):
    return dataset[column_name(dataset)].std()


def report(data):
    result = {
        "mean": (stats_mean(data)),
        "median": (stats_median(data)),
        "std_dev": (stats_std(data)),
        "mode": ((stats_mode(data)[0])),
    }
    return result
