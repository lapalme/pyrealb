<?xml version="1.0"?>

<xsl:transform xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0"
 xmlns:xalan="http://xml.apache.org/xalan" xmlns:xalan2="http://xml.apache.org/xslt"
 exclude-result-prefixes="xalan xalan2">


 <!-- ***** Import Core Dictionary Definitions ***** -->

 <!--<xsl:import href="core-en-dict.xsl"/>-->

 <xsl:output indent="yes" xalan2:indent-amount="2"/>
 <xsl:strip-space elements="*"/>


 <!-- ***** Start Output Here ***** -->
 <xsl:template match="/">
  <dictionary name="crag" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xsi:noNamespaceSchemaLocation="../dict.xsd">

   <!-- Add core entries -->
   <!--<xsl:call-template name="add-entries"/>-->



   <entry stem="and" pos="Conj">
    <member-of family="Conj-Sentential-Binary"/>
   </entry>

   <entry stem=";" pos="Conj">
    <member-of family="Conj-Sentential-Binary"/>
   </entry>

   <entry stem="which" pos="RelPro" macros="@X-thing">
    <member-of family="RelPro"/>

   </entry>



   <entry stem="who" pos="RelPro" macros="@X-person">
    <member-of family="RelPro"/>
    <!--	<member-of family="RelPro-Appos" pred="elab-rel"/>-->
   </entry>

   <entry stem="from" pos="Prep">
    <member-of family="Prep-Nom"/>
   </entry>

   <entry stem="between" pos="Prep">
    <member-of family="Prep-Nom"/>
   </entry>

   <entry stem="to" pos="Prep">
    <member-of family="Prep-Nom"/>
   </entry>

   <entry stem="of" pos="Prep">
    <member-of family="Prep-Filler"/>
    <member-of family="Prep-Nom"/>
    <member-of family="Prep-Poss"/>
   </entry>

   <entry stem="by" pos="Prep">
    <!--	<member-of family="Prep-Nom"/>-->
    <member-of family="Prep-Filler"/>
   </entry>

   <entry stem="during" pos="Prep">
    <!--	<member-of family="Prep-Nom"/>-->
    <member-of family="Prep-Filler"/>
   </entry>

   <entry stem="in" pos="Prep">
    <member-of family="Prep-Nom"/>
    <member-of family="Prep-Filler"/>
   </entry>

   <entry stem="on" pos="Prep">
    <member-of family="Prep-Nom"/>
    <member-of family="Prep-Filler"/>
   </entry>

   <entry stem="using" pos="Prep">
    <!--	<member-of family="Prep-Nom"/>-->
    <member-of family="Prep-Filler"/>
   </entry>

   <entry stem="with" pos="Prep">
    <!--	<member-of family="Prep-Nom"/>-->
    <member-of family="Prep-Filler"/>
   </entry>

   <entry stem="the_opposite_of" pos="Prep">
    <member-of family="Prep-Nom"/>
   </entry>



   <entry stem="currently" pos="Adv">
    <member-of family="forward-adverb2"/>
   </entry>

   <entry stem="now" pos="Adv">
    <member-of family="Adverb-initial"/>
   </entry>

   <entry stem="just" pos="Adv">
    <member-of family="forward-adverb"/>
   </entry>

   <entry stem="recently" pos="Adv">
    <member-of family="forward-adverb"/>
   </entry>

   <entry stem="high" pos="Adv">
    <member-of family="Adverb-final"/>
   </entry>

   <entry stem="today" pos="Adv">
    <member-of family="Adverb-initial"/>
   </entry>


   <entry stem="happily" pos="Adv">
    <member-of family="forward-adverb"/>
   </entry>



   <entry stem="originally" pos="Adv">
    <member-of family="forward-adverb2"/>
   </entry>

   <entry stem="like" pos="Comparator">
    <member-of family="Comparator"/>
   </entry>

   <entry stem="unlike" pos="Comparator">
    <member-of family="Comparator"/>
   </entry>

   <entry stem="previous" pos="Adj">
    <member-of family="Adjective" entry="Predicative"/>
   </entry>

   <entry stem="other" pos="Adj">
    <member-of family="Adjective" entry="Predicative"/>
   </entry>

   <entry stem="last" pos="Adj">
    <member-of family="Adjective" entry="Predicative"/>
   </entry>

   <entry stem="be-aux" pos="Aux">
    <member-of family="PassiveBe"/>
    <word form="be" macros="@base" excluded="Inverted"/>
    <!--	<word form="am" macros="@pres @sg-agr @1st-agr"/>
	    <word form="'m" macros="@pres @sg-agr @1st-agr"/>-->
    <word form="are" macros="@pres @sg-agr @2nd-agr"/>
    <!--	<word form="'re" macros="@pres @sg-agr @2nd-agr"/>-->
    <word form="is" macros="@pres @sg-or-mass-agr @3rd-agr"/>
    <!--	<word form="'s" macros="@pres @sg-or-mass-agr @3rd-agr"/>-->
    <word form="are" macros="@pres @pl-agr"/>
    <!--	<word form="'re" macros="@pres @pl-agr"/>-->
    <word form="was" macros="@past @sg-agr @1st-agr"/>
    <word form="were" macros="@past @sg-agr @2nd-agr"/>
    <word form="was" macros="@past @sg-or-mass-agr @3rd-agr"/>
    <word form="were" macros="@past @pl-agr"/>
   </entry>





   <!--      <entry stem="made" pos="Adj">
	   <member-of family="Made-Adj"/>
	   </entry>-->

   <!--      <entry stem="located" pos="Adj">
	   <member-of family="Located-Adj"/>
	   </entry>-->

   <!--      <entry stem="inscribed" pos="Adj">
	   <member-of family="Inscribed-Adj"/>
	   </entry>-->

   <entry stem="έκθεμα" pos="N" class="exhibit">
    <word form="έκθεμα" macros="@sg"/>
    <word form="έκθεματα" macros="@pl"/>
   </entry>

   <entry class="sem-obj" pos="N" stem="picture-np">
    <word macros="@sg" form="picture"/>
    <word macros="@pl" form="pictures"/>
   </entry>

   <entry class="sem-obj" pos="N" stem="king-np">
    <word macros="@sg" form="king"/>
    <word macros="@pl" form="kings"/>
   </entry>

   <entry class="sem-obj" pos="N" stem="thing-np">
    <word macros="@sg" form="thing"/>
    <word macros="@pl" form="things"/>
   </entry>



   <!-- common nouns automatically extracted from M-PIRO english lexicon -->


   <entry class="amphora-handle" pos="N" stem="amphora-handle-np">
    <word macros="@sg" form="amphora_handle"/>
    <word macros="@pl" form="amphora_handles"/>
   </entry>

   <entry class="amphora" pos="N" stem="amphora-np">
    <word macros="@sg" form="amphora"/>
    <word macros="@pl" form="amphoras"/>
   </entry>

   <entry class="amphora-with-a-neck" pos="N" stem="amphora-with-a-neck-np">
    <word macros="@sg" form="amphora_with_a_neck"/>
    <word macros="@pl" form="amphoras_with_a_neck"/>
   </entry>

   <entry class="archaeological-site" pos="N" stem="archaeological-site-np">
    <word macros="@sg" form="archaeological_site"/>
    <word macros="@pl" form="archaeological_sites"/>
   </entry>

   <entry class="aryballos" pos="N" stem="aryballos-np">
    <word macros="@sg" form="aryballos"/>
    <word macros="@pl" form="aryballoses"/>
   </entry>

   <entry class="black-kantharos" pos="N" stem="black-kantharos-np">
    <word macros="@sg" form="black_kantharos"/>
    <word macros="@pl" form="black_kantharoi"/>
   </entry>

   <entry class="bronze-material" pos="NNP" stem="bronze-material-np">
    <word macros="@sg" form="bronze"/>
    <word macros="@mass" form="bronze"/>
   </entry>

   <entry class="cauldron" pos="N" stem="cauldron-np">
    <word macros="@sg" form="cauldron"/>
    <word macros="@pl" form="cauldrons"/>
   </entry>

   <entry class="city" pos="N" stem="city-np">
    <word macros="@sg" form="city"/>
    <word macros="@pl" form="cities"/>
   </entry>

   <entry class="clay-material" pos="NNP" stem="clay-material-np">
    <word macros="@sg" form="clay"/>
    <word macros="@mass" form="clay"/>
   </entry>

   <entry class="coin" pos="N" stem="coin-np">
    <word macros="@sg" form="coin"/>
    <word macros="@pl" form="coins"/>
   </entry>

   <entry class="complex-statue" pos="N" stem="complex-statue-np">
    <word macros="@sg" form="complex"/>
    <word macros="@pl" form="complexes"/>
   </entry>

   <entry class="continuous-outline-hydria" pos="N" stem="continuous-outline-hydria-np">
    <word macros="@sg" form="continuous_outline_hydria"/>
    <word macros="@pl" form="continuous_outline_hydrias"/>
   </entry>

   <entry class="copy" pos="N" stem="copy-np">
    <word macros="@sg" form="copy"/>
    <word macros="@pl" form="copies"/>
   </entry>

   <entry class="country" pos="N" stem="country-np">
    <word macros="@sg" form="country"/>
    <word macros="@pl" form="countries"/>
   </entry>

   <entry class="decorative-artefact" pos="N" stem="decorative-artefact-np">
    <word macros="@sg" form="decorative_artefact"/>
    <word macros="@pl" form="decorative_artefacts"/>
   </entry>

   <entry class="government-department" pos="N" stem="department-np">
    <word macros="@sg" form="department"/>
    <word macros="@pl" form="departments"/>
   </entry>

   <entry class="donor" pos="N" stem="donor-np">
    <word macros="@sg" form="donor"/>
    <word macros="@pl" form="donors"/>
   </entry>

   <entry class="drachma" pos="N" stem="drachma-np">
    <word macros="@sg" form="drachma"/>
    <word macros="@pl" form="drachmas"/>
   </entry>

   <entry class="earrings" pos="N" stem="earring-np">
    <word macros="@sg" form="earring"/>
    <word macros="@pl" form="earrings"/>
   </entry>

   <entry class="emperor" pos="N" stem="emperor-np">
    <word macros="@sg" form="emperor"/>
    <word macros="@pl" form="emperors"/>
   </entry>

   <entry class="exhibit" pos="N" stem="exhibit-np">
    <word macros="@sg" form="exhibit"/>
    <word macros="@pl" form="exhibits"/>
   </entry>

   <entry class="figurine" pos="N" stem="figurine-np">
    <word macros="@sg" form="figurine"/>
    <word macros="@pl" form="figurines"/>
   </entry>

   <entry class="god" pos="N" stem="god-np">
    <word macros="@sg" form="god"/>
    <word macros="@pl" form="gods"/>
   </entry>

   <entry class="goddess" pos="N" stem="goddess-np">
    <word macros="@sg" form="goddess"/>
    <word macros="@pl" form="goddesses"/>
   </entry>

   <entry class="gold-material" pos="NNP" stem="gold-material-np">
    <word macros="@sg" form="gold"/>
    <word macros="@mass" form="gold"/>
   </entry>

   <entry class="grave" pos="N" stem="grave-np">
    <word macros="@sg" form="relief_tomb_stele"/>
    <word macros="@pl" form="relief_tomb_steles"/>
   </entry>

   <entry class="helmet" pos="N" stem="helmet-np">
    <word macros="@sg" form="helmet"/>
    <word macros="@pl" form="helmets"/>
   </entry>

   <entry class="historical-period" pos="N" stem="historical-period-np">
    <word macros="@sg" form="historical_period"/>
    <word macros="@pl" form="historical_periods"/>
   </entry>

   <entry class="hydria-hadra" pos="N" stem="hydria-hadra-np">
    <word macros="@sg" form="hadra_ware_hydria"/>
    <word macros="@pl" form="hadra_ware_hydrias"/>
   </entry>

   <entry class="hydria" pos="N" stem="hydria-np">
    <word macros="@sg" form="hydria"/>
    <word macros="@pl" form="hydrias"/>
   </entry>

   <entry class="imperial-portrait" pos="N" stem="imperial-portrait-np">
    <word macros="@sg" form="imperial_portrait"/>
    <word macros="@pl" form="imperial_portraits"/>
   </entry>

   <entry class="island" pos="N" stem="island-np">
    <word macros="@sg" form="island"/>
    <word macros="@pl" form="islands"/>
   </entry>

   <entry class="ivory-material" pos="NNP" stem="ivory-material-np">
    <word macros="@sg" form="ivory"/>
    <word macros="@mass" form="ivory"/>
   </entry>

   <entry class="jewel" pos="N" stem="jewel-np">
    <word macros="@sg" form="jewel"/>
    <word macros="@pl" form="jewels"/>
   </entry>

   <entry class="kantharos" pos="N" stem="kantharos-np">
    <word macros="@sg" form="kantharos"/>
    <word macros="@pl" form="kantharoses"/>
   </entry>

   <entry class="king" pos="N" stem="king-np">
    <word macros="@sg" form="king"/>
    <word macros="@pl" form="kings"/>
   </entry>

   <entry class="kouros" pos="N" stem="kouros-np">
    <word macros="@sg" form="kouros"/>
    <word macros="@pl" form="kouroi"/>
   </entry>

   <entry class="kylix" pos="N" stem="kylix-np">
    <word macros="@sg" form="kylix"/>
    <word macros="@pl" form="kylixes"/>
   </entry>

   <entry class="league" pos="N" stem="league-np">
    <word macros="@sg" form="league"/>
    <word macros="@pl" form="leagues"/>
   </entry>

   <entry class="lekythos" pos="N" stem="lekythos-np">
    <word macros="@sg" form="lekythos"/>
    <word macros="@pl" form="lekythoses"/>
   </entry>

   <entry class="location" pos="N" stem="location-np">
    <word macros="@sg" form="location"/>
    <word macros="@pl" form="locations"/>
   </entry>

   <entry class="marble-material" pos="NNP" stem="marble-material-np">
    <word macros="@sg" form="marble"/>
    <word macros="@mass" form="marble"/>
   </entry>

   <entry class="marriage-cauldron" pos="N" stem="marriage-cauldron-np">
    <word macros="@sg" form="marriage_cauldron"/>
    <word macros="@pl" form="marriage_cauldrons"/>
   </entry>

   <entry class="material" pos="NNP" stem="material-np">
    <word macros="@sg" form="material"/>
    <word macros="@pl" form="materials"/>
   </entry>

   <entry class="military" pos="N" stem="military-artefact-np">
    <word macros="@sg" form="military_artefact"/>
    <word macros="@pl" form="military_artefacts"/>
   </entry>

   <entry class="museum" pos="N" stem="museum-np">
    <word macros="@sg" form="museum"/>
    <word macros="@pl" form="museums"/>
   </entry>

   <entry class="painter" pos="N" stem="painter-np">
    <word macros="@sg" form="painter"/>
    <word macros="@pl" form="painters"/>
   </entry>

   <entry class="painting" pos="N" stem="painting-np">
    <word macros="@sg" form="painting"/>
    <word macros="@pl" form="paintings"/>
   </entry>

   <entry class="painting-technique" pos="N" stem="painting-technique-np">
    <word macros="@sg" form="painting_technique"/>
    <word macros="@pl" form="painting_techniques"/>
   </entry>

   <entry class="panathenaic-amphora" pos="N" stem="panathenaic-amphora-np">
    <word macros="@sg" form="panathenaic_amphora"/>
    <word macros="@pl" form="panathenaic_amphoras"/>
   </entry>

   <entry class="portrait" pos="N" stem="portrait-np">
    <word macros="@sg" form="portrait"/>
    <word macros="@pl" form="portraits"/>
   </entry>

   <entry class="potsherd" pos="N" stem="potsherd-np">
    <word macros="@sg" form="potsherd"/>
    <word macros="@pl" form="potsherds"/>
   </entry>

   <entry class="potter" pos="N" stem="potter-np">
    <word macros="@sg" form="potter"/>
    <word macros="@pl" form="potters"/>
   </entry>

   <entry class="prochous" pos="N" stem="prochous-np">
    <word macros="@sg" form="prochous"/>
    <word macros="@pl" form="prochouses"/>
   </entry>

   <entry class="quadriga" pos="N" stem="quadriga-np">
    <word macros="@sg" form="quadriga"/>
    <word macros="@mass" form="quadriga"/>
   </entry>

   <entry class="region" pos="N" stem="region-np">
    <word macros="@sg" form="region"/>
    <word macros="@pl" form="regions"/>
   </entry>

   <entry class="relief" pos="N" stem="relief-np">
    <word macros="@sg" form="relief"/>
    <word macros="@pl" form="reliefs"/>
   </entry>

   <entry class="rhyton" pos="N" stem="rhyton-np">
    <word macros="@sg" form="rhyton"/>
    <word macros="@pl" form="rhytons"/>
   </entry>

   <entry class="roman-copy-type" pos="N" stem="roman-copy-type-np">
    <word macros="@sg" form="roman_copy"/>
    <word macros="@pl" form="roman_copies"/>
   </entry>

   <entry class="roman-emperor" pos="N" stem="roman-emperor-np">
    <word macros="@sg" form="roman_emperor"/>
    <word macros="@pl" form="roman_emperors"/>
   </entry>

   <entry class="sculptor" pos="N" stem="sculptor-np">
    <word macros="@sg" form="sculptor"/>
    <word macros="@pl" form="sculptors"/>
   </entry>

   <entry class="silver-material" pos="NNP" stem="silver-material-np">
    <word macros="@sg" form="silver"/>
    <word macros="@mass" form="silver"/>
   </entry>

   <entry class="stamnos" pos="N" stem="stamnos-np">
    <word macros="@sg" form="stamnos"/>
    <word macros="@pl" form="stamnoses"/>
   </entry>

   <entry class="stater" pos="N" stem="stater-np">
    <word macros="@sg" form="stater"/>
    <word macros="@pl" form="staters"/>
   </entry>

   <entry class="statue" pos="N" stem="statue-np">
    <word macros="@sg" form="statue"/>
    <word macros="@pl" form="statues"/>
   </entry>

   <entry class="style" pos="N" stem="style-np">
    <word macros="@sg" form="style"/>
    <word macros="@pl" form="styles"/>
   </entry>

   <entry class="suit-of-armour" pos="N" stem="suit-of-armour-np">
    <word macros="@sg" form="suit_of_armour"/>
    <word macros="@pl" form="suit_of_armours"/>
   </entry>

   <entry class="technique" pos="N" stem="technique-np">
    <word macros="@sg" form="technique"/>
    <word macros="@pl" form="techniques"/>
   </entry>

   <entry class="tetradrachm" pos="N" stem="tetradrachm-np">
    <word macros="@sg" form="tetradrachm"/>
    <word macros="@pl" form="tetradrachms"/>
   </entry>

   <entry class="university" pos="N" stem="university-np">
    <word macros="@sg" form="university"/>
    <word macros="@pl" form="universities"/>
   </entry>

   <entry class="vessel" pos="N" stem="vessel-np">
    <word macros="@sg" form="vessel"/>
    <word macros="@pl" form="vessels"/>
   </entry>

   <entry class="white-lekythos" pos="N" stem="white-lekythos-np">
    <word macros="@sg" form="white_lekythos"/>
    <word macros="@pl" form="white_lekythoi"/>
   </entry>

   <entry class="wood-material" pos="NNP" stem="wood-material-np">
    <word macros="@sg" form="wood"/>
    <word macros="@mass" form="wood"/>
   </entry>


   <!-- end of common nouns -->

   <!-- proper nouns automatically extracted from mpiro instances -->


   <entry class="region" pos="NNP" stem="pennsylvania-np">
    <word macros="@sg" form="Pennsylvania"/>
   </entry>
   <entry class="museum" pos="NNP" stem="archaeological-argos-np">
    <word macros="@sg" form="the_Archaeological_Museum_of_Argos"/>
   </entry>
   <entry class="city" pos="NNP" stem="philadelphia-usa-np">
    <word macros="@sg" form="Philadelphia"/>
   </entry>
   <entry class="donor" pos="NNP" stem="mantiklos-np">
    <word macros="@sg" form="Mantiklos"/>
   </entry>
   <entry class="city" pos="NNP" stem="florina-np">
    <word macros="@sg" form="Florina"/>
   </entry>
   <entry class="museum" pos="NNP" stem="archaeological-florina-np">
    <word macros="@sg" form="the_Archaeological_Museum_of_Florina"/>
   </entry>
   <entry class="museum" pos="NNP" stem="national-copenhagen-np">
    <word macros="@sg"
     form="the_National_Museum,_Copenhagen,_Department_of_Classical_and_Near_Eastern_Antiquities"/>
   </entry>
   <entry class="museum" pos="NNP" stem="national-copenhagen-short-np">
    <word macros="@sg" form="the_National_Museum"/>
   </entry>
   <entry class="city" pos="NNP" stem="amphipolis-np">
    <word macros="@sg" form="Amphipolis"/>
   </entry>
   <entry class="sculptor" pos="NNP" stem="polyklitus-np">
    <word macros="@sg" form="Polykleitos"/>
   </entry>
   <entry class="city" pos="NNP" stem="croton-np">
    <word macros="@sg" form="Croton"/>
   </entry>
   <entry class="country" pos="NNP" stem="italy-np">
    <word macros="@sg" form="Italy"/>
   </entry>
   <entry class="league" pos="NNP" stem="aetolian-league-np">
    <word macros="@sg" form="the_Aetolian_league"/>
   </entry>
   <entry class="government-department" pos="NNP" stem="hellenic-ministry-of-culture-np">
    <word macros="@sg" form="the_Hellenic_Ministry_of_Culture"/>
   </entry>
   <entry class="city" pos="NNP" stem="rome-np">
    <word macros="@sg" form="Rome"/>
   </entry>
   <entry class="museum" pos="NNP" stem="rhodes-archaeological-np">
    <word macros="@sg" form="the_Archaeological_Museum_of_Rhodes"/>
   </entry>
   <entry class="region" pos="NNP" stem="boeotia-np">
    <word macros="@sg" form="Boeotia"/>
   </entry>
   <entry class="museum" pos="NNP" stem="archaeological-olympia-np">
    <word macros="@sg" form="the_Archaeological_Museum_of_Olympia"/>
   </entry>
   <entry class="museum" pos="NNP" stem="archaeological-thessaloniki-np">
    <word macros="@sg" form="the_Archaeological_Museum_of_Thessaloniki"/>
   </entry>
   <entry class="archaeological-site" pos="NNP" stem="temple-sarapis-np">
    <word macros="@sg" form="the_Temple_of_Sarapis"/>
   </entry>
   <entry class="city" pos="NNP" stem="kavala-np">
    <word macros="@sg" form="Kavala"/>
   </entry>
   <entry class="city" pos="NNP" stem="korinth-np">
    <word macros="@sg" form="Corinth"/>
   </entry>
   <entry class="sculptor" pos="NNP" stem="aristocles-np">
    <word macros="@sg" form="Aristocles"/>
   </entry>
   <entry class="archaeological-site" pos="NNP" stem="sanctuary-zeus-olympia-np">
    <word macros="@sg" form="the_Sanctuary_of_Zeus"/>
   </entry>
   <entry class="archaeological-site" pos="NNP" stem="sanctuary-zeus-olympia-short-np">
    <word macros="@sg" form="the_Sanctuary"/>
   </entry>
   <entry class="king" pos="NNP" stem="alexander-the-great-np">
    <word macros="@sg" form="Alexander_the_Great"/>
   </entry>
   <entry class="king" pos="NNP" stem="fake-king-np">
    <word macros="@sg" form="A_Fake_King"/>
   </entry>
   <entry class="king" pos="NNP" stem="other-fake-king-np">
    <word macros="@sg" form="Another_Fake_King"/>
   </entry>
   <entry class="king" pos="NNP" stem="alexander-the-great-short-np">
    <word macros="@sg" form="Alexander"/>
   </entry>
   <entry class="region" pos="NNP" stem="ipeiros-np">
    <word macros="@sg" form="Ipeiros"/>
   </entry>
   <entry class="painter" pos="NNP" stem="painter-of-kleofrades-np">
    <word macros="@sg" form="the_painter_of_Kleofrades"/>
   </entry>
   <entry class="city" pos="NNP" stem="athens-np">
    <word macros="@sg" form="Athens"/>
   </entry>
   <entry class="museum" pos="NNP" stem="museum-fur-kunst-hamb-np">
    <word macros="@sg" form="the_Museum_Fur_Kunst_und_Gewerbe_Hamburg"/>
   </entry>
   <entry class="museum" pos="NNP" stem="national-archaeological-athens-np">
    <word macros="@sg" form="the_National_Archaeological_Museum_of_Athens"/>
   </entry>
   <entry class="city" pos="NNP" stem="patrae-np">
    <word macros="@sg" form="Patras"/>
   </entry>
   <entry class="painting-technique" pos="NNP" stem="red-figure-technique-np">
    <word macros="@sg" form="the_red_figure_technique"/>
   </entry>
   <entry class="city" pos="NNP" stem="newyork-np">
    <word macros="@sg" form="New_York"/>
   </entry>
   <entry class="painting-technique" pos="NNP" stem="black-figure-technique-np">
    <word macros="@sg" form="the_black_figure_technique"/>
   </entry>
   <entry class="museum" pos="NNP" stem="archaeologico-taranto-np">
    <word macros="@sg" form="The_National_Archaeological_Museum_of_Taranto"/>
   </entry>
   <entry class="museum" pos="NNP" stem="archaeological-kavala-np">
    <word macros="@sg" form="the_Archaeological_Museum_of_Kavala"/>
   </entry>
   <entry class="museum" pos="NNP" stem="national-archaeological-florence-np">
    <word macros="@sg" form="the_National_Archaeological_Museum_of_Florence"/>
   </entry>
   <entry class="god" pos="NNP" stem="apollo-np">
    <word macros="@sg" form="Apollo"/>
   </entry>
   <entry class="city" pos="NNP" stem="taranto-np">
    <word macros="@sg" form="Taranto"/>
   </entry>
   <entry class="museum" pos="NNP" stem="acropolis-museum-np">
    <word macros="@sg" form="the_Acropolis_Museum"/>
   </entry>
   <entry class="archaeological-site" pos="NNP" stem="agora-athens-np">
    <word macros="@sg" form="the_Ancient_Agora_of_Athens"/>
   </entry>
   <entry class="donor" pos="NNP" stem="attalus-np">
    <word macros="@sg" form="Attalus"/>
   </entry>
   <entry class="archaeological-site" pos="NNP" stem="ismenion-thebes-np">
    <word macros="@sg" form="Ismenion"/>
   </entry>
   <entry class="painting-technique" pos="NNP" stem="west-sl-technique-np">
    <word macros="@sg" form="the_West_slope_technique"/>
   </entry>
   <entry class="city" pos="NNP" stem="thessaloniki-np">
    <word macros="@sg" form="Thessaloniki"/>
   </entry>
   <entry class="government-department" pos="NNP" stem="soprinteendenza-firenze-np">
    <word macros="@sg" form="Soprinteendenza_Archaeologica_per_la_Toscana_Firenze"/>
   </entry>
   <entry class="painter" pos="NNP" stem="painter-of-dinos-np">
    <word macros="@sg" form="the_painter_of_Dinos"/>
   </entry>
   <entry class="city" pos="NNP" stem="wurzburg-np">
    <word macros="@sg" form="Wurzburg"/>
   </entry>
   <entry class="museum" pos="NNP" stem="un-museum-pensylvania-np">
    <word macros="@sg" form="University_Museum_of_Pensylvania"/>
   </entry>
   <entry class="region" pos="NNP" stem="california-np">
    <word macros="@sg" form="California"/>
   </entry>
   <entry class="museum" pos="NNP" stem="getty-california-np">
    <word macros="@sg" form="The_John_Paul_Getty_Museum"/>
   </entry>
   <entry class="museum" pos="NNP" stem="getty-california-short-np">
    <word macros="@sg" form="the_Getty"/>
   </entry>
   <entry class="museum" pos="NNP" stem="arch-museo-napoli-np">
    <word macros="@sg" form="the_Archaeological_Museum_of_Napoli"/>
   </entry>
   <entry class="museum" pos="NNP" stem="athens-agora-museum-np">
    <word macros="@sg" form="the_Agora_Museum"/>
   </entry>
   <entry class="city" pos="NNP" stem="pergamos-np">
    <word macros="@sg" form="Pergamos"/>
   </entry>
   <entry class="city" pos="NNP" stem="florence-np">
    <word macros="@sg" form="Florence"/>
   </entry>
   <entry class="city" pos="NNP" stem="copenhagen-np">
    <word macros="@sg" form="Copenhagen"/>
   </entry>
   <entry class="museum" pos="NNP" stem="archaeological-corinth-np">
    <word macros="@sg" form="the_Archaeological_Museum_of_Corinth"/>
   </entry>
   <entry class="painter" pos="NNP" stem="painter-of-achilles-np">
    <word macros="@sg" form="the_Painter_of_Achilles"/>
   </entry>
   <entry class="archaeological-site" pos="NNP" stem="grave-warrior-np">
    <word macros="@sg" form="the_Grave_of_the_warrior_at_Argos"/>
   </entry>
   <entry class="archaeological-site" pos="NNP" stem="grave-warrior-short-np">
    <word macros="@sg" form="the_grave"/>
   </entry>
   <entry class="museum" pos="NNP" stem="archaeological-aquileia-np">
    <word macros="@sg" form="the_Archaeological_Museum_of_Aquileia"/>
   </entry>
   <entry class="island" pos="NNP" stem="delos-np">
    <word macros="@sg" form="Delos"/>
   </entry>
   <entry class="museum" pos="NNP" stem="new-york-metropolitan-art-np">
    <word macros="@sg" form="the_New_York_Metropolitan_Museum_of_Art"/>
   </entry>
   <entry class="museum" pos="NNP" stem="new-york-metropolitan-art-short-np">
    <word macros="@sg" form="the_Met"/>
   </entry>
   <entry class="university" pos="NNP" stem="uniwurzburg-np">
    <word macros="@sg" form="the_University_of_Wurzburg"/>
   </entry>
   <entry class="city" pos="NNP" stem="napoli-np">
    <word macros="@sg" form="Naples"/>
   </entry>
   <entry class="historical-period" pos="NNP" stem="classical-period-np">
    <word macros="@sg" form="the_classical_period"/>
   </entry>
   <entry class="country" pos="NNP" stem="denmark-np">
    <word macros="@sg" form="Denmark"/>
   </entry>
   <entry class="city" pos="NNP" stem="boston-np">
    <word macros="@sg" form="Boston"/>
   </entry>
   <entry class="museum" pos="NNP" stem="arch-mus-ioannina-np">
    <word macros="@sg" form="the_Archaeological_Museum_of_Ioannina"/>
   </entry>
   <entry class="region" pos="NNP" stem="macedonia-np">
    <word macros="@sg" form="Macedonia"/>
   </entry>
   <entry class="country" pos="NNP" stem="greece-np">
    <word macros="@sg" form="Greece"/>
   </entry>
   <entry class="style" pos="NNP" stem="corinthian-type-np">
    <word macros="@sg" form="the_corinthian_type"/>
   </entry>
   <entry class="city" pos="NNP" stem="paris-np">
    <word macros="@sg" form="Paris"/>
   </entry>
   <entry class="country" pos="NNP" stem="germany-np">
    <word macros="@sg" form="Germany"/>
   </entry>
   <entry class="museum" pos="NNP" stem="athens-numismatic-np">
    <word macros="@sg" form="the_Numismatic_Museum_of_Athens"/>
   </entry>
   <entry class="archaeological-site" pos="NNP" stem="iraion-delos-np">
    <word macros="@sg" form="the_Temple_of_Hera"/>
   </entry>
   <entry class="city" pos="NNP" stem="argos-np">
    <word macros="@sg" form="Argos"/>
   </entry>
   <entry class="style" pos="NNP" stem="rich-style-np">
    <word macros="@sg" form="the_rich_(or_ornate)_style"/>
   </entry>
   <entry class="style" pos="NNP" stem="rich-style-short-np">
    <word macros="@sg" form="the_rich_style"/>
   </entry>
   <entry class="painter" pos="NNP" stem="eucharides-np">
    <word macros="@sg" form="Eucharides"/>
   </entry>
   <entry class="city" pos="NNP" stem="ioannina-np">
    <word macros="@sg" form="Ioannina"/>
   </entry>
   <entry class="archaeological-site" pos="NNP" stem="acropolis-np">
    <word macros="@sg" form="the_Acropolis"/>
   </entry>
   <entry class="museum" pos="NNP" stem="epigraphical-athens-np">
    <word macros="@sg" form="the_Epigraphical_Museum_of_Athens"/>
   </entry>
   <entry class="country" pos="NNP" stem="spain-np">
    <word macros="@sg" form="Spain"/>
   </entry>
   <entry class="goddess" pos="NNP" stem="potnia-np">
    <word macros="@sg" form="Potnia_Theron"/>
   </entry>
   <entry class="archaeological-site" pos="NNP" stem="vergina-np">
    <word macros="@sg" form="Vergina"/>
   </entry>
   <entry class="region" pos="NNP" stem="attica-np">
    <word macros="@sg" form="Attica"/>
   </entry>
   <entry class="painter" pos="NNP" stem="painter-of-sotades-np">
    <word macros="@sg" form="the_painter_of_Sotades"/>
   </entry>
   <entry class="island" pos="NNP" stem="rhodes-np">
    <word macros="@sg" form="Rhodes"/>
   </entry>
   <entry class="roman-emperor" pos="NNP" stem="leucius-caesar-np">
    <word macros="@sg" form="Leucius_Caesar"/>
   </entry>
   <entry class="roman-emperor" pos="NNP" stem="leucius-caesar-short-np">
    <word macros="@sg" form="Leucius"/>
   </entry>
   <entry class="historical-period" pos="NNP" stem="roman-period-np">
    <word macros="@sg" form="the_roman_period"/>
   </entry>
   <entry class="city" pos="NNP" stem="olympia-np">
    <word macros="@sg" form="Olympia"/>
   </entry>
   <entry class="historical-period" pos="NNP" stem="archaic-period-np">
    <word macros="@sg" form="the_archaic_period"/>
   </entry>
   <entry class="museum" pos="NNP" stem="national-archaeological-napoli-np">
    <word macros="@sg" form="the_National_Archaeological_Museum_of_Napoli"/>
   </entry>
   <entry class="city" pos="NNP" stem="hamburg-np">
    <word macros="@sg" form="Hamburg"/>
   </entry>
   <entry class="historical-period" pos="NNP" stem="hellenistic-period-np">
    <word macros="@sg" form="the_hellenistic_period"/>
   </entry>
   <entry class="museum" pos="NNP" stem="archaeological-delos-np">
    <word macros="@sg" form="the_Archaeological_Museum_of_Delos"/>
   </entry>
   <entry class="archaeological-site" pos="NNP" stem="cave-pitsa-np">
    <word macros="@sg" form="the_Cave_of_Pitsa,_near_Sikyon"/>
   </entry>
   <entry class="archaeological-site" pos="NNP" stem="cave-pitsa-short-np">
    <word macros="@sg" form="the_cave_of_Pitsa"/>
   </entry>
   <entry class="city" pos="NNP" stem="thebes-np">
    <word macros="@sg" form="Thebes"/>
   </entry>
   <entry class="style" pos="NNP" stem="meidias-style-np">
    <word macros="@sg" form="the_manner_of_Meidias"/>
   </entry>
   <entry class="painter" pos="NNP" stem="painter-of-meidias-np">
    <word macros="@sg" form="the_painter_of_Meidias"/>
   </entry>
   <entry class="museum" pos="NNP" stem="museum-of-art-toledo-np">
    <word macros="@sg" form="the_Museum_of_Art"/>
   </entry>
   <entry class="museum" pos="NNP" stem="nationale-romano-roma-np">
    <word macros="@sg" form="the_Museum_Nationale_Romano"/>
   </entry>
   <entry class="archaeological-site" pos="NNP" stem="vitsa-np">
    <word macros="@sg" form="Vitsa_Zagoriou"/>
   </entry>
   <entry class="archaeological-site" pos="NNP" stem="vitsa-short-np">
    <word macros="@sg" form="Vitsa"/>
   </entry>
   <entry class="archaeological-site" pos="NNP" stem="anavyssos-np">
    <word macros="@sg" form="Anavyssos"/>
   </entry>
   <entry class="country" pos="NNP" stem="usa-np">
    <word macros="@sg" form="the_USA"/>
   </entry>
   <entry class="country" pos="NNP" stem="france-np">
    <word macros="@sg" form="France"/>
   </entry>
   <entry class="potter" pos="NNP" stem="sotades-np">
    <word macros="@sg" form="Sotades"/>
   </entry>
   <entry class="painter" pos="NNP" stem="amasis-np">
    <word macros="@sg" form="Amasis"/>
   </entry>
   <entry class="city" pos="NNP" stem="toledo-np">
    <word macros="@sg" form="Toledo"/>
   </entry>
   <entry class="museum" pos="NNP" stem="musee-du-petit-palais-np">
    <word macros="@sg" form="the_Musee_du_Petit_Palais"/>
   </entry>
   <entry class="museum" pos="NNP" stem="mfa-np">
    <word macros="@sg" form="the_Museum_of_Fine_Arts"/>
   </entry>
   <entry class="museum" pos="NNP" stem="mfa-short-np">
    <word macros="@sg" form="the_MFA"/>
   </entry>
   <entry class="roman-emperor" pos="NNP" stem="octavian-augustus-np">
    <word macros="@sg" form="Octavian_Augustus"/>
   </entry>
   <entry class="roman-emperor" pos="NNP" stem="octavian-augustus-short-np">
    <word macros="@sg" form="Octavian"/>
   </entry>
   <entry class="museum" pos="NNP" stem="martin-von-wagner-museum-np">
    <word macros="@sg" form="the_Martin_von_Wagner_Museum"/>
   </entry>
   <entry class="museum" pos="NNP" stem="thassos-archaeological-np">
    <word macros="@sg" form="the_Archaeological_Museum_of_Thassos"/>
   </entry>



   <!-- end of proper nouns -->

   <!-- dates automatically extracted from mpiro lexicon -->



   <entry stem="circa_460_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit9-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="circa_the_5th_century_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit8-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="the_1st_century_A.D." class="creation-time" pos="NP">
    <member-of pred="exhibit7-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="between_440_and_420_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit6-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="between_530_and_510_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit5-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="circa_440_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit4-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="the_late_5th_century_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit3-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="circa_530_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit2-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="the_early_5th_century_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit1-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="between_336_and_330_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit49-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="circa_420_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit47-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="the_2nd_century_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit46-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="circa_the_third_quarter_of_the_4th_century_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit45-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="320_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit44-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="between_510_and_500_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit43-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="between_470_and_460_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit42-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="between_475_and_470_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit41-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="between_750_and_700_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit40-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="between_177_A.D._and_192_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit39-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="circa_440_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit37-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="circa_480_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit36-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="circa_the_third_quarter_of_the_2nd_century_A.D." class="creation-time" pos="NP">
    <member-of pred="exhibit35-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="between_circa_398_and_397_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit34-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="between_circa_530_and_520_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit33-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="the_first_quarter_of_the_5th_century_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit32-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="the_5th_century_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit31-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="the_5th_century_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit30-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="the_second_quarter_of_the_3rd_century_A.D." class="creation-time" pos="NP">
    <member-of pred="exhibit29-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="the_second_quarter_of_the_5th_century_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit28-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="the_third_quarter_of_the_7th_century_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit27-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="circa_470_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit26-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="between_313_and_312_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit25-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="the_late_7th_century_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit24-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="circa_700_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit23-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="between_500_and_480_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit22-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="510_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit21-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="the_late_4th_century_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit20-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="between_circa_230_and_220_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit19-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="490_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit18-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="between_17_and_34_A.D." class="creation-time" pos="NP">
    <member-of pred="exhibit17-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="between_100_and_200_A.D." class="creation-time" pos="NP">
    <member-of pred="exhibit16-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="circa_550_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit15-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="the_2nd_century_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit12-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="between_220_and_189_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit11-creation-time" family="Canned-NP"/>
   </entry>
   <entry stem="between_420_and_410_B.C." class="creation-time" pos="NP">
    <member-of pred="exhibit10-creation-time" family="Canned-NP"/>
   </entry>

   <!-- end of dates -->


   <entry pos="V" stem="rule-verb">
    <member-of family="TransitiveVerbs"/>
    <word form="rule" macros="@base"/>
    <word form="rules" macros="@pres @sg-or-mass-agr @3rd-agr"/>
    <word form="rule" macros="@pres @pl-agr @3rd-agr"/>
    <word form="ruled" macros="@past"/>
    <word form="ruled" macros="@ppart"/>
   </entry>


   <!-- verbs automatically extracted from mpiro lexicon -->


   <entry pos="V" stem="attribute-verb">
    <member-of family="TransitiveVerbs"/>
    <word form="attribute" macros="@base"/>
    <word form="attributes" macros="@pres @sg-or-mass-agr @3rd-agr"/>
    <word form="attribute" macros="@pres @pl-agr @3rd-agr"/>
    <word form="attributed" macros="@past"/>
    <word form="attributed" macros="@ppart"/>
   </entry>
   <entry pos="V" stem="belong-verb">
    <member-of family="IVPrepVerbs"/>
    <word form="belong" macros="@base"/>
    <word form="belongs" macros="@pres @sg-or-mass-agr @3rd-agr"/>
    <word form="belong" macros="@pres @pl-agr @3rd-agr"/>
    <word form="belonged" macros="@past"/>
   </entry>

   <entry stem="come-verb" pos="V">
    <member-of family="IVPrepVerbs"/>
    <word form="comes" macros="@pres @sg-agr @3rd-agr"/>
    <word form="come" macros="@pres @pl-agr @3rd-agr"/>
    <word macros="@past" form="came"/>
   </entry>

   <entry pos="V" stem="cover-verb">
    <member-of family="TransitiveVerbs"/>
    <word form="cover" macros="@base"/>
    <word form="covers" macros="@pres @sg-or-mass-agr @3rd-agr"/>
    <word form="cover" macros="@pres @pl-agr @3rd-agr"/>
    <word form="covered" macros="@past"/>
    <word form="covered" macros="@ppart"/>
   </entry>
   <entry pos="V" stem="create-verb">
    <member-of family="TransitiveVerbs"/>
    <word form="create" macros="@base"/>
    <word form="creates" macros="@pres @sg-or-mass-agr @3rd-agr"/>
    <word form="create" macros="@pres @pl-agr @3rd-agr"/>
    <word form="created" macros="@past"/>
    <word form="created" macros="@ppart"/>
   </entry>
   <entry pos="V" stem="date-verb">
    <member-of family="IVPrepVerbs"/>
    <word form="date" macros="@base"/>
    <word form="dates" macros="@pres @sg-or-mass-agr @3rd-agr"/>
    <word form="date" macros="@pres @pl-agr @3rd-agr"/>
    <word form="dated" macros="@past"/>
   </entry>
   <entry pos="V" stem="decorate-verb">
    <member-of family="TransitiveVerbs"/>
    <word form="decorate" macros="@base"/>
    <word form="decorates" macros="@pres @sg-or-mass-agr @3rd-agr"/>
    <word form="decorate" macros="@pres @pl-agr @3rd-agr"/>
    <word form="decorated" macros="@past"/>
    <word form="decorated" macros="@ppart"/>
   </entry>
   <entry pos="V" stem="depict-verb">
    <member-of family="TransitiveVerbs"/>
    <word form="depict" macros="@base"/>
    <word form="depicts" macros="@pres @sg-or-mass-agr @3rd-agr"/>
    <word form="depict" macros="@pres @pl-agr @3rd-agr"/>
    <word form="depicted" macros="@past"/>
    <word form="depicted" macros="@ppart"/>
   </entry>
   <entry pos="V" stem="develop-verb">
    <member-of family="TransitiveVerbs"/>
    <word form="develop" macros="@base"/>
    <word form="develops" macros="@pres @sg-or-mass-agr @3rd-agr"/>
    <word form="develop" macros="@pres @pl-agr @3rd-agr"/>
    <word form="developed" macros="@past"/>
    <word form="developed" macros="@ppart"/>
   </entry>
   <entry pos="V" stem="donate-verb">
    <member-of family="TransitiveVerbs"/>
    <word form="donate" macros="@base"/>
    <word form="donates" macros="@pres @sg-or-mass-agr @3rd-agr"/>
    <word form="donate" macros="@pres @pl-agr @3rd-agr"/>
    <word form="donated" macros="@past"/>
    <word form="donated" macros="@ppart"/>
   </entry>
   <entry pos="V" stem="exhibit-verb">
    <member-of family="TransitiveVerbs"/>
    <word form="exhibit" macros="@base"/>
    <word form="exhibits" macros="@pres @sg-or-mass-agr @3rd-agr"/>
    <word form="exhibit" macros="@pres @pl-agr @3rd-agr"/>
    <word form="exhibited" macros="@past"/>
    <word form="exhibited" macros="@ppart"/>
   </entry>
   <entry pos="V" stem="find-verb">
    <member-of family="TransitiveVerbs"/>
    <word form="find" macros="@base"/>
    <word form="finds" macros="@pres @sg-or-mass-agr @3rd-agr"/>
    <word form="find" macros="@pres @pl-agr @3rd-agr"/>
    <word form="found" macros="@past"/>
    <word form="found" macros="@ppart"/>
   </entry>
   <entry pos="V" stem="follow-verb">
    <member-of family="TransitiveVerbs"/>
    <word form="follow" macros="@base"/>
    <word form="follows" macros="@pres @sg-or-mass-agr @3rd-agr"/>
    <word form="follow" macros="@pres @pl-agr @3rd-agr"/>
    <word form="followed" macros="@past"/>
    <word form="followed" macros="@ppart"/>
   </entry>
   <entry pos="V" stem="inscribe-verb">
    <member-of family="TransitiveVerbs"/>
    <word form="inscribe" macros="@base"/>
    <word form="inscribes" macros="@pres @sg-or-mass-agr @3rd-agr"/>
    <word form="inscribe" macros="@pres @pl-agr @3rd-agr"/>
    <word form="inscribed" macros="@past"/>
    <word form="inscribed" macros="@ppart"/>
   </entry>
   <entry pos="V" stem="last-verb">
    <member-of family="IVPrepVerbs"/>
    <word form="last" macros="@base"/>
    <word form="lasts" macros="@pres @sg-or-mass-agr @3rd-agr"/>
    <word form="last" macros="@pres @pl-agr @3rd-agr"/>
    <word form="lasted" macros="@past"/>
   </entry>
   <entry pos="V" stem="locate-verb">
    <member-of family="TransitiveVerbs"/>
    <word form="locate" macros="@base"/>
    <word form="locates" macros="@pres @sg-or-mass-agr @3rd-agr"/>
    <word form="locate" macros="@pres @pl-agr @3rd-agr"/>
    <word form="located" macros="@past"/>
    <word form="located" macros="@ppart"/>
   </entry>
   <entry pos="V" stem="make-verb">
    <member-of family="TransitiveVerbs"/>
    <word form="make" macros="@base"/>
    <word form="makes" macros="@pres @sg-or-mass-agr @3rd-agr"/>
    <word form="make" macros="@pres @pl-agr @3rd-agr"/>
    <word form="made" macros="@past"/>
    <word form="made" macros="@ppart"/>
   </entry>
   <entry pos="V" stem="originate-verb">
    <member-of family="IVPrepVerbs"/>
    <word form="originate" macros="@base"/>
    <word form="originates" macros="@pres @sg-or-mass-agr @3rd-agr"/>
    <word form="originate" macros="@pres @pl-agr @3rd-agr"/>
    <word form="originated" macros="@past"/>
   </entry>
   <entry pos="V" stem="paint-verb">
    <member-of family="TransitiveVerbs"/>
    <word form="paint" macros="@base"/>
    <word form="paints" macros="@pres @sg-or-mass-agr @3rd-agr"/>
    <word form="paint" macros="@pres @pl-agr @3rd-agr"/>
    <word form="painted" macros="@past"/>
    <word form="painted" macros="@ppart"/>
   </entry>
   <entry pos="V" stem="portray-verb">
    <member-of family="TransitiveVerbs"/>
    <word form="portray" macros="@base"/>
    <word form="portrays" macros="@pres @sg-or-mass-agr @3rd-agr"/>
    <word form="portray" macros="@pres @pl-agr @3rd-agr"/>
    <word form="portrayed" macros="@past"/>
    <word form="portrayed" macros="@ppart"/>
   </entry>
   <entry pos="V" stem="range-verb">
    <member-of family="IVPrepVerbs"/>
    <word form="range" macros="@base"/>
    <word form="ranges" macros="@pres @sg-or-mass-agr @3rd-agr"/>
    <word form="range" macros="@pres @pl-agr @3rd-agr"/>
    <word form="ranged" macros="@past"/>
   </entry>

   <entry stem="read-verb" pos="V">
    <member-of family="TransitiveVerbs"/>
    <word form="reads" macros="@pres @sg-or-mass-agr @3rd-agr"/>
    <word form="reads" macros="@pres @pl-agr @3rd-agr"/>
    <word macros="@past" form="read"/>
    <word form="read" macros="@ppart"/>
   </entry>


   <entry pos="V" stem="sculpt-verb">
    <member-of family="TransitiveVerbs"/>
    <word form="sculpt" macros="@base"/>
    <word form="sculpts" macros="@pres @sg-or-mass-agr @3rd-agr"/>
    <word form="sculpt" macros="@pres @pl-agr @3rd-agr"/>
    <word form="sculpted" macros="@past"/>
    <word form="sculpted" macros="@ppart"/>
   </entry>
   <entry pos="V" stem="see-verb">
    <member-of family="TransitiveVerbs"/>
    <word form="see" macros="@base"/>
    <word form="sees" macros="@pres @sg-or-mass-agr @3rd-agr"/>
    <word form="see" macros="@pres @pl-agr @3rd-agr"/>
    <word form="saw" macros="@past"/>
    <word form="seen" macros="@ppart"/>
   </entry>
   <entry pos="V" stem="show-verb">
    <member-of family="TransitiveVerbs"/>
    <word form="show" macros="@base"/>
    <word form="shows" macros="@pres @sg-or-mass-agr @3rd-agr"/>
    <word form="show" macros="@pres @pl-agr @3rd-agr"/>
    <word form="showed" macros="@past"/>
    <word form="shown" macros="@ppart"/>
   </entry>

   <!-- end of verbs -->

   <!-- canned text automatically extracted from mpiro instances -->

   <entry
    stem="Marriages_in_Ancient_Athens_served_to_establish_the_family_unit,_the_oikos,_which_ensured_civic_rights_in_Athenian_society_and_produced_legitimate_children._The_festivities_lasted_for_three_days._The_various_stages_of_the_wedding_ceremony_are_all_shown_on_Classical_Attic_pots"
    class="exhibit-story" pos="S">
    <member-of pred="generic-marriage-cauldron-exhibit-story" family="Canned-Sentence"/>
   </entry>
   <entry stem="were_a_special_type_of_cauldron_used_only_for_wedding_ceremonies"
    class="exhibit-definition" pos="V">
    <member-of pred="generic-marriage-cauldron-exhibit-definition" family="Canned-VP"/>
   </entry>
   <entry
    stem="Another_very_popular_work_of_Polykleitos,_known_only_through_copies,_was_the_'Diadumenos'"
    class="other-work" pos="S">
    <member-of pred="polyklitus-other-work" family="Canned-Sentence"/>
   </entry>
   <entry
    stem="was_with_Phidias_the_most_important_sculptors_of_their_time._Their_figures_expressed,_through_their_beauty,_the_spirituality_and_the_anthropocentric_attitude_of_the_Classical_world"
    class="person-story" pos="V">
    <member-of pred="polyklitus-person-story" family="Canned-VP"/>
   </entry>
   <entry stem="was_a_Greek_colony_in_Southern_Italy" class="location-information" pos="V">
    <member-of pred="croton-location-information" family="Canned-VP"/>
   </entry>
   <entry stem="was_among_the_leagues_that_played_an_important_political_role_in_ancient_Greece"
    class="location-information" pos="V">
    <member-of pred="aetolian-league-location-information" family="Canned-VP"/>
   </entry>
   <entry
    stem="is_representative_of_Early_Classical_vase_painting,_a_period_when_the_archaic_models_had_not_yet_been_totally_abandoned,_but_some_significant_differences_were_starting_to_appear-_among_these_differences_are_a_substantial_increase_in_the_variety_and_naturalness_of_figure_poses,_and_the_appearance_of_well_studied_and_harmonious_compositions"
    class="exhibit-characteristics" pos="V">
    <member-of pred="exhibit9-exhibit-characteristics" family="Canned-VP"/>
   </entry>
   <entry stem="has_the_form_of_a_crocodile_tearing_apart_an_African" class="exhibit-form" pos="V">
    <member-of pred="exhibit9-exhibit-form" family="Canned-VP"/>
   </entry>
   <entry
    stem="was_enough_for_a_metic_(that_is,_a_foreigner_that_stayed_in_Athens),_to_pay_the_'metic_tax'_each_month"
    class="exhibit-purpose" pos="V">
    <member-of pred="exhibit8-exhibit-purpose" family="Canned-VP"/>
   </entry>
   <entry
    stem="American_School_of_Classical_Studies_at_Athens,_Greek_and_Roman_Coins_in_the_Athenian_Agora,_Princeton,_New_Jersey_1975,_fig._9"
    class="references" pos="S">
    <member-of pred="exhibit8-references" family="Canned-Sentence"/>
   </entry>
   <entry
    stem="has_an_image_of_Athena_crowned_with_a_branch_of_olive,_her_tree,_on_its_obverse._On_the_other_side_there_is_a_picture_of_her_owl"
    class="exhibit-form" pos="V">
    <member-of pred="exhibit8-exhibit-form" family="Canned-VP"/>
   </entry>
   <entry
    stem="is_rendered_with_youthful_features_and_an_athletic_bearing,_similar_to_the_poses_that_the_classic_sculptor_Polykleitos_was_using_in_his_statues"
    class="exhibit-form" pos="V">
    <member-of pred="exhibit7-exhibit-form" family="Canned-VP"/>
   </entry>
   <entry
    stem="Oikonomidis,_M.,_Elliniki_Techni-_Archaia_Nomismata,_Ekdotiki_Athinon_plc,_Athens_1996,_pp.106-107,_ill.79"
    class="references" pos="S">
    <member-of pred="exhibit6-references" family="Canned-Sentence"/>
   </entry>
   <entry
    stem="has_an_image_of_Athena_crowned_with_a_branch_of_olive,_her_tree,_on_its_obverse._On_the_reverse_there_is_a_picture_of_her_owl"
    class="exhibit-form" pos="V">
    <member-of pred="exhibit6-exhibit-form" family="Canned-VP"/>
   </entry>
   <entry
    stem="has_a_picture_of_a_tripod_on_each_side._A_tripod_is_a_vessel_with_three_legs_and_it_was_the_sacred_symbol_of_the_god_Apollo"
    class="exhibit-form" pos="V">
    <member-of pred="exhibit5-exhibit-form" family="Canned-VP"/>
   </entry>
   <entry stem="2.12_metres" class="exhibit-height" pos="NP">
    <member-of pred="exhibit4-exhibit-height" family="Canned-NP"/>
   </entry>
   <entry stem="a_group_of_Nymphs" class="exhibit-depicts" pos="NP">
    <member-of pred="exhibit3-exhibit-depicts" family="Canned-NP"/>
   </entry>
   <entry
    stem="There_were_two_types_of_hydria-_one_with_a_continuous_outline_and_one_where_the_neck_was_separate_from_the_rest_of_the_body._This_one_belongs_to_the_first_type"
    class="exhibit-story" pos="S">
    <member-of pred="exhibit3-exhibit-story" family="Canned-Sentence"/>
   </entry>
   <entry stem="1.94_metres" class="exhibit-height" pos="NP">
    <member-of pred="exhibit2-exhibit-height" family="Canned-NP"/>
   </entry>
   <entry stem="honours_the_memory_of_Kroissos,_a_young_man_who_died_in_battle"
    class="exhibit-purpose" pos="V">
    <member-of pred="exhibit2-exhibit-purpose" family="Canned-VP"/>
   </entry>
   <entry stem="Greek_Sculpture,_the_Archaic_period,_Thames_and_Hudson_1978,_fig_107"
    class="references" pos="S">
    <member-of pred="exhibit2-references" family="Canned-Sentence"/>
   </entry>
   <entry
    stem="`Stand_and_cry_in_front_of_the_grave_of_dead_Kroissos_who_found_death_by_Ares,_as_he_was_fighting_on_the_front`"
    class="inscription-says" pos="NP">
    <member-of pred="exhibit2-inscription-says" family="Canned-NP"/>
   </entry>
   <entry
    stem="was_secretly_cut_in_two_pieces_and_transported_to_Paris_in_1937,_before_it_was_returned_to_Greece"
    class="exhibit-form" pos="V">
    <member-of pred="exhibit2-exhibit-form" family="Canned-VP"/>
   </entry>
   <entry
    stem="Kourosses_evolved_gradually-_as_the_years_went_by,_the_form_of_the_anatomy_and_the_muscles_became_more_realistic_and_a_discreet_smile_(meidiama)_was_added_as_a_stereotypical_feature_of_the_face._This_Kouros_effectively_demonstrates_these_gradual_changes"
    class="exhibit-story" pos="S">
    <member-of pred="exhibit2-exhibit-story" family="Canned-Sentence"/>
   </entry>
   <entry stem="Boardman_J-_Athenian_red_figure_vases,_the_Archaic_period,_Thames_and_Hudson,_1975"
    class="references" pos="S">
    <member-of pred="exhibit1-references" family="Canned-Sentence"/>
   </entry>
   <entry
    stem="a_warrior_performing_splachnoscopy_before_leaving_for_battle._Splachnoscopy_is_the_study_of_animal_entrails,_through_which_people_tried_to_predict_the_future._It_was_one_of_the_most_common_divination_methods_used_in_the_archaic_period"
    class="exhibit-depicts" pos="NP">
    <member-of pred="exhibit1-exhibit-depicts" family="Canned-NP"/>
   </entry>
   <entry
    stem="was_one_of_the_most_important_subjects_of_painting_and_sculpture_during_the_Hellenistic_period._The_evidence_that_we_have_for_what_his_face_looked_like_comes_from_copies_created_after_his_death._These_elements_greatly_influenced_the_depictions_of_the_other_Hellenistic_rulers"
    class="person-story" pos="V">
    <member-of pred="alexander-the-great-person-story" family="Canned-VP"/>
   </entry>
   <entry
    stem="are_pots_which_were_mostly_used_for_storing_and_mixing._They_have_two_small_horizontal_handles_on_the_side_and_a_round_body_with_a_short_neck"
    class="exhibit-definition" pos="V">
    <member-of pred="generic-stamnos-exhibit-definition" family="Canned-VP"/>
   </entry>
   <entry
    stem="Leagues_were_formed_after_the_merging_of_many_cities_into_a_unified_political_association"
    class="location-definition" pos="S">
    <member-of pred="generic-league-location-definition" family="Canned-Sentence"/>
   </entry>
   <entry
    stem="has_a_black-painted_background._The_figures,_which_were_predesigned,_had_the_natural_color_of_the_clay"
    class="technique-description" pos="V">
    <member-of pred="red-figure-technique-technique-description" family="Canned-VP"/>
   </entry>
   <entry stem="were_coins_with_the_value_of_four_drachmas" class="exhibit-definition" pos="V">
    <member-of pred="generic-tetradrachm-exhibit-definition" family="Canned-VP"/>
   </entry>
   <entry
    stem="uses_decoration,_usually_floral,_which_is_made_of_added_clay._This_is_a_technique_typically_used_on_vases_of_the_Hellenistic_period._Its_name_comes_from_the_west_slopes_of_the_Acropolis,_where_several_of_these_vases_were_found"
    class="technique-description" pos="V">
    <member-of pred="west-sl-technique-technique-description" family="Canned-VP"/>
   </entry>
   <entry
    stem="represent_young_men,_usually_naked,_always_standing_up_straight,_with_their_palms_forming_fists_and_their_left_foot_slightly_in_front_of_the_right._They_were_used_as_burial_monuments,_or_offerings_to_temples,_especially_those_of_the_God_Apollo._They_usually_have_inscriptions_on_their_bases"
    class="exhibit-definition" pos="V">
    <member-of pred="generic-kouros-exhibit-definition" family="Canned-VP"/>
   </entry>
   <entry
    stem="are_vessels_which_were_used_for_pouring_liquids._They_have_one_handle,_a_large_belly_and_a_rim_that_projects_so_that_the_liquid_comes_out_easily"
    class="exhibit-definition" pos="V">
    <member-of pred="generic-prochous-exhibit-definition" family="Canned-VP"/>
   </entry>
   <entry stem="has_a_seal_on_which_there_is_a_representation_of_Helios_on_his_four-horsed_chariot"
    class="exhibit-form" pos="V">
    <member-of pred="exhibit50-exhibit-form" family="Canned-VP"/>
   </entry>
   <entry
    stem="are_sculptures_consisting_of_shapes_carved_on_a_surface_so_as_to_stand_out_from_the_surrounding_background"
    class="exhibit-definition" pos="V">
    <member-of pred="generic-relief-exhibit-definition" family="Canned-VP"/>
   </entry>
   <entry
    stem="probably_belonged_in_the_decoration_of_Philip_II's_death_bed,_in_the_large_grave_at_the_tomb_of_Vergina"
    class="exhibit-purpose" pos="V">
    <member-of pred="exhibit49-exhibit-purpose" family="Canned-VP"/>
   </entry>
   <entry stem="is_thought_to_depict_Philip_II" class="exhibit-form" pos="V">
    <member-of pred="exhibit49-exhibit-form" family="Canned-VP"/>
   </entry>
   <entry
    stem="Vokotopoulou,I.,_Elliniki_Techni-_Argyra_kai_Chalkina_Erga_Technis,_Ekdotiki_Athinon,_Athens_1997,_p._108,_fig._96"
    class="references" pos="S">
    <member-of pred="exhibit48-references" family="Canned-Sentence"/>
   </entry>
   <entry
    stem="Dionysus_(centre)_being_garlanded_by_maenads_in_a_state_of_ecstasy._One_maenad_(left)_is_filling_a_skyphos_with_wine,_another_(right)_is_playing_a_drum"
    class="exhibit-depicts" pos="NP">
    <member-of pred="exhibit47-exhibit-depicts" family="Canned-NP"/>
   </entry>
   <entry stem="a_shield_with_a_bust_in_its_centre,_as_was_customary_on_macedonian_coins"
    class="exhibit-depicts" pos="NP">
    <member-of pred="exhibit46-exhibit-depicts" family="Canned-NP"/>
   </entry>
   <entry
    stem="From_168_BC,_after_the_defeat_of_Perseus,_king_of_Macedonia,_by_the_Roman_Aemilius_Paulus_in_Pydna,_Macedonia_devolved_to_Roman_control._The_Romans_divided_the_region_into_four_smaller_administrative_districts,_the_so-called_merides_(sectors)._This_coin_comes_from_the_`first_merida'_of_Macedonia"
    class="exhibit-story" pos="S">
    <member-of pred="exhibit46-exhibit-story" family="Canned-Sentence"/>
   </entry>
   <entry
    stem="an_actor_playing_a_slave._He_is_standing_on_a_pedestal_with_his_right_hand_on_his_mask_and_the_left_one_behind_his_back"
    class="exhibit-depicts" pos="NP">
    <member-of pred="exhibit45-exhibit-depicts" family="Canned-NP"/>
   </entry>
   <entry
    stem="Constant_wars_during_the_Hellenistic_period_resulted_in_an_increase_in_the_number_of_slaves_in_the_entire_Mediterranean"
    class="exhibit-story" pos="S">
    <member-of pred="exhibit45-exhibit-story" family="Canned-Sentence"/>
   </entry>
   <entry
    stem="On_this_amphora_you_can_see_athletes_running_naked,_as_was_customary,_except_for_during_the_`race_in_armour',_in_which_athletes_ran_wearing_their_helmets,_shields_and_greaves_(armour_which_protected_the_bottom_half_of_the_leg)._The_sport_of_running_is_so_ancient_that_it_is_impossible_to_find_out_exactly_when_and_how_it_started._Its_importance_was_never_in_doubt,_however;_during_antiquity_it_was_one_of_the_most_important_parts_of_a_child's_education._There_were_many_running_events,_in_which_the_athletes_ran_different_distances"
    class="exhibit-story" pos="S">
    <member-of pred="exhibit44-exhibit-story" family="Canned-Sentence"/>
   </entry>
   <entry stem="a_discus_thrower_preparing_to_throw_the_discus" class="exhibit-depicts" pos="NP">
    <member-of pred="exhibit43-exhibit-depicts" family="Canned-NP"/>
   </entry>
   <entry
    stem="The_discus_thrower_on_this_kylix_is_weighing_the_discus_in_his_hands_as_he_gets_ready_to_throw_it._Discus_throwing_techniques_have_changed_little_since_ancient_times,_but_the_discus_itself,_had_various_differences._In_antiquity_it_was_initially_made_of_stone,_and_later_of_bronze,_lead_or_iron._It_weighed_between_1.3_and_6.6_kilos_and_so_the_athlete_required_both_strength_and_precision_to_direct_its_course"
    class="exhibit-story" pos="S">
    <member-of pred="exhibit43-exhibit-story" family="Canned-Sentence"/>
   </entry>
   <entry stem="an_athlete_preparing_to_throw_his_javelin" class="exhibit-depicts" pos="NP">
    <member-of pred="exhibit42-exhibit-depicts" family="Canned-NP"/>
   </entry>
   <entry
    stem="In_antiquity,_javelin_throwing_was_intimately_bound_up_with_the_Greek_way_of_life._Before_it_became_a_feature_of_sporting_life,_the_javelin_was_one_of_the_weapons_used_by_ancient_Greeks_in_war_and_hunting._A_javelin_is_a_sharp,_wooden_spear_about_the_height_of_a_tall_man"
    class="exhibit-story" pos="S">
    <member-of pred="exhibit42-exhibit-story" family="Canned-Sentence"/>
   </entry>
   <entry stem="an_athlete_preparing_to_perform_a_jump" class="exhibit-depicts" pos="NP">
    <member-of pred="exhibit41-exhibit-depicts" family="Canned-NP"/>
   </entry>
   <entry
    stem="The_origin_of_the_long_jump_lies_in_the_challenge_presented_by_traversing_the_cliffs,_ravines_and_rough_terrain_of_the_Greek_countryside,_and,_accordingly,_by_the_challenge_of_waging_war_on_this_terrain._It_was_a_complicated_sport_in_which_the_athletes_used_special_weights,_the_halteres,_to_increase_their_momentum_and_the_distance_of_the_jump._On_this_lekythos,_the_athlete_holds_the_weights_in_his_hands_and_is_about_to_jump_away_from_the_springboard._In_order_to_win,_he_needs_not_only_great_speed_and_strong_legs_but_also_precise_coordination_between_his_hands_and_feet_as_they_make_contact_with_the_springboard._This_is_why_the_long_jump_was_occasionally_accompanied_by_music,_which_helped_the_jumper_pace_his_rhythm"
    class="exhibit-story" pos="S">
    <member-of pred="exhibit41-exhibit-story" family="Canned-Sentence"/>
   </entry>
   <entry stem="consists_of_a_helmet_and_a_cuirass_(which_covered_the_chest_and_back)"
    class="exhibit-form" pos="V">
    <member-of pred="exhibit40-exhibit-form" family="Canned-VP"/>
   </entry>
   <entry stem="480_and_323_B.C." class="historical-period-time" pos="NP">
    <member-of pred="classical-period-historical-period-time" family="Canned-NP"/>
   </entry>
   <entry
    stem="was_defined_by_the_rise_in_the_political_supremacy_of_Athens_(its_'golden_age')_and_the_expansion_of_the_Greek_world_under_the_rule_of__Alexander_the_Great_of_Macedonia"
    class="historical-period-description" pos="V">
    <member-of pred="classical-period-historical-period-description" family="Canned-VP"/>
   </entry>
   <entry
    stem="are_made_of_fine_quality_clay_and_have_painted_decoration_on_a_white_background._They_took_their_name_from_the_Hadra_Necropolis,_near_Alexandria,_where_a_large_number_of_them_were_found._They_were_produced_between_the_end_of_the_4th_and_the_beginning_of_the_2nd_century_BC._Their_shape_and_decoration_was_replicated_by_many_workshops"
    class="exhibit-definition" pos="V">
    <member-of pred="generic-hydria-hadra-exhibit-definition" family="Canned-VP"/>
   </entry>
   <entry
    stem="a_view_of_the_harbour_of_Patras_from_the_sea._In_the_background_there_are_rows_of_columns,_temples_and_other_buildings;in_the_foreground_there_is_a_ship_and_a_statue_of_a_male_form"
    class="exhibit-depicts" pos="NP">
    <member-of pred="exhibit39-exhibit-depicts" family="Canned-NP"/>
   </entry>
   <entry
    stem="is_possibly_the_helmet_of_the_famous_Miltiades,_who_donated_it_to_the_sanctuary_of_Zeus_after_the_battle_of_Marathon"
    class="exhibit-characteristics" pos="V">
    <member-of pred="exhibit38-exhibit-characteristics" family="Canned-VP"/>
   </entry>
   <entry stem="&quot;MILTIADES_ETHEKEN_TO_DII&quot;_(Miltiades_offered_to_Zeus)"
    class="inscription-says" pos="NP">
    <member-of pred="exhibit38-inscription-says" family="Canned-NP"/>
   </entry>
   <entry
    stem="an_Athenian_warrior_bidding_his_wife_farewell;_she_is_seated_on_a_klismos,_which_is_a_type_of_chair"
    class="exhibit-depicts" pos="NP">
    <member-of pred="exhibit37-exhibit-depicts" family="Canned-NP"/>
   </entry>
   <entry stem="Scenes_related_to_war_were_quite_frequent_in_Athenian_art_during_this_period"
    class="exhibit-story" pos="S">
    <member-of pred="exhibit37-exhibit-story" family="Canned-Sentence"/>
   </entry>
   <entry
    stem="a_young_woman_in_the_act_of_sacrificing_at_an_altar._She_is_carrying_a_basket_in_her_left_hand,_and_pouring_wine_on_the_blazing_altar_with_her_right"
    class="exhibit-depicts" pos="NP">
    <member-of pred="exhibit36-exhibit-depicts" family="Canned-NP"/>
   </entry>
   <entry stem="'EUKARPOS_PHILOXENOU_MEILESIOS_PHILOXENOS_MEILESIOY'" class="inscription-says"
    pos="NP">
    <member-of pred="exhibit35-inscription-says" family="Canned-NP"/>
   </entry>
   <entry stem="two_farmers,_as_can_be_seen_from_the_ploughshare_depicted_on_the_pediment"
    class="exhibit-depicts" pos="NP">
    <member-of pred="exhibit35-exhibit-depicts" family="Canned-NP"/>
   </entry>
   <entry
    stem="the_goddess_Athena_shaking_the_hand_of_a_thoughtful_man_(representing_the_deme_(area)_of_Athens)"
    class="exhibit-depicts" pos="NP">
    <member-of pred="exhibit34-exhibit-depicts" family="Canned-NP"/>
   </entry>
   <entry
    stem="is_the_best_preserved_painting_among_the_ones_that_were_found_in_the_Pitsa_Cave._All_of_them_are_covered_with_a_white_coating_and_their_figures_are_decorated_in_several_colours"
    class="exhibit-form" pos="V">
    <member-of pred="exhibit33-exhibit-form" family="Canned-VP"/>
   </entry>
   <entry stem="a_sacrifice" class="exhibit-depicts" pos="NP">
    <member-of pred="exhibit33-exhibit-depicts" family="Canned-NP"/>
   </entry>
   <entry
    stem="were_special_drinking_cups._They_had_a_high_base_and_projecting_handles_that_stretched_from_the_rim_to_the_bottom_of_the_cup._An_ancient_myth_said_that_Dionysus,_the_god_of_wine,_invented_them_himself!"
    class="exhibit-definition" pos="V">
    <member-of pred="generic-kantharos-exhibit-definition" family="Canned-VP"/>
   </entry>
   <entry stem="a_carpenter_at_work" class="exhibit-depicts" pos="NP">
    <member-of pred="exhibit32-exhibit-depicts" family="Canned-NP"/>
   </entry>
   <entry stem="was_used_in_religious_worship" class="exhibit-purpose" pos="V">
    <member-of pred="exhibit31-exhibit-purpose" family="Canned-VP"/>
   </entry>
   <entry
    stem="a_woman_raising_the_cover_of_a_chest,_in_order_to_take_out_a_folded_cloth._A_basket,_a_mirror,_a_lekythos_and_a_kantharos_are_hanging_on_the_wall"
    class="exhibit-depicts" pos="NP">
    <member-of pred="exhibit31-exhibit-depicts" family="Canned-NP"/>
   </entry>
   <entry stem="are_broken_fragments_of_pottery" class="exhibit-definition" pos="V">
    <member-of pred="generic-potsherd-exhibit-definition" family="Canned-VP"/>
   </entry>
   <entry
    stem="were_large_jars_used_mostly_for_carrying_water._They_had_three_handles,_two_horizontal_and_one_vertical"
    class="exhibit-definition" pos="V">
    <member-of pred="generic-hydria-exhibit-definition" family="Canned-VP"/>
   </entry>
   <entry stem="seven_relief_busts_of_the_members_of_a_family" class="exhibit-depicts" pos="NP">
    <member-of pred="exhibit29-exhibit-depicts" family="Canned-NP"/>
   </entry>
   <entry
    stem="The_family_was_the_basic_social_unit_of_Roman_society,_since_wealth_and_social_status_were_transmitted_through_it._Roman_private_law_is_our_main_source_of_information_for_the_Roman_family_(familia),_the_members_of_which_were_under_the_control_of_one_individual,_the_father,_known_as_the_pater_familias"
    class="exhibit-story" pos="S">
    <member-of pred="exhibit29-exhibit-story" family="Canned-Sentence"/>
   </entry>
   <entry stem="a_Greek_hunting_a_Persian" class="exhibit-depicts" pos="NP">
    <member-of pred="exhibit28-exhibit-depicts" family="Canned-NP"/>
   </entry>
   <entry stem="end_in_a_conical_fitting" class="exhibit-form" pos="V">
    <member-of pred="exhibit27-exhibit-form" family="Canned-VP"/>
   </entry>
   <entry
    stem="are_wine_cups_with_a_shallow_bowl_placed_on_top_of_a_base.__They_have_two_horizontal_handles"
    class="exhibit-definition" pos="V">
    <member-of pred="generic-kylix-exhibit-definition" family="Canned-VP"/>
   </entry>
   <entry
    stem="&quot;Mourning_Athena&quot;._The_goddess_is_clad_in_an_Attic_peplos_(gown)_with_a_belt,_leaning_on_her_spear_looking_melancholically_at_a_rectangular_stele_(gravestone),_which_according_to_some_scholars_bears_the_names_of_those_killed_in_a_battle"
    class="exhibit-depicts" pos="NP">
    <member-of pred="exhibit26-exhibit-depicts" family="Canned-NP"/>
   </entry>
   <entry
    stem="Dionysos_seated_and_wearing_a_crown_of_olives._In_front_of_him_stands_a_satyr_with_an_oinochoe_(wine_jug)_in_his_hands._Hanging_on_the_architrave_are_five_masks,_of_(from_left)-_the_Tetchy_Father;_the_Old_Woman;_the_Crafty_Slave;_the_Beardless_Youth;_and_the_Young_Woman_with_Short_Hair"
    class="exhibit-depicts" pos="NP">
    <member-of pred="exhibit25-exhibit-depicts" family="Canned-NP"/>
   </entry>
   <entry stem="is_spherical_in_shape" class="exhibit-form" pos="V">
    <member-of pred="exhibit24-exhibit-form" family="Canned-VP"/>
   </entry>
   <entry
    stem="On_the_body_a_wide_zone_is_distinguished_with_pairs_of_comastes_among_supplementary_patterns,_mainly_rosettes_(jewels_representing_roses_with_open_radiate_leaves)._&quot;Comastes&quot;_were_the_participants_in_&quot;comous&quot;,_feasts_in_honour_of_Dionysus"
    class="exhibit-story" pos="S">
    <member-of pred="exhibit24-exhibit-story" family="Canned-Sentence"/>
   </entry>
   <entry
    stem="'Mantiklos_dedicated_me_as_a_tithe_(tax)_to_the_Archer_God_of_the_Silver_Bow._And_you,_Phoebus_(Apollo),_return_the_favour!'"
    class="inscription-says" pos="NP">
    <member-of pred="exhibit23-inscription-says" family="Canned-NP"/>
   </entry>
   <entry stem="has_an_inscription_on_its_thigh_in_the_shape_of_a_horseshoe" class="exhibit-form"
    pos="V">
    <member-of pred="exhibit23-exhibit-form" family="Canned-VP"/>
   </entry>
   <entry stem="a_young_man_who_is_sitting_down_and_writing_with_a_stylus_(pen)"
    class="exhibit-depicts" pos="NP">
    <member-of pred="exhibit22-exhibit-depicts" family="Canned-NP"/>
   </entry>
   <entry
    stem="During_the_archaic_period,_the_most_poular_method_of_writing_must_have_been_wooden_tablets_coated_with_wax,_on_which_letters_were_written_with_the_stylus_and_could_easily_be_rubbed_out_and_rewritten"
    class="exhibit-story" pos="S">
    <member-of pred="exhibit22-exhibit-story" family="Canned-Sentence"/>
   </entry>
   <entry stem="states_the_names_of_the_people_depicted_and_the_sculptor" class="exhibit-form"
    pos="V">
    <member-of pred="exhibit21-exhibit-form" family="Canned-VP"/>
   </entry>
   <entry stem="the_Athenian_hoplite_(soldier)_Aristion" class="exhibit-depicts" pos="NP">
    <member-of pred="exhibit21-exhibit-depicts" family="Canned-NP"/>
   </entry>
   <entry
    stem="The_burial_customs_of_the_Archaic_period_make_it_clear_that_the_place_of_the_individual_was_beginning_to_be_defined_in_his_city"
    class="exhibit-story" pos="S">
    <member-of pred="exhibit21-exhibit-story" family="Canned-Sentence"/>
   </entry>
   <entry stem="The_&quot;West_Slope&quot;_decoration_is_obvious_on_the_neck_of_this_kantharos"
    class="exhibit-story" pos="S">
    <member-of pred="exhibit20-exhibit-story" family="Canned-Sentence"/>
   </entry>
   <entry
    stem="introduced_a_decoration_that_is_much_more_ornamental_than_Attic_vase_painting_of_previous_periods._Multi-level_compositions_also_became_more_frequent"
    class="style-description" pos="V">
    <member-of pred="rich-style-style-description" family="Canned-VP"/>
   </entry>
   <entry stem="the_leader_of_the_Galatians_committing_suicide_after_having_already_killed_his_wife"
    class="exhibit-depicts" pos="NP">
    <member-of pred="exhibit19-exhibit-depicts" family="Canned-NP"/>
   </entry>
   <entry
    stem="The_original_statue_was_part_of_a_larger_bronze_synthesis,_placed_in_the_yard_of_Athena's_sanctuary"
    class="exhibit-story" pos="S">
    <member-of pred="exhibit19-exhibit-story" family="Canned-Sentence"/>
   </entry>
   <entry stem="is_one_of_the_best_examples_of_a_propaganda_statue" class="exhibit-form" pos="V">
    <member-of pred="exhibit17-exhibit-form" family="Canned-VP"/>
   </entry>
   <entry
    stem="In_keeping_with_the_classical_models,_the_emperor_is_shown_half_nude,_as_a_heroized_leader"
    class="exhibit-story" pos="S">
    <member-of pred="exhibit17-exhibit-story" family="Canned-Sentence"/>
   </entry>
   <entry
    stem="a_banker_in_front_of_&quot;mensa_nummularia&quot;,_which_was_a_table_used_for_counting_out_coins"
    class="exhibit-depicts" pos="NP">
    <member-of pred="exhibit16-exhibit-depicts" family="Canned-NP"/>
   </entry>
   <entry
    stem="a_wedding_scene-_two_newlyweds_on_a_carriage_escorted_by_relatives_and_friends._The_event_of_the_bride's_transport_to_her_new_house_was_very_important,_because_a_marriage_was_considered_valid_only_after_the_bride_and_the_groom_started_living_together"
    class="exhibit-depicts" pos="NP">
    <member-of pred="exhibit15-exhibit-depicts" family="Canned-NP"/>
   </entry>
   <entry stem="1.94_metres" class="exhibit-height" pos="NP">
    <member-of pred="exhibit12-exhibit-height" family="Canned-NP"/>
   </entry>
   <entry stem="an_old_woman_carrying_a_basket_of_fruit_and_vegetables" class="exhibit-depicts"
    pos="NP">
    <member-of pred="exhibit12-exhibit-depicts" family="Canned-NP"/>
   </entry>
   <entry
    stem="Compared_to_the_idealistic_portraits_of_the_classical_period,_the_hellenistic_ones_express_the_features_of_the_face_with_a_more_intense_realism._The_gradual_replacement_of_the_classical_idealisation_by_a_more_individualistic_realism_became_one_of_the_most_typical_characteristics_of_hellenistic_art"
    class="exhibit-story" pos="S">
    <member-of pred="exhibit12-exhibit-story" family="Canned-Sentence"/>
   </entry>
   <entry
    stem="has_the_head_of_Athena_with_a_Corinthian_helmet_on_the_reverse_side,_as_was_common_in_coins_of_the_Ancient_World._On_the_obverse_side_is_a_female_figure,_the_personification_of_Aetolia,_seated_on_Macedonian_and_Galatic_shields._The_scene_refers_to_the_fight_of_the_Aetolians_against_the_Macedonians_and_the_Galatians"
    class="exhibit-form" pos="V">
    <member-of pred="exhibit11-exhibit-form" family="Canned-VP"/>
   </entry>
   <entry
    stem="a_wedding_scene,_showing_a_bride_in_nymphides,_that_is_'bridal_footwear'._In_many_scenes_related_to_the_adorning_of_the_bride,_the_sandals_receive_especially_detailed_treatment"
    class="exhibit-depicts" pos="NP">
    <member-of pred="exhibit10-exhibit-depicts" family="Canned-NP"/>
   </entry>
   <entry stem="31_B.C._and_the_4th_century_A.D" class="historical-period-time" pos="NP">
    <member-of pred="roman-period-historical-period-time" family="Canned-NP"/>
   </entry>
   <entry
    stem="represents_a_period_when_the_Greek_world_was_under_the_rule_of_the_Romans,_for_whom_and_under_whose_patronage_many_Greek_artists_worked"
    class="historical-period-description" pos="V">
    <member-of pred="roman-period-historical-period-description" family="Canned-VP"/>
   </entry>
   <entry
    stem="In_imperial_portraits,_all_the_Emperors,_even_the_older_ones,_were_portrayed_youthfully._These_portraits_were_strongly_inspired_by_the_classical_statues_of_the_5th_century_BC,_especially_the_ones_made_by_Polykleitus._Imperial_portraits_first_appeared_in_the_capital,_Rome,_but_later_they_spread_all_over_the_Empire,_with_the_help_of_casts,_known_as_&quot;imagines&quot;"
    class="exhibit-story" pos="S">
    <member-of pred="generic-imperial-portrait-exhibit-story" family="Canned-Sentence"/>
   </entry>
   <entry stem="700_and_480_B.C." class="historical-period-time" pos="NP">
    <member-of pred="archaic-period-historical-period-time" family="Canned-NP"/>
   </entry>
   <entry
    stem="marked_the_beginnings_of_Greek_monumental_stone_sculpture_and_other_developments_in_the_naturalistic_representation_of_the_human_figure"
    class="historical-period-description" pos="V">
    <member-of pred="archaic-period-historical-period-description" family="Canned-VP"/>
   </entry>
   <entry
    stem="The_side_of_a_coin_which_displays_the_principal_symbol_(`heads'_in_`heads_or_tails')_is_known_as_the_obverse"
    class="exhibit-story" pos="S">
    <member-of pred="generic-coin-exhibit-story" family="Canned-Sentence"/>
   </entry>
   <entry stem="323_and_31_B.C." class="historical-period-time" pos="NP">
    <member-of pred="hellenistic-period-historical-period-time" family="Canned-NP"/>
   </entry>

   <entry
    stem="covers_the_chaotic_period_from_the_Death_of_Alexander_the_Great_and_the_subsequent_dissolution_of_his_empire_to_the_victory_of_the_Romans_over_the_Greeks_at_the_Battle_of_Actium,_comprising_a_truly_cosmopolitan_or_international_range_of_artistic_trends"
    class="historical-period-description" pos="V">
    <member-of pred="hellenistic-period-historical-period-description" family="Canned-VP"/>
   </entry>
   <entry
    stem="are_basically_oil_bottles._They_are_vessels_with_a_tall_shape,_usually_forming_an_ellipse;_they_have_a_base,_a_single_vertical_handle,_a_narrow_neck_and_a_small_mouth"
    class="exhibit-definition" pos="V">
    <member-of pred="generic-lekythos-exhibit-definition" family="Canned-VP"/>
   </entry>
   <entry
    stem="have_an_ovoid_body_and_two_looped_handles,_reaching_from_the_shoulders_up._This_was_a_very_common_shape_in_ancient_times"
    class="exhibit-definition" pos="V">
    <member-of pred="generic-amphora-exhibit-definition" family="Canned-VP"/>
   </entry>
   <entry
    stem="are_a_special_sort_of_relief,_which_ancient_people_used_in_order_to_commemorate_members_of_their_family_and_friends_who_had_died._These_reliefs_were_placed_in_grave_areas._Many_of_them_depict_scenes_from_the_life_of_the_deceased_and_have_inscriptions_that_give_interesting_information_about_them._The_quality_of_the_relief_was_dependent_on_the_social_class_and_the_economic_status_of_the_deceased"
    class="exhibit-definition" pos="V">
    <member-of pred="generic-grave-exhibit-definition" family="Canned-VP"/>
   </entry>
   <entry
    stem="is_the_most_typical_representative_of_the_rich_style._His_figures_are_graceful;_they_are_often_posed_as_though_dancing,_with_expressions_that_range_from_tenderness_to_melancholy._The_atmosphere_is_low-key,_avoiding_drama_-_a_long_way_from_the_Classical_models_of_the_previous_generation._The_clothing_on_this_painter's_pots_is_always_very_carefully_drawn-_it_has_patterns_of_plant_motifs_or_stars._His_compositions_are_well_balanced;_They_manage_to_give_a_'lift'_to_the_hydria_and_other_kinds_of_pot_awkward_to_decorate"
    class="person-story" pos="V">
    <member-of pred="painter-of-meidias-person-story" family="Canned-VP"/>
   </entry>
   <entry
    stem="The_decoration_of_ancient_Greek_vessels_provides_a_lot_of_information_about_the_life,_the_habits_and_the_beliefs_of_the_Ancient_Greeks._Decoration_of_Ancient_Greek_pottery_began_with_simple_linear_drawings_but_gradually,_potters_started_to_depict_scenes_from_nature,_including_plants,_animals_and_finally_human_figures_on_their_vases._There_was_not_usually_any_decoration_on_pots_used_every_day_in_poor_households_and_in_shops._The_colours_and_decorations_used_on_vessels_help_to_determine_their_period_of_creation"
    class="exhibit-story" pos="S">
    <member-of pred="generic-vessel-exhibit-story" family="Canned-Sentence"/>
   </entry>
   <entry
    stem="were_large_open_globular_pots,_perhaps_based_on_bronze_originals._They_had_many_uses,_but_it_seems_that_they_was_mostly_used_for_mixing_wine_and_water_for_ritual_and_festival_events"
    class="exhibit-definition" pos="V">
    <member-of pred="generic-cauldron-exhibit-definition" family="Canned-VP"/>
   </entry>
   <entry
    stem="were_pots_used_by_athletes_to_hold_oil,_with_which_they_cleaned_themselves_after_exercising._Each_athlete_probably_had_his_personal_aryballos._They_are_usually_ball_shaped_with_one_or_two_handles._Some_have_the_shape_of_animals,_birds,_or_human_heads"
    class="exhibit-definition" pos="V">
    <member-of pred="generic-aryballos-exhibit-definition" family="Canned-VP"/>
   </entry>
   <entry
    stem="The_handles_of_Rhodian_amphoras,_which_have_been_found_dispersed_in_the_Mediterranean,_reveal_the_island's_trade_relations_with_different_regions_in_that_area"
    class="exhibit-story" pos="S">
    <member-of pred="generic-amphora-handle-exhibit-story" family="Canned-Sentence"/>
   </entry>
   <entry
    stem="were_special_cups_for_wine,_mostly_used_in_rituals._They_were_made_in_a_variety_of_shapes,_resembling_a_horn,_the_head_of_an_animal,_or_the_figure_of_a_person"
    class="exhibit-definition" pos="V">
    <member-of pred="generic-rhyton-exhibit-definition" family="Canned-VP"/>
   </entry>
   <entry
    stem="were_amphoras_given_as_prizes_to_the_winners_of_the_Panathenaic_games,_which_were_held_in_Athens_in_honor_of_the_city's_patron_godess,_Athena"
    class="exhibit-definition" pos="V">
    <member-of pred="generic-panathenaic-amphora-exhibit-definition" family="Canned-VP"/>
   </entry>



   <entry
    stem="made_a_major_contribution_to_art_through_his_studies_of_the_proportions_and_symmetry_of_the_human_body._He_summed_up_his_conclusions_in_a_written_text,_'the_Canon'._This_text,_together_with_his_sculptures_was_to_be_a_decisive_influence_in_the_centuries_which_followed._Since_Polykleitos_embodied_his_theoretical_observations_in_a_sculpture_called_Doryphorus,_this_sculpture_itself_is_also_known_as_the_Canon"
    class="person-information" pos="V">
    <member-of pred="polyklitus-person-information" family="Canned-VP"/>
   </entry>
   <entry
    stem="was_given_this_title_because_his_actual_name_is_not_known,_but_we_know_that_he_used_to_decorate_vases_made_by_a_pot_maker_named_Kleofrades._He_can_be_distinguished_among_the_painters_who_decorated_big_vases;_his_works_are_characterised_by_tension,_dynamism_and_dramatic_movement;_these_attributes_clearly_show_the_influences_of_Euthimides_and_the_school_of_Pioneers._He_placed_emphasis_on_the_details_of_the_eyes,_the_nose_and_the_ears._Among_his_most_interesting_works_are_a_krater_(a_type_of_bowl)_and_an_amphora_with_dionysian_scenes_and_a_kalpis_(a_sort_of_hydria)_with_scenes_from_Iliou_Persis,_a_lost_epic_poem_about_the_fall_of_Troy_by_the_Greeks.__This_scene_has_strong_symbolic_value,_because_at_the_time_is_was_painted,_Greece_was_facing_the_Persian_Invasion"
    class="person-information" pos="V">
    <member-of pred="painter-of-kleofrades-person-information" family="Canned-VP"/>
   </entry>
   <entry
    stem="was_one_of_the_12_olympian_gods._The_myth_tells_us_that_he_was_born_in_Delos,_and_was_the_son_of_Zeus_and_Leto._He_had_a_twin_sister,_Artemis,_who_was_also_an_Olympian_goddess._Apollo_was_the_god_of_music_and_light_and_symbolized_the_sun._He_was_very_dear_to_ancient_Greeks,_who_devoted_some_very_important_sacred_places_to_him"
    class="person-information" pos="V">
    <member-of pred="apollo-person-information" family="Canned-VP"/>
   </entry>
   <entry
    stem="was_known_as_the_protector_of_the_animals._Her_cult_came_from_the_East_and_in_Greece_it_was_identified_with_the_goddess_Artemis"
    class="person-information" pos="V">
    <member-of pred="potnia-person-information" family="Canned-VP"/>
   </entry>
   <entry
    stem="was_given_this_title_because_his_exact_name_is_not_known,_but_he_decorated_a_pot_signed_by_the_pot_maker_Meidias"
    class="person-information" pos="V">
    <member-of pred="painter-of-meidias-person-information" family="Canned-VP"/>
   </entry>
   <entry
    stem="is_considered_to_be_one_of_the_most_successful_craftsmen_of_his_period._His_work_is_marked_by_imagination_and_grace,_elegance_and_originality._He_mainly_made_moulded_vessels_shaped_like_animal_heads._(A_moulded_vessel_is_a_vessel_in_the_shape_of_some_human_or_animal_figure.)_At_the_same_time_he_was_producing_other_types_of_pots,_like_kylixes,_with_unusually_slender_handles._He_was_in_long_term_partnership_with_a_painter,_known_to_us_as_the_Painter_of_Sotades"
    class="person-information" pos="V">
    <member-of pred="sotades-person-information" family="Canned-VP"/>
   </entry>
   <entry stem="is_thought_to_have_been_both_a_maker_and_a_painter_of_pots"
    class="person-information" pos="V">
    <member-of pred="amasis-person-information" family="Canned-VP"/>
   </entry>


   <!-- end of canned text -->

   <!-- fixed strings extracted from mpiro predicates -->

   <entry pos="Adv" class="string" stem="In">
    <member-of family="Adverb"/>
   </entry>

   <entry pos="Adv" class="string" stem="has_a_picture_of">
    <member-of family="Adverb"/>
   </entry>

   <entry pos="Adv" class="string" stem="is_only">
    <member-of family="Adverb"/>
   </entry>

   <entry pos="Adv" class="string" stem="of_the_original.">
    <member-of family="Adverb-final"/>
   </entry>

   <entry pos="Adv" class="string" stem="is_not_the_original_object,">
    <member-of family="Adverb"/>
   </entry>

   <entry pos="Adv" class="string" stem="it_is">
    <member-of family="Adverb"/>
   </entry>

   <entry pos="Adv" class="string" stem="name_means">
    <member-of family="Adverb"/>
   </entry>

   <entry pos="Adv" class="string" stem="For_further_information,_see">
    <member-of family="Adverb"/>
   </entry>

   <entry pos="Adv" class="string" stem="The_inscription_on">
    <member-of family="Adverb"/>
   </entry>

   <entry pos="Adv" class="string" stem="was_the_king_of">
    <member-of family="Adverb"/>
   </entry>

   <entry pos="Adv" class="string" stem="covers_the_time">
    <member-of family="Adverb"/>
   </entry>

   <entry pos="Adv" class="string" stem="is_the_period">
    <member-of family="Adverb"/>
   </entry>



   <!-- end of fixed strings -->



   <!-- Add core macros -->
   <!--<xsl:call-template name="add-macros"/>-->

  </dictionary>
 </xsl:template>
</xsl:transform>
