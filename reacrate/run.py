import os
import sys
import argparse

import reacnetrate

def main_cli(args=None):
    parser = argparse.ArgumentParser(
        prog = "reacrate",
        description="a rate calculate program for reacnetgenerattor")
    
    parser.add_argument('-s','--species',help="species for the trajtory",dest='species',default='')
    parser.add_argument('-f','--formula',help="the reaction in the species",dest='formula',default='')
    #parser.add_argument('-o','--output',help="output the species",dest='output',default='')
    args = parser.parse_args()
    #print(args.nclusts)
    if args.species == '' or args.formula=='':
        parser.print_help()
        print("No species and fromula file")
        sys.exit(1)
    return args
def main():
    options = main_cli()
    species=options.species
    formula=options.formula
    reacnetrate.get_rate(species,formula)

if __name__ == "__main__":
    main()
