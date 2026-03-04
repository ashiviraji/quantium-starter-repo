import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("data/processed_pink_morsel_sales.csv")

# Convert date
df['Date'] = pd.to_datetime(df['Date'])

# Sort by date
df = df.sort_values('Date')

app = dash.Dash(__name__)

app.layout = html.Div([

    html.H1(
        "Pink Morsels Sales Dashboard",
        style={'textAlign': 'center'}
    ),

    dcc.RadioItems(
        id='region-filter',
        options=[
            {'label': 'All', 'value': 'all'},
            {'label': 'North', 'value': 'north'},
            {'label': 'South', 'value': 'south'},
            {'label': 'East', 'value': 'east'},
            {'label': 'West', 'value': 'west'}
        ],
        value='all',
        inline=True,
        style={'textAlign': 'center'}
    ),

    dcc.Graph(id='sales-chart')

])


@app.callback(
    Output('sales-chart', 'figure'),
    Input('region-filter', 'value')
)

def update_chart(selected_region):

    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['Region'] == selected_region]

    fig = px.line(
        filtered_df,
        x='Date',
        y='Sales',
        title='Pink Morsels Sales Over Time'
    )

    return fig


if __name__ == '__main__':
    app.run(debug=True)