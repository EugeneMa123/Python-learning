# -*- coding:utf-8 -*-
def findMinAndMax(L):
  if L!= []:
    max = L[0]
    min = L[0]
    for i in L:
      if max < i:
        max = i
      if min > i:
        min = i
    return (min,max)
  else:
    return (None,None)
  
  
# 测试
if findMinAndMax([]) != (None,None):
  print(u'测试失败！')
elif findMinAndMax([7]) != (7,7):
  print(u'测试失败！')
elif findMinAndMax([7,1]) != (1,7):
  print(u'测试失败！')
elif findMinAndMax(7,1,3,9,5) != (1,9):
  print(u'测试失败！')
else:
  print(u'测试成功！')
  
  
