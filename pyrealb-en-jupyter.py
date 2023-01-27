# %% [markdown]
# # Experimenting with `pyrealb`
# 
# This Jupyter notebook shows a few live examples of text realization with **pyrealb**.  
# 
# **pyrealb** is a system for realizing English or French Sentences from a specification given as a Python structure built with constructor and function calls.
# 
# The names of constructors have been chosen to be similar to the usual conventions in constituent grammars: terminals embedded in phrases each of them can be modified by options specified using object property functions. It is also possible to use a dependency syntax notation to build sentences.
# 
# **pyrealb** manages automatically conjugation, declensions and most agreements between constituents. One important feature is the fact that once an affirmative sentence has been defined, many variants (e.g. negative, passive, interrogative, etc.) can be obtained by just adding specific options. Not all options are described in this document, the complete list can be found in the [**pyrealb** documentation](docs/documentation.html).
# 
# This *Jupyter* notebook briefly introduces **pyrealb** syntax with a few simple examples and also shows more challenging ones.  You can modify the examples and immediately see the effects on the realization. Once an expression is modified, it can be executed with (shift-return) or by clicking one of the appropriate buttoons.
# 
# *Nota bene*: When **pyrealb** detects a specification error which often results in realizing a word between double square brackets `[[...]]`, it also writes a warning on the console which is displayed before the result. 
# 
# First import the package and indicate that English text will be realized.

# %%
# uncomment the following two statements at the launch of the notebook
# import sys,os
# sys.path.append(os.path.join(os.path.abspath(""),'src'))
from pyrealb import *
loadEn() 

# %% [markdown]
# ## Creation and realization of a first word
# 
# We call a constructor to create a Python structure, for example to create a noun.

# %%
N('cat')

# %% [markdown]
# This call shows that a Python object of type `Terminal` has been created. As we will show, this object can be saved in a variable, used and modified like any Python object. Its realization is obtained by asking for its string value with `str(..)` (`print(..)` does this implicitely) or by calling the object function property `.realize()`.
# 
# To simplify notation in the rest of this notebook, we define a function to realize each argument and create a string joining the realizations separated by a comma.

# %%
def realize(*exps):
    return ", ".join(exp.realize() for exp in exps)

# %% [markdown]
# It can be called as follows:

# %%
realize(N('cat'),N("dog"))

# %% [markdown]
# ## Terminal creation
# The constructor is called by giving the base form as parameter:
# * singular for an article or a noun

# %%
realize(D("a"),
        N("cat"))

# %% [markdown]
# * infinitive for a verb which is conjugated to the present tense at the 3rd person singular

# %%
realize(V("love"))

# %% [markdown]
# * first person singular for a pronoun which is declined by default at neutral 3rd person singular

# %%
realize(Pro("I"))

# %% [markdown]
# * adjective, adverb, preposition, conjunction and *canned text*, with the base form which is not declined in English

# %%
realize(A("good"),
        Adv("so"),
        P("of"),
        C("or"),
        Q("Wow!!"))

# %% [markdown]
# * date and time specified with the usual JavaScript syntax. When called without argument, it returns the current date and time. We will see later how to display specific fields of a date.

# %%
realize(DT("2020-12-25"),
        DT())

# %% [markdown]
# * number corresponding the numeric value given as parameter

# %%
realize(NO(123),
        NO(45678))

# %% [markdown]
# 


