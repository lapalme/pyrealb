import xml.etree.ElementTree as ET
from pprint import pprint

# parse dict.xsl to get the canned text strings
canned = {}

tree = ET.parse("dict.xsl")
for entry in tree.getroot().iter("entry"):
    stem=entry.get("stem")
    if stem.endswith("np"):
        canned[stem]=[entry.find("word").get("form"),entry.get("pos")]
    else:
        member=entry.find("./member-of")
        if member is not None and "family" in member.attrib:
            family=member.get("family")
            if family.startswith("Canned"):
                canned[member.get("pred")]=[entry.get("stem"),entry.get("pos")]

for k,vs in sorted(canned.items()):
    print(k+"\t"+vs[0]+"\t"+vs[1])
