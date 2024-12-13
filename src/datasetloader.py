import pandas as pd

class DatasetLoader:
    def __init__(self, data_path):
        self.data_path = data_path
        self.df = None

    def load_data(self, file_name):
        """Loads the dataset from the given path."""
        file_path = f"{self.data_path}/{file_name}"
        self.df = pd.read_csv(file_path)
        return self.df
"""
    def clean_data(self):
        """Clean dataset (replace or remove invalid values)."""
        # Example: Remove rows with missing values in critical columns
        self.df.dropna(subset=['GHI', 'DNI', 'DHI'], inplace=True)
        
        # Example: Replace negative values in solar radiation columns
        for col in ['GHI', 'DNI', 'DHI']:
            self.df[col] = self.df[col].apply(lambda x: max(x, 0))  # Replace negative with 0
        return self.df

    def get_summary_stats(self):
        """Returns summary statistics for numerical columns."""
        return self.df.describe()

    def get_column(self, column_name):
        """Returns a specific column from the dataset."""
        return self.df[column_name]

# Example usage:
# loader = DatasetLoader('data')
# benin_data = loader.load_data('benin_data.csv')
# cleaned_benin = loader.clean_data()
# stats = loader.get_summary_stats()
