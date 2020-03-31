# ssmode

### Installing & Importing
To use the helper functions in a Mode Python Notebook, first install the package by adding this cell:
```python
pip install ssmode -t "/tmp" > /dev/null 2>&1
```
You can then import various functions like:
```python
from ssmode.tables import style_table
```

### Styling Documentation
The functions in files `bar_chart.py`, `kpi.py`, `tables.py` are designed to "fake" the Mode Analytics built-in widgets from the Notebook.

##### Styling Tables
`style_table(df, hl_type=None, n=3, bar_cols=[])`
- `df`: Pandas Dataframe (index will not be displayed)
- `hl_type`: `None` or string `'nlargest'`, `'gradient'` or `'bars'` specifying cell highlighting type
- `n`: integer > 0 specifying how many greatest cells will be highlighted (only applicable for `hl_type='nlargest'`), all numeric columns will get this style
- `bar_cols`: array of strings specifying which columns will get the "bar charty style" (only applicable for `hl_type='bars'`)

##### Styling Bar & Line Charts
`style_bar_chart(ptl_fig, ytitle='')` OR `style_line_chart(ptl_fig, ytitle='')`
- `ptl_fig`: plotly chart with bars
- `ytitle`: title on y-axis

##### Displaying KPI Widget
`display_as_kpi(kpi_name, value)`
- `kpi_name`: string specifying KPI title/name (displayed on top)
- `value`: value of the KPI (large value)

### Processing Functions Documentation

##### Outlier Removal
`prune_quotes(df, variable_col, group_cols, log_scale=True, k=1.5, max_diffs=[(2,3),(3,5),(4,10)])`
- `df`: Pandas Dataframe with data to remove outliers from
- `variable_col`: string with column name based on which outliers will be removed (e.g. `'price'`)
- `group_cols`: array of string(s) with columns to group `df` by for quartile calculation purposes (e.g. `['item_id']`)
- `log_scale`: boolean specifying whether to use logarithmic scale for outlier removal
- `k`: float specifying limit ranges `Q1-k*IQR` and `Q3+k*IQR`
- `max_diffs`: list of tuples with two values, each tuple specifies total number of quotes and the maximal allowed ratio between max/min quotes (if violated, RFQ will be removed before the IQR outlier detection method)