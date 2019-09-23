from bugs.models import Bug
from features.models import Feature

import pygal
from pygal.style import Style, LightenStyle

dark_lighten_style = LightenStyle('#A9A9A9',
                                   title_font_size =60,
                                   tooltip_font_size = 30,
                                   background = 'transparent',
                                   font_family = 'Muli',
                                   legend_font_size	 = 18,
                                   )

def bug_pie_chart():
    todo = Bug.objects.filter(status="To do").count()
    progress = Bug.objects.filter(status="In progress").count()
    complete = Bug.objects.filter(status="Complete").count()
    
    pie_chart = pygal.Pie(
        print_values=False,
        human_readable=True,
        show_legend=True,
        fill=True,
        style = dark_lighten_style,
        )
    pie_chart.title = 'Bugs'
    pie_chart.add('To do', todo)
    pie_chart.add('In progress', progress)
    pie_chart.add('Complete', complete)
    bug_pie_chart = pie_chart.render()
    return bug_pie_chart




def feature_pie_chart():
    todo = Feature.objects.filter(status="To do").exclude(paid=False).count()
    progress = Feature.objects.filter(status="In progress").count()
    complete = Feature.objects.filter(status="Complete").count()
    
    pie_chart = pygal.Pie(
        print_values=False,
        human_readable=True,
        show_legend=True,
        fill=True,
        style = dark_lighten_style,
        )
    pie_chart.title = "Features"
    pie_chart.add('To do', todo)
    pie_chart.add('In progress', progress)
    pie_chart.add('Complete', complete)
    feature_pie_chart = pie_chart.render()
    return feature_pie_chart


        
