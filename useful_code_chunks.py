#%%
import pandas as pd
import plotly.express as px
import dash
import html
app = dash.Dash(__name__)
df = pd.DataFrame(
    dict(
        x=[1, 2, 3],
        y=[2, 4, 6],
        urls=[
            "https://www.google.com",
            "https://www.plotly.com",
            "https://plotly.com/dash/",
        ],
    )
)
app.layout = html.Div(
    [
        html.A(
            children="Please click this link",
            id="link",
            href="https://dash.plot.ly",
            target="_blank",
        ),
        dcc.Graph(
            id="figure",
            # specify custom_data to be the "urls" column
            figure=px.scatter(data_frame=df, x="x", y="y", custom_data=("urls",)),
        ),
    ]
)

#%%
import dash
import pandas as pd
import plotly.express as px

urls = ["https://www.google.com", "https://www.plotly.com", "https://plotly.com/dash/"]

fig = px.scatter(x=[1, 2, 3], y=[2, 4, 6], custom_data=urls)
fig.update_traces(customdata=urls)

app = dash.Dash(__name__)
#
app.layout = html.Div(
    [
        html.A(
            children="Please click this link",
            id="link",
            href="https://dash.plot.ly",
            target="_blank",
        ),
        dcc.Graph(id="figure", figure=fig),
    ]
)
# %%
