import operator


def gi(para):
	alfaaz = para.split()
	num_lfz = len(alfaaz)
	para_dict = {}
	for lfz in alfaaz:
		if lfz in para_dict:
			para_dict[lfz] += 1
		else:
			para_dict[lfz] = 1
	sorted_para = sorted(para_dict.items(), key=operator.itemgetter(1), reverse=True)
	return num_lfz, sorted_para
