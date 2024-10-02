import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# page config
st.set_page_config(
    page_title="Elias Ortiz",
    page_icon="🏂"
)


# Data
jobs = ['UdeG', 'INP', 'UoE', 'HAL', 'Schlumberger', 'Whittaker Engineering', 'RFD']
starts = [2008, 2011, 2012, 2013, 2013.6, 2018, 2024.7]
ends = [2011, 2012, 2013, 2013.6, 2018, 2024.7, 2026]
colors = ['#f1c40f', '#dc7633', '#ff9999', '#c0392b', '#1f77b4', '#00008b', '#3CB371']

# Create a DataFrame
df = pd.DataFrame({
    'Job': jobs,
    'Start': starts,
    'End': ends,
    'Color': colors,
    'Duration': [end - start for start, end in zip(starts, ends)]
})

# Sort the DataFrame to reverse the order (bottom to top)
df = df.sort_values('Start', ascending=False).reset_index(drop=True)

# Create the figure
fig = go.Figure()

# Add the horizontal bars
for i, row in df.iterrows():
    fig.add_trace(go.Bar(
        y=[row['Job']],
        x=[row['Duration']],
        orientation='h',
        marker_color=row['Color'],
        name=row['Job'],
        hoverinfo='text',
        hovertext=f"Job: {row['Job']}<br>Period: {row['Start']:.1f} - {row['End']:.1f}<br>Duration: {row['Duration']:.1f} years",
        showlegend=False,
        base=row['Start']
    ))

# Customize the layout
fig.update_layout(
    title={
        'text': "Career Timeline: Elias",
        'font': {'size': 24},
        'x': 0.01,
    },
    height=600,
    width=1000,
    barmode='overlay',
    yaxis={
        'categoryorder': 'array',
        'categoryarray': df['Job'].tolist(),
        'showticklabels': False,  # Remove y-axis tick labels
        'showgrid': False,
        'showline': False,
        'zeroline': False,
    },
    xaxis={
        'range': [2007, 2026],
        'tickfont': {'size': 16},#, 'color': '#787878'},
        'showgrid': False,  # We'll add custom grid lines later
        'zeroline': False,
    },
    plot_bgcolor='white',
    margin={'l': 30, 'r': 30, 't': 80, 'b': 50}  # Reduced left margin
)

# Add text labels to the bars
for i, row in df.iterrows():
    fig.add_annotation(
        x=row['Start'] - 0.1,
        y=row['Job'],
        text=row['Job'],
        showarrow=False,
        font={'size': 14, 'color': 'white'},
        xanchor='left',
        xshift=5
    )

# Adjust x-axis ticks and grid lines
major_ticks = list(range(2008, 2026, 2))
minor_ticks = [year + 1 for year in major_ticks[:-1]]

fig.update_xaxes(
    ticktext=[str(year) if year != 2026 else 'Present' for year in major_ticks],
    tickvals=major_ticks,
    tickmode='array',
    minor=dict(
        ticklen=4,
        tickcolor='#787878',
        tickmode='array',
        tickvals=minor_ticks,
        tickwidth=1
    )
)

# Add custom grid lines for every other major tick
for year in major_ticks[::2]:
    fig.add_shape(
        type="line",
        x0=year, x1=year, y0=0, y1=1,
        yref="paper",
        line=dict(color="lightgray", width=1, dash="dash")
    )

st.plotly_chart(fig)
