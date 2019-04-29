class Break1:
    def demo(self):
        i = 1
        number = 1
        while i <= 100:
            if i%2 == 0:
               print("===========")
               number += 1
               if number == 20:
                  #break
                continue
                print(i)
            i += 1

if __name__ == '__main__':
    Break1.demo('self')