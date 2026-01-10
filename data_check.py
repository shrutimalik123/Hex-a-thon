import pandas as pd

try:
    df = pd.read_csv('data/survey.csv')
    print(f"Loaded dataset with {len(df)} rows.")
except Exception as e:
    print(f"Failed to load data: {e}")
    exit()

# Cleaning
def clean_gender(g):
    if isinstance(g, str):
        g = g.lower().strip()
        if g in ['male', 'm', 'man', 'cis male', 'mal', 'male (cis)', 'make', 'male-ish', 'maile']:
            return 'Male'
        elif g in ['female', 'f', 'woman', 'cis female', 'femake', 'female ']:
            return 'Female'
    return 'Other'

df['Gender_Clean'] = df['Gender'].apply(clean_gender)
print("\nGender Distribution:")
print(df['Gender_Clean'].value_counts())

print("\nMissing Values:")
print(df.isnull().sum()[df.isnull().sum() > 0])
