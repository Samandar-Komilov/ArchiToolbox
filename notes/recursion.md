# Recursion

Reference: [Recursive Book of Recursion](https://www.amazon.com/Recursive-Book-Recursion-Interview-Javascript/dp/1718502028)

## Chapter 1: What is Recursion?
The chapter 1 starts with explaining what recursion is and how it works. So, let's start by answering Practice Questions of the chapter:

**1. In general, what is a recursive thing?**
Answer: A recursive thing is a self-referential, self-containing structures. If we see them as a function, it is exactly a function that calls itself.

**2. What is a stack?**
Answer: A stack is a data structure which only permits adding or removing elements from top. It is a LIFO data structure, just like washing dishes.

**3. What is a call stack?**
Answer: A call stack is a stack located in each process address space, where the function calls are stored. Each recursive function call is stored in call stack.

**4. What causes a stack overflow to happen?**
Answer: If a recursive function calls itself infinite times, it will allocate all of the computer memory for stack. When it reaches out of memory, stackoverflow happens.

**5. What is a base case? What is a recursive case?**
Answer: A recursive function, to work properly, should have some condition to stop calling itself and return something. Otherwise it calls itself forever, which is meaningless. So, the condition it stops increasing call stack is base case. The condition it calls itself is a recursive case.

**6. What happens if a recursive function has zero base cases?**
Answer: If a function has no base case, it just runs forever (until stackoverflow).

**7. What happens if a recursive function has zero recursive cases?**
Answer: It simply returns the value of base case.


## Recursion with Iteration
We have a rule of thumb: any iterative algorithm can be rewritten using recursion and any recursive algorithm can be rewritten using iteration.

> Okay, but when they are useful actually?

**1. What is 4! (that is, the factorial of 4)?**
Answer: It is:
    - the factorial(3) * 4:
        - the factorial(2) * 3 * 4:
            - the factorial(1) * 2 * 3 * 4:
        - 1 * 2 * 3 * 4:
    - 1 * 2 * 3 * 4:
1*2*3*4 = 24

**2. What is the critical weakness of the recursive factorial function?**
Answer: It calculates a single calculation over and over again blindly. Especially functions with more than 1 base case are so horrible. Like Fibonacci sequence.

**3. What does an iterative algorithm always use?**
Answer: An iterative algorithm always uses a loop with a mutable variable, while a recursive algorithm uses a stack.

**4. Is it always possible to convert an iterative algorithm into a recursive one?**
Answer: Yes. We should only convert iteration's body into a function, take the loop's condition, and make it a recursive case.

**5. Is it always possible to convert a recursive algorithm into an iterative one?**
Answer: Yes. We should only convert recursive case into a loop body, while taking base case's reverse as a loop condition.

**6. What three features do programming problems that are suitable to recursive solutions have?**
Answer: There are 3 features of a programming problem which makes it to solve with recursion:
- Tree-like structure (self-referencing or self-containing)
- Involves backtracking (reaching the base case and returning to the start)
- Is not so deep to cause stack overflow.

So, my conclusion is to use recursion mostly in divide and conquer algorithms which helps to achieve much less operational cost than plain iterations.

**7. When is recursion required to solve a programming problem?**
Answer: 