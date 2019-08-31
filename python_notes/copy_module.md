# copy模块的copy()和deepcopy()函数

```
import copy
a = [1,2,3,4]
b = copy.copy(a)
b[1] = 3
# 不影响a的值

c = [1, [2,3], [2,3,4],5]
d = copy.deepcopy(c)
# 当内部有列表等值时，使用deepcopy()
```