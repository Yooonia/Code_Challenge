import pandas as pd


def find_row(col_heading, col_value):
    file_path = "https://raw.githubusercontent.com/Yooonia/Code_Challenge/main/titanic_train.csv"
    # set pandas to display all the columns
    pd.set_option('display.max_columns', None)
    df = pd.read_csv(file_path, dtype=object, header=0)
    print(df.loc[df[col_heading] == col_value])


if __name__ == '__main__':
    find_row("PassengerId","2")
