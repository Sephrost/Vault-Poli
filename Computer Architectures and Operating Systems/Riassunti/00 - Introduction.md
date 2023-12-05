# Introduction
A modern architectures executes instruction via a processor, which is composed by one or more execution units(core), which fetch the data from the primary memory, decodes it and executes it to run a thread.

The instruction were once executed in order, but nowadays the instruction are fetched in order, executed out of order using multiple execution units and reservation station, which are buffers, and reordered by a reorder buffer to get the correct result of the computation.

The computer architectures have reached the point where physical constrains hinders the improvement of performance by making the hardware faster, so we had to resort to run multiple instruction by parallelizing the execution of instruction, with method such as pipelining and dynamic scheduling.
## Different kinds of internal storage
There are actually different types of architectures, which uses different ways to of handling the internal storage:
- **stack-based architecture**: the results of computation are stored on a stack(a LIFO data structure)
	- with this kind of memory storage, the operands are positioned implicitly on the top of the stack
- **accumulator-based architecture**: the results of computation are stored in an accumulator
	- the operands are implicitly the value of the accumulator itself, which is also the result
- **register-memory-based architecture**: the instruction of this architecture uses only an implicit operand
- **load-store-based architecture**: this architecture uses two implicit operation, and can only manage registers operations

![[Pasted image 20231103181105.png]]

The differences between these kinds of architectures becomes vert clear when a simple operation, such as $C=A+B$ is performed, as shown in the following picture.

![[Pasted image 20231005141306.png|650]]

As such, we can split these architectures into two kinds, based on the way operands are accessed and stored: one that can access the memory as part of the instruction(*register-memory* architecture) and one that can access it only with load and store instructions(*load-store* architecture).

> After 1980, every new architecture use load-store architecture, for two reasons: registers are faster than main memory and are easier for a compiler to use.

Another way to discern architectures is the number of memory operands used per ALU istructions.
# Instruction set Architecture
An **instruction set architecture** is the set of instruction which is the portion of the computer visible to the programmer or compiler.

Modern ISAs uses general-purpose registers to perform operations for two main reasons:
- registers are faster than memory
- registers are easier for a compiler to use
## Memory Addressing
An architecture *must* define how memory addresses are interpreted and how they are specified.
### Little Endian vs Big endian
There are two different convention for ordering the bytes within a larger object:
- Big Endian: the least-significant bit first
![[Pasted image 20231005145616.png]]
- Little Endian: the more significant bit first
![[Pasted image 20231005145603.png]]

> When operating within one computer, the byte order is often unnoticeable
### Memory alignment
A second memory issue is that in many computers, accesses to objects larger than a byte **must be aligned**.

We can store in memory large objects, an the access to those must be aligned: an access of $s$ bytes at a byte address $A$ is aligned if $A\mod s =0$.
![[Pasted image 20231005150239.png|600]]

> Misalignment causes hardware complications, because the memory is typically aligned on a multiple of a word or double-word boundary.
>
> Even in computers that allow misaligned access, programs with aligned accesses run faster.
### Addressing Modes
An architecture must specify how the address of an object is specified.

Addressing modes specify constants and registers in addition to locations in memory. When a memory location is used, the actual
memory address specified by the addressing mode is called the **effective address**.

The following figure shows and describes the most common names for the addressing modes.

![[Pasted image 20231005150557.png]]

Addressing modes have the ability to significantly reduce instruction counts.
They also add to the complexity of building a computer and may increase the average clock cycles per instruction (CPI) of computers that implement those modes.
Thus, the usage of various addressing modes is quite important in helping the architect choose what to **include**.

By carefully choosing the addressing modes, one can
obtain some important consequences:
- Reducing the number of instructions
- Increasing the CPU architecture complexity
- Increasing the average Cycles Per Instruction (CPI)
### Operations in the Instruction Set
Most ISAs can be categorized by the type of computation that they can carry out.

The operation supported by most ISAs are categorized in the following picture.

![[Pasted image 20231005151819.png]]

All computers generally provide a full set of operations for the *first three* categories. 
The support for system functions in the instruction set varies widely among architectures, but all computers must have some instruction support for basic system functions.


> One rule of thumb across all architectures is that the most widely executed instructions are the simple operations of an instruction set. This is because not all the instructions are executed at the same frequency.
### Types and sizes of Operands
To specify the type of an operand, the encoding of the opcode is use to designate it, and it's the most common way.

The most frequently supported data types:
- char (1 byte)
- half word (2 bytes)
- word (4 bytes)
- double word (8 bytes)
- single-precision floating-point (4 bytes)
- double-precision floating-point (8 bytes).
### Control flow instructions
We can distinguish four different types of control flow change:
- Conditional branches
- Jumps
- Procedure calls
- Procedure returns

> The terminology for conditional and unconditional branch is often inconsistent. So as a rule of thumb, the term *jump* is used when the change in control flow is unconditional, and *branch* when the change is conditional.
#### Addressing Modes for Control Flow Instructions
The destination address of a control flow instruction **must always be specified**. 

This destination is specified explicitly in the instruction in the vast majority of cases, with the exception of return routines, where the address in not known at compile time.

The most common way to specify the destination is to supply a displacement that is added to the program counter (PC). PC-relative branches or jumps are advantageous because the target is often near the current instruction, and specifying the position relative to the current PC requires fewer bits and allow the code to run independently of where its loadei(position independence).

### Encoding an instruction set
The encoding of the ISA does not affect only the size of compiled program, but also the implementation of the processor, which must decode the representation to quickly find the operator and its operands.

The operation is typically specified in one field, called the **opcode**.

Instruction Set Encoding depends on:
- which instructions compose the Instruction Set
- which addressing modes are supported

When a high number of addressing modes is supported, an address specifier field is used to specify the addressing mode and the registers which are possibly involved.
When the number of addressing modes is low, they can be encoded together with the opcode.

When encoding the instructions, the number of registers and the number of addressing modes both have a significant impact on the size of instructions, as the register field and addressing mode field may appear many times in a single instruction.

There are three main choices for encoding the Instruction Set.

The first is often called **variable**, because it allows virtually all addressing modes to be with all operations. 
This style is best when there are many addressing modes and operations.

The variable format can support any number of operands, with
each address specifier determining the addressing mode and the length of the specifier for that operand. 
It generally enables the smallest code representation, because
unused fields need not be included.

![[Pasted image 20231105180205.png|550]]

The second one is called **fixed**, because it combines the operation and the addressing mode into the opcode. 
Often fixed encoding will have only a single size for all instructions.
It works best when there are few addressing modes and operations.

![[Pasted image 20231105180543.png|550]]

The fixed format always has the same number of operands, with the addressing modes (if options exist) specified as part of the
opcode. It generally results in the largest code size. 
Although the fields tend not to vary in their location, they will be used for different purposes by different instructions.

