import time


def getCharge(drinkNo, foodNo):
    drinkCharge = 0.0
    foodCharge = 0.0
    if drinkNo == 1:
        drinkCharge = 3.0
    elif drinkNo == 2:
        drinkCharge = 4.5
    elif drinkNo == 3:
        drinkCharge = 4.0
    if foodNo == 1:
        foodCharge = 1.0
    elif foodNo == 2:
        foodCharge = 2.5
    elif foodNo == 3:
        foodCharge = 2.0
    elif foodNo == 4:
        foodCharge = 1.5
    return drinkCharge + foodCharge


DrinkMenu = {1: "豆浆", 2: "果汁", 3: "牛奶"}
FoodMenu = {1: "馒头", 2: "包子", 3: "鸡蛋", 4: "油条"}
OrderList = []


def orderMenu():
    print("\n----欢迎点餐----")
    print("我们提供的饮品：")
    for drink in DrinkMenu:
        print(str(drink)+": "+DrinkMenu[drink])
    drinkNo = int(input("请输入序号选择您需要的饮品（1~3）："))
    while drinkNo > 3:
        drinkNo = int(input("输入错误，请输入序号选择您需要的饮品（1~3）"))
    print("您选择了：" + DrinkMenu[drinkNo]+"\n")
    print("我们提供的食物：")
    for food in FoodMenu:
        print(str(food)+": "+FoodMenu[food])
    foodNo = int(input("请输入序号选择您需要的食物（1~4）："))
    while foodNo > 4:
        foodNo = int(input("输入错误，请输入序号选择您需要的食物（1~3）"))
    print("您选择了：" + FoodMenu[foodNo]+"\n")
    totalPrice = getCharge(drinkNo, foodNo)
    print("将马上为您奉上%s和%s，共消费%.2f元。" %
          (DrinkMenu[drinkNo], FoodMenu[foodNo], totalPrice))
    OrderDate = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    OrderTime = time.strftime('%H:%M:%S', time.localtime(time.time()))
    OrderList.append(
        [OrderDate, OrderTime, DrinkMenu[drinkNo], FoodMenu[foodNo], totalPrice])


def printReport(OrderList):
    totalPrice = 0
    print("\n------ 统计报表 ------")
    print("点餐日期 \t点餐时间 \t饮料 \t主食 \t花费(元)")
    for order in OrderList:
        totalPrice += order[4]
        print(order[0]+"\t"+order[1]+"\t%s\t%s\t%.2f" %
              (order[2], order[3], order[4]))
        print("\n累计收入 %.2f 元。" % totalPrice)


def exportReport(OrderList):
    dataFile = open("./AllReport.txt", "w")
    # for order in OrderList:
    #     dataFile.write(order[0]+","+order[1]+",%s,%s,%.2f 元\n" %
    #                    (order[2], order[3], order[4]))
    dataFile.write(str(1))
    dataFile.close()
    print("---- 成功导出报表 ----")


while(True):
    print("\n------ 欢迎使用点餐系统 ------")
    print("本软件提供如下功能：\n 1. 点餐\n 2. 打印报表\n 3. 存储报表\n 4. 退出系统")
    choice = int(input("请输入数字选择一项功能："))
    if choice == 1:
        orderMenu()
    elif choice == 2:
        printReport(OrderList)
    elif choice == 3:
        exportReport(OrderList)
    elif choice == 4:
        exit(0)
    else:
        print("请输入正确的序号(1~4)")
