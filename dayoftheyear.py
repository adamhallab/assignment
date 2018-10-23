'''
Adam Hallab
netid: aah101
idnumber: 201901200
'''
import sys
month = sys.argv[1]
day = int(sys.argv[2])

number_days = {"jan":31, "feb":28, "mar":30, "may":31, "jun":30, "jul":31, "aug":30, "sep":30, "oct":31, "nov":30, "dec":31}

def day_of_the_year(month,day):
    days = 0
    for i in number_days:
        if i == month:
            break
        else:
            days += number_days[i]
    num = days + day
    return num
print("Day of the Year:", day_of_the_year(month, day))