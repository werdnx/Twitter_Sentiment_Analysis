import sys
import json

def processString(s):
    return s.replace("."," ").replace(","," ").replace(":"," ").replace("!"," ").replace("?"," ").replace(")"," ").replace("("," ").replace(";"," ")

def main():
    tweet_file = open(sys.argv[1])

    count_map = {}
    for tweet_line in tweet_file:
        json_item = json.loads(tweet_line)
        sentence = json_item.get("text",None)
        if sentence is not None:
            terms = sentence.replace("\n"," ").split(" ")
            sum = 0
            for term in terms:
                s_term = processString(term).strip().lower()
                if(s_term != ""):
                    count = count_map.get(s_term,0)
                    count_map[s_term] = count + 1

    for key in count_map.keys():
        sys.stdout.write("%s %s\n" % (key.encode('utf-8'),count_map[key]))




if __name__ == '__main__':
    main()
