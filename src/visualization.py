import plotly.express as px

def visuzlize(df):
    '''This function is general visualizer, able to visualize all kinf of csvs
    in Scatter, if I have time or date, it detects it and put is as x axis
    or else is adding as x axis the first numeric column of the dataframe'''

    # update the axis to the preferable view
    try:
        df = df.drop('_id', axis=1)
    except:
        pass

    # Make lowercase all titles and replace them
    cols = df.columns.tolist()
    cols = [each_string.lower() for each_string in cols]
    df = df.set_axis(cols, axis=1)

    # Check If I have time or Date
    elem_found = None
    time_saved = None

    time_list = ['date','time','weeks','datetime']
    for i in range (0,len(time_list)):
        if time_list[i] in cols:
            elem_found = time_list[i]
            time_saved = df[time_list[i]].tolist()


    # # Select only the numeric columns for visualization
    df = df.select_dtypes(include=['number'])


    if elem_found != None and time_list != None:

        df[elem_found] = time_saved
        fig = px.scatter(df, x=elem_found, y=df.columns)

    else:
        fig = px.scatter(df, x=cols[0], y=df.columns)

    fig.update_layout(autosize=False, height=655)

    return fig

# if __name__ == "__main__":
#
#     df = pd.read_csv('data/uploaded/starlink_launched.csv')
#
#     fig = visuzlize(df)
#
#     fig.show()














