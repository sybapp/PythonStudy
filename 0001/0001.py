# 调用 python 的随机库和字符串库
import random, string

# 激活码由字母和数字组成， string.letter 表示所有的字母，string.digits则表示[0 - 9]所有的数字
key = string.ascii_letters + string.digits


# 获得四个(字母和数字)的随机组合
def getRandom():
    return "".join(random.sample(key, 4))


# 将上述生成的group个随机组合用'-'连接起来
def getKey(group):
    return "-".join(getRandom() for i in range(group))


# 生成n个key并放到一个list里
def getKeyForN(n):
    return [getKey(4) for i in range(n)]


if __name__ == '__main__':
    print(getKeyForN(200))
