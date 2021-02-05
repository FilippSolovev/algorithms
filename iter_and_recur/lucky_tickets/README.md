# Lucky Tickets

If you've ever used public transportation, you might have noticed that each ticket for a ride has its own number.
A ticket is considered to be lucky if a sum of the left digits in a number is equal to the one from the right. Among 6-digit tickets luckies are `100001` since 1 + 0 + 0 = 0 + 0 + 1, `157904` because 1 + 5 + 7 = 9 + 0 + 4, for 8-digit an example is `97142289` cause 9 + 7 + 1 + 4 = 2 + 2 + 8 + 9 and so on. You got the idea 🤓

Wonder how many such tickets can be in a roll? The good news is this python script can help you to answer that question. It takes half of the ticket number length (since ticket numbers are usually symmetrical) as an argument and prints an answer to the console.

# Example

Let's count how many lucky ones are among 8-digit tickets, i.e. in a range between 00000000 and 99999999. To do this, just type the following and hit Enter:
~~~~
$ python lucky_tickets.py 4
~~~~
And the answer is 🥁🥁🥁 4816030!

To run tests with the [naive-tester](https://github.com/FilippSolovev/naive-tester) (it should be installed first)
use the command:
~~~
$ tester lucky_tickets.py tests
~~~

# A few words about an algorithm

The algorithm is iterative by its essence but with a few tricks. To certain extent it represents MapReduce ideas though it lacks parallelism and distribution.

A couple of notes about its effectiveness (or ineffectiveness 🙈) can be better shown in the pictures.

![line profiler results]()

![memory profiler results]()

As you can see the most costly thing is sorting key-value pairs and final summation.
