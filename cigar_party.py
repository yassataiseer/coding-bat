def cigar_party(cigars, is_weekend):
  if is_weekend ==False and cigars>=40 and cigars<=60:
    return True
  elif is_weekend == True and cigars>=40:
    return True
  else:
    return False
