import streamlit as st
import plotly.graph_objects as go

st.title("Wa")

# Data
jobs = ['UdeG', 'INP', 'UoE', 'HAL', 'Schlumberger', 'Whittaker Engineering', 'RFD']
starts = [2009, 2011, 2012, 2013, 2013.6, 2018, 2024.7]
ends = [2011, 2012, 2013, 2013.6, 2018, 2024.7, 2026]
colors = ['#f1c40f', '#dc7633', '#ff9999', '#c0392b', '#1f77b4', '#00008b', '#3CB371']  # Job-specific colors
durations = [end - start for start, end in zip(starts, ends)]
y_pos = list(reversed(range(len(jobs))))  # Assign each job a vertical position

# Create bars for each job
bars = []
for i in range(len(jobs)):
    bars.append(go.Bar(
        x=[durations[i]],  # Duration of each job
        y=[jobs[i]],       # Job names for the y-axis
        base=[starts[i]],  # Starting year for each job
        orientation='h',   # Horizontal bar
        marker=dict(color=colors[i], line=dict(color='white', width=1)),
        hovertemplate=f"<b>{jobs[i]}</b><br>Period: {starts[i]} - {ends[i]}<br>Duration: {durations[i]} years<extra></extra>"
    ))

# Create the figure
fig = go.Figure(data=bars)

# Customize the layout
fig.update_layout(
    title=dict(text='Career Timeline: Elias', font=dict(size=19), x=0.05),
    barmode='stack',
    height=500,
    width=800,
    xaxis=dict(
        range=[2009, 2026],
        tickvals=[2009, 2011, 2013, 2015, 2017, 2019, 2021, 2023, 2025],
        ticktext=[str(i) for i in range(2009, 2026)] + ['Present'],
        tickmode='array',
        tickangle=-45,
        showgrid=True,
        gridcolor='lightgray',
        dtick=2,  # Control tick interval
        ticks="outside",
        ticklen=10,
        tickwidth=2,
        tickcolor="gray",
        showline=True
    ),
    yaxis=dict(
        showticklabels=False,
        showgrid=False,
        zeroline=False
    ),
    paper_bgcolor='white',
    plot_bgcolor='white',
    showlegend=False
)

# Add annotations for job labels (similar to Bokeh's LabelSet)
for i, job in enumerate(jobs):
    fig.add_annotation(
        dict(
            x=starts[i],
            y=i,
            text=job,
            showarrow=False,
            xanchor='left',
            yanchor='middle',
            font=dict(size=10, color='white')
        )
    )

# Show the plot
st.plotly_chart(fig, use_container_width=True)
