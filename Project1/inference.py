#Importing all the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

#Reading the values and storing it in a dataframe using pandas
death_df = pd.read_csv("https://raw.githubusercontent.com/ArunMathew7/DAV-5400/main/Project1/Monthly_Counts_of_Deaths_by_Select_Causes__2014-2019.csv",encoding='unicode_escape')        

class inference_analysis:
    """
    This class contains the function to analyse and get the conclusions of the research question.
    """
    def __init__(self):
       pass

    def output():
        """
        Code visualizes seasonal variations in mortality for different diseases or causes over a span of months.
        By plotting each disease or cause separately, the viewer can observe how each one's mortality rate changes throughout the year.
        Patterns and trends specific to certain diseases or causes can be identified. For example, some diseases may exhibit seasonal spikes or declines.
        """

        # Select the columns representing diseases and the month
        disease_columns = death_df.columns[4:]

        # Group the dataset by month and calculate the mean number of deaths for each disease
        monthly_disease_deaths = death_df.groupby('Month')[disease_columns].mean()

        #Plotting using matplotlib
        plt.figure(figsize=(20, 6))
        plt.subplot(1, 2, 1)
        # Plot each disease separately
        for column in disease_columns:
            plt.plot(monthly_disease_deaths.index, monthly_disease_deaths[column], label=column)

        # Add plot title and labels
        plt.title('Seasonal Variations in Mortality for Different Diseases or Causes using Matplotlib')
        plt.xlabel('Month')
        plt.ylabel('Mean Number of Deaths')
        plt.legend(title='Disease or Cause', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.grid(True)

        #Plotting using Seaborn
        plt.figure(figsize=(20, 6))
        plt.subplot(1, 2, 2)
        sns.lineplot(data=monthly_disease_deaths, dashes=False, markers=True)
        plt.title('Seasonal Variations in Mortality for Different Diseases or Causes using Seaborn')
        plt.xlabel('Month')
        plt.ylabel('Mean Number of Deaths')
        plt.legend(title='Disease or Cause', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.grid(True)
        plt.show()