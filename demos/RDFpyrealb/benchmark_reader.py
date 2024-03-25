# Extracted from the Benchmark_reader for the WebNLG Challenge 2020
from os import listdir
import random, re

class Triple:

    def __init__(self, s, p, o):
        self.s = s
        self.o = o
        # if p[0].isupper():
        #     p = p[0].lower()+p[1:]
        self.p = p

    def flat_triple(self):
        return self.s + ' | ' + self.p + ' | ' + self.o


class Tripleset:

    def __init__(self):
        self.triples = []
        self.clusterid = 0

    def fill_tripleset(self, t):
        for xml_triple in t:
            s, p, o = xml_triple.text.split(' | ')
            triple = Triple(s, p, o)
            self.triples.append(triple)

    def fill_tripleset_text(self,texts):
        for text in texts:
            s, p, o = text.split(' | ')
            triple = Triple(s, p, o)
            self.triples.append(triple)


class Lexicalisation:

    def __init__(self, lex, lid, comment='', lang=''):
        self.lex = lex
        self.id = lid
        self.comment = comment
        self.lang = lang

    def chars_length(self):
        return len(self.lex)


class Entry:

    def __init__(self, category, size, eid, shape, shape_type):
        self.category = category
        self.size = size
        self.id = eid
        self.shape = shape
        self.shape_type = shape_type
        self.originaltripleset = []
        self.modifiedtripleset = Tripleset()
        self.lexs = []
        self.dbpedialinks = []
        self.links = []

    def fill_originaltriple(self, xml_t):
        otripleset = Tripleset()
        self.originaltripleset.append(otripleset)   # multiple originaltriplesets for one entry
        otripleset.fill_tripleset(xml_t)

    def fill_modifiedtriple(self, xml_t):
        self.modifiedtripleset.fill_tripleset(xml_t)

    def create_lex(self, xml_lex):
        try:
            comment = xml_lex.attrib['comment']
        except KeyError:
            comment = ''
        try:
            lang = xml_lex.attrib['lang']
        except KeyError:
            lang = ''
        lid = xml_lex.attrib['lid']
        lex = Lexicalisation(xml_lex.text, lid, comment, lang)
        self.lexs.append(lex)

    def fill_modifiedtriple_texts(self, texts):
        self.modifiedtripleset.fill_tripleset_text(texts)

    def create_dbpedialinks(self, xml_dbpedialinks):
        for xml_dblink in xml_dbpedialinks:
            s, p, o = xml_dblink.text.split(' | ')
            dbp_link = Triple(s, p, o)
            self.dbpedialinks.append(dbp_link)

    def create_links(self, xml_links):
        for xml_link in xml_links:
            s, p, o = xml_link.text.split(' | ')
            link = Triple(s, p, o)
            self.links.append(link)

    def count_lexs(self):
        return len(self.lexs)

    def flat_tripleset(self):
        """
        Render modified triples to the flat representation with <br>.
        :return: flat representation
        """
        flat_mr = []
        for triple in self.modifiedtripleset.triples:
            flat_triple = triple.s + ' | ' + triple.p + ' | ' + triple.o
            flat_mr.append(flat_triple)
        if self.size == '1':
            return flat_mr[0]
        else:
            return '<br>'.join(flat_mr)

    def relations(self):
        """
        Give a set of properties found in tripleset
        :return: set of properties
        """
        rel_set = set()
        for triple in self.modifiedtripleset.triples:
            rel_set.add(triple.p)
        return rel_set

    def list_triples(self):
        """
        Return a list of triples for an entry.
        :return: list of triples
        """
        triples = []
        for triple in self.modifiedtripleset.triples:
            flat_triple = triple.s + ' | ' + triple.p + ' | ' + triple.o
            triples.append(flat_triple)
        return triples

    def has_property(self,tripleRE):
        """
        Check if one the triple has a property that matches a regex
        :param tripleRE: regex to match a property
        :return: True
        """
        for triple in self.modifiedtripleset.triples:
            if re.match(tripleRE,triple.p,re.I) is not None:
                return True
        return False

class Benchmark:

    def __init__(self):
        self.entries = []

    def benchmark_from_dataset(self, dataset, category='', start=1, end=7, eid=None):
        from collections import Counter
        counts = Counter()
        cat_counts = Counter()
        for i in range(len(dataset)):
            data = dataset[i]
            if (category == '' or category==data['category']) and start <= data["size"] <= end\
                    and (eid is None or eid == data["eid"] ):
                entry = Entry(data['category'],data['size'],data["eid"],data['shape'],data["shape_type"])
                data_lex = data["lex"]
                counts[data['size']]+=1
                cat_counts[(data['category'],data["size"])]+=1
                entry.lexs = [Lexicalisation(text, lid, comment, "en")
                              for (text,lid,comment) in zip(data_lex["text"],data_lex["lid"],data_lex["comment"])]
                for m_triples in data["modified_triple_sets"]["mtriple_set"]:
                    entry.fill_modifiedtriple_texts(m_triples)
                self.entries.append(entry)
        # print(counts)
        # print([f"{k[0]}-{k[1]}:{cat_counts[k]}" for k in sorted(cat_counts)])

    def fill_benchmark(self, fileslist):
        """
        Parse xml files and fill Benchmark with Entry instances.
        :param fileslist: [(path_to_file, filename.xml), (), ... ()]
        :return:
        """
        for file in fileslist:
            import sys
            import xml.etree.ElementTree as Et
            myfile = file[0] + '/' + file[1]
            sys.stderr.write("Loading: "+myfile+"\n")
            tree = Et.parse(myfile)
            root = tree.getroot()
            for xml_entry in root.iter('entry'):
                entry_id = xml_entry.attrib['eid']
                category = xml_entry.attrib['category']
                size = xml_entry.attrib['size']
                shape = xml_entry.attrib['shape'] if 'shape' in xml_entry.attrib else ""
                shape_type = xml_entry.attrib['shape_type'] if 'shape_type' in xml_entry.attrib else ""

                entry = Entry(category, size, entry_id, shape, shape_type)
                for child in xml_entry:
                    if child.tag == 'originaltripleset':
                        entry.fill_originaltriple(child)
                    elif child.tag == 'modifiedtripleset':
                        entry.fill_modifiedtriple(child)
                    elif child.tag == 'lex':
                        entry.create_lex(child)
                    elif child.tag == 'dbpedialinks':
                        entry.create_dbpedialinks(child)
                    elif child.tag == 'links':
                        entry.create_links(child)
                self.entries.append(entry)

    def total_lexcount(self):
        count = [entry.count_lexs() for entry in self.entries]
        return sum(count)

    def unique_p_otriples(self):
        properties = [triple.p for entry in self.entries for triple in entry.originaltripleset[0].triples]
        return set(properties)

    def unique_p_mtriples(self):
        properties = [triple.p for entry in self.entries for triple in entry.modifiedtripleset.triples]
        return set(properties)

    def entry_count(self, size=None, cat=None):
        """
        calculate the number of entries in benchmark
        :param size: size (should be string)
        :param cat: category
        :return: entry count
        """
        if not size and cat:
            entries = [entry for entry in self.entries if entry.category == cat]
        elif not cat and size:
            entries = [entry for entry in self.entries if entry.size == size]
        elif not size and not cat:
            return len(self.entries)
        else:
            entries = [entry for entry in self.entries if entry.category == cat and entry.size == size]
        return len(entries)

    def lexcount_size_category(self, size, cat):
        """Calculate the number of lexicalisations."""
        counts = [entry.count_lexs() for entry in self.entries if entry.category == cat and entry.size == size]
        return sum(counts)


    def triplesets(self):
        """
        List of all modified triplesets.
        :return: a list of objects Tripleset
        """
        all_triplesets = [entry.modifiedtripleset for entry in self.entries]
        return all_triplesets

    def get_lex_by_id(self, entry_category, entry_size, entry_id, lex_id):
        """Get lexicalisation by supplying entry and lex ids."""
        for entry in self.entries:
            if entry.id == entry_id and entry.size == entry_size and entry.category == entry_category:
                for lex in entry.lexs:
                    if lex.id == lex_id:
                        return lex.lex

    def subjects_predicates_objects(self):
        from collections import Counter
        subjects = Counter()
        predicates = Counter()
        objects = Counter()
        for entry in self.entries:
            for triple in entry.modifiedtripleset.triples:
                subjects[triple.s]+=1
                predicates[triple.p]+=1
                objects[triple.o]+=1
        return subjects.most_common(), predicates.most_common(),objects.most_common()

    def verbalisations(self):
        """Get all lexicalisations."""
        verbalisations = []
        for entry in self.entries:
            for lex in entry.lexs:
                verbalisations.append(lex.lex)
        return verbalisations

    @staticmethod
    def categories():
        return ['Airport', 'Artist', 'Astronaut', 'Athlete', 'Building', 'CelestialBody', 'City',
                'ComicsCharacter', 'Company', 'Food', 'MeanOfTransportation', 'Monument',
                'Politician', 'SportsTeam', 'University', 'WrittenWork']

    ### added by Guy Lapalme
    def sample(self,nb):
        """ Get a random sample of nb entries. Entries are NOT copied """
        return random.sample(self.entries,nb)


def select_files(topdir, category='', size=(1, 8)):
    finaldirs = [topdir+'/'+str(item)+'triples' for item in range(size[0], size[1])]
    # print(finaldirs)
    finalfiles = []
    for item in finaldirs:
        finalfiles += [(item, filename) for filename in sorted(listdir(item)) if category in filename and '.xml' in filename]
    return finalfiles

if __name__ == "__main__":
    from datasets import load_dataset

    # you can use any of the following config names as a second argument:
    configs = ["release_v1", "release_v2", "release_v2.1", "release_v2.1_constrained",
                "release_v2_constrained", "release_v3.0_en", "release_v3.0_ru", "webnlg_challenge_2017"]
    splits = ["train","dev","test"]
    dataset = load_dataset("web_nlg", "release_v3.0_en",split="train")
    print(dataset)
    b = Benchmark()
    b.benchmark_from_dataset(dataset)
    print(b.unique_p_mtriples())
