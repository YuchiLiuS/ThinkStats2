"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz'):
    """Reads the NSFG pregnancy data.

    dct_file: string file name
    dat_file: string file name

    returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    return df

def ValidatePregNum(resp):
    fem_preg = nsfg.ReadFemPreg()
    preg_map = nsfg.MakePregMap(fem_preg)
    
    for index, pregnum in resp.pregnum.iteritems():
        caseid = resp.caseid[index]
        indices = preg_map[caseid]
        if len(indices) != pregnum:
            print (caseid, len(indices), pregnum)
            return False
    return True
    
def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    df = ReadFemResp()
    assert(len(df) == 7643)
    assert(df.pregnum.value_counts()[0] == 2610)
    print(df.pregnum.value_counts().sort_index())
    assert(ValidatePregNum(df))
    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
