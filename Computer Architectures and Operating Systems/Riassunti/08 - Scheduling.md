In modern architecture, the maximum instruction throughput possible is desired. Thus, instruction execution overlapping is inevitable and necessary.

Modern programs are a interleaving of two kinds of operations:
- CPU operation(bursts)
- I/O operations(bursts)

![[Pasted image 20231130131311.png]]

I/O bursts are slower compared to the CPU ones. When a program is waiting for an I/O operation, it is possible to start a CPU one.

The part of a system which assigns the CPU to the different programs is the scheduler.
## CPU scheduler
The CPU scheduler selects from among the processes in ready queue, and allocates a CPU core to one of them.

It usually implements an decision algorithm, which uses a queue during the decision phase.

CPU scheduling decisions may take place when a process generates an event, such as:
1. Switches from running to waiting state
2. Switches from running to ready state
3. Switches from waiting to ready
4. Terminates
##### Scheduler preemption
In some cases, the scheduler may decide to remove the right CPU execution to a program in favor of another one. This kind of scheduler are called preemptive.

If the scheduler cannot remove the execution privilege from a process for which it has been allocated before it releases it by either terminating or switching to a waiting state, it is called **nonpreemptive**.

> Virtually all modern operating systems including Windows, MacOS, Linux, and UNIX use preemptive scheduling algorithms.

Preemptive schedulers may cause a **race condition** when data are shared among several processes.

> Consider the case of two processes that share data. While one process is updating the data, it is preempted so that the second process can run. The second process then tries to read the data, which are in an inconsistent state.
### Dispatcher
The dispatcher is the module that physically assign the CPU to a given process. 
It handles saving the state into the **Process control block**(a data structure which stores processes states with some addition informations) and restoring it when needed.

Its duty involves:
- handling the context switch
- switching to user mode
- jumping to the proper location in the user program to restart that program

> In some cases, it is part of the scheduler.

A context switch requires a certain amount of time, to save the state and restore the state of another one, which is called **dispatch latency**.

![[Pasted image 20231130132800.png]]
### Scheduling criteria
All scheduling algorithms are design to optimize a certain aspect of the problem.

One crucial aspect is certainly to keep the CPU as busy as possible, but other ones are also important. For example the process throughput is also a considerable factor for a processor performance.

Others criteria are:
- the **turnaround time**: the amount of time needed to completely execute a given process
- the **waiting time**: the amount of time a process has been waiting in the ready queue
- the **response time**: the amount of time it takes from when a request was submitted until the first response is produced.

Given the previously described criteria, a optimal scheduler should:
- maximize the CPU utilization
- maximize the throughput
- minimize the turnaround time
- minimize the waiting time
- minimize the response time
#### FCFS: first-come first-served
Is the simplest scheduler possible.

When implementing this schema, the scheduler assigns the CPU to the first process requiring it, using a FIFO queue.

The median waiting time for this algorithm is quite long.
Take a look at this example:

Process|Required time|Waiting time
--|--|--
$P_1$|$24$|$0$
$P_2$|$3$|$24$
$P_3$|$3$|$27$

The average waiting time is $(0+24+27)/3=17ms$, but with the inverted order execution time would be shorter.
Thus, the the average waiting time of this schema depends on the order of the processes in the queue.

This schema is also **nonpreemptive**.
##### SJF: Shortest job first
This schema associates each process to the length of the next CPU burst, using it to schedule the process with the shortest time.

When the CPU is available, the scheduler assigns it to the process which has the lowest CPU burst time required. This allows to minimize the average waiting time, which makes it optimal.

Take int account the previous example, the average execution time is $(0+3+27)/3=10ms$, which is much lower.
This schema is also nonpreemptive.
#### SRTF: shortest remaining time first
The preemptive version of the previous schema is the **shortest remaining time first** schema.

As previously said, the burst time of a process is not usually known, but can be estimated using exponential averaging:
$$τ_{n+1}=\alpha t_n+(1-\alpha)τ_n$$

where:
- $0\le \alpha \le 1$
- $t_n$ is the actual length of the $n^{th}$ CPU burst
- $τ_n$ predicts the value of the next CPU burst using the computation history

> The expanded formula is:$$τ_{n+1}=\alpha t_n+\alpha(1-\alpha)t_{n-1}+...+\alpha(1-\alpha)^jt_{n-j}+...+(1-\alpha)^{n+1}τ_0$$

The SJF schema is only theoretical, because is it difficult to estimate precisely the burst time of a process, and is also non preemptive. 

Take a look at this example: the first picture shows the scheduling that would occur if the SJF schema is implemented
![[Pasted image 20231226163909.png|600]]
meanwhile, the following picture shows the scheduling that would occur with the SRTF schema instead:
![[Pasted image 20231226163657.png|600]]
#### RR: round robin
The round robin algorithm is similar to the fcfs one.
This schema divides the CPU execution time between all the waiting processes, splitting it into **time quantum** usually of 10 to 100 milliseconds .

> A time quantum should always take longer than the time required for the context switch, which often takes less than $10\,ms$.
> A time quantiles shouldn't be to long either, in that case this schema performance can be compared to the FCFS one.

If there are $n$ processes in the ready queue and the time quantum is $q$, then each process gets $1/n$ of the CPU time in chunks of at most $q$ time units at once. 
In this way, no process waits more than $(n-1)q$ time units.

It also implements a timer, which is used to generate a interrupt which forces the context switch in favour of the next process.

The time quantum should be large compared to context switch time, it is usually in the order of 10 to 100 milliseconds, because the context switch usually takes less than 10 ms.
#### Priority scheduling
Another schema associates a **priority** value to each process.

The CPU is allocated to the process with the highest priority, meaning that a process with a lowest priority value has the maximum priority in the queue.

This schema can be both preemptive or nonpreemptive.

> SJF is priority scheduling where priority is the inverse of predicted next CPU burst time.

In some cases, some processes with low priority value may never be executed. this problem is called **starvation**. To solve this, an **aging mechanism** is implemented, which increases a process priority as time passes, to ensure it is executes at some point.

![[Pasted image 20231226163333.png|600]]
> It is also possible to combine with the Round robin algorithm.
#### Multilevel queue
A multilevel queue is a CPU scheduling algorithm that divides the ready queue into **multiple levels**, each with a different priority.

Processes are assigned to queues based on their characteristics, such as priority, memory usage, and CPU usage.

Processes can move between queues during execution if certain criteria are met.

> For example, real-time processes, which need to meet specific deadlines, can be assigned to a high-priority queue. 
> Interactive processes, which need to respond to user input quickly, can be assigned to a medium-priority queue. 
> And batch processes, which can run in the background, can be assigned to a low-priority queue.

The MLFQ scheduler is defined by the following parameters:
- **Number of queues:** The number of queues in the MLFQ scheduler.
- **Scheduling algorithms for each queue:** The scheduling algorithm used for each queue.
- **Method used to determine when to upgrade a process:** The method used to determine when to move a process to a higher-priority queue.
- **Method used to determine when to demote a process:** The method used to determine when to move a process to a lower-priority queue.
- **Method used to determine which queue a process will enter when that process needs service:** The method used to determine which queue a new process will be placed in.
##### Multilevel Feedback Queue
To solve the issues that can arise with starvation, aging is implemented using **multilevel feedback queue**.

To explain how those work, consider a multilevel feedback queue with three queues:
- **Q0:** A round-robin queue with a time quantum of 8 milliseconds.
- **Q1:** A round-robin queue with a time quantum of 16 milliseconds.
- **Q2:** A first-come-first-served (FCFS) queue.

A new process enters queue Q0, which is served in round-robin. When a process gains the CPU, it receives 8 milliseconds of CPU time. If a process does not finish in 8 milliseconds, it is moved to queue Q1.

At Q1, the job is again served in round-robin and receives 16 additional milliseconds of CPU time. If a process still does not complete, it is preempted and moved to queue Q2.

Processes in queue Q2 are served in first-come-first-served order.
![[Pasted image 20231226165152.png|600]]