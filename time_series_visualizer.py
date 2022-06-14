import matplotlib.pyplot as plt
from datetime import date
from datetime import datetime
import pandas as pd
import calendar
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)

df = pd.read_csv('fcc-forum-pageviews.csv')
df["date"] = pd.to_datetime(df["date"])
df = df.set_index('date')
# Clean data
df = df.loc[(df["value"] >= df["value"].quantile(0.025)) & (df["value"] <= df["value"].quantile(0.975)) ]





def draw_line_plot():
    # Draw line plot

    fig,ax = plt.subplots()
    ax.plot(df.index.values, df.value)
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")



    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month_name()
    
    df_bar = df_bar.groupby(["year", "month"], as_index = False).value.mean().round()
    df_bar = df_bar.fillna(method = "backfill")
    # Draw bar plot

    labels = df_bar["year"]
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars
    
    # Draw the chart
    fig,ax = plt.subplots()
    ax.bar(x,df_bar["year"], df_bar["value"])
    

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    sns.boxplot(ax = ax1 , data = df_box , x = df_box["year"] , y = df_box["value"])
    ax1.set(xlabel="Year", ylabel="Page Views", title="Year-wise Box Plot (Trend)")
    
    sns.boxplot(ax = ax2 , data = df_box , x = df_box["month"] , y = df_box["value"] ,  order=[
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",])

    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
