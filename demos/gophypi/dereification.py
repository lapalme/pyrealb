'''
Created on Feb 23, 2021

@author: lapalme
'''

## reification table taken from
##        https://github.com/goodmami/norman/blob/master/maps/reifications-full.tsv
## explained in 
# @inproceedings{Goodman:2019,
#   title     = "{AMR} Normalization for Fairer Evaluation",
#   author    = "Goodman, Michael Wayne",
#   booktitle = "Proceedings of the 33rd Pacific Asia Conference on Language, Information, and Computation",
#   year      = "2019",
#   address   = "Hakodate"
# }


reifications = [
    (':accompanier','accompany-01',':ARG0',':ARG1'),
    (':age','age-01',':ARG1',':ARG2'),
    (':beneficiary','benefit-01',':ARG0',':ARG1'),
    (':beneficiary','receive-01',':ARG2',':ARG0'),
    (':cause','cause-01',':ARG1',':ARG0'),
    (':concession','have-concession-91',':ARG1',':ARG2'),
    (':condition','have-condition-91',':ARG1',':ARG2'),
    # (':cost','cost-01',':ARG1',':ARG2'), ## unprocessed role
    (':degree','have-degree-92',':ARG1',':ARG2'),
    (':destination','be-destined-for-91',':ARG1',':ARG2'),
    (':domain','have-mod-91',':ARG2',':ARG1'),
    (':duration','last-01',':ARG1',':ARG2'),
    # (':employed-by','have-org-role-91',':ARG0',':ARG1'), ## unprocessed role
    (':example','exemplify-01',':ARG0',':ARG1'),
    # (':extent','have-extent-91',':ARG1',':ARG2'),  ## unprocessed role
    (':frequency','have-frequency-91',':ARG1',':ARG2'),
    (':instrument','have-instrument-91',':ARG1',':ARG2'),
    (':li','have-li-91',':ARG1',':ARG2'),
    (':location','be-located-at-91',':ARG1',':ARG2'),
    (':manner','have-manner-91',':ARG1',':ARG2'),
    (':meaning','mean-01',':ARG1',':ARG2'), ## unprocessed role
    (':mod','have-mod-91',':ARG1',':ARG2'),
    (':name','have-name-91',':ARG1',':ARG2'),
    (':ord','have-ord-91',':ARG1',':ARG2'),
    # (':part','have-part-91',':ARG1',':ARG2'), ## unprocessed role but :part-of
    (':polarity','have-polarity-91',':ARG1',':ARG2'),
    (':poss','own-01',':ARG0',':ARG1'),
    (':poss','have-03',':ARG0',':ARG1'),
    (':purpose','have-purpose-91',':ARG1',':ARG2'),
    (':quant','have-quant-91',':ARG1',':ARG2'),
    (':role','have-org-role-91',':ARG0',':ARG2'),
    (':source','be-from-91',':ARG1',':ARG2'),
    (':subevent','have-subevent-91',':ARG1',':ARG2'),
    # (':subset','include-91',':ARG2',':ARG1'), ## unprocessed role
    # (':superset','include-91',':ARG1',':ARG2'), ## unprocessed role
    (':time','be-temporally-at-91',':ARG1',':ARG2'),
    (':topic','concern-02',':ARG0',':ARG1'),
    (':value','have-value-91',':ARG1',':ARG2'), ## unprocessed role    
]

def dereify(semR):
    res=None
    _a=semR.concept # does not change... but kept to match Prolog code
    roles=semR.roles
    for role,concept,source,target in reifications:
        sourceOf=source+"-of"
        targetOf=target+"-of"
        if sourceOf in roles:
            ##  A Role B)    <==> (A :Source-of (c/Concept :Target B)) [regular role]
            semRSourceOf=roles[sourceOf]
            if semRSourceOf.concept==concept and len(semRSourceOf.roles)==1 and target in semRSourceOf.roles:
                b=semRSourceOf.roles[target]
                del roles[sourceOf]
                semR.roles.addRole(role,b)
                res=semR
                res2=dereify(semR)
                return res2 if res2!=None else res
        elif targetOf in roles:
                ## (A Role-of B) <==> (A :Target-of (c/Concept :Source B)) [inverted role]
                semRTargetOf=roles[targetOf]
                if semRTargetOf.concept==concept and len(semRTargetOf.roles)==1 and source in semRTargetOf.roles:
                    b=semRTargetOf.roles[source]
                    del roles[targetOf]
                    semR.roles.addRole(role+"-of",b)
                    res=semR
                    res2=dereify(semR)
                    return res2 if res2!=None else res
    return res          
            
#### original PROLOG code
## reification(Role,Concept,:Source,:Target)
## used in transforming 
##       (A Role B)    <==> (A :Source-of (c/Concept :Target B)) [regular role]
# dereify([A,Var|Roles],[A,Var,[Role,B]|Roles2]):-
#     reification(Role,Concept,Source,Target),invRole(Source,SourceOf),
#     select([SourceOf,[Concept,_,[Target,B]]],Roles,Roles1),
#     dereify(Roles1,Roles2).
# ##       (A Role-of B) <==> (A :Target-of (c/Concept :Source B)) [inverted role]
# dereify([A,Var|Roles],[A,Var,[RoleOf,B]|Roles2]):-
#     reification(Role,Concept,Source,Target),invRole(Target,TargetOf),
#     select([TargetOf,[Concept,_,[Source,B]]],Roles,Roles1), # must not be involved in other roles
#     dereify(Roles1,Roles2),
#     invRole(Role,RoleOf).

if __name__ == '__main__':
    pass