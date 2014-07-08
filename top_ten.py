import sys
import json
import operator


def getHashTags(entities):
    return entities.get("hashtags", None)


def main():
    tweet_file = open(sys.argv[1])

    tag_map = {}
    for tweet_line in tweet_file:
        json_item = json.loads(tweet_line)
        entities = json_item.get("entities", None)
        if entities is not None:
            tags = getHashTags(entities)
            if tags is not None and len(tags) > 0:
                for tag in tags:
                    tag_name = tag.get("text").encode('utf-8')
                    count = tag_map.get(tag_name, 0)
                    tag_map[tag_name] = count + 1

    sorted_tags = sorted(tag_map.iteritems(), key=operator.itemgetter(1),reverse=True)

    for i in range(1, 11):
        sys.stdout.write("%s %s\n" % (sorted_tags[i][0].encode('utf-8'), sorted_tags[i][1]))


if __name__ == '__main__':
    main()
