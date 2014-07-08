import sys
import json

def add_score(dict, term):
    s = dict.get(term,0)
    return s

def processString(s):
    return s.replace("."," ").replace(","," ").replace(":"," ").replace("!"," ").replace("?"," ").replace(")"," ").replace("("," ").replace(";"," ")

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
            terms = sentence.replace("\n"," ").split(" ")
            sum = 0
            for term in terms:
                s_term = processString(term).strip().lower()
                if(s_term != ""):
                    sum += add_score(scores,s_term)

            sys.stdout.write("%s\n" % sum)
        else:
            sys.stdout.write("0\n")


if __name__ == '__main__':
    main()
