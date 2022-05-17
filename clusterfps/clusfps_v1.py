import os
import sys
import argparse

from clusterfps import cluster

#from cluster import *
#import cluster
#from yaml import parse

def main_cli(args=None):
    parser = argparse.ArgumentParser(
        prog = "clufps",
        description="a program for cluster the fps")
    
    parser.add_argument('-i','--input',dest='input',
                            help='intput sdf file', 
                            default='')
    parser.add_argument("--fp",dest='fp',
                            help='fingerprint type: tp,mc,mo (Topological Fingerprints, MACCS Keys, Morgan Fingerprints), default is mc', 
                            default='mc')
    parser.add_argument('--radius',dest='radius',
                            help=' the radius of the Morgan fingerprint, default is 2',
                            type=int, 
                            default=2)   
    parser.add_argument('--algorithm',dest='algorithm',
                            help='cluster algorithm :b,m (Butina, Murtagh), default is b', 
                            default='b')
    parser.add_argument('--cutoff',dest='cutoff',
                            help='distThresh(0-1),elements within this range of each other are considered to be neighbors, needed for Butina cluster algorithm, default is 0.5', 
                            type=float, 
                            default=0.5)
    parser.add_argument('--nclusts',dest='nclusts',
                            help='number of clusters, needed for Murtagh cluster algorithm, default is 1',
                            type=int, 
                            default=1)
    parser.add_argument('--murtype',dest='Murtype',
                            help='Method for Murtagh:Wards, SLINK, CLINK, UPGMA,needed when Murtagh is set as algorithm, default is Wards', 
                            default='Wards')
    parser.add_argument('-o','--output',dest='output',
                            help='output sdf file', 
                            default='')
    args = parser.parse_args()
    #print(args.nclusts)
    if args.input == '' or args.output=='':
        parser.print_help()
        print("No input and output")
        sys.exit(1)
    return args
    #print(args.nclusts)
def main():
    options = main_cli()
    fpOpdict = {'tp':'Topological Fingerprints','mc':'MACCS Keys','mo':'Morgan Fingerprints'}
    algOpdict = {'b':'Butina','m':'Murtagh'}
    options.algorithm = algOpdict[options.algorithm]
    print("fingerprint type: %s" % fpOpdict[options.fp])
    if options.fp == 'mo':
        print("radius: %s" % str(options.radius))
    print("cluster algorithm: %s" % options.algorithm)
    if options.algorithm == "Murtagh":
        print("Murtagh method: %s" % options.Murtype)
        print("Murtagh cluster number set: %s" % options.nclusts)
    elif options.algorithm == "Butina":
        print("cutoff(distThresh) : %s" % options.cutoff)
    print('sdf reading...')
    sdfparse = cluster.ChemParse(options.input)
    sdfparse.sdf_reader()
    print('fingerprint calculating...')
    sdfparse.get_fps(options.fp, options.radius)
    print('clustering...')
    fpCluster = cluster.Fingerprint_Cluster(sdfparse.fps)
    fpCluster.distance_matrix()
    fpCluster.cluster_dict(options.algorithm, options.cutoff, options.Murtype, options.nclusts)
    print ('done, output to %s' % options.output)
    sdfparse.clusterOutput(options.output, fpCluster.cdict)
    for c in fpCluster.clustdict:
        print("cluster%s: %s" % (str(c),str(fpCluster.clustdict[c])))

if __name__ == "__main__":
    main()

