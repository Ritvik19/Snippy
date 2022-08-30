import plotly.graph_objs as go

data = dict(
    type="choropleth",
    locations=["India", "Russia", "Australia"],
    locationmode="country names",
    colorscale="Portland",
    z=[1.0, 2.0, 3.0],
    colorbar={"title": "Colorbar Title"},
)

layout = dict(geo={"scope": "world"})

fig = go.Figure(data=[data], layout=layout)
fig.update_layout(
    title=TITLE, font=dict(family="Courier New, monospace", size=18, color="#7f7f7f")
)

fig.show()

html_content = fig.to_html()
with open("abc.html", "w") as f:
    f.write(html_content)
