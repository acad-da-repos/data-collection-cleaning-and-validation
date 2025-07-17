
import unittest
import pandas as pd
import numpy as np
from assignment import clean_and_validate_data

class TestDataCleaning(unittest.TestCase):
    def test_clean_and_validate_data(self):
        # Create a sample dataframe with duplicates, missing values, and invalid emails
        data = {'Name': ['Alice', 'Bob', 'Alice', 'Charlie', 'David'],
                'Age': [25, 35, 25, np.nan, 45],
                'Email': ['alice@example.com', 'bob@example.com', 'alice@example.com', 'charlie', 'david@example.com']}
        df = pd.DataFrame(data)

        result_df = clean_and_validate_data(df)

        # Check the shape of the output
        self.assertEqual(result_df.shape, (3, 3))

        # Check for duplicates
        self.assertFalse(result_df.duplicated().any())

        # Check for missing values in Age
        self.assertFalse(result_df['Age'].isnull().any())

        # Check for invalid emails
        self.assertTrue(result_df['Email'].str.contains('@').all())

if __name__ == '__main__':
    unittest.main()
