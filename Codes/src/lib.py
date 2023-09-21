from datetime import datetime


def column_name(dataset):
    return dataset.columns[4]


def stats_mean(dataset):
    return dataset["No of student per staff"].mean()


def stats_median(dataset):
    return dataset["No of student per staff"].median()


def stats_mode(dataset):
    return dataset["No of student per staff"].mode()


def stats_std(dataset):
    return dataset["No of student per staff"].std()


def report(data):
    result = {
        "mean": (stats_mean(data)),
        "median": (stats_median(data)),
        "std_dev": (stats_std(data)),
        "mode": ((stats_mode(data)[0])),
    }

    return result


def create_summary(data, file_path):
    now = datetime.now()
    dt_string = now.strftime("%d-%b-%Y %H:%M") + " (UTC)"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(dt_string)
        f.write("\n")
        for key, value in report(data).items():
            f.write("%s:%s\n" % (key, value))
