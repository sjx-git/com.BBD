class aaa(object):
    def bb(self):
        test = ['aa','bb','vv','ff']
        print(test)

        test.append('gg')
        print(test)

        test.insert(0,11)
        print(test)
        idq = test.index('aa')
        print(idq)
        



if __name__ == '__main__':
   aaa.bb('self')
