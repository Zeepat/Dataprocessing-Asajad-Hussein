from dash import Dash, html, dcc, callback, Output, Input

app = Dash(__name__)

my_h1 = html.H1("My Dash Application") # <h1>My Dash App</h1>
my_h2 = html.H2("More info...") # <div><h1>My Dash App</h1></div>
my_dropdown = dcc.Dropdown(options=["Äpple", "Banan", "Citron"], value="Banan")
app.layout = html.Div(children=[my_h1, my_h2, my_dropdown])

@callback(
    Output(my_h2, component_property="children"),
    Input(my_dropdown, component_property="value")
)

def update_heading2(fruit):
    return fruit

app.run(debug=True)