import plotly.express as px

import pandas as pd
wf_data = "...2019.csv"
wf_df = pd.read_csv(wf_data)
wf_df

api_token =''

fig = px.scatter_mapbox(wf_df, hover_name='Name', hover_data=['ArchiveYear', 'AcresBurned', 'AdminUnit', 'Counties','Started', 'Extinguished' ],lat='Latitude', lon="Longitude", center={'lat':36.316666, 'lon':-119.300003}, color_continuous_scale=['red', 'black'], color="AcresBurned",size_max=30, zoom=5, height = 850, width = 750, title='2019 California Wildfires',
                       )
fig.update_layout(font_size=16,  title={'xanchor': 'center','yanchor': 'top', 'y':0.95, 'x':0.5,}, title_font_size = 24, mapbox_accesstoken=api_token, mapbox_style = "mapbox://styles/ntoliverapp/ckwu41ke5748m14oyacujuiqb")
fig.update_traces(marker=dict(size=6))
fig.write_image('2019.png')
fig.write_image('2019.pdf')
fig.write_html('2019.html')
fig.show()