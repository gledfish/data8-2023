OK_FORMAT = True
OK_Format = True
test = {   'name': 'q3_5',
    'points': [0, 0, 4, 0],
    'suites': [   {   'cases': [   {'code': '>>> # celsius_temperature_ranges should be an array\n>>> type(celsius_temperature_ranges) is np.ndarray\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> # Don't round your answers\n>>> np.isclose(celsius_temperature_ranges.item(0), 7.222)\nFalse", 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isclose(round(sum(celsius_temperature_ranges)), 768487)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> len(celsius_temperature_ranges) == len(max_temperatures)\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
