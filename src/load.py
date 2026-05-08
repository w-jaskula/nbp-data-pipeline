def save_to_csv(df, filename="nbp_data.csv"):
    df.to_csv(filename, index=False)
    return filename