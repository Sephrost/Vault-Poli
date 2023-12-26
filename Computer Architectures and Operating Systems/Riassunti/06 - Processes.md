A **process** is a program in execution on a system, which is executed in sequential fashion(referring to the instructions that compose it).

A process includes:
- some processor registers, which includes the program counter and the processor status word 
- the program memory area, which contains the 
- Data memory area, which contains:
	- the constant data 
	- the Initialized data 
	- the Non-initialized data 
- the stack area
- the heap area

In general, the process memory structure can be summarized with the following table:

|Memory Area|Section|Section Type|Write Operation|Initial Value|Contents|
|---|---|---|---|---|---|
|Program area|.text|Code|Disabled|Yes|Stores machine codes.|
|Constant area|.rodata|Data|Disabled|Yes|Constant data. This section may not be produced, especially for host compilers (e.g. UNIX/PC)|
|Initialized data area|.data|Data|Enabled|Yes|Initialized global and static data.|
|Non-initialized data area|.bss|Data|Enabled|No|Stores global data whose initial values are not specified (zero initialized). BSS "Block Started by Symbol"|
|Stack area|||Enabled|No|Required for program execution. Dynamic Area Allocation.|
|Heap area|||Enabled|No|Used by a library function (malloc, realloc, calloc, and new). Dynamic Area Allocation.|
## Process in memory: an example
To further understand how a process is stored into the main memory, take into account the following C code:
```c
const int alfa=25;
int beta = 44;
char tmp; 

int foo(int X) {
	char *ptr;
	ptr = (char *)malloc(X);
}
```
Obviously, the code as a whole is stored in the program area of the process, but when it is running, the outcome of the various instructions is stored in different portion of the allocated memory.

Furthermore, each of the declared variables is allocated in a different portion of the memory:
- `alpha` is stored in the constant area
- `beta` is stored in the initialized data area
- `tmp` is stored in the non-initialized data area

The function `foo`, when called, is loaded onto the stack to allow linking and execution, whereas the memory area which is reserved by the `malloc` call is located in the heap.

In general, the memory view of the process in RAM during the execution is as follows:
![[Pasted image 20231224152349.png]]
## Process states
During its lifetime, a process continuously **changes state**:
- **New**: The process is being created 
- **Running**: Instructions are being executed 
- **Waiting**: The process is waiting for some event to occur 
- **Ready**: The process is waiting to be assigned to a processor 
- **Terminated**: The process has finished execution

To determine when the state changes, it is used the Process State Diagram as a reference:
![[Pasted image 20231224152904.png|600]]

At any given moment, it is pretty common that more than one process are loaded in the main memory.
Given $N$ processes, and one processor, at any given time:
- only one process is in the running state
- $M$ processes can be blocked waiting for a resource to become available to resume the execution
- $N-M-1$ are ready to be executed waiting to access the processor

This picture better depicts the state changes that happens during a multi process execution and the events that can cause a state change: 
![[Pasted image 20231224153542.png|600]]

In general:
- Transition 1 occurs when a **process** discovers that it **cannot continue**
	- For example it needs to use a portion of shared memory a now-ready process reserved for its own use
- Transitions 2 and 3 are **caused** by the **operating system**
	- Preemptive scheduler: process is moved from running to ready after a certain time quantum (time slice) is expired 
	- Cooperative scheduler: process voluntary moves from running to ready
- Transition 4 occurs when the **event** the process **was waiting** for is **occurred**
	- For example the running process sets free the shared memory it previously locked, which the blocked process was waiting for
## Process Control Block (PCB)
When loaded in memory, a little bit of overhead is necessary to store the information about the process execution and the aspects that it concerns.
Those informations are stored in a **Process control block**, which describes each process, and in particular
- the process state 
- the program counter 
- the CPU registers 
- the CPU scheduling information 
- the Memory-management information
- the accounting information 
- the I/O status information

> One PCB is maintained for each process

![[Pasted image 20231224154520.png|600]]
