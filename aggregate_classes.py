taxonomia_ataque_dict = {
    'BENIGN'                    : 'BENIGN',
    'Port Scan'                 : 'Port Scan',
    'Brute Force: FTP-Patator'  : 'Brute Force',
    'Brute Force: SSH-Patator'  : 'Brute Force',
    'Web Attack: Brute Force'   : 'Web-Attack' ,
    'Web Attack: XSS'           : 'Web-Attack',
    'Web Attack: Sql Injection' : 'Web-Attack',
    'DoS: Hulk'                 : '(D)DOS',
    'DDoS'                      : '(D)DOS',
    'DoS: GoldenEye'            : '(D)DOS',
    'DoS: Slowloris'            : '(D)DOS',
    'DoS: Slowhttptest'         : '(D)DOS',
    'Botnet'                    : 'Botnet',
    'Infiltration'              : 'Unkown',
    'Heartbleed'                : 'Unkown', 
    } 

high_level_class = lambda ataque_especifico : taxonomia_ataque_dict[ataque_especifico]
