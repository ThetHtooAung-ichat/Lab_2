def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5,67,32)")

def get_user_input():
    print("get_user_input")
    inputstr = input()
    print("Raw input= "+inputstr)
    splitlist = inputstr.split(",")
    print("After splitting= ",splitlist)
    floatlist = []
    for x in splitlist:
        floatnum = float(x)
        floatlist.append(floatnum)
    print("Float list = ", floatlist)
    return floatlist

def cal_average(input_list):
    print("calc_average")

def find_min_max(input_lsit):
    print("find_min_max")

def sort_temperature(input_list):
    print("sort_temperature")

def calc_median_temperature(input_list):
    print("calc_median_temperature")


def main():
    print("ET0735 (DevOps for AIOT) - Lab 2 - intro to python")
    display_main_menu()
    floatlist = get_user_input()


if __name__ == "__main__":
    main()