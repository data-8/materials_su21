test = {   'name': 'q1_1',
    'points': 1,
    'suites': [   {   'cases': [   {'code': ">>> # Check your column labels and spelling;\n>>> h_pop.labels == ('time', 'population_total')\n", 'hidden': False, 'locked': False},
                                   {   'code': '>>> # Times should range from 1970 through 2020;\n>>> all(h_pop.sort("time").column("time") == np.arange(1970, 2021))\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
