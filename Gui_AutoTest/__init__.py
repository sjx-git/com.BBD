'''
 1.驱动浏览器 需要先将webdriver驱动 放到Python-script目录下，并且要先检查驱动和当前浏览器版本是否匹配，chrome标签中有相关对应表
 2.一、强制等待 time.sleep(5)
     强制等待是利用python语言自带的time库中的sleep()方法：import time time.sleep(3) sleep()顾明思义就是睡觉的意思，
     就是脚本一旦执行到条语句sleep(10)就睡10s，再执行后面的语句，他是一个强制等待的方式，使得整个脚本暂停。
     但是这种方式会导致这个脚本运行时间过长，不到万不得已尽可能少用，特殊情况下，时间设置最好不超过1秒，一般0.5秒。
    二、 隐式等待（全局）driver.implicitly_wait(20) 隐式等待相比强制等待更智能，顾明思义，在脚本中我们一般看不到等待语句，但是它会在每个页面加载的时候自动等待；
     隐式等待只需要声明一次，一般在打开浏览器后进行声明。声明之后对整个drvier的生命周期都有效，后面不用重复声明。 
     implicitly_wait()方法用来等待页面加载完成（直观的就是浏览器tab页上的小圈圈转完），implicitly_wait(10)，超时时间10s，10秒内一旦加载完成，就执行下一条语句；
     如果10秒内页面都没有加载完，就超时抛出异常。但是隐式等待依然存在一个问题，那就是程序会一直等待整个页面加载完成，也就是一般情况下你看到浏览器标签栏那个小圈不再转，
     才会执行下一步，但有时候页面想要的元素早就在加载完成了，但是因为个别js之类的东西特别慢，我仍得等到页面全部完成才能执行下一步。这里webdriver提供了一种更加智能的等待方式：显示等待
    三、显示等待 WebDriverWait(driver,30,0.1)    显示等待与隐式等待相对，显示等待必须在每个需要等待的元素前面进行声明。是针对于某个特定的元素设置的等待时间，在设置时间内，
     默认每隔一段时间检测一次当前页面某个元素是否存在，如果在规定的时间内找到了元素，则直接执行，即找到元素就执行相关操作，如果超过设置时间检测不到则抛出异常。默认检测频率为0.5s，默认抛出异常为：NoSuchElementException
      显示等待需要用到两个类：    WebDriverWait和expected_conditions两个类。1、WebDriverWait(driver,timeout,poll_frequency=0.5,ignored_exceptions=None)
     driver：浏览器驱动 timeout：最长超时时间，默认以秒为单位poll_frequency：检测的间隔步长，默认为0.5s ignored_exceptions：超时后的抛出的异常信息，默认抛出NoSuchElementExeception异常。
     WebDriverWait()中的until()和until_not()方法：
     until
     method: 在等待期间，每隔一段时间（__init__中的poll_frequency）调用这个传入的方法，直到返回值不是False message: 如果超时，抛出TimeoutException，将message传入异常
     until_not 与until相反，until是当某元素出现或什么条件成立则继续执行，until_not是当某元素消失或什么条件不成立则继续执行，参数也相同。
     expected_conditions类 各种类，达到某种条件，返回True和False presence_of_element_located 判断某个元素是否被加到了DOM树里，并不代表该元素一定可见 visibility_of_element_located判断某个元素是否可见，可见代表元素非隐藏，
     并且元素的宽和高都不等于0
     关于显示等待，也可以自己写条件： #设置等待wait = WebDriverWait(driver,10,0.5) #使用匿名函数 wait.until(lambda diver:driver.find_element_by_id('kw'))
 3.1.ActionChains用法整理
   click(on_element=None) ——单击鼠标左键
    click_and_hold(on_element=None) ——点击鼠标左键，不松开
    context_click(on_element=None) ——点击鼠标右键
    double_click(on_element=None) ——双击鼠标左键
    drag_and_drop(source, target) ——拖拽到某个元素然后松开
    drag_and_drop_by_offset(source, xoffset, yoffset) ——拖拽到某个坐标然后松开
    key_down(value, element=None) ——按下某个键盘上的键
    key_up(value, element=None) ——松开某个键
    move_by_offset(xoffset, yoffset) ——鼠标从当前位置移动到某个坐标
    move_to_element(to_element) ——鼠标移动到某个元素
    move_to_element_with_offset(to_element, xoffset, yoffset) ——移动到距某个元素（左上角坐标）多少距离的位置
    perform() ——执行链中的所有动作
    release(on_element=None) ——在某个元素位置松开鼠标左键
    send_keys(*keys_to_send) ——发送某个键到当前焦点的元素
    send_keys_to_element(element, *keys_to_send) ——发送某个键到指定元素
4.

 '''