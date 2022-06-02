# 如何在列表、字典、集合中根据条件筛选数据

# 1.过滤 [3, -9, 0, 11, 2, -2]中的负数

# 最low的方法，也是底层
data = [3, -9, 0, 11, 2, -2]
res = []
for i in data:
    if i >= 0:
        res.append(i)

print("直接使用循环", res)
# a = [randint(-10, 10) for _ in range(10)]

a = [1, -8, -9, 1, -4, -6, -5, 4, 0, 7]

# 方法1.使用列表生成式实现过滤
filtered_a = [x for x in a if x >= 0]
print("使用列表生成式", filtered_a)

# 方法2.使用内置filter函数

g = filter(lambda num: num >= 0, a)  # 返回生成器对象
print("filter的返回结果是生成器对象", g)
new_a = list(g)
print(new_a)

# scores = {f"stu{i}":randint(50,100) for i in range(5)}
scores = {'stu0': 100,
          'stu1': 92,
          'stu2': 74,
          'stu3': 52,
          'stu4': 93}
# 找到分数大于90的同学

great_stu = {id: score for id, score in scores.items() if score >= 90}
print("分数大于90的", great_stu)

g = filter(lambda item: item[1] <= 80, scores.items())
print(g)
# print(list(g))
print("成绩小于80的", dict(g))

# s = {randint(0,10) for _ in range(10)}
s = {2, 3, 4, 6, 7, 8, 9}
# 找到集合s 中能被3整除的数字
filtered_s = {x for x in s if x % 3 == 0}
print(filtered_s)
print("集合中能被3整除的数字", filtered_s)
