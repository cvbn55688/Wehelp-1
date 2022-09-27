console.log("====================[要求一]====================")
function calculate(min, max, step){
    // 請用你的程式補完這個函式的區塊
    let sum = 0;
    while (true){
        if(min <= max){
            sum += min;
            min += step;
        }else{
            break;
        }
    }
    console.log(sum);
}

calculate(1, 3, 3);
calculate(1, 3, 1); // 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2); // 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2); // 你的程式要能夠計算 -1+1，最後印出 0
    

console.log("====================[要求二]====================")
function avg(data){
    // 請用你的程式補完這個函式的區塊
    n = 0;
    sum = 0;
    for (let i = 0 ; i < (data["employees"]).length; i++){
        if (data["employees"][i]["manager"] == false){
            sum +=  data["employees"][i]["salary"];
            n += 1;
        }
    }
    console.log("非manager的員工有" + n + "位, 薪水總和為" + sum + "元, 平均為" + sum/n + "元")
}    

avg({
    "employees":[
    {
    "name":"John",
    "salary":30000,
    "manager":false
    },
    {
    "name":"Bob",
    "salary":60000,
    "manager":true
    },
    {
    "name":"Jenny",
    "salary":50000,
    "manager":false
    },
    {
    "name":"Tony",
    "salary":40000,
    "manager":false
    }
    ]
}); // 呼叫 avg 函式


console.log("====================[要求三]====================")
function func(a){
    // 請用你的程式補完這個函式的區塊
    function inner_func(b, c){
        console.log(a + (b * c));
    }
    return inner_func;
}

func(2)(3, 4); // 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5); // 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9); // 你補完的函式能印出 -3+(2*9) 的結果 15
// 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果


console.log("====================[要求四]====================")
function maxProduct(nums){
    // 請用你的程式補完這個函式的區塊
    let max = nums[0] * nums[1];
    
    for (let i = 0; i < nums.length; i++){
        for (let j = 0; j < nums.length; j++){
            if ((nums[i] * nums[j]) > max && i != j){
                max = nums[i] * nums[j];
            }
        }
    }
    console.log(max);
}

maxProduct([5, 20, 2, 6]); // 得到 120
maxProduct([10, -20, 0, 3]); // 得到 30
maxProduct([10, -20, 0, -3]); // 得到 60
maxProduct([-1, 2]); // 得到 -2
maxProduct([-1, 0, 2]); // 得到 0 或 -0
maxProduct([5, -1, -2, 0]); // 得到 2
maxProduct([-5, -2]); // 得到 10
    

console.log("====================[要求五]====================")
function twoSum(nums, target){
    // your code here
    for (let i = 0; i < nums.length; i++){
        for (let j = i; j < nums.length; j++){
            if (i != j && nums[i] + nums[j] == target){
                lis = [i, j];
                return `[${lis}] because nums[${i}] + nums[${j}] is ${target}`
            }
        }
    }
}

let result=twoSum([2, 11, 7, 15], 9);
console.log(result); // show [0, 2] because nums[0]+nums[2] is 9
    

console.log("====================[要求六]====================")
function maxZeros(nums){
    // 請用你的程式補完這個函式的區塊
    nums.push(1)
    let total = 0
    let cont = 0
    nums.forEach(i => {
        if (i == 0){
            cont += 1;
        }else{
            if (cont > total){
                total = cont;
                cont = 0;
            }
        }
    });
    console.log(total)
}

maxZeros([0, 1, 0, 0]); // 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]); // 得到 4
maxZeros([1, 1, 1, 1, 1]); // 得到 0
maxZeros([0, 0, 0, 1, 1]); // 得到 3
