# coding: utf-8

# This file is part of Cae Mobile.
#
# Cae Mobile is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Cae Mobile is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Cae Mobile.  If not, see <http://www.gnu.org/licenses/>.

'''
Mock interface to return pre-recorded answers to requests.

'''
from json import JSONDecoder, JSONEncoder
JDECODE = JSONDecoder().decode
JENCODE = JSONEncoder().encode


class Mock(object):
    def __init__(self, **kw):
        self.__dict__.update(kw)


def get_answer(path, req_body, **kwargs):
    if path.endswith('login'):
        return mock_login(req_body)

    elif path.endswith('expenseoptions'):
        return mock_expenseoptions(req_body)

    elif path.endswith('expenses'):
        return mock_expenses(req_body, **kwargs)

    print path, req_body, kwargs
    return True, None, Mock()


def mock_login(body):
    body = JDECODE(body)
    resp = {}
    if body['login'] == 'test' and body['password'] == 'test':
        resp['status'] = 'success'
        req = Mock(resp_status=200)
    else:
        resp['status'] = 'success'
        req = Mock(resp_status=401)

    return resp['status'] == 'success', req, resp


def mock_expenseoptions(body):
    return True, Mock(resp_status=200), {
        "status": "success",
        "result": {
            "kmtypes": [
                {"amount": 1.25, "value": "3", "label": "Scooter"},
                {"amount": 1.28, "value": "4", "label": "Voiture"}],
            "expensetypes": [
                {"value": "5", "label": "Restauration"},
                {"value": "6", "label": "Fournitures"}],
            "teltypes": [
                {"percentage": 80, "value": "1", "label": "Mobile"},
                {"percentage": 80, "value": "2", "label": "Fixe + Adsl"}],
            "categories": [
                {"value": "1", "label": "Frais direct de fonctionnement"},
                {"value": "2", "label": "Frais concernant directement votre "
                    "activit\u00e9 aupr\u00e8s de vos clients"}]
            }
        }


def mock_expenses(body, **kwargs):
    print body, kwargs

    if kwargs.get('method') == 'POST':
        return True, Mock(resp_status=200), {
            "status": "success",
            "result": {
                }
            }
