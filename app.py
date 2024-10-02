import streamlit as st

st.title("About me")

st.write("---")

from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool, LabelSet, SingleIntervalTicker

# Data
jobs = ['UdeG', 'INP', 'UoE', 'HAL', 'Schlumberger', 'Whittaker Engineering', 'RFD']
starts = [2009, 2011, 2012, 2013, 2013.6, 2018, 2024.7]
ends = [2011, 2012, 2013, 2013.6, 2018, 2024.7, 2026]
colors = ['#f1c40f', '#dc7633', '#ff9999', '#c0392b', '#1f77b4', '#00008b', '#3CB371']  # Job-specific colors

# Create a ColumnDataSource
source = ColumnDataSource(data=dict(
    jobs=jobs,
    starts=starts,
    ends=ends,
    colors=colors,
    durations=[end - start for start, end in zip(starts, ends)],
    y_pos=list(reversed(range(len(jobs))))  # Assign each job a vertical position
))

# Create the figure
p = figure(
    y_range=jobs[::-1],
    x_range=(2009, 2026),
    height=500,
    width=800,
    title="Career Timeline: Elias",
    toolbar_location=None,
    outline_line_color=None
)

# Add the horizontal bars (thinner with more space above and below)
p.hbar(
    y='y_pos',
    left='starts',
    right='ends',
    height=0.8,
    color='colors',
    source=source,
    line_color="white",
    line_width=1,
    fill_alpha=0.8
    )

# Add hover tool with job details
hover = HoverTool(tooltips=[
    ("Job", "@jobs"),
    ("Period", "@starts - @ends"),
    ("Duration", "@durations years")
])
p.add_tools(hover)

# Add labels to the bars
labels = LabelSet(
    x='starts',
    y='y_pos',
    text='jobs',
    level='glyph',
    x_offset=5,
    y_offset=-10,
    source=source,
    text_font_size="9pt",
    text_color="white"
    )
p.add_layout(labels)

# Customize title style
p.title.text_color = "black"
p.title.text_font_size = "19pt"
p.title.align = "left"

# Customize the plot


# Customize the x-axis to replace 2025 with '?'
p.xaxis.ticker = list(range(2009, 2027))
p.xaxis.major_label_overrides = {2026: 'Present'}

# tick lines: x
p.xaxis.ticker = SingleIntervalTicker(interval=2, num_minor_ticks=0)
p.xaxis.major_tick_in = -5
p.xaxis.major_tick_out = 10
p.axis.major_tick_line_width = 1
p.xgrid.grid_line_dash = "dashed"
p.xgrid.grid_line_color = 'lightgray'

# tick lines: y
p.yaxis.axis_line_color = None
p.ygrid.grid_line_color = None
#p.yaxis.axis_label = "Positions"

p.xaxis.major_label_standoff = 2
p.axis.major_label_text_color = "#787878"
#p.axis.major_label_text_font_style = "bold"
p.axis.major_label_text_font_size = "11px"
p.axis.axis_label_text_color = "#787878"
p.axis.axis_label_standoff = 10
# p.axis.axis_label_text_font_style="bold"

# padding
p.min_border_left = 20
p.min_border_right = 30
p.min_border_bottom = 50

p.y_range.range_padding = 0.3

# Remove y-axis ticks and labels
p.yaxis.major_label_text_font_size = '0pt'  # Hides the y-axis labels
p.yaxis.major_tick_line_color = None # Hides the major ticks
p.yaxis.minor_tick_line_color = None  # Hides the minor ticks

p.outline_line_color = None

# Display the enhanced Gantt chart
st.bokeh_chart(p, use_container_width=True)