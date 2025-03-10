# building html documentation to be installed at http://www.iro.umontreal.ca/~lapalme/pyrealb/documentation.html
#   make all : recompile all html if needed
#   make export : list all files that should be exported to the pyrealb-documentation directory of my home page
%.html : %.md
	pandoc -o $@ $<

documentation.html: documentation.py
	python3 documentation.py

docs = Lexicon-Format-en.html Lexicon-Format-fr.html Realizer-Architecture.html Hacking-pyrealb.html documentation.html

.PHONY: all export
all : ${docs}
export:
	@echo ${docs} user.js style.css classes-hierarchy.jpg pyrealb-classes.jpg

