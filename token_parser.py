def search(data,tokens):
  def innersearch(data,token):
    data_l = list(data)
    for loc, item in enumerate(data_l):
      if item == token:
        yield loc
  dd = {}
  for i in tokens:
    dd[i] = list(innersearch(data,i))
  return(dd)

def find_1_layer_parenthesis(data_ls):
  lines = data_ls.splitlines()
  pset_inners = {}
  for line_n,data in enumerate(lines):
    parenthesis = search(data,['(',')'])
    parenthesis_sets = []
    for ind, p_l in enumerate(parenthesis['(']):
      p_set = (p_l, parenthesis[')'][ind])
      parenthesis_sets.append(p_set)
    for ps in parenthesis_sets:
      pset_inners[(ps[0]-1,ps[1]-1,line_n)] = data[ps[0]+1:ps[1]]
    
  return pset_inners
  
  
print(find_1_layer_parenthesis('print(x+4)\nsets(x*4))'))
