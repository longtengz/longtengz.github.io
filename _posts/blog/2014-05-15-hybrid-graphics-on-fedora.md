---
layout: post
title: "Disable discrete VGA on Fedora 20 while radeon and fglrx are both not working"
date: 2014-05-15 21:56:40
category: blog 
tags: hardware VGA
description: There is really a lot going on in the open source world, I just didn't know about them yet. 
---

I just migrated to Fedora 20 only out of pure love for its slick UI. When I first installed Fedora 15, I had this annoying VGA cooler that spinned like crazy and consumed a great portion of power that drained my battery pretty fast. I have a Dell, and it has dual graphics cards, one discrete and the other integrated. After a bit of search, I think I solved the problem by installing the **propriety** AMD Catalyst Driver **fglrx** and succeeded using the hybrid graphics cards alternatively. 


But this time, Fedora 20 is quite new, and the latest propriety driver is not up to date with the new linux kernels. There are compatibility issues around that I cannot address. But Fedora 20 does ship with the [**open** source radeon drivers][radeon]. These drivers are written mostly by the community based on specs published by AMD.

You can use the following command to check whether the Fedora installation has detected your discrete VGA card and installed the **radeon** for you automatically.

{% highlight bash %}
lsmod | grep radeon
# lsmod - Show the status of modules in Linux Kernel
{% endhighlight %}

By checking the PCI devices that are currently connected,

{% highlight bash %}
# list all PCI devices
lspci -v | less
# search '/VGA'
# or less verbose
lspci | grep -i VGA
{% endhighlight %}

 
I see two graphics cards turned on, but only the integrated one with the tag `[VGA controller]` which indicates it currently controls how my computer displays on screen. However the radeon open-source driver doesn't seem to work event it's now turned on. As I don't need two cards, and I don't need extremely fancy graphics, so the integrated Intel graphics card should work for me. And so I opt to turn off the discrete AMD card.

I found a solution on [wiki archlinux][archlinux], and it elaborates quite well on related topics:

{% highlight bash %}
echo OFF > /sys/kernel/debug/vgaswitcheroo/switch
# turns off the discrete GPU
{% endhighlight %}


Note the **Current Problems** section on the page very well clarifies the issues about intel+ati cards on Linux:

>The Dynamic Switch needs Xorg support for the discrete videocard assigned for rendering to work [1]. So, rendering on the discrete gpu will not work until the Xorg team adds support for it.

>This means that with a muxless intel+ati design, you cannot use your discrete card by simply modprobing ( `modprobe`- Add and remove modules from the Linux Kernel ) the radeon module.

I added the above script in `/etc/rc.d/rc.local` to turn off the discrete AMD card on *startup*.

Though I don't quite how the whole thing actually work, but at least I made my VGA cooler shut up when it's not supposed to talk much. And battery life does improve as opposed to that of Fedora 15 I was running with hybrid cards.

p.s. There is a [site][site] providing document tips, tricks and problems related to AMD's proprietary Linux driver (a.k.a. fglrx) which might be helpful if you are not using the newest Linux distros.


[radeon]: http://www.x.org/wiki/RadeonFeature/
[archlinux]: https://wiki.archlinux.org/index.php/hybrid_graphics
[site]: http://wiki.cchtml.com/index.php/Main_Page
