
import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def clean_data(df):
    # Remove duplicates
    df = df.drop_duplicates()
    # Handle missing values
    df = df.fillna(method='ffill')
    return df

if __name__ == "__main__":
    data = load_data('data/education_data.csv')
    cleaned_data = clean_data(data)
    cleaned_data.to_csv('data/cleaned_education_data.csv', index=False)