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


def create_summary(data, file_path="Generated summary report.md"):
    with open(file_path, "w", encoding="utf-8") as f:
        for key, value in report(data).items():
            f.write("\n![Visualization](https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/markdown/markdown.png)\n")
            f.write("%s:%s\n" % (key, value))
            f.write("\n")
