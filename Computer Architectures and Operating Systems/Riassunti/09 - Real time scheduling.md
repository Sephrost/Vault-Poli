Tasks(processes in Micrium-OS) can be periodic, aperiodic, or sporadic.
- **Periodic tasks:** Consist of an infinite sequence of identical activities, called instances or jobs, that are regularly activated at a constant rate. They are also referred as **time-based tasks**.
- **Aperiodic tasks:** Consist of an infinite sequence of identical jobs, which are not activated at a regular rate.
- **Sporadic tasks:** Aperiodic tasks for which it is not possible to determine a minimum inter-arrival time interval are called sporadic tasks.

**Periodic** tasks are the **most predictable** type of task, as they always occur at the same rate. **Aperiodic** tasks are **less predictable** , as they can occur at any time. 
**Sporadic** tasks are the **least predictable**, as there is no guaranteed minimum amount of time between occurrences.
## Notation used
| Notation | Meaning |
| ---- | ---- |
| $τ$ | Periodic task |
| $τ_i$ | $i$-th instance of the task |
| $T$ | Period of the task |
| $D_i$ | Relative deadline |
| $d_i$ | Absolute deadline |
| $a_i$ | Activation time |
|$S_i$|Start time| 
|$F_i$|Finishing time|
|$C_i$|Worst-case execution time
|R|The response time
|$f_i$|The finishing time
![[Pasted image 20231231121253.png|650]]
## Scheduling of periodic tasks
Scheduling of periodic tasks should be, on the paper, the simplest kind of task scheduling. We consider three algorithms.
### Timeline scheduling
**Timeline scheduling** is a real-time scheduling algorithm that **divides** the **time** axis into **slots** of **equal length** called **minor cycles**. 
**One or more tasks** can be allocated for execution **in minor cycles**, in such a way to respect the frequencies derived from the application requirements. 
A **timer synchronizes** the activation of the tasks at the beginning of each time slot. 
A sequence of minor cycles repeated identically is called a **major cycle**.

![[Pasted image 20231227164753.png|650]]
Timeline scheduling is feasible if:
- The sum of the WCETs(worst case execution time) for the tasks in the minor cycle is at most equal to the minor cycle length.
- The tasks are independent, i.e., they must not require any synchronization or communication.
#### Implementation
Timeline scheduling is quite easy to implement: each task can be coded as a function, while each minor cycle is implemented as a function that call each task allotted in the minor cycle.
At this point, the major cycle is a endless loop that call each minor cycle function.

![[Pasted image 20231227174552.png|550]]

The execution of the minor cycle function call is regulated by an interrupt timer programmed with the minor cycle duration.
### Rate Monotonic scheduling
Another algorithm used to schedule periodic task is the **Rate Monotonic Scheduling** (RMS) one.
RMS assigns priorities to tasks based on their **periods**(also called deadline), with **shorter** periods having **higher priorities**. This ensures that tasks with closer deadlines are more likely to meet their deadlines.

> The priorities of tasks are assigned pre runtime and do not change during the execution of the system, as in timeline scheduling.

To schedule processes using rate monotonic scheduling, the following steps are taken:
1. Each process is assigned a priority based on its period. The shorter the period, the higher the priority.
2. When a process becomes ready to run, the scheduler selects the process with the highest priority.
3. The selected process runs until it completes or is preempted by a higher priority process.
4. If a higher priority process becomes ready to run while a lower priority process is running, the lower priority process is preempted.
#### Example
Take a look at the tasks shown in this picture.
At $t=0$, all tasks are ready. The first one to be executed is $\tau_1$ then, at its completion, $\tau_3$. 
At $t = 13$, $\tau_2$ finally starts but, at $t = 20$, $\tau_1$ is released again.

![[Pasted image 20231230183929.png|600]]

Hence, $\tau_2$ is preempted in favour of $\tau_1$. 
While $\tau_1$ is executing, $\tau_3$ is released, but this does not lead to a preemption: $\tau_3$ is executed after $\tau_1$ has finished. 
Finally, $\tau_2$ is resumed and then completed at $t = 39$.

![[Pasted image 20231230184243.png|600]]
At $t = 40$, after $1 ms$ of idling, task $\tau_1$ is released.
Since it is the only ready task, it is executed immediately, and completes at $t = 47$.

![[Pasted image 20231230185116.png|600]]

At $t = 50$, both $\tau_3$ and $\tau_2$ become ready simultaneously.
$\tau_3$ is run first, then $\tau_2$ starts and runs for $4 ms$. However, at $t = 60$, $\tau_1$ is released again.

![[Pasted image 20231230185246.png|600]]

As before, this leads to the preemption of $\tau_2$ and $\tau_1$ runs to completion.
Then, $\tau_2$ is resumed and runs for $8 ms$, until $\tau_3$ is released.

![[Pasted image 20231230185416.png|600]]

$\tau_2$ is preempted again to run $\tau_3$. The latter runs for $5 ms$ but at $t = 80$, $\tau_1$ is released for the fifth time.

![[Pasted image 20231230185512.png|600]]

$\tau_3$ is preempted, too, to run $\tau_1$. 
After the completion of $\tau_1$, both $\tau_3$ and $\tau_2$ are ready. $\tau_3$ runs for $1 ms$, then completes.

![[Pasted image 20231230185628.png|600]]

Finally, $\tau_2$ runs and completes its execution cycle by consuming $1 ms$ of CPU time.
After that, the system stays idle until $t = 100$, where the whole cycle starts again.

#### Feasibility of RMS
Given a task, its relative deadline is equal to its period($D_i=T_i\;\forall\; i$), while its absolute deadline its the time of its next release($d_{i,j}=r_{i,j+I}$).

Furthermore, an **overflow** occurs when a task was released, but it was not able to finish executing before its deadline. Thus, scheduling is feasible for a given task set if there is a possible schedule such as no overflow ever occurs.
##### Example of overflow
Let us consider two tasks, $τ_1$ and $τ_2$, with $T_1 < T_2$.
If their priorities are not assigned according to RM, then $τ_2$ will have a priority higher than $τ_1$.

At a critical instant ($r_1=r_2=0$), their situation is as follows:
![[Pasted image 20231230192551.png|600]]

This means that both tasks are released at the same time. The graph shows that τ₂ will start executing before τ₁, even though τ₁ has a higher priority. This is because τ₂ has a shorter period and therefore a higher priority according to RM scheduling.

The scheduling is feasible **iff**: $C_1+C_2 < T_1$.

Lets take another look at that case. If priorities are assigned according to RM, $τ_1$ will have a priority higher than $τ_2$.
Two cases must then be considered:
- **Case 1:** The execution time of task τ₁, C₁ is short enough so that all instances of τ₁ are completed before the next release of τ₂.
- **Case 2:** The execution of the last instance of τ₁ overlaps the next release of τ₂.

In Case 1, the scheduling is feasible because all instances of τ₁ are completed before the next release of τ₂. This means that τ₂ will never be preempted by τ₁, and therefore τ₂ will always be able to meet its deadline.

![[Pasted image 20231230193200.png|600]]

Given any set of tasks $\Gamma=\{\tau_1,\dots,\tau_n\}$ be a set of n periodic tasks, where each task $\tau_i$ is characterized by a processor utilization $U_i$.
$\Gamma$ is schedulable with RMS if
$$\prod^{n}_{i=1}(U_i+1)\le 2$$
### Earliest Deadline First Scheduling
The Earliest Deadline First Algorithm, or EDF, **selects tasks** according to **their absolute deadlines**. At each instant, the task with earliest deadline will receive highest priority.

This schema assumes that:
- tasks have dynamic priority, to they can change over time
- The scheduler is preemptive
- The architecture only implements one processor

A set of periodic task is schedulable in this manner only if the scheduler factor is equal or less than 1, or
$$\sum^{n}_{i=1}\frac{C_i}{T_i}\le1$$
EDF is more complex than RM, but is also more performant.
In overloading situation, such as starting and stopping a lot of tasks, it is more difficult to predict with precision, so RM is a much simpler approach to predict, which can be more suitable. In such situations, EDF can also experience a domino effect, in n which a large number of tasks unnecessarily miss their deadline.

As a rule of thumb, EDF is always able to exploit the full processor capacity, whereas RM in the worst case does not.
## Aperiodic Task
Aperiodic tasks are tasks that are not activated in regular intervals.

For those kind of tasks, scheduling algorithms are defined using:
- $\alpha$, which described the machine environment on which the task set has to be scheduled(number of processors, distributed architecture,$\dots$)
- $\beta$, which describes the task itself and its resource characteristics(preemptive, synchronous activations, $\dots$)
- $\gamma$, which indicates the optimality criterion to be followed in the schedule
### Jackson's algorithm
A common problem is the scheduling of a series of tasks with asynchronous arrival time on a machine which implements a single processor. In this scenario, tasks can have different WCET and deadline.

To minimize the lateness of the tasks, this algorithm uses the earliest due date criteria. In fact, given a set of $n$ independent tasks, any algorithm that executes the tasks in order of non decreasing deadlines is optimal with respect to minimizing the maximum lateness.
#### Example
Take a look at the set of 5 tasks shown in the following example. with their WCET and absolute deadline. The arrival time of all tasks is 0.

 | |J_1|J_2|J_3|J_4|J_5|
--|--|--|--|--|--
$C_i$|1|1|1|3|4|5
$d_i$|3|10|7|8|5

The algorithm is applied as follows:
1. The tasks are sorted in order of nondecreasing deadline. This gives the following order: $J_1$, $J_5$, $J_3$, $J_4$, and $J_2$.
2. The tasks are scheduled in the order given in step 1.
This order generate the following timetable:

![[Pasted image 20231231124852.png|650]]

which also allows to graphically see that the maximum lateness is the one of $J_4$, which is $-1$.
### Horn's algorithm
Jackson's algorithm assumes that all the tasks arrives at the same time. This allows to ignore the preemption handling overhead. 
In any other scenario, preemption is needed.

Given a set of $n$ independent tasks with arbitrary arrival times, any algorithm that at any instant executes the task with the earliest absolute deadline among all the ready tasks is optimal with respect to minimizing the maximum lateness.
## Both periodic and aperiodic
So far we considered only homogenous task sets, but in reality tasks are not an homologous type.
In real application heterogeneous task sets are used.
### Background scheduling
Background scheduling can improve system responsiveness and reduce latency.
With this technique, **periodic** tasks are **scheduled** using **rate monotonic scheduling**, while **aperiodic** tasks are scheduled in **background**, when no periodic instance is ready.
This ensures that critical tasks are always processed first, and also ensures that background tasks are not allowed to interfere with critical tasks.

![[Pasted image 20240102131114.png|550]]

This approach is very simple, requiring only **two queue**(one for periodic tasks and one for aperiodic), but it has quite a **few issues**.
First of all, **background tasks can be starved** if the system is always processing foreground tasks, leading to performance degradation and reliability issues. So it is really only suitable when aperiodic tasks are soft real-time.
### Polling server
Polling servers are a type of server that is designed to serve periodic tasks as soon as possible.

The server is characterized by:
- **Ts:** The period of the server. This is the amount of time between each time that the server checks for new tasks to run.
- **Cs:** The capacity/budget of the server. This is the amount of time that the server has available to run tasks each period.

Polling servers are constantly checking for new tasks to run. 
If there are any aperiodic tasks ready to run, the server will run them until its budget is exhausted. If there are no aperiodic tasks ready to run, the server will idle until the beginning of the next period, when its budget is replenished.

Considering $n$ period tasks each with utilization $U_i$ and a polling server with utilization $U_s=C_s/T_s$, the task set is feasible with RM:
$$\prod^{n}_{i=1}(U_i+1)\le\frac{2}{U_s+1}$$
So, how to set $C_s$ and $T_s$ so that the resulting scheduling is feasible? 
we are looking for the polling server maximum utilization factor 
$$P=\prod^{n}_{i=1}(U_i+1)$$
$$U_s^{max}=\frac{2-P}{P}$$
So, given $U_s^{max}$, as a rule of thumb:
- Set U, at most equal to $U_s^{max}$
- Set T, as the period of the periodic task with the shortest period (the polling server becomes the highest priority task) 
- Set $C_s=U_s\cdot T_s$
### Deferrable server
Deferrable servers are a type of server that is designed to serve aperiodic tasks by creating a periodic task(which usually has high priority) only for this end, like polling servers.

The capacity of a deferrable server is maintained until the end of the period, and is replenished at the start of a new one.
Aperiodic requests can be serviced at the same server’s priority at anytime, as long as the capacity has not been exhausted.

Considering $n$ period tasks each with utilization $U_i$ and a deferrable server with utilization $U_s=C_s/T_s$, the task set is feasible with RM:
$$\prod^{n}_{i=1}(U_i+1)\le\frac{U_s+2}{2U_s+1}$$
So, how to set $C_s$ and $T_s$ so that the resulting scheduling is feasible? 
we are looking for the deferrable server maximum utilization factor 
$$P=\prod^{n}_{i=1}(U_i+1)$$$$U_s^{max}=\frac{2-P}{2P-1}$$
## Priority inversion
At any moment, a process may need some resource to continue its execution. 
Those can be either shared between processes, private/dedicated to a process, or shared but protected against concurrent processes(mutex).

We recall that a piece of code executed under mutual exclusion is called **critical section**.
Any task that needs to enter a critical section has to wait until no other task is holding the resource, entering the waiting state, stalling until the blocking resource is available.
When a task leaves a critical section, the resource associated with the critical section becomes free, and it can be allocated to another waiting task, if any.

But what if a process with a lower priority holds an exclusive resource privilege for its execution and another process with higher priority is blocked by it?

The blocking time of a task on a busy resource cannot be bounded by the duration of the critical section executed by the lower-priority task.

Assuming that rate monotonic scheduling is used, there are three possible solutions.
### Non-Preemptive Protocol
As we know, preemption is not allowed during critical section execution.

One simple solution to the problem is to raise the priority of a task to the highest value possible whenever it enters a critical section, and lowering it whenever it exits it.
### Immediate Priority Ceiling
Another solution is similar to NPP, but instead of setting the priority to the highest value possible, it is possible to set it to the highest priority among the tasks sharing that resource, lowering it when the task exits its critical section.
### Priority Inheritance Protocol
When a task $\tau_i$ blocks one or more higher-priority tasks, it temporarily assumes (inherits) the highest priority of the blocked tasks
This prevents medium-priority tasks from preempting $t_i$ and prolonging the blocking duration experienced by the higher-priority tasks.

