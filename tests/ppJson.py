import json

## to sort object fields without accents
import unicodedata
def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str.decode("utf-8"))
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

#### prettyprint a JSON in more compact format
##   that I find more readable
def ppJson(file,obj,level=0,sortkeys=False,max_length=100):
    # auxiliary function that creates a string
    def pp(obj,level,res):
        def out(s):
            nonlocal res
            res += s

        def quoted(s):
            if '\\' in s: s = s.replace('\\', '\\\\')
            if '"' in s: s = s.replace('"', '\\"')
            if '\n' in s: s = s.replace('\n', '\\n')
            return '"' + s + '"'

        if isinstance(obj,str):
            out(quoted(obj))
        elif obj==None:
            out("null")
        elif type(obj) is bool:
            out("true" if obj else "false")
        elif isinstance(obj,(int,float)):
            out(str(obj))
        elif type(obj) is dict:
            keys=list(obj.keys())
            if sortkeys: keys.sort(key=remove_accents)
            out("{"+
                (",\n"+(level+1)*" ").join(map(lambda key:quoted(key)+":"+pp(obj[key],level+1+len(key)+3,""),keys))
                +"}")
        elif type(obj) is list:
            children = list(map(lambda elem:pp(elem,level+1,"") ,obj))
            indent = any(map(lambda elem: isinstance(elem,(list,dict)),obj))
            if not indent: # check if all children fit on the same line
                if sum(map(lambda e:len(e),children))+len(list(children))+level+2 > max_length:
                    indent = True
            out("[" + ((",\n" + (level + 1) * " ") if indent else ",").join(children)+ "]")
        return res
    file.write(pp(obj,level,""))
    file.write("\n")

if __name__ == '__main__':
    import sys
    ppJson(sys.stdout,
           {"hello":"world",
            "my":["dear",1.45,"friends",None],
            "array":[1,3,True,False,None,{"a":"b"},["a","b","c","one very very long string",345.0]],
            "anotherarray":["one very very long string","a second very long string",2345.02,True,
                       "Finally another super-long string that should not fit on a single line"]})

