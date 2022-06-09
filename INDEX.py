print("\n" * 5)

import datetime
import os

DRINKS_MENU = []
LIST_SERVICES = []
LIST_FOODS = []

list_item_price = [0] * 100

var_discount_1 = 200
var_discount_2 = 1000
var_discount_3 = 5000
var_discount_1_rate = 0.05
var_discount_2_rate = 0.10
var_discount_3_rate = 0.15

navigator_symbol = "/"
if os.name == "nt":
    navigator_symbol = "\\"


def def_default():
    global LIST_SERVICES, LIST_FOODS, DRINKS_MENU, list_item_price, list_item_order
    list_item_order = [0] * 100
def_default()



def def_main():
    while True:
        print("*" * 28 + "FOODEMY" + "*" * 24 + "\n")
        print("*" * 31 + "MAIN MENU" + "*" * 32 + "\n"
              "\t(0) ORDER\n"
              "\t(R) REPORT\n"
              "\t(P) PAYMENT\n"
              "\t(E) EXIT\n" 
              "_" * 72)


        input_1 = str(input("Please select your operation: ")).upper()
        if (len(input_1) == 1):
            if (input_1 == 'O'):
                print("\n" * 10)
                def_order_menu()
                break
            elif (input_1 == 'R'):
                print("\n" * 10)
                def_report()
                break
            elif (input_1 == 'P'):
                print("\n" * 10)
                def_payment()
                break
            elif (input_1 == 'E'):
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                break
            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")
        else:
            print("\n" * 10 + "ERROR: Invalid Input(" + str(input_1) + "). Try again!")

def def_order_menu():
    while True:
        print("*" * 31 + "ORDER PAGE" + "*" + 31 + "\n"
          "\t(F) FOOD AND DRINKS\n"
          "\t(O) OTHER SERVICES\n"
          "\t(M) MAIN MENU\n"
          "\t(E) EXIT\n" +
          "_" * 72)

        input_1 = str(input("Please Select Your Operation: ")).upper()
        if len(input_1) == 1:
            if (input_1 == 'F'):
               print("\n" * 10)
               def_food_drink_order()
               break
            elif (input_1 == '0'):
               print("\n" * 10)
               def_other_services()
               break
            elif (input == 'M'):
               print("\n" * 10)
               def_main()
               break
            elif (input_1 == 'E'):
               print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
               break
            else:
               print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")
        else:
         print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

def def_full_file_reader():
    file_foods = open('LIST_FOODS.fsd', 'r')
    for i in file_foods:
        LIST_FOODS.append(str(i.strip()))
    file_foods.close()

    file_drinks = open('DRINKS_MENU.fsd', 'r')
    for i in file_drinks:
        DRINKS_MENU.append(str(i.strip()))
    file_foods.close()

    file_services = open('LIST_SERVICES.fsd', 'r')
    for i in file_services:
        LIST_SERVICES.append(str(i.strip()))
    file_services.close()

    i = 0
    while i <= (len(LIST_FOODS)-1):
        if '$' in LIST_FOODS[i]:
            LIST_FOODS[i] = str(LIST_FOODS[i][:LIST_FOODS[i].index('$') - 1]) + ' ' * (20 - (LIST_FOODS[i].index('$') - 1)) + str(LIST_FOODS[i][LIST_FOODS[i].index('$'):])
        i += 1
    i = 0
    while i <= (len(DRINKS_MENU) - 1):
        if '$' in DRINKS_MENU[i]:
            DRINKS_MENU[i] = str(DRINKS_MENU[i][:DRINKS_MENU[i].index('$') - 1] + ' ' * (20 - (DRINKS_MENU[i].index('$') - 1)) + str(DRINKS_MENU[i][DRINKS_MENU[i].index('$'):]))
        i += 1

    i = 0
    while i <= (len(LIST_SERVICES) - 1):
        if '$' in LIST_SERVICES[i]:
            LIST_SERVICES[i] = str(LIST_SERVICES[i][:LIST_SERVICES[i].index('$') - 1] + ' ' * (20 - (LIST_SERVICES[i].index('$') - 1)) + str(LIST_SERVICES[i][LIST_SERVICES[i].index('$' ):]))
        i += 1
def_full_file_reader()

def def_file_sorter():
    global LIST_SERVICES, LIST_FOODS, DRINKS_MENU
    LIST_FOODS = sorted(LIST_FOODS)
    LIST_SERVICES = sorted(LIST_SERVICES)
    DRINKS_MENU = sorted(DRINKS_MENU)

    i = 0
    while i < len(LIST_FOODS):
        list_item_price[i] = float(LIST_FOODS[i][int(LIST_FOODS[i].index("$") + 2):])
        i += 1


    i = 0
    while i < len(DRINKS_MENU):
        list_item_price[40 + i] = float(DRINKS_MENU[i][int(DRINKS_MENU[i].index("$") + 2):])

    i = 0
    while i < len(LIST_SERVICES):
        list_item_price[80 + i] = float(LIST_SERVICES[i][int(LIST_SERVICES[i].index("$") + 2):])
        i += 1

def_file_sorter()

def def_food_drink_order():
    while True:
        print("*" * 26 + "ORDER FOOD AND DRINKS" + "*" * 26)
        print(" |NO| |FOOD NAME|          |PRICE|    |NO| |DRINK NAME|      |PRICE|")

        i = 0
        while i < len(LIST_FOODS) or i< len(DRINKS_MENU):
            var_space = 1
            if i <= 8:
                var_space = 2

            if i < len(LIST_FOODS):
                food = " (" + str(i + 1) + ")" + " " * var_space + str(LIST_FOODS[i]) + "  | "
            else:
                food = " " * 36 + "| "
            if i < len(DRINKS_MENU):
                drink = "(" + str(41 + i) + ")" + " " + str(DRINKS_MENU[i])
            else:
                drink = ""
            print(food, drink)
            i += 1

        print("\n (M) MAIN MENU                     (P) PAYMENT             (E) EXIT\n" + "_" * 72)

        input_1 = input("Please select your operation: ").upper()
        if (input_1 == 'M'):
            print("\n" * 10)
            def_main()
            break
        if (input_1 == 'E'):
            print("\n" * 32 + "THANK YOU" + "*" * 31 + "\n")
            break
        if (input_1 == 'P'):
            print("\n" * 10)
            def_payment()
            break
        try:
            int(input_1)
            if((int(input_1) <= len(LIST_FOODS) and int(input_1) > 0) or int(input_1) <= len(DRINKS_MENU) + 40 and int(input_1) > 40):
                try:
                    print("\n" + "_" * 72 + "\n" + str(LIST_FOODS[int(input_1) - 1]))
                except:
                     pass
                try:
                    print("\n" + "_" * 72 + "\n" + str(DRINKS_MENU[int(input_1) - 41]))
                except:
                    pass

                input_2 = input("How many you want to order?: ").upper()
                if int(input_2) > 0:
                    list_item_order[int(input_1) - 1] += int(input_2)
                    print("\n" * 10)
                    print("Successfully Ordered!")
                    def_food_drink_order()
                    break
                else:
                  print("\n" * 10 + "ERROR: Invalid Input (" + str(input_2) + "). Try again!")
        except:
               print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

def def_other_services():
    while True:
        print("*" * 29 + "OTHER SERVICES" + "*" * 29)
        print(" |NO|  |SERVICE NAME|   |PRICE|")

        i = 0
        while i < len(LIST_SERVICES):
            print(" (" + str(81 + i) + ")" + " " + str(LIST_SERVICES[i]))

            i += 1

            print("\n (M) MAIN MENU         (P) PAYMENT          (E) EXIT\n" + "_" * 72)

            input_1 = input("Please Select Your Operation: ").upper()
            if (input_1 == 'M'):
                print("\n" * 10)
                def_main()
                break
            if (input_1 == 'E'):
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                break
            if (input_1 == 'P'):
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                def_payment()
                break
            try:
                input(input_1)
                if (int(input_1) > 80) and int(int(input_1) < 100):
                    print("\n" * 10)
                    print("Successfully Ordered: " + str(LIST_SERVICES[int(input_1) - 81]))
                    list_item_order[int(input_1) - 1] = 1
                    def_other_services()
                    break
                else:
                    print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try Again!")
            except:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

def def_report():
    while True:
        print("*" * 33 + "REPORT" + 33 + "\n")
        file_report = open('files' + navigator_symbol+'report.fsd', 'r').read()
        print(file_report)
        print("\n(M) MAIN MENU        (E) EXIT" + "_" * 72)
        input_1 = str(input("Select operation: ")).upper()
        if (input_1 == 'M'):
            print("\n" * 10)
            def_main()
            break
        elif (input_1 == 'E'):
            print("*" * 32 + "THANK YOU" + 31 + "\n")
            break
        else:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

def def_payment():
    while True:
        print("*" * 32 + "PAYMENT" + "*" * 33 + "\n")
        total_price = 0

        report_new = "\n\n\n" + " " * 17 + "*" * 35 + "\n" + " " * 17 + "DATE: " + str(datetime.datetime.now())[:19] + "\n" + " " * 17 + "-" * 35
        i = 0
        while i < len(list_item_order):
            if(list_item_order[i] != 0):
                if (i >= 0) and (i < 40):
                    report_new += "\n" + " " * 17 + str(LIST_FOODS[i]) + "  *  " + str(list_item_order[i])
                    print(" " * 17 + str(LIST_FOODS[i]) + "  *  " + str(list_item_order[i]))
                    total_price += list_item_price[i] * list_item_order[i]
                if (i >= 40) and (i < 80):
                    report_new += "\n" + " " * 17 + str(DRINKS_MENU[i - 40]) + "  *  " + str(list_item_order[i])
                    total_price += list_item_price[i] * list_item_order[i]
                if (i >= 80) and (i < 100):
                    report_new += "\n" + " " * 17 + str(LIST_SERVICES[i - 80])
                    print(" " * 17 + str(LIST_SERVICES[i - 80]))
                    total_price += list_item_price[i] * list_item_order[i]
                    i += 1
            else:
                i += 1


        if total_price > var_discount_3:
            total_price -= total_price * var_discount_3_rate
            report_new += "\n" + " " * 17 + "-" * 35 + "\n" \
               "" + " " * 17 + "DISCOUNT RATES:       % " + str(var_discount_3_rate * 100) + "\n" \
               "" + " " * 17 + "DISCOUNT AMOUNTS:    $ " + str(round(total_price * var_discount_3_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n" \
               "" + " " * 17 + "TOTAL PRICES:         $ " + str(round(total_price, 2)) + "\n" + " " * 17 + "*" * 35
            print(" " * 17 + "-" * 35 + "\n"
               "" + " " * 17 + "DISCOUNT RATES:       %" + str(var_discount_3_rate * 100) + "\n"
               "" + " " * 17 + "DISCOUNT AMOUNT:      $ " + str(round(total_price * var_discount_3_rate, 2)) + "\n" + " " * 17 + " " * 35 + "\n"
               "" + " " * 17 + "TOTAL PRICES:         $ " + str(round(total_price,2)))
        elif total_price > var_discount_2:
            total_price -= total_price * var_discount_2_rate
            report_new += "\n" + " " * 17 + "-" * 35 + "\n" \
                "" + " " * 17 + "DISCOUNT RATES:      % " + str(var_discount_2_rate * 100) + "\n" \
                "" + " " * 17 + "DISCOUNT AMOUNTS:   $ " + str(round(total_price * var_discount_2_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n" \
                "" + " " * 17 + "TOTAL PRICES:       $ " + str(round(total_price, 2)) + "\n" + " " * 17 + "*" * 35
            print(" " * 17 + "-" * 35 + "\n"
                "" + " " * 17 + "DISCOUNT RATES:      % " + str(var_discount_2_rate * 100) + "\n"
                "" + " " * 17 + "DISCOUNT AMOUNTS:   $ " + str(round(total_price * var_discount_2_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n"
                "" + " " * 17 + "TOTAL PRICES:       $ " + str(round(total_price, 2)))
        elif total_price > var_discount_1:
             total_price -= total_price * var_discount_1_rate
             report_new += "\n" + " " * 17 + "-" * 35 + "\n" \
                "" + " " * 17 + "DISCOUNT RATES:      % " + str(var_discount_1_rate * 100) + "\n" \
                "" + " " * 17 + "DISCOUNT AMOUNTS:   $ " + str(round(total_price * var_discount_1_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n" \
                "" + " " * 17 + "TOTAL PRICES:       $ " + str(round(total_price, 2)) + "\n" + " " * 17 + "*" * 35
             print(" " * 17 + "-" * 35 + "\n"
                "" + " " * 17 + "DISCOUNT RATES:      % " + str(var_discount_1_rate * 100) + "\n"
                "" + " " * 17 + "DISCOUNT AMOUNTS:   $ " + str(round(total_price * var_discount_1_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n"
                "" + " " * 17 + "TOTAL PRICES:       $ " + str(round(total_price, 2)))
        else:
             report_new += "\n" + " " * 17 + "-" * 35 + "\n" + " " * 17 + "TOTAL PRICES:       $ " + str(round(total_price, 2)) + "\n" + " " * 17 + "*" * 35
             print(" " * 17 + "_" * 35 + "\n" + " " * 17 + "TOTAL PRICES:       $ " + str(round(total_price, 2)))

        print("\n (P) PAY           (M) MAIN MENU           (R) REPORT          (E) EXIT\n" + "_" * 72)
        input_1 = str(input("Please Select Your Operation: ")).upper()
        if (input_1 == 'P'):
            print("\n" * 10)
            print("Successfully Paid!")
            file_report = open('files' + navigator_symbol + 'report.fsd', 'a')
            file_report.write(report_new)
            file_report.close()
            def_default()
        elif (input_1 == 'M'):
             print("\n" * 10)
             def_main()
             break
        elif (input_1 == 'R'):
             print("\n" * 10)
             def_report()
             break
        elif ('E' in input_1) or ('e' in input_1):
             print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
             break
        else:
             print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")
def_main()

