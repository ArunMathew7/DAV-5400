# Importing all the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")

# Reading the values and storing it in a dataframe using pandas
death_df = pd.read_csv(
    "https://raw.githubusercontent.com/ArunMathew7/DAV-5400/main/Analysis%20of%20death%20by%20selected%20causes%20from%202014%20to%202019/Monthly_Counts_of_Deaths_by_Select_Causes__2014-2019.csv",
    encoding="unicode_escape",
)


class inferenceAnalysis:
    """
    This class contains the functions to analyse the plots regarding research questions
    and get the conclusions of all the research questions.
    """

    def __init__(self):
        pass

    def research_question2():
        """
        Code visualizes seasonal variations in mortality for different diseases or causes over a span of months.
        By plotting each disease or cause separately, the viewer can observe how each one's mortality rate changes throughout the year.
        Patterns and trends specific to certain diseases or causes can be identified. For example, some diseases may exhibit seasonal spikes or declines.
        """

        # Select the columns representing diseases and the month
        disease_columns = death_df.columns[4:]

        # Group the dataset by month and calculate the mean number of deaths for each disease
        monthly_disease_deaths = death_df.groupby("Month")[disease_columns].mean()

        # Plotting using matplotlib
        plt.figure(figsize=(20, 6))
        plt.subplot(1, 2, 1)
        # Plot each disease separately
        for column in disease_columns:
            plt.plot(
                monthly_disease_deaths.index,
                monthly_disease_deaths[column],
                label=column,
            )

        # Add plot title and labels
        plt.title(
            "Seasonal Variations in Mortality for Different Diseases or Causes using Matplotlib"
        )
        plt.xlabel("Month")
        plt.ylabel("Mean Number of Deaths")
        plt.legend(title="Disease or Cause", bbox_to_anchor=(1.05, 1), loc="upper left")
        plt.grid(True)

        # Plotting using Seaborn
        plt.figure(figsize=(20, 6))
        plt.subplot(1, 2, 2)
        sns.lineplot(data=monthly_disease_deaths, dashes=False, markers=True)
        plt.title(
            "Seasonal Variations in Mortality for Different Diseases or Causes using Seaborn"
        )
        plt.xlabel("Month")
        plt.ylabel("Mean Number of Deaths")
        plt.legend(title="Disease or Cause", bbox_to_anchor=(1.05, 1), loc="upper left")
        plt.grid(True)
        plt.show()

    def research_question1():
        """
        Code visualizes the trends in monthly deaths due to influenza and pnuemonia over the years.
        Analysing this graph it is seen that average deaths of influenza and pnuemoia is a dip in the period of fall months
        and its high in winter period, which shows that cold weather has a role for these diseases.
        """

        # Select relevant columns
        df_subset = death_df[["Year", "Month", "Influenza and Pneumonia"]]

        # Group data by year and month and calculate the mean for Influenza and Pneumonia
        monthly_mean = df_subset.groupby(["Year", "Month"]).mean().reset_index()

        # Plotting using matplotlib
        # Plotting
        plt.figure(figsize=(20, 6))
        plt.subplot(1, 2, 1)
        sns.lineplot(
            data=monthly_mean,
            x="Month",
            y="Influenza and Pneumonia",
            hue="Year",
            marker="o",
        )

        plt.title(
            "Monthly Trends in Deaths due to Influenza and Pneumonia Over the Years using Seaborn"
        )
        plt.xlabel("Month")
        plt.ylabel("Average Deaths")
        plt.legend(title="Year", loc="upper right", bbox_to_anchor=(1.2, 1))
        plt.tight_layout()

        # Plotting using Seaborn
        plt.subplot(1, 2, 2)
        # Loop through unique years and plot the lines
        for year in monthly_mean["Year"].unique():
            year_data = monthly_mean[monthly_mean["Year"] == year]
            plt.plot(
                year_data["Month"],
                year_data["Influenza and Pneumonia"],
                marker="o",
                label=str(year),
            )

        plt.title(
            "Monthly Trends in Deaths due to Influenza and Pneumonia Over the Years using Matplotlib"
        )
        plt.xlabel("Month")
        plt.ylabel("Average Deaths")
        plt.legend(title="Year", loc="upper right", bbox_to_anchor=(1.2, 1))
        plt.tight_layout()
        plt.show()
