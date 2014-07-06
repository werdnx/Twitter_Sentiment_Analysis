import sys
import json


def hw():
    print 'Hello, world!'


def lines(fp):
    print str(len(fp.readlines()))

def add_score(dict, term):
    s = dict.get(term,0)
    return s

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {}  # initialize an empty dictionary
    for line in sent_file:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    for tweet_line in tweet_file:
        json_item = json.loads(tweet_line)
        sentence = json_item.get("text",None)
        if sentence is not None:
            terms = sentence.split(" ")
            sum = 0
            for term in terms:
                sum += add_score(scores,term)

            sys.stdout.write("%s\n" % sum)
        else:
            sys.stdout.write("0\n")


if __name__ == '__main__':
    main()
