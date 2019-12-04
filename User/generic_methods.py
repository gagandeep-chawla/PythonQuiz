
def student_name(name):
    instance = ''
    while True:
        instance = input('Enter student name')
        if instance.isaplha():
            break
        else:
            print('invalid student name \n please try again')
            continue
    return instance

def student_standard():
    instance = ''
    while True:
        instance = input('Enter the student standard')
        if instance.isnumeric():
            break
        else:
            print('invalid standard\n please enter valid standard ')
            continue
        
            