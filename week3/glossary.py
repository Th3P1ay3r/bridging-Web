glossary ={'function': "A Function, a method, or a subroutine is a reusable block of code that performs a specific task or calculation. Functions help organize code, improve modularity, and enable code reuse. They accept input parameters, perform operations, and may return a value.", 
'loop':"A Loop is a programming construct that allows repetitive execution of a code block based on a specified condition. It helps automate tasks and process large amounts of data efficiently. Common loops include the for loop, while loop, and do-while loop.",
'variable':"A Variable is a named storage location in a computer's memory that holds a value or data. Variables are used to store and manipulate data during program execution. They have a specific data type (integer, string, or boolean) and can be assigned new values throughout the program.",
'version control': "Version Control, also known as Source Code Management (SCM), tracks and manages source code file changes. It allows developers to collaborate, maintain different versions of code, and track modifications over time. Version control systems, such as Git or SVN, provide mechanisms for branching, merging, and reverting changes.",
'error handling':"Error Handling is anticipating, detecting, and handling errors or exceptions that may occur during program execution. It involves implementing strategies, such as try-catch blocks or error codes, to handle errors and prevent program crashes or unexpected behavior safely."}

print(glossary)
print("Computer glossaries")
for key, meaning in glossary.items():
    print(key)
    print(f"\t{meaning}")