
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_exam_score_distribution(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Exam_Score'], bins=20, kde=True)
    plt.title('Distribution of Exam Scores')
    plt.xlabel('Exam Score')
    plt.ylabel('Frequency')
    plt.savefig('docs/exam_score_distribution.png')
    plt.show()

def plot_boxplot_score_vs_parental_involvement(df):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Parental_Involvement', y='Exam_Score', data=df)
    plt.title('Exam Score vs Parental Involvement')
    plt.xlabel('Parental Involvement Level')
    plt.ylabel('Exam Score')
    plt.savefig('docs/score_vs_parental_involvement.png')
    plt.show()

if __name__ == "__main__":
    cleaned_data = pd.read_csv('data/cleaned_education_data.csv')
    plot_exam_score_distribution(cleaned_data)
    plot_boxplot_score_vs_parental_involvement(cleaned_data)