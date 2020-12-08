# #%% preprocess the data
# import pandas as pd
# import numpy as np

# all_art_df = pd.read_csv('/Users/maryam/Google Drive/ComputerScience_PhD/covid and art/covid_art_visualization/all_scraped_data_dec06.csv', sep=',')
# #notna = df.dropna()
# #%% assign date and location

# from random import randrange
# from datetime import timedelta
# from datetime import datetime

# def random_date(start, end):
#     """
#     This function will return a random datetime between two datetime 
#     objects.
#     run example:
#     >>>random_date('1/1/2008 1:30 PM', '1/1/2009 4:50 AM')
#     """
#     start = datetime.strptime(start, '%m/%d/%Y %I:%M %p')
#     end = datetime.strptime(end, '%m/%d/%Y %I:%M %p')
#     delta = end - start
#     int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
#     random_second = randrange(int_delta)
#     randome_time = start + timedelta(seconds=random_second)
#     return randome_time.isoformat()[0:10]

# def add_random_date (all_art_df):
#     """ get a df of list of all downloaded artworks. Assign random dates to each row. """
    
#     assigned_date = ['NaN']*len(all_art_df)
#     all_art_df['date'] = assigned_date
#     for index in range(len(all_art_df)):
#         new_date = random_date('3/1/2020 1:30 PM','12/8/2020 1:30 PM')
#         all_art_df.loc[index , 'date'] = new_date
    
#     return all_art_df

# add_random_date (all_art_df)


# def add_city_coordinates(all_art_df):
#     """ get df with some of the rows having a value in the form of city names such as 
#     Moscow, Shiraz, Toronto. Add latitude and longitude for those cities. 
#     """
#     city_coordinates = pd.read_csv('/Users/maryam/Google Drive/ComputerScience_PhD/covid and art/covid_art_visualization/simplemaps_worldcities_basicv1.73/worldcities.csv', sep=',')
    
#     original_location_list = all_art_df['original location'].str.split(',').tolist()
#     assigned_lat = ['NaN']*len(all_art_df)
#     all_art_df['lat'] = assigned_lat
#     assigned_lon = ['NaN']*len(all_art_df)
#     all_art_df['lon'] = assigned_lon
#     assigned_city = ['NaN']*len(all_art_df)
#     all_art_df['sub zone'] = assigned_city
#     assigned_country = ['NaN']*len(all_art_df)
#     all_art_df['zone'] = assigned_country
#     for index,item in enumerate(original_location_list):
#         try:
#             all_art_df.loc[index, 'lat'] = city_coordinates[city_coordinates['city_ascii'].str.contains(item[0], case = False)]['lat'].get_values()[0]
#             all_art_df.loc[index, 'lon'] = city_coordinates[city_coordinates['city_ascii'].str.contains(item[0], case = False)]['lng'].get_values()[0]
#             all_art_df.loc[index, 'sub zone'] = city_coordinates[city_coordinates['city_ascii'].str.contains(item[0], case = False)]['city_ascii'].get_values()[0]
#             all_art_df.loc[index, 'zone'] = city_coordinates[city_coordinates['country'].str.contains(item[0], case = False)]['country'].get_values()[0]
#             print('real lat and lon added to index ', index, 'for ', item[0])
#         except:
#             rand_location = randrange(1,len(city_coordinates))
#             all_art_df.loc[index, 'lat'] = city_coordinates.loc[rand_location]['lat']
#             all_art_df.loc[index, 'lon'] = city_coordinates.loc[rand_location]['lng']
#             all_art_df.loc[index, 'sub zone'] = city_coordinates.loc[rand_location]['city_ascii']
#             all_art_df.loc[index, 'zone'] = city_coordinates.loc[rand_location]['country']
#             print ('nan value in original location, added a random location instead: ',\
#                 'country ', city_coordinates.loc[rand_location]['country'], 
#                 'city ', city_coordinates.loc[rand_location]['city_ascii'], 
#                 'lat ', city_coordinates.loc[rand_location]['lat'], 
#                 'lon ', city_coordinates.loc[rand_location]['lng'])
#     return all_art_df

# add_city_coordinates(all_art_df)

# all_art_df.to_csv('/Users/maryam/Google Drive/ComputerScience_PhD/covid and art/covid_art_visualization/all_art_assigned_date_zone.csv')

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
#df = pd.read_csv('/Users/maryam/Documents/covid and art visualization/covid-19-pandemic-worldwide-data.csv', sep=';')
df = pd.read_csv('/Users/maryam/Google Drive/ComputerScience_PhD/covid and art/covid_art_visualization/all_art_assigned_date_zone.csv')
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
    #df['lat'] = df['location'].apply(lambda x: str(x).split(',')[0])
    #print ('done with lat')
    #df['lon'] = df['location'].apply(lambda x: str(x).split(',')[-1])
    #print ('done with lon')
    # Saving countries positions (latitude and longitude per subzones)
    #country_position = df[['zone', 'lat', 'lon']].drop_duplicates(['zone']).set_index(['zone'])
    #print ('done with country position')

    # Pivoting per category
    df2 = df.set_index('date')
    #print ('done with pivoting')
    #df.columns = ['title / user name', 'image link']

    # Merging locations after pivoting
    #df = df.join(country_position)
    #print ('done with merging')
    # Filling nan values with 0
    df2 = df2.fillna(0)
    print ('done with filling nan valies')

    # Compute bubble sizes
    df2['size'] = 15
    print ('done with bubble size')
    
    # Compute bubble color
    df2['color'] = 100
    print ('done with bubble color')
    
    return df2

#%%
df2 = process_pandemic_data(df)
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
days= df2.index.tolist()
#Sort the dates

def sort_the_list(days):
    from datetime import datetime
    days.sort(key = lambda days: datetime.strptime(days, '%Y-%m-%d'))


sort_the_list(days)

frames = [{   
    'name':'frame_{}'.format(day),
    'data':[{
        'type':'scattermapbox',
        'lat':df2.xs(day)['lat'],
        'lon':df2.xs(day)['lon'],
        'marker':go.scattermapbox.Marker(
            size=df2.xs(day)['size'],
            color=df2.xs(day)['color'],
            # showscale=True,
            # colorbar={'title':'number', 'titleside':'top', 'thickness':4, 'ticksuffix':""},
        ),
        'customdata':np.stack((df2.xs(day)['image-href'], df2.xs(day)[ 'title/username'], pd.Series(df2.xs(day).index)), axis=-1),
        'hovertemplate': "<extra></extra><em>%{customdata[1]}  </em><br> 🏡  %{customdata[0]}<br>🚨 %{customdata[2]}",
    }],           
}for day in days]  

#%% Adding a colormap.



day = '2020-05-01'
tmp = df2.xs(day)
marker=go.scattermapbox.Marker(
      size=tmp['size'],
      color=tmp['color'],
    #   showscale=True,
    #   colorbar={'title':'number', 'titleside':'top', 'thickness':4, 'ticksuffix':''},
  )

# %%Adding custom hover information

day = '2020-05-01'
tmp = df2.xs(day)
customdata=np.stack(
  (pd.Series(tmp.index),
   tmp['image-href'],
   tmp['title/username']),
  axis=-1
),

hovertemplate="""
  <extra></extra>
  <em>%{customdata[0]}  </em><br>
  🚨  %{customdata[1]}<br>
  🏡  %{customdata[2]}<br>}
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
                {'mode':'immediate', 'frame':{'duration':30, 'redraw': True}, 'transition':{'duration':17}}
              ],
        } for day in days]
}]
# %% Play button
play_button = [{
    'type':'buttons',
    'showactive':True,
    'x':0.045, 'y':-0.04,
    'buttons':[{ 
        'label':'🎬', # Play
        'method':'animate',
        'args':[
            None,
            {
                'frame':{'duration':30, 'redraw':True},
                'transition':{'duration':17},
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
    # updatemenus=play_button,
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
# def do_click(trace, points, state):
#     if points.point_inds:
#         ind = points.point_inds[0]
#         url = df.link.iloc[ind]
#         webbrowser.open_new_tab(url)
        
# scatter.on_click(do_click)