OK_FORMAT = True
OK_Format = True
test = {   'name': 'q4_4',
    'points': [2, 3],
    'suites': [   {   'cases': [   {   'code': ">>> # There should be exactly as many elements in deck_statistics\n>>> # as the number 'repetitions'\n>>> len(deck_statistics) == repetitions\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Each element of deck_statistics should be between 0\n>>> # and 13 inclusive\n>>> all([0 <= k <= 13 for k in deck_statistics])\nTrue',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
