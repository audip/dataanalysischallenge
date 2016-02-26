import plotly.plotly as py
import plotly.graph_objs as go
import os
import webbrowser

trace = go.Scatter(
    x = [0.000333324, 0.006999994, 0.01699999, 0.02533333, 0.03366666, 0.04366666, 0.052, 0.06033332, 0.07033332, 0.07866666, 0.08699999],
    y = [29.8162, 29.81659, 29.81704, 29.81734, 29.81756, 29.81857, 29.81922, 29.81896, 29.8192, 29.81885, 29.82022], name='Orange Trace'
)
data = [trace]

layout = go.Layout(
    title='Industrial: Temperature v/s Time',
    xaxis=dict(
        title='Time'
    ),
    yaxis=dict(
        title='Temperature'
    ), showlegend=True, legend=dict(
        x=0.9,
        y=1
    )
)

# second_plot_url = py.plot(fig, height=1000, width=1000, auto_open=False, filename='Major technology and CPG stock prices in 2014 - scatter matrix')
# print second_plot_url
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='styling-names', sharing='private', auto_open=False)

html_string = '''
<html>
    <head>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">
        <style>body{ margin:0 100; background:whitesmoke; }</style>
    </head>
    <body>
        <h1>Plot 1: Industrial Temperature vs Time</h1>

        <!-- *** Section 1 *** --->
        <div style="margin:auto;">
            <iframe width="800" height="450" frameborder="0" seamless="seamless" scrolling="no"
    src="''' + plot_url + '''.embed?width=800&height=450"></iframe>
        </div>
    </body>
</html>'''

filename = 'reports/problem3.html'
if not os.path.exists(os.path.dirname(filename)):
    try:
        os.makedirs(os.path.dirname(filename))
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise
with open(filename, "w") as f:
    f.write(html_string)
    f.close()

print "Plot complete, report available at ./reports/problem3.html"
# webbrowser.open(filename)
# full_path = os.getcwd()+'/'+filename
# print full_path
# webbrowser.open(full_path)
