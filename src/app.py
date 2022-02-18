

# Dash
import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import plotly.express as px

#Python
import os

#Others
import base64
import pandas as pd

#My imports
from toolbox import create_full_dir
from visualization import visuzlize


# #Read Users
# users_all = pd.read_csv(os.getcwd() + "\\assets\\accounts.csv")


UPLOAD_DIRECTORY = create_full_dir('data/uploaded/')




app = dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO])

######################## Authenticasion here ####################
# pas = {}
# for i in range(0, len(users_all)):
#     case = {users_all['name'].loc[i]: users_all['password'].loc[i]}
#     pas.update(case)
#
# auth = dash_auth.BasicAuth(app, pas)

#################################################################

app.layout = html.Div(
    className='body',
    children=[
    dbc.Row(className = 'header',
            children=[
                dbc.Col([html.H1(['CSV Visualizer'])]),
                dbc.Col([]),
                ]
            ),


    ################  First Row ##########################################
    dbc.Row(className='rowNormal',children=[
        dbc.Col(id = 'row1', children =[
            html.P("Upload new files:"),
            dcc.Upload(
                id = 'upload-data',
                className='Upload',
                children=[html.Div(['Drag and Drop or ',html.A('Select Files')])],
                style={
                    "width": "80%",
                    "height": "60px",
                    "lineHeight": "60px",
                    "borderWidth": "1px",
                    "borderStyle": "dashed",
                    "borderRadius": "5px",
                    "textAlign": "center",
                    "margin": "10px",
                }
            ),
            html.Div(id='file-name', className='div-in')
        ]),
        dbc.Col([
            html.P("Select File to Visualize:"),
            dcc.Dropdown(
                id='select-file',
                className='dropdowm',
                clearable=True,
                placeholder='Select File', )

        ]),
        dbc.Col([

        ]),
        dbc.Col([]),
    ]), # End of Row 1

    ################  Second Row ##########################################
    dbc.Row(className='rowNormal', children=[

        dcc.Graph(id = 'graph-results',className='graph-results')


    ]), # End of second Row

    ################  Third Row ##########################################
    dbc.Row(className='rowNormal', children=[


    ]),  # End of Third Row


]) # End of Layout here

##############################################################################################################
###########################    Starting of Callbacks    ######################################################
##############################################################################################################

##############################################################################################################
###########################     UPDDATE GRAPH rESULTS   ######################################################
##############################################################################################################
# Functionality for upload file
@app.callback(
    Output('graph-results', 'figure'),
    [Input('select-file', 'value')],
)
def graph_results(selectedFile):

    if selectedFile == None:
        raise PreventUpdate
    else:
        df = pd.read_csv(UPLOAD_DIRECTORY+selectedFile)
        df = df.dropna()

        fig = visuzlize(df)

        return fig




##############################################################################################################
###########################     UPLOAD FILE  #################################################################
##############################################################################################################

# Functionality for upload file
@app.callback(
    Output('file-name', 'children'),
    Output('select-file', 'options'),
    [Input('upload-data', 'contents'),
     Input('upload-data', 'filename')],
)
def upload_pdf_to_server(content, filename):

    if not content:

        opt = [{'label': x, 'value': x} for x in os.listdir(UPLOAD_DIRECTORY)]

        return 'No files',opt


    data = content.encode("utf8").split(b";base64,")[1]

    with open(os.path.join(UPLOAD_DIRECTORY, filename), "wb") as fp:
        fp.write(base64.decodebytes(data))

    opt = [{'label': x, 'value': x} for x in os.listdir(UPLOAD_DIRECTORY)]

    # Extracting Information
    return filename +' uploaded!',opt




if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8091, debug=False, use_reloader=False)
