
1. How  AsyncConnectionPool works?
i think: is a set of different types of connections to db in async form

the real meaning is: It is a mechanism used to manage and reuse database connections asynchronously in an application. Instead of creating a new connection every time the application needs to interact with the database, a connection pool maintains a set of pre-established database connections. When a request is made, the pool provides an available connection, and once the request is complete, the connection is returned to the pool for reuse.


2. how AsyncIterator works?
i think: i think is type of value who returns a iteretor who can do a async interation

the real meaning is: 
An AsyncIterator is an object in Python that implements the asynchronous iteration protocol. It is used to iterate over asynchronous data streams or objects. Unlike a regular iterator, which uses the __iter__ and __next__ methods, an AsyncIterator must define the __aiter__() and __anext__() methods.

    __aiter__() returns the async iterator itself.
    __anext__() is a coroutine that retrieves the next item asynchronously.

Async iterators are typically used with the async for loop, allowing you to iterate over items produced by asynchronous sources, such as reading data from a file or fetching records from a database, without blocking the program's execution.



3. why we put a asserts in the main module?
i think: the assert is a keyword of the python package "pytest" and we only can use it in tests

the real meaning:  An assert statement in Python is not specific to the pytest package or testing. It is a built-in Python keyword used to verify that a condition is true during runtime. If the condition is False, the program raises an AssertionError with an optional error message.


4. how: , name: str | None = None, phone: str | None = None, email: str | None = None  works?
i think: is first we take we the parameter all the arguments an after we check with the "|" if that is none ignore it

the real meaning:


5. how isintance works?
i think: check if that object is instanced and if that is a specific datatype i think it returns a boolean

the real meaning:

6. how that kind of atributes works?: 
	class UpdateContact(TypedDict):
    name: str | None
    phone: str | None
    email: str | None
i think: if you dont pass a value to that atributes it ignore it 

the real meaning: 

7. what "verbose" means"?
i think: idk really (sorry)

the real meaning:


8. what "@contextlib.asynccontextmanager" ?means?
i think: controls when you create and close the life span to close and open correctly


9. what is a data class?
i think: is  a class who can manage special data apropietly 

the real meaning is: 


10. what is a static method?
i think: is who we can access directly 
the real meaning:

11. what is the file pyproject.toml?
i think: is a project which we can switch the information of the db of production to the information of the test

12. what is License file?
i think: is a file of who can use the program legaly
the real meaning:


13. what is README.md ?
i think: is a file where we say how we can run the program
the real meaning:


























