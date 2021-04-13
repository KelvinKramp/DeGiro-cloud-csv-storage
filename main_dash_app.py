#
# # DASH APP code for downloading of wallet data via link
# # import modules
# import os
# import dash
# import dash_html_components as html
# import pandas as pd
# from dash.dependencies import Output, Input
# from dash_extensions import Download
# from dash_extensions.snippets import send_data_frame
#
# # Create app.
# app = dash.Dash(prevent_initial_callbacks=True)
# server = app.server
# app.layout = html.Div([html.Button("Download csv", id="btn"), Download(id="download")])
#
#
# @app.callback(Output("download", "data"), [Input("btn", "n_clicks")])
# def generate_csv(n_nlicks):
#     # define path of file
#     cwd = os.path.dirname(os.path.realpath(__file__))
#     file_path_wallet = cwd + "NAME WALLET"
#     print(file_path_wallet)
#     print(os.path.abspath(os.getcwd()))
#     df = pd.read_csv(file_path_wallet)
#     print(df)
#     return send_data_frame(df.to_csv, filename="NAME WALLET")
#
# if __name__ == '__main__':
#     app.run_server()



