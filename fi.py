#!/bin/env python 
import requests 
from tqdm import tqdm 
from optparse import OptionParser 
parse = OptionParser("""
                                            
         ,----,                             
       .'   .`|                     ,--,    
    .'   .'   ;                   ,--.'|    
  ,---, '    .' ,---.             |  | :    
  |   :     ./ '   ,'\            :  : '    
  ;   | .'  / /   /   |  ,--.--.  |  ' |    
  `---' /  ; .   ; ,. : /       \ '  | |    
    /  ;  /  '   | |: :.--.  .-. ||  | :    
   ;  /  /--,'   | .; : \__\/: . .'  : |__  
  /  /  / .`||   :    | ," .--.; ||  | '.'| 
./__;       : \   \  / /  /  ,.  |;  :    ; 
|   :     .'   `----' ;  :   .'   \  ,   /  
;   |  .'             |  ,     .-./---`-'   
`---'                  `--`---'             
                                            
  ---------------------------------------------- 
                  Version 1.0.0
       "----------------------------------"
           "========>Z.O.A.L<========"
               "===>ZoalKtoom<===="
                 "---------------"
               python fi.py -h for help
 -----------------------------------------------
""")
parse.add_option("-u","--url",dest="url",type="string",help="url please")
(options,args) = parse.parse_args()
if options.url == None:
     print(parse.usage)
     exit(0)
else:
     url = str(options.url)
     req = requests.get(url)
     fileName = url.split("/")[-1]
     file = open(fileName, 'wb')
     for chunk in req.iter_content(100000):
         file.write(chunk)
     file.close()
     print("Download Is Done")

