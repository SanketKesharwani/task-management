#print("Hello, World!")
import sys

def excess_data():
    try:
        file = open('task.txt','r')
        index = 1
        for task in file:
            task = task.strip('\n')
            value = task.split(" ")[0]
            key = task.split(" ")[1]
            task_list.update({key:value})
            index = index+1
    except:
        sys.stdout.buffer.write("There are no pending tasks!".encode('utf8'))
        
def ls():
    try:
        excess_data()
        index = 1
        if len(task_list) == 0:
            sys.stdout.buffer.write("There are no pending tasks!".encode('utf8'))
        else:
            for task in sorted (task_list):
                sys.stdout.buffer.write(f"{index}. {task_list[task]} {task}".encode('utf8'))
                sys.stdout.buffer.write("\n".encode('utf8'))
                index = index+1
    except Exception as e:
        raise e
    
def deL(num):
    try:
        excess_data()
        num = int(num)
        sorted_task_list = list(sorted(task_list))
        task = sorted_task_list[num-1]
        with open("task.txt", "r+") as file1:
            remove_task = file1.readlines()
            file1.seek(0)
            for i in remove_task:
                if i.strip('\n') != task_list[task]+" "+task:
                    file1.write(i)
            file1.truncate()
        sys.stdout.buffer.write(f"Deleted task #{num}".encode('utf8'))
    except:
        sys.stdout.buffer.write(f"task with index #{num} does not exist. Nothing deleted.".encode('utf8'))
        
def done(num):
    try:
        excess_data()
        num = int(num)
        sorted_task_list = list(sorted(task_list))
        task = sorted_task_list[num-1]
        file = open('completed.txt','a')
        file.write(task_list[task])
        file.write(" ")
        file.write(task)
        file.write('\n')
        file.close()
        sys.stdout.buffer.write(f"Marked item as done.".encode('utf8'))
        with open('task.txt', 'r') as file1:
            with open('completed.txt', 'r') as file2:
                content_diff = set(file1).difference(file2)
        content_diff.discard('\n')

        with open('task.txt', 'w') as file_out:
            for line in content_diff:
                file_out.write(line)
                
    except:
        sys.stdout.buffer.write(f"Error: no incomplete item with index #{num} exists.".encode('utf8'))
           

def add(task_num,task_name):
    file = open('task.txt','a')
    file.write(task_name)
    file.write(" ")
    file.write("["+task_num+"]")
    file.write('\n')
    file.close()
    sys.stdout.buffer.write(f"Added task: \"{task_name}\" with priority {task_num}".encode('utf8'))

def help():
    usage_manual = """Usage :-
    $ ./task add 2 hello world    # Add a new item with priority 2 and text \"hello world\" to the list
    $ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
    $ ./task del INDEX            # Delete the incomplete item with the given index
    $ ./task done INDEX           # Mark the incomplete item with the given index as complete
    $ ./task help                 # Show usage
    $ ./task report               # Statistics"""
    sys.stdout.buffer.write(usage_manual.encode('utf8'))
    
def report():
    excess_data()
    try:
        file2 = open('completed.txt','r')
        index = 1
        for task in file2:
            task = task.strip('\n')
            value = task.split(" ")[0]
            key = task.split(" ")[1]
            done_list.update({key:value})
            index = index+1
        sys.stdout.buffer.write(f"Pending : {len(task_list)}".encode('utf8'))
        sys.stdout.buffer.write("\n".encode('utf8'))
        ind1 = 1
        for task in sorted (task_list):
            sys.stdout.buffer.write(f"{ind1}. {task_list[task]} {task}".encode('utf8'))
            sys.stdout.buffer.write("\n".encode('utf8'))
            ind1 = ind1+1
        sys.stdout.buffer.write(f"Completed : {len(done_list)}".encode('utf8'))
        sys.stdout.buffer.write("\n".encode('utf8'))
        ind2 = 1
        for task in sorted (done_list):
            sys.stdout.buffer.write(f"{ind2}. {done_list[task]}".encode('utf8'))
            sys.stdout.buffer.write("\n".encode('utf8'))
            ind2 = ind2+1
    except:
        sys.stdout.buffer.write(f"Pending : {len(task_list)}".encode('utf8'))
        sys.stdout.buffer.write(f"Completed : {len(done_list)}".encode('utf8'))
        
    

if __name__ == "__main__":
    try:
        values = sys.argv
        task_list = {}
        done_list = {}
        if(values[1] == 'del'):
            values[1] = 'deL'
        if(values[1]=='add' and len(values[2:])==0):
            sys.stdout.buffer.write("Missing tasks string. Nothing added!".encode('utf8'))
        elif(values[1]=='deL' and len(values[2:])==0):
            sys.stdout.buffer.write("Missing NUMBER for deleting tasks.".encode('utf8'))
        elif(values[1]=='done' and len(values[2:])==0):
            sys.stdout.buffer.write("Missing NUMBER for marking tasks as done.".encode('utf8'))
        else:
            globals()[values[1]](*values[2:])
    except Exception as e:
        usage_manual = """Usage :-
    $ ./task add 2 hello world    # Add a new item with priority 2 and text \"hello world\" to the list
    $ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
    $ ./task del INDEX            # Delete the incomplete item with the given index
    $ ./task done INDEX           # Mark the incomplete item with the given index as complete
    $ ./task help                 # Show usage
    $ ./task report               # Statistics"""
        sys.stdout.buffer.write(usage_manual.encode('utf8'))
        