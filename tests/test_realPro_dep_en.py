import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..','src')))

from pyrealb import *
load("en")

addToLexicon("John",{"N":{"tab":"nI","g":"m"}})
addToLexicon("Mary",{"N":{"tab":"nI","g":"f"}})
addToLexicon("Fred",{"N":{"tab":"nI","g":"m"}})
addToLexicon("Maria-Luz",{"N":{"tab":"nI","g":"f"}})
addToLexicon("firefighter",getLemma("fighter"))

def test_realPro_dep_en_1():
    assert (
root(V("see").t('ip').pe(1).n('p'),
     comp(Pro("something")),
     comp(V("get").t('ps'),
          subj(Pro("I").pe(1)),
          comp(P("for"),
               comp(Pro("me").pe(2))))).realize()   
    ) == "Let's see something I got for you. ",\
    './letssee.dss'


def test_realPro_dep_en_2():
    assert (
root(V("love"),
     subj(N("John")),
     comp(N("Mary"))).typ({'neg': True}).realize()   
    ) == 'John does not love Mary. ',\
    './Examples_from_User_Manual/10-John-does-not-love-Mary.dss'


def test_realPro_dep_en_3():
    assert (
root(V("be"),
     subj(Pro("there").n('p')),
     mod(N("firefighter"),
         det(D("a"))).n('p'),
     mod(A("available")),
     comp(P("in"),
          comp(N("city"),
               det(D("this"))))).typ({'neg': True, 'perf': True, 'int': 'yon'}).realize()   
    ) == 'Have there not been firefighters available in this city? ',\
    './Examples_from_User_Manual/11-Have-there-not-been-firefighters.dss'


def test_realPro_dep_en_4():
    assert (
root(V("love"),
     subj(N("John")),
     comp(N("Mary"))).realize()   
    ) == 'John loves Mary. ',\
    './Examples_from_User_Manual/11-John-loves-Mary.dss'


def test_realPro_dep_en_5():
    assert (
root(V("tell"),
     subj(N("John")),
     comp(N("Mary")),
     comp(N("story"),
          det(D("a")))).realize()   
    ) == 'John tells Mary a story. ',\
    './Examples_from_User_Manual/11-John-tells-Mary-a-story.dss'


def test_realPro_dep_en_6():
    assert (
root(V("see").t('ps'),
     subj(Pro("I").pe(1)),
     comp(V("eat").t('pr'),
          subj(N("John")),
          comp(N("bean").n('p')))).realize()   
    ) == 'I saw John eating beans. ',\
    './Examples_from_User_Manual/12-I-saw-John-eating-beans.dss'


def test_realPro_dep_en_7():
    assert (
root(V("tell").t('ps'),
     subj(Pro("I").pe(1)),
     comp(N("Mary")),
     comp(Pro("that"),
          comp(V("eat").t('p'),
               subj(N("John")),
               comp(N("bean").n('p'))))).realize()   
    ) == 'I told Mary that John eats beans. ',\
    './Examples_from_User_Manual/12-I-told-Mary-that-John-eats-beans.dss'


def test_realPro_dep_en_8():
    assert (
root(V("bother").t('p'),
     subj(Pro("I")),
     comp(N("Mary")),
     comp(Pro("that"),
          comp(V("see").t('p'),
               subj(N("John")),
               comp(Pro("myself").g('m'))).typ({'neg': True, 'mod': 'poss'}))).realize()   
    ) == 'It bothers Mary that John cannot see himself. ',\
    './Examples_from_User_Manual/12-It-bothers-Mary-that-John-can-not.dss'


def test_realPro_dep_en_9():
    assert (
root(V("be").t('c'),
     subj(Pro("I")),
     mod(A("horrible")),
     comp(P("for"),
          comp(V("see").t('b'),
               subj(N("John")),
               mod(P("to")).pos('pre'),
               comp(Pro("myself").g('m'))))).realize()   
    ) == 'It would be horrible for John to see himself. ',\
    './Examples_from_User_Manual/12-It-would-be-horrible-for-John-to.dss'


def test_realPro_dep_en_10():
    assert (
root(V("wonder"),
     subj(N("authority"),
          det(D("the"))).n('p'),
     comp(V("give").t('ps'),
          subj(Pro("who")),
          comp(N("book").n('p')),
          comp(Pro("whom"),
               mod(P("to")).pos('pre')))).typ({'prog': True}).realize()   
    ) == 'The authorities are wondering who gave books to whom. ',\
    './Examples_from_User_Manual/13-The-authorities-are-wondering-who-whom.dss'


def test_realPro_dep_en_11():
    assert (
root(P("under"),
     comp(Pro("which"),
          comp(N("bridge"))),
     mod(V("sleep").t('ps'),
         subj(N("Maria-Luz"))).typ({'int': 'yon'})).realize()   
    ) == 'Under which bridge did Maria-Luz sleep? ',\
    './Examples_from_User_Manual/13-Under-which-bridge-did-Maria-Luz-sleep.dss'


def test_realPro_dep_en_12():
    assert (
root(V("like"),
     comp(N("John")),
     subj(N("Mary"))).typ({'int': 'wos'}).realize()   
    ) == 'Who likes John? ',\
    './Examples_from_User_Manual/13-Who-likes-John.dss'


def test_realPro_dep_en_13():
    assert (
root(V("like"),
     comp(N("John")),
     subj(N("Mary"))).typ({'int': 'wod'}).realize()   
    ) == 'Whom does Mary like? ',\
    './Examples_from_User_Manual/13-Whom-does-Mary-like.dss'


def test_realPro_dep_en_14():
    assert (
root(V("sleep"),
     mod(Adv("admittedly")).pos('pre').a(','),
     subj(N("Maria-Luz")).pro(True),
     mod(Adv("really")),
     mod(Adv("very")),
     mod(Adv("soundly")),
     comp(Pro("there")),
     mod(Adv("now"))).typ({'prog': True}).realize()   
    ) == 'Admittedly, she is sleeping really very soundly there now. ',\
    './Examples_from_User_Manual/14-Admittedly,-she-is-really-sleeping-very-soundly.dss'


def test_realPro_dep_en_15():
    assert (
root(V("do").t('c'),
     comp(C("if"),
          comp(V("have").t('ps'),
               subj(Pro("you")),
               comp(N("money")))).pos('pre'),
     subj(Pro("I").pe(1)),
     comp(Pro("anything")),
     comp(P("for"),
          mod(Pro("you")))).realize()   
    ) == 'If you had money I would do anything for you. ',\
    './Examples_from_User_Manual/14-If-you-had-money.dss'


def test_realPro_dep_en_16():
    assert (
root(V("eat"),
     subj(N("John")),
     comp(N("bean").n('p')),
     comp(Adv("often"))).realize()   
    ) == 'John eats beans often. ',\
    './Examples_from_User_Manual/14-John-eats-beans-often.dss'


def test_realPro_dep_en_17():
    assert (
root(V("eat"),
     subj(N("John")),
     comp(N("bean").n('p')),
     comp(Adv("often")).pos('pre')).realize()   
    ) == 'John often eats beans. ',\
    './Examples_from_User_Manual/14-John-often-eats-beans.dss'


def test_realPro_dep_en_18():
    assert (
root(V("eat"),
     comp(Adv("often")).pos('pre').a(','),
     subj(N("John")),
     comp(N("bean").n('p'))).realize()   
    ) == 'Often, John eats beans. ',\
    './Examples_from_User_Manual/14-Often,-John-eats-beans.dss'


def test_realPro_dep_en_19():
    assert (
root(V("eat"),
     comp(Adv("often")).pos('pre'),
     subj(N("John")),
     comp(N("bean").n('p'))).realize()   
    ) == 'Often John eats beans. ',\
    './Examples_from_User_Manual/14-Often-John-eats-beans.dss'


def test_realPro_dep_en_20():
    assert (
coord(C("but"),
      root(V("laugh").t('ps'),
           subj(N("John"))),
      root(V("smack").t('ps'),
           subj(N("Mary")),
           coord(C("and"),
                 comp(N("butler"),
                      det(D("the"))),
                 comp(N("maid"),
                      det(D("the")))))).realize()   
    ) == 'John laughed but Mary smacked the butler and the maid. ',\
    './Examples_from_User_Manual/15-John-laughed-but-Mary-smacked-butler&.dss'


def test_realPro_dep_en_21():
    assert (
root(V("see").t('ps'),
     subj(Pro("I").pe(1)),
     comp(N("Fred").a(','),
          comp(V("drink").t('ps'),
               subj(Pro("who")),
               comp(N("martini"),
                    det(D("a")))).typ({'prog': True}))).realize()   
    ) == 'I saw Fred, who was drinking a martini. ',\
    './Examples_from_User_Manual/16-I-saw-Fred,-who-was-drinking-a-martini.dss'


def test_realPro_dep_en_22():
    assert (
root(V("see").t('ps'),
     subj(Pro("I").pe(1)),
     comp(N("guy").n('p'),
          det(D("the")),
          comp(V("drink").t('ps'),
               subj(Pro("who")),
               comp(N("martini").n('p'),
                    det(D("a")))).typ({'prog': True}))).realize()   
    ) == 'I saw the guys who were drinking martinis. ',\
    './Examples_from_User_Manual/16-I-saw-the-guys-who-were-drinking-martinis.dss'


def test_realPro_dep_en_23():
    assert (
root(V("attack").t('pp'),
     comp(P("by"),
          mod(N("Mary"))),
     subj(N("guy"),
          det(D("the"))).n('p')).realize()   
    ) == 'The guys attacked by Mary. ',\
    './Examples_from_User_Manual/16-The-guys-attacked-by-Mary.dss'


def test_realPro_dep_en_24():
    assert (
root(V("be"),
     subj(Pro("this")),
     comp(N("test"),
          det(D("a")))).cap(False).a('.').realize()   
    ) == 'this is a test. ',\
    './Examples_from_User_Manual/17-this-is-a-test.dss'


def test_realPro_dep_en_25():
    assert (
root(V("love"),
     subj(N("John")),
     comp(N("Mary"))).ba('(').realize()   
    ) == '(John loves Mary) ',\
    './Examples_from_User_Manual/18-(John-loves-Mary).dss'


def test_realPro_dep_en_26():
    assert (
root(V("be"),
     subj(Pro("this")),
     comp(Q("CoGenTex").tag("a",{'href': 'http:#www.cogentex.com'}))).realize()   
    ) == 'This is <a href="http:#www.cogentex.com">CoGenTex</a>. ',\
    './Examples_from_User_Manual/19-HTML-This-is-CoGenTex.dss'


def test_realPro_dep_en_27():
    assert (
Q("**&FuN aNd GaMeS&**.").realize()   
    ) == '**&FuN aNd GaMeS&**.',\
    './Examples_from_User_Manual/4-Fun-and-Games.dss'


def test_realPro_dep_en_28():
    assert (
Q("Mesmerizingly").a('.').realize()   
    ) == 'Mesmerizingly. ',\
    './Examples_from_User_Manual/4-Mesmerizingly.dss'


def test_realPro_dep_en_29():
    assert (
root(Q("Yemen"),
     det(D("the"))).realize()   
    ) == 'The Yemen. ',\
    './Examples_from_User_Manual/5-The-Yemen.dss'


def test_realPro_dep_en_30():
    assert (
root(N("car"),
     det(D("this"))).n('p').realize()   
    ) == 'These cars. ',\
    './Examples_from_User_Manual/5-These-cars.dss'


def test_realPro_dep_en_31():
    assert (
root(N("tiara")).n('p').realize()   
    ) == 'Tiaras. ',\
    './Examples_from_User_Manual/5-Tiaras.dss'


def test_realPro_dep_en_32():
    assert (
root(NO("14"),
     det(D("all")),
     comp(P("of"),
          comp(N("duck").n('p'),
               det(D("the"))))).realize()   
    ) == 'All 14 of the ducks. ',\
    './Examples_from_User_Manual/6-All-14-of-the-ducks.dss'


def test_realPro_dep_en_33():
    assert (
root(D("all"),
     comp(N("duck").n('p'),
          det(D("the")))).realize()   
    ) == 'All the ducks. ',\
    './Examples_from_User_Manual/6-All-the-ducks.dss'


def test_realPro_dep_en_34():
    assert (
root(N("duck"),
     det(NO("6").nat(True),
         mod(Adv("more"),
             comp(P("than"))).pos('pre'))).realize()   
    ) == 'More than six ducks. ',\
    './Examples_from_User_Manual/6-More-than-6-ducks.dss'


def test_realPro_dep_en_35():
    assert (
root(N("duck"),
     det(NO("4").nat(True),
         det(D("the")))).realize()   
    ) == 'The four ducks. ',\
    './Examples_from_User_Manual/6-The-four-ducks.dss'


def test_realPro_dep_en_36():
    assert (
root(N("definition"),
     mod(N("friend"),
         det(D("my").pe(1).ow('p')),
         det(V("esteem").t('pp'))).a("'s").pos('pre'),
     det(NO("2").nat(True)),
     mod(A("bland")),
     comp(P("of"),
          comp(N("happiness")))).realize()   
    ) == "Our esteemed friend's two bland definitions of happiness. ",\
    './Examples_from_User_Manual/7-Our-esteemed-friend.dss'


def test_realPro_dep_en_37():
    assert (
root(V("be").t('c'),
     subj(Pro("anything"),
          mod(Adv("almost")).pos('pre'),
          mod(Adv("else"))),
     comp(Pro("something"),
          mod(A("new")).pos('post'))).realize()   
    ) == 'Almost anything else would be something new. ',\
    './Examples_from_User_Manual/8-Almost-anything-else-would-be-something-new.dss'


def test_realPro_dep_en_38():
    assert (
root(V("do").t('c'),
     subj(Pro("I").pe(1)),
     comp(Pro("anything")),
     comp(P("for"),
          comp(N("girl"),
               det(D("the"))).pro(True))).realize()   
    ) == 'I would do anything for her. ',\
    './Examples_from_User_Manual/8-I-would-do-anything.dss'


def test_realPro_dep_en_39():
    assert (
root(V("see"),
     subj(N("John"))).typ({'refl': True}).realize()   
    ) == 'John sees himself. ',\
    './Examples_from_User_Manual/8-John-sees-himself.dss'


def test_realPro_dep_en_40():
    assert (
root(V("reveal").t('ps'),
     subj(N("psychiatrist"),
          det(D("the"))),
     comp(N("patient"),
          det(D("the"))),
     comp(P("to"),
          mod(Pro("myself").g('f')))).realize()   
    ) == 'The psychiatrist revealed the patient to herself. ',\
    './Examples_from_User_Manual/8-The-psych-rev-patient-to-herself.dss'


def test_realPro_dep_en_41():
    assert (
root(N("egg").a(','),
     det(NO("2").nat(True)),
     mod(A("small")).pos('post')).realize()   
    ) == 'Two eggs, small. ',\
    './Examples_from_User_Manual/9-Two-eggs,-small.dss'


def test_realPro_dep_en_42():
    assert (
root(V("kiss").t('ps'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True}).realize()   
    ) == 'John was kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/aac0i00.dss'


def test_realPro_dep_en_43():
    assert (
root(V("kiss"),
     subj(N("John")),
     comp(N("Mary"))).t('ps').typ({'prog': True, 'int': 'yon'}).realize()   
    ) == 'Was John kissing Mary? ',\
    './Examples_from_User_Manual/Verbs/aac0i0q.dss'


def test_realPro_dep_en_44():
    assert (
root(V("kiss"),
     subj(N("John")),
     comp(N("Mary"))).t('ps').typ({'prog': True, 'neg': True}).realize()   
    ) == 'John was not kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/aac0in0.dss'


def test_realPro_dep_en_45():
    assert (
root(V("kiss"),
     subj(N("John")),
     comp(N("Mary"))).t('ps').typ({'prog': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'Was John not kissing Mary? ',\
    './Examples_from_User_Manual/Verbs/aac0inq.dss'


def test_realPro_dep_en_46():
    assert (
root(V("kiss"),
     comp(N("Mary"))).t('ps').typ({'prog': True}).realize()   
    ) == 'Was kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/aac0m00.dss'


def test_realPro_dep_en_47():
    assert (
root(V("kiss"),
     subj(Pro("I").pe(2)),
     comp(N("Mary"))).t('ps').typ({'prog': True, 'neg': True}).realize()   
    ) == 'You were not kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/aac0mn0-bl-fix.dss'


def test_realPro_dep_en_48():
    assert (
root(V("kiss"),
     subj(Pro("I").pe(2)),
     comp(N("Mary"))).t('ps').typ({'prog': True, 'neg': True}).realize()   
    ) == 'You were not kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/aac0mn0.dss'


def test_realPro_dep_en_49():
    assert (
root(V("kiss"),
     subj(N("John")),
     comp(N("Mary"))).t('ps').typ({'prog': True, 'perf': True}).realize()   
    ) == 'John had been kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/aacpi00.dss'


def test_realPro_dep_en_50():
    assert (
root(V("kiss"),
     subj(N("John")),
     comp(N("Mary"))).t('ps').typ({'prog': True, 'perf': True, 'int': 'yon'}).realize()   
    ) == 'Had John been kissing Mary? ',\
    './Examples_from_User_Manual/Verbs/aacpi0q.dss'


def test_realPro_dep_en_51():
    assert (
root(V("kiss"),
     subj(N("John")),
     comp(N("Mary"))).t('ps').typ({'prog': True, 'perf': True, 'neg': True}).realize()   
    ) == 'John had not been kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/aacpin0.dss'


def test_realPro_dep_en_52():
    assert (
root(V("kiss"),
     subj(N("John")),
     comp(N("Mary"))).t('ps').typ({'prog': True, 'perf': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'Had John not been kissing Mary? ',\
    './Examples_from_User_Manual/Verbs/aacpinq.dss'


def test_realPro_dep_en_53():
    assert (
root(V("kiss"),
     comp(N("Mary"))).t('ps').typ({'prog': True, 'perf': True}).realize()   
    ) == 'Had been kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/aacpm00.dss'


def test_realPro_dep_en_54():
    assert (
root(V("kiss"),
     subj(Pro("I").pe(2)),
     comp(N("Mary"))).t('ps').typ({'prog': True, 'perf': True, 'neg': True}).realize()   
    ) == 'You had not been kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/aacpmn0.dss'


def test_realPro_dep_en_55():
    assert (
root(V("love"),
     subj(N("John")),
     comp(N("Mary"))).t('ps').realize()   
    ) == 'John loved Mary. ',\
    './Examples_from_User_Manual/Verbs/aas0i00.dss'


def test_realPro_dep_en_56():
    assert (
root(V("love"),
     subj(N("John")),
     comp(N("Mary"))).t('ps').typ({'int': 'yon'}).realize()   
    ) == 'Did John love Mary? ',\
    './Examples_from_User_Manual/Verbs/aas0i0q.dss'


def test_realPro_dep_en_57():
    assert (
root(V("love"),
     subj(N("John")),
     comp(N("Mary"))).t('ps').typ({'neg': True}).realize()   
    ) == 'John did not love Mary. ',\
    './Examples_from_User_Manual/Verbs/aas0in0.dss'


def test_realPro_dep_en_58():
    assert (
root(V("love"),
     subj(N("John")),
     comp(N("Mary"))).t('ps').typ({'neg': True, 'int': 'yon'}).realize()   
    ) == 'Did John not love Mary? ',\
    './Examples_from_User_Manual/Verbs/aas0inq.dss'


def test_realPro_dep_en_59():
    assert (
root(V("love"),
     comp(N("Mary"))).t('ps').realize()   
    ) == 'Loved Mary. ',\
    './Examples_from_User_Manual/Verbs/aas0m00.dss'


def test_realPro_dep_en_60():
    assert (
root(V("love"),
     subj(Pro("I").pe(2)),
     comp(N("Mary"))).t('ps').typ({'neg': True}).realize()   
    ) == 'You did not love Mary. ',\
    './Examples_from_User_Manual/Verbs/aas0mn0.dss'


def test_realPro_dep_en_61():
    assert (
root(V("love"),
     subj(N("John")),
     comp(N("Mary"))).t('ps').typ({'perf': True}).realize()   
    ) == 'John had loved Mary. ',\
    './Examples_from_User_Manual/Verbs/aaspi00.dss'


def test_realPro_dep_en_62():
    assert (
root(V("kiss"),
     subj(N("John")),
     comp(N("Mary"))).t('ps').typ({'int': 'yon', 'perf': True}).realize()   
    ) == 'Had John kissed Mary? ',\
    './Examples_from_User_Manual/Verbs/aaspi0q.dss'


def test_realPro_dep_en_63():
    assert (
root(V("kiss"),
     subj(N("John")),
     comp(N("Mary"))).t('ps').typ({'neg': True, 'perf': True}).realize()   
    ) == 'John had not kissed Mary. ',\
    './Examples_from_User_Manual/Verbs/aaspin0.dss'


def test_realPro_dep_en_64():
    assert (
root(V("kiss"),
     subj(N("John")),
     comp(N("Mary"))).t('ps').typ({'perf': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'Had John not kissed Mary? ',\
    './Examples_from_User_Manual/Verbs/aaspinq.dss'


def test_realPro_dep_en_65():
    assert (
root(V("love"),
     comp(N("Mary"))).t('ps').typ({'perf': True}).realize()   
    ) == 'Had loved Mary. ',\
    './Examples_from_User_Manual/Verbs/aaspm00.dss'


def test_realPro_dep_en_66():
    assert (
root(V("kiss"),
     subj(Pro("I").pe(2)),
     comp(N("Mary"))).t('ps').typ({'perf': True, 'neg': True}).realize()   
    ) == 'You had not kissed Mary. ',\
    './Examples_from_User_Manual/Verbs/aaspmn0.dss'


def test_realPro_dep_en_67():
    assert (
root(V("kiss"),
     comp(N("John"))).t('ps').typ({'prog': True, 'pas': True}).realize()   
    ) == 'John was being kissed. ',\
    './Examples_from_User_Manual/Verbs/apc0i00.dss'


def test_realPro_dep_en_68():
    assert (
root(V("kiss"),
     comp(N("John"))).t('ps').typ({'prog': True, 'int': 'yon', 'pas': True}).realize()   
    ) == 'Was John being kissed? ',\
    './Examples_from_User_Manual/Verbs/apc0i0q.dss'


def test_realPro_dep_en_69():
    assert (
root(V("kiss"),
     comp(N("John"))).t('ps').typ({'prog': True, 'neg': True, 'pas': True}).realize()   
    ) == 'John was not being kissed. ',\
    './Examples_from_User_Manual/Verbs/apc0in0.dss'


def test_realPro_dep_en_70():
    assert (
root(V("kiss").t('ps'),
     comp(N("John"))).typ({'prog': True, 'neg': True, 'pas': True, 'int': 'yon'}).realize()   
    ) == 'Was John not being kissed? ',\
    './Examples_from_User_Manual/Verbs/apc0inq.dss'


def test_realPro_dep_en_71():
    assert (
root(V("kiss")).t('ps').typ({'pas': True, 'prog': True}).realize()   
    ) == 'Was being kissed. ',\
    './Examples_from_User_Manual/Verbs/apc0m00.dss'


def test_realPro_dep_en_72():
    assert (
root(V("kiss").t('ps'),
     comp(Pro("I").pe(2))).typ({'prog': True, 'neg': True, 'pas': True}).realize()   
    ) == 'You were not being kissed. ',\
    './Examples_from_User_Manual/Verbs/apc0mn0.dss'


def test_realPro_dep_en_73():
    assert (
root(V("kiss").t('ps'),
     comp(N("John"))).typ({'perf': True, 'prog': True, 'pas': True}).realize()   
    ) == 'John had been being kissed. ',\
    './Examples_from_User_Manual/Verbs/apcpi00.dss'


def test_realPro_dep_en_74():
    assert (
root(V("kiss").t('ps'),
     comp(N("John"))).typ({'perf': True, 'prog': True, 'pas': True, 'int': 'yon'}).realize()   
    ) == 'Had John been being kissed? ',\
    './Examples_from_User_Manual/Verbs/apcpi0q.dss'


def test_realPro_dep_en_75():
    assert (
root(V("kiss").t('ps'),
     comp(N("John"))).typ({'perf': True, 'prog': True, 'neg': True, 'pas': True}).realize()   
    ) == 'John had not been being kissed. ',\
    './Examples_from_User_Manual/Verbs/apcpin0.dss'


def test_realPro_dep_en_76():
    assert (
root(V("kiss").t('ps'),
     comp(N("John"))).typ({'perf': True, 'prog': True, 'neg': True, 'pas': True, 'int': 'yon'}).realize()   
    ) == 'Had John not been being kissed? ',\
    './Examples_from_User_Manual/Verbs/apcpinq.dss'


def test_realPro_dep_en_77():
    assert (
root(V("kiss")).t('ps').typ({'perf': True, 'prog': True, 'pas': True}).realize()   
    ) == 'Had been being kissed. ',\
    './Examples_from_User_Manual/Verbs/apcpm00.dss'


def test_realPro_dep_en_78():
    assert (
root(V("kiss").t('ps'),
     comp(Pro("I").pe(2))).typ({'prog': True, 'perf': True, 'neg': True, 'pas': True}).realize()   
    ) == 'You had not been being kissed. ',\
    './Examples_from_User_Manual/Verbs/apcpmn0.dss'


def test_realPro_dep_en_79():
    assert (
root(V("love").t('ps'),
     comp(N("John"))).typ({'pas': True}).realize()   
    ) == 'John was loved. ',\
    './Examples_from_User_Manual/Verbs/aps0i00.dss'


def test_realPro_dep_en_80():
    assert (
root(V("love").t('ps'),
     comp(N("John"))).typ({'pas': True, 'int': 'yon'}).realize()   
    ) == 'Was John loved? ',\
    './Examples_from_User_Manual/Verbs/aps0i0q.dss'


def test_realPro_dep_en_81():
    assert (
root(V("love").t('ps'),
     comp(N("John"))).typ({'pas': True, 'neg': True}).realize()   
    ) == 'John was not loved. ',\
    './Examples_from_User_Manual/Verbs/aps0in0.dss'


def test_realPro_dep_en_82():
    assert (
root(V("love").t('ps'),
     comp(N("John"))).typ({'pas': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'Was John not loved? ',\
    './Examples_from_User_Manual/Verbs/aps0inq.dss'


def test_realPro_dep_en_83():
    assert (
root(V("love").t('ps')).typ({'pas': True}).realize()   
    ) == 'Was loved. ',\
    './Examples_from_User_Manual/Verbs/aps0m00.dss'


def test_realPro_dep_en_84():
    assert (
root(V("kiss").t('ps'),
     comp(Pro("I").pe(2))).typ({'neg': True, 'pas': True}).realize()   
    ) == 'You were not kissed. ',\
    './Examples_from_User_Manual/Verbs/aps0mn0.dss'


def test_realPro_dep_en_85():
    assert (
root(V("like").t('ps'),
     comp(N("John"))).typ({'perf': True, 'pas': True}).realize()   
    ) == 'John had been liked. ',\
    './Examples_from_User_Manual/Verbs/apspi00.dss'


def test_realPro_dep_en_86():
    assert (
root(V("like").t('ps'),
     comp(N("John"))).typ({'perf': True, 'pas': True, 'int': 'yon'}).realize()   
    ) == 'Had John been liked? ',\
    './Examples_from_User_Manual/Verbs/apspi0q.dss'


def test_realPro_dep_en_87():
    assert (
root(V("kiss").t('ps'),
     comp(N("John"))).typ({'perf': True, 'pas': True, 'neg': True}).realize()   
    ) == 'John had not been kissed. ',\
    './Examples_from_User_Manual/Verbs/apspin0.dss'


def test_realPro_dep_en_88():
    assert (
root(V("love").t('ps'),
     comp(N("John"))).typ({'perf': True, 'pas': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'Had John not been loved? ',\
    './Examples_from_User_Manual/Verbs/apspinq.dss'


def test_realPro_dep_en_89():
    assert (
root(V("like").t('ps')).typ({'perf': True, 'pas': True}).realize()   
    ) == 'Had been liked. ',\
    './Examples_from_User_Manual/Verbs/apspm00.dss'


def test_realPro_dep_en_90():
    assert (
root(V("kiss").t('ps'),
     comp(Pro("I").pe(2))).typ({'perf': True, 'neg': True, 'pas': True}).realize()   
    ) == 'You had not been kissed. ',\
    './Examples_from_User_Manual/Verbs/apspmn0.dss'


def test_realPro_dep_en_91():
    assert (
root(V("kiss").t('f'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True}).realize()   
    ) == 'John will be kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/fac0i00.dss'


def test_realPro_dep_en_92():
    assert (
root(V("kiss").t('f'),
     subj(N("John")),
     comp(N("Mary"))).typ({'int': 'yon', 'prog': True}).realize()   
    ) == 'Will John be kissing Mary? ',\
    './Examples_from_User_Manual/Verbs/fac0i0q.dss'


def test_realPro_dep_en_93():
    assert (
root(V("kiss").t('f'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True, 'neg': True}).realize()   
    ) == 'John will not be kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/fac0in0.dss'


def test_realPro_dep_en_94():
    assert (
root(V("kiss").t('f'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'Will John not be kissing Mary? ',\
    './Examples_from_User_Manual/Verbs/fac0inq.dss'


def test_realPro_dep_en_95():
    assert (
root(V("kiss").t('f'),
     comp(N("Mary"))).typ({'prog': True}).realize()   
    ) == 'Will be kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/fac0m00.dss'


def test_realPro_dep_en_96():
    assert (
root(V("kiss").t('f'),
     subj(Pro("I").pe(2)),
     comp(N("Mary"))).typ({'prog': True, 'neg': True}).realize()   
    ) == 'You will not be kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/fac0mn0.dss'


def test_realPro_dep_en_97():
    assert (
root(V("kiss").t('f'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True, 'perf': True}).realize()   
    ) == 'John will have been kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/facpi00.dss'


def test_realPro_dep_en_98():
    assert (
root(V("kiss").t('f'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True, 'perf': True, 'int': 'yon'}).realize()   
    ) == 'Will John have been kissing Mary? ',\
    './Examples_from_User_Manual/Verbs/facpi0q.dss'


def test_realPro_dep_en_99():
    assert (
root(V("kiss").t('f'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True, 'perf': True, 'neg': True}).realize()   
    ) == 'John will not have been kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/facpin0.dss'


def test_realPro_dep_en_100():
    assert (
root(V("kiss").t('f'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True, 'perf': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'Will John not have been kissing Mary? ',\
    './Examples_from_User_Manual/Verbs/facpinq.dss'


def test_realPro_dep_en_101():
    assert (
root(V("kiss").t('ip'),
     comp(N("Mary"))).typ({'prog': True, 'perf': True}).realize()   
    ) == 'Have been kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/facpm00.dss'


def test_realPro_dep_en_102():
    assert (
root(V("kiss"),
     subj(Pro("I").pe(2)),
     comp(N("Mary"))).typ({'neg': True, 'prog': True, 'perf': True}).realize()   
    ) == 'You have not been kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/facpmn0.dss'


def test_realPro_dep_en_103():
    assert (
root(V("love").t('f'),
     subj(N("John")),
     comp(N("Mary"))).realize()   
    ) == 'John will love Mary. ',\
    './Examples_from_User_Manual/Verbs/fas0i00.dss'


def test_realPro_dep_en_104():
    assert (
root(V("love").t('f'),
     subj(N("John")),
     comp(N("Mary"))).typ({'int': 'yon'}).realize()   
    ) == 'Will John love Mary? ',\
    './Examples_from_User_Manual/Verbs/fas0i0q.dss'


def test_realPro_dep_en_105():
    assert (
root(V("love").t('f'),
     subj(N("John")),
     comp(N("Mary"))).typ({'neg': True}).realize()   
    ) == 'John will not love Mary. ',\
    './Examples_from_User_Manual/Verbs/fas0in0.dss'


def test_realPro_dep_en_106():
    assert (
root(V("love").t('f'),
     subj(N("John")),
     comp(N("Mary"))).typ({'neg': True, 'int': 'yon'}).realize()   
    ) == 'Will John not love Mary? ',\
    './Examples_from_User_Manual/Verbs/fas0inq.dss'


def test_realPro_dep_en_107():
    assert (
root(V("love").t('ip'),
     comp(N("Mary"))).realize()   
    ) == 'Love Mary. ',\
    './Examples_from_User_Manual/Verbs/fas0m00.dss'


def test_realPro_dep_en_108():
    assert (
root(V("kiss"),
     subj(Pro("I").pe(2)),
     comp(N("Mary"))).typ({'neg': True}).realize()   
    ) == 'You do not kiss Mary. ',\
    './Examples_from_User_Manual/Verbs/fas0mn0.dss'


def test_realPro_dep_en_109():
    assert (
root(V("love").t('f'),
     subj(N("John")),
     comp(N("Mary"))).typ({'perf': True}).realize()   
    ) == 'John will have loved Mary. ',\
    './Examples_from_User_Manual/Verbs/faspi00.dss'


def test_realPro_dep_en_110():
    assert (
root(V("love"),
     subj(N("John")),
     comp(N("Mary"))).t('f').typ({'perf': True, 'int': 'yon'}).realize()   
    ) == 'Will John have loved Mary? ',\
    './Examples_from_User_Manual/Verbs/faspi0q.dss'


def test_realPro_dep_en_111():
    assert (
root(V("kiss"),
     subj(N("John")),
     comp(N("Mary"))).t('f').typ({'perf': True, 'neg': True}).realize()   
    ) == 'John will not have kissed Mary. ',\
    './Examples_from_User_Manual/Verbs/faspin0.dss'


def test_realPro_dep_en_112():
    assert (
root(V("kiss"),
     subj(N("John")),
     comp(N("Mary"))).t('f').typ({'perf': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'Will John not have kissed Mary? ',\
    './Examples_from_User_Manual/Verbs/faspinq.dss'


def test_realPro_dep_en_113():
    assert (
root(V("love"),
     comp(N("Mary"))).pe(1).typ({'perf': True}).realize()   
    ) == 'Have loved Mary. ',\
    './Examples_from_User_Manual/Verbs/faspm00.dss'


def test_realPro_dep_en_114():
    assert (
root(V("kiss"),
     subj(Pro("I").pe(2)),
     comp(N("Mary"))).pe(1).typ({'perf': True, 'neg': True}).realize()   
    ) == 'You have not kissed Mary. ',\
    './Examples_from_User_Manual/Verbs/faspmn0.dss'


def test_realPro_dep_en_115():
    assert (
root(V("kiss"),
     comp(N("John"))).t('f').typ({'pas': True, 'prog': True}).realize()   
    ) == 'John will be being kissed. ',\
    './Examples_from_User_Manual/Verbs/fpc0i00.dss'


def test_realPro_dep_en_116():
    assert (
root(V("kiss"),
     comp(N("John"))).t('f').typ({'pas': True, 'prog': True, 'int': 'yon'}).realize()   
    ) == 'Will John be being kissed? ',\
    './Examples_from_User_Manual/Verbs/fpc0i0q.dss'


def test_realPro_dep_en_117():
    assert (
root(V("kiss"),
     comp(N("John"))).t('f').typ({'pas': True, 'prog': True, 'neg': True}).realize()   
    ) == 'John will not be being kissed. ',\
    './Examples_from_User_Manual/Verbs/fpc0in0.dss'


def test_realPro_dep_en_118():
    assert (
root(V("kiss"),
     comp(N("John"))).t('f').typ({'pas': True, 'prog': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'Will John not be being kissed? ',\
    './Examples_from_User_Manual/Verbs/fpc0inq.dss'


def test_realPro_dep_en_119():
    assert (
root(V("kiss")).t('f').typ({'pas': True, 'prog': True}).realize()   
    ) == 'Will be being kissed. ',\
    './Examples_from_User_Manual/Verbs/fpc0m00.dss'


def test_realPro_dep_en_120():
    assert (
root(V("kiss"),
     comp(N("John"))).t('f').typ({'pas': True, 'perf': True, 'prog': True}).realize()   
    ) == 'John will have been being kissed. ',\
    './Examples_from_User_Manual/Verbs/fpcpi00.dss'


def test_realPro_dep_en_121():
    assert (
root(V("kiss"),
     comp(N("John"))).t('f').typ({'pas': True, 'perf': True, 'prog': True, 'int': 'yon'}).realize()   
    ) == 'Will John have been being kissed? ',\
    './Examples_from_User_Manual/Verbs/fpcpi0q.dss'


def test_realPro_dep_en_122():
    assert (
root(V("kiss"),
     comp(N("John"))).t('f').typ({'pas': True, 'perf': True, 'neg': True, 'prog': True}).realize()   
    ) == 'John will not have been being kissed. ',\
    './Examples_from_User_Manual/Verbs/fpcpin0.dss'


def test_realPro_dep_en_123():
    assert (
root(V("kiss"),
     comp(N("John"))).t('f').typ({'pas': True, 'perf': True, 'prog': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'Will John not have been being kissed? ',\
    './Examples_from_User_Manual/Verbs/fpcpinq.dss'


def test_realPro_dep_en_124():
    assert (
root(V("kiss").t('p').n('p')).typ({'prog': True, 'pas': True, 'perf': True}).realize()   
    ) == 'Have been being kissed. ',\
    './Examples_from_User_Manual/Verbs/fpcpm00.dss'


def test_realPro_dep_en_125():
    assert (
root(V("kiss").t('p'),
     comp(Pro("I").pe(2))).typ({'prog': True, 'pas': True, 'perf': True, 'neg': True}).realize()   
    ) == 'You have not been being kissed. ',\
    './Examples_from_User_Manual/Verbs/fpcpmn0.dss'


def test_realPro_dep_en_126():
    assert (
root(V("love").t('f'),
     comp(N("John"))).typ({'pas': True}).realize()   
    ) == 'John will be loved. ',\
    './Examples_from_User_Manual/Verbs/fps0i00.dss'


def test_realPro_dep_en_127():
    assert (
root(V("love"),
     comp(N("John"))).t('f').typ({'pas': True, 'int': 'yon'}).realize()   
    ) == 'Will John be loved? ',\
    './Examples_from_User_Manual/Verbs/fps0i0q.dss'


def test_realPro_dep_en_128():
    assert (
root(V("love"),
     comp(N("John"))).t('f').typ({'pas': True, 'neg': True}).realize()   
    ) == 'John will not be loved. ',\
    './Examples_from_User_Manual/Verbs/fps0in0.dss'


def test_realPro_dep_en_129():
    assert (
root(V("love"),
     comp(N("John"))).t('f').typ({'pas': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'Will John not be loved? ',\
    './Examples_from_User_Manual/Verbs/fps0inq.dss'


def test_realPro_dep_en_130():
    assert (
root(V("love")).t('f').typ({'pas': True}).realize()   
    ) == 'Will be loved. ',\
    './Examples_from_User_Manual/Verbs/fps0m00.dss'


def test_realPro_dep_en_131():
    assert (
root(V("kiss"),
     comp(Pro("I").pe(2))).t('f').typ({'pas': True, 'neg': True}).realize()   
    ) == 'You will not be kissed. ',\
    './Examples_from_User_Manual/Verbs/fps0mn0.dss'


def test_realPro_dep_en_132():
    assert (
root(V("like"),
     comp(N("John"))).t('f').typ({'pas': True, 'perf': True}).realize()   
    ) == 'John will have been liked. ',\
    './Examples_from_User_Manual/Verbs/fpspi00.dss'


def test_realPro_dep_en_133():
    assert (
root(V("like"),
     comp(N("John"))).t('f').typ({'pas': True, 'perf': True, 'int': 'yon'}).realize()   
    ) == 'Will John have been liked? ',\
    './Examples_from_User_Manual/Verbs/fpspi0q.dss'


def test_realPro_dep_en_134():
    assert (
root(V("like"),
     comp(N("John"))).t('f').typ({'pas': True, 'perf': True, 'neg': True}).realize()   
    ) == 'John will not have been liked. ',\
    './Examples_from_User_Manual/Verbs/fpspin0.dss'


def test_realPro_dep_en_135():
    assert (
root(V("kiss").t('f'),
     comp(N("John"))).typ({'pas': True, 'perf': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'Will John not have been kissed? ',\
    './Examples_from_User_Manual/Verbs/fpspinq.dss'


def test_realPro_dep_en_136():
    assert (
root(V("like")).t('ip').typ({'pas': True, 'perf': True}).realize()   
    ) == 'Have been liked. ',\
    './Examples_from_User_Manual/Verbs/fpspm00.dss'


def test_realPro_dep_en_137():
    assert (
root(V("kiss"),
     comp(Pro("I").pe(2))).typ({'pas': True, 'perf': True, 'neg': True}).realize()   
    ) == 'You have not been kissed. ',\
    './Examples_from_User_Manual/Verbs/fpspmn0.dss'


def test_realPro_dep_en_138():
    assert (
root(V("kiss").t('pp'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True}).realize()   
    ) == 'John been kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/pac0a00.dss'


def test_realPro_dep_en_139():
    assert (
root(V("kiss").t('pp'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True, 'int': 'yon'}).realize()   
    ) == 'John been kissing Mary? ',\
    './Examples_from_User_Manual/Verbs/pac0a0q.dss'


def test_realPro_dep_en_140():
    assert (
root(V("kiss").t('pp'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True, 'neg': True}).realize()   
    ) == 'John not been kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/pac0an0.dss'


def test_realPro_dep_en_141():
    assert (
root(V("kiss").t('pp'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'John not been kissing Mary? ',\
    './Examples_from_User_Manual/Verbs/pac0anq.dss'


def test_realPro_dep_en_142():
    assert (
root(V("kiss").t('c'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True}).realize()   
    ) == 'John would be kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/pac0c00.dss'


def test_realPro_dep_en_143():
    assert (
root(V("kiss").t('c'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True, 'int': 'yon'}).realize()   
    ) == 'Would John be kissing Mary? ',\
    './Examples_from_User_Manual/Verbs/pac0c0q.dss'


def test_realPro_dep_en_144():
    assert (
root(V("kiss").t('c'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True, 'neg': True}).realize()   
    ) == 'John would not be kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/pac0cn0.dss'


def test_realPro_dep_en_145():
    assert (
root(V("kiss").t('c'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'Would John not be kissing Mary? ',\
    './Examples_from_User_Manual/Verbs/pac0cnq.dss'


def test_realPro_dep_en_146():
    assert (
root(V("kiss").t('p'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True}).realize()   
    ) == 'John is kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/pac0i00.dss'


def test_realPro_dep_en_147():
    assert (
root(V("kiss").t('p'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True, 'int': 'yon'}).realize()   
    ) == 'Is John kissing Mary? ',\
    './Examples_from_User_Manual/Verbs/pac0i0q.dss'


def test_realPro_dep_en_148():
    assert (
root(V("kiss").t('p'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True, 'neg': True}).realize()   
    ) == 'John is not kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/pac0in0.dss'


def test_realPro_dep_en_149():
    assert (
root(V("kiss").t('p'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'Is John not kissing Mary? ',\
    './Examples_from_User_Manual/Verbs/pac0inq.dss'


def test_realPro_dep_en_150():
    assert (
root(V("kiss").t('p'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True}).realize()   
    ) == 'John is kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/pac0n00.dss'


def test_realPro_dep_en_151():
    assert (
root(V("kiss").t('p'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True, 'int': 'yon'}).realize()   
    ) == 'Is John kissing Mary? ',\
    './Examples_from_User_Manual/Verbs/pac0n0q.dss'


def test_realPro_dep_en_152():
    assert (
root(V("kiss").t('p'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True, 'neg': True}).realize()   
    ) == 'John is not kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/pac0nn0.dss'


def test_realPro_dep_en_153():
    assert (
root(V("kiss").t('p'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'Is John not kissing Mary? ',\
    './Examples_from_User_Manual/Verbs/pac0nnq.dss'


def test_realPro_dep_en_154():
    assert (
root(V("kiss").t('pr'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True}).realize()   
    ) == 'John being kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/pac0p00.dss'


def test_realPro_dep_en_155():
    assert (
root(V("kiss").t('pr'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True, 'int': 'yon'}).realize()   
    ) == 'John being kissing Mary? ',\
    './Examples_from_User_Manual/Verbs/pac0p0q.dss'


def test_realPro_dep_en_156():
    assert (
root(V("kiss").t('pr'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True, 'neg': True}).realize()   
    ) == 'John not being kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/pac0pn0.dss'


def test_realPro_dep_en_157():
    assert (
root(V("kiss").t('pr'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'John not being kissing Mary? ',\
    './Examples_from_User_Manual/Verbs/pac0pnq.dss'


def test_realPro_dep_en_158():
    assert (
root(N("John"),
     det(P("for")),
     comp(V("kiss").t('b-to'),
          comp(N("Mary"))).typ({'prog': True})).realize()   
    ) == 'For John to be kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/pac0t00.dss'


def test_realPro_dep_en_159():
    assert (
root(N("John"),
     det(P("for")),
     comp(V("kiss").t('b-to'),
          comp(N("Mary"))).typ({'prog': True, 'int': 'yon'})).realize()   
    ) == 'For John to be kissing Mary? ',\
    './Examples_from_User_Manual/Verbs/pac0t0q.dss'


def test_realPro_dep_en_160():
    assert (
root(N("John"),
     det(P("for")),
     comp(V("kiss").t('b-to'),
          comp(N("Mary"))).typ({'prog': True, 'neg': True})).realize()   
    ) == 'For John not to be kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/pac0tn0.dss'


def test_realPro_dep_en_161():
    assert (
root(N("John"),
     det(P("for")),
     comp(V("kiss").t('b-to'),
          comp(N("Mary"))).typ({'prog': True, 'neg': True, 'int': 'yon'})).realize()   
    ) == 'For John not to be kissing Mary? ',\
    './Examples_from_User_Manual/Verbs/pac0tnq.dss'


def test_realPro_dep_en_162():
    assert (
root(V("kiss").t('p'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True, 'perf': True}).realize()   
    ) == 'John has been kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/pacpa00.dss'


def test_realPro_dep_en_163():
    assert (
root(V("kiss").t('p'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True, 'perf': True, 'int': 'yon'}).realize()   
    ) == 'Has John been kissing Mary? ',\
    './Examples_from_User_Manual/Verbs/pacpa0q.dss'


def test_realPro_dep_en_164():
    assert (
root(V("kiss").t('p'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True, 'perf': True, 'neg': True}).realize()   
    ) == 'John has not been kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/pacpan0.dss'


def test_realPro_dep_en_165():
    assert (
root(V("kiss").t('p'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True, 'perf': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'Has John not been kissing Mary? ',\
    './Examples_from_User_Manual/Verbs/pacpanq.dss'


def test_realPro_dep_en_166():
    assert (
root(V("kiss").t('c'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True, 'perf': True}).realize()   
    ) == 'John would have been kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/pacpc00.dss'


def test_realPro_dep_en_167():
    assert (
root(V("kiss").t('c'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True, 'perf': True, 'int': 'yon'}).realize()   
    ) == 'Would John have been kissing Mary? ',\
    './Examples_from_User_Manual/Verbs/pacpc0q.dss'


def test_realPro_dep_en_168():
    assert (
root(V("kiss").t('c'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True, 'perf': True, 'neg': True}).realize()   
    ) == 'John would not have been kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/pacpcn0.dss'


def test_realPro_dep_en_169():
    assert (
root(V("kiss").t('c'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True, 'perf': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'Would John not have been kissing Mary? ',\
    './Examples_from_User_Manual/Verbs/pacpcnq.dss'


def test_realPro_dep_en_170():
    assert (
root(V("kiss").t('p'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True, 'perf': True}).realize()   
    ) == 'John has been kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/pacpi00.dss'


def test_realPro_dep_en_171():
    assert (
root(V("kiss").t('p'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True, 'perf': True, 'int': 'yon'}).realize()   
    ) == 'Has John been kissing Mary? ',\
    './Examples_from_User_Manual/Verbs/pacpi0q.dss'


def test_realPro_dep_en_172():
    assert (
root(V("kiss").t('p'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True, 'perf': True, 'neg': True}).realize()   
    ) == 'John has not been kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/pacpin0.dss'


def test_realPro_dep_en_173():
    assert (
root(V("kiss").t('p'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True, 'perf': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'Has John not been kissing Mary? ',\
    './Examples_from_User_Manual/Verbs/pacpinq.dss'


def test_realPro_dep_en_174():
    assert (
root(V("kiss").t('p').n('p'),
     comp(N("Mary"))).typ({'prog': True, 'perf': True}).realize()   
    ) == 'Have been kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/pacpm00.dss'


def test_realPro_dep_en_175():
    assert (
root(V("kiss").t('p').n('p'),
     subj(Pro("I").pe(2)),
     comp(N("Mary"))).typ({'prog': True, 'perf': True, 'neg': True}).realize()   
    ) == 'You have not been kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/pacpmn0.dss'


def test_realPro_dep_en_176():
    assert (
root(V("kiss").t('p').n('p'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True, 'perf': True}).realize()   
    ) == 'John has been kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/pacpn00.dss'


def test_realPro_dep_en_177():
    assert (
root(V("kiss").t('p').n('p'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True, 'perf': True, 'int': 'yon'}).realize()   
    ) == 'Has John been kissing Mary? ',\
    './Examples_from_User_Manual/Verbs/pacpn0q.dss'


def test_realPro_dep_en_178():
    assert (
root(V("kiss").t('pr'),
     subj(N("John")),
     comp(N("Mary"))).typ({'prog': True, 'perf': True}).realize()   
    ) == 'John having been kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/pacpp00.dss'


def test_realPro_dep_en_179():
    assert (
root(N("John"),
     det(P("for")),
     comp(V("kiss").t('b-to'),
          comp(N("Mary"))).typ({'prog': True, 'perf': True})).realize()   
    ) == 'For John to have been kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/pacpt00.dss'


def test_realPro_dep_en_180():
    assert (
root(N("John"),
     det(P("for")),
     comp(V("kiss").t('b-to'),
          comp(Q("Mary"))).typ({'prog': True, 'perf': True, 'int': 'yon'})).realize()   
    ) == 'For John to have been kissing Mary? ',\
    './Examples_from_User_Manual/Verbs/pacpt0q.dss'


def test_realPro_dep_en_181():
    assert (
root(N("John"),
     det(P("for")),
     comp(V("kiss").t('b-to'),
          comp(N("Mary"))).typ({'prog': True, 'perf': True, 'neg': True})).realize()   
    ) == 'For John not to have been kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/pacptn0.dss'


def test_realPro_dep_en_182():
    assert (
root(N("John"),
     det(P("for")),
     comp(V("kiss").t('b-to'),
          comp(N("Mary"))).typ({'prog': True, 'perf': True, 'neg': True, 'int': 'yon'})).realize()   
    ) == 'For John not to have been kissing Mary? ',\
    './Examples_from_User_Manual/Verbs/pacptnq.dss'


def test_realPro_dep_en_183():
    assert (
root(V("like").t('ps'),
     subj(N("John")),
     comp(N("Mary"))).realize()   
    ) == 'John liked Mary. ',\
    './Examples_from_User_Manual/Verbs/pas0a00.dss'


def test_realPro_dep_en_184():
    assert (
root(V("like").t('pp'),
     subj(N("John")),
     comp(N("Mary"))).typ({'int': 'yon'}).realize()   
    ) == 'John liked Mary? ',\
    './Examples_from_User_Manual/Verbs/pas0a0q.dss'


def test_realPro_dep_en_185():
    assert (
root(V("like").t('pp'),
     subj(N("John")),
     comp(N("Mary"))).typ({'neg': True}).realize()   
    ) == 'John not liked Mary. ',\
    './Examples_from_User_Manual/Verbs/pas0an0.dss'


def test_realPro_dep_en_186():
    assert (
root(V("like").t('pp'),
     subj(N("John")),
     comp(N("Mary"))).typ({'neg': True, 'int': 'yon'}).realize()   
    ) == 'John not liked Mary? ',\
    './Examples_from_User_Manual/Verbs/pas0anq.dss'


def test_realPro_dep_en_187():
    assert (
root(V("like").t('c'),
     subj(N("John")),
     comp(N("Mary"))).realize()   
    ) == 'John would like Mary. ',\
    './Examples_from_User_Manual/Verbs/pas0c00.dss'


def test_realPro_dep_en_188():
    assert (
root(V("like").t('c'),
     subj(N("John")),
     comp(N("Mary"))).typ({'int': 'yon'}).realize()   
    ) == 'Would John like Mary? ',\
    './Examples_from_User_Manual/Verbs/pas0c0q.dss'


def test_realPro_dep_en_189():
    assert (
root(V("love").t('c'),
     subj(N("John")),
     comp(N("Mary"))).typ({'neg': True}).realize()   
    ) == 'John would not love Mary. ',\
    './Examples_from_User_Manual/Verbs/pas0cn0.dss'


def test_realPro_dep_en_190():
    assert (
root(V("love").t('c'),
     subj(N("John")),
     comp(N("Mary"))).typ({'neg': True, 'int': 'yon'}).realize()   
    ) == 'Would John not love Mary? ',\
    './Examples_from_User_Manual/Verbs/pas0cnq.dss'


def test_realPro_dep_en_191():
    assert (
root(V("like").t('p'),
     subj(N("John")),
     comp(N("Mary"))).realize()   
    ) == 'John likes Mary. ',\
    './Examples_from_User_Manual/Verbs/pas0i00.dss'


def test_realPro_dep_en_192():
    assert (
root(V("like").t('p'),
     subj(N("John")),
     comp(N("Mary"))).typ({'int': 'yon'}).realize()   
    ) == 'Does John like Mary? ',\
    './Examples_from_User_Manual/Verbs/pas0i0q.dss'


def test_realPro_dep_en_193():
    assert (
root(V("like").t('p'),
     subj(N("John")),
     comp(N("Mary"))).typ({'neg': True}).realize()   
    ) == 'John does not like Mary. ',\
    './Examples_from_User_Manual/Verbs/pas0in0.dss'


def test_realPro_dep_en_194():
    assert (
root(V("like").t('p'),
     subj(N("John")),
     comp(N("Mary"))).typ({'neg': True, 'int': 'yon'}).realize()   
    ) == 'Does John not like Mary? ',\
    './Examples_from_User_Manual/Verbs/pas0inq.dss'


def test_realPro_dep_en_195():
    assert (
root(V("love").t('ip'),
     comp(N("Mary"))).realize()   
    ) == 'Love Mary. ',\
    './Examples_from_User_Manual/Verbs/pas0m00.dss'


def test_realPro_dep_en_196():
    assert (
root(V("love").t('p'),
     subj(Pro("I").pe(2)),
     comp(N("Mary"))).typ({'neg': True}).realize()   
    ) == 'You do not love Mary. ',\
    './Examples_from_User_Manual/Verbs/pas0mn0.dss'


def test_realPro_dep_en_197():
    assert (
root(V("like").t('p'),
     subj(N("John")),
     comp(N("Mary"))).realize()   
    ) == 'John likes Mary. ',\
    './Examples_from_User_Manual/Verbs/pas0n00.dss'


def test_realPro_dep_en_198():
    assert (
root(V("like").t('p'),
     subj(N("John")),
     comp(N("Mary"))).typ({'int': 'yon'}).realize()   
    ) == 'Does John like Mary? ',\
    './Examples_from_User_Manual/Verbs/pas0n0q.dss'


def test_realPro_dep_en_199():
    assert (
root(V("like").t('p'),
     subj(N("John")),
     comp(N("Mary"))).typ({'neg': True}).realize()   
    ) == 'John does not like Mary. ',\
    './Examples_from_User_Manual/Verbs/pas0nn0.dss'


def test_realPro_dep_en_200():
    assert (
root(V("like").t('p'),
     subj(N("John")),
     comp(N("Mary"))).typ({'neg': True, 'int': 'yon'}).realize()   
    ) == 'Does John not like Mary? ',\
    './Examples_from_User_Manual/Verbs/pas0nnq.dss'


def test_realPro_dep_en_201():
    assert (
root(V("kiss").t('pr'),
     subj(N("John")),
     comp(N("Mary"))).realize()   
    ) == 'John kissing Mary. ',\
    './Examples_from_User_Manual/Verbs/pas0p00.dss'


def test_realPro_dep_en_202():
    assert (
root(V("like").t('pr'),
     subj(N("John")),
     comp(N("Mary"))).typ({'int': 'yon'}).realize()   
    ) == 'John liking Mary? ',\
    './Examples_from_User_Manual/Verbs/pas0p0q.dss'


def test_realPro_dep_en_203():
    assert (
root(V("like").t('pr'),
     subj(N("John")),
     comp(N("Mary"))).typ({'neg': True}).realize()   
    ) == 'John not liking Mary. ',\
    './Examples_from_User_Manual/Verbs/pas0pn0.dss'


def test_realPro_dep_en_204():
    assert (
root(V("like").t('pr'),
     subj(N("John")),
     comp(N("Mary"))).typ({'neg': True, 'int': 'yon'}).realize()   
    ) == 'John not liking Mary? ',\
    './Examples_from_User_Manual/Verbs/pas0pnq.dss'


def test_realPro_dep_en_205():
    assert (
root(V("love").t('b-to'),
     subj(N("John"),
          det(P("for"))),
     comp(N("Mary"))).realize()   
    ) == 'For John to love Mary. ',\
    './Examples_from_User_Manual/Verbs/pas0t00.dss'


def test_realPro_dep_en_206():
    assert (
root(N("John"),
     det(P("for")),
     comp(V("like").t('b-to'),
          comp(Q("Mary"))).typ({'int': 'yon'})).realize()   
    ) == 'For John to like Mary? ',\
    './Examples_from_User_Manual/Verbs/pas0t0q.dss'


def test_realPro_dep_en_207():
    assert (
root(N("John"),
     det(P("for")),
     comp(V("like").t('b-to'),
          comp(N("Mary"))).typ({'neg': True})).realize()   
    ) == 'For John not to like Mary. ',\
    './Examples_from_User_Manual/Verbs/pas0tn0.dss'


def test_realPro_dep_en_208():
    assert (
root(N("John"),
     det(P("for")),
     comp(V("like").t('b-to'),
          comp(N("Mary"))).typ({'neg': True, 'int': 'yon'})).realize()   
    ) == 'For John not to like Mary? ',\
    './Examples_from_User_Manual/Verbs/pas0tnq.dss'


def test_realPro_dep_en_209():
    assert (
root(V("love").t('p'),
     subj(N("John")),
     comp(N("Mary"))).typ({'perf': True}).realize()   
    ) == 'John has loved Mary. ',\
    './Examples_from_User_Manual/Verbs/paspa00.dss'


def test_realPro_dep_en_210():
    assert (
root(V("kiss").t('p'),
     subj(N("John")),
     comp(N("Mary"))).typ({'int': 'yon', 'perf': True}).realize()   
    ) == 'Has John kissed Mary? ',\
    './Examples_from_User_Manual/Verbs/paspa0q.dss'


def test_realPro_dep_en_211():
    assert (
root(V("kiss").t('p'),
     subj(N("John")),
     comp(N("Mary"))).typ({'neg': True, 'perf': True}).realize()   
    ) == 'John has not kissed Mary. ',\
    './Examples_from_User_Manual/Verbs/paspan0.dss'


def test_realPro_dep_en_212():
    assert (
root(V("kiss").t('p'),
     subj(N("John")),
     comp(N("Mary"))).typ({'neg': True, 'perf': True, 'int': 'yon'}).realize()   
    ) == 'Has John not kissed Mary? ',\
    './Examples_from_User_Manual/Verbs/paspanq.dss'


def test_realPro_dep_en_213():
    assert (
root(V("love").t('c'),
     subj(N("John")),
     comp(N("Mary"))).typ({'perf': True}).realize()   
    ) == 'John would have loved Mary. ',\
    './Examples_from_User_Manual/Verbs/paspc00.dss'


def test_realPro_dep_en_214():
    assert (
root(V("kiss").t('c'),
     subj(N("John")),
     comp(N("Mary"))).typ({'perf': True, 'int': 'yon'}).realize()   
    ) == 'Would John have kissed Mary? ',\
    './Examples_from_User_Manual/Verbs/paspc0q.dss'


def test_realPro_dep_en_215():
    assert (
root(V("kiss").t('c'),
     subj(N("John")),
     comp(N("Mary"))).typ({'perf': True, 'neg': True}).realize()   
    ) == 'John would not have kissed Mary. ',\
    './Examples_from_User_Manual/Verbs/paspcn0.dss'


def test_realPro_dep_en_216():
    assert (
root(V("kiss").t('c'),
     subj(N("John")),
     comp(N("Mary"))).typ({'perf': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'Would John not have kissed Mary? ',\
    './Examples_from_User_Manual/Verbs/paspcnq.dss'


def test_realPro_dep_en_217():
    assert (
root(V("love").t('p'),
     subj(N("John")),
     comp(N("Mary"))).typ({'perf': True}).realize()   
    ) == 'John has loved Mary. ',\
    './Examples_from_User_Manual/Verbs/paspi00.dss'


def test_realPro_dep_en_218():
    assert (
root(V("kiss"),
     subj(N("John")),
     comp(N("Mary"))).t('p').typ({'perf': True, 'int': 'yon'}).realize()   
    ) == 'Has John kissed Mary? ',\
    './Examples_from_User_Manual/Verbs/paspi0q.dss'


def test_realPro_dep_en_219():
    assert (
root(V("kiss"),
     subj(N("John")),
     comp(N("Mary"))).t('p').typ({'perf': True, 'neg': True}).realize()   
    ) == 'John has not kissed Mary. ',\
    './Examples_from_User_Manual/Verbs/paspin0.dss'


def test_realPro_dep_en_220():
    assert (
root(V("kiss"),
     subj(N("John")),
     comp(N("Mary"))).t('p').typ({'perf': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'Has John not kissed Mary? ',\
    './Examples_from_User_Manual/Verbs/paspinq.dss'


def test_realPro_dep_en_221():
    assert (
root(V("love"),
     comp(N("Mary"))).t('ip').typ({'perf': True}).realize()   
    ) == 'Have loved Mary. ',\
    './Examples_from_User_Manual/Verbs/paspm00.dss'


def test_realPro_dep_en_222():
    assert (
root(V("kiss"),
     subj(Pro("I").pe(2)),
     comp(N("Mary"))).t('p').typ({'perf': True, 'neg': True}).realize()   
    ) == 'You have not kissed Mary. ',\
    './Examples_from_User_Manual/Verbs/paspmn0.dss'


def test_realPro_dep_en_223():
    assert (
root(V("love"),
     subj(N("John")),
     comp(N("Mary"))).t('p').typ({'perf': True}).realize()   
    ) == 'John has loved Mary. ',\
    './Examples_from_User_Manual/Verbs/paspn00.dss'


def test_realPro_dep_en_224():
    assert (
root(V("kiss"),
     subj(N("John")),
     comp(N("Mary"))).t('p').typ({'perf': True, 'int': 'yon'}).realize()   
    ) == 'Has John kissed Mary? ',\
    './Examples_from_User_Manual/Verbs/paspn0q.dss'


def test_realPro_dep_en_225():
    assert (
root(V("kiss").t('p'),
     subj(N("John")),
     comp(N("Mary"))).typ({'neg': True, 'perf': True}).realize()   
    ) == 'John has not kissed Mary. ',\
    './Examples_from_User_Manual/Verbs/paspnn0.dss'


def test_realPro_dep_en_226():
    assert (
root(V("kiss"),
     subj(N("John")),
     comp(N("Mary"))).t('p').typ({'perf': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'Has John not kissed Mary? ',\
    './Examples_from_User_Manual/Verbs/paspnnq.dss'


def test_realPro_dep_en_227():
    assert (
root(V("love"),
     subj(N("John")),
     comp(N("Mary"))).t('pr').typ({'perf': True}).realize()   
    ) == 'John having loved Mary. ',\
    './Examples_from_User_Manual/Verbs/paspp00.dss'


def test_realPro_dep_en_228():
    assert (
root(V("kiss"),
     subj(N("John")),
     comp(N("Mary"))).t('pr').typ({'perf': True, 'int': 'yon'}).realize()   
    ) == 'John having kissed Mary? ',\
    './Examples_from_User_Manual/Verbs/paspp0q.dss'


def test_realPro_dep_en_229():
    assert (
root(V("kiss"),
     subj(N("John")),
     comp(N("Mary"))).t('pr').typ({'perf': True, 'neg': True}).realize()   
    ) == 'John not having kissed Mary. ',\
    './Examples_from_User_Manual/Verbs/pasppn0.dss'


def test_realPro_dep_en_230():
    assert (
root(V("kiss"),
     subj(N("John")),
     comp(N("Mary"))).t('pr').typ({'perf': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'John not having kissed Mary? ',\
    './Examples_from_User_Manual/Verbs/pasppnq.dss'


def test_realPro_dep_en_231():
    assert (
root(N("John"),
     det(P("for")),
     comp(V("kiss").t('b-to'),
          comp(N("Mary"))).typ({'perf': True})).realize()   
    ) == 'For John to have kissed Mary. ',\
    './Examples_from_User_Manual/Verbs/paspt00.dss'


def test_realPro_dep_en_232():
    assert (
root(N("John"),
     det(P("for")),
     comp(V("kiss").t('b-to'),
          comp(N("Mary"))).typ({'perf': True, 'int': 'yon'})).realize()   
    ) == 'For John to have kissed Mary? ',\
    './Examples_from_User_Manual/Verbs/paspt0q.dss'


def test_realPro_dep_en_233():
    assert (
root(N("John"),
     det(P("for")),
     comp(V("kiss").t('b-to'),
          comp(N("Mary"))).typ({'perf': True, 'neg': True})).realize()   
    ) == 'For John not to have kissed Mary. ',\
    './Examples_from_User_Manual/Verbs/pasptn0.dss'


def test_realPro_dep_en_234():
    assert (
root(N("John"),
     det(P("for")),
     comp(V("kiss").t('b-to'),
          comp(N("Mary"))).typ({'perf': True, 'neg': True, 'int': 'yon'})).realize()   
    ) == 'For John not to have kissed Mary? ',\
    './Examples_from_User_Manual/Verbs/pasptnq.dss'


def test_realPro_dep_en_235():
    assert (
root(V("kiss"),
     comp(N("John"))).t('p').typ({'pas': True, 'prog': True}).realize()   
    ) == 'John is being kissed. ',\
    './Examples_from_User_Manual/Verbs/ppc0a00.dss'


def test_realPro_dep_en_236():
    assert (
root(V("kiss"),
     comp(N("John"))).t('p').typ({'pas': True, 'prog': True, 'int': 'yon'}).realize()   
    ) == 'Is John being kissed? ',\
    './Examples_from_User_Manual/Verbs/ppc0a0q.dss'


def test_realPro_dep_en_237():
    assert (
root(V("kiss"),
     comp(N("John"))).t('p').typ({'pas': True, 'prog': True, 'neg': True}).realize()   
    ) == 'John is not being kissed. ',\
    './Examples_from_User_Manual/Verbs/ppc0an0.dss'


def test_realPro_dep_en_238():
    assert (
root(V("kiss"),
     comp(N("John"))).t('p').typ({'pas': True, 'prog': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'Is John not being kissed? ',\
    './Examples_from_User_Manual/Verbs/ppc0anq.dss'


def test_realPro_dep_en_239():
    assert (
root(V("kiss"),
     comp(N("John"))).t('c').typ({'pas': True, 'prog': True}).realize()   
    ) == 'John would be being kissed. ',\
    './Examples_from_User_Manual/Verbs/ppc0c00.dss'


def test_realPro_dep_en_240():
    assert (
root(V("kiss").t('c'),
     comp(N("John"))).typ({'pas': True, 'prog': True, 'int': 'yon'}).realize()   
    ) == 'Would John be being kissed? ',\
    './Examples_from_User_Manual/Verbs/ppc0c0q.dss'


def test_realPro_dep_en_241():
    assert (
root(V("kiss").t('c'),
     comp(N("John"))).typ({'pas': True, 'prog': True, 'neg': True}).realize()   
    ) == 'John would not be being kissed. ',\
    './Examples_from_User_Manual/Verbs/ppc0cn0.dss'


def test_realPro_dep_en_242():
    assert (
root(V("kiss").t('c'),
     comp(N("John"))).typ({'pas': True, 'prog': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'Would John not be being kissed? ',\
    './Examples_from_User_Manual/Verbs/ppc0cnq.dss'


def test_realPro_dep_en_243():
    assert (
root(V("kiss").t('p'),
     comp(N("John"))).typ({'pas': True, 'prog': True}).realize()   
    ) == 'John is being kissed. ',\
    './Examples_from_User_Manual/Verbs/ppc0i00.dss'


def test_realPro_dep_en_244():
    assert (
root(V("kiss"),
     comp(N("John"))).t('p').typ({'pas': True, 'prog': True, 'int': 'yon'}).realize()   
    ) == 'Is John being kissed? ',\
    './Examples_from_User_Manual/Verbs/ppc0i0q.dss'


def test_realPro_dep_en_245():
    assert (
root(V("kiss"),
     comp(N("John"))).t('p').typ({'pas': True, 'prog': True, 'neg': True}).realize()   
    ) == 'John is not being kissed. ',\
    './Examples_from_User_Manual/Verbs/ppc0in0.dss'


def test_realPro_dep_en_246():
    assert (
root(V("kiss"),
     comp(N("John"))).t('p').typ({'pas': True, 'prog': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'Is John not being kissed? ',\
    './Examples_from_User_Manual/Verbs/ppc0inq.dss'


def test_realPro_dep_en_247():
    assert (
root(V("kiss")).n('p').t('p').typ({'pas': True, 'prog': True}).realize()   
    ) == 'Are being kissed. ',\
    './Examples_from_User_Manual/Verbs/ppc0m00.dss'


def test_realPro_dep_en_248():
    assert (
root(V("kiss"),
     comp(N("John"))).t('ip').typ({'pas': True, 'prog': True}).realize()   
    ) == 'John be being kissed. ',\
    './Examples_from_User_Manual/Verbs/ppc0n00.dss'


def test_realPro_dep_en_249():
    assert (
root(V("kiss"),
     comp(N("John"))).t('p').typ({'pas': True, 'prog': True, 'int': 'yon'}).realize()   
    ) == 'Is John being kissed? ',\
    './Examples_from_User_Manual/Verbs/ppc0n0q.dss'


def test_realPro_dep_en_250():
    assert (
root(V("kiss"),
     comp(N("John"))).t('p').typ({'pas': True, 'prog': True, 'neg': True}).realize()   
    ) == 'John is not being kissed. ',\
    './Examples_from_User_Manual/Verbs/ppc0nn0.dss'


def test_realPro_dep_en_251():
    assert (
root(V("kiss"),
     comp(N("John"))).t('p').typ({'pas': True, 'prog': True, 'int': 'yon', 'neg': True}).realize()   
    ) == 'Is John not being kissed? ',\
    './Examples_from_User_Manual/Verbs/ppc0nnq.dss'


def test_realPro_dep_en_252():
    assert (
root(V("kiss"),
     comp(N("John"))).t('pr').typ({'pas': True, 'prog': True}).realize()   
    ) == 'John being being kissed. ',\
    './Examples_from_User_Manual/Verbs/ppc0p00.dss'


def test_realPro_dep_en_253():
    assert (
root(V("kiss"),
     comp(N("John"))).t('pr').typ({'pas': True, 'prog': True, 'int': 'yon'}).realize()   
    ) == 'John being being kissed? ',\
    './Examples_from_User_Manual/Verbs/ppc0p0q.dss'


def test_realPro_dep_en_254():
    assert (
root(V("kiss"),
     comp(N("John"))).t('pr').typ({'pas': True, 'prog': True, 'neg': True}).realize()   
    ) == 'John not being being kissed. ',\
    './Examples_from_User_Manual/Verbs/ppc0pn0.dss'


def test_realPro_dep_en_255():
    assert (
root(V("kiss"),
     comp(N("John"))).t('pr').typ({'pas': True, 'prog': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'John not being being kissed? ',\
    './Examples_from_User_Manual/Verbs/ppc0pnq.dss'


def test_realPro_dep_en_256():
    assert (
root(N("John"),
     det(P("for")),
     comp(V("kiss").t('b-to')).typ({'pas': True, 'prog': True})).realize()   
    ) == 'For John to be being kissed. ',\
    './Examples_from_User_Manual/Verbs/ppc0t00.dss'


def test_realPro_dep_en_257():
    assert (
root(N("John"),
     det(P("for")),
     comp(V("kiss").t('b-to')).typ({'pas': True, 'prog': True, 'int': 'yon'})).realize()   
    ) == 'For John to be being kissed? ',\
    './Examples_from_User_Manual/Verbs/ppc0t0q.dss'


def test_realPro_dep_en_258():
    assert (
root(N("John"),
     det(P("for")),
     comp(V("kiss").t('b-to')).typ({'neg': True, 'pas': True, 'prog': True})).realize()   
    ) == 'For John not to be being kissed. ',\
    './Examples_from_User_Manual/Verbs/ppc0tn0.dss'


def test_realPro_dep_en_259():
    assert (
root(N("John"),
     det(P("for")),
     comp(V("kiss").t('b-to')).typ({'neg': True, 'pas': True, 'prog': True, 'int': 'yon'})).realize()   
    ) == 'For John not to be being kissed? ',\
    './Examples_from_User_Manual/Verbs/ppc0tnq.dss'


def test_realPro_dep_en_260():
    assert (
root(V("kiss"),
     comp(N("John"))).typ({'pas': True, 'prog': True, 'perf': True}).realize()   
    ) == 'John has been being kissed. ',\
    './Examples_from_User_Manual/Verbs/ppcpa00.dss'


def test_realPro_dep_en_261():
    assert (
root(V("kiss"),
     comp(N("John"))).typ({'pas': True, 'prog': True, 'perf': True, 'int': 'yon'}).realize()   
    ) == 'Has John been being kissed? ',\
    './Examples_from_User_Manual/Verbs/ppcpa0q.dss'


def test_realPro_dep_en_262():
    assert (
root(V("kiss"),
     comp(N("John"))).typ({'pas': True, 'prog': True, 'perf': True, 'neg': True}).realize()   
    ) == 'John has not been being kissed. ',\
    './Examples_from_User_Manual/Verbs/ppcpan0.dss'


def test_realPro_dep_en_263():
    assert (
root(V("kiss"),
     comp(N("John"))).typ({'pas': True, 'prog': True, 'perf': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'Has John not been being kissed? ',\
    './Examples_from_User_Manual/Verbs/ppcpanq.dss'


def test_realPro_dep_en_264():
    assert (
root(V("kiss").t('c'),
     comp(N("John"))).typ({'pas': True, 'prog': True, 'perf': True}).realize()   
    ) == 'John would have been being kissed. ',\
    './Examples_from_User_Manual/Verbs/ppcpc00.dss'


def test_realPro_dep_en_265():
    assert (
root(V("kiss").t('c'),
     comp(N("John"))).typ({'pas': True, 'prog': True, 'perf': True, 'int': 'yon'}).realize()   
    ) == 'Would John have been being kissed? ',\
    './Examples_from_User_Manual/Verbs/ppcpc0q.dss'


def test_realPro_dep_en_266():
    assert (
root(V("kiss").t('c'),
     comp(N("John"))).typ({'pas': True, 'perf': True, 'prog': True, 'neg': True}).realize()   
    ) == 'John would not have been being kissed. ',\
    './Examples_from_User_Manual/Verbs/ppcpcn0.dss'


def test_realPro_dep_en_267():
    assert (
root(V("kiss").t('c'),
     comp(N("John"))).typ({'pas': True, 'int': 'yon', 'neg': True, 'perf': True, 'prog': True}).realize()   
    ) == 'Would John not have been being kissed? ',\
    './Examples_from_User_Manual/Verbs/ppcpcnq.dss'


def test_realPro_dep_en_268():
    assert (
root(V("kiss"),
     comp(N("John"))).t('p').typ({'pas': True, 'perf': True, 'prog': True}).realize()   
    ) == 'John has been being kissed. ',\
    './Examples_from_User_Manual/Verbs/ppcpi00.dss'


def test_realPro_dep_en_269():
    assert (
root(V("kiss"),
     comp(N("John"))).t('p').typ({'pas': True, 'perf': True, 'prog': True, 'int': 'yon'}).realize()   
    ) == 'Has John been being kissed? ',\
    './Examples_from_User_Manual/Verbs/ppcpi0q.dss'


def test_realPro_dep_en_270():
    assert (
root(V("kiss"),
     comp(N("John"))).t('p').typ({'pas': True, 'perf': True, 'prog': True, 'neg': True}).realize()   
    ) == 'John has not been being kissed. ',\
    './Examples_from_User_Manual/Verbs/ppcpin0.dss'


def test_realPro_dep_en_271():
    assert (
root(V("kiss"),
     comp(N("John"))).t('p').typ({'pas': True, 'perf': True, 'prog': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'Has John not been being kissed? ',\
    './Examples_from_User_Manual/Verbs/ppcpinq.dss'


def test_realPro_dep_en_272():
    assert (
root(V("kiss").pe(1)).t('p').typ({'pas': True, 'perf': True, 'prog': True}).realize()   
    ) == 'Have been being kissed. ',\
    './Examples_from_User_Manual/Verbs/ppcpm00.dss'


def test_realPro_dep_en_273():
    assert (
root(V("kiss"),
     comp(Pro("I").pe(2))).t('p').typ({'pas': True, 'perf': True, 'prog': True, 'neg': True}).realize()   
    ) == 'You have not been being kissed. ',\
    './Examples_from_User_Manual/Verbs/ppcpmn0.dss'


def test_realPro_dep_en_274():
    assert (
root(V("kiss"),
     comp(N("John"))).t('p').typ({'pas': True, 'perf': True, 'prog': True}).realize()   
    ) == 'John has been being kissed. ',\
    './Examples_from_User_Manual/Verbs/ppcpn00.dss'


def test_realPro_dep_en_275():
    assert (
root(V("kiss").t('p'),
     comp(N("John"))).typ({'pas': True, 'perf': True, 'prog': True, 'int': 'yon'}).realize()   
    ) == 'Has John been being kissed? ',\
    './Examples_from_User_Manual/Verbs/ppcpn0q.dss'


def test_realPro_dep_en_276():
    assert (
root(V("kiss").t('p'),
     comp(N("John"))).typ({'pas': True, 'perf': True, 'prog': True, 'neg': True}).realize()   
    ) == 'John has not been being kissed. ',\
    './Examples_from_User_Manual/Verbs/ppcpnn0.dss'


def test_realPro_dep_en_277():
    assert (
root(V("kiss").t('p'),
     comp(N("John"))).typ({'pas': True, 'perf': True, 'prog': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'Has John not been being kissed? ',\
    './Examples_from_User_Manual/Verbs/ppcpnnq.dss'


def test_realPro_dep_en_278():
    assert (
root(V("kiss").t('pr'),
     comp(N("John"))).typ({'pas': True, 'perf': True, 'prog': True}).realize()   
    ) == 'John having been being kissed. ',\
    './Examples_from_User_Manual/Verbs/ppcpp00.dss'


def test_realPro_dep_en_279():
    assert (
root(V("kiss").t('pr'),
     comp(N("John"))).typ({'pas': True, 'perf': True, 'prog': True, 'int': 'yon'}).realize()   
    ) == 'John having been being kissed? ',\
    './Examples_from_User_Manual/Verbs/ppcpp0q.dss'


def test_realPro_dep_en_280():
    assert (
root(V("kiss").t('pr'),
     comp(N("John"))).typ({'pas': True, 'neg': True, 'perf': True, 'prog': True}).realize()   
    ) == 'John not having been being kissed. ',\
    './Examples_from_User_Manual/Verbs/ppcppn0.dss'


def test_realPro_dep_en_281():
    assert (
root(V("kiss").t('pr'),
     comp(N("John"))).typ({'pas': True, 'neg': True, 'perf': True, 'prog': True, 'int': 'yon'}).realize()   
    ) == 'John not having been being kissed? ',\
    './Examples_from_User_Manual/Verbs/ppcppnq.dss'


def test_realPro_dep_en_282():
    assert (
root(V("kiss").t('b'),
     comp(N("John"),
          det(P("for"))).a(' to')).typ({'pas': True, 'perf': True, 'prog': True}).realize()   
    ) == 'For John to have been being kissed. ',\
    './Examples_from_User_Manual/Verbs/ppcpt00.dss'


def test_realPro_dep_en_283():
    assert (
root(N("John"),
     det(P("for")),
     comp(V("kiss").t('b-to')).typ({'pas': True, 'perf': True, 'prog': True, 'int': 'yon'})).realize()   
    ) == 'For John to have been being kissed? ',\
    './Examples_from_User_Manual/Verbs/ppcpt0q.dss'


def test_realPro_dep_en_284():
    assert (
root(N("John"),
     det(P("for")),
     comp(V("kiss").t('b-to')).typ({'pas': True, 'perf': True, 'prog': True, 'neg': True})).realize()   
    ) == 'For John not to have been being kissed. ',\
    './Examples_from_User_Manual/Verbs/ppcptn0.dss'


def test_realPro_dep_en_285():
    assert (
root(N("John"),
     det(P("for")),
     comp(V("kiss").t('b-to')).typ({'pas': True, 'perf': True, 'prog': True, 'neg': True, 'int': 'yon'})).realize()   
    ) == 'For John not to have been being kissed? ',\
    './Examples_from_User_Manual/Verbs/ppcptnq.dss'


def test_realPro_dep_en_286():
    assert (
root(V("love"),
     comp(N("John"))).typ({'pas': True}).realize()   
    ) == 'John is loved. ',\
    './Examples_from_User_Manual/Verbs/pps0a00.dss'


def test_realPro_dep_en_287():
    assert (
root(V("love"),
     comp(N("John"))).typ({'pas': True, 'int': 'yon'}).realize()   
    ) == 'Is John loved? ',\
    './Examples_from_User_Manual/Verbs/pps0a0q.dss'


def test_realPro_dep_en_288():
    assert (
root(V("love").t('p'),
     comp(N("John"))).typ({'pas': True, 'neg': True}).realize()   
    ) == 'John is not loved. ',\
    './Examples_from_User_Manual/Verbs/pps0an0.dss'


def test_realPro_dep_en_289():
    assert (
root(V("love").t('p'),
     comp(N("John"))).typ({'pas': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'Is John not loved? ',\
    './Examples_from_User_Manual/Verbs/pps0anq.dss'


def test_realPro_dep_en_290():
    assert (
root(V("love").t('c'),
     comp(N("John"))).typ({'pas': True}).realize()   
    ) == 'John would be loved. ',\
    './Examples_from_User_Manual/Verbs/pps0c00.dss'


def test_realPro_dep_en_291():
    assert (
root(V("love").t('c'),
     comp(N("John"))).typ({'pas': True, 'int': 'yon'}).realize()   
    ) == 'Would John be loved? ',\
    './Examples_from_User_Manual/Verbs/pps0c0q.dss'


def test_realPro_dep_en_292():
    assert (
root(V("love").t('c'),
     comp(N("John"))).typ({'pas': True, 'neg': True}).realize()   
    ) == 'John would not be loved. ',\
    './Examples_from_User_Manual/Verbs/pps0cn0.dss'


def test_realPro_dep_en_293():
    assert (
root(V("love").t('c'),
     comp(N("John"))).typ({'pas': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'Would John not be loved? ',\
    './Examples_from_User_Manual/Verbs/pps0cnq.dss'


def test_realPro_dep_en_294():
    assert (
root(V("love").t('p'),
     comp(N("John"))).typ({'pas': True}).realize()   
    ) == 'John is loved. ',\
    './Examples_from_User_Manual/Verbs/pps0i00.dss'


def test_realPro_dep_en_295():
    assert (
root(V("love").t('p'),
     comp(N("John"))).typ({'pas': True, 'int': 'yon'}).realize()   
    ) == 'Is John loved? ',\
    './Examples_from_User_Manual/Verbs/pps0i0q.dss'


def test_realPro_dep_en_296():
    assert (
root(V("love").t('p'),
     comp(N("John"))).typ({'pas': True, 'neg': True}).realize()   
    ) == 'John is not loved. ',\
    './Examples_from_User_Manual/Verbs/pps0in0.dss'


def test_realPro_dep_en_297():
    assert (
root(V("love").t('p'),
     comp(N("John"))).typ({'pas': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'Is John not loved? ',\
    './Examples_from_User_Manual/Verbs/pps0inq.dss'


def test_realPro_dep_en_298():
    assert (
root(V("love").t('p').n('p')).typ({'pas': True}).realize()   
    ) == 'Are loved. ',\
    './Examples_from_User_Manual/Verbs/pps0m00.dss'


def test_realPro_dep_en_299():
    assert (
root(V("love").t('p'),
     comp(N("John"))).typ({'pas': True}).realize()   
    ) == 'John is loved. ',\
    './Examples_from_User_Manual/Verbs/pps0n00.dss'


def test_realPro_dep_en_300():
    assert (
root(V("love").t('p'),
     comp(N("John"))).typ({'pas': True, 'int': 'yon'}).realize()   
    ) == 'Is John loved? ',\
    './Examples_from_User_Manual/Verbs/pps0n0q.dss'


def test_realPro_dep_en_301():
    assert (
root(V("love").t('p'),
     comp(N("John"))).typ({'pas': True, 'neg': True}).realize()   
    ) == 'John is not loved. ',\
    './Examples_from_User_Manual/Verbs/pps0nn0.dss'


def test_realPro_dep_en_302():
    assert (
root(V("love").t('p'),
     comp(N("John"))).typ({'pas': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'Is John not loved? ',\
    './Examples_from_User_Manual/Verbs/pps0nnq.dss'


def test_realPro_dep_en_303():
    assert (
root(V("love").t('pr'),
     comp(N("John"))).typ({'pas': True}).realize()   
    ) == 'John being loved. ',\
    './Examples_from_User_Manual/Verbs/pps0p00.dss'


def test_realPro_dep_en_304():
    assert (
root(V("love").t('pr'),
     comp(N("John"))).typ({'pas': True, 'int': 'yon'}).realize()   
    ) == 'John being loved? ',\
    './Examples_from_User_Manual/Verbs/pps0p0q.dss'


def test_realPro_dep_en_305():
    assert (
root(V("love").t('pr'),
     comp(N("John"))).typ({'pas': True, 'neg': True}).realize()   
    ) == 'John not being loved. ',\
    './Examples_from_User_Manual/Verbs/pps0pn0.dss'


def test_realPro_dep_en_306():
    assert (
root(V("love").t('pr'),
     comp(N("John")).pos('pre')).typ({'pas': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'John not being loved? ',\
    './Examples_from_User_Manual/Verbs/pps0pnq.dss'


def test_realPro_dep_en_307():
    assert (
root(N("John"),
     det(P("for")),
     comp(V("love").t('b-to')).typ({'pas': True})).realize()   
    ) == 'For John to be loved. ',\
    './Examples_from_User_Manual/Verbs/pps0t00.dss'


def test_realPro_dep_en_308():
    assert (
root(N("John"),
     det(P("for")),
     comp(V("love").t('b-to')).typ({'pas': True, 'int': 'yon'})).realize()   
    ) == 'For John to be loved? ',\
    './Examples_from_User_Manual/Verbs/pps0t0q.dss'


def test_realPro_dep_en_309():
    assert (
root(N("John"),
     det(P("for")),
     comp(V("love").t('b-to')).typ({'pas': True, 'neg': True})).realize()   
    ) == 'For John not to be loved. ',\
    './Examples_from_User_Manual/Verbs/pps0tn0.dss'


def test_realPro_dep_en_310():
    assert (
root(N("John"),
     det(P("for")),
     comp(V("love").t('b-to')).typ({'pas': True, 'neg': True, 'int': 'yon'})).realize()   
    ) == 'For John not to be loved? ',\
    './Examples_from_User_Manual/Verbs/pps0tnq.dss'


def test_realPro_dep_en_311():
    assert (
root(V("like").t('p'),
     comp(N("John")).pos('pre')).typ({'pas': True, 'perf': True}).realize()   
    ) == 'John has been liked. ',\
    './Examples_from_User_Manual/Verbs/ppspa00.dss'


def test_realPro_dep_en_312():
    assert (
root(V("kiss").t('p'),
     comp(N("John"))).typ({'pas': True, 'perf': True, 'int': 'yon'}).realize()   
    ) == 'Has John been kissed? ',\
    './Examples_from_User_Manual/Verbs/ppspa0q.dss'


def test_realPro_dep_en_313():
    assert (
root(V("kiss").t('p'),
     comp(N("John")).pos('pre')).typ({'pas': True, 'perf': True, 'neg': True}).realize()   
    ) == 'John has not been kissed. ',\
    './Examples_from_User_Manual/Verbs/ppspan0.dss'


def test_realPro_dep_en_314():
    assert (
root(V("kiss").t('p'),
     comp(N("John")).pos('pre')).typ({'pas': True, 'perf': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'Has John not been kissed? ',\
    './Examples_from_User_Manual/Verbs/ppspanq.dss'


def test_realPro_dep_en_315():
    assert (
root(V("like").t('c'),
     comp(N("John"))).typ({'perf': True, 'pas': True}).realize()   
    ) == 'John would have been liked. ',\
    './Examples_from_User_Manual/Verbs/ppspc00.dss'


def test_realPro_dep_en_316():
    assert (
root(V("kiss").t('c'),
     comp(N("John"))).typ({'perf': True, 'pas': True, 'int': 'yon'}).realize()   
    ) == 'Would John have been kissed? ',\
    './Examples_from_User_Manual/Verbs/ppspc0q.dss'


def test_realPro_dep_en_317():
    assert (
root(V("kiss").t('c'),
     comp(N("John"))).typ({'perf': True, 'pas': True, 'neg': True}).realize()   
    ) == 'John would not have been kissed. ',\
    './Examples_from_User_Manual/Verbs/ppspcn0.dss'


def test_realPro_dep_en_318():
    assert (
root(V("kiss").t('c'),
     comp(N("John"))).typ({'perf': True, 'pas': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'Would John not have been kissed? ',\
    './Examples_from_User_Manual/Verbs/ppspcnq.dss'


def test_realPro_dep_en_319():
    assert (
root(V("like"),
     comp(N("John"))).t('p').typ({'perf': True, 'pas': True}).realize()   
    ) == 'John has been liked. ',\
    './Examples_from_User_Manual/Verbs/ppspi00.dss'


def test_realPro_dep_en_320():
    assert (
root(V("kiss"),
     comp(N("John"))).t('p').typ({'perf': True, 'pas': True, 'int': 'yon'}).realize()   
    ) == 'Has John been kissed? ',\
    './Examples_from_User_Manual/Verbs/ppspi0q.dss'


def test_realPro_dep_en_321():
    assert (
root(V("kiss"),
     comp(N("John"))).t('p').typ({'perf': True, 'pas': True, 'neg': True}).realize()   
    ) == 'John has not been kissed. ',\
    './Examples_from_User_Manual/Verbs/ppspin0.dss'


def test_realPro_dep_en_322():
    assert (
root(V("kiss"),
     comp(N("John"))).t('p').typ({'perf': True, 'pas': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'Has John not been kissed? ',\
    './Examples_from_User_Manual/Verbs/ppspinq.dss'


def test_realPro_dep_en_323():
    assert (
root(V("like").t('ip')).typ({'pas': True, 'perf': True}).realize()   
    ) == 'Have been liked. ',\
    './Examples_from_User_Manual/Verbs/ppspm00.dss'


def test_realPro_dep_en_324():
    assert (
root(V("kiss").t('p'),
     comp(Pro("I").pe(2))).typ({'pas': True, 'perf': True, 'neg': True}).realize()   
    ) == 'You have not been kissed. ',\
    './Examples_from_User_Manual/Verbs/ppspmn0.dss'


def test_realPro_dep_en_325():
    assert (
root(V("like"),
     comp(N("John"))).t('p').typ({'perf': True, 'pas': True}).realize()   
    ) == 'John has been liked. ',\
    './Examples_from_User_Manual/Verbs/ppspn00.dss'


def test_realPro_dep_en_326():
    assert (
root(V("kiss"),
     comp(N("John"))).t('p').typ({'perf': True, 'pas': True, 'int': 'yon'}).realize()   
    ) == 'Has John been kissed? ',\
    './Examples_from_User_Manual/Verbs/ppspn0q.dss'


def test_realPro_dep_en_327():
    assert (
root(V("kiss"),
     comp(N("John"))).t('p').typ({'perf': True, 'pas': True, 'neg': True}).realize()   
    ) == 'John has not been kissed. ',\
    './Examples_from_User_Manual/Verbs/ppspnn0.dss'


def test_realPro_dep_en_328():
    assert (
root(V("kiss"),
     comp(N("John"))).t('p').typ({'perf': True, 'pas': True, 'neg': True, 'int': 'yon'}).realize()   
    ) == 'Has John not been kissed? ',\
    './Examples_from_User_Manual/Verbs/ppspnnq.dss'


def test_realPro_dep_en_329():
    assert (
root(V("kiss"),
     comp(N("John"))).t('pr').typ({'perf': True, 'pas': True}).realize()   
    ) == 'John having been kissed. ',\
    './Examples_from_User_Manual/Verbs/ppspp00.dss'


def test_realPro_dep_en_330():
    assert (
root(V("kiss"),
     comp(N("John"))).t('pr').typ({'perf': True, 'pas': True, 'int': 'yon'}).realize()   
    ) == 'John having been kissed? ',\
    './Examples_from_User_Manual/Verbs/ppspp0q.dss'


def test_realPro_dep_en_331():
    assert (
root(V("kiss"),
     comp(N("John"))).t('pr').typ({'perf': True, 'neg': True, 'pas': True}).realize()   
    ) == 'John not having been kissed. ',\
    './Examples_from_User_Manual/Verbs/ppsppn0.dss'


def test_realPro_dep_en_332():
    assert (
root(V("kiss"),
     comp(N("John"))).t('pr').typ({'perf': True, 'neg': True, 'pas': True, 'int': 'yon'}).realize()   
    ) == 'John not having been kissed? ',\
    './Examples_from_User_Manual/Verbs/ppsppnq.dss'


def test_realPro_dep_en_333():
    assert (
root(V("kiss"),
     comp(N("John"),
          mod(P("for")).pos('pre')),
     mod(P("to")).pos('pre')).t('b').typ({'perf': True, 'pas': True}).realize()   
    ) == 'For John to have been kissed. ',\
    './Examples_from_User_Manual/Verbs/ppspt00.dss'


def test_realPro_dep_en_334():
    assert (
root(N("John"),
     det(P("for")),
     comp(V("kiss").t('b-to')).typ({'pas': True, 'perf': True, 'int': 'yon'})).realize()   
    ) == 'For John to have been kissed? ',\
    './Examples_from_User_Manual/Verbs/ppspt0q.dss'


def test_realPro_dep_en_335():
    assert (
root(N("John"),
     det(P("for")),
     comp(V("kiss").t('b-to')).typ({'pas': True, 'perf': True, 'neg': True})).realize()   
    ) == 'For John not to have been kissed. ',\
    './Examples_from_User_Manual/Verbs/ppsptn0.dss'


def test_realPro_dep_en_336():
    assert (
root(N("John"),
     det(P("for")),
     comp(V("kiss").t('b-to')).typ({'pas': True, 'neg': True, 'perf': True, 'int': 'yon'})).realize()   
    ) == 'For John not to have been kissed? ',\
    './Examples_from_User_Manual/Verbs/ppsptnq.dss'

