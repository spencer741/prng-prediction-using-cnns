## **Observation:**
Society relies on Pseudo-random numbers for a multitude of reasons. Whether the usecases fall in Information Security or, more broadly, modeling and simulation, we shall not highlight their importance in computing.

We think it is important to not only push the boundary for the modern pseudo random number directly, but to also analyze the history of pseudo randomness to aide in that effort.

Whether true randomness is a inhibition of the human perception or not, there is clear need to push the modern pseudo-random number closer to converging on perceived "true" randomness.

## **Questions/Aim:**
To train a neural net to predict PRNs from a chosen PRNGs output. We aim to train neural nets to predict values of assigned PRNGs and track attributes of each to make generalized conclusions about the development of PRNGs with respect to time and any PRN correlations we uncover.


## **Hypotheses:**
1) We predict there will be a positive trend over time on the cryptographic strength of each subsequent PRNG, given the nature of the increasing importance of stronger PRNGs.

2) We also predict that as we get into cryptographically stronger generation methods, our prediction success rates (even with learning) will be less effective.

3) We expect to uncover correlations in Pseudo-random numbers based on each individual generator, and aim to extract more generalized correlations between generators themselves.

## **Experimental Design:**



### **Seeding Method:**

We went with a seed generation method that allowed a way to introduce some level of semi-controlled "entropy" for the sake of simplicity, while still maintaining a baseline of integrity for most given PRNGs to exercise individual "potential."

The seed generation method we chose derives directly from Microsoft's [.NET system.datetime.ticks](https://docs.microsoft.com/en-us/dotnet/api/system.datetime.ticks?view=netframework-4.8) property. We chose to single out this method due to its documentation and unqiue simplicity, in addition to system time being widely used as a parameter for modern seed generation methods (more on reasoning at the bottom).

> A single tick represents one hundred nanoseconds or one ten-millionth of a second. There are 10,000 ticks in a millisecond, or 10 million ticks in a second. The value of this property represents the number of 100-nanosecond intervals that have elapsed since 12:00:00 midnight, January 1, 0001 in the Gregorian calendar.

**We found this implementation on StackOverflow that ported this method over to python for ease-of-use:**

[Python Implementation of .NET system.datetime.ticks](https://stackoverflow.com/questions/29366914/what-is-python-equivalent-of-cs-system-datetime-ticks)

As noted by the author . . .
   > * UTC times are assumed.
   > * The resolution of the datetime object is given by datetime.resolution, which is datetime.timedelta(0, 0, 1) or microsecond resolution (1e-06 seconds). C# Ticks are purported to be 1e-07 seconds.
   
**The reasoning behind our chosen method:**

This method will allow enough spread between occaisonally retreived ticks, where we can assume reasonable pseudo-unpredictabililty. This serves as a simplistic and constantly changing control mechanism for being able to seed PRNGs and test experimental outcomes. While not the most cryptographically strong, we needed a way to have some controlled aspect of seed generation to feed into generators of varying cryptographic complexity (to have some baseline of comparison).

**Here is a more trivial explanation that we found appropriate to include in summarization:**

[source](https://stackoverflow.com/users/33708/mehrdad-afshari)

> Normally, a (pseudo-)random number generator is a deterministic algorithm that given an initial number (called seed), generates a sequence of numbers that adequately satisfies statistical randomness tests. Since the algorithm is deterministic, the algorithm will always generate the exact same sequence of numbers if it's initialized with the same seed. That's why system time (something that changes all the time) is usually used as the seed for random number generators.


### **PRNG implementations:**


### **Predictive Network Setup:**


### **Experiment Overview:**


### **Environment Setup:**


### **Trials:**