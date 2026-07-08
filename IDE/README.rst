*******************************************
*pyrealb* Interactive Development Environment
*******************************************

One way of testing and developing ``pyrealb`` expressions is to use the development environment
built on top of the standard Python 3 *Read-Eval-Print* loop.

The system is started by typing launching a Python 3 interpreter and, at the Python prompt, typing::

    from ide import *

which imports all public ``pyrealb`` constructors and functions and loads the English lexicon and rule sets.
It then displays the version and Python prompt::

    ** pyrealb 1.0 Interactive Development Environment [_help() for info]
    English rules and lexicon loaded
    >>>

A *pyrealb* expression can be evaluated to return a ``Constituent`` object that could be modified.
Its realization is obtained using the ``str`` function. For example::

    >>> s=S(NP(D("the"),N("cat")).n("p"),VP(V("sit")))
    >>> s
    <Phrase.S object at 0x104246ef0>
    >>> str(s)
    'The cats sit.'

The IDE defines the unary plus operator for a ``Constituent`` which prints its realization, thus not showing outer string quotes. So to display only the realization, instead of typing ``print(str(s))``, we can use::

    +s
    The cats sit.

The IDE also defines utility functions with names starting with an underscore.

    * Show information about the lexicon entries:
        * ``_lm(word)``: *lemmatize* a word by giving ``pyrealb`` expressions that can realize this word
        * ``_lx(lemma)``: show the lexical information associated with this lemma

    * Show information about the declension and conjugation tables:
        * ``_cn(no)``: show conjugation table ``no``
        * ``_dn(no)``: show declension table ``no``
        * ``_ce(end)``: show conjugation table for verbs ending with ``end``
        * ``_dn(end)``: show declension table for words ending with ``end``

    * Change the current realization language:
        * ``_en()``: set the current language to English
        * ``_fr()``: set the current language to French

    * Briefly remind the special commands of the IDE: ``_help()``

These commands also accept as parameter a regular expression instead of a specific value, in which case they will return the result for each form that matches the regular expression.

Examples of use
***************

    >>> _lm("checks")  # show how to realize "check"
    N("check").n("p")
    V("check")

    >>> _lm("him")   # whow how to realize "him"
    Pro("me").g("m").tn("")
    Pro("me").g("m").c("acc")
    Pro("me").g("m").c("dat")
    Pro("him").g("m").tn("")
    Pro("him").g("m").c("acc")
    Pro("him").g("m").c("dat")

    >>> _lx("check")   # show lexical information about a lemma
    check:{"N":{"tab":"n1"},
           "V":{"tab":"v1"},
           "basic":true}

    >>> _lx("check.*") # show lexical information about lemmata matching a pattern
    check:{"N":{"tab":"n1"},
           "V":{"tab":"v1"},
           "basic":true}
    check-list:{"N":{"tab":"n1"}}
    check-out:{"N":{"tab":"n1"}}
    checkbook:{"N":{"tab":"n1"}}
    checked:{"A":{"tab":"a1"}}
    checker:{"N":{"tab":"n1"},
             "V":{"tab":"v1"}}
    checkers:{"N":{"tab":"n5"}}
    checkmate:{"N":{"tab":"n1"},
               "V":{"tab":"v3"}}
    checkout:{"N":{"tab":"n1"}}
    checkpoint:{"N":{"tab":"n1"}}
    checkroom:{"N":{"tab":"n1"}}
    checkup:{"N":{"tab":"n1"}}

    >>> _ce("ve")   # find the table corresponding to an ending
    v83:{"ending":"ve",
         "t":{"b":"ve",
              "ps":"d",
              "pr":"ving",
              "pp":"d",
              "p":["ve","ve","s","ve","ve","ve"]}}

    >>> _fr()     # load the French table and work in French
    Règles et lexique français chargés

    >>> f=S(NP(D("le"),N("chat")).n("p"),VP(V("asseoir")).typ({"refl":True})) # realize a sentence in French
    >>> +f
    Les chats s'assoient.

    >>> +S(NP(D("un"),N("chat")).n("p"),VP(V("être"),A("populaire"),PP(P("sur"),N("Facebook"))))
    N('Facebook'):: absent du lexique français.
    Des chats sont populaires sur [[Facebook]].

As *Facebook* is not in the French lexicon, we add it. First find a lexicon entry
with the same ending. Here, we look for words ending in *ok*

    >>> >>> _lx(".*ok")
    amok:{"N":{"g":"m",
               "tab":"n3"}}
    chinook:{"N":{"g":"m",
                  "tab":"n3"}}
    flock-book:{"N":{"g":"m",
                     "tab":"n3"}}
    kapok:{"N":{"g":"m",
                "tab":"n3"}}
    new-look:{"N":{"g":"m",
                   "tab":"n2"}}

We choose *flock-book* as our model and copy its lemma information for *Faceebook*.
The realization does not raise a warning anymore.

    >>> getLemma("flock-book")
    {'N': {'g': 'm', 'tab': 'n3'}}
    >>> addToLexicon("Facebook",{'N': {'g': 'm', 'tab': 'n3'}})
    {'N': {'g': 'm', 'tab': 'n3'}}

    >>> +S(NP(D("un"),N("chat")).n("p"),VP(V("être"),A("populaire"),PP(P("sur"),N("Facebook"))))
    Des chats sont populaires sur Facebook.

`Guy Lapalme <mailto:lapalme@iro.umontreal.ca>`_