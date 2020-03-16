import numpy as np
import pandas as pd

def remove_diff_quotes(df, limits, main_identifier, count, max_diff):
    """Remove bids on items that have count quotes if min/max differ by >max_diff times"""
    df_copy = df.copy()
    df_copy["too_diff_quotes"] = np.logical_and(limits.loc[df[main_identifier]]['count'].values == count, limits.loc[df[main_identifier]]['max'].values/limits.loc[df[main_identifier]]['min'].values > max_diff)
    return df_copy[~df_copy["too_diff_quotes"]]

def prune_quotes(df, variable_col, group_cols, log_scale=True, k=1.5, max_diffs=[(2,3),(3,5),(4,10)]):
    """ 
    Remove abnormal quotes from df. The variable_col can be price, time_to_bid etc, although this
    function has been mainly used for removing price outliers thus far. Group_cols specify columns
    to group by for statistics (e.g. item_id can be sufficient for this) and extracting counts and
    quartiles. The variable max_diffs is a list of tuples (m,l) and these specify to remove RFQ's,
    where we have m quotes and the min/max differ by more than l times (see remove_diff_quotes). 
    After that, anything over Q3+k*IQR and below Q1-k*IQR will be removed.
    First element of group_cols must specify other values of columns in group_cols uniquely."""
    main_identifier = group_cols[0]
    df_copy = df.copy()
    if log_scale:
        df_copy['analysis_col']=np.log(df_copy[variable_col].values)
    else:
        df_copy['analysis_col']=df_copy[variable_col]
    grouped = df_copy[group_cols + [variable_col, 'analysis_col']].groupby(group_cols)

    limits = grouped.quantile(q=0.75).rename(columns={'analysis_col':'Q3'}).drop(columns=[variable_col])
    limits['Q1'] = grouped.quantile(q=0.25)['analysis_col']
    limits['upper'] = limits['Q3'].values+k*(limits['Q3'].values-limits['Q1'].values)
    limits['lower'] = limits['Q1'].values-k*(limits['Q3'].values-limits['Q1'].values)
    limits['count'] = grouped.count()[variable_col]
    limits['max'] = grouped.max()[variable_col]
    limits['min'] = grouped.min()[variable_col]
    limits=limits.reset_index().set_index(main_identifier)

    for val in max_diffs:
        df_copy = remove_diff_quotes(df_copy, limits, main_identifier, val[0], val[1])
    
    df_copy['upper_outlier'] = df_copy['analysis_col'].values > limits.loc[df_copy[main_identifier]]['upper'].values
    df_copy['lower_outlier'] = df_copy['analysis_col'].values < limits.loc[df_copy[main_identifier]]['lower'].values
    df_copy=df_copy[~df_copy['upper_outlier']]
    df_copy=df_copy[~df_copy['lower_outlier']]

    return df_copy