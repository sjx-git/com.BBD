'''
一个包下，必须有此方法 在别的地方才可以引用，即便此方法是空的
一. 框架
    1.创建测试用例类，内容包括：
        测试用例和Testfixtrue的四大组件，必须要放在一起，不然执行的时候不会去运行相关设置
    2.创建测试用例集合类，内容包括：
        加载测试用例到集合，并且要return集合，以便调用使用
    3.在main集成，相关调用，内容包括
        基本就是调用 测试用例集合类中的方法
            TextTestRunner()和HTMLTestRunner()

'''
