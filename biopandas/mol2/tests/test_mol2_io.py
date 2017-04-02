# BioPandas
# Author: Sebastian Raschka <mail@sebastianraschka.com>
# License: BSD 3 clause
# Project Website: http://rasbt.github.io/biopandas/
# Code Repository: https://github.com/rasbt/biopandas

import os
from biopandas.mol2.mol2_io import split_multimol2

this_dir = os.path.dirname(os.path.realpath(__file__))


def test_split_multimol2():
    all_mol2 = []
    for i in split_multimol2(os.path.join(this_dir,
                                          'data', '40_mol2_files.mol2')):
        all_mol2.append(i[0])
    assert(all_mol2[1] == 'ZINC04084113')
    assert(len(all_mol2) == 40)


def test_split_multimol2_gz():
    all_mol2 = []
    for i in split_multimol2(os.path.join(this_dir,
                                          'data', '40_mol2_files.mol2.gz')):
        all_mol2.append(i[0])
    assert(all_mol2[1].decode() == 'ZINC04084113')
    assert(len(all_mol2) == 40)
