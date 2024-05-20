#!/usr/bin/env python
# coding: utf-8

# In[2]:


#QUESTION 1

ages =  [19, 22, 19, 24, 20, 25, 26, 24, 25, 24] ##creating a list for the ages

ages.sort() #sorting the Ages list
print("sorted list = ", ages)

print(f"max age:{max(ages)}, min age:{min(ages)}") #To print the min and max age
ages.extend([min(ages),max(ages)]) #adding min and max ages to the ages list
print(f"added list: {ages}") # list after addition

Middle_Index = int(len(ages)/2) # middle index in the list
print(Middle_Index)
if Middle_Index % 2 == 0:   #Condition to find if the length is even
 print(f"The median of ages: {int((ages[Middle_Index-1]  + ages[Middle_Index])/ 2)}") #Printing the median age

print(f"Average age is: {sum(ages)/len(ages)}")      #Printing the average age

print(f"Range of the ages: {max(ages) - min(ages)}") # printing the range of the ages 


# In[1]:


#QUESTION 2

dog = {} #Created a empty dictionary
dog = {"name":"Max", "color":"brown", "bread":"Poomarian", "legs":"4", "age":"2"} #adding keys and values to the created directory

#Created a empty student dictionary
student= {} 
student= {"first_name":"Vinay","last_name":"Veereddy","gender":"Male","age":"25","martial status":"Single",
           "skills":['Critical Thinking '],"country":"india","city":"Hyderabad","address":"DilshukNagar"} #adding key values to Student Dictionary

print(f"length of student: {len(student)}") # Printing the lenght of student dictionary

print(type(student['skills']),student['skills'])         #Printing the values in skills and type of date   

student['skills'].extend(['Communication', 'Creativity', 'Leadership']) #modifying skills by extend function
print(student['skills'])

print(f"keys of student dictionary:{student.keys()}")   #Printing dictionary keys as list

print(f"values of student dictionary: {student.values()}") #Printing dictionary keys as values

      


# In[1]:


#QUESTION 3

brothers = ("Surya", "Srinu", "Gowtham", "Chintu")    #Created a brother tuple
sisters = ("Pooji", "Tulasi", "Sailu", "Chitti","Swapna")  #Created a sisters tuple
siblings = brothers+sisters                           #Adding the siblings tuple 
print(f"no of siblings: {len(siblings)}")             #Printing the number of siblings
print(siblings)
family_member = ()                           # created a family_member tuple
family_member += siblings + ("Madhu", "Gopika")  # modifying the family_member tuple by adding sibling to it
print("type: ",type(family_member))           # Printing the type of family_member
print("family member: ",family_member)                      


# In[3]:


#QUESTION 4

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
count = len(it_companies)
print(f"length of it_companies: ", count)                  #Printing the length of companies

it_companies.add("twitter")                                 #add twitter to the it_companies Set

print(f"add new company: ", it_companies)
it_companies.update(['Walmart', 'Accenture', 'BOFA'])  # multiple it companies
print(f"updated it companies:", it_companies)   

it_companies.remove('Accenture')                           #remove one company(which raises error)
print(f"remove it companies:", it_companies)

it_companies.discard('infosys')                           #discard which doesnt raise an error
print(f"discard it companies:", it_companies)

print(f"join A union B:{A | B}")                          # Printing the Union of A and B
print(f"join A intersection B:{A & B}")                   # Printing the intersection of A and B
print(f"if A is subset of B:{A.issubset(B)}")             #Printing the subset of B 
print(f"if A is disjoint of B:{A.isdisjoint(B)}")         #printng the disjoint of B

A.update(B)                                               #joint A with B and B with A
print(A) 
B.update(A)
print(B)

print(f"symmetric difference:{A.symmetric_difference(B)}") #Printing the symmetric difference
A.clear()
B.clear()
print(f"deleting both A and B: ", A.clear(), B.clear())    #Printing the deleted set 
print(f"The length of the list age:{len(age)}")
AgeSet=set(age)                                            #convert age to set and compare length of list and set
print(f"The length of the set age:{len(age)}")


# In[4]:


#QUESTION 5

radius=30                                       #taking radius as per input
print(f"radius of the circle is: ", radius)
area_of_circle=3.14*(radius**2)                 #area of circle                    
circumference_of_circle=2*3.14*radius           #circumference of circle
print(f"area of circle: ", area_of_circle)
print(f"circumference of circle: ", circumference_of_circle)
radius_input = int(input("enter radius"))      #To take the input from the console
new_area = 3.14*radius_input*radius_input
print(f"Area from user input radius: ", new_area)


# In[5]:


#QUESTION 6

sentence = "I am a teacher and I love to inspire and teach people"
list = sentence.split(' ')          #Split function by default uses whiteSpaces as the separator in the string sentence
print(list)
unique_words=len(set(list))                #number of unique words in given string
print(f"number of unique words in the given string: ",unique_words )      # printing the Unique_words length


# In[6]:


# QUESTION 7

print("Name\t\tAge\t\tCountry\t\tCity\nAsabeneh\t250\t\tFinland\t\tHelsinki")  #To print the text by using the tab escape sequence


# In[7]:


#QUESTION 8

radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")  #To find the radius of the circle



# In[10]:


#QUESTION 9

#list of students weights
weight_lbs = [150, 155, 145, 148]
weight_kgs = []

#converting weight to kgs
for x in weight_lbs:
    weight_kgs.append(x*0.453592)
print(f"weight in kgs: ",weight_kgs)   # Printing the Weight in Kgs


# In[ ]:




