from scipy.stats import pearsonr
import pandas as pd
data = {
    'SepalLengthCm': [5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9, 5.4, 4.8, 4.8, 4.3, 5.8, 5.7, 5.4, 5.1, 5.7, 5.1],
    'SepalWidthCm': [3.5, 3.0, 3.2, 3.1, 3.6, 3.9, 3.4, 3.4, 2.9, 3.1, 3.7, 3.4, 3.0, 3.0, 4.0, 4.4, 3.9, 3.5, 3.8, 3.8]
}

df = pd.DataFrame(data)

# Calculate the Pearson correlation coefficient
corr, _ = pearsonr(df['SepalLengthCm'], df['SepalWidthCm'])

print(f"Pearson correlation coefficient: {corr}")
