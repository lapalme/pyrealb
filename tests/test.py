def test(title,lang,testsFn,kept=None,badOnly=False):
    print("===",title,"===")
    nbTests=0
    nbOK=0
    for i,s in enumerate(testsFn()):
        if kept is None or i in kept:
            if "expression" in s:
                nbTests+=1
                try:
                    expression=s["expression"]
                    expected=s["expected"]
                    message=s["message"]
                    realized=expression.realize()
                    if expected is None or realized==expected:
                        nbOK+=1
                        if not badOnly:
                            print("OK",i,message)
                            print(realized)
                            print("---")
                    else:
                        print("KO",i,message)
                        print(expression.toSource())
                        print(realized)
                        print(expected)
                        print("---")
                except Exception as e:
                    print("**** Exception: ",repr(e))
                    print(expression.toSource())
                    print(expected)
                    print("---")

    print(nbOK,"réussites sur" if lang=="fr" else "successes over",nbTests)
    print("="*40+"\n")
    return (nbOK,nbTests)

if __name__ == '__main__':
    pass