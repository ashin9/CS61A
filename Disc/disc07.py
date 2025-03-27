# 1.1
# >>> callahan = Professor("Callahan")
# >>> elle = Student("Elle", callahan)
# name = "Elle"
# statff = callahan

# "There are now 1 students"

# >>> elle.visit_office_hours(callahan)
# callahan, student.understanding = 1
# "Thanks Callahan"

# >>> elle.visit_office_hours(Professor("Paulette"))
# Paulette, student.understanding = 2
# "Thanks Paulette"

# >>> elle.understanding
# 2

# >>> [name for name in callahan.students]
# [{"Elle": elle}] ❎，没有{}
# ['Elle']

# >>> x = Student("Vivian", Professor("Stromwell")).name
# "There are now 2 students"

# >>> x
# "Vivian"

# >>> [name for name in callahan.students]
# [{"Elle": elle}] ❎，没有{}
# ['Elle']

# 1.2
# 实现特殊 list，MinList

# 可以 append 和 pop，但只能 pop 最小的值

# class MinList 包含一下几个方法

# - 1，append(self, item)，追加元素
# - 2，pop(self)，移除并返回最小元素

# 每个实例包含 size 属性，表示有多少元素，append 和 pop 后，更新 size

# 提示：实际上，将 Python 列表作为每个 MinList 的实例属性包含在内可能会有所帮助，以跟踪我们拥有的项目。

class MinList:
    """A list that can only pop the smallest element """
    def __init__(self):
        self.items= []
        self.size = 0

    def append(self, item):
        """Appends an item to the MinList
        >>> m = MinList()
        >>> m.append(4)
        >>> m.append(2)
        >>> m.size
        2
        """
        self.items.append(item)
        self.size += 1
    
    def pop(self):
        """ Removes and returns the smallest item from the MinList
        >>> m = MinList()
        >>> m.append(4)
        >>> m.append(1)
        >>> m.append(5)
        >>> m.pop()
        1
        >>> m.size
        2
        """
        min_item = min(self.items)
        self.items.remove(min_item)
        self.size -= 1
        return min_item
    

# 1.3
class Email:
    """Every email object has 3 instance attributes: the message, 
    the sender name, and the recipient name.
    """
    
    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name

class Server:
    """Each Server has an instance attribute clients, 
    which is a dictionary that associates client names with client objects.
    """
    
    def __init__(self):
        self.clients = {}

    def send(self, email):
        """Take an email and put it in the inbox of the client it is addressed to.
        """
        # email.recipient_name.receive(email)
        client = self.clients[email.recipient_name]
        client.receive(email)

    def register_client(self, client, client_name):
        """Takes a client object and client_name and adds them to the clients instance attribute.
        """
        self.clients[client_name] = client


class Client:
    """Every Client has instance attributes name (which is used for addressing emails to the client), 
    server (which is used to send emails out to other clients), 
    and inbox (a list of all emails the client has received).
    """
    
    def __init__(self, server, name):
        self.inbox = []

        self.server = server
        self.name = name
        self.server.register_client(self, self.name)


    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the given recipient client.
        """
        email = Email(msg, self.name, recipient_name)
        self.server.send(email)
        

    def receive(self, email):
        """Take an email and add it to the inbox of this client.
        """
        self.inbox.append(email)


# 2.1

class Pet():
    def __init__(self, name, owner):
        self.is_alive = True # It's alive!!!
        self.name = name
        self.owner = owner

        def eat(self, thing):
            print(self.name + " ate a " + str(thing) + "!")
        
        def talk(self):
            print(self.name)

class Dog(Pet):

    def talk(self):
        print(self.name + ' says woof!')

class Cat(Pet):

    def __init__(self, name, owner, lives=9):
        super().__init__(name, owner)
        self.lives = lives
    
    def talk(self):
        """ Print out a cat's greeting.

        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        print(self.name + " says meow!")

    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero, 'is_alive' 
        becomes False. If this is called after lives has reached zero, print out 
        that the cat has no more lives to lose.
        """
        if self.lives > 0:
            self.lives -= 1
            if self.lives == 0:
                self.is_alive = False
        else:
            print('This cat has no more lives to lose :(')


# 2.2
class NoisyCat(Cat): # Fill me in!

    """A Cat that repeats things twice."""
    def __init__(self, name, owner, lives=9):
        # Is this method necessary? Why or why not?
        # 没必要, 因为已经继承了 Cat
        super().__init__(name, owner, lives)

    def talk(self):
        """Talks twice as much as a regular cat.
        >>> NoisyCat('Magic', 'James').talk() 
        Magic says meow!
        Magic says meow!
        """
        super().talk()
        super().talk()

    def __repr__(self):
        """The interpreter-readable representation of a NoisyCat

        >>> muffin = NoisyCat('Muffin', 'Catherine')
        >>> repr(muffin)
        "NoisyCat('Muffin', 'Catherine')"
        >>> muffin
        NoisyCat('Muffin', 'Catherine')
        """
        s = "NoisyCat('{}', '{}')".format(self.name, self.owner)
        return s
    
        # 1. repr(muffin) 的输出
        # repr(muffin) 直接调用 __repr__ 方法，返回的是 字符串 "NoisyCat('Muffin', 'Catherine')"，这个字符串本身带有引号（"" 或 ''），因为 repr() 的作用就是返回一个可以在代码中直接使用的、可解释的字符串。

        # 2. 直接输入 muffin 的输出
        # 当你在交互式环境（如 Python 解释器或 Jupyter Notebook）中直接输入 muffin，Python 解释器会自动调用 repr(muffin)，但不会再额外加引号，而是直接显示 repr 方法返回的内容，就像普通对象的打印输出。
        