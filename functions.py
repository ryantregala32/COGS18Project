import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def column_analyzer(df, column_name):
    '''
    Analyzes a column for descriptive statistics.

    Parameters:
    df (DataFrame): The pandas DataFrame containing the data.
    column_name (str): The name of the column to analyze.

    Returns:
    Series: Descriptive statistics of the column.
    '''
    return df[column_name].describe()

def analyze_two_columns(df, column1, column2):
    '''
    Analyzes the correlation between two columns.

    Parameters:
    df (DataFrame): The pandas DataFrame containing the data.
    column1 (str): The first column to analyze.
    column2 (str): The second column to analyze.

    Returns:
    DataFrame: Correlation matrix between the two columns.
    '''
    return df[[column1, column2]].corr()

def compare_two_columns(df, column1, column2):
    '''
    Creates a scatter plot comparing two columns.

    Parameters:
    df: The pandas DataFrame containing the data.
    column1: The first column to compare.
    column2: The second column to compare.

    Returns:
    None
    '''
    # we are using seaborn to plot the data, using df, and the parameters
    scatter_plot = sns.scatterplot(data=df, x=column1, y=column2)
    # This is our x-axis
    plt.xlabel(column1)
    
    # This is our y-axis
    plt.ylabel(column2)
    
    # This gives us the title of the graph
    plt.title("Scatter Plot of Shooting Performance")
    
    # This makes the scatterplot have a grid
    plt.grid(True)

    # This displays the graph
    plt.show()
    

def create_line_plot(df, column1, column2):
    '''
    Creates a line plot to visualize shooting performance over time.

    Parameters:
    column1: The x-axis value (typically time or game number).
    column2: The y-axis value (e.g., shooting percentage).

    Returns:
    None
    '''
    # Create the line plot
    # This is another seaborn function, we are using df
    # column1, and column2 to plot the data
    line_plot = sns.lineplot(data=df, x=column1, y=column2)

    # Create the line of best fit (regression line)
    # We are making a line of best fit to see how
    # it looks on the graph. Overall, I expect a downward slope.
    reg_plot = sns.regplot(data=df,
                           x=column1,
                           y=column2,
                           scatter_kws={"alpha": 0.5},
                           line_kws={"color": "red"})


    # Cleaned x-axis and y-axis labels
    plt.xlabel(column1.replace("_", " ").capitalize())
    plt.ylabel(column2.replace("_", " ").capitalize())
    
    # Title of the plot
    plt.title(f"Line Plot of {column1.capitalize()} vs. {column2.capitalize()}")

    # Makes the line plot show a graph
    plt.grid(True)
    
    # Display the plot
    plt.show()
    
def shot_distribution(df, column1, column2, hue_column, palette, alpha):
    '''
    Plots the shot distribution of Lebron James' shots on the court.
    
    What I'm visualizing is the shot location from where he made a basket
    covered by the x and y axes known as column1 and column 2, with the hue column
    being the one that shows the color of the plotpoints.

    parameters :
    column1 : name of the column to use for the x-axis
    column2 : name of the column to use for the y-axis
    hue_column : name of the column to use for color encoding.

    returns :
    Wer'e not returning a value because we are showing a graph.
    
    '''

    # Plot the shot distribution
    # To show more, we can use the colors, palettes, and alpha
    # to show how our data would look at what location Lebron would
    # make the shot
    shot_chart = sns.scatterplot(
        data=df,
        x=column1,
        y=column2,
        hue=hue_column,
        palette=palette,
        alpha=alpha
    )
    # We are creating the title
    plt.title(f"Shot Chart: {column1} vs {column2}")
    # Labeling the x-axis
    plt.xlabel(column1.capitalize())
    # Labeling the y-axis
    plt.ylabel(column2.capitalize())
    # Using a data to show the results, and to point out which
    # color correlates with the shots he made and missed
    plt.legend(title=hue_column.capitalize(), loc="upper right")
    # This makes the scatterplot have a grid
    plt.grid(True)
    # We're gonna display the plot
    plt.show()




