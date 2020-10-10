import numpy as np
import pandas as pd

scores_df = pd.read_excel('sample_scores.xlsx')
#print(scores_df)

scores_df['average'] = scores_df.mean(axis=1)

#scores_df['Pass/Fail'] = np.where(scores_df['average'] > 60, 'Pass', 'Fail')
#print(scores_df)

conditions = [
(scores_df['average'] >= 90),
(scores_df['average'] < 90) & (scores_df['average'] >= 80),
(scores_df['average'] < 80) & (scores_df['average'] >= 70),
(scores_df['average'] < 70) & (scores_df['average'] >= 60),
(scores_df['average'] < 60)
]
results = ['A', 'B', 'C', 'D', 'F']

scores_df['Letter Grade'] = np.select(conditions, results)
#print(scores_df)

scores_df['Pass/Fail'] = ['Pass' if x > 60 else 'fail' for x in scores_df['average']]
print(scores_df)
