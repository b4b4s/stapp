import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import base64
from PIL import Image
from io import BytesIO

st.set_page_config(
    layout="wide",
    page_title="Elias",
    page_icon=":skateboard:"
    )

# Function to encode image to base64
def encode_image(image_path):
    img = Image.open(image_path)
    img = img.resize((30, 20))  # Resize image to 30x20 pixels
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    encoded_image = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return f"data:image/png;base64,{encoded_image}"

# Your existing data setup...
company = [
    'UdeG',
    'INP', 'UoE',
    'HAL',
    'Schlumberger',
    'WEL MX',
    'WEL',
    'RFD'
    ]

company_long = [
    'Universidad de Gudalajara',
    'Grenoble INP',
    'University of Edinburgh',
    'Halliburton',
    'Schlumberger',
    'Whittaker Engineering MX',
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
    'Data Scientist',
    'Senior Geophysicist'
    ]

starts = [2008, 2011, 2012, 2013, 2013.6, 2018, 2021,  2024.7]

ends = [2011, 2012, 2013, 2013.6, 2018, 2021, 2024.7, 2026]

colors = ['#f1c40f', '#dc7633', '#ff9999', '#c0392b', '#1f77b4', '#00008b', '#00008b', '#3CB371']
country = ['Mexico', 'France', 'Scotland', 'England', 'Scotland', 'Mexico', 'Scotland', 'Scotland']

flag_paths = {
    'Mexico': 'images/mx.png',
    'France': 'images/fr.png',
    'Scotland': 'images/sco.png',
    'England': 'images/eng.png'
}

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
    'Flag': [flag_paths[c] for c in country]
})

# Encode flag images
df['EncodedFlag'] = df['Flag'].apply(encode_image)

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
        marker_line_color='white',
        marker_line_width=1,
        name=row['Company'],
        customdata=[[row['Company_name'], row['Position'], row['Country']]],
        hovertemplate=(
            "<span style='font-size: 16px;'><b>Company:</b> %{customdata[0]}</span><br>" +
            "<span style='font-size: 16px;'><b>Position:</b> %{customdata[1]}</span><br>" +
            "<span style='font-size: 16px;'><b>Country:</b> %{customdata[2]}</span><br>" +
            "<extra></extra>"
        ),
        showlegend=False,
        base=row['Start']
    ))

    # Add flag image at the end of each bar
    fig.add_layout_image(
        dict(
            source=row['EncodedFlag'],
            xref="x",
            yref="y",
            x=row['End'] + 0.1,
            y=row['Company'],
            sizex=0.5,
            sizey=0.8,
            xanchor="left",
            yanchor="middle",
            layer="above"
        )
    )

# The rest of your layout code remains the same...
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
        'showticklabels': False,
        'showgrid': False,
        'showline': False,
        'zeroline': False,
    },
    xaxis={
        'range': [2007, 2027],
        'tickfont': {'size': 14},
        'showgrid': False,
        'zeroline': False,
    },
    plot_bgcolor='white',
    margin={'l': 30, 'r': 30, 't': 80, 'b': 50}
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

# Add custom grid lines for every major tick
for year in major_ticks:
    fig.add_shape(
        type="line",
        x0=year, x1=year, y0=0, y1=1,
        yref="paper",
        line=dict(color="lightgray", width=1, dash="dash")
    )


st.plotly_chart(fig)
