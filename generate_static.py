import dash
import dash_html_components as html
import dash_core_components as dcc
import preprocess
import make_viz
import plotly.io as pio
import hovertemplate as hover

# Initialize Dash app
app = dash.Dash(__name__)
app.title = 'SportsAI Project'

data = preprocess.preprocess()

pio.templates.default = 'simple_white'

fig1 = make_viz.create_scatter(data, hover.get_scatter_hover_template())
fig2 = make_viz.create_stacked_bars(data, hover.get_stacked_bar_hover_template)

# Define HTML for components
html_content = '''
<!DOCTYPE html>
<html>
<head>
    <title>SportsAI Project</title>
    <!-- Include any CSS files or styles here -->
    <link rel="stylesheet" href="assets/style.css">
</head>
<body>
    <h1>SportsAI Project</h1>
    
    <div class="viz-container">
        <div class="graph">
            {fig1}
        </div>
    </div>

    <div class="viz-container">
        <div class="graph">
            {fig2}
        </div>
    </div>

    <!-- Include any JavaScript files here if needed -->
</body>
</html>
'''.format(fig1=fig1.to_html(), fig2=fig2.to_html())

# Save the static HTML
with open("index.html", "w") as file:
    file.write(html_content)