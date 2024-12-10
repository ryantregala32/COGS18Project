# Title: LeBron James Shooting Analysis (2023 Season)
# Description: This project analyzes LeBron James' shooting accuracy
# during the NBA 2023 season. Using Python libraries like pandas, seaborn, 
# and matplotlib, it explores shooting accuracy, trends, and relationships 
# between various performance metrics.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class ShotAnalyzer():
    '''
    This class analyzes LeBron James's shooting performance.
    '''

    def __init__(self, df):
        '''
        Initializes the ShotAnalyzer class.

        Parameters:
        df (pandas.DataFrame): The dataframe containing the shooting data.

        Returns :
        None because we are just initializing the parameters to be 
        instance attributes.
        '''
        self.df = df

    def column_analyzer(self, column_name):
        '''
        Analyzes a column for basic statistics (mean, std, etc.).

        Parameters:
        column_name : The name of the column to analyze.

        Returns:
        pandas.describe(): Descriptive statistics for the column.
        '''
        return self.df[column_name].describe()

    def analyze_two_columns(self, column1, column2):
        '''
        Analyzes the correlation between two columns.

        Parameters:
        column1 : The first column to analyze.
        column2 : The second column to analyze.

        Returns:
        pandas.corr(): The correlational relationship 
        between the two columns.
        '''
        return self.df[[column1, column2]].corr()

    def compare_two_columns(self, column1, column2):
        '''
        Compares two columns using a scatterplot.
    
        Parameters:
        column1 : The first column to compare.
        column2 : The second column to compare.
    
        Returns:
        None: we are just showing a scatterplot, not
        returning a value.
        '''
        # here we care setting up our x and y values,
        # and accessing data from the csv file we are
        # using
        # we are using seaborn to plot the data, using df, and the parameters
        scatter_plot = sns.scatterplot(data=self.df, x=column1, y=column2)
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
    
        


    def create_line_plot(self, column1, column2):
        '''
        Creates a line plot to visualize shooting performance over time.

        Parameters:
        column1 : The x-axis value (typically time or game number).
        column2 : The y-axis value (e.g., shooting percentage).

        Returns:
        None
        '''
        # This creates the line plot
        line_plot = sns.lineplot(data=self.df, x=column1, y=column2)

        # This creates the line of best fit
        reg_plot = sns.regplot(data=self.df,
        x=column1,
        y=column2,
        scatter_kws={"alpha": 0.5},
        line_kws={"color": "red"})

        # Cleaned x-axis label
        plt.xlabel(column1.replace("_", " ").capitalize())

        # Cleaned y-axis label
        plt.ylabel(column2.replace("_", " ").capitalize())
        
        # Title
        plt.title(f"Line Plot of {column1.replace('_', ' ').capitalize()} vs. {column2.capitalize()}")

        # This makes the lineplot have a grid
        plt.grid(True)

        # This displays the grid
        plt.show()


    def shot_distribution(self, column1, column2, hue_column, palette, alpha):
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
        shot_chart = sns.scatterplot(
            data=self.df,
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


