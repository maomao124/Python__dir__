"""
 * Project name(项目名称)：Python __dir__
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/27 
 * Time(创建时间)： 22:25
 * Version(版本): 1.0
 * Description(描述)： 
 """


class C:
    def __init__(self, name, age) -> None:
        self.__name = name
        self.__age = age

    def __repr__(self) -> str:
        return "姓名：" + self.__name + ",年龄：" + str(self.__age)

    def __del__(self):
        print("调用__del__() 销毁对象，释放其空间")


if __name__ == '__main__':
    c = C("张三", 19)
    print(dir(c))
    print()
    print(c.__dir__())
