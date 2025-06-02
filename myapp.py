from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata

# Load the gapminder dataset
df = pldata.gapminder()

# Create a Series of unique country names
countries = df['country'].drop_duplicates()

# Initialize Dash app
app = Dash(__name__)
server = app.server

# Layout
app.layout = html.Div([
    dcc.Dropdown(
        id="country-dropdown",
        options=[{"label": country, "value": country} for country in countries],
        value="Canada"  # Initial dropdown value
    ),
    dcc.Graph(id="gdp-growth")
])

# Callback for dynamic plot updates
@app.callback(
    Output("gdp-growth", "figure"),
    [Input("country-dropdown", "value")]
)
def update_graph(selected_country):
    filtered_df = df[df['country'] == selected_country]
    fig = px.line(
        filtered_df,
        x='year',
        y='gdpPercap',
        title=f"GDP per Capita Over Time - {selected_country}"
    )
    return fig

# Run the app
if __name__ == "__main__":
    app.run(debug=True)