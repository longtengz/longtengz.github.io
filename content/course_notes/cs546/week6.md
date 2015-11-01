Title: Week 7 of Computer System Security
Date: 2015-10-19 17:26
Modified: 2015-10-19 17:30
Category: CourseNotes
Tags: OS, Security, CS546
Authors: Teng Long 

### Contents

* Capsicum (cont'd)
* Comparison of defenses discussed so far
* Information flow control (in HiStar)

----------------------------------------------------------------


#### Capsicum (cont'd)

##### Adapting Applications to Capsicum

In order for applications to run with the features provided by Capsicum, programmers have two choices:

1. directly use `cap_enter()` to enter into a capability mode process from an existing process currently running with ambient authority.
2. Modify the application to use the full **libcapsicum** API (this is included in FreeBSD)


###### Examples

**tcpdump**

**dhclient**

**gzip**

It contains no existing compartmentalisation, and it executes with ambient user(rather than system) privileges.

Adapting **gzip** to Capsicum results in 409 lines of code changes (about 16%) of the gzip source code, large to marshal and un-marshal RPCs.


Differences between RPCs and IPCs.

what does flatten in computer science mean?

Essentialy it's a process of the following:

`[[1, 2, 3], [4, 5, 6], [7, 8, 9]]`

to

`[1, 2, 3, 4, 5, 6, 7, 8, 9]`




#### Comparison of defenses discussed so far

the big table in the handwritten notes


#### Information flow control (in HiStar)

Bell-LaPadula model

what exactly is a state machine?

Check out covert channels

what's chroot? And chroot jail? check out chroot on wiki, especially the Uses section.

What's microkernel? Microkernel vs monolithic kernel?



