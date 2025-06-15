from pyrealb import *

loadEn()
addToLexicon({"fussy":{"A":{"tab":"a4"}}})

# Illustration of the fact that modifications are "permanent"
cat1=NP(D("the"),N("cat"))
mouse1=NP(D("a"),A("grey"),N("mouse"))

# a simple sentence but ensure creating a new object at each occurrence
cat=lambda:NP(D("the"),N("cat"))
mouse=lambda:NP(D("a"),A("grey"),N("mouse"))
sent=S(cat(),VP(V("eat"),mouse()))


# random NP
def np():
    return NP(D("a"),a(),N(oneOf("cat","mouse","dog","rabbit")).n(oneOf("s","p")))

# random Adjective
def a():
    return oneOf(
        lambda:A(oneOf("hungry","grey","nervous")),
        lambda:Q("")
        )

# random VP or VP,NP
def vp():
    return oneOf(
        lambda:VP(V(oneOf("eat","run","love")).t(oneOf("p","ps","f"))),
        lambda:VP(V(oneOf("eat","love")).t(oneOf("p","ps","f")),np())
    )

def show(exp):
    print(exp.toSource())
    print(exp.realize())
    print("---")

if __name__ == '__main__':
    ## show what happens when modifications directly on objects
    show(S(cat1.n("p"),VP(V("eat"),mouse1.n("p").pro())))
    print('notice that the source is not: S(cat1,VP(V("eat"),mouse1)). It is the same as the previous.')
    show(S(cat1,VP(V("eat"),mouse1))) # bad...
    # instead create new object at each call
    show(S(cat(),VP(V("eat"),mouse())))
    show(S(cat(),VP(V("eat"),mouse())).n("p").t("f"))
    show(S(cat(),VP(V("eat"),mouse())).typ({"pas":True}))
    show(S(cat(),VP(V("eat"),mouse())).typ({"neg":True}))
    show(S(cat(),VP(V("eat"),mouse())).typ({"int":"wos"}))
    show(S(cat(),VP(V("eat"),mouse())).typ({"int":"wos","pas":True,"neg":True}))
    # create many random sentences
    print("======")
    for i in range(0,10):
        show(S(np(),vp()))
