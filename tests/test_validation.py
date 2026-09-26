"""Check that common data and provenance corruptions are rejected."""
import copy
import csv
from pathlib import Path
import sys
import unittest
import yaml
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from validate import validate

class CorruptionChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with (ROOT/'data/complex_frontier.csv').open() as stream:
            cls.rows=list(csv.DictReader(stream))
        cls.sources=yaml.safe_load((ROOT/'data/sources.yaml').read_text())
        cls.derivations=yaml.safe_load((ROOT/'data/derivations.yaml').read_text())
        cls.tables=yaml.safe_load((ROOT/'data/source_tables.yaml').read_text())

    def run_case(self,change):
        rows,sources,derivations,tables=copy.deepcopy((self.rows,self.sources,self.derivations,self.tables))
        change(rows,sources,derivations,tables)
        self.assertTrue(validate(rows,sources,derivations,tables))

    def test_duplicate_cell(self):
        self.run_case(lambda r,s,d,t:r.append(r[0]))

    def test_false_exact(self):
        self.run_case(lambda r,s,d,t:r[0].update(exact='false'))

    def test_missing_source(self):
        self.run_case(lambda r,s,d,t:r[0].update(lower_source_ids='missing-authority'))

    def test_bounds_reversed(self):
        self.run_case(lambda r,s,d,t:r[0].update(lower='3',upper='2'))

    def test_noncanonical_orientation(self):
        self.run_case(lambda r,s,d,t:r[1].update(r='2',s='1'))

    def test_cycle(self):
        def change(r,s,d,t):
            node=next(x for x in d['derivations'] if x['inputs'])
            node['inputs']=[node['id']]
        self.run_case(change)

    def test_wrong_bp_witness(self):
        def change(r,s,d,t):
            node=next(x for x in d['derivations'] if x['parameters'].get('theorem')=='bp2')
            node['parameters']['value']+=1
        self.run_case(change)

    def test_wrong_sum(self):
        def change(r,s,d,t):
            node=next(x for x in d['derivations'] if x['operation']=='direct sum')
            node['result']['upper']+=1
        self.run_case(change)

if __name__=='__main__':unittest.main()
