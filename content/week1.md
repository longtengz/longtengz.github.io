Title: Architectural Review
Date: 2015-10-18 10:20
Modified: 2015-10-18 19:30
Category: CourseNotes
Tags: OS, Computer Architecture, CS519
Authors: Teng Long 


#### Basic Computer Structure (Von Neumann Machine)

A computer with Von Neumann architecture stores instructions and data in the same memory whereas a **Harvard architecture** has separate memories dedicated for instructions and data. Basically, all the computer does is **fetch** data and instruction from the same memory, **decode** them, and **execute** them.

Due to the competetion between data and instruction fetching from the same memory, Von Neumann computers often encounter **Von Neumann bottleneck** which can sort of be alleviated by providing separate caches for data and instructions like most modern computers do.

CPUs load data and instructions from memory to registers, operate using registers(which is way faster than memories), save results to memories. And compilers optimize the use of registers to make CPUs process faster. Also compilers need to worry about the **addressing modes** of computer architectures.


##### Addressing Modes TODO

##### Turing Machine

Turing Machine is just a hypothetical machine invented by Alan Turing. It operates on infinite tapes like today's computer operates on memories. It's only a model that defines a device which can be used to express any arbitrary computation. An advanced version of Turing Machine would be a Universal Turing Machine which is considered by some people to be the predecessor of Von Neumann architecture. The Universal Turing Machine is one special Turing Machine that can simulate any other Turing Machine. You can think of it as a more general purpose one of Turing Machine. Regular Turing Machine can only be constructed to be facilated on one specific task, though it's defined to be able to compute arbitrarily. Universal Turing Machine has the ability to read in any configuration/instructions of one Turing Machine it needs to simulate, and starts to simulate.


##### Stored-program Computer? TODO


---------------------------------------------------

#### Memory Hierarchy


##### How does cache work? Terms in cache?

| Tag | Set Index | Block Offset |
| ---| ---| ---|

* tag

Tag says which address from main memory this piece of data comes from. Why using tags? Because memory is bigger than cache, in order for cache to cache any data from abitrary location of memory, we need to come up with a way to distinguish the origin of different data. And using tag is one way!

For example, in a fully associative cache, we have to compare the address of data in question with all tags in cache.

If the size of the cache entry (block size) is 4 bytes, then if we start from address 0. Then every block will have the address with last 2 bit being 00. So in this way, we don't have to compare all the 32-bit address with tag, we only need to compare with the first 30-bit now.

It seems like if we increase the size of each cache line (block), we might decrease the amount of comparison we need to make. However, now we have to use more bits to tell which piece of data (that is of size smaller than block size) is in the cache line.

* set index

If we have a fully associative cache, we have to compare every cache entry with the address in question to see if what we want is in the cache. That is not very efficient if cache has a lot of entries. There is a simple solution to that like in the search problem. We divide a cache into a number of sets. Each set stores a proportional data from memory. We use the middle bits of an address to designated which set a data should go to. And thses middle bits are set index.

Instead of compare each tag with an address, now we first determine which set should have this address by matching the middle bits with set index. Then we do a comparison between higher bits in the address and tag.

* block offset

Block offset specifies which data in a cache line (block) is needed. Often, we want block size to be big (but not as that big) and also to naturally align the [word][word_wiki] size. For example, if we have 4 words in a cache line, then that's 16 bytes of data, so when we request any data in this block range, the whole block will be dragged into cache. And this is cache taking advantage of spatial locality. So it's very common to have multi-words cache line.


* cache line

Cache line, cache entry and block are used interchangeably to mean one item stored in a set.


##### Principles of Cache

* Temporal locality

What's has been used recently has a higher chance to be reused again.

* Spatial locality

Due to some data structures used in programs, like arrays, some data are very likely to be used after its neighbor has been used before.


##### Fully Associative Cache vs. Set Associative Cache vs. Direct Mapped Cache

Fully Associative Cache is that you have to compare every cache entry.

Set Associative Cache is that you first determine which set your data belongs and make comparisons in that specific set.

Direct Mapped Cache is that you only have to do one comparison because now every set only has one cache line. If the higher bits of the address and the tag associated with that set don't match, then you have to fetch that data from memory. The disadvantage to this scheme is that you'll find

#### What's the problem with direct mapped cache?


##### Type of Misses

* Compulsory miss (cold miss)

Like its name suggests, you cannot avoid this type of misses which occured when you first reference some new data that you never process them before. For example when you boot your PC, you'll get a miss for every data you started accessing when your computer starts up, but after a while those data region will no longer suffer compulsory misses because they maybe already in the cache.

* Capacity miss

Because cache is expensive and only has a limited amount of space to cache data from memory. So if your program needs a lot of memory or say your program's **working set** is way large than the cache can offer, your cache will suffer from capacity misses. That is it continuously get misses because your program needs to much memory and it will kick out those oldest data and replace with what has just been brought in by your program. Simply put, cache cannot contain all the data you need for your entire program.

* Conflict miss

In the case of set associative and direct mapped cache, most data will have to share a spot in the cache. So it's very likely that several data shares same block in the cache will constantly kick each other out and results in forever misses and never get a hit.


##### Write Back Cache vs. Write Through Cache

These two are different in the write policy of a cache, which means it stimulates a different timing of writes to main memory whenever data is written to cache.

A **write through** cache forces every write to main memory.

A **write back** cache will use a **dirty bit** to mark an entry that's been written to the cache, and only writes back to memory if that entry is kicked out from cache. That is whenever cache decides to kick out an entry, it checks whether that entry is marked **dirty**. If it is, then writes back to memory. Otherwise, just replace it. In this case, if a dirty entry is kicked out by a read (which means there is a read miss), it needs two memory accesses to accomplish a read instruction. Whereas in write through, you don't have to write back the dirty entry(since it doesn't have one), you only need to read in from memory and replace what's in cache.


##### Virtually Addressed Cache vs. Physically Addressed Cache

What are the advantages and downsides of the following 4 schemes?

What happens on context switch?

What about virtual memory aliasing?

So what's wrong with physically addressed caches?

* Physically indexed, physically tagged

This scheme is kind of slow because cache can only be accessed after virtual address is resolved to physical address by TLB.


* Virtually indexed, virtually tagged

This scheme causes various **aliasing** and **homonyms** problems.


* Virtually indexed, physically tagged

It has lower latency than PIPT because now looking up in TLB and cache can happen in parallel and it can detect homonyms.


* Physically indexed, virtually tagged

Only thoretical.

##### Aliasing and Homonyms? TODO

--------------------------------------------------------

#### I/O


If all CPU does is fetch-decode-execute, then how does the program running on it affect I/O? Computers are useless without I/O.

##### Memory-mapped I/O

Memory-mapped I/O uses some portion of memory to map I/O operations. Then read and write from memory-mapped I/O would be just as simple as read and write memory. One disadvantage is that accessing I/O in memory could really slow down real memory access. But merits are accessing I/O becomes easy.

The contrast to this approach is **port-mapped I/O**. Port-mapped I/O is often controlled by CPU via a dedicated I/O bus instead of sharing the same data bus with main memory. Thus, it needs another set of instructions to access and instructions are very limited both in number and function.


Modern computers use a combination of these two methods? Why? TODO


##### Polling vs. Interrupt

Polling is constantly asking whether I/O is ready for further processing. So polling is expensive.

Interrupt is asynchronous whereas polling is synchronous. What does this means is that you wasting CPU processing time while polling. On the other hand, CPU never has to wait for an interrupt, it's only signaled by the interrupt once I/O is ready. In the meantime, it can process other computations. So interrupt is considered async.

For a hardware interrupt, a hardware singal (either a level trigger or a edge trigger) is sent to the CPU to force CPU to stop whatever it's doing and run a special **interrupt handler** for this interrupt. After handler is finished, CPU goes back to where it has left.

##### Programmed Input/Output (PIO)

PIO is a way of transferring data between memory and IO via CPU. Basically, programs running on CPU will issue some instructions to access Memory-mapped I/O to perform data transfer. And because I/O is way slower than CPU, most of the time CPU has to wait for I/O to respond. And during that period of time, CPU can do nothing. So it's not efficient.


##### Direct Memory Access (DMA)

With DMA, I/O can talk to memory directly without having to access CPU the whole time while transferring data and in the end blocking CPU from doing anything else. And with DMA, programs on CPU now can issue a data transfer from memory to I/O and leave the job to memory and I/O themselves. So CPU can work on others things. When transfers complete, DMA controller will issue an interrupt to CPU to signal transfer completion. So DMA is considered more efficient than PIO.



[word_wiki]: https://en.wikipedia.org/wiki/Word_(computer_architecture) "Word (computer architecture) - Wiki"
