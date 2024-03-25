from pyrealb import *
import abc

class LexicalChoices(abc.ABC):
    @property
    @abc.abstractmethod
    def v_be(self):pass

    @property
    @abc.abstractmethod
    def conj_and(self):pass

    @property
    @abc.abstractmethod
    def pro_I(self):pass

    @property
    @abc.abstractmethod
    def def_det(self):pass

    @property
    @abc.abstractmethod
    def undef_det(self):pass

    @property
    @abc.abstractmethod
    def lang(self):pass

    @property
    @abc.abstractmethod
    def sentence_patterns(self): pass

    @property
    @abc.abstractmethod
    def wikidata_properties(self): pass

    @abc.abstractmethod
    def rel_pro(self,isHuman): pass

    @abc.abstractmethod
    def direction(self, dir): pass

    @abc.abstractmethod
    def number_of(self, entities): pass

    @abc.abstractmethod
    def fix_language(self, term): pass

    @abc.abstractmethod
    def runway(self, no, type): pass

    @abc.abstractmethod
    def code(self, type): pass

