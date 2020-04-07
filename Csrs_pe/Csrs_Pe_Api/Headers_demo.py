class headers_demo(object):
    def New_headers(self):
        #步设置 header信息
        headers = {
            'Accept': 'application/json, text/plain, */* ',
            'Content-Type': 'application/json;charset=UTF-8'
        }
        return headers
if __name__ == '__main__':
    headers_demo().New_headers()