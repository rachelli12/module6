"""
Program: inner_functions_assignment.py
Author: Rachel Li
Last date modified: 06/16/2020

The purpose of this program is to write a function
that accepst list of measurements for a rectangle
and list of measurements for square.
Print perimeter and area in string.
"""
#write function measurements that accepts list of measurements for a rectangle
def measurements(a_list):
    """
    Use reST style
    :param a_list: this represents the length
    :return: perimeter and area of rectangle and square
    """
    def area(a_list):
        """
        :param a_list: this represents the length
        :return: area of rectangle and square
        """
        if len(a_list) >= 1:
            square_area = a_list[0] * a_list[0]
            return square_area
        elif len(a_list) <= 2:
            rectangle_area = a_list[0] * a_list[1]
            return rectangle_area
        #can have one or two arguments
        #if square, area = length^2
        #if rectangle, area = length * width
    calculated_area = area(a_list)

    def perimeter(a_list):
        """
        :param a_list: this represents length
        :return: returns perimeter of square and rectangle
        """
        if len(a_list) >= 1:
            square_perimeter = a_list[0] * 4
            return square_perimeter
        elif len(a_list) <= 2:
            rectangle_perimeter = (a_list[0] + a_list[1]) * 2
            return rectangle_perimeter
        #perimeter = (length + width) * 2

    calculated_peri = perimeter(a_list)


    # assign variable to returned value from area
    # assign variable to returned value from perimenter
    return f'Perimeter={calculated_peri:.1f} Area={calculated_area:.1f}'
    # returns string with perimeter and area
    #"Perimeter = 14.0 Area = 12.25"

if __name__ == '__main__':
    rectangle_dimen = measurements([5.6, 8.9])
    print(rectangle_dimen)
    square_dimen = measurements([4.2])
    print(square_dimen)

#output:
#Perimeter=22.4 Area=31.4
#Perimeter=16.8 Area=17.6
