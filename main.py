# RUN EMPTY SERVER, CONFIGURE THE HEROKU SCHEDULER FOR RUNNING worker.py with command "python worker.py"
import dash
import dash_html_components as html
import threading as Threading
from worker import start_working
from datetime import datetime as dt

print("Running timed jobs on the background through a thread")
t1 = Threading.Thread(target=start_working)
t1.start()
print("Timed jobs started on ", dt.now())

# Create app.
app = dash.Dash(prevent_initial_callbacks=True)
server = app.server
app.layout = html.Div("None")

if __name__ == '__main__':
    app.run_server(debug=False)