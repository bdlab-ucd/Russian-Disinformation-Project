import json

from barchart_plotter import BarChartPlotter

with open('NB_measures.json') as json_file:
    data_nb = json.load(json_file)

with open('SVM_measures.json') as json_file:
    data_svm = json.load(json_file)

joined_data = data_nb['cases'] + data_svm['cases']

measures_accuracy = {}
measures_precision = {}
measures_recall = {}
measures_f1 = {}
measures_sensitivity = {}
measures_specificity = {}
for case in joined_data:
    measures_accuracy[case['name']] = case['accuracy']
    measures_precision[case['name']] = case['precision']
    measures_recall[case['name']] = case['recall']
    measures_f1[case['name']] = case['f1']
    measures_sensitivity[case['name']] = case['sensitivity']
    measures_specificity[case['name']] = case['specificity']

bar_plotter_accuracy = BarChartPlotter('Accuracy', **measures_accuracy)
bar_plotter_precision = BarChartPlotter('Precision', **measures_precision)
bar_plotter_recall = BarChartPlotter('Recall', **measures_recall)
bar_plotter_f1 = BarChartPlotter('F1', **measures_f1)
bar_plotter_sensitivity = BarChartPlotter(
    'Sensitivity', **measures_sensitivity)
bar_plotter_specificity = BarChartPlotter(
    'Specificity', **measures_specificity)

bar_plotter_accuracy.plot()
bar_plotter_precision.plot()
bar_plotter_recall.plot()
bar_plotter_f1.plot()
bar_plotter_sensitivity.plot()
bar_plotter_specificity.plot()
