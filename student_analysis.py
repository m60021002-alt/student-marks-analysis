
import pandas as pd

df = pd.read_csv('student_marks.csv')
# print(df)

average_marks = df['marks'].mean()
highest_marks = df['marks'].max()
lowest_marks = df['marks'].min()

# print("Average Marks", average_marks)
# print("Highest Marks", highest_marks)
# print("Lowest Marks", lowest_marks)

subject_wise = df.groupby('subject')['marks'].mean()
# print("\nSubject-wise Average Marks:")
# print(subject_wise)


df['status'] = df['marks'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')
print(df)

pass_fail_count = df['status'].value_counts()
print("\nPass /Fail Count:")
print(pass_fail_count)
