import operator


def count(article):
	words = article.split()
	count = len(words)
	article_dic = {}
	for word in words:
		if word in article_dic:
			article_dic[word] += 1
		else:
			article_dic[word] = 1
	sorted_article = sorted(article_dic.items(), key=operator.itemgetter(1), reverse=True)
	return sorted_article , count
