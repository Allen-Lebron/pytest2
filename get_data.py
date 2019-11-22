import os
import json


def get_data_path(case_path):
    file_name = os.path.dirname(case_path).split(os.sep + 'tests' + os.sep, 1)
    test_data = os.sep.join([file_name[0], 'data', file_name[1], os.path.basename(case_path).replace('.py', '.json')])
    return test_data


def get_test_data(test_data_path):
    case = []
    headers = []
    querystring = []
    payload = []
    expected = []
    with open(test_data_path, encoding='utf-8') as f:
        dat = json.loads(f.read())
        test = dat['test']
        for td in test:
            case.append(td['case'])
            headers.append(td.get('headers', {}))
            querystring.append(td.get('querystring', {}))
            payload.append(td.get('payload', {}))
            expected.append(td.get('expected', {}))
            list_parameters = list(zip(case, headers, querystring, payload, expected))
            return case, list_parameters
