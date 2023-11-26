def calculate_bmi(height,weight):
    print("Height =  " + str(height))
    print("Weight = " + str(weight))

    bmi = weight/(height*height)

    print("bmi = " + str(bmi))
    if bmi < 18.5:
        print("Under Weight")
        return -1
    elif bmi > 25.0:
        print("Over weight")
<<<<<<< HEAD
        return 0
    else:
        print("Normal Weight")
        return 1
calculate_bmi(weight=57, height=1.73)
=======
        return 1
    else:
        print("Normal Weight")
        return 0
calculate_bmi(weight=57, height=1.73)
>>>>>>> 68d434337bab7c139a984f11f09a8bbffc66434f
