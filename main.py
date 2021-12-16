#make an improper list, means un equal number of rows and columns.
#You can also make equal the list to have equal nuber of rows and columns 
students = [['Joe', 'Kim','senan'], ['Sam', 'Sue'], ['Kelly']]

#make a for loop
#The len(students) is to pass the number of rows as an argument to the range function
for r in range(len(students)):
    
    #len(students[r]) counts every index with in the index, to assign the number of columns to the col_count variable
    col_count = len(students[r])
    
    for c in range(col_count):
        print(students[r][c])