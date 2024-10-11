#create list of x*2 for x up to 10
list_doubles = [x*2 for x in range(11)]
print(list_doubles)

#create list of x*x for x up to 10
list_squares = [number*number for number in range(11)]
print(list_squares)

#create list of scores which are >50
list_scores_general = [40, 60, 70, 30, 20, 100, 80]
list_scores_good = [score for score in list_scores_general if score > 50]
print(list_scores_good)

#create list of positive numbers
list_numbers = [-2, -1, 0, 1, 2, 3, -4, -5, -6, 5, 6]
list_numbers_positive = [number for number in list_numbers if number >= 0]
print(list_numbers_positive)