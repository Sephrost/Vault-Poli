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
Throughout the yeas, different kind of operative system architectures have been proposed. generally, there's no clear better one, but the suitability only depends on the use case of the system.
### Flat architecture
