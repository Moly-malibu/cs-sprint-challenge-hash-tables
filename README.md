# Sprint Challenge: Hash Tables

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This challenge allows you to practice the concepts and techniques learned over the past sprint and apply them in a concrete project. This sprint explored hash tables. During this sprint, you studied hash functions, collision resolution, complexity analysis of hash tables, load factor, resizing, and various use cases for hash tables. In your challenge this week, you will demonstrate mastery of these skills by solving five problems related to hash tables.

The sprint challenge is an individual assessment. All work must be your own. Your challenge score is a measure of your ability to work independently using the material covered through this sprint. You need to demonstrate proficiency in the concepts and objectives introduced and practiced in preceding days.

You are not allowed to collaborate during the sprint challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your TL if you need direction.

_You have **three hours** to complete this challenge. Plan your time accordingly._

## Introduction

This challenge requires you to solve algorithm problems that are amenable to being solved efficiently with a hash table.

### Commits

Commit your code regularly and meaningfully. This practice helps both you (in case you ever need to return to old code for any number of reasons) and your Team Lead as they evaluate your solution.

## Interview Questions

Be prepared to demonstrate your understanding of this week's concepts by answering questions on the following topics. You might prepare by writing down your answers beforehand.

1.	Hashing functions: HF is a mathematical function that converts a numerical input value into another compressed numerical value. HF is used to compute the hash value for a key, also HF may return the same hash value for two or more keys.

a.	Input: in the HF the input is of arbitrary length
b.	Output: in the HF the output fixed length
c.	Values return by HF are called message or hash values.

        i.	Hash value is used as an index to store the key in the hash table.
            Hash=hash_function(key)
            Index=hast % array_size

            Stored array
            Arr[index]=value

2. Collision resolution:

when two or more items should be kept in the same location, keeping subsequent items within the table and computing possible locations. Keeping lists for items that collide in the chaining, or keeping one special overflow area.

3. Performance of basic hash table operations

Since there is always the initial (constant) cost of hashing, the cost of hash table operations with a good hash function is, on average, O(1 + α). If we can ensure that the load factor α never exceeds some fixed value αmax, then all operations will be O(1 + αmax) = O(1).

Set_item(key, value)
Get_item(key)
Delete_item(key)

Data structure      lookup     (contains/get)	add/put	remove
Array				O(n)		O(1)		    O(n)
Function			O(1)		O(n)		    N/A
Linked list			O(n)		O(1)		    O(n)
Search tree			O(lg n)		O(lg n)		    O(lg n)

4. Load factor

The load factor defines the balance between access time and space. A load factor of f uses a hash table using approximately n/f hash buckets for storing n keys. Each hash bucket will have f keys on average. When more keys are added, the hash table size will be increased by a fixed factor (e.g. 2), and rehashing is done, to ensure that the actual load factor is near the desired load factor. You can use a larger load factor to save space, but at more elements per bucket and therefore worse access time. You can reduce the load factor to improve access time, but the hash table will be larger. This is a typical trade-off between time and space (memory). Time is usually more precious than space. Simply use the default, e.g. 0.75. Using (much) smaller load factors blows up the used memory, but gives you only a minuscule improvement of the access time.

5. Automatic resizing:

The rehash size specifies how much to increase the usable size of the hash table when it becomes full. It is either an exact positive integer, or a real number greater than one. If it is an integer, the new size is the sum of the old size and the rehash size. Otherwise, it is a real number, and the new size is the product of the old size and the rehash size. Increasing the rehash size decreases the average cost of an insertion, but increases the average amount of space used by the table. The rehash size of a table may be altered dynamically by the application in order to optimize the resizing of the table; for example, if the table will grow quickly for a known period and afterwards will not change size, performance might be improved by using a large rehash size during the growth phase and a small one during the static phase. The default rehash size of a newly constructed hash table is 2.0.

6. Various use cases for hash tables:

*Storing access based on a non integer
*Storing sparse storage even based on an integer.
*Storing anything where there is no need to access data in the order the data is inserted 
*Storage where insertion and access both need to be fast.
*Storage where uniqueness is useful.

We expect you to be able to answer questions in these areas. Your responses contribute to your Sprint Challenge grade.

## Instructions

### Task 1: Project Set-Up

- [ ] Create a forked copy of this project
- [ ] Add your team lead as a collaborator on Github
- [ ] Clone your OWN version of the repository (Not Lambda's by mistake!)
- [ ] Create a new branch: git checkout -b `<firstName-lastName>`.
- [ ] Implement the project on your newly created `<firstName-lastName>` branch, committing changes regularly
- [ ] Push commits: git push origin `<firstName-lastName>`

### Task 2: Project Requirements

Your finished project must include all of the following requirements:

- [ ] Solve any three of the five problems

For each problem that you choose to solve, complete the following:

- [ ] Navigate into each exercise's directory
- [ ] Read the instructions for the exercise in the README
- [ ] Implement your solution in the `.py` skeleton file
- [ ] Make sure your code passes the tests running the test script with make tests

*Note: For these exercises, we expect you to use Python's built-in `dict` as a hashtable. That said, if you wish, you can attempt to solve using your own hashtable implementation, as well. All solutions should utilize a `dict` or hashtable. You should not use Sets. (Though you can make a `dict` behave like a set if you wish.)*

### Task 3: Stretch Goals

After finishing your required elements, you can push your work further. These goals may or may not be things you have learned in this module, but they build on the material you just studied. Time allowing, stretch your limits, and see if you can deliver on the following optional goals:

- [ ] Solve any four of the five problems
- [ ] Solve all five problems

## Submission format

Follow these steps to complete your project.

- [ ] Submit a Pull-Request to merge <firstName-lastName> Branch into master (student's  Repo). **Please don't merge your own pull request**
- [ ] Add your team lead as a reviewer on the pull-request
- [ ] Your team lead will count the project as complete after receiving your pull-request

