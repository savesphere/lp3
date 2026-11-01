
# DAA: Job Sequencing with Deadlines using Greedy Method

def job_sequencing(jobs):

    if not jobs:
        print("No jobs available!")
        return

    # Sort jobs according to profit in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)

    # Find maximum deadline
    max_deadline = max((job[1] for job in jobs if job[1] > 0), default=0)

    # Create time slots
    slots = [None] * max_deadline

    total_profit = 0
    step_count = 0

    # Schedule jobs in available slots
    for job in jobs:
        job_id, deadline, profit = job

        # Check slots from latest to earliest
        for j in range(min(deadline, max_deadline) - 1, -1, -1):
            step_count += 1

            if slots[j] is None:
                slots[j] = job_id
                total_profit += profit
                break

    # Display scheduled jobs
    print("\nScheduled Jobs:")

    for job in slots:
        if job is not None:
            print(job, end=" ")

    print("\nTotal Profit:", total_profit)
    print("Step Count:", step_count)


# Main Program
n = int(input("Enter number of jobs: "))

if n <= 0:
    print("Enter a positive number of jobs")

else:
    jobs = []

    for i in range(n):
        job_id = input("Enter job ID: ")
        deadline = int(input("Enter deadline: "))
        profit = int(input("Enter profit: "))

        jobs.append((job_id, deadline, profit))

    job_sequencing(jobs)
