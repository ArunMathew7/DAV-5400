import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class carManufacturers:
    """
    Class contains code which extracts the data from https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json
    and returns it to a dataframe
    """

    def __init__(self, base_url="https://vpic.nhtsa.dot.gov/api/vehicles/"):
        self.base_url = base_url

    def get_all_manufacturers(self):
        """
        Function gets the response after hitting the url if the response is OK then data is stored else
        it will create an exception and print the error.

        Args:
        self - contains the url of API

        Returns:
        data["Results"] - data extracted from the API
        """
        endpoint = "getallmanufacturers"
        url = f"{self.base_url}{endpoint}?format=json"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data["Results"]
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Request Exception: {err}")

        return None

    def create_dataframe(self, manufacturers_data):
        """
        Converts the data into a dataframe.

        Args:
        manufacturers_data - contains the extracted data

        Returns:
        pd.DataFrame(manufacturers_data) - returns the extracted data as a dataframe
        """
        if manufacturers_data is not None:
            return pd.DataFrame(manufacturers_data)
        else:
            return None


carManufacturers_api = carManufacturers()
manufacturers_data = carManufacturers_api.get_all_manufacturers()

if manufacturers_data:
    df = carManufacturers_api.create_dataframe(manufacturers_data)
    print(df)
else:
    print("Failed to retrieve manufacturers data from the NHTSA API.")


class EDA:
    """
    Class is used for exploratory data analysis for the data from API
    """

    def details():
        """
        Function used to show some of the initial content of the data to get an idea on how the data looks like.
        """
        return df.head()

    def attributes():
        """
        Function used to show the attributes of data.
        """
        return df.columns

    def info():
        """
        This function shows the details of the attributes such as count of non-null values and data type.
        """
        info = df.info()
        return info

    def null_values():
        """
        Function showing the count of non-null values of each attributes.
        """
        null_values = pd.isnull(df).sum()
        return null_values

    def shape():
        """
        Function showing the dimension of the data.
        """
        shape = df.shape
        return shape

    def describe():
        """
        Function used to see the statistical summary of data
        """
        describe = df.describe()
        return describe

    def data_type():
        """
        Function used to see datatypes of attributes
        """
        data_types = df.dtypes
        return data_types

    def vehicle_types():
        # Plotting a pie chart for the distribution of vehicle types
        vehicle_types = df["VehicleTypes"].apply(
            lambda x: [item["Name"] for item in x] if x else []
        )
        flat_vehicle_types = [item for sublist in vehicle_types for item in sublist]
        plt.figure(figsize=(10, 6))
        plt.pie(
            pd.Series(flat_vehicle_types).value_counts(),
            labels=pd.Series(flat_vehicle_types).value_counts().index,
            autopct="%1.1f%%",
        )
        plt.title("Distribution of Vehicle Types")
        plt.show()

    def mfrID():
        # Distribution of Mfr_ID using histogram
        plt.figure(figsize=(12, 6))
        sns.histplot(df["Mfr_ID"], bins=20, kde=True)
        plt.show()

    def manufacturers_by_country():
        # Bar plot representing count of manufacturers by country
        plt.figure(figsize=(12, 6))
        sns.countplot(data=df, x="Country")
        plt.title("Count of Manufacturers by Country")
        plt.xticks(rotation=45)
        plt.show()

    def manufacturers_by_commonName():
        # Representation of count of manufacturers by common name by countplot
        plt.figure(figsize=(12, 6))
        sns.countplot(data=df, x="Mfr_CommonName")
        plt.title("Count of Manufacturers by Common Name")
        plt.xticks(rotation=90)
        plt.show()
