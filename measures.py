import json


class Measures:
    """Class used to represent measures for
        all 6 cases tested.

        ...
        Attributes
        ----------
        file_name (string): String specifying filepath
            for all objects to write their data to.
        case_name (string): String specifying which
            case we are holding data for.
        **measures: Dictionary containing data for each
            measure on the specific case.

        Methods
        -------
        plot_barchart: Plots barchart displaying 
            all measures for a specific case.
    """

    file_name = "oversampled_dictionary.txt"

    def __init__(self, case_name, **measures):
        self._case_name = case_name
        self._accuracy = measures['accuracy']
        self._precision = measures['precision']
        self._recall = measures['recall']
        self._f1 = measures['f1']
        self._sensitivity = measures['sensitivity']
        self._specitivity = measures['specificity']
        self._measures = measures

    @property
    def accuracy(self):
        return self._accuracy

    @accuracy.setter
    def accuracy(self, accuracy):
        self._accuracy = accuracy

    @property
    def precision(self):
        return self._precision

    @precision.setter
    def precision(self, precision):
        self._precision = precision

    @property
    def recall(self):
        return self._recall

    @recall.setter
    def recall(self, recall):
        self._recall = recall

    @property
    def f1(self):
        return self._f1

    @f1.setter
    def f1(self, f1):
        self._f1 = f1

    @property
    def sensitivity(self):
        return self._sensitivity

    @sensitivity.setter
    def sensitivity(self, sensitivity):
        self._sensitivity = sensitivity

    @property
    def specitivity(self):
        return self._specitivity

    @specitivity.setter
    def specitivity(self, specitivity):
        self._specitivity = specitivity

    @property
    def measures(self):
        return self._measures

    @measures.setter
    def measures(self, measures):
        self._measures = measures

    @property
    def case_name(self):
        return self._case_name

    @case_name.setter
    def case_name(self, case_name):
        self._case_name = case_name

    def write_to_file(self):
        with open(str(Measures.file_name), 'a') as file:
            dict_to_write = self.measures
            dict_to_write['case_name'] = self.case_name
            file.write(json.dumps(dict_to_write))
