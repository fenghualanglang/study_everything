

import requests

def set_hospital_reserve_access_token():
    url = 'https://rainbow.arxanfintech.com/book/rainbow/v1/set_hospital_reserve_access_token'
    res = requests.get(url)
    print(res.json())

def query_hospital_reserve(token, pub_time):

    url = 'https://rainbow.arxanfintech.com/book/rainbow/v1/query_hospital_reserve?access_token={}&reserve_datetime={}'.format(token, pub_time)
    res = requests.get(url)
    print(res.json())


def delete_hospital_reserve_access_token():

    url = 'https://rainbow.arxanfintech.com/book/rainbow/v1/delete_hospital_reserve_access_token'
    res = requests.get(url)
    print(res.json())


if __name__ == '__main__':
    # set_hospital_reserve_access_token()
    token = '6aa559eb98174eaba2f0d47c8de9218b'
    pub_time = '2020-09-16'
    query_hospital_reserve(token, pub_time)
    delete_hospital_reserve_access_token()


# ss = {'retbody': {'access_token': 'e1347e6538f94283872d8bd6f8cf6d30'}, 'message': 'ok', 'retcode': 0}
