Title: Processes, Threads & Synchronization
Date: 2015-10-19 17:29
Modified: 2015-10-19 17:30
Category: CourseNotes
Tags: OS, Threads, CS519
Authors: Teng Long 


#### The Unix Time-Sharing System

##### No locks in file system on Unix?

Actually, locks are not mandatory in file system on Unix, and Unix uses advisory locking instead of mandatory locking like on Windows. Think of advisory locking as you don't have to lock the files if you don't want to, but it's advisory to do so. It's kind of like how you would use mutex to provide mutual exclusion, the OS doesn't enforce you to use mutex, but somehow developers would use it themselves to prevent race condition. It's the same here with file locks on Unix. File locks under Unix are by default advisory. Check out this [wiki][file_lock] and [SO question][file_lock_so].


##### UIDs

* Effective UID
* Real UID
* Saved UID
* File system UID

**Effective UID** is used as the effective identifier of a user for access checks. **Real UID** is pretty self-explanatory and it means the real UID of a user instead of an UID of an elevated privilege. **Saved UID** is often used to save the UID of an elevated privilege in order to temporarily go back as an unprivileged user to do some unprivileged work. **File system UID** is almost always the same as effective UID unless some programs (like the NFS server) explicitly change it. And file system UID is no longer necessary since kernel 2.0 but still lingers for compatibility.


##### Computer Security Model

* Access control list
* Bell-La Padula model
* Capability-based security

##### Pipeline and Filter

Filters are programs that process on a stream of data. For exmaple, a filter program can get its data from stdin and writes its output to stdout.

A pipeline is a series of filters that are strung together with the pipe operator `|` to filter stream of data by each filter.

For example:

```bash
ps -ef | grep sshd | ls
```

xargs?  <! TODO >


Linux has no threads? All it ever has are processes.

----------------------------------------------------------

#### Process

##### What is a process?

A process is an instance of execution of a program. It not only includes the program it's executing, but also contains the executing context (e.g register states, address space etc.).

##### Reason for multiple processes in single-CPU and many-core

In the past, people want concurrency even if it's in a serial fashion. Becauso some program are I/O bound, it's not efficient at all to allow a program to wait for I/O operation while sitting in CPU and doing nothing. So in order to multiplex various resources, the notion of multi-tasking came to life. And later hardware improved and brought us multi-processors, that's when everything starts to execute in parallel. Multiple processes allow multi-core computers to run them concurrently in parallel which is more efficient than the past.

##### Memory layout before VM is introduced?

Before virtual memory was introduced, memories were split and assigned to each process so they were very limited resources. Some program wasn't possible because of the limitation of memory usage and it's hard to get it to work if you have to manage your data between hard disk and memory. Programmers need to manage memory themselves and often times things got really messy. And sometimes you thought your program fails because you coded incorrectly, but it's really because some poor programmer wrote some bad programs unintentionally messed up the memory that's been allocated to your very program.

##### Process Control Block (PCB)

What's in PCB often depends on the implementation of OS. But there are some common things that should be included in every implementation of PCB.

* Process ID
* User ID, Group ID
* Context Information (register values, CPU status, stack and frame pointers etc.)
* Scheduling Information (current scheduling state, scheduling priority etc.)

PCB typically resides in the begining of the address space, and specifically in the kernel stack (i.e. where OS bookkeeping stuff). 

##### Multi-level feedback queue


----------------------------------------------------------

#### Thread

##### What is a thread?

##### Why multi-threading even in single processor?

##### Thread Control Block (TCB)

* stack pointer
* program counter
* state of the thread (running, ready, waiting, start, done)
* thread's register values
* pointer to the PCB of the process that the thread lives on

##### How is context switch between threads different than it between processes? Consider problems in cache, TLB and page table?

Because processes are in disjoing address space, the overhead for context switching would be kicking out some data already in cache and bring some data in memory for this new process, and of course do the almost the same thing for TLB, because they're in different address spaces. And cache misses will be a lot.

As for threads, it's a whole different story. Because threads share memory spaces, and cache misses will not be a lot compared to that of processes' context switch. And since we're still in the same address space, the translation map from physical memory to virtual memory will not change. So little will affect the performance of TLB. 

Typically, context switching between threads in the same process is faster than context switching between processes.

##### Hyper-threading and its implementation

##### User-level threads vs. kernel-level threads

User-level threads are threads that kernel doesn't know exist. There will be specific user-level code that deal with the scheduling user-level threads.

However, in the scenario of kernel-level threads, it's the OS who does all the scheduling.

And the biggest difference is that context switching in user-level threads are cheaper than that of kernel-level threads. First, you don't have to go all the way to the kernel through a expensive system call which will incur context switch to kernel code. Second, if it's kernel threads in different processes, there would be way more overhead cost by cache penalties and TLB penalties.

##### Reason behind more kernel-level threads than processors

Remember not all threads are going to be CPU-bound. Some of the threads will have to do a lot of I/O. So if some of them are waiting for I/O response, we can take them off the CPU and let other threads run for a while. Thus having more kernel-level threads than processors are going to be efficient.

#### Scheduling

##### Preemptive scheduling vs. Cooperative scheduling

**Preemptive scheduling** is a scheduling scheme in which the OS will force a process off the CPU and give chance for other processes to run and later resume to the processes that's been hauled off the CPU. **Cooperative scheduling** is processes being cooperative and voluntarily yiled the CPU to other waiting processes.

----------------------------------------------------------

#### Synchronization

##### Deadlock

I think the best analogy to explain deadlock is the **dining philosophers' problem**. Philosophers need to have 2 chopsticks in order to eat the spaghetti, and there is only one chopstick between each philosopher. And when the dinner begins, each philosopher grab the only chopstick in their immediate right. Then each philosopher would only have on chopstick in their hand, and they need 2 to eat so they'll never give up the one they already got. They'll just sit there forever and think about the philosophy of eating with 2 chopsticks.

An example in OS would be process A wants to write file 1 and then write file 2 while at the same time process B wants to write file 2 and then file 1. Process A and process B starts off by writing file 1 and file 2 repectively, and then they finish writing these two and start to request for writing the file they haven't written which is file 2 and file 1 respectively. They somehow still needs the current file they finished writing to complete the task they're assigned, so they will not give up the current file lock and try to grab another file lock. So there you have it, another forever waiting couple.

##### Livelock <! TODO>

##### Starvation

Starvation is that a process never gets the resources it wants. The resources could be CPU time, I/O or files etc.

##### Priority Inversion

Priority inversion happens when a high prioity process is wating for a low priority process which is starved on a resource that's being used by a middle priority process. So essentially, the high priority needs to wait for the middle priority process. And that's how priority gets inversed.


##### Mutex and implementation <! TODO>

Does mutex have a wait key? what happens if grabbing a mutex fails? And does user put mutex_lock() in a while loop? Then that would be busy waiting even if the implementation of mutex is not busy waiting?

If mutex does have a queue, then what's the difference between it and condition variable?

##### Condition variable and implementation <! TODO>

Why do we need another synchronization method? Because, there is situation where a thread needs to wait for some condition to hold true to go into the critical section. And mere mutex is not good enough as threads wait on a lock can waste resources if programmers decide to busy-waiting on the lock (i.e. constantly checking if a lock is available in a while loop). Second, because

Why always check a condition in a while loop?

----------------------------------------------------------

#### Lock-free and Wait-free Synchronization

If we already have synchronization primitives like locks, mutex and condition variables, why would we need lock-free and wait-free synchronization?

And whole other questions in the lecture notes!!!!

----------------------------------------------------------

#### DTHREADS

How does DTHREADS get rid of false sharing?


See letcure notes!




[file_lock]: https://en.wikipedia.org/wiki/File_locking#In_Unix-like_systems
[file_lock_so]: http://unix.stackexchange.com/questions/147392/what-is-advisory-locking-on-files-that-unix-systems-typically-employs
