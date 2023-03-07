#Build Tower
#Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

#For example, a tower with 3 floors looks like this:

#[
#  "  *  ",
 # " *** ", 
#  "*****"
#]
#And a tower with 6 floors looks like this:

#[
#  "     *     ", 
#  "    ***    ", 
#  "   *****   ", 
#  "  *******  ", 
#  " ********* ", 
#  "***********"
#]
#Go challenge Build Tower Advanced once you have finished this :)

# My Solution

def tower_builder(n_floors):
    # build here
    tower = []
    floor = ''

    for f in range(n_floors):
        stars = '*' * (f*2 + 1)
        spaces = ' ' * (n_floors - f - 1)
        floor = spaces + stars + spaces
        tower.append(floor)
        
    return tower