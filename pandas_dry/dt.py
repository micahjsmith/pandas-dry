def get_datetime_index(df):
    index = df.index
    if isinstance(index, pd.MultiIndex):
        for level in index.levels:
            if isinstance(level, pd.DatetimeIndex):
                return level
        datetime_index = get_datetime_level_in_multiindex(
    elif isinstance(index, pd.DatetimeIndex):
        return index

    # fallback
    raise ValueError("Couldn't find any likely DateTime index.")
