**ARM** is a family of RISC instruction set architectures for computer processors.

The ARM processor was first developed (between 1983 and 1985) by Acorn Computers, with several versions introduced since. 
Today, ARM cores are widely popular among SoC designers, mainly because they show a very good trade off between performance and power consumption.
## Arm architecture
The arm datapath is represented in the following picture.

x registers are available, with two read ports and one write ports, with an additional write port reserved for the 15th register.

![[Pasted image 20231207155638.png]]
### Instruction execution
when an instruction is executed, the following happens:
1. The two operands are read from the registers(R$n$ and R$m$)
2. One operand is possibly rotated if needed for more complex operators
3. The ALU then generates the result
4. The result is written to register R$d$
5. A further instruction is fetched from memory
6. The PC is finally updated

![[Pasted image 20231207160640.png]]

From this prospective, it is possible to notice that the fetch, decode and execute stages are carried out in the same stage of the pipeline.
### Data transfer instructions (Load and store)
The instruction with require to fetch some data from the registers actually requires two clock cycles for the execution stage.

In the first clock cycle, the the address is computed using one register and one immediate, whereas in the second one the memory is actually accessed.
### Branch instructions
Branch instructions too require two clock cycles.

In the first one, the target address is computed by adding and immediate value(which is also shifted by two positions) to the program counter. In the second one, the pipeline is flushed to be filled again.

In case of jumps to a subroutine, a further clock cycle is needed to save the return address to the special address $R14$. During this time the pipeline is filled again.

![[Pasted image 20231207162217.png|550]]
## Arm ISA
In an arm ISA, all the instructions are 32 bit long and can be unconditionally executed.

Arm is also a **load-store architecture**, diving the instructions in memory access ones and ALU operations and managing only registers operations.

This architecture also uses the three operand format.

> It is also possible to extend the instruction set via preprocessing techniques, converting the added instruction before execution.
### The Cortex-M3 Register set
Take into account the Cortex-M3 register set.

It uses 18 32-bit wide registers, that support only 3 types of data:
- byte(8 bits)
- half word(16 bits)
- word(32 bits)

> This paragraph only purpose is to give an insight of how a ARM register set is structured. Shouldn't be part of the exam.
### Program counter
As explained before, all instruction are 32 bits long. Thus the must be word aligned(start on the first bit).

For this end, the Program counter value is stored in the the bits in range \[31:2], with the bits \[1:0] equal to zero.

In an ARM architecture, it i also possible to overwrite he PC with an arbitrary value when necessary.

The program counter is also stored in the 15th register.
### The link register
The link register is used when a call to a subroutine has to be executed, meaning that is necessary to store the return address somewhere. Thus, the 14th register is used at this end.

To return from a linked branch, is used the instruction `MOV r15,r14`, or `MOV pc, lr`.
### The stack pointer
The 13th register is used as the stack pointer.

It is automatically updated at boot(so no additional instruction required), retrieving the value from the vector table, and during the program execution if a stack oriented instruction is executed.
#### Processor operating modes and levels
The processor can run a program in two modes:
- **thread mode**, which is used on reset or after an exception
- **handler mode**, which is used when an exception occurs

Different programs can also run with two distinct access level to the hardware:
- **user mode**, with limited access to the resources
- **privileged level**, with full access to the resources.

A program which runs in handler mode is always privileged.
## Interrupt controller
The main function of a Input/Output (I/O) system is to exchange information with the external world. it has to be controlled by the CPU, which has to intercept the service requests and handle them.
#### System events categorizations
The events that a system has to handle can be categorized as follows:
- Respond to infrequent but important events, such as an error or alarm condition.
- I/O synchronization, such as a trigger interrupt when signal on a port changes.
- Periodic interrupts
- Data acquisition samples ADC

There are 2 main approaches to handle I/O devices:
- **polling**, which does not require specific hardware
- **interrupt**, which does require it
#### Polling
Polling is the simplest approach. The CPU constantly asks every external device if it needs an I/O operation. Thus, it is usually implemented as a software cycle.

The CPU see the external devices as status register, and has to map them to a memory address. So part of the system memory addresses is reserved to accommodate those values, which are checked on regular basis.

This approach wastes a lot of CPU cycled just to check, making it power inefficient and reducing performances.
#### Interrupt
This is a more efficient approach, because the external devices interact directly with the CPU, making an I/O operation request directly to the computing unit, which, at that moment, can even be in IDLE mode.

When a request is received, the CPU needs to recognize the source of request in order to execute the proper handler. Thus, a data structure, which is a table, is initialized at boot time. This solves the problem of address translation for each I/O device. The system also implements an **interrupt controller**.

![[Pasted image 20231210163514.png|550]]

Interrupts are generally a problem: they are asynchronous, so they can be detected at any point. An interrupt is generally equivalent of a jump instruction. The CPU has to, at first, conclude the execution of the instruction that is altering the architectural state(eg: a instruction in the WB state). After that the following instruction in the program flow has to be discarded.
##### System setup for interrupt mode
To handle I/O operation in interrupt mode, the system has to some work to handle at boot time:
- it initializes an **interrupt handler table**, in which each line represent a different interrupt line(one for each handler). Each line stores the reference to a handler function that has to be executed in case of interrupt.
	- Eventually, it is possible to use additional memory to store a flag variable that can be used as a semaphore that can interrupt the flow of the running program.
- it configures the **interrupt controller**, to enable each interrupt sources an set their priority to handle simultaneous interrupt signals.

Every time a interrupt routine is called, during or after the handle event, the CPU has also to **clear the flags** that indicate the interrupt is active. This can be done in different parts of the interrupt service routine, which may be relevant for nesting interrupts.