"use strict";
var jsRealBdir='http://rali.iro.umontreal.ca/JSrealB/current/dist/';
var currentLang;

// taken from https://www.sitepoint.com/url-parameters-jquery/
$.urlParam = function(name){
    var results = new RegExp('[?&]' + name + '=([^&#]*)').exec(window.location.href);
    if (results==null){
       return null;
    }
    else{
       return results[1] || 0;
    }
}

// go the corresponding element in the other language
function changeLanguage(){
    // find the index first h2 or h3 element displayed on the page in the current language
    let h2Tops = $(`h2[lang=${currentLang}],h3[lang=${currentLang}]`).map(function(){return this.offsetTop}).get();
    const currTop = window.scrollY;
    const idx=h2Tops.findIndex(v => v>=currTop);
    setLanguage(currentLang=="en"?"fr":"en");
    if (idx>=0){
        // scroll to the corresponding element in the new language
        h2Tops = $(`h2[lang=${currentLang}],h3[lang=${currentLang}]`).map(function(){return this.offsetTop}).get();
        window.scrollTo(0,h2Tops[idx])
    }
}

function setLanguage(lang){
    if (lang=="en"){
        currentLang="en"; $("[lang=en]").show(); $("[lang=fr]").hide();
    } else {
        currentLang="fr"; $("[lang=fr]").show(); $("[lang=en]").hide();        
    }
}

function tag(tagName,body,attrs){
    if(arguments.length==1)return "<"+tagName+"/>";
    return "<"+tagName+(arguments.length>2?" "+attrs:"")+">"+
        body+"</"+tagName+">";
}


function insertQuickLinks(lang){
    var $ql=$("#quicklinks .dropdown-content");
    $("h2[lang="+lang+"]").each(function(){
        var id=$(this).attr("id");
        $ql.append(tag("a",$(this).html(),'href="#'+id+'" '+'lang="'+lang+'"'));
    });
}


//// for the table of pronouns...
var options = {
    pe:[1,2,3],
    g:["m","f"],
    n:["s","p"],
    ow:["s","p"],
    tn:["","refl"],
    c:["nom","acc","dat","refl"]
}


function makeOptions(opts){
    if (opts.length==0)return [""];
    var o1=opts.shift();
    var rest = makeOptions(opts);
    var out=[];
    for (var i = 0; i < options[o1].length; i++) {
        var o=options[o1][i];
        var res = o1=="pe" ? `.pe(${o})` : `.${o1}("${o}")`;
        for (var j = 0; j < rest.length; j++) {
            out.push(res+rest[j]);
        }
    }
    return out;
}

function $makeCell(Const,terminal,options){
    var exp=`${Const}("${terminal}")`+options;
    // console.log(exp);
    return $("<td><span class='realisation'>"+eval(exp)+"</span><br/>\
    <span class='pattern'>"+exp+"</span></td>");
}


function ajouterTitre($t,titres){
    let $tr=$("<tr/>")
    for (var i = 0; i < titres.length; i++) {
        $tr.append("<th>"+titres[i]+"</th>")
    }
    $t.append($tr);    
}

function pronomsPersonnels($t,pro,opts,tnC){
    for (var i = 0; i < opts.length; i++) {
        let $tr=$("<tr/>");
        if (i==opts.length-1)$tr.addClass("last");
        const os=opts[i];
        const exp=`Pro("${pro}")`+os;
        const citation=pro=="on"?"on":eval(exp);
        $tr.append($makeCell("Pro",pro,os))
        for (var j = 1; j < tnC.length; j++) {
            $tr.append($makeCell("Pro",citation,tnC[j]+(i==0 && opts.length>1?".pe(1)":"")));
        }
        $t.append($tr);
    }
}


function flexionsGenreNombre($t,Const,singPlur,gn){
    for (var i = 0; i < singPlur.length; i++) {
        let mot=singPlur[i];
        for (let j=1;j<4;j++){
            let $tr=$("<tr/>");
            if (j==3)$tr.addClass("last")
            const exp=`${Const}("${mot}").pe(${j})`
            const citation=eval(eval(exp))
            $tr.append($makeCell(Const,mot,`.pe(${j})`))
            for (var k = 1; k < gn.length; k++) {
                $tr.append($makeCell(Const,citation,(j==1?".pe(1)":"")+gn[k]))
            }
            $t.append($tr)
        }
    }
}

function tableauFrancais(){
    loadFr();
    let titres=["lemme","tonique","tonique réfléchi",
                  "clitique nominatif","clitique accusatif","clitique datif","clitique réfléchi"];
    const tnC=["",'.tn("")','.tn("refl")','.c("nom")','.c("acc")','.c("dat")','.c("refl")']
    var header="<tr><td><code>jsRealB</code><br/>Réalisation</td></tr>"
    let $pronomTon=$("#pronomsTon");
    let $t=$("<table/>");
    ajouterTitre($t,titres)
    pronomsPersonnels($t,"moi",makeOptions(["g","n","pe"]),tnC)
    pronomsPersonnels($t,"on",[""],tnC);
    $pronomTon.append($t)
    
    let $pronomPoss=$("#pronomsPoss")
    $t=$("<table/>");
    titres=["lemme","masculin singulier","féminin singulier","masculin pluriel","féminin pluriel"];
    const gn=makeOptions(["n","g"]);
    gn.unshift("")
    ajouterTitre($t,titres)
    flexionsGenreNombre($t,"Pro",["mien","nôtre"],gn);
    $pronomPoss.append($t)
    
    let $determinantsPoss=$("#determinantsPoss");
    $t=$("<table/>");
    ajouterTitre($t,titres)
    flexionsGenreNombre($t,"D",["mon","notre"],gn); 
    $determinantsPoss.append($t)
}

function englishPossessiveDeterminers($t){
    const genres=options.g.concat(["n"])
    const ow=["s","p"];
    for (var i = 0; i < ow.length; i++) {
        var o= ow[i];
        for (var pe=1;pe<4;pe++){
            let opts=`.pe(${pe}).ow("${o}")`;
            if (pe==3 && o=="s"){
                for (var k = 0; k < genres.length; k++) {
                    var g=genres[k];
                    opts+=`.g("${g}")`
                    $t.append($("<tr/>").append($makeCell("D","my",opts)))
                }
            } else {
                $t.append($("<tr/>").append($makeCell("D","my",opts)))
            }
        }
    }
    return 
}

function englishTable(){
    loadEn();
    let titres=["lemma","tonic","tonic reflexive",
                "clitic nominative","clitic accusative","clitic dative","clitic genitive"];
    const tnC=["",'.tn("")','.tn("refl")','.c("nom")','.c("acc")','.c("dat")','.c("gen")']
    let $tonicPro=$("#tonicPro");
    let $t=$("<table/>");
    ajouterTitre($t,titres);
    pronomsPersonnels($t,"me",makeOptions(["pe","g","n"]),tnC);
    pronomsPersonnels($t,"it",[""],tnC);
    $tonicPro.append($t);

    let $possDet=$("#possDet")
    $t=$("<table/>");
    const gn=makeOptions(["n","g"]);
    gn.unshift("")
    ajouterTitre($t,["Possessive determiner"]);
    
    englishPossessiveDeterminers($t)
    $possDet.append($t);
}


///


$(document).ready(function() {
    insertQuickLinks("fr");
    insertQuickLinks("en");
    $("#langSelect").css({"cursor":"pointer"})
    $("#langSelect").click(changeLanguage);
    var lang=$.urlParam("lang");
    // console.log("lang="+lang);
    if (lang=="en" || lang=="fr")
        setLanguage(lang);
    else
        setLanguage("fr");
});
