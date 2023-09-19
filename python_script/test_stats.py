from polar_stats import stats_mean, stats_median
from polar_stats import stats_mode, stats_std, create_summary
import polars as pl

url = "https://github.com/nogibjj/IDS706-Individual_Project_1_us26/blob/main/Ranking.csv?raw=true"
# Calculating values for "No of student per staff"
data = pl.read_csv(url)

def test_values(data):
    assert (stats_mean(data)) == 16.72500000000001
    assert (stats_median(data)) == 13.5
    assert (stats_mode(data)[0]) == 10.3
    assert (stats_std(data)) == 10.557828968365255
    return



