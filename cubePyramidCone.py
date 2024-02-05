#Global Variables

#Sub-Programs
def Cube_Volume():
    Side = float(input("Please Input a side of the cube: "))# asks for input from the user
    print( f"The volume of the cube is {round(Side*Side*Side , 3)}")# calculates the volume and formats the value to 3 decimal figure

def SquarebasePyramid_Volume():
    base = float(input("Please input the base of the pyramid: "))# asks for input from the user
    height = float(input("Please input the height of the pyramid: "))# asks for input from the user
    print(f'The volume of the square based pyramid is {round((base*base)*(height/3) , 3)}')# calculates the volume and formats the value to 3 decimal figure

def Cone_Volume():
    radius = float(input("Please input the radius of the cone: "))# asks for input from the user
    height = float(input("Please input the height of the cone: "))# asks for input from the user
    print(f'The volume of the cone is {round((height/3)*(radius*radius)*3.14 , 3)}') # calculates the volume and formats the value to 3 decimal figure

#MainProgram
Cube_Volume()
SquarebasePyramid_Volume()
Cone_Volume()