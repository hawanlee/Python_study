# 定义变量
ways = 0

# 三层嵌套循环
#（1元不用计算，因为前三种货币用完后不到100的话总能用1元补上）
for a in range(11):
  # a 代表10元的数量，最大不会超过10张
  for b in range(21):
    # b 代表5元，同样不会超过20张
    for c in range(51):
      # c代表2元
      # 以上三层循环能生成这三种钱币数量的所有组合
      if (10*a+5*b+2*c<=100):
        # 判断是否小于100
        ways=ways+1
        # 小于等于100则说明：加上1元的钱币能组成100元
        print('way: '+str(ways)+', 10:'+str(a)+', 5:'+str(b)+', 2:'+str(c)+', 1:'+str(100-10*a-5*b-2*c))
        # 上边输出每种方法的组成（受限于输出窗口行数限制，可能显示不全）

print(ways)
# 最终输出所有可能的方法数量

print(2)
print(3)
for b in range (4,1001):
  is_zhi = True
  for c in range(2, b):
    if(b%c==0):
      is_zhi = False
      break
  if (is_zhi):
    print(b)