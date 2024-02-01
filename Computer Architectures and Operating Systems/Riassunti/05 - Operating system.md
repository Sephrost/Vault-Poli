Embedded systems are made up of many different components, like the CPU, the memory and the various I/O devices. Each one of those provides different functionalities that can be used trough programs.
To use those functionalities, application developers should know how each component work to make the most of it, which is quite irrealistic. The operation system role is to abstract away part of this complexity, by providing an abstraction layer that allows to simplify the increasingly complexity of the modern hardware, allowing at the same time to control the system trough the use of interfaces.

A  basic software is thus composed of 
- the **operating system code**, necessary to implement services using the hardware, such as:
	- **CPU manager**, which implements algorithms to optimize the usage of the CPU time 
	- **Memory manager**, which implements algorithms to satisfy the memory demands of application
	- **File manager**, which provides a unifies access to the persistent storage
	- **Device manager**, which implements service routines for the I/O peripherals 
	- **Hw-specific services**, which implements CPU-specific operations, for example context switches
- **System-call interface**, which is an application programming interface to access the services provided by the rest of the basic software

The stack that has just been described is represented in the following picture

![[Pasted image 20231212140717.png]]
## Operating system architecture
Throughout the yeas, different kind of operative system architectures have been proposed. Generally, there's no clear better one, but the suitability only depends on the use case of the system.
### Flat architecture
A flat architecture OS is an operating system intended to provide the most of the
functionalities in the least space.

![[Pasted image 20240131163518.png]]

The components of the operating system are essentially functions that any application can invoke, and there is no clear separation between the application an the OS.

This means that malfunctions can freely propagate corrupting the system.
### Monolithic kernel
A monolithic kernel OS is an operating system divided into a number of layer, each one uses functions and services provided by the lover layers.

Each layer makes use of a dedicated virtual address space.
All the services are delivered by a single executable.

> An example is the linux os.

![[Pasted image 20240131163530.png]]

If a driver must be loaded in the kernel it can either be linked to it, and be available on the next boot, or inserted in the kernel space at runtime.

With this approach, malfunctions in the application cannot propagate to the kernel, but malfunctions in the O.S. components can corrupt the whole system.
### Microkernel architecture
A microkernel OS is based on the concept of moving as much from the kernel into user space.

Each component/application operates in a dedicated virtual address space.
In this way, it is:
- easier to extend a microkernel
- easier to port the operating system to new architectures
- More reliable (less code is running in kernel mode)
- More secure
but it has some performance overhead on the user space to allow communication with the kernel.
![[Pasted image 20240131164549.png|500]]

> Microkernels can be better validated than monolithic kernel as much smaller.

![[Pasted image 20240131164635.png]]