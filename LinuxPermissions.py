# Pregunta 3
# The permissions of a file in a Linux system are split into three sets of three 
# permissions: read, write, and execute for the owner, group, and others. 
# Each of the three values can be expressed as an octal number summing each permission,
#  with 4 corresponding to read, 2 to write, and 1 to execute. Or it can be written 
# with a string using the letters r, w, and x or - when the permission is not granted.
# For example: 
# 640 is read/write for the owner, read for the group, and no permissions for the others;
#  converted to a string, it would be: "rw-r-----"
# 755 is read/write/execute for the owner, and read/execute for group and others; 
# converted to a string, it would be: "rwxr-xr-x"


def octal_to_string(octal):

    data =[(4,"r"),(2,"w"),(1,"x")]
    result =""

    #We obtain each octal number so we need to use a range which say to us the long of the octal number

    for i in [int (n) for n in str(octal)]:
        # we go over the three possible numbers and see if the octal digit is bigger than
        # the reference numbers we have.If it does, we find the necessary output.
        #At the same time , we will take out the first number and see if there is a number more or
        #we finished

        for number,type in data:
            if i >= number:
                result += type
                i -= number
            else:
                result += "-"

    return result


print (octal_to_string("755"))