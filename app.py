import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Data
company = ['UdeG', 'INP', 'UoE', 'HAL', 'Schlumberger', 'Whittaker Engineering', 'RFD']
company_long = [
    'Universidad de Gudalajara',
    'Grenoble INP',
    'University of Edinburgh',
    'Halliburton',
    'Schlumberger',
    'Whittaker Engineering',
    'Rock Flow Dynamics'
]
position = [
    'Bsc. Physics',
    'MRes. Fluid Dynamics',
    'Msc. Exploration Geophysics',
    'Intern Geophysicist',
    'Geophysicist',
    'Data Scientist',
    'Senior Geophysicist'
    ]
starts = [2008, 2011, 2012, 2013, 2013.6, 2018, 2024.7]
ends = [2011, 2012, 2013, 2013.6, 2018, 2024.7, 2026]
colors = ['#f1c40f', '#dc7633', '#ff9999', '#c0392b', '#1f77b4', '#00008b', '#3CB371']
country = ['Mexico', 'France', 'U.K.', 'U.K.', 'U.K.', 'Mexico & U.K.', 'U.K.']

# Create a DataFrame
df = pd.DataFrame({
    'Company': company,
    'Company_name': company_long,
    'Position': position,
    'Start': starts,
    'End': ends,
    'Color': colors,
    'Duration': [end - start for start, end in zip(starts, ends)],
    'Country': country,
})

# Sort the DataFrame to reverse the order (bottom to top)
df = df.sort_values('Start', ascending=False).reset_index(drop=True)

# Create the figure
fig = go.Figure()

# Add the horizontal bars
for i, row in df.iterrows():
    fig.add_trace(go.Bar(
        y=[row['Company']],
        x=[row['Duration']],
        orientation='h',
        marker_color=row['Color'],
        name=row['Company'],
        customdata=[[row['Company_name'], row['Position'], row['Country']]],
        hovertemplate="<b>Company:</b> %{customdata[0]}<br>" +
                      "<b>Position:</b> %{customdata[1]}<br>" +
                      "<b>Country:</b> %{customdata[2]}<br>" +
                      "<extra></extra>",
        #hoverinfo='text',
        #hovertext=f"Position: {row['Position']}<br>Period: {row['Start']:.1f} - {row['End']:.1f}<br>Duration: {row['Duration']:.1f} years",
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
        'categoryarray': df['Company'].tolist(),
        'showticklabels': False,  # Remove y-axis tick labels
        'showgrid': False,
        'showline': False,
        'zeroline': False,
    },
    xaxis={
        'range': [2007, 2027],
        'tickfont': {'size': 14},# , 'color': '#787878'},
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
        y=row['Company'],
        text=row['Company'],
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
for year in major_ticks[::1]:
    fig.add_shape(
        type="line",
        x0=year, x1=year, y0=0, y1=1,
        yref="paper",
        line=dict(color="lightgray", width=1, dash="dash")
    )

st.plotly_chart(fig)
