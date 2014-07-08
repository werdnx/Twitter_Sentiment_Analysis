import sys
import json


def add_score(dict, term):
    s = dict.get(term, 0)
    return s


def processString(s):
    return s.replace(".", " ").replace(",", " ").replace(":", " ").replace("!", " ").replace("?", " ").replace(")",
                                                                                                               " ").replace(
        "(", " ").replace(";", " ")


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {}  # initialize an empty dictionary
    for line in sent_file:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    terms_map = {}
    for tweet_line in tweet_file:
        json_item = json.loads(tweet_line)
        sentence = json_item.get("text", None)
        if sentence is not None:
            terms = sentence.replace("\n", " ").split(" ")
            list_terms = []
            sum = 0
            for term in terms:
                strip_term = processString(term).strip().lower()
                if (strip_term != ""):
                    sum += add_score(scores, strip_term)
                    score_item = scores.get(strip_term, None)
                    if score_item is None and strip_term != "" and strip_term != "\n":
                        list_terms.append(strip_term)

            for not_apear_term in list_terms:
                term_score = terms_map.get(not_apear_term, 0)
                terms_map[not_apear_term] = float(float(term_score) + float(sum) / float(len(terms)))

    for key in terms_map.keys():
        sys.stdout.write("%s %s\n" % (key.encode('utf-8'), terms_map[key]))


if __name__ == '__main__':
    main()
