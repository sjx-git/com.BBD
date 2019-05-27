import requests
class tester(object):
    def get_url(self):
        url = requests.get('http://192.168.8.240:8088/api/json')
        json_res = url.json()["jobs"][0]
        js = dict(json_res).values()
        print(js)
        print(dict(json_res).keys())
    def post_url(self):
        url = "http://192.168.8.240:8088/j_acegi_security_check"
        post_data = requests.post(url,data={"j_username":"sjx","j_password":"sjx@123A","from":"/","Submit":"登录"},json={})
        #print(post_data.text)
        r = post_data.status_code
        print(r)


if __name__ == '__main__':
    tester.get_url('self')
    tester.post_url('self')
