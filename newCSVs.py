import pandas as pd


def extractNewCSVs(file):
    if "aka" in file:
        df = pd.read_csv(file, sep = "\t")
        new_df = flatten("types", "titleId", df)
        df.drop("types")
        return df, new_df




def flatten(col_to_extract, index_col, df):
    extracted = df[col_to_extract].astype(str)
    extracted=extracted.apply(lambda x: x.split(", "))
    index = df[index_col]
    new_df= pd.concat([index, extracted], axis=1)
    new_df = new_df.explode(col_to_extract)
    return new_df


if __name__ == "__main__":
    file = "title.akas.tsv"
    df, new_df = extractNewCSVs(file)
    df.to_csv("title.akas.csv", index=False)
    new_df.to_csv("titleTypes.csv", index=False)
