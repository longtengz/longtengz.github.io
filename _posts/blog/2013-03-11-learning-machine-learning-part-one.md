---
layout: post
title: "Introduction into Machine Learning"
date: 2013-03-11 11:26:47
category: blog
tags: linear-regression gradient-descent normal-equation
description: Course note
---

<!-- Today, I will begin taking notes on the machine learning course taught on Coursera by Andrew Ng. This is part one, and only goes as far as 4th segment of all video lectures. -->

# Introduction

### Machine Learning Definition

Tom Mitchell once said:

>   A computer program is said to learn
>   from experience E with respect to some task T
>   and some performance measure P, if its
>   performance on T, as measured by P, improves
>   with experience E.

Three things needs to pay attention here:

* Task
* Performance
* Experience

A task can be an email program classifying emails as spams or not spams, or a program which determines a person have cancer or not.

Performance can be described as how good the *task* has done，that is the number of emails correctly classified as spams for an email program, and how correct is the diagonosis carried out by a program.

Experience, in my opinion, is considered to be the knowledge that is going to be used when performing certain *task*.

### Machine Learning Algorithms

There are *mainly* two algorithms in ml:

* Supervised Learning
* Unsupervised Learning

And along with the above two, there are two other:

- Reinforcement Learning
- Recommender Systems

#### What is Supervised Learning?

To supervise is to watch and direct someone or something. When implementing a supervised learning algorithm, we feed the algorithm an amount of data in the form of paired inputs and outputs. After the algorithm has *experienced* a lot of occasions（which is on what input, generates what ouput), we give the program a non-output-paired input in the hope that it could give us the right output. By 'right', here it means probably right with bigger probability than most other answers.

In supervised learning, there are two basic approaches: **regression** and **classification**. Both will give us right answers. But they are for different use cases. In real practice, the desired output could be binary like yes or no, or continuous values like the housing price. 

- **Regression** is used to predict continuous valued output (or say real valued) like price. 
- **Classification** is used for discrete valued output.

Either way, we get right answers from supervised learning algorithms.



#### What is Unsupervised Learning? 

On the contrary, to unsupervise means simply to give only inputs but paired outputs (which you can think of as class labels) and leave the algorithm itself output whatever hidden structure in those unlabeled data (aka non-output-paried inputs) have. So there is no way (not that I know of) to say an unsupervised learning algorithm is outputing a right or wrong result, since the data we input have no labels at all.

Sounds confusing, right? I'm a little confusing too. An example might clarify. Google news has this feature that news similar to top stories can be grouped and presented to users. But sometimes, the included news are not quite relevant to the main top stories. But they are actually very content-related. Google does this by using unsupervised learning algorithms that cluster news or, less fancier, group news. Any news that shares something in common, we get to collect them together.

Big difference here with supervised learning, *unsupervised learning* doesn't present **right answers** but they can manage quite a good job at **clustering** things.

There is one question I often asked myself when I first started learning this: what is the difference between *classification* with *clustering*?<br>
**Classification** means predicting the output that shall fall under a specific category, like binary results labeled with yes and no, or tenary results likewise. But **clustering**, in my humble opinion, it means group things, but the algorithm don't get to tell us which category or what similarity they share in common within a cluster. It can only tell us 'Ok, group A is similar, group B is similar'. But it never tells us, what is group A or B, how to tag them, how to put them into categories.


After having a sense about what kind of algorithms we can use, let's start with something basic.

# Linear Regression With One Variable

As pointed out before, linear regression is a kind of supervised learning algorithm. Because it gives the right anwsers. And it can predict real-valued output. Consider this example, you for some reason want to know how many people will go swimming when temperature is as high as 40 degrees of Celcius or as moderate as 25 degrees. You want the program to output the number of people will go swimming when you input degrees of Celcius. There should be a training set that this algorithm needs to learn from and base on when asked for prediction of a new input.

A training set is an **experience** which we previously talked about. After the learning phase of this algorithm, it should work out one **hypothesis** function that can do a **task** that output the right answer we desired.

### What is a hypothesis function?

Certainly, a hypothesis function, as the name suggests, is a function or model representation that makes hypothesis or, say, predictions. Like a fortune teller, we ask the hypothesis function (do input) one question about the unknown future and it will give us answers (receive output). But we can not tell whether the answers are true or not until then. So it's best if we just call it predictions instead. When that day finally come, it turns out that the fortune teller was telling half truth and half lie and he becomes aware of the **performance** of last prediction. Back then he might made a few mistakes when performing prediction. Now he notices the mistakes and makes adjustment on the approach of predicting. Next time, he might end up with a truth (that is, **performance improved**).

Here, the hypothesis function of univariate linear regression is a linear function with one variable:

$$ h_\theta(x) = \theta_0 + \theta_1x $$

\\( h_\theta(x) \\) is the prediction (output) of \\( x \\) (input). 
Given that, but how do we exactly get this hypothesis function? How to choose \\( \theta_0 \\) and \\( \theta_1 \\)?

We all know that two points on a plane can determine one straight line. So clearly, if we have only 2 pairs of input and output in the training set, then we only get one unique hypothesis function. As the training sets get more, there should be infinite hypothesis functions we can draw to model the linear relation between input and output. Which one will be the fittest to perform the **task** with a bigger probability?

Let's get back to the training set of only two pairs. The two points are on the line drawn from the hypothesis function. Even if the hypothesis function is the fittest. It's very likely it will perform badly because it lacks **experience**. The **performance** shall improve when **experience** gets more. And that's the essence of machine learning. 

As **experience** gets more, the hypothesis function will no longer be unique. Every hypothesis function you draw from one training set is going to perform differently on next **task**. But which has the best shot to work out the closest prediction as opposed to outcome? Is it the straight line that no points sit near or most points sit near (this is considered one implementation of building cost function and in turn improve hypothesis function, later we'll delve into more depth)? Apparently, it's the latter.

Then how do we find the latter one? This is where cost function comes in.

### What is a Cost Function?

On [wiki/Loss_function][lossFunction]

> In statistics, typically a loss function is used for parameter estimation, and the event in question is some function of the difference between estimated and true values for an instance of data. 

In machine learning, we want to find the optimized solution. In terms of optimization, we need to minimize the cost function to try to get the biggest number of points on the hypothesis straight line.

The cost function for univariate linear regression is often defined as following:

$$ J(\theta_0, \theta_1) = \frac{1}{2m}\sum\limits_{i=1}^{m} (h_\theta(x^{i})-y^{i})^{2} $$

\\( m \\) here denotes the number of data in a training set.
\\( x^{i} \\) and \\( y^{i} \\) means input and output respectively.

The cost function above is called **squared-error loss function**. You should know it is only one implementation. And You can build whatever cost function of which minimization won't be expensive and it can help you efficiently improve the performance of hypothesis function when it's minimized.

However, different cost functions will likely generate different hypothesis functions with different performances. Like we can find one hypothesis function by the biggest number of points sit right **on** the straight line instead of **near** it, so the cost function can be defined as below:

$$ J(\theta_0, \theta_1) = \sum\limits_{i=1}^{m} e^{i} $$

$$ e^{i} = \begin{cases}1 & h_\theta(x^{i}) - y^{i} \neq 0 \\\\ 0 & h_\theta(x^{i}) - y^{i} = 0 \end{cases} $$

When we minimize it, we are finding one straight line with the most points of data (in the training set) on it. But consider the situation (when training set is not large) where only 2 points can be found on the hypothesis straight line, no matter how we draw this line, we cannot find the minimal since each the cost function is always equal to 2. Therefore we can not determine the hypothesis function.

So cost function can be very problem-specific. The squared-error loss function is very popular in choosing the parameters for linear regression's hypothesis function. When you learn deeper, you can define your own cost function. By now we'll keep on using squared-error loss function.


[lossFunction]: http://en.wikipedia.org/wiki/Loss_function
