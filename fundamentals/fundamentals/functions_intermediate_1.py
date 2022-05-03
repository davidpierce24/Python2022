# 1 Update values in dictionaries and lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1
x[1][0] = 15
print(x)

# 2
students[0]['last_name'] = 'Bryant'
print (students)

# 3
sports_directory['soccer'][0] = 'Andres'
print (sports_directory)

# 4
z[0]['y'] = 30
print(z)



# 2 Iterate through a list of dictionaries
def iterateDictionary(some_list):
    for x in range(0, len(some_list)):
            print (some_list[x])

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel




# 3 Get values from a list of dictionaries



# 4 Iterate through a dictionary with list values