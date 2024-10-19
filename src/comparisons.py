
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def compare_exam_score_by_school_type(df):
    plt.figure(figsize=(10, 6))
    sns.barplot(x='School_Type', y='Exam_Score', data=df, estimator='mean')
    plt.title('Average Exam Score by School Type')
    plt.xlabel('School Type')
    plt.ylabel('Average Exam Score')
    plt.savefig('docs/average_score_by_school_type.png')
    plt.show()

if __name__ == "__main__":
    cleaned_data = pd.read_csv('data/cleaned_education_data.csv')
    compare_exam_score_by_school_type(cleaned_data)