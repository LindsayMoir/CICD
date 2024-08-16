# Badly formatted example of a Python script

import pandas as pd


def process_data():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50], 'C': ['foo', 'bar', 'baz', 'qux', 'quux'], 'D': [1000, 2000, 3000, 4000, 5000]})
    df['E'] = df.apply(
        lambda row: row['A'] *
        row['B'] *
        row['D'] /
        row['A'],
        axis=1)
    filtered_df = df[df['E'] > 1].sort_values(by='E', ascending=False)
    print(
        "The processed DataFrame after applying complex operations is:\n",
        filtered_df)


if __name__ == "__main__":
    process_data()
    print('v15')
