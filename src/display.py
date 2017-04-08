# Display: Graphs bee data with sliding scale
# Must install Plotly: pip install plotly
import plotly.offline as py
import plotly.graph_objs as go

# Display: call this function to graph the whole thing
def display(data):
    # Data must be a dictionary where the keys are state
    # abbreviations and values are populations.
    for stat in data.values:
        data[col] = data[col].astype(str)

    scl = [[0.0, 'rgb(229,255,204)'],[0.2, 'rgb(153,255,153)'],\
            [0.4, 'rgb(188,255,0)'], [0.6, 'rgb(102,204,0)'],[0.8, 'rgb(0,153,76)'],\
            [1.0, 'rgb(0,102,51)']]
    text = []
    text = data['state'] + '<br>' +\
        'Population: '+data['pop']+

    data = [ dict(
        type='choropleth',
        colorscale = scl,
        autocolorscale = False,
        locations = data['state'],
        z = data['pop'].astype(float),
        locationmode = 'USA-states',
        text = data,
        marker = dict(
            line = dict (
                color = 'rgb(255,255,255)',
                width = 2
            ) ),
        colorbar = dict(
            title = "Bee Population")
        ) ]

    layout = dict(
        title = 'Bee Population',
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showlakes = True,
            lakecolor = 'rgb(255, 255, 255)'),
             )

    fig = dict(data=data, layout=layout)
    py.plot(fig)

def graph():
    pass

def update():
    pass

display()
