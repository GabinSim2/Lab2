def calc_average_temperature():
    Temperature = get_values()
    print("Average temperature:", sum(Temperature)/len(Temperature))
def calc_min_max_temperature():
    Temperature = get_values()
    min_temp = min(Temperature)
    max_temp = max(Temperature)
    print("The min Temperature is ", min_temp, "\nThe max Temperature is ", max_temp)
def calc_median_temperature():
    Temperature = get_values()
    Temperature.sort()
    length_of_Temp = len(Temperature)
    if length_of_Temp % 2 == 1:
        median = Temperature[length_of_Temp//2]
    else:
        median = (Temperature[length_of_Temp//2 - 1] + Temperature[length_of_Temp// 2])/2

    print("The median is ", median)