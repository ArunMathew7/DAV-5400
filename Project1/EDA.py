#Importing all the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

#Reading the values and storing it in a dataframe using pandas
death_df = pd.read_csv("https://raw.githubusercontent.com/ArunMathew7/DAV-5400/main/Project1/Monthly_Counts_of_Deaths_by_Select_Causes__2014-2019.csv",encoding='unicode_escape')        

class EDA_analysis:
    """
    This class contains all the functions which does exploratory data analysis comparing different attributes.
    Visualises it using different graph using Matplotlib and seaborn libraries coming with conclusions based on the graphs.
    """
    def __init__(self):
       pass

    def trend_all_cause():
        """
        Code to show how the number of "All Cause" deaths changes over the years using a barplot.
        This visualization helps in understanding the temporal trends in "All Cause" mortality. 
        """
        #Setting the dimensions of the graph
        plt.figure(figsize=(12, 6))
        #Plotting using seaborn
        sns.barplot(data=death_df, x='Year', y='All Cause', hue='Month')
        #Labelling Title
        plt.title('Trend of "All Cause" Deaths Over Time')
        #Labelling X-axis
        plt.xlabel('Year')
        #Labelling Y-axis
        plt.ylabel('Number of Deaths')
        #Printing
        plt.show()

    def temp_trend():
        """
        Code illustrates how the mean "All Cause" mortality varies over different years,
        helping to visualize temporal trends in this specific health metric using line plot
        """
        # Group data by year and calculate the mean All Cause mortality for each year
        all_cause_yearly_mean = death_df.groupby("Year")["All Cause"].mean()

        # Visualize temporal trends
        plt.figure(figsize=(20, 6))

        #Plotting using matplotlib
        plt.subplot(1, 2, 1)
        plt.plot(all_cause_yearly_mean.index, all_cause_yearly_mean.values, marker='o')
        plt.xlabel("Year")
        plt.ylabel("Mean All Cause Mortality")
        plt.title("Temporal Trends in All Cause Mortality using Matplotlib")


        #Plotting using Seaborn
        plt.subplot(1,2,2)
        sns.lineplot(x=all_cause_yearly_mean.index, y=all_cause_yearly_mean.values, marker='o')
        plt.xlabel("Year")
        plt.ylabel("Mean All Cause Mortality")
        plt.title("Temporal Trends in All Cause Mortality using Seaborn")

        plt.show()

    def lead_cause():
        """
        Code illustrate the leading causes of death and their respective total death counts,
        making it easy to identify the primary causes of mortality in the dataset. 
        The causes are displayed as horizontal bars, allowing for a clear comparison of their impact.
        """
        causes_of_death = death_df.iloc[:, 4:]

        # Sum the causes of death for each year to identify leading causes
        leading_causes = causes_of_death.sum().sort_values(ascending=False)

        plt.figure(figsize=(20, 6))
        plt.subplot(1, 2, 1)

        #Plotting using matplotlib
        plt.barh(leading_causes.index, leading_causes.values)
        plt.xlabel("Total Deaths")
        plt.title("Leading Causes of Death using Matplotlib")
        plt.gca().invert_yaxis()  # Invert y-axis to display the highest cause at the top

        #Plotting using Seaborn
        plt.figure(figsize=(20, 6))
        plt.subplot(1,2,2)
        sns.barplot(x=leading_causes.values, y=leading_causes.index, orient='h')
        plt.xlabel("Total Deaths")
        plt.title("Leading Causes of Death using Seaborn")

        plt.show()

    def external_factors():
        """
        Code displays the trends over time for accidents (motor vehicle and unintentional), suicides or homicides and drug overdoses,
        allowing for a visual comparison(line plots) of how these external factors have evolved. 
        """
        
        external_factors = death_df[["Year", "Accidents (Unintentional Injuries)","Motor Vehicle Accidents", "Intentional Self-Harm (Suicide)",
                                      "Assault (Homicide)", "Drug Overdose"]]

        plt.figure(figsize=(20, 6))
        plt.subplot(1, 2, 1)
        #Plotting using matplotlib
        for factor in ["Accidents (Unintentional Injuries)","Motor Vehicle Accidents", "Intentional Self-Harm (Suicide)", "Assault (Homicide)", "Drug Overdose"]:
            plt.plot(external_factors["Year"], external_factors[factor], label=factor)
        plt.xlabel("Year")
        plt.ylabel("Number of Deaths")
        plt.title("Trends in External Factors using Matplotlib")
        plt.legend()

        #Plotting using Seaborn
        plt.subplot(1,2,2)
        for factor in ["Accidents (Unintentional Injuries)","Motor Vehicle Accidents", "Intentional Self-Harm (Suicide)", "Assault (Homicide)", "Drug Overdose"]:
            sns.lineplot(data=external_factors, x="Year", y=factor, label=factor)
        plt.xlabel("Year")
        plt.ylabel("Number of Deaths")
        plt.title("Trends in External Factors using Seaborn")
        plt.legend()

        plt.show()

    def natural_by_month():
        """
        Code for visualization of the total deaths by month due to natural causes and identifies the month with the highest number of deaths.
        Bar charts are used for visualisation
        """

        # Grouping dataset according to month and calculating total
        monthly_deaths = death_df.groupby('Month')['Natural Cause'].sum().reset_index()

        # Sort the data by total deaths in descending order to find the month with the highest number of deaths
        monthly_deaths = monthly_deaths.sort_values(by='Natural Cause', ascending=False)

        plt.figure(figsize=(20, 6))
        plt.subplot(1, 2, 1)
        #Plotting using matplotlib
        plt.bar(monthly_deaths['Month'], monthly_deaths['Natural Cause'])
        plt.xlabel('Month')
        plt.ylabel('Total Deaths')
        plt.title('Total Deaths by Month due to Natural Cause using Matplotlib')
        plt.xticks(monthly_deaths['Month'])
        
        #Plotting using Seaborn
        plt.subplot(1,2,2)
        sns.barplot(data=monthly_deaths, x='Month', y='Natural Cause')
        plt.xlabel('Month')
        plt.ylabel('Total Deaths')
        plt.title('Total Deaths by Month due to Natural Cause using Seaborn')
        
        plt.show()

    def monthly_death_disease():
        """
        Code for visualization of monthly deaths by various diseases using a heatmap, 
        making it easy to identify patterns and trends in disease-related deaths over time.
        heatmap is used to visualise this. 
        """

        # Select the columns representing diseases and the month
        disease_columns = death_df.columns[4:]

        # Group death_df by month and calculate the total deaths for each disease
        monthly_disease_deaths = death_df.groupby('Month')[disease_columns].sum()

        plt.figure(figsize=(20, 6))
        plt.subplot(1, 2, 1)
        #Plotting using matplotlib
        heatmap = plt.imshow(monthly_disease_deaths.T, cmap='YlOrRd', aspect='auto')
        plt.colorbar(heatmap, label='Total Deaths')
        plt.title('Monthly Deaths by Disease using Matplotlib')
        plt.xlabel('Month')
        plt.ylabel('Disease')
        plt.xticks(np.arange(len(monthly_disease_deaths.index)), monthly_disease_deaths.index, rotation=45)
        plt.yticks(np.arange(len(monthly_disease_deaths.columns)), monthly_disease_deaths.columns)

        #Plotting using Seaborn
        plt.figure(figsize=(20, 6))
        plt.subplot(1,2,2)
        sns.heatmap(monthly_disease_deaths.T, cmap='YlOrRd', linewidths=0.5)
        plt.title('Monthly Deaths by Disease using seaborn')
        plt.xlabel('Month')
        plt.ylabel('Disease')
        plt.xticks(rotation=45)

        plt.show()

    def correlation_matrix():
        """
        Code to use a correlation matrix which visualizes the correlation between different causes of death using a heatmap created with Matplotlib and Seaborn. 
        It helps identify relationships and associations between various causes of death in the dataset.
        """

        # Select the columns representing diseases and the month
        causes_of_death = death_df.iloc[4:]
        # Calculate correlation between different causes of death
        correlation_matrix = causes_of_death.corr()

        plt.figure(figsize=(30, 10))
        plt.subplot(1, 2, 1)
        #Plotting using matplotlib
        heatmap = plt.imshow(correlation_matrix, cmap="coolwarm", interpolation="nearest")

        plt.colorbar(heatmap)
        plt.xticks(np.arange(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=90)
        plt.yticks(np.arange(len(correlation_matrix.index)), correlation_matrix.index)
        plt.title("Correlation Matrix of Causes of Death using Matplotlib")

        # Annotate the values
        for i in range(len(correlation_matrix.index)):
            for j in range(len(correlation_matrix.columns)):
                text = plt.text(j, i, round(correlation_matrix.iloc[i, j], 2),
                                ha="center", va="center", color="black")

        #Plotting using Seaborn
        plt.figure(figsize=(30, 10))
        plt.subplot(1,2,2)
        sns.heatmap(correlation_matrix, cmap="coolwarm", annot=True)
        plt.title("Correlation Matrix of Causes of Death using Seaborn")

        plt.show()