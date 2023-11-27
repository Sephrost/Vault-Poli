Caches are small but high speed memories interposed between the processor and the main memory to reduce the latency of subsequent memory accesses.

Usually there are only a cache for both data and instructions, but in some cases they can be separated.
### Locality reference
Programs tend to reuse data and instructions they have used recently.

> A widely held rule of thumb is that a program spends 90% of its execution time in only 10% of the code.

To exploit this locality principle, it case used to predict with reasonable accuracy which instruction and date will be used in the near future.

Two different types of locality have been observed: 
- **temporal locality**: recently accessed items are likely to be accessed soon
	- if at time $t$ the program accesses to a given memory cell, it is highly probable that the program accesses again the same cell by the time $t_0 + \Delta_t$
- **Spatial locality**: items whose addresses are near one another tend to be referenced close together in time.
	- if at time $t_0$ the program accesses a memory cell with address $x$, it is highly likely that by the time $t_0 + \Delta t$ the program will also access the memory cell with address $X ± e$.

If the entire block is loaded in the cache at time $t_0$ (first access to a memory block), it is likely that for a certain time $\Delta_t$ the program will find in the cache all of the words it needs.
### Evaluating cache performance
As previously said, implementing a cache memory allows to reduce the latency of consequential memory accesses. 

Thus, we define a **cache miss** as an unsuccessful lookup into the cache, and a **cache hit** as a successful one.

The performance of a cache memory can be evaluated in terms of the ratio of cache hit/miss(where an higher rate of hit is obviously desired).

The average access time to the memory in a hierarchy implemented a cache is
$$Avarage\; memory\; access\;time=Hit\;time+Miss\;Rate\times Miss\; penalty$$
or 
$$h\cdot C+(1-h)\cdot M$$
where:
- $h$ is the cache hit ratio
- $C$ is the cache access time
- $M$ is the memory access time when the data is not in the cache

Usually, a normal value for this formula is in the order of $0.9$.
### Memory organization
A cache memory is organized in **lines**, or **blocks**, which is simply a collection of (adjacent) words.

> When a word is not found in the cache, it must be fetched from a lower level of the memory hierarchy and be placed in the cache, together with the adjacent words(which compose a block) for efficiency reasons: to take advantage of the locality principles.

Each cache line is associated with a **tag** field, which indicates the memory block present in the line at that time.

The cache is also managed by a **controller**, which intercepts the lookup request to the main memory to possibly return the block itself.

![[Pasted image 20231126172137.png|650]]
### Cache lookups
When the CPU requires the data located at memory address, the lookup should be first effectuated in the cache. 

For this goal, the memory address is at first divided in three portions:
- the **offset**, which indicates where the requested word is located in the data block of a cache line.
- an **index**, which identifies in which cache line the data should be stored
- a **tag**, used to determine the correct way in which the data is actually stored, and is also the $n$ more significant bits of the address.

![[Pasted image 20231126180130.png|650]]
### Cache position
The cache is normally located between the CPU and the main memory, but is more accurate to say that is located between the CPU and the bus.

This implementation allows to reduce the bus load and is compatible with a multiprocessor architecture.

![[Pasted image 20231126172906.png|650]]
### Cache size
Choosing the optimal size of the cache is very important for the system cost and the performance.

Bigger memories improves the system's overall performances, but makes the cache itself slower and more expensive.

Usually, the preferred cache sized spaces between a few kB to some MBs.
### Cache mapping
A key design decision is where blocks (or lines) can be placed in a cache. The most popular scheme is **set associative**, where a set is a **group** of blocks in the cache.

A block is first mapped onto a **set**, and then the block can be placed *anywhere* within that set.

The set is chosen by the address of the data:
$$(block\; address)\mod (number\; of \; cache\; set)$$
Another way to address the problem of cache placement is allow any memory location to be stored in any position of the cache. A cache that implements this approach is called *fully associative*, which is a particular case of set associative cache, where there's only one set withing one cache.

An opposite way to address the problem is also a particular case of set associativity, where one memory location can be mapped only to one location of the cache. This approach is called *direct mapping*, in which the size of a block is equal to one.

![[Pasted image 20231102132133.png|650]]

> In a fully associative cache, the index field used in a lookup is not used, only the tag is important.
#### Replacing algorithm
Now that we have explained how to place and retrieve the content of a memory location in the cache, we should talk about how a cache replaces it's blocks.

There are many possible approaches:
- LRU (Least Recently Used): the most used, not according to the teacher.
- FIFO (First-In First-Out): the cheapest
- LFU (Least Frequently Used): theoretically, the most effective, but really hard to implement in hardware in a way that requires a single cycle of clock.
- random: simple and effective.

![[Pasted image 20231126183207.png|650]]
##### Pseudo-LRU
Pseudo-LRU, o pLRU, is an efficient approximation of a LRU algorithm.

It allows to select an item that most likely has not been accessed very recently, given a set of items and a sequence of access events to the items in an efficient way.

With this technique, the age of the cache ways is arranged in a binary tree, where each node represent a history bit. To find the pLRU element, the tree is traversed according to the values of the flags:
- a value 1 represent that the left side has been referenced more frequently
- a value 0 the opposite

To update the tree with a value, it is necessary to traverse the tree to insert it, and update the path values during the traversal.

> The starting configuration is right updated more frequently.
#### Updating the main memory
The consistency between the content of the cache and the correspondent address in the main memory is always required.

As such, two main strategies are proposed.
##### Write-back
For each cache block, a flag (called *dirty bit*) is introduced, which remembers whether or not the block has been changed since it was loaded into the cache.

When a block is evicted from the cache and the *dirty bit is set*, the **block** is **copied** from the cache to the main memory.

Such strategy has a few disadvantages:
- the replacement is slower because it sometimes requires copying in the main memory the replaced block
- in multiprocessor systems there may be incoherence between the caches of different processors
- it may not be possible to restore memory data after possible system failures
###### Write-through
**Each time** the CPU performs a write operation, it **writes on both** the cache data and the main memory data.

The resulting loss of efficiency is limited by the fact that writing operations are usually much less numerous than reading ones.
#### Cache coherence
The consistency between the content of the cache and the correspondent address in the main memory is always required.

As such, two main strategies are proposed.
##### Write-back
For each cache block, a flag (called *dirty bit*) is introduced, which remembers whether or not the block has been changed since it was loaded into the cache.

When a block is evicted from the cache and the *dirty bit is set*, the **block** is **copied** from the cache to the main memory.

Such strategy has a few disadvantages:
- the replacement is slower because it sometimes requires copying in the main memory the replaced block
- in multiprocessor systems there may be incoherence between the caches of different processors
- it may not be possible to restore memory data after possible system failures
###### Write-through
**Each time** the CPU performs a write operation, it **writes on both** the cache data and the main memory data.

The resulting loss of efficiency is limited by the fact that writing operations are usually much less numerous than reading ones.