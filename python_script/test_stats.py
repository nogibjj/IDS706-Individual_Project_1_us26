from polar_stats import stats_mean, stats_median, stats_mode, stats_std, create_summary
import polars as pl

url = "https://github.com/nogibjj/IDS706-Individual_Project_1_us26/blob/main/Ranking.csv?raw=true"

dataset = pl.read_csv(url)

# Calculating values for "No of student per staff"


def test_values(data):
    assert (stats_mean(data)) == 16.72500000000001
    assert (stats_median(data)) == 13.5
    assert (stats_mode(data)[0]) == 10.3
    assert (stats_std(data)) == 10.557828968365255


test_values(dataset)
create_summary(dataset, file_path="../Generated summary report.md")
