jobs = {}
total_resources = int(input("Enter total resources: "))
numbers_of_jobs = int(input("Enter Number Of Jobs: "))
sequence = []
    
for i in range(numbers_of_jobs):
    name = input("Enter Job Name: ").upper()
    allocation = int(input("Enter Job Allocation: "))
    max_allocation = int(input("Enter Job Max: "))
    job_need = max_allocation - allocation
    jobs[name] = [allocation, max_allocation, job_need]

total_of_allocations = 0
for job_name, values in jobs.items():
    total_of_allocations += values[0]

available = total_resources - total_of_allocations

rtrn= 0
i = 0
deadlock = False
while jobs:
    for job_name, values in jobs.items():
        if available < values[2]:
            pass
        else:
            available -= values[2]
            print("{:>2}     {:<3} {:<3} {:<3}".format(job_name, values[2], "", available))

            rtrn = values[1]
            available += values[1]

            print("{:>2}exit {:<3} {:<3} {:<3}".format(job_name, "", rtrn, available))
            del jobs[job_name]
            sequence.append(job_name)
            break
    i = i + 1
    if i > numbers_of_jobs:
        deadlock = True
        break
        
if deadlock == False:
    print(f"Safe Sequence: {sequence}")
else:
    print("Unsafe: DEADLOCK DETECTED")