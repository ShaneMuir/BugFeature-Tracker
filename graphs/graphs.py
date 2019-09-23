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
    """
    This function creates a pie chart for use on the profile page
    it gives our users some statistics on our bug model
    """
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
    """
    This function creates a pie chart for use on the profile page
    it gives our users some statistics on our features model
    """
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


def most_upvoted_bug():
    """
    This function creates a bar chart for use on the profile page
    it gives our users some statistics on our most upvoted bug
    """
    
    bugs = Bug.objects.order_by('-bug_upvotes').exclude(bug_upvotes=0)[:5]
    
    bar_chart = pygal.Bar(
        print_values=False,
        human_readable=True,
        show_legend=True,
        fill=True,
        style = dark_lighten_style,
        )
    bar_chart.title = "Most upvoted Bug"
    
    for bug in bugs:
        bar_chart.add(bug.title, bug.bug_upvotes)
    most_upvoted_bug = bar_chart.render()
    return most_upvoted_bug
    
    
def most_upvoted_feature():
    """
    This function creates a bar chart for use on the profile page
    it gives our users some statistics on our most upvoted feature
    """
    
    features = Feature.objects.order_by('-feature_upvotes').filter(paid=True).exclude(feature_upvotes=0)[:5]
    
    bar_chart = pygal.Bar(
        print_values=False,
        human_readable=True,
        show_legend=True,
        fill=True,
        style = dark_lighten_style,
        )
    bar_chart.title = "Most upvoted Bug"
    
    for feature in features:
        bar_chart.add(feature.title, feature.feature_upvotes)
    most_upvoted_feature = bar_chart.render()
    return most_upvoted_feature