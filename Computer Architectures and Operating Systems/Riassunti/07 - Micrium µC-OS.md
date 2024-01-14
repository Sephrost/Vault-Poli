**Micro-Controller Operating Systems** (**MicroC/OS**, stylized as **μC/OS**, or **Micrium OS**) is a real-time operating system (RTOS) that is based on a flat architecture and written in ANSI C. It is a royalty-free RTOS that is licensed on a per-end-product basis. 
Micrium µC/OS is preemptive and deterministic, making it ideal for use in safety-critical systems. 
It has a large user base and is used in hundreds of products all over the world, also thanks to its extensive documentation and support.

> The teacher literally copy-pasted chunks of the book.
> The manual for micro-c/os can be found [here](https://www.analog.com/media/en/dsp-documentation/software-manuals/Micrium-uCOS-III-UsersManual.pdf)
## Code structure
The code structure of a MicroC program is divided into different portions:
- **Application code:** The application code consists of project or product files. For convenience, these are simply called `APP.C` and `APP.H`, however an application can contain any number of files that do not have to be called APP.\*. 
	- The application code is typically where one would find the main function.
- **CPU**: Semiconductor manufacturers often provide library functions in source form for accessing the peripherals on their CPU or MCU. These libraries are quite useful and often save valuable time.
	- Since there is no naming convention for these files, \*.C and \*.H are assumed
- **Board Support Package (BSP):**  is code that is typically written to interface to peripherals on a target board. For example such code can turn on and off Light Emitting Diodes (LEDs), turn on and off relays, or code to read switches, temperature sensors, and more.
- **µC/OS-III:** This section contains part of the µC/OS-III real-time operating system (RTOS), in particular the processor independent portion. This provides a number of services that are essential for developing real-time embedded systems, such as task scheduling, memory management, and device management.
- **µC/OS-III/CPU**: This section contains the other part of the RTOS, in particular the CPU dependent code. This provides some essential services, such as the code for saving/restoring process context, or enable and disable interrupts.
- **µC/LIB**: a set of C library functions that are specifically designed for microcontrollers. These functions provide a variety of commonly used operations, such as memory copy, string manipulation, and ASCII conversion
- **Configuration files**: files containing settings or parameters that can be used to customize the behaviour of the µRTOS. The configuration file is typically read by the µRTOS when it starts up, and it is used to set various parameters, such as setting idle task stack size, tick rate, and the size of the message pool

![[Pasted image 20231224174856.png|550]]
## Process model
First of all, in µC/OS the **process** is referred to as **task**.
Taking this into account, a task code is a C function consisting of an **endless loop**. 
Each task has **its own stack** and is associated with a **task control block** (*TCB*), which contains information about the task, such as its state, priority, and stack pointer.

Tasks are created using the `OSTaskCreate()` system call, which takes as arguments:
- **the pointer to the Task Control Block (TCB)**: The TCB is a data structure that contains information about the task, such as its state, priority, and stack pointer.
- **the sorting arguments with the name of the task**: This argument is used to sort the task list. A lower value means that the task will be scheduled sooner.
- **the pointer to the task function**: This is the function that will be executed by the task.
- **the pointer to the priority of the task**: This argument specifies the priority of the task. Higher priority tasks are scheduled sooner than lower priority tasks.
- **the base address of the task stack**: This argument specifies the base address of the task's stack. The stack is used to store the task's local variables and function call stack frames.
- **the amount of stack space before the stack is full**: This argument specifies the amount of stack space that is allocated to the task.
- **the options for task creation**: This argument specifies various options for task creation, such as whether to check the stack usage or clear the stack on task creation.
- **the clear stack on task creation**: This argument specifies whether to clear the stack on task creation.
- **the variable storage errors**: This argument specifies a pointer to a variable where any errors that occur during task creation will be stored.
![[Pasted image 20231224183940.png|550]]
An example of a task is the following:
```c
void MyTask (void *p_arg) { 
	// Do something with “p_arg”.
	while (1) { 
		/* Task body */ 
	} 
}
```

When a task is created, the operating system allocates memory for the task's stack and TCB. 
The task's stack is used to store the task's local variables and function call stack frames, and is a global array of type `CPU_STK`. 
The TCB is used by the operating system to manage the task, and is actually a global variable of type `OS_TCB`.
## Semaphores
Semaphores in micrium µC/OS are synchronization mechanisms used to control access to shared resources. 
They are defined as **global variables** of data type `OS_SEM` and created using the `OSSemCreate` system call.
![[Pasted image 20231224184444.png|650]]
To block a calling task until the semaphore becomes available or until the timeout period expires the `OSSemPend` system call is used:
![[Pasted image 20231224184734.png|650]]
To to signal a semaphore, the `OSSemPost` system call is used:
![[Pasted image 20231224185013.png|650]]
### An example of semaphore usage
```c
// Define a semaphore to protect the shared resource.
OS_SEM g_SharedResourceSemaphore;

// Initialize the semaphore.
OSSemCreate(&g_SharedResourceSemaphore, 1, NULL);

// Task A.
void TaskA(void *p_arg) {
  // Acquire the semaphore to protect the shared resource.
  OSSemPend(&g_SharedResourceSemaphore, OS_WAIT_FOREVER);

  // Access the shared resource.

  // Release the semaphore to allow other tasks to access the shared resource.
  OSSemPost(&g_SharedResourceSemaphore);
}

// Task B.
void TaskB(void *p_arg) {
  // Acquire the semaphore to protect the shared resource.
  OSSemPend(&g_SharedResourceSemaphore, OS_WAIT_FOREVER);

  // Access the shared resource.

  // Release the semaphore to allow other tasks to access the shared resource.
  OSSemPost(&g_SharedResourceSemaphore);
}
```
## Timer
Timers are used to associate actions to time instants. There are two types of timers in µC/OS:
- **Periodic timers:** Periodic timers are configured to generate an interrupt at a regular interval. 
- **One-shot timers:** One-shot timers are configured to generate a single interrupt after a specified delay. 

To use a timer in µC/OS, the task must first create the timer using the `OSTmrCreate` system call. 
It takes the following arguments:
![[Pasted image 20231224185900.png|650]]

Once the timer has been created, the task can start it using the `OSTmrStart` system call, which takes the following arguments:
- **Pointer to the timer:** This is a pointer to the timer that the task wants to start.
- **Error pointer:** This is a pointer to a variable where any errors that occur during the OSTmrStart system call will be stored.
![[Pasted image 20231224190038.png|450]]

> In micrium OS, a timer depends on the frequency of the OS timer signal, that being how often the OS timer signal is called. This is configurable by the parameter `OS_CFG_TMR_TASK_RATE_HZ`.
> If the OS timer signal is called every 1/10 of a second, then the period of a timer specifies the number of 1/10 of a second before the timer repeats.
## Events
**Events** are a powerful tool for implementing synchronization and communication between tasks in Micrium OS. Events can be used to implement a variety of tasks, such as signalling that a resource is available.

To create an event, you can use the `OSFlagCreate` function:
![[Pasted image 20231226120108.png|650]]
Once a flag group has been created, you can set and clear events using the `OSFlagSet` and `OSFlagClear` functions.
![[Pasted image 20231226121042.png|650]]

Tasks can also wait for events to be set using the `OSFlagPend` function
![[Pasted image 20231226121222.png|650]]
If the flag is not set before the timeout expires, the `OSFlagPend` function will return an error. Furthermore, some of the possible flags that can be set are:
- `OS_OPT_PEND_FLAG_CLR_ALL`: wait until all bits in the event are cleared (0)
- `OS_OPT_PEND_FLAG_CLR_ANY`: wait until any bit in the event is cleared (0)
- `OS_OPT_PEND_FLAG_SET_ALL`: wait until all bits in the event are set (1)
- `OS_OPT_PEND_FLAG_SET_ANY`: wait until any bits in the event are set (1)

It is also possible to get the events that were previously posted using the `OSFlagPendGetFlagsRdy` call.

Here is an example of how to use events in Micrium OS:
```c
// Create a flag group to signal that a task has completed.
OS_FLAG_GRP *p_flag_grp = OSFlagCreate(NULL, 0, "Task Completed", NULL);

// Start the task.
OSTaskStart(p_task);

// Wait for the task to complete.
OS_ERR err;
OSFlagPend(p_flag_grp, 0, OS_WAIT_FOREVER, &err);

// Check for errors.
if (err != OS_ERR_NONE) {
  // Handle the error.
}
```