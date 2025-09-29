# exxon-design-2025

### Requirement

> "Exxon","Mobil", "Bangalore" , "Bdd", "Encapsulation"

- Get List of strings where each item begin with "E"
- C# - No LINQ
- JAVA - NO Stream
- TypeScript - No Map/Reduce/Filter
- Python - No Built in Reduce api's


### Separation of source, iterator and predicate

```
#Python Code
# Source
words = ["Exxon", "Mobil", "Bangalore", "Bdd", "Encapsulation"]

# Predicate
def starts_with_e(word: str) -> bool:
    return word.startswith("E")

# Iterator
def filter_words(source, predicate):
    for w in source:
        if predicate(w):
            yield w

# Usage
result = list(filter_words(words, starts_with_e))
print("Words starting with 'E':", result)


```

```
//C#
using System;
using System.Collections.Generic;

class Program
{
    // Predicate
    static bool StartsWithE(string word) => word.StartsWith("E");

    // Iterator
    static IEnumerable<string> FilterWords(IEnumerable<string> source, Func<string, bool> predicate)
    {
        foreach (var word in source)
        {
            if (predicate(word))
                yield return word;
        }
    }

    static void Main()
    {
        // Source
        List<string> words = new List<string> { "Exxon", "Mobil", "Bangalore", "Bdd", "Encapsulation" };

        var result = FilterWords(words, StartsWithE);

        Console.WriteLine("Words starting with 'E': " + string.Join(", ", result));
    }
}



```
