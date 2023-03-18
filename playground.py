from nreinas.checar_ataques import checar_ataques
from nreinas.expand import Expand

conf = [0,0,0,0]

os = Expand.expand(conf)

#os = [checar_ataques(conf) for conf in os]

os.sort(key=checar_ataques)

print(os)

