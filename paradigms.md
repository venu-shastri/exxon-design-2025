# exxon-design-2025

### Requirement

> "Exxon","Mobil", "Bangalore" , "Bdd", "Encapsulation"

- Get List of strings where each item begin with "E"
- C# - No LINQ
- JAVA - NO Stream
- TypeScript - No Map/Reduce/Filter
- Python - No Built in Reduce api's


### Separation of source, iterator and predicate

``` Python Code
# Source
words = ["Exxon", "Mobil", "Bangalore", "Bdd", "Encapsulation"]

# Predicate
def starts_with_e(word: str) -> bool:
    return word.startswith("E")

def starts_with_b(word: str) -> bool:
    return word.startswith("B")

# Iterator
def filter_words(source, predicate):
    for w in source:
        if predicate(w):
            yield w

# Usage
result = list(filter_words(words, starts_with_e))
print("Words starting with 'E':", result)
result = list(filter_words(words, starts_with_b))
print("Words starting with 'B':", result)



```

``` csharp
using System;
using System.Collections.Generic;

class Program
{
    // Predicate
    static bool StartsWithE(string word) => word.StartsWith("E");
static bool StartsWithB(string word) => word.StartsWith("B");

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
        result = FilterWords(words, StartsWithB)
        Console.WriteLine("Words starting with 'B': " + string.Join(", ", result));
    }
}

```

### Using Closures
``` python
def starts_with(letter):
    def predicate(word):
        return word.startswith(letter)  # uses 'letter' from outer function
    return predicate  # return the inner function

# Create closures
starts_with_e = starts_with("E")
starts_with_b = starts_with("B")

print(starts_with_e("Exxon"))  # True
print(starts_with_b("Bangalore"))  # True

```

``` charp
Func<string, Func<string, bool>> StartsWith = letter =>
{
    return word => word.StartsWith(letter); // captures "letter"
};

var startsWithE = StartsWith("E");
var startsWithB = StartsWith("B");

Console.WriteLine(startsWithE("Exxon"));      // True
Console.WriteLine(startsWithB("Bangalore")); // True

```

### Object Orientation
```
words = ["Exxon", "Mobil", "Bangalore", "Bdd", "Encapsulation"]

# Predicate as a class
class StartsWith:
    def __init__(self, letter):
        self.letter = letter
    
    def matches(self, word):
        return word.startswith(self.letter)

# Iterator as a function
def filter_words(source, predicate_obj):
    for w in source:
        if predicate_obj.matches(w):
            yield w

# Usage
starts_with_e = StartsWith("E")
starts_with_b = StartsWith("B")

print("Starts with E:", list(filter_words(words, starts_with_e)))
print("Starts with B:", list(filter_words(words, starts_with_b)))


```
```
using System;
using System.Collections.Generic;

class StartsWith
{
    private string _letter;

    public StartsWith(string letter)
    {
        _letter = letter;
    }

    public bool Matches(string word)
    {
        return word.StartsWith(_letter);
    }
}

class Program
{
    static IEnumerable<string> FilterWords(IEnumerable<string> source, StartsWith predicateObj)
    {
        foreach (var word in source)
        {
            if (predicateObj.Matches(word))
                yield return word;
        }
    }

    static void Main()
    {
        var words = new List<string> { "Exxon", "Mobil", "Bangalore", "Bdd", "Encapsulation" };

        var startsWithE = new StartsWith("E");
        var startsWithB = new StartsWith("B");

        Console.WriteLine("Starts with E: " + string.Join(", ", FilterWords(words, startsWithE)));
        Console.WriteLine("Starts with B: " + string.Join(", ", FilterWords(words, startsWithB)));
    }
}
```

### Contract Driven : using Encapsulation and Abstarction + Runtime Polymorphism
```
from abc import ABC, abstractmethod

words = ["Exxon", "Mobil", "Bangalore", "Bdd", "Encapsulation"]

# Interface
class Predicate(ABC):
    @abstractmethod
    def matches(self, word: str) -> bool:
        pass

# Implementation: StartsWith
class StartsWith(Predicate):
    def __init__(self, letter: str):
        self.letter = letter
    
    def matches(self, word: str) -> bool:
        return word.startswith(self.letter)

# Implementation: StartsWith
class EndsWith(Predicate):
    def __init__(self, letter: str):
        self.letter = letter
    
    def matches(self, word: str) -> bool:
        return word.endswith(self.letter)


# Iterator
def filter_words(source, predicate_obj: Predicate):
    for w in source:
        if predicate_obj.matches(w):
            yield w

# Usage
starts_with_e = StartsWith("E")
starts_with_b = StartsWith("B")

print("Starts with E:", list(filter_words(words, starts_with_e)))
print("Starts with B:", list(filter_words(words, starts_with_b)))
```

```
using System;
using System.Collections.Generic;

// Interface
interface IPredicate
{
    bool Matches(string word);
}

// Implementation: StartsWith
class StartsWith : IPredicate
{
    private string _letter;

    public StartsWith(string letter)
    {
        _letter = letter;
    }

    public bool Matches(string word)
    {
        return word.StartsWith(_letter);
    }
}

// Implementation: StartsWith
class EndsWith : IPredicate
{
    private string _letter;

    public StartsWith(string letter)
    {
        _letter = letter;
    }

    public bool Matches(string word)
    {
        return word.EndsWith(_letter);
    }
}
class Program
{
    // Iterator
    static IEnumerable<string> FilterWords(IEnumerable<string> source, IPredicate predicateObj)
    {
        foreach (var word in source)
        {
            if (predicateObj.Matches(word))
                yield return word;
        }
    }

    static void Main()
    {
        var words = new List<string> { "Exxon", "Mobil", "Bangalore", "Bdd", "Encapsulation" };

        IPredicate startsWithE = new StartsWith("E");
        IPredicate startsWithB = new StartsWith("B");

        Console.WriteLine("Starts with E: " + string.Join(", ", FilterWords(words, startsWithE)));
        Console.WriteLine("Starts with B: " + string.Join(", ", FilterWords(words, startsWithB)));
    }
}
```
