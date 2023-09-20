# calling the test_script
import polars as pl
from test_script import check_values
from lib import create_summary

url = "https://github.com/nogibjj/IDS706-Individual_Project_1_us26/blob/main/Ranking.csv?raw=true"

data = pl.read_csv(url)

create_summary(data, file_path="./Generated summary report.md")
check_values(data)