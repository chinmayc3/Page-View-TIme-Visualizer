# This entrypoint file to be used in development. Start by reading README.md
from datetime import date
from datetime import datetime
import time_series_visualizer
from unittest import main
import pandas as pd
import calendar


  
# df = pd.read_csv('fcc-forum-pageviews.csv')
# df["date"] = pd.to_datetime(df["date"])
# df = df.set_index('date')
# df_bar = df.copy()
    
# df_bar["year"] = df_bar.index.year
# df_bar["month"] = df_bar.index.month_name()

# df_bar = df_bar.groupby(["year", "month"], as_index = False).value.mean().round()
# df_bar = df_bar.fillna(method = "backfill")
# print(df_bar)
# Draw bar plot

# print(df_bar)    
# # Test your function by calling it here
time_series_visualizer.draw_line_plot()
time_series_visualizer.draw_bar_plot()
time_series_visualizer.draw_box_plot()

# # # Run unit tests automatically
main(module='test_module', exit=False)