from .constants import colors
from .constants import ss_light
from .constants import ss_dark
from IPython.core.display import display, HTML

"""
Following function makes a very basic copy of Mode's KPI widget.
To get the alignment right, you will need to add the following to HTML <style>:
  #python_0345f7eb7ecc .mode-python {
    position: relative;
    top: -12px;
  }
Don't forget to update the id of the object!
"""

def display_as_kpi(kpi_name, value):
  # KPI header and middle line style and divs
  header_style="color: #393945;font-size: 18px;"
  header_html="<div style='{}'>{}</div>".format(header_style, kpi_name)
  line_style="color: #757782;letter-spacing: 0.3px;font-size: 12px;"
  line_html="<div style=\"{}\">__________________</div>".format(line_style)
  
  # KPI value style and div, add pieces together
  value_style="color: #333333;font-size: 48px;"
  value_html="<div style=\"{}\">{}</div>".format(value_style, value)
  inner_html = header_html+line_html+value_html

  # Define common styles and compose div
  outer_style="text-align: center;font-weight: 400;"
  outer_div="<div style=\"{}\">{}</div>".format(outer_style, inner_html)
  display(HTML(outer_div))