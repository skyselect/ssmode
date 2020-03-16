from .constants import colors
from .constants import ss_light
from .constants import ss_dark

def style_bar_chart(ptl_fig, ytitle=''):
  # Add axis title and style the legend
  ptl_fig.layout.yaxis = {"title": ytitle, "titlefont": {"size": 12}}
  ptl_fig.layout.legend = {"xanchor":"center", "yanchor":"top", "x":0.5,"y":-0.15, "orientation":"h"}
  ptl_fig.layout.font = dict(family='Graphik, Arial, sans-serif', size=11, color='#666666')

  # Color the bars, need to modify color library with more colors
  i=0
  for bar in ptl_fig.data:
    bar.marker = {"color": colors[i % len(colors)]}
    bar.textposition='inside'
    bar.textfont={"size": 11, "color": "#FFFFFF", "family": "Graphik, Arial, sans-serif"}
    bar.hoverinfo='x+text'
    i+=1

  # Format hovering
  ptl_fig.layout.hovermode = "x"
  ptl_fig.layout.hoverlabel = {"namelength": -1, "bgcolor":"#F1F2F5"}
  return ptl_fig