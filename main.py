import os
import dash
import dash_html_components as html
import pandas as pd
from dash.dependencies import Output, Input
from dash_extensions import Download
from dash_extensions.snippets import send_data_frame

# run data worker for first time
import worker

# Create app.
app = dash.Dash(prevent_initial_callbacks=True)
app.layout = html.Div([html.Button("Download csv", id="btn"), Download(id="download")])


@app.callback(Output("download", "data"), [Input("btn", "n_clicks")])
def generate_csv(n_nlicks):
    # define path of file
    file_path_wallet = os.path.join("data_wallet.csv")
    df = pd.read_csv(file_path_wallet)
    return send_data_frame(df.to_csv, filename="wallet.csv")

if __name__ == '__main__':
    app.run_server()



