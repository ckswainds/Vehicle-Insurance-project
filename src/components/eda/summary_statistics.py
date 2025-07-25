import pandas as pd


class SummaryStatistics:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def get_overview(self):
        """Returns a basic overview of the DataFrame including shape, columns, and data types.

        This method provides essential structural information about the DataFrame.

        Returns:
            dict: A dictionary containing the shape, columns, and data types of the DataFrame.
        """
        return {
            "shape": self.df.shape,
            "columns": self.df.columns,
            "dtypes": self.df.dtypes,
        }

    def get_missing_value_summary(self):
        """Returns a summary of missing values for each column in the DataFrame.

        This method helps identify columns with missing data and the count of missing values.

        Returns:
            pandas.DataFrame: A DataFrame with the count of missing values per column.
        """
        return self.df.isnull().sum().to_frame("missing_count")

    def get_numeric_summary(self):
        """Returns summary statistics for all numeric columns in the DataFrame.

        This method provides count, mean, std, min, max, and quartile values for numeric columns.

        Returns:
            pandas.DataFrame: A DataFrame with summary statistics for numeric columns.
        """
        return self.df.describe()

    def get_categorical_summary(self):
        """Returns summary statistics for all categorical columns in the DataFrame.

        This method provides count, unique, top, and frequency values for categorical columns.

        Returns:
            pandas.DataFrame: A DataFrame with summary statistics for categorical columns.
        """
        return self.df.select_dtypes(include="object").describe()
