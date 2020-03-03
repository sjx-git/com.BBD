import Request_get,Request_post
import unittest
class Auto_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print ('-'*20 + '开始测试' + '-'*20 +'\n')

    @classmethod
    def tearDownClass(cls):
        print ('-'*20 + '结束测试' + '-'*20 +'\n')

    def setUp(self):
        print ('-'*20 + '开始执行测试用例' + '-'*20 +'\n')

    def tearDown(self):
        print ('-'*20 + '结束执行测试用例' + '-'*20 +'\n')

    def test_get(self):
        Request_get.Api_test().test_get()

    def test_post(self):
        Request_post.Api_test1().test_post('1')
if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=1)
    unittest.TestSuite()
