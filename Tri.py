def tri_couleur(inst:list):
  l=[[],[],[],[],[]]
  for ele in inst:
    if ele>100:
      c=cartes_sanctuaire[ele-1][0]
    else:
      c=cartes_region[ele-1][0]
    if c=='B':
      l[0].append(ele)
    elif c=='R':
      l[1].append(ele)
    elif c=='J' :
      l[2].append(ele)
    elif c=='V':
      l[3].append(ele)
    else:
      l[4].append(ele)
  return l

def tri_ressource_n_ind(inst:list):
  ressources={"I":[], "N":[],"P":[],"CHI":[],"CHA":[]}
  for carte in inst:
    if carte<100:
      ele= cartes_region[carte-1]
    elif carte<100:
      ele=cartes_sanctuaire[carte-1]
    if ele[1]=='N':
      ressources["N"].append(carte)
    if ele[2]=='I':
      ressources["I"].append(carte)
    if ele[3][0]>0:
      ressources

