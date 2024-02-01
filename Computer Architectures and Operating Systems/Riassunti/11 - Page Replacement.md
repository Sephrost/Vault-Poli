A process is some code that is running on the machine, so it should be fully loaded in the memory to be executed, but the entirety of it is not needed at the same time. Requiring more memory than necessary is not an ideal outcome.
## Virtual memory
Virtual memory is an memory management abstraction layer that allows to separate the local memory from the physical one.

The logical address space can be much larger that the physical one, allowing concurrent processes to share the same for a better memory allocation, resulting also in less I/O and swap operations at runtime. 

Another difference is that the virtual address space start at address 0 (usually), whereas the physical memory is organized in pages, requiring the Memory Management Unit to map logical addresses to physical ones.

![[Pasted image 20240123161105.png|550]]
### Demand Paging
Furthermore, it is possible to load the process in memory only when needed, instead than at load time. 
With this approach, the pager guesses which pages will be used before swapping out again, bringing them into memory. This prediction mechanism requires a new MMU functionality.

When a page are already in memory(memory resident), then it doesn't need to be loaded, but on the other hand, if its not present, the page must be located and loaded without changing the program behaviour.

![[Pasted image 20240123162917.png|550]]
#### Handling Page Fault with demand paging
The steps of the handling sequence are as follows:
1. If there is a reference to a page, first reference to that page will trap to operating system, this is called a page fault.
2. Operating system looks at another table to decide if
	1. it is an invalid reference, raising an abort signal.
	2. it is simply not in memory
3. Locate a free frame
4. Swap the page into the frame via scheduled disk operation
5. Reset tables to indicate page now in memory, setting the validation bit to true(v)
6. Restart the instruction that caused the page fault

![[Pasted image 20240123163314.png|550]]
#### Some other aspects
We take in consideration some special cases.
##### Start of the process
When a process starts, none of its pages are actually in memory.

The first instruction will thus cause a page fault, so the handling mechanism will be executed.
##### Multiple page faults
Some instruction could require access to different pages.

This problem could be leveraged by implementing a locality reference mechanism when bringing pages into the memory.
##### Hardware support
To implement demand paging, some additional hardware is required
- a page table with validity bit
- a swap device with swap space
- an instruction restart
#### Free-Frame list
The free-frame list is a data structure used by operating systems to manage memory allocation in virtual memory systems.

Most operating systems maintain a free-frame list, a pool of free frames that can be used to satisfy page fault requests.

When a system starts up, all available memory is placed on the free-frame list. This ensures that there are always enough free frames available to satisfy page fault requests.

It is typically maintained by the operating system's memory management unit (MMU).
##### Zero-fill-on-Demand
Most operating systems typically allocate free frames using a technique known as zero-fill-on-demand. 

This means that the operating system does not actually allocate any memory to a frame until it is actually needed. 
Instead, the content of the frame is zeroed-out when it is first allocated. This is a more efficient way to allocate memory, as it avoids the need to copy data from secondary storage into memory.
#### Performance of Demand Paging
Demand paging involves three major activities:
1. **Servicing the interrupt:** When a page fault occurs, the operating system interrupts the current process and performs several operations to handle the fault. These operations include saving the process state, determining the location of the missing page on disk, and allocating a free frame in memory.    
2. **Reading the page:** The operating system then reads the missing page from disk into the allocated frame. 
3. **Restarting the process:** Once the page has been read, the operating system restores the process state and resumes execution of the process from the interrupted instruction.

The first and third tasks can be reduced, with careful coding, to several hundred instructions.
These tasks may take from 1 to 100 microseconds each.
##### Page Fault Rate and Effective Access Time (EAT)
The performance of demand paging is affected by the page fault rate, which is the percentage of memory references that cause page faults. 
A lower page fault rate means that fewer interruptions are required, which can improve overall system performance.

The effective access time (EAT) is a measure of the average time it takes to access a memory location. 

The EAT for demand paging is calculated as follows:
$$

(1-p)\times memory\; access+
p \times (page\; fault\; overhead + swap\; page\; out + swap\; page\; in)

$$
where 
- $p$ is the page fault rate
- memory access time is the time it takes to access a memory location that is already in memory
- page fault overhead is the time it takes to handle a page fault.
###### An example
Let's now consider the case of a HDD as a paging device.
With an average page-fault service time of $8 ms$ and a memory-access time of $200 ns$, the effective access time in nanoseconds is:
$$
\begin{equation}
\begin{split}
effective\;access \;time &= (1 − p) \times (200) + p\,(8ms)\\
&= (1 − p) \times 200 + p \times 8,000,000\\
&= 200 + 7,999,800 \times p.
\end{split}
\end{equation}
$$
> The effective **access time** is **directly proportional** to the page-fault rate.

If one access out of $1000$ causes a page fault, the effective access time is $8.2 ms$.
The computer will be slowed down by a factor of $40$ because of demand paging!

If we want performance degradation to be less than $10\, \%$, we need to keep the probability of page faults at the following level:
$$
\begin{equation}
\begin{split}
&220 > 200 + 7,999,800 \times p,\\
&20 > 7,999,800 \times p,\\
&p < 0.0000025.
\end{split}
\end{equation}
$$
That is, to keep the slowdown due to paging at a reasonable level, we can allow fewer that one memory access out of 399,990 to page-fault.
#### Page replacement
To avoid memory waste it is possible to allocate the pages not currently being used by a process to other ones, increasing the level of multiprogramming, **over-allocating** the memory. Doing so, as a drawback, it could also increase the number of page faults overall.

When all the frames are allocated and a page must be brought in the main memory( as shown in the following picture), it could either:
- terminate a process. but paging should be transparent, so its a no-go
- swap a process out, but its no longer supported by most OSs
- combine swapping pages with page replacement, that is the current solution

![[Pasted image 20240131122027.png|650]]

Thus, if no frame is free, we find one that is not currently being used and free it, by writing it's contents to swap space and changing the page table (and all other tables) to indicate that the page is no longer in memory.
##### Page fault routine with page replacement
1. Find the location of the desired page on secondary storage.
2. Find a free frame:
	1. If there is a free frame, use it.
	2. If there is no free frame, use a page-replacement algorithm to select a victim frame.
	3. Write the victim frame to secondary storage (if necessary); change the page and frame tables accordingly.
3. Read the desired page into the newly freed frame; change the page and frame tables.
4. Continue the process from where the page fault occurred.

##### Reducing EAT
If no frames are free, two page transfers (one for the page-out and one for the page-in) are required. 
This situation effectively doubles the page-fault service time and increases the effective access time accordingly

We can reduce this overhead by using a modify bit (or **dirty bit**), associating a bit in the hardware to each page.
The dirty bit for a page is set by the hardware whenever any byte in the page is written into, indicating that the page has been modified. 

When we select a page for replacement:
- if the bit is set, we must write the page to storage, because it has been modified since it has been read from the secondary storage
- if the modify bit is not set, the content is already there

![[Pasted image 20240131123423.png|650]]
##### Page and Frame Replacement Algorithms
If we have multiple processes in memory, we must decide how many frames to allocate to each process; and when page replacement is required, we must select the frames that are to be replaced.

There are many different page-replacement algorithms. To evaluate its performances, we run the, on a particular string of memory references, called **reference string** and computing the number of page faults. 

Here's some tips:
- the number of page faults decreases as the number of page frames increase
- two consecutive page references will never cause a page fault
###### FIFO page replacement
A FIFO replacement algorithm associates with each page the time when that page was brought into memory. 
When a page must be replaced, the oldest page is chosen.

An example:
Take into account the following reference string
$$7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1$$
and consider a frame space of $3$.

Our three frames are initially empty. The first three references ($7, 0, 1$) cause page faults and are brought into these empty frames.
The next reference ($2$) replaces page $7$, because page $7$ was brought in first.
 Since $0$ is the next reference and $0$ is already in memory, we have no fault for this reference. 
 And so on and so forth.
![[Pasted image 20240131124851.png|650]]

The FIFO page-replacement algorithm is easy to understand and program.
However, its performance is not always good.

Notice that, even if we select for replacement a page that is in active use, everything still works correctly. After we replace an active page with a new one, a fault occurs almost immediately to retrieve the active page, increases the page-fault rate and slowing down process execution.
It does not, however, cause incorrect execution.

To illustrate the problems that are possible with a FIFO page-replacement algorithm, consider the following reference string:
$$1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5$$
The following picture shows the curve of page faults for this reference string versus the
number of available frames:
![[Pasted image 20240131130404.png|650]]

Notice that the number of faults for four frames (ten) is greater than the number of faults for three frames (nine)! 

This most unexpected result is known as **Belady’s anomaly**: for some page-replacement algorithms, the page-fault rate may increase as the number of allocated frames increases.
###### Optimal Page Replacement
An algorithm with a low page-fault rate will never suffer from Belady's anomaly.

Such an algorithm **does exist** and has been called **OPT** (or MIN). 
It is simply this:
<p style="text-align: center;">Replace the page that will not be used for the longest period of time.</p>
> Use of this page-replacement algorithm guarantees the lowest possible page-fault rate for a fixed number of frames.

For example, on our sample reference string, the optimal page-replacement algorithm would yield nine page faults, opposed to the fifteen of the FIFO algorithm: 
![[Pasted image 20240131130912.png|650]]
###### LRU Page Replacement
Unfortunately, the optimal page-replacement algorithm is difficult to implement, because it requires future knowledge of the reference string.
 As a result, the optimal algorithm is used mainly for **comparison** studies. 
###### LRU Page Replacement
If the optimal algorithm is not feasible, perhaps an approximation of the opti-
mal algorithm is possible. 

If we use the **recent past as** an **approximation** of the **near future**, then we can replace the page that has not been used for the longest period of time.
This approach is the **least recently used** (LRU) algorithm.

LRU replacement associates with **each page** the **time** of that page’s **last use**.
When a page must be replaced, LRU chooses the **page that** **has not** been **used** for the **longest** period of time.

Take into account the example reference string of the FIFO example.
Applying it with the LRU algorithm, we find out that it causes 12 page faults, which is better than FIFO but worse than OPT.

![[Pasted image 20240131131526.png|650]]

Despite this fact, the LRU policy is often used as a page-replacement algorithm and is considered to be good.
The major problem is how to implement LRU replacement, because it can require significant hardware overhead.

Two implementations are feasible:
- **Counters**
	- Every page entry has a counter; every time page is referenced through this entry, copy the clock into the counter
	- When a page needs to be changed, look at the counters to find smallest value
- **Stack**
	- Keep a stack of page numbers in a double link form
	- Whenever a page is referenced, it is removed from the stack and put on the top.
		- the most recently used page is always at the top of the stack
		- the least recently used page is always at the bottom
	- Removing a page and putting it on the top of the stack then requires changing six pointers at worst.
	- Each update is a little more expensive

> LRU replacement does not suffer from Belady’s anomaly.

###### LRU-Approximation Page Replacement
Not many computer systems provide sufficient hardware support for true LRU page replacement.

Many systems provide some help, however, in the form of a **reference bit**, which is set when a page is referenced.

Initially, all bits are cleared (to 0) by the operating system.
As a process executes, the bit associated with each page referenced is set (to 1) by the
hardware.
After some time, we can determine which pages have been used and which have not been used by examining the reference bits, although we do not know the order of use.
###### Second-Chance Algorithm
The basic algorithm of **second-chance replacement** is a **FIFO** replacement algorithm.

When a page has been selected, however, we **inspect** its **reference bit**:
- If the value is 0, we proceed to replace this page; 
- if the reference bit is set to 1, we give the page a second chance and move on to select the next FIFO page.

When a page gets a second chance, its reference bit is cleared, and its arrival time is reset to the current time.
> A page that is given a second chance will not be replaced until all other pages have been replaced.

One way to implement the second-chance algorithm is as a **circular queue**.
A **pointer** indicates which **page** is **to be replaced next**.
When a frame is needed, the **pointer advances** until it finds a page with a 0 reference bit. 
As it advances, it **clears** the **reference bits**.  Once a victim page is found, the page is replaced, and the new page is inserted in the circular queue in that position.

![[Pasted image 20240131134627.png]]

Second-chance replacement degenerates to FIFO replacement if all bits are set.
###### Enhanced Second-Chance Algorithm
We can enhance the second-chance algorithm by considering the reference bit and the modify bit  as an ordered pair. 

With these two bits, we have the following four possible classes:
1. **(0, 0)**: **neither** recently used nor modified—best page to replace
2. **(0, 1)**: not recently used but modified—not quite as good, because the page will need to be written out before replacement
3. **(1, 0)**: recently used but clean—probably will be used again soon
4. **(1, 1)**: recently used and modified—probably will be used again soon, and the page will be need to be written out to secondary storage before it can be replaced

When page replacement is called for, we use the same scheme as in the clock algorithm; but instead of examining whether the page to which we are pointing has the reference bit set to 1,
we examine the class to which that page belongs.

<p style="text-align: center;">We replace the first page encountered in the lowest nonempty class. </p>
#### Trashing
If a process does not have “enough” pages, the page-fault rate is very high

This high paging activity is called **thrashing**. 
A process is thrashing if it is **spending more time paging than executing**.

This leads to:
- low CPU utilization
- operating system thinking that it needs to increase the degree of multiprogramming
- another process added to the system
##### Cause of trashing
If CPU utilization is too low, we simply increase the degree of multiprogramming by introducing
a new process to the system.

When using a global page-replacement algorithm (replaces pages without regard to the process to which they belong), if a process request more frames, it starts faulting, taking frames from other processes, which start also to fault, because their frames have been overwritten.

Those faults will need to swap out the overwritten frames, requesting the use of the paging device, emptying at the same time the ready queue.

The CPU scheduler sees the decreasing CPU utilization and increases the degree of multiprogramming as a result. 
The new process tries to get started by taking frames from running processes, causing more page faults and a longer queue for the paging device.

As a result, CPU utilization drops even further, and the CPU scheduler tries to increase the degree of multiprogramming even more.
Thrashing has thus occurred.

This phenomenon is illustrated in the following picture.
As the degree of multiprogramming increases, CPU utilization also increases, although more slowly,
until a maximum is reached.
If the degree of multiprogramming is increased further, thrashing sets in, and CPU utilization drops sharply.

![[Pasted image 20240131161017.png|650]]
##### Working-Set Model
To prevent thrashing, we must provide a process with as many frames as it needs, which is difficult to estimate.
One strategy starts by **looking** at **how many frames** a process is **actually using**. This approach
defines the **locality model** of process execution.

<p style="text-align: center;">As a process executes, it moves from locality to locality.</b>
> A locality is a **set of pages** that are **actively used together**.
> A running program is generally composed of several different localities, which may overlap.

The **working-set model** is **based** on the assumption of **locality**.
This model uses a parameter($\Delta$) to define the **working-set window**, a fixed number of page references.

The idea is to examine the most recent $\Delta$ page references, which pages forms the **working set**.
If a page is in **active use**, it **will be in** the **working set**. **Otherwise**, it **will drop** from the working set
$\Delta$ time units **after** its last reference.

![[Pasted image 20240131162727.png|650]]

The accuracy of the working set depends on the selection of $\Delta$:
- If $\Delta$ is too small, it will not encompass the entire locality; 
- if Δ is too large, it may overlap several localities. 
-  if $\Delta=\infty$, it will encompass the entire program page history

We define the working-set size of a process $i$ as $WSS_i$, and
$$D=\sum WSS_i$$
the total demand for frames.

If the total demand is greater than the total number of available frames ($D > m$), **thrashing will occur**, because some processes will not have enough frames.
So if $D$ becomes greater, a process is usually suspended or swapped out.


###### Working Sets and Page Fault Rates
There is a direct relationship between the working set of a process and its page-fault rate.

The **working set** of a process **changes over time** as references to data and code sections move from one locality to another. 
Assuming there is sufficient memory to store the working set of a process (that is, the process is not thrashing), the page-fault rate of the process will transition between peaks and valleys over time. 

This general behaviour is shown below:
![[Pasted image 20240131163057.png|650]]

A peak in the page-fault rate occurs when we begin demand-paging a new locality. 
However, once the working set of this new locality is in memory, the page-fault rate falls. 
When the process moves to a new working set, the page-fault rate rises toward a peak once again.