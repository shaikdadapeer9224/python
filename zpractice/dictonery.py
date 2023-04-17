# ???students={
#     1:'farak',
#     2:'appa',
#     3:'appanna',
#     'asdasdasdasdqejnp':'badi'
# }
# print(students['asdasdasdasdqejnp'])
#get method
# print(students.get(1))
#print(students[11]) we get error 11 key not found but in get it will show none
# print(students.get(11))
# print(students.get(11),'student not available')
#custom also we can print
# students[123]='kaaaaaaa'# adding
# print(students)

'''alll                          mixxing code
fark_talents={
    'chiru':'dancing',
    'balayya':['fighting','dialogue'],
    'ntr_family':{
        'ntr':['temper','janata_garage'],
        'balakrishna':['veerasimhareedy','akhanda']
    }
}
print(fark_talents['ntr_family']['balakrishna'][1])#akhanda printing '''

#conveerting data to dictonary
'''name='dadapeer'
age=22
height=5.6
data=dict(
name='dadapeer',
age=22,
height=5.6
)
print(data)
print(data.keys())
print(data.values())
'''
# adding two lists into dictonary
'''hero=['chiru','allu','mahesh']
heroines=['sneha','pooja','rashmika']
result=zip(hero,heroines)
final_result=dict(result)
print(final_result)
final_result['raviteja']='kajal'
print(final_result)
print(type(final_result))'''

#while loop

# age=19
# while age<25:
#     print(age)
#     age=age+1
# print(age)

# for loop
# for i in range(0,10,2): #2 represents even
#     print(i)