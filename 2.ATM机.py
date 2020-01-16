

def print_menu():
    print("_"*20)
    print("  ATM机   ")
    print("1:查询余额")
    print("2:存款")
    print("3:取款")
    print("4:退出")
    print("_" * 20)


def search_info(money):
    print(f"卡上余额为:%.4f" %money)


def save_money(money):
    smoney = float(input("请输入要存入的金额:"))
    money += smoney
    print("存款成功!")
    return money


def draw_money(money):
    smoney = float(input("请输入要取出的金额:"))
    if money <= smoney:
        print("卡上余额不足!")
    else:
        money -= smoney
        print("取款成功!")
        return money


def main():
    global money
    money = 0
    while True:
        print_menu()
        num = input("请输入操作:")
        if num == "1":
            search_info(money)
        elif num == "2":
            money = save_money(money)
        elif num == "3":
            money = draw_money(money)
        elif num =="4":
            break
        else:
            print("输入有误,请重新输入...")


main()

