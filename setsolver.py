from itertools import combinations
import time 
import re
import requests

startTime = time.time()

# Downloads website data
url = "http://www.setgame.com/set/puzzle"
downloaded_obj = requests.get(url)

with open("puzzle", "wb") as file:
    file.write(downloaded_obj.content)

#Reads data from file ^
with open('puzzle') as intxt:
    data = intxt.read()

#generate all picture filename
picture_list = []
x = 1
for g in range(81):
    test_file_name = None
    x= str(x)
    test_file_name = " src=\"/sites/all/modules/setgame_set/assets/images/new/" + x + ".png\""
    picture_list.append(test_file_name)
    x = int(x)
    x += 1

'''
This is how how the image files are found

class="A1" = first shape
class="A2" = second shape
etc.
'''

#Function to find the file name from document
def find(g):
    x = re.findall(g, data)
    return x

#Appends file which corresponds to the the class
final = []
def search(num):
    x = 0
    for a in range(81):
        tmp = num + picture_list[x]
        test_file = find(tmp)
        if len(test_file) > 0:
            final_append = test_file[0].replace("[", "")
            final.append(final_append)
            break
        x += 1

#Puts the shape names into the searching fn
search("class=\"A1\"")
search("class=\"A2\"")
search("class=\"A3\"")
search("class=\"A4\"")
search("class=\"A5\"")
search("class=\"A6\"")
search("class=\"A7\"")
search("class=\"A8\"")
search("class=\"A9\"")
search("class=\"A10\"")
search("class=\"A11\"")
search("class=\"A12\"")

#Sorts
sorted(final)

#Extracts number from file
def filename_to_number(filename):
    tmp = filename
    return_var = tmp[65:]
    return_var = return_var.replace(".", "")
    return_var = return_var.replace("png", "")
    return_var = return_var.replace("\"", "")
    return_var = return_var.replace("/", "")
    return return_var

tmps1 = filename_to_number(final[0])
tmps2 = filename_to_number(final[1])
tmps3 = filename_to_number(final[2])
tmps4 = filename_to_number(final[3])
tmps5 = filename_to_number(final[4])
tmps6 = filename_to_number(final[5])
tmps7 = filename_to_number(final[6])
tmps8 = filename_to_number(final[7])
tmps9 = filename_to_number(final[8])
tmps10 = filename_to_number(final[9])
tmps11 = filename_to_number(final[10])
tmps12 = filename_to_number(final[11])

#Creates 4 objects associated w/ each object - color, opacity, number, shape
class info_gather:

    '''
    color:
        g = green
        p = purple
        r = red

    opacity:
        100 = solid
        50 = striped
        0 = open

    num:
        1 = 1 of shape
        2 = 2 of shape
        3 = 3 of shape

    shape: 
        diamond
        squiggle
        oval
    '''

    #Turns args into vars
    def __init__(self, color, opacity, num, shape):
        self.color = color
        self.opacity = opacity
        self.num = num
        self.shape = shape
    
    #Unused 
    def printtest(self):
        print(self.color, self.opacity, self.num, self.shape)


# set_list = []

#Used to compare 3 classes
def compare(name1, color1, opacity1, num1, shape1, name2, color2, opacity2, num2, shape2, name3, color3, opacity3, num3, shape3):

    '''
        1 = all different
        2 = all same
        3 = mixed
    '''
    
    #Used to find what properties the class parameters have
    if color1 != color2 and color2 != color3 and color1 != color3:
        # print('color all diff')
        color = 1
    elif color1 == color2 and color2 == color3 and color1 == color3:
        # print('color all same')
        color = 2
    else:
        # print('color mixed')
        color = 3

    if opacity1 != opacity2 and opacity2 != opacity3 and opacity1 != opacity3:
        # print('opac all diff')
        opac = 1
    elif opacity1 == opacity2 and opacity2 == opacity3 and opacity1 == opacity3:
        # print('opac all same')
        opac = 2
    else:
        # print('opac mixed')
        opac = 3

    if num1 != num2 and num2 != num3 and num1 != num3:
        # print('num all diff')
        number = 1
    elif num1 == num2 and num2 == num3 and num1 == num3:
        # print('num all same')
        number = 2
    else:
        # print('num mixed')
        number = 3

    if shape1 != shape2 and shape2 != shape3 and shape1 != shape3:
        # print('shape all diff')
        shape = 1
    elif shape1 == shape2 and shape2 == shape3 and shape1 == shape3:
        # print('shape all same')
        shape = 2
    else:
        # print('shape mixed')
        shape = 3


    #Compares the values created above
    if color == 1 and opac == 1 and number == 1 and shape == 1:
        print('set ', name1, ' ', name2, ' ', name3)


    if color == 2 and opac == 1 and number == 1 and shape == 1:
        print('set ', name1, ' ', name2, ' ', name3)

    if color == 1 and opac == 2 and number == 1 and shape == 1:
        print('set ', name1, ' ', name2, ' ', name3)


    if color == 1 and opac == 1 and number == 2 and shape == 1:
        print('set ', name1, ' ', name2, ' ', name3)


    if color == 1 and opac == 1 and number == 1 and shape == 2:
        print('set ', name1, ' ', name2, ' ', name3)



    if color == 2 and opac == 2 and number == 1 and shape == 1:
        print('set ', name1, ' ', name2, ' ', name3)


    if color == 2 and opac == 1 and number == 2 and shape == 1:
        print('set ', name1, ' ', name2, ' ', name3)


    if color == 2 and opac == 1 and number == 1 and shape == 2:
        print('set ', name1, ' ', name2, ' ', name3)


    if color == 1 and opac == 2 and number == 2 and shape == 1:
        print('set ', name1, ' ', name2, ' ', name3)


    if color == 1 and opac == 2 and number == 1 and shape == 2:
        print('set ', name1, ' ', name2, ' ', name3)


    if color == 1 and opac == 1 and number == 2 and shape == 2:
        print('set ', name1, ' ', name2, ' ', name3)


    if color == 1 and opac == 2 and number == 2 and shape == 2:
        print('set ', name1, ' ', name2, ' ', name3)

    if color == 2 and opac == 1 and number == 2 and shape == 2:
        print('set ', name1, ' ', name2, ' ', name3)

    if color == 2 and opac == 2 and number == 1 and shape == 2:
        print('set ', name1, ' ', name2, ' ', name3)

    if color == 2 and opac == 2 and number == 2 and shape == 1:
        print('set ', name1, ' ', name2, ' ', name3)


#Assigns the link number to the properties of the corresponding shape
def assignment(number):
    if number == '1':
        return ['r', 100, 1, "squiggle"]
    if number == '2':
        return ['r', 100, 2, 'squiggle']
    if number == '3':
        return ['r', 100, 3, 'squiggle']
    if number == '4':
        return ['p', 100, 1, 'squiggle']
    if number == '5':
        return ['p', 100, 2, "squiggle"]
    if number == '6':
        return ['p', 100, 3, 'squiggle']
    if number == '7':
        return ['g', 100, 1, 'squiggle']
    if number == '8':
        return ['g', 100, 2, 'squiggle']
    if number == '9':
        return ['g', 100, 3, 'squiggle']
    if number == '10':
        return ['r', 100, 1, 'diamond']
    if number == '11':
        return ['r', 100, 2, 'diamond']
    if number == '12':
        return ['r', 100, 3, 'diamond']
    if number == '13':
        return ['p', 100, 1, 'diamond']
    if number == '14':
        return ['p', 100, 2, 'diamond']
    if number == '15':
        return ['p', 100, 3, 'diamond']
    if number == '16':
        return ['g', 100, 1, 'diamond']
    if number == '17':
        return ['g', 100, 2, 'diamond']
    if number == '18':
        return ['g', 100, 3, 'diamond']
    if number == '19':
        return ['r', 100, 1, 'oval']
    if number == '20':
        return ['r', 100, 2, 'oval']
    if number == '21':
        return ['r', 100, 3, 'oval']
    if number == '22':
        return ['p', 100, 1, 'oval']
    if number == '23':
        return ['p', 100, 2, 'oval']
    if number == '24':
        return ['p', 100, 3, 'oval']
    if number == '25':
        return ['g', 100, 1, 'oval']
    if number == '26':
        return ['g', 100, 2, 'oval']
    if number == '27':
        return ['g', 100, 3, 'oval']
    if number == '28':
        return ['r', 50, 1, 'squiggle']
    if number == '29':
        return ['r', 50, 2, 'squiggle']
    if number == '30':
        return ['r', 50, 3, 'squiggle']
    if number == '31':
        return ['p', 50, 1, 'squiggle']
    if number == '32':
        return ['p', 50, 2, 'squiggle']
    if number == '33':
        return ['p', 50, 3, 'squiggle']
    if number == '34':
        return ['g', 50, 1, 'squiggle']
    if number == '35':
        return ['g', 50, 2, 'squiggle']
    if number == '36':
        return ['g', 50, 3, 'squiggle']
    if number == '37':
        return ['r', 50, 1, 'diamond']
    if number == '38':
        return ['r', 50, 2, 'diamond']
    if number == '39':
        return ['r', 50, 3, 'diamond']
    if number == '40':
        return ['p', 50, 1, 'diamond']
    if number == '41':
        return ['p', 50, 2, 'diamond']
    if number == '42':
        return ['p', 50, 3, 'diamond']
    if number == '43':
        return ['g', 50, 1, 'diamond']
    if number == '44':
        return ['g', 50, 2, 'diamond']
    if number == '45':
        return ['g', 50, 3, 'diamond']
    if number == '46':
        return ['r', 50, 1, 'oval']
    if number == '47':
        return ['r', 50, 2, 'oval']
    if number == '48':
        return ['r', 50, 3, 'oval']
    if number == '49':
        return ['p', 50, 1, 'oval']
    if number == '50':
        return ['p', 50, 2, 'oval']
    if number == '51':
        return ['p', 50, 3, 'oval']
    if number == '52':
        return ['g', 50, 1, 'oval']
    if number == '53':
        return ['g', 50, 2, 'oval']
    if number == '54':
        return ['g', 50, 3, 'oval']
    if number == '55':
        return ['r', 0, 1, 'squiggle']
    if number == '56':
        return ['r', 0, 2, 'squiggle']
    if number == '57':
        return ['r', 0, 3, 'squiggle']
    if number == '58':
        return ['p', 0, 1, 'squiggle']
    if number == '59':
        return ['p', 0, 2, 'squiggle']
    if number == '60':
        return ['p', 0, 3, 'squiggle']
    if number == '61':
        return ['g', 0, 1, 'squiggle']
    if number == '62':
        return ['g', 0, 2, 'squiggle']
    if number == '63':
        return ['g', 0, 3, 'squiggle']
    if number == '64':
        return ['r', 0, 1, 'diamond']
    if number == '65':
        return ['r', 0, 2, 'diamond']
    if number == '66':
        return ['r', 0, 3, 'diamond']
    if number == '67':
        return ['p', 0, 1, 'diamond']
    if number == '68':
        return ['p', 0, 2, 'diamond']
    if number == '69':
        return ['p', 0, 3, 'diamond']
    if number == '70':
        return ['g', 0, 1, 'diamond']
    if number == '71':
        return ['g', 0, 2, 'diamond']
    if number == '72':
        return ['g', 0, 3, 'diamond']
    if number == '73':
        return ['r', 0, 1, 'oval']
    if number == '74':
        return ['r', 0, 2, 'oval']
    if number == '75':
        return ['r', 0, 3, 'oval']
    if number == '76':
        return ['p', 0, 1, 'oval']
    if number == '77':
        return ['p', 0, 2, 'oval']
    if number == '78':
        return ['p', 0, 3, 'oval']
    if number == '79':
        return ['g', 0, 1, 'oval']
    if number == '80':
        return ['g', 0, 2, 'oval']
    if number == '81':
        return ['g', 0, 3, 'oval']


    
#Sets up object args for the logic function
s1_arg = assignment(tmps1)
# print(s1_arg)
s1 = info_gather(s1_arg[0], s1_arg[1], s1_arg[2], s1_arg[3])

s2_arg = assignment(tmps2)
# print(s2_arg)
s2 = info_gather(s2_arg[0], s2_arg[1], s2_arg[2], s2_arg[3])

s3_arg = assignment(tmps3)
# print(s3_arg)
s3 = info_gather(s3_arg[0], s3_arg[1], s3_arg[2], s3_arg[3])

s4_arg = assignment(tmps4)
# print(s4_arg)
s4 = info_gather(s4_arg[0], s4_arg[1], s4_arg[2], s4_arg[3])

s5_arg = assignment(tmps5)
# print(s5_arg)
s5 = info_gather(s5_arg[0], s5_arg[1], s5_arg[2], s5_arg[3])

s6_arg = assignment(tmps6)
# print(s6_arg)
s6 = info_gather(s6_arg[0], s6_arg[1], s6_arg[2], s6_arg[3])

s7_arg = assignment(tmps7)
# print(s7_arg)
s7 = info_gather(s7_arg[0], s7_arg[1], s7_arg[2], s7_arg[3])

s8_arg = assignment(tmps8)
# print(s8_arg)
s8 = info_gather(s8_arg[0], s8_arg[1], s8_arg[2], s8_arg[3])

s9_arg = assignment(tmps9)
# print(s9_arg)
s9 = info_gather(s9_arg[0], s9_arg[1], s9_arg[2], s9_arg[3])

s10_arg = assignment(tmps10)
# print(s10_arg)
s10 = info_gather(s10_arg[0], s10_arg[1], s10_arg[2], s10_arg[3])

s11_arg = assignment(tmps11)
# print(s11_arg)
s11 = info_gather(s11_arg[0], s11_arg[1], s11_arg[2], s11_arg[3])

s12_arg = assignment(tmps12)
# print(s12_arg)
s12 = info_gather(s12_arg[0], s12_arg[1], s12_arg[2], s12_arg[3])

s1 = ("s1", s1.color, s1.opacity, s1.num, s1.shape)
s2 = ("s2", s2.color, s2.opacity, s2.num, s2.shape)
s3 = ("s3", s3.color, s3.opacity, s3.num, s3.shape)
s4 = ("s4", s4.color, s4.opacity, s4.num, s4.shape)
s5 = ("s5", s5.color, s5.opacity, s5.num, s5.shape)
s6 = ("s6", s6.color, s6.opacity, s6.num, s6.shape)
s7 = ("s7", s7.color, s7.opacity, s7.num, s7.shape)
s8 = ("s8", s8.color, s8.opacity, s8.num, s8.shape)
s9 = ("s9", s9.color, s9.opacity, s9.num, s9.shape)
s10 = ("s10", s10.color, s10.opacity, s10.num, s10.shape)
s11 = ("s11", s11.color, s11.opacity, s11.num, s11.shape)
s12 = ("s12", s12.color, s12.opacity, s12.num, s12.shape)




#Generates all combinations
def rSubset(arr, r):
    # return list of all subsets of length r
    # to deal with duplicate subsets use 
    # set(list(combinations(arr, r)))
    return list(combinations(arr, r))

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    r = 3
    combination_list = (rSubset(arr, r))

#Puts objects into comparing fn
for x in combination_list:
    Que = []
    for y in x:
        if y == 1:
            Que.append(s1)
        if y == 2:
            Que.append(s2)
        if y == 3:
            Que.append(s3)
        if y == 4:
            Que.append(s4)
        if y == 5:
            Que.append(s5)
        if y == 6:
            Que.append(s6)
        if y == 7:
            Que.append(s7)
        if y == 8:
            Que.append(s8)
        if y == 9:
            Que.append(s9)
        if y == 10:
            Que.append(s10)
        if y == 11:
            Que.append(s11)
        if y == 12:
            Que.append(s12) 
    compare(((Que[0])[0]), ((Que[0])[1]), ((Que[0])[2]), ((Que[0])[3]), ((Que[0])[4]), ((Que[1])[0]), ((Que[1])[1]), ((Que[1])[2]), ((Que[1])[3]), ((Que[1])[4]), ((Que[2])[0]), ((Que[2])[1]), ((Que[2])[2]), ((Que[2])[3]), ((Que[2])[4]))

#Time
executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))