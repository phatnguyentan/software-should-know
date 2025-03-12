# Core concepts of your primary backend language (Java, Python, Node.js, etc.)

## Java Interview Questions:

Q: What is the difference between JDK, JRE, and JVM? 
A:

JDK (Java Development Kit): Complete development environment including compiler, debugger, documentation tools

JRE (Java Runtime Environment): Contains libraries and JVM needed to run Java applications

JVM (Java Virtual Machine): Executes Java bytecode and provides platform independence

Q: Explain the difference between String, StringBuilder, and StringBuffer in Java? 
A:

String: Immutable, thread-safe

StringBuilder: Mutable, not thread-safe, better performance

StringBuffer: Mutable, thread-safe, slower than StringBuilder

Q: What is the difference between == and .equals() in Java? 
A:

== compares object references (memory addresses)

.equals() compares the content of objects


## Python Interview Questions:

Q: What is the difference between lists and tuples? A:

# Lists are mutable
list_example = [1, 2, 3]
list_example[0] = 10  # Valid

# Tuples are immutable
tuple_example = (1, 2, 3)
tuple_example[0] = 10  # Raises TypeError


Q: Explain Python decorators 
A:

def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")


Q: What are Python generators? A:

def number_generator(n):
    for i in range(n):
        yield i

# Uses less memory than storing all numbers in a list
gen = number_generator(1000000)

## Node.js Interview Questions:

Q: What is the Event Loop in Node.js? 
A: The Event Loop is a mechanism that allows Node.js to perform non-blocking I/O operations despite JavaScript being single-threaded. It handles executing callbacks and managing async operations.

Q: Explain callbacks and promises 
A:

// Callback
function fetchData(callback) {
    setTimeout(() => {
        callback("Data");
    }, 1000);
}

// Promise
function fetchDataPromise() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("Data");
        }, 1000);
    });
}

// Async/Await
async function getData() {
    const data = await fetchDataPromise();
    console.log(data);
}

Q: What is middleware in Express.js? 
A:

const express = require('express');
const app = express();

// Middleware example
app.use((req, res, next) => {
    console.log('Time:', Date.now());
    next();
});

## General Backend Concepts:

Q: What is REST API? 
A: REST (Representational State Transfer) is an architectural style for designing networked applications. It uses HTTP methods (GET, POST, PUT, DELETE) and is stateless.

Q: Explain ACID properties in databases 
A:

Atomicity: Transactions are all or nothing

Consistency: Database remains in a valid state

Isolation: Transactions don't interfere with each other

Durability: Committed changes are permanent

Q: What is dependency injection? 
A: A design pattern where objects receive their dependencies instead of creating them. This promotes loose coupling and easier testing.

Remember to:

Understand the concepts thoroughly rather than memorizing answers

Practice coding examples

Be prepared to explain with real-world examples

Know how to handle edge cases

Be able to discuss performance implications
