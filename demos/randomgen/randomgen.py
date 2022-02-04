from context import pyrealb
from pyrealb.all import *

loadEn();
addToLexicon({"fussy":{"A":{"tab":"a4"}}});
# a simple sentence
cat=NP(D("the"),N("cat"));
mouse=NP(D("a"),A("grey"),N("mouse"));
sent=S(cat,VP(V("eat"),mouse));

# modifications are "permanent"
cat1=NP(D("the"),N("cat"));
mouse1=NP(D("a"),A("grey"),N("mouse"));

# modifications are "permanent"
cat2=NP(D("the"),N("cat"));
mouse2=NP(D("a"),A("grey"),N("mouse"));

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
    print(str(exp))
    print("---")

if __name__ == '__main__':
    show(S(cat,VP(V("eat"),mouse)));
    show(S(cat,VP(V("eat"),mouse)).n("p").t("f"));
    show(S(cat,VP(V("eat"),mouse)).typ({"pas":True}));
    show(S(cat,VP(V("eat"),mouse)).typ({"neg":True}));
    show(S(cat,VP(V("eat"),mouse)).typ({"int":"wos"}));
    show(S(cat,VP(V("eat"),mouse)).typ({"int":"wos","pas":True,"neg":True}));

    show(S(cat1.n("p"),VP(V("eat"),mouse1.n("p").pro())));
    show(S(cat1,VP(V("eat"),mouse1))); # bad...
    # clone before modification

    show(S(eval(cat.toSource()).n("p"),VP(V("eat"),eval(mouse.toSource()).n("p").pro())))
    show(S(cat,VP(V("eat"),mouse)))
    for i in range(0,10):
        show(S(np(),vp()))
