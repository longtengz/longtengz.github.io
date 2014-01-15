---
layout: post
title: "Setting up Jekyll with GitHub"
date: 2014-01-15 22:28:50
categories: website
tages: Jekyll GitHub git ruby rvm gem
---

You can use GitHub to host your personal blog for you, and simply blog with Jekyll.

What is Jekyll?
=================
[Jekyll][jekyll] is "a simple, blog aware, static site generator". It is one site generator that you can build static websites using dynamic components. Such components include templates, partials, liquid code, markdown, etc. Aside all that Jekyll has brought us, its killer feature(at least that's what I think) is the ablity to be hosted freely on [GitHub Pages](http://pages.github.com).

I'm not expert and only 3-days after learning something, so to take some notes, here I will go through some of the details of how I used *Jekyll*, *git* and *GitHub* to build this mini site.

Jekyll
---------

Because Jekyll is bundled as a ruby gem, you have to use `gem install jekyll`. Some of you might not be familiar with `gem`, it's a package manager for ruby. To use a gem, go to [RubyGems][rubygems], download it from source. Unzip that zip file, `cd` into that unzipped directory, and 

	cd zipfile 	
	# or whatever compressed file you just uncompressed

	ruby setup.rb

Then you just installed RubyGems. And there is always a easy way to install it using *yum*, *apt-get*.

	# if you are using apt-get on Ubuntu
	sudo apt-get install rubygems

	# if you are using yum like me on Fedora
	sudo yum install rubygems

That's the case if you already have ruby. But for me, I then have ruby v1.8.~ when I `ruby setup.rb`, it prompts with an error. After a little search on Google, I chose to reinstall *ruby* with its latest and stable version using [**rvm**][rvm].

After successfully installing *rvm*, we can then install a new version of *ruby* and delete the older version of that.

	rvm install 2.1.0
	rvm list 
	rvm use 2.1.0 --default

If it occurs an error saying "RVM is not a function", then you probably are not using a login shell.
Solutions found in [here][rvmNotAFunction]

If you're under Bash shell, do the following:

	/bin/bash --login
	
then change your ruby version again:

	rvm use 2.1.0 --default

	rvm remove older-version-of-ruby 
		# as listed in the `rvm list`

Then you are ready to install *RubyGems* with `ruby setup.rb`, and then *Jekyll* with `gem install jekyll`.

After you've installed Jekyll, you're only one step away from your mini site.

	jekyll new your-site-name
	cd your-site-name
	jekyll serve

Then hit [localhost:4000](localhost:4000) in your browser, there you go, you've built your site!
A whole lot more you can do with Jekyll, I'm not gonna cover everything here so go to [Jekyll][jekyll] and learn for yourself.

git & GitHub
-------
If you ever want to freely host your website somewhere, I'd say the combination of Jekyll, git and GitHub is definately the choice. According to [JekyllBootstrap][jekyllbootstrap] and [GitHub Pages][github pages], GitHub will only run your code as a website if you specify your repo to be **username.github.io**. In that case, you'd better 

	jekyll new username.github.io

since you'll need that directory in a minute.

After the Jekyll part, while you are still in that root directory of your site, run the following:

	git init
	git add .
	git commit -m 'Initial commit'
	
And then you go to your [GitHub][github] homepage, and create a new repo named **username.github.io**, and then hit *create*.
Again in command line:
	
	git remote add origin git@github.com:username/username.github.io.git
	git push origin master

After a couple minutes(may be around ten mins), you can see your website in *username.github.io*

That's it!

[jekyll]: http://jekyllrb.com
[github]: https://github.com
[github-pages]: http://pages.github.com
[JekyllBootstrap]: http://jekyllbootstrap.com
[rvmNotAFunction]: http://stackoverflow.com/questions/9336596/rvm-installation-not-working-rvm-is-not-a-function "StackOverflow"
[rubygems]: http://rubygems.org
[rvm]: https://rvm.io/rvm/install
