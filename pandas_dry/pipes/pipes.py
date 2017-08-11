import pandas as pd

from pandas_dry._utils import flatten_strings

def move_column(df, name, position=0):
    if name not in df.columns:
        raise ValueError("Column '{}' not in DataFrame".format(name))

    df = df.copy()
    col = df[name]
    del df[name]
    df.insert(position, name, col)
    return df

def flatten_multiindex(df, sep, axis=1):
    df = df.copy()
    df.set_axis(axis, df._get_axis(axis).map(lambda x: flatten_strings(x, sep=sep)))
    return df

def add_level(df, value, axis=1, name=None):
    df = df.copy()
    axis_ = df._get_axis(axis)
    names = axis_.names
    new_index = pd.MultiIndex.from_tuples(
        [[value] + list(x) for x in axis_],
        names = [name] + names
    )
    df.set_axis(axis, new_index)
    return df

def drop_level(df, level, axis=1):
    df = df.copy()
    df.set_axis(axis, df._get_axis(axis).droplevel(level))
    return df
