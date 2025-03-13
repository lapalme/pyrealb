---
title: pyrealb Hacking
author: Guy Lapalme
description: Tricks for modifying pyrealb structures
---

<center style="font-size:3em; font-family: 'Open Sans'; font-weight: bold"><code>pyrealb</code> Hacking</center>
<center><a href="mailto:lapalme@iro.umontreal.ca">Guy Lapalme</a><br/>RALI-DIRO<br/>Université de Montréal<br/>March 2025</center>

[*pyrealb*](https://github.com/lapalme/pyrealb) is a Python package which allows English and French sentence 
realization by programming language instructions that create internal data structures corresponding to the elements of the sentence. The data structure can be built incrementally and, when needed,  the realization process traverses it to produce a string in the appropriate language. 

Python function calls build sentence structures from terminals and properly order words within a sentence, performing the most common agreements between constituents and carrying out other useful sentence organization tasks such as managing coordination or applying sentence transformations. It also performs the spelling out of numbers and the wording of temporal expressions.

The names of the function for building syntactic structures were chosen to be similar to the symbols typically used by linguists for constituent syntax trees and for dependency structures. The following code shows two *pyrealb* expressions that are realized as *'He eats apples. '* when called as `s.realize()` or `r.realize()`.

```python
# CONSTITUENT notation
s = S(                         # Sentence
      Pro("him").c("nom"),     # Pronoun (citation form), nominative case
      VP(V("eat"),             # Verb at present tense by default
         NP(D("a"),            # Noun Phrase, Determiner
            N("apple").n("p")  # Noun plural
           )       
        )
    )
# DEPENDENCY notation
r = root(V("eat"),                  # Sentence with a verb as head, two dependents
         subj(Pro("him").c("nom")), # Subject with a pronoun as head
         comp(N("apple").n("p"),    # Complement with a noun as head
              det(D("a")))          # dependent with a determiner
    )
```

The  previous examples of *pyrealb* expressions were written explicitly in the source programs, but in some contexts, these expressions can be built or modified by programs by invoking *Python* functions. It is only when the `.realize()` function is called that realization choices are made. In some cases (e.g,  negation or passivization), this implies adding word or reorganizing the structure of the original expression.

 *Note*: Although this document describes how to modify *pyrealb* expressions, it applies *mutatis mutandis* to *jsRealB* whose constituent modification API is identical to the one of *pyrealb*.

# `Constituent` organization

In order to modify `pyrealb` constituents, it is important to understand  how they are organized. The following table gives the names of the main classes and *factory* functions that create their instances. 



| Class         | Functions                      |
| ------------- | ------------------------------ |
| `Constituent` |                                |
| `Terminal`    | `N,A,Pro,D,V,Adv,P,C,DT,NO,Q`  |
| `Phrase`      | `NP,AP,VP,AdvP,PP,CP,S,SP`     |
| `Dependent`   | `root,subj,det,comp,mod,coord` |

This diagram shows a simplified inheritance structure with the attributes that are relevant for structure modification. Each block has three parts: the class name, the field names  and the method names associated with an instance of a class that will be described in detail below. The types of the fields and of the parameters and result of methods are also given. When value can be `None`, its type is followed by a question mark.

<img src="./pyrealb-classes.jpg" alt="pyrealb-classes" style="zoom:50%;" />

Internally, [the class structure is more complex with language specific classes and auxiliary ones that are not shown here](./classes-hierarchy.png) as they are not relevant for structure modifications.  

# Exploring an expression

A *pyrealb* expression is a tree of `Constituent` instances: all instances have a `constType` field that indicates its kind and a dictionary of features that will drive the realization process. For a `Terminal` instance, the lemma field is added. Each `Phrase` or `Dependent` instance has a list of children constituents. A `Dependent` instance also has a field for a `Terminal` which is the head of the dependency. 

Most of the modifications imply adding or removing children nodes in `Phrase` or `Dependent`. Properties are usually modified by options using the dotted notation.

## Type checking

- `isinstance(object, class)`: like any Python object, this function can be used for testing if an object is a `Terminal`, a `Phrase` or a `Dependent`.
- `.isA(string,...)` : this method can be used to check if an instance of a `Constituent` is specific `Terminal` (e.g. `N`, `V`...), a `Phrase` (e.g. `NP`, `VP`...) or a `Dependent` (`subj`, `comp`,...). If more than one parameter is given, then the function returns `True` if the object is one of specified *kinds*. Note that the parameter is a *string* which is compared with the `constType` field of the object.

## Showing structure 

- `.toSource(indent=-1)` : returns a string representation of a `Constituent`. If the indent parameter is not specified, the string does not have any newline.  The following is the result of `print(s.toSource())`.

  ```python
  S(Pro("him").c("nom"),VP(V("eat"),NP(D("a"),N("apple").n("p"))))
  ```

  When it is specified (it often starts at 0), it indicates the number of spaces to add before each line to better make the structure of the expression standout.  The following is the result of `print(s.toSource(0))`

  ```python
  S(Pro("him").c("nom"),
    VP(V("eat"),
       NP(D("a"),
          N("apple").n("p"))))
  ```

  The output of `toSource` is a *legal* *pyrealb* expression that can be `eval`ed to recreate the original expression.

- `.toDebug(indent=1)` :   this function was developed for the maintainer for checking if the agreement links were correctly set. To appreciate this output, we refer to the details of a *pyrealb*/*jsRealB* structure and of the realization process explained in section 4 of [this](https://arxiv.org/pdf/2012.15425) document. 

  ```json
  S#1-1(Pro#1("him"){"c": "nom"},
        VP#1-1(V#1-1("eat"),
               NP#4(D#4("a"),
                    N#4("apple"){"cnt": "both", "n": "p"})))
  ```

- .`toJSON()` : a `Constituent` can be *converted* a  Python `dict` which can then be easily transformed to a JSON structure with `json.dumps()`, hence the name of the function.  [This format can be used as input to `jsRealB/pyrealb`](http://rali.iro.umontreal.ca/JSrealB/current/documentation/jsRealB-jsonInput.html) ; it was originally developed to simplify the generation of `pyrealb` expressions from other programming languages.  Here is the output of `pprint(s.toJSON())` where `pprint` is imported from the `pprint` package.

  ```json
  {"elements": [{"lemma": "him", "props": {"c": "nom"}, "terminal": "Pro"},
                {"elements": [{"lemma": "eat", "terminal": "V"},
                              {"elements": [{"lemma": "a", "terminal": "D"},
                                            {"lemma": "apple",
                                             "props": {"cnt": "both", "n": "p"},
                                             "terminal": "N"}],
                               "phrase": "NP"}],
                 "phrase": "VP"}],
   "lang": "en",
   "phrase": "S"}
  ```

## Getting information about a `Constituent`

As with any Python object, the value of a field can be obtained with the dotted notation such as `.lemma` or `.terminal`. It is also possible to change these values, but this is discouraged because of the hidden implications of such direct modifications. One should instead use the [methods described in the documentation](http://rali.iro.umontreal.ca/JSrealB/current/documentation/user.html?lang=en) to modify these fields. The methods for retrieving values are the following:

- `.getProp(key)`  the value of a property corresponding to a key (a string) including the shared values between `Constituent`s.
- `.nbConstituents()` : the number of `Element`s of a `Phrase` or the number of `Dependent`s of a `Dependent`
- `.constituents()`:. the list of `Element`s of a `Phrase` or the number of `Dependent`s of a `Dependent`

## Cloning a `Constituent`

- `.clone()` : create a copy of a `Constituent` because the realization process can change its structure. 

- Another way of creating a copy of an expression is to create a function or a *lambda* with the expression as body and call it when needed.  For example given the following definition:

  ```python
  sL = lambda: S(Pro("him").c("nom"),
                 VP(V("eat"),
                    NP(D("a"),
                       N("apple").n("p"))))
  ```

  A fresh copy of this expression is created at each `sL()` call.

#  Modifying an expression

Before the final realization, an expression can be modified by adding or removing parts of it. This useful iwhen not all arguments to a phrase are known before starting to build it. For example, its subject and verb can be determined in one part of a program, but its complements only specified later. Many coordinated constituents are built incrementally.

To account for this possibility, `pyrealb` allows adding a new `Constituent` to an existing `Phrase` or a new `Dependent` to another `Dependent` at a given position within its children.  It is also possible to remove a `Constituent`, although this is most often used internally during the realization process.  

As these methods return the modified constituent, calls can be chained as in the following examples, although in practice such calls are seldom encountered because it would have been simpler to create the structure by the original functions. Most often adding or removing constituents is done incrementally in different places during the course of execution of the program.

- for a `Phrase`:

  - `.add(constituent,position=None)`:  insert either a `Phrase` or a `Terminal` to the current `Phrase` at a certain position given by a non-negative index when specified, at the end otherwise. 

    ```python
    s1 = S(Pro("him").c("nom"),
           VP(V("eat"),
              NP(D("a"),N("apple").n("p")).add(A("red")))
           ).add(Adv("now").a(","),0)
    ```

    `s1.realize()` returns *Now, he eats red apples.* The adjective *red* is added at the end of the *NP* but, because adjectives in English are placed before the noun, it is realized before the noun. The adverb *now* followed by comma is inserted at the start of the sentence because the position is set to 0. 

    This can be seen by  the result of the `s1.toSource(0)` call, which corresponds to the modified structure. 


    ```python
    S(Adv("now").a(','),
      Pro("him").c("nom"),
      VP(V("eat"),
         NP(D("a"),
            N("apple").n("p"),
            A("red"))))
    ```

  - `.remove(position)`: delete the `Constituent` at a given position within a `Phrase`

- For a `Dependent`:

  - `.add(dependent,position=None)`:  insert either `Dependent` to the current `Dependent` at a certain position given by a non-negative index when specified, at the end otherwise. A `Dependent` cannot be created empty,  its head, a `Terminal`, must always be specified. The following *Python* expression split on many lines to make `.add()` calls standout.

    ```python
    r1 = root(V("eat"))\
              .add(subj(Pro("him").c("nom")))\
              .add(comp(N("apple").n("p"),
                        det(D("a"))))\
              .add(det(Adv("now").a(",")),0)
    ```

    `r1.realize()` returns *Now, he eats red apples.* The resulting structure shown by `r1.toSource(0)` is the following. 

    ```python
    root(V("eat"),
         det(Adv("now").a(',')),
         subj(Pro("him").c('nom')),
         comp(N("apple").n('p'),
              det(D("a"))))
    ```

    We see that the last `Dependent` added is now the first dependency because its position was specified as 0. In order to be realized at the start of the sentence, a `det` `Dependent` was used; a `subj` would also have been possible. As dependency structures are less position dependent than constituency  ones, the `position` argument is seldom needed for `Dependent`s.  In this specific example, the realization would have been the same without specifying the position, because `det` or `subj` are always realized before the head.

  - `.remove(position)`: delete the `Dependent` at a given position within a `Dependent`

These dynamic modifications explain why, in *pyrealb*,  most realization decisions are taken at the very last moment (i.e., when `.realize()` is called) and not while the structure is being built. Internally,  `.add(...)`  is used by `pyrealb` to build constituent expressions. 

## An alternative to structure modifications

Given the fact  that `pyrealb` expressions are *Python* objects,  they can be inserted in a list (or a tuple) and manipulated by standard *Python* functions. The list can then be used as a parameter for `pyrealb` creation functions which *flatten* their list or tuple arguments before building the structure.  Here is an example of incrementally building the `pyrealb` expression `s2` equivalent to `s1`.

```python
n = [D("a"),N("apple").n("p")]
n.append(A("red"))
vp = (VP(V("eat"),NP(n)))
selems = [Pro("him").c("nom"),vp]
selems.insert(0,Adv("new").a(","))
s2 = S(selems)
```

# Conclusion

This note has described how to dynamically modify existing `pyrealb` structures before their realization. This process is only briefly described in the `pyrealb` documentation, but we felt that it deserved a more comprehensive description.

