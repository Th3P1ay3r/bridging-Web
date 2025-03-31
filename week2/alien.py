#clist =[45,56,44,233,67] list,list()
#ctuple= (78,44,333,44) tuple, tuple()
#creading a dictionary
alien_0 = {'color' : 'green', 'points' :5}
print(alien_0['color'])
print(alien_0['points'])
print("type",type(alien_0))
print("len",len(alien_0))
print(alien_0)

#adding new item including key and value
alien_0['x_position']=0
alien_0['y_position']=25

#viewing the whole raw dictionary
print(alien_0)

#updating a value at specified key
alien_0['x_position']= 10

#
print(alien_0)

