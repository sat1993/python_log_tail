# -*- coding: utf-8 -*-
# coding=utf-8
"""
    __thread_pool类，负责线程池管理。尽量不要使用网络现成的线程池。我们的程序是比较吃cpu的并不吃i/o，不适合网络流传的线程池版本。
    思路：
        依赖模块：threading、queue
        属性：执行队列(占用线程池的队列，执行完pop掉)，空闲队列(一定时间会触发空闲队列的pop事件。保证在空闲队列不为0的时候，执行队列一定有任务在执行)，阻塞队列(在执行队列与空闲队列都满载的时候，暂存到这。)
        add():添加线程，在完成添加之后，判断线程池中空闲线程数量，如果等于全线程数量，则直接调用pop()。如果空闲队列与执行队列都满，则add到阻塞队列中。
        pop():对空闲线程对象进行pop操作。取出一个线程之后进行执行。如果空闲线程没有线程需要执行。则返回None。每次pop之后，检查一遍执行队列、空闲队列、阻塞队列。
        run():增加一个参数(有必要可以使用变长参数)，传递需要执行的方法进来，整个run()方法就是为了执行这个方法。。以及在run()的最后调用一下pop()函数。
        线程执行完之后记得join()一下
"""