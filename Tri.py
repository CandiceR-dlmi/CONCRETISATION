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
