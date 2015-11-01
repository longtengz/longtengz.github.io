Title: Why bother to have type definitions if we already have macros?
Date: 2015-11-01 15:49
Modified: 2015-11-01 15:50
Category: Programming Languages
Tags: C 
Authors: Teng Long 

#### Macro Definitions

**Macro definitions** are recognized during preprocessing phase, and macro names are naively replaced by the preprocessor.

Consider following example:

```C
#define Int_Ptr (int *)

Int_Ptr a, b, c;
```

In the above case, only `a` will be defined as a pointer pointed to and Integer, whereas `b` and `c` are two Integers.

Preprocessor just replace macro names as it sees them, so after preprocessing the above code becomes:


```C
int * a, b, c;
```

Similar to pointers, array types can't be defined as macros either.


#### Type Definitions

**Type definitions** are not preprocessed directives but compiled statements. They literally define a new type. So it can define new pointer and array types which macro definitions cannot.


```C
typedef int* Int_ptr;

Int_Ptr a, b, c;

typedef char Char_Arr[10];

Char_Arr x, y;
```
The above code will give us 3 Integer pointers and 2 arrays of 10 characters.

One of the biggest differences is that type definitions are subject to the same scope rules are variables, that is a `typedef` defined typed in a function body will not be recognized outside that function. However, macro names will be replaced everywhere in the source file as long as the preprocessor finds a macro.



