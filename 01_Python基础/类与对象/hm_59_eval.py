# eval函数：将字符串 当成一个 有效表达式来求值 并返回计算结果
print(eval("1+2"))  # 解析为相加
print(eval("1==1"))  # 判断
print(eval("'*'*10"))  # 复制
print(eval("{1,2,3,4,}"))  # {}
print(eval("(1,2,)"))  # ()
instr= input("请输入一个算术题：")
print(eval(instr))