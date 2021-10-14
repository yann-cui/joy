# -*- coding:utf-8 -*-

# 已实现函数
def rand13():
    pass

# 已实现函数
def rand5():
    pass

def rand13to5():
    ret = None
    while True:
        ret = rand13()
        if ret <= 10:
            break
    return (ret+1)//2

def rand5to13():
    def rand4():
        ret = None
        while True:
            ret = rand5()
            if ret <= 4:
                break
        return ret

    ret = None
    while True:
        base = rand4()
        rate_1 = (rand4()-1)//2
        rate_2 = (rand4()-1)//2
        ret = base + 4 * rate_1 + 8 * rate_2
        if ret <= 13:
            break
    return ret
