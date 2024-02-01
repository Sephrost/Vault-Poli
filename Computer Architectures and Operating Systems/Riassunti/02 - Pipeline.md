**Pipelining** is an **implementation technique** whereby multiple instructions are overlapped in execution.
It allows to take advantage of parallelism that exists among the actions needed to execute an instruction.

In a pipeline, different units (called **pipe stages** or **segments**) are completing different parts of different instructions in parallel. Thus, those stages are connected together to form a pipe.
### Throughput of a pipeline
The throughput of a pipelined processor is the **number** of **instructions** which exit the pipeline(completed) in the **time unit**.

All the pipeline stages are synchronized (they proceed to executing a new ask all together); the time for executing one step is called **machine cycle**, and normally corresponds to *one clock cycle*.

The length of the machine cycle is determined by the slowest stage.

If the stages are perfectly balanced, then the time per instruction on the pipelined processor, assuming ideal conditions, is equal to
$$\frac{Time\; per\; instruction\; on\; unpipelined\; machine}{Number\; of\; pipe\; stages}$$
and the throughput of the pipeline is equal to 
$$throughput_{underpipelined}\ast n$$
where $n$ is the number of pipeline stages.

Usually, however, the stages *will not* be perfectly balanced; furthermore, pipelining does involve some overhead. 
Thus, the time per instruction on the pipelined processor will not have its minimum possible value, yet it can be close.
### Performance issues
Pipelining increases the processor instruction throughput, but it does not reduce the execution time of an individual instruction. In fact, it usually slightly increases the execution time of each instruction due to overhead in the control of the pipeline.

It means that, an higher throughput indicates that a program runs faster, having a lower execution time, but no single instruction is running faster. This puts some limits to the pipeline, which are caused by:
- Imbalance among the pipe stages 
	- It reduces performance because the clock can run no faster than the time needed for the slowest pipeline stage.
- Pipeline overhead
	- pipeline register: add setup time, which is the time that a register input must be stable before the clock signal that triggers a write occurs, plus propagation delay to the clock cycle.
	- Clock skew: they are the maximum delay between when the clock arrives at any two registers
#### Pipeline Hazards
**Hazards** are situations that prevent an instruction in the instruction stream from executing during its designated clock cycle.

There are three classes of hazards:
- **structural hazards**: which arise from resource conflicts
- **data hazards**: which arise when an instruction depends of the result of a previous instruction
- **control hazards**: which depend depend on pipelining branches and other instructions that change the PC

Hazards in pipelines can make it necessary to stall the pipeline, which isn't ideal at all. To avoid it, allowing other instructions to run while the others are delayed, while the stalling instruction is suspended.

As such, a stall causes the introduction of a *bubble* in the pipeline.
##### Data Hazards
Data hazards occur when the pipeline changes the order of read/write accesses to operands so that the order differs from the order seen by sequentially executing instructions on an unpipelined processor. This can induce wrong results and nondeterministic behaviours.

There are three kind of data hazards:
- **Read After Write**: a read operation occurs before a write one in program order. Is the most common data hazard.
- **Write After Read**: a write operation occurs before a read one in program order. It is impossible in a simple five stage pipeline, but occurs when the instructions are reordered.
- **Write After Write**: two write operation occurs in a order different from the program one, leaving the register with a wrong stored value. It is impossible in a simple five stage pipeline, but occurs when the instructions are reordered.
###### An example of Data hazard(read after write)
Consider the pipelined execution of these instructions:
```c
add x1,x2,x3
sub x4,x1,x5
and x6,x1,x7
or x8,x1,x9
xor x10,x1,x11
```
All the instructions after the `add` use the result of the `add` instruction.

The pipelined execution is shown in the following picture:
![[Pasted image 20231117113253.png|650]]

The add instruction writes the value of x1 in the WB pipe stage, but the sub instruction reads the value during its ID stage, which results in a RAW hazard.

Unless precautions are taken to prevent it, the `sub` instruction will read the wrong value and try to use it, which is even nondeterministic!
###### Forwarding to avoid stalls
To solve data hazards, a technique called **forwarding** can be used. 

A special hardware in the datapath detects when a previous ALU operation should write the register corresponding to the source of the current ALU operation.
In this case, the hardware selects the ALU result as the ALU input rather than the value from the register file.

The hardware must be able:
- to forward a data from any of the previously started instructions (provided that they didn’t already write the data in its final location)
- not to forward anything, if the following instruction is stalled, or an interrupt occurred.

Looking back at the previous example of data hazard, we can observe that the result of the `add` instruction is not needed by the `sub` instruction until the result of the first instruction is actually available. Thus, it can be moved to where the `sub` needs it from the storage location of the `add` to avoid the stall.

![[Pasted image 20231117161640.png|650]]

In this case, forwarding works as follows:
1. The ALU result from both the EX/MEM and MEM/WB pipeline registers is always fed back to the ALU inputs.
2. If the forwarding hardware detects that the previous ALU operation has written the register corresponding to a source for the current ALU operation, control logic selects the forwarded result as the ALU input rather than the value read from the register file.

> we need to forward results not only from the immediately previous instruction but also possibly from an instruction that started two cycles earlier.

Forwarding can be generalized to include passing a result directly to the functional unit that requires it: a result is forwarded from the pipeline register corresponding to the output of one unit to the input of another, rather than just from the result of a unit to the input of the same unit.
###### Data Hazards requiring stalls
Unfortunately, not all potential data hazards can be handled by bypassing. In fact, some results of a previous operation in code order cant be available to be forwarded when needed. Thus, some data hazards cant be resolved only with hardware.

For reference, take in account the following snippet of code:
```asm 
ld  x1,0(x2)
sub x6,x1,x7
and x4,x1,x5
or  x8,x1,x9
```
the pipelined execution is the following:
![[Pasted image 20231117164415.png|650]]

We can observe that a forwarding path goes back in time, which is not possible on modern computers!

To persevere the correct execution patter a **pipeline interlock** has to be added. It detects hazards and stalls in the pipeline and stalls the execution until the hazard is cleared, introducing bubbles or stalling the execution completely.
##### Control Hazard
**Control hazards** are caused by branch instruction, both conditional and unconditional, which may, or not, change the program counter after the following instruction has already been fetched.

In the case of conditional branches, the decision on
whether the PC should be modified (branch taken) or not
(branch not taken) can be taken even later, because the instruction has not been decoded yet.

One stall cycle for every branch will yield a performance loss of 10% to 30% depending on the branch frequency.
###### Reducing Pipeline branch penalties
There are many methods for dealing with the pipeline stalls caused by branch delay, each of those ones being static: they are fixed for any branch during the entire execution.
###### Freezing the Pipeline
The simplest scheme to handle branches is to **freeze** or **flush** the pipeline, holding or deleting any instructions after the branch until the branch destination is known.

It is the simplest solution to implement.
###### Always predict not-taken
A higher-performance, and only slightly more complex, scheme is to treat **every branch as not taken**, simply allowing the hardware to continue as if the branch were not executed.

If the branch turns out to be taken, the effects of the wrongly executed operations are simply cancelled.

The following image explains how this schema works:

![[Pasted image 20231118160244.png]]

If the branch is not taken, determined during ID, we fetch the fall-through and just continue. Otherwise, we restart the fetch at the branch target. This causes all instructions following the branch to stall 1 clock cycle.
###### Always predict taken
An alternative scheme is to **treat every branch as taken**. As soon as the branch is decoded and the target address is computed, we assume the branch to be taken and begin fetching and executing at the target.

This buys us a one-cycle improvement when the branch is actually taken, because we know the target address at the end of ID, one cycle before we know whether the branch condition is satisfied in the ALU stage.

In either a predicted-taken or predicted-not-taken scheme, the compiler can improve performance by organizing the code so that the most frequent path matches the hardware’s choice.
For example, the predict not-taken scheme is suitable when a `for` loop has to be executed.
###### Delayed branches
A fourth scheme, which was heavily used in early RISC processors is called delayed branch.

This technique is based on **filling the slot after** the **branch instruction** (named *branch-delay slot*) with instructions which have to be executed no matter the branch outcome.

It is up to the compiler to fill each branch-delay slot with
the right instructions.
##### Structural hazards
**Structural hazards** may happen when some pipeline unit is not able to execute all the operations scheduled for a given cycle, for example when two instruction in the pipeline both need to access the memory in the same clock cycle.

This requires adding new hardware or improving the existing one.
The designer has to trade-off between performance and cost, basing on the frequency of occurrence of structural hazards
### Floating-point operations
Floating point units perform more complex operations than integer ones.

Therefore, in order to force them to perform their job in a single clock cycle, the designer should:
- either use a very slow clock, or
- make these units very complex.

As a popular alternative, floating point units generally require more than one clock cycle to complete.

The EX stage is composed of different functional units, and is repeated as many times, as the instruction requires.

![[Pasted image 20231118172559.png|550]]

Due to the different structure of the EX stage, hazards may become more frequent, especially structural hazards, which may occur for two reasons:
- because of the unpipelined divide unit, several instructions could need it at the same time.
- because the instructions have varying running times, the number of register writes required in a cycle can be larger than 1.


#### The MIPS R4000 pipeline
he MIPS R-4000 processor is a 64-bit microprocessor introduced in 1991, whose instruction set is similar to the MIPS64 one.

The R4000 implements MIPS64 but uses a deeper pipeline than that of our five-stage design both for integer and FP programs. This deeper pipeline allows it to achieve higher clock rates by decomposing the five-stage integer pipeline into eight stages.

The extra pipeline stages come from decomposing the memory access. Deeper kind of pipeline like this usually take the name of *superpipeline*.

The stages are described in the following image:

![[Pasted image 20231118180956.png|550]]

The function of each stage is as follows:
- IF: First half of instruction fetch; PC selection actually happens here, together with initiation of instruction cache access.
- IS: Second half of instruction fetch, complete instruction cache access.
- RF: Instruction decode and register fetch, hazard checking, and instruction cache hit detection.
- EX: Execution, which includes effective address calculation, ALU operation, and branch-target computation and condition evaluation.
- DF: Data fetch, first half of data cache access.
- DS: Second half of data fetch, completion of data cache access.
- TC: Tag check, to determine whether the data cache access hit.
- WB: Write-back for loads and register-register operations.

> In addition to substantially increasing the amount of forwarding required, this longer-latency pipeline increases both the load and branch delays.

The MIPS architecture has a single-cycle delayed branch. 
The R4000 uses a predicted-not-taken strategy for the remaining two cycles of the branch delay. Not-taken branches are simply one-cycle delayed branches, while taken branches have a one-cycle delay slot followed by two idle cycles.
##### The floating-Point pipeline
The R4000 floating-point unit consists of three functional units: 
- a floating-point divider
- a floating-point multiplier
- a floating-point adder.

> Double-precision FP operations can take from 2 cycles (for a negate) up to 112 cycles (for a square root).

The Floating point eight stages are described in the following table:

Stage |Functional unit|Description
--|--|--
A|FP adder|Mantissa add stage
D|FP divider|Divide pipeline stage
E|FP multiplier|Exception test stage
M|FP multiplier|First stage of multiplier
N|FP multiplier|Second stage of multiplier
R|FP adder|Rounding stage
S|FP adder|Operand shift stage
U| |Unpack FP number
