import time
import random

def linear(l,target):
  	start_time = time.time()
  	for index,val in enumerate(l):
    	if val == target:
      		break
  	end_time = time.time()
  	exe_time = end_time - start_time
  	return exe_time
  
def bin_search(l,target):
  	start_time = time.time()
  	left = 0
  	right = len(l) - 1

  	while left <= right:
    	  mid = (left + right) // 2

      	if l[mid] == target:
        	  break
      	elif l[mid] < target:
        	  left = mid + 1
      	else:
        	  right = mid - 1
  	end_time = time.time()
  	exe_time = end_time - start_time
  	return exe_time
  
  
def fib(l_len):
    fib_list = [0]*l_len
    fib_list[1] = 1
    for i in range(2,l_len):
        fib_list[i] = fib_list[i-1] + fib_list[i-2]
    return fib_list

def getY(fib_list, n):
    i = 0
    while fib_list[i] <= n:
        i += 1
    return i - 1





def fib_search(l,target):
  	fib_list = fib(len(l))
  	max =  len(l) - 1
  	y = getY(fib_list, max + 1)
  	m = max - fib_list[y]
  	x = y - 1
  	i = x
  	start_time = time.time()
  	if l[i] < target:
    	i += m
  	while fib_list[x] > 0:
      	if l[i] < target:
        	 x -= 1
         	 i += fib_list[x]
      	elif l[i] > target:
        	x -= 1
          	i -= fib_list[x]
      	else:
          	break
  	end_time = time.time()
  	exe_time = end_time - start_time
  	return exe_time
  
  
linear_mean_time=[]
bin_mean_time=[]
fib_mean_time=[]
for i in range(10,1001,10):
  	linear_time=[]
  	bin_time=[]
  	fib_time=[]
  	for t in range(5):
    	random_list=[]
    	for j in range(i):
      		random_list.append(random.randint(0,100000))
    	target = random.randint(0,10000)
    	linear_time.append(linear(random_list,target))
    	random_list.sort()
    	bin_time.append(bin_search(random_list,target))
    	fib_time.append(fib_search(random_list,target))
  linear_mean_time.append(sum(linear_time)/5)
  bin_mean_time.append(sum(bin_time)/5)
  fib_mean_time.append(sum(fib_time)/5)
  
  
import matplotlib.pyplot as plt
x= list(range(10,1001,10))

# 繪製線性圖
plt.plot(x,linear_mean_time, label='linear')
plt.plot(x,bin_mean_time, label='binary')
plt.plot(x,fib_mean_time, label='fibonacci')

# 設定圖表標題和軸標籤
plt.title('Line Chart')
plt.xlabel('data size')
plt.ylabel('time')

# 設定圖例
plt.legend()

# 顯示圖表
plt.show()
