import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler


def fill_missing_median(df, columns=None):
    """
    Fill missing values in selected numeric columns
    with each column's median.

    If columns is None, all numeric columns are used.
    Returns a copy of the DataFrame.
    """
    df_copy = df.copy()

    if columns is None:
        columns = df_copy.select_dtypes(
            include=np.number
        ).columns

    for col in columns:
        df_copy[col] = df_copy[col].fillna(
            df_copy[col].median()
        )

    return df_copy


def drop_missing(df, columns=None, threshold=None):
    """
    Drop rows containing missing values.

    If columns is supplied, only missingness in those
    columns is considered.

    If threshold is supplied, rows must contain at least
    that proportion of non-missing values.

    With neither argument, all rows containing any
    missing value are dropped.
    """
    df_copy = df.copy()

    if columns is not None:
        return df_copy.dropna(subset=columns)

    if threshold is not None:
        return df_copy.dropna(
            thresh=int(
                threshold * df_copy.shape[1]
            )
        )

    return df_copy.dropna()


def normalize_data(df, columns=None, method="minmax"):
    """
    Scale selected numeric columns.

    method='minmax' uses MinMaxScaler.
    Any other method uses StandardScaler.

    If columns is None, all numeric columns are scaled.
    Returns a copy of the DataFrame.
    """
    df_copy = df.copy()

    if columns is None:
        columns = df_copy.select_dtypes(
            include=np.number
        ).columns

    if method == "minmax":
        scaler = MinMaxScaler()
    else:
        scaler = StandardScaler()

    df_copy[columns] = scaler.fit_transform(
        df_copy[columns]
    )

    return df_copy