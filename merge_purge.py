import glob
files = glob.glob( 'Logs/*.log' )

with open( 'Output.txt', 'w' ) as result:
    for file_ in files:
        for line in open( file_, 'r' ):
            if not (line.startswith('#')):
                result.write( line ) 
