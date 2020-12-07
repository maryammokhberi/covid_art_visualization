#%% preprocess the data
import pandas as pd
import numpy as np

df = pd.read_csv('/Users/maryam/Google Drive/ComputerScience_PhD/covid and art/covid_art_visualization/all_scraped_data_dec06.csv', sep=';')

#%% visualization using plotly and mapbox
# original tutorial from https://towardsdatascience.com/how-to-create-animated-scatter-maps-with-plotly-and-dash-f10bb82d357a
import pandas as pd
import numpy as np
import plotly.graph_objects as go
mapbox_access_token= open("config.ini").read()

# Define dataset path
# online_dataset_path = 'https://public.opendatasoft.com/explore/dataset/covid-19-pandemic-worldwide-data/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B'
# print ('done with downloadding online_dataset_path')
# # # Load dataset
# df = pd.read_csv(online_dataset_path, sep=';')
df = pd.read_csv('/Users/maryam/Documents/covid and art visualization/covid-19-pandemic-worldwide-data.csv', sep=';')

print ('done with df')

# # Display first 5 lines
df.head()

def process_pandemic_data(df):

    # Columns renaming
    df.columns = [col.lower() for col in df.columns]
    print ('done with df.columns')
    

    # Create a zone per zone/subzone
    df['zone'] = df['zone'].apply(str) + ' ' + df['sub zone'].apply(lambda x: str(x).replace('nan', ''))
    print ('done with zone')
    
    # Extracting latitute and longitude
    df['lat'] = df['location'].apply(lambda x: str(x).split(',')[0])
    print ('done with lat')
    df['lon'] = df['location'].apply(lambda x: str(x).split(',')[-1])
    print ('done with lon')
    # Saving countries positions (latitude and longitude per subzones)
    country_position = df[['zone', 'lat', 'lon']].drop_duplicates(['zone']).set_index(['zone'])
    print ('done with country position')

    # Pivoting per category
    df = pd.pivot_table(df, values='count', index=['date', 'zone'], columns=['category'])
    print ('done with pivoting')
    df.columns = ['confirmed', 'deaths', 'recovered']

    # Merging locations after pivoting
    df = df.join(country_position)
    print ('done with merging')
    # Filling nan values with 0
    df = df.fillna(0)
    print ('done with filling nan valies')

    # Compute bubble sizes
    df['size'] = df['confirmed'].apply(lambda x: (np.sqrt(x/100) + 1) if x > 500 else (np.log(x) / 2 + 1)).replace(np.NINF, 0)
    print ('done with bubble size')
    
    # Compute bubble color
    df['color'] = (df['recovered']/df['confirmed']).fillna(0).replace(np.inf , 0)
    print ('done with bubble color')
    
    return df

#%%
df = process_pandemic_data(df)
print('done with process_pandemic_data')
#%%
# day = '2020-05-01'
# tmp = df.xs(day)

# # Create the figure and feed it all the prepared columns
# fig = go.Figure(
#     go.Scattermapbox(
#         lat=tmp['lat'],
#         lon=tmp['lon'],
#         mode='markers',
#         marker=go.scattermapbox.Marker(
#             size=tmp['size'],
#             color=tmp['color']
#         )
#     )
# )

# # Specify layout information
# fig.update_layout(
#     mapbox=dict(
#         accesstoken=mapbox_access_token, #
#         center=go.layout.mapbox.Center(lat=45, lon=-73),
#         zoom=1
#     )
# )

# # Display the figure
# fig.show()

#%% Frames
days= df.index.levels[0].tolist()

frames = [{   
    'name':'frame_{}'.format(day),
    'data':[{
        'type':'scattermapbox',
        'lat':df.xs(day)['lat'],
        'lon':df.xs(day)['lon'],
        'marker':go.scattermapbox.Marker(
            size=df.xs(day)['size'],
            color=df.xs(day)['color'],
            showscale=True,
            colorbar={'title':'Recovered', 'titleside':'top', 'thickness':4, 'ticksuffix':' %'},
        ),
        'customdata':np.stack((df.xs(day)['confirmed'], df.xs(day)['recovered'],  df.xs(day)['deaths'], pd.Series(df.xs(day).index)), axis=-1),
        'hovertemplate': "<extra></extra><em>%{customdata[3]}  </em><br>🚨  %{customdata[0]}<br>🏡  %{customdata[1]}<br>⚰️  %{customdata[2]}",
    }],           
} for day in days]  

#%% Adding a colormap.
day = '2020-05-01'
tmp = df.xs(day)
marker=go.scattermapbox.Marker(
      size=tmp['size'],
      color=tmp['color'],
      showscale=True,
      colorbar={'title':'Recovered', 'titleside':'top', 'thickness':4, 'ticksuffix':' %'},
  )

# %%Adding custom hover information

day = '2020-05-01'
tmp = df.xs(day)
customdata=np.stack(
  (pd.Series(tmp.index),
   tmp['confirmed'],
   tmp['recovered'],
   tmp['deaths']),
  axis=-1
),

hovertemplate="""
  <extra></extra>
  <em>%{customdata[0]}  </em><br>
  🚨  %{customdata[1]}<br>
  🏡  %{customdata[2]}<br>
  ⚰️  %{customdata[3]}
  """,



#%% Sliders
sliders = [{
    'transition':{'duration': 0},
    'x':0.08, 
    'len':0.88,
    'currentvalue':{'font':{'size':15}, 'prefix':'📅 ', 'visible':True, 'xanchor':'center'},  
    'steps':[
        {
            'label':day,
            'method':'animate',
            'args':[
                ['frame_{}'.format(day)],
                {'mode':'immediate', 'frame':{'duration':100, 'redraw': True}, 'transition':{'duration':50}}
              ],
        } for day in days]
}]
# %% Play button
play_button = [{
    'type':'buttons',
    'showactive':True,
    'x':0.045, 'y':-0.08,
    'buttons':[{ 
        'label':'🎬', # Play
        'method':'animate',
        'args':[
            None,
            {
                'frame':{'duration':100, 'redraw':True},
                'transition':{'duration':50},
                'fromcurrent':True,
                'mode':'immediate',
            }
        ]
    }]
}]
# %% Putting it altogether
data = frames[0]['data']

# Adding all sliders and play button to the layout
layout = go.Layout(
    sliders=sliders,
    updatemenus=play_button,
    mapbox={
        'accesstoken':mapbox_access_token,
        'center':{"lat": 37.86, "lon": 2.15},
        'zoom':1.7,
        'style':'light',
    }
)

# Creating the figure
fig = go.Figure(data=data, layout=layout, frames=frames)

# Displaying the figure
fig.show()
# %%
def do_click(trace, points, state):
    if points.point_inds:
        ind = points.point_inds[0]
        url = df.link.iloc[ind]
        webbrowser.open_new_tab(url)
        
scatter.on_click(do_click)