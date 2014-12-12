---
layout: post
title: "Difference between exec() and spawn() of childprocess Node.js"
date: 2014-03-12 22:34
categories: nodejs
tags: node child process exec spawn IO stdout stderr Windows cmd 
---

Currently I am making an application that does roll call in a classroom for teachers who don't want to waste their time on a roll call. We need to invoke some Matlab-implemented algorithm using OpenCV on Visual C++. So I turned to Windows to build a site where teachers can log in and do a roll call on the server with footages uploaded by a video camera in the classroom.

Considering executing C++ code would be an external process for Node. Node is designed to handle I/O efficiently with the help of its `child_process` module. You can actually use `exec()` and `spawn()` to control external processes and communicate with them.

On Linux, I am not aware of any command that both the above methods apply differently. Then why bother create two separate functions? Because they are for different needs. There are commands that result with a lot of data, if you use `exec()` to run these, it will consume a lot of memory because the child process's output is **buffered**, plus it has a `maxBuffer` default option that only allows for 200k data buffered though this default option can be changed. Unlike `exec()`, `spawn()` uses **streams** both input(stdin) and output(stdout, stderr), so it's there for a huge amount of data.

But on Windows their differences not only lie in buffer or stream, but also in what type of commands they are about to execute in a child process. So let's take a look at `child_process.js` to find out how they are implemented:

exec()
=================================

child_process.exec(command, [options], callback)

{% highlight JavaScript %}	
	normalizeExecArgs():

	  if (process.platform === 'win32') {
	    file = 'cmd.exe';
	    args = ['/s', '/c', '"' + command + '"'];
	    // Make a shallow copy before patching so we don't clobber the user's
	    // options object.
	    options = util._extend({}, options);
	    options.windowsVerbatimArguments = true;
	  } else {
	    file = '/bin/sh';
	    args = ['-c', command];
	  }


	child_process.execFile():
		var child = spawn(file, args, {
		    cwd: options.cwd,
		    env: options.env,
		    windowsVerbatimArguments: !!options.windowsVerbatimArguments
		});
{% endhighlight %}
	

After seeing this code it's quite clear why this method is named **exec**, it pays more attention on how to run a command on a child process. So it specifies `cmd.exe` or `/bin/sh` for either Windows or Linux to excute a command using these two command.(It might sound confusing). But take a look at the man page for `cmd.exe` or `sh`, with options specified by the code above, they only execute the command and terminates.

You can check out what does `cmd /c` means by typing `cmd /?` in cmd:
> /C      Carries out the command specified by string and then terminates

As for Linux, you can run the following:

{% highlight bash %}
$ ps
$ /bin/sh -c ls
$ ps
{% endhighlight %}

and see whether another process has showed up. Obviously no new process will show up, because when `sh -c ls` finished executing `ls`,it stops and terminates.



spawn()
=============================
	
{% highlight javascript %}
child_process.spawn(command, [args], [options])

// the first argument **command** should be named **file** as this is a bit confusing in Node documentation.

normalizeSpawnArguments(/*file, args, options*/):
    // when this normalized arguments child_process.spawn() takes in, 
    // the *file* argument is never normalized
    // and the *file* is not normalized as that in the arguemnts of exec()
{% endhighlight %}

So it's quite clear now, the so-called **command** argument isn't exactly command but rather a file name that will be excuted alone as a child process. `cmd.exe` or `/bin/sh` is just one of many child processes that can be executed.

Be aware that on **Windows**, some command isn't exactly considered as a process but a built-in command in **cmd**, such as `dir`. On the other hand, there are some executable files considered as a process that come with an extension '.cmd', '.exe' or '.bat', then you can't just call them without extension when using **spawn()**, becuase **spawn()** expects a file name.

So in a nut shell, you use `spawn()` whenever you want to outsource something in a child process, you use `exec()` whenever you only want to execute a command and don't want another subshell.


