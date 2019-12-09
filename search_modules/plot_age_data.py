
from matplotlib import pyplot as plt


class Plot():
    ''' This class creates a blueprint for visual presentation of data
        using Matplotlib module. '''


    def __init__(self, plot_title, dependent_data1_name, dependent_data2_name,
                x_label, y_label, x_data, y1_data, y2_data):
        self.title = plot_title
        self.data1_name = dependent_data1_name
        self.data2_name = dependent_data2_name
        self.x_label = x_label
        self.y_label = y_label
        self.x_data = x_data
        self.y1_data = y1_data
        self.y2_data = y2_data

    def run_plot(self):
        ''' Method to create a line plot representation of data. '''

        plt.style.use('seaborn-dark-palette')

        plt.plot(self.x_data, self.y1_data, color='#adad3b', linewidth=3,
        marker='o', label=self.data1_name)
        plt.plot(self.x_data, self.y2_data, color='#5a7d9a', linewidth=3,
        marker='o', label=self.data2_name)

        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.title(self.title)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('plot.png')
        plt.show()