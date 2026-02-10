
import deserialize
import operations

work = True
transaction_list  = deserialize.transaction_list

while work:
    print("Виберіть дію з рахунком: ")
    print("=======================")
    print("1. Внести витрати")
    print("2. Внести надходження")
    print("3. Глянути історію надходжень")
    print("4. Вивести загальний баланс")
    print("5. Вихід")
    print("=======================")

    selected_menu = int(input())
    if selected_menu == 1:
        operations.add_expense()
    elif selected_menu == 2:
        operations.add_income()
    elif selected_menu == 3:
        operations.print_transactions()
    elif selected_menu == 4:
        operations.count_balance()
    elif selected_menu == 5:
        operations.save_data_to_file()
        work = False

