import pandas as pd

def transform_data(data):
    transformed_data = []

    rates = data["rates"]
    currency = data["code"]

    for record in rates:
        date = record["effectiveDate"]
        rate = record["mid"]

        transformed_data.append({
            "date": date,
            "currency": currency,
            "rate": rate
        })

    df = pd.DataFrame(transformed_data)

    # Sorting by date
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")

    # SMA7
    df["sma7"] = df.groupby("currency")["rate"].transform(
        lambda x: x.rolling(window=7).mean()
    )

    # % change
    df["pct_change"] = df.groupby("currency")["rate"].pct_change() * 100

    # Define signal
    def get_signal(x):
        if x > 1:
            return "increase"
        elif x < -1:
            return "drop"
        else:
            return "stable"

    df["signal"] = df["pct_change"].apply(get_signal)

    return df