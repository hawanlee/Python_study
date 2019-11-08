ways = 0
for i in range(6):
  for j in range(11):
    for m in range(11):
      # 上边的循环能生成i从0到5，j从0到10，m从0到10的所有情况
      # 还需要其他参数就继续嵌套循环
      # 要执行判断的语句写在这里