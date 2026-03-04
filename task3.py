import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load dataset
df = pd.read_csv("data/processed_pink_morsel_sales.csv")

# Convert date column
df['Date'] = pd.to_datetime(df['Date'])

# Sort by date
df = df.sort_values('Date')

# Create line chart
fig = px.line(df, x='Date', y='Sales', title='Pink Morsels Sales Over Time')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsels Sales Visualisation"),

    dcc.Graph(
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)