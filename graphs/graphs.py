from bugs.models import Bug
from features.models import Feature

import pygal
from pygal.style import NeonStyle

def chart():
    todo = Bug.objects.filter(status="To do").count()
    progress = Bug.objects.filter(status="In progress").count()
    complete = Bug.objects.filter(status="Complete").count()
    
    pie_chart = pygal.Pie(
        print_values=True,
        show_legend=True,
        human_readable=True,
        fill=True,
        )
    pie_chart.title = 'Bugs'
    pie_chart.add('To do', todo)
    pie_chart.add('In progress', progress)
    pie_chart.add('Complete', complete)
    chart = pie_chart.render()
    return chart
    


        
