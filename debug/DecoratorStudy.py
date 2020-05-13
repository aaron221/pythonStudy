# 装饰器学习

# 1.一切皆对象
# def sayHello(content="hello "):
#     return content+"the world"
#
# print(sayHello())
#
# print(sayHello("aaron "))
#
# param = sayHello()
#
# print(param)
#
# # print(param)
#
# print(sayHello())
#
# # 在函数中定义函数
#
# def hi(name="yasoob"):
#     print("now you are inside the hi() function")
#
#     def greet():
#         return "now you are in the greet() function"
#
#     def welcome():
#         return "now you are in the welcome() function"
#
#     print(greet())
#     print(welcome())
#     print("now you are back in the hi() function")

# 上面展示了无论何时你调用hi(), greet()和welcome()将会同时被调用。
# 然后greet()和welcome()函数在hi()函数之外是不能访问的，比如：

# greet()
#outputs: NameError: name 'greet' is not defined

# 从函数中返回函数

# def hi(name="yasoob"):
#     def greet():
#         return "now you are in th greet() function"
#     def welcome():
#         return "now you are in the welcome() function"
#
#     if name == "yasoob":
#         return greet
#     else:
#         return welcome
#
# a = hi()
# print(a)
#
# #上面清晰地展示了`a`现在指向到hi()函数中的greet()函数
# #现在试试这个
#
# print(a())

# 再次看看这个代码。在 if/else 语句中我们返回 greet 和 welcome，而不是 greet() 和 welcome()。为什么那样？这是因为当你把一对小括号放在后面，这个函数就会执行；然而如果你不放括号在它后面，那它可以被到处传递，并且可以赋值给别的变量而不去执行它。 你明白了吗？让我再稍微多解释点细节。
#
# 当我们写下 a = hi()，hi() 会被执行，而由于 name 参数默认是 yasoob，所以函数 greet 被返回了。如果我们把语句改为 a = hi(name = "ali")，那么 welcome 函数将被返回。我们还可以打印出 hi()()，这会输出 now you are in the greet() function。


# 将函数作为参数传递给另一个函数
# def hi():
#     return "hi yasoob!"
#
# def doSomethingBeforeHi(func):
#     print("I am doing some boring work before executing hi()")
#     print(func())
#
# doSomethingBeforeHi(hi)


# 你的第一个装饰器

# def a_new_decorator(a_func):
#
#     def wrapTheFunction():
#         print("I am doing some boring work before excuting a_func()")
#         a_func()
#         print("I am doing some boring work after executing a_function()")
#     return wrapTheFunction
#
# def a_function_requiring_decoreation():
#     print("I am the function which needs some decoration to remove my foul smell")

# a_function_requiring_decoreation()

# a_function_requiring_decoreation = a_new_decorator(a_function_requiring_decoreation)
#
# a_function_requiring_decoreation()

# 你看明白了吗？我们刚刚应用了之前学习到的原理。这正是 python 中装饰器做的事情！
# 它们封装一个函数，并且用这样或者那样的方式来修改它的行为。现在你也许疑惑，我们在代码里并没有使用 @ 符号？
# 那只是一个简短的方式来生成一个被装饰的函数。这里是我们如何使用 @ 来运行之前的代码：

# @a_new_decorator
# def a_function_requiring_decoration1():
#     """"Hey you! Decorate me!"""
#     print("I am the function which needs some decoration to "
#           "remove my foul smell3")
#
# a_function_requiring_decoration1()
#
# a_function_requiring_decoration1 = a_new_decorator(a_function_requiring_decoration1)
#
# print(a_function_requiring_decoration1.__name__)
#
# from functools import wraps
#
# def a_new_decorator5(a_func):
#     @wraps(a_func)
#     def wrapTheFunction():
#         print("I am doing some boring work before executing a_func()")
#         a_func()
#         print("I am doing some boring work after executing a_func()")
#     return wrapTheFunction
#
# @a_new_decorator5
# def a_function_requiring_decoration9():
#     """"Hey yo! Decorate me!"""
#     print("I am the function which needs some decoration to "
#           "remove my foul smell99")
#
# print(a_function_requiring_decoration9.__name__)

# can_run=True
#
# from functools import wraps
# def decorator_name(f):
#     @wraps(f)
#     def decorated(*args,**kwargs):
#         if not can_run:
#             return "Function will not run"
#         return f(*args,**kwargs)
#     return decorated
#
# @decorator_name
# def func():
#     return ("Function is running")
#
# print(func())
#
# can_run = False
#
# print(func())

# 注意：@wraps接受一个函数来进行装饰，并加入了复制函数名称、
# 注释文档、参数列表等等的功能。这可以让我们在装饰器里面访问在装饰
# 之前的函数的属性。

# 装饰器使用场景

#授权Authorization

# from functools import wraps
#
#
# def check_auth(username="aaron", password="123456"):
#     pass
#
# def requires_auth(f):
#     @wraps(f)
#     def decorated(*args,**kwargs):
#         auth = request.authorization
#         if not auth or not check_auth(auth.username,auth.password):
#             authenticate()
#         return f(*args,**kwargs)
#     return decorated

# 日志

# from functools import wraps
#
# def logit(func):
#     @wraps(func)
#     def with_logging(*args,**kwargs):
#         print(func.__name__+" was called")
#         return func(*args,**kwargs)
#     return with_logging
#
# @logit
# def addtion_func(x):
#     # Do some math.
#     return x+x
#
# result = addtion_func(4)
#
# print(result)

# 其他用途
# 凡是可以抽象出公有的一些操作，都可以使用装饰器来实现，比如抛出一套定义好的异常
# 相当于java语言的切面效果

#带参数的装饰器
# from functools import wraps
#
#
# def logit(logfile='out.log'):
#     def logging_decorator(func):
#         @wraps(func)
#         def wrapped_function(*args,**kwargs):
#             log_string = func.__name__+" war called"
#             print(log_string)
#
#             with open(logfile,'a') as opened_file:
#                 opened_file.write(log_string+'\n')
#             return func(*args,**kwargs)
#         return wrapped_function
#     return logging_decorator
#
#
# @logit(logfile='test.log')
# def myfunc2():
#     pass
#
#
# myfunc2()

# from functools import wraps
#
#
# class logit(object):
#     def __init__(self,logfile='error.log'):
#         self.logfile = logfile
#
#     def notify(self):
#         pass
#
#     def __call__(self,func):
#         @wraps(func)
#         def wrapped_function(*args,**kwargs):
#             log_string = func.__name__+ "was called"
#             print(log_string)
#             with open(self.logfile,'a') as opened_file:
#                 opened_file.write(log_string + '\n')
#
#             self.notify()
#             return func(*args,**kwargs)
#         return wrapped_function
#
#
# @logit()
# def myfunc3():
#     pass
#
#
# myfunc3()


# class email_logit(logit):
#     '''
#     一个logit的实现版本，可以在函数调用时发送email给管理员
#     '''
#     def __init__(self,email='admin@myproject.com',*args,**kwargs):
#         self.email = email
#         super(email_logit, self).__init__(*args,**kwargs)
#
#     def notify(self):
#         pass
#
#
# @email_logit(logfile='email.log')
# def func3():
#     pass
#
#
# func3()



