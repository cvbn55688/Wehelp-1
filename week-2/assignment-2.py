print("="*30 + " [要求一] " + "="*30)


def calculate(min, max, step):
    # 請用你的程式補完這個函式的區塊
    sum = 0
    while True:
        if min <= max:
            sum += min
            min += step
        else:
            break
    print(sum)


calculate(1, 3, 1)  # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2)  # 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2)  # 你的程式要能夠計算 -1+1，最後印出 0


print("="*30 + " [要求二] " + "="*30)


def avg(data):
    # 請用你的程式補完這個函式的區塊
    n = 0
    sum = 0
    # print(data["employees"][1]["manager"])
    # print(len(data["employees"]))
    for i in range(len(data["employees"])):
        if data["employees"][i]["manager"] == False:
            sum += data["employees"][i]["salary"]
            n += 1
    print(f"非manager的員工有[{n}]位, 薪水總和為[{sum}]元, 平均為[{sum/n}]元")


avg({
    "employees": [
        {
            "name": "John",
            "salary": 30000,
            "manager": False
        },
        {
            "name": "Bob",
            "salary": 60000,
            "manager": True
        },
        {
            "name": "Jenny",
            "salary": 50000,
            "manager": False
        },
        {
            "name": "Tony",
            "salary": 40000,
            "manager": False
        }
    ]
})  # 呼叫 avg 函式


print("="*30 + " [要求三] " + "="*30)


def func(a):
    # 請用你的程式補完這個函式的區塊
    def inner_func(b, c):
        print(a + (b * c))
    return inner_func


func(2)(3, 4)  # 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5)  # 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9)  # 你補完的函式能印出 -3+(2*9) 的結果 15
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果


print("="*30 + " [要求四] " + "="*30)


def maxProduct(nums):
    # 請用你的程式補完這個函式的區塊
    max = nums[0] * nums[1]

    for i in nums:
        for j in nums:
            if (i * j) > max and i != j:
                max = i * j
    print(max)


maxProduct([5, 20, 2, 6])  # 得到 120
maxProduct([10, -20, 0, 3])  # 得到 30
maxProduct([10, -20, 0, -3])  # 得到 60
maxProduct([-1, 2])  # 得到 -2
maxProduct([-1, 0, 2])  # 得到 0
maxProduct([5, -1, -2, 0])  # 得到 2
maxProduct([-5, -2])  # 得到 10


print("="*30 + " [要求五] " + "="*30)


def twoSum(nums, target):
    # your code here
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if i != j and nums[i] + nums[j] == target:
                lis = [i, j]
                return f"{lis} because nums[{i}] + nums[{j}] is {target}"


result = twoSum([2, 11, 7, 15], 9)
print(result)  # show [0, 2] because nums[0]+nums[2] is 9


print("="*30 + " [要求六] " + "="*30)


def maxZeros(nums):
    # 請用你的程式補完這個函式的區塊
    nums.append(1)
    total = 0
    cont = 0
    for i in nums:
        if i == 0:
            cont += 1
        else:
            if cont > total:
                total = cont
                cont = 0
    print(total)


maxZeros([0, 1, 0, 0])  # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])  # 得到 4
maxZeros([1, 1, 1, 1, 1])  # 得到 0
maxZeros([0, 0, 0, 1, 1])  # 得到 3
