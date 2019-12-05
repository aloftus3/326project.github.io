import json
import requests
from matplotlib import pyplot as plt
from search_modules.plot_age_data import *
from search_modules.proPublicaAPI import *



def run_search3():

    congress_start_years = [] # starting year of each Congressional Session
    house_average_ages =[] # average age in the House of Rep. in each Session
    senate_average_ages =[] # average age in the Senate in each Session


    api = ProPublicaAPI() # new instance of ProPublicaAPI class

    for num in range(102, 117):
        cong = Congress(num) # new instance of Congress per each session

        session_start_year = cong.getSessionStartYear(num)
        congress_start_years.append(session_start_year)

        senate_reps_ages = cong.get_reps_ages(num, "senate", api)
        senate_average_ages.append(cong.average_age(num, senate_reps_ages))

        house_reps_ages = cong.get_reps_ages(num, "house", api)
        house_average_ages.append(cong.average_age(num, house_reps_ages))


    # preparing/assigning variables needed for visual representation of data
    plot_title = "Average Age in Congressional Chambers by Session"
    dependent_data1_name = "Senate"
    dependent_data2_name = "House"
    x_label = "Session Start Year"
    y_label = "Average Age"
    x_data = congress_start_years
    y1_data = senate_average_ages
    y2_data = house_average_ages

    # new instance of Plot class to visual date using Matplotlib
    visual = Plot(plot_title, dependent_data1_name, dependent_data2_name,
                  x_label, y_label, x_data, y1_data, y2_data)

    # invoking Plot class' method to create graph using Matplot
    visual.run_plot()
