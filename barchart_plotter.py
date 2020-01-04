import matplotlib.pyplot as plt
import numpy as np


class BarChartPlotter:
    """Class used to encapsulate single measure
        from each of the 6 cases and plot them
        on barchart.

        ...
        Attributes
        ----------
        measure_name (string): String specifying which
            measure we are plotting for.
        **measures: Dictionary containing measure data
            for each of the 6 cases.

        Methods
        -------
        plot_barchart: Plots barchart displaying 
            all measures for a specific case.
    """

    def __init__(self, measure_name, **measures):
        self._measure_name = measure_name
        self._measures = measures

    @property
    def measure_name(self):
        return self._measure_name

    @measure_name.setter
    def measure_name(self, measure_name):
        self._measure_name = measure_name

    @property
    def measures(self):
        return self._measures

    @measures.setter
    def measures(self, measures):
        self._measures = measures

    def plot(self):
        case_names = []
        measures = []
        for key, value in self.measures.items():
            case_names.append(key)
            measures.append(value)
        case_names = [case_names[2], case_names[5], case_names[0],
                      case_names[1], case_names[4], case_names[3]]
        measures = [measures[2], measures[5], measures[0],
                    measures[1], measures[4], measures[3]]
        y_pos = np.arange(len(case_names))
        plt.figure(figsize=(10, 10))
        plt.bar(y_pos, measures, align='center', alpha=0.5)
        plt.xticks(y_pos, case_names, rotation=10)
        # plt.xlabel('{}'.format(self.measure_name))
        plt.ylabel('Measure')
        plt.title('{} Measure for Each of the Six Cases:'.format(
            self.measure_name))
        plt.savefig('{}_barchart.png'.format(self.measure_name), dpi=400)
        # plt.show()
