import pandas as pd
import dash
from dash import html
from dash.dash_table import DataTable

# Load data
df0 = pd.read_csv("data/daily_sales_data_0.csv")
df1 = pd.read_csv("data/daily_sales_data_1.csv")
df2 = pd.read_csv("data/daily_sales_data_2.csv")

def make_table(df, title):
    return html.Div(
        style={"marginBottom": "40px"},
        children=[
            html.H2(title),
            DataTable(
                data=df.to_dict("records"),
                columns=[{"name": c, "id": c} for c in df.columns],
                page_size=10,
                style_table={"overflowX": "auto"},
                style_cell={"textAlign": "left", "padding": "8px"},
                style_header={"fontWeight": "bold"},
            ),
        ],
    )

app = dash.Dash(__name__)

app.layout = html.Div(
    style={"padding": "20px"},
    children=[
        html.H1("Daily Sales Data - All Files"),
        make_table(df0, "Table 1: daily_sales_data_0.csv"),
        make_table(df1, "Table 2: daily_sales_data_1.csv"),
        make_table(df2, "Table 3: daily_sales_data_2.csv"),
    ],
)

if __name__ == "__main__":
    app.run(debug=True)