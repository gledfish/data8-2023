OK_FORMAT = True
OK_Format = True
test = {   'name': 'q2_1',
    'points': [0, 0, 0, 0],
    'suites': [   {   'cases': [   {'code': '>>> job_titles.num_columns\n2', 'hidden': False, 'locked': False},
                                   {'code': '>>> job_titles.num_rows\n6', 'hidden': False, 'locked': False},
                                   {   'code': '>>> # Make sure that you have the correct column labels!\n>>> np.asarray(job_titles.labels).item(1) != "Job full_array"\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> # Make sure that you have the correct column labels!\n>>> np.asarray(job_titles.labels).item(1) == "Jobs"\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
