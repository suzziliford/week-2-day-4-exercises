# 2) Best Time to Meet
# Billy is trying to figure out if there is a time that he and his team can meet to work on the project. 
# His three teammates each give him a list of times they are available ('HH:MM' 24-hour). 
# Create a function that will take in an original list plus any number of lists of teammate's 
# available times (remember *args) and return a list of times where everyone can meet.

# def my_function(arg1, arg2, *args, **kwargs):
#     print(arg1)
#     print(arg2)
#     print(args)
#     print(type(args))
#     print(kwargs)
#     print(type(kwargs))

person1 = ['09:00', '10:30', '11:30', '12:00', '13:00', '14:30']
person2 = ['09:30', '10:00', '10:30', '12:00', '14:30', '16:00']
person3 = ['09:00', '09:30', '11:00', '11:30', '12:00', '13:30', '14:30', '15:00']
person4 = ['11:00', '11:30', '12:00', '14:00', '14:30', '16:30', '17:00']
# Available Times: '12:00' and '14:30'

# s5 = s2.intersection(s1)
# e = set(my_list)

# def peeps_availabile( ):

#     bob = set(person1)
#     adam = set(person2)
#     pete = set(person3)
#     jeff = set(person4)

#     list_of_available_times = bob & adam & pete & jeff
    
#     print()


# def meet = set()
#     for time in args:
#         if time not in meet:
#             meet.add(time)



# meet & set(args)
# return list(meet)     
# 
#        

person1 = ['09:00', '10:30', '11:30', '12:00', '13:00', '14:30']
person2 = ['09:30', '10:00', '10:30', '12:00', '14:30', '16:00']
person3 = ['09:00', '09:30', '11:00', '11:30', '12:00', '13:30', '14:30', '15:00']
person4 = ['11:00', '11:30', '12:00', '14:00', '14:30', '16:30', '17:00']

def times_to_meet(a_list, *args):
    set1 = set(a_list)
    for person in args:
        set1 &= set(person)
    return set1

print(times_to_meet(person1, person2, person3, person4))