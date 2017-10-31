chem1 = {'C':6,'H':12, 'O':6}
chemorder = ('C','H','O')


SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

def chemprinter(chemd, chemord):
  chemform = []
  for chem in chemord:
    if chemd[chem] > 1:
      chemform.append((chem+str(chemd[chem])).translate(SUB))
    else:
      chemform.append(chem)
  print(''.join(chemform))
  

chemprinter(chem1, chemorder)


def ion_bond_1_to_1(m,nm):
  m_oxidation = m['oxidation']
  nm_oxidation = nm['oxidation']
  print('Metal loses', abs(m_oxidation))
  print('Non metal/Metalloid gains', abs(nm_oxidation))
  
ion_bond_1_to_1({'oxidation':1},{'oxidation':1})
ion_bond_1_to_1({'oxidation':2},{'oxidation':2})

