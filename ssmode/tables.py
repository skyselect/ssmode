from .constants import colors
from .constants import ss_light
from .constants import ss_dark

def style_table(df, hl_type=None, n=3, bar_cols=[]):
  # Add basic styles to table
  font_family=("font-family", 'Graphik, Helvetica, Arial, sans-serif')
  font_size=("font-size", "12px")
  styles=[
    dict(selector="th", props=[font_family, font_size, ("color", "#191925"), ("background-color","#F1F2F5"), ("text-align", "center")]),
    dict(selector="tbody", props=[font_family, font_size, ("color", "#333333"), ("background-color","#FFFFFF")]),
    dict(selector="td", props=[("text-align", "left")])
  ]
  s=df.style.hide_index().set_table_styles(styles)
  
  # Highlight cells if specified
  if hl_type=='nlargest':
    return s.apply(highlight_nlargest, n=n)
  elif hl_type=='gradient':
    return s.background_gradient(cmap='Blues', text_color_threshold=0.6)
  elif hl_type=='bars':
    return s.bar(subset=bar_cols, color=ss_light)
  else:
    return s

def highlight_nlargest(ser, n=3, bg_color=ss_dark, text_color='#FFFFFF'):
  # Function to highlight n largest values in a dataframe (applies to all numeric columns)
  if (ser.dtype!='object' and ser.dtype!='bool' and ser.dtype!='datetime64'):
    attr = 'background-color: {}; color: {}'.format(bg_color, text_color)
    nlargest_values = ser.nlargest(n).values
    return [attr if value in nlargest_values else '' for value in ser]
  else:
    return ['' for value in ser]