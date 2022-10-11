es_w = 50
es_c = 18

la_w = 200
la_m = 150
la_c = 24

ca_w = 250
ca_m = 100
ca_c = 24

water_content = 300
milk_content = 200
coffee_content = 100
money_content = 0

cost_espresso = 1.5
cost_latte = 2.5
cost_cappuccino = 3

switch = True

while switch == True:
    choice = input("What would you like to have ? (espresso/latte/cappuccino): ").lower()

    if choice == "report":
        print(f"Water : {water_content}ml")
        print(f"milk : {milk_content}ml")
        print(f"coffee : {coffee_content}g")
        print(f"money : {money_content}")

    elif choice == "off":
        switch = False

    elif choice == "espresso":
        if water_content > es_w and coffee_content > es_c:
            print("Please insert coins. ")
            m1 = float(input("how many quarters?: "))
            m2 = float(input("how many dimes?: "))
            m3 = float(input("how many nickels?: "))
            m4 = float(input("how many pennys?: "))
            total_money = ((m1*0.25)+(m2*0.1)+(m3*0.05)+(m4*0.01))
            if total_money > cost_espresso:
                refund_money = total_money-cost_espresso
                water_content -= 50
                coffee_content -= 18
                money_content += 1.5
                print(f"Here is ${refund_money} in change")
                print("Here is your espresso. Enjoy!!")
            else:
                print("That's not sufficient money. Money refunded")
        else:
            print("Sorry not enough ingrediants")

    elif choice == "latte":
        if water_content > la_w and coffee_content > la_c  and milk_content >  la_m:
            print("Plesae insert coins. ")
            m1 = float(input("how many quarters?: "))
            m2 = float(input("how many dimes?: "))
            m3 = float(input("how many nickels?: "))
            m4 = float(input("how many pennys?: "))
            total_money = ((m1*0.25)+(m2*0.1)+(m3*0.05)+(m4*0.01))
            if total_money < cost_latte:
                print("That's not sufficient money. Money refunded")
            elif total_money > cost_latte:
                refund_money = total_money-cost_latte
                water_content -= 200
                milk_content -= 150
                coffee_content -= 24
                money_content += 2.5
                print(f"Here is ${refund_money} in change")
                print("Here is your latte. Enjoy!!")
        else:
            print("Sorry not enough ingrediants")

    elif choice == "cappuccino":
        if water_content > ca_w and coffee_content > ca_c  and milk_content >  ca_m:
            print("Plesae insert coins. ")
            m1 = float(input("how many quarters?: "))
            m2 = float(input("how many dimes?: "))
            m3 = float(input("how many nickels?: "))
            m4 = float(input("how many pennys?: "))
            total_money = ((m1*0.25)+(m2*0.1)+(m3*0.05)+(m4*0.01))
            if total_money < cost_cappuccino:
                print("That's not sufficient money. Money refunded")
            elif total_money > cost_cappuccino:
                refund_money = total_money-cost_cappuccino
                water_content -= 250
                milk_content -= 100
                coffee_content -= 24
                money_content += 3.0
                print(f"Here is ${refund_money} in change")
                print("Here is your cappuccino. Enjoy!!")
        else:
            print("Sorry not enough ingrediants")





