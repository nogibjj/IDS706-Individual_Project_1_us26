import polars as pl
from lib import stats_mean, stats_median, stats_mode, stats_std 

# Calculating values for "No of student per staff"
data = pl.read_csv('World University Rankings 2023.csv')

@pytest.fixture
def test_values(data):
    assert (stats_mean(data)) == 16.72500000000001
    assert (stats_median(data)) == 13.5
    assert (stats_mode(data)[0]) == 10.3
    assert (stats_std(data)) == 10.557828968365255
