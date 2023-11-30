# Importing necessary libraries
import numpy as np
import pandas as pd

# Reading the values and storing it in a dataframe using pandas
death_df = pd.read_csv(
    "https://raw.githubusercontent.com/ArunMathew7/DAV-5400/main/Analysis%20of%20death%20by%20selected%20causes%20from%202014%20to%202019/Monthly_Counts_of_Deaths_by_Select_Causes__2014-2019.csv",
    encoding="unicode_escape",
)


class data:
    """
    This class contains all the functions needed for data reading,interpretation and cleaning.
    """

    def __init__(self):
        pass

    def details():
        """
        Function used to show some of the initial content of the dataset to get an idea on how the data looks like.
        """
        return death_df.head()

    def attributes():
        """
        Function used to show the attributes of dataset.
        """
        return death_df.columns

    def info():
        """
        This function shows the details of the attributes such as count of non-null values and data type.
        """
        info = death_df.info()
        return info

    def null_values():
        """
        Function showing the count of non-null values of each attributes.
        """
        null_values = pd.isnull(death_df).sum()
        return null_values

    def shape():
        """
        Function showing the dimension of the dataset.
        """
        shape = death_df.shape
        return shape

    def describe():
        """
        Function used to see the statistical summary of data
        """
        describe = death_df.describe()
        return describe

    def data_type():
        """
        Function used to see datatypes of attributes
        """
        data_types = death_df.dtypes
        return data_types
