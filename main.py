# coding=utf-8
# Solution for coding challenge
import sys
import os


class teamScore:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def appendScore(self, extraScore):
        self.score = self.score + extraScore.score


# returns two teamScore objects in an array
def split_scores(inputline):
    scores = inputline.split(',')

    score1 = scores[0].strip().rsplit(' ', 1)
    score2 = scores[1].strip().rsplit(' ', 1)
    p1 = int(score1[1])
    p2 = int(score2[1])
    if (p1 == p2):
        return [teamScore(score1[0], 1), teamScore(score2[0], 1)]
    elif (p1 > p2):
        return [teamScore(score1[0], 3), teamScore(score2[0], 0)]
    else:
        return [teamScore(score1[0], 0), teamScore(score2[0], 3)]


# turn a dictionary of teamScores into a list of strings to write.
def create_output(teamScores):
    results = list(teamScores.values())
    results.sort(key=lambda x: (-int(x.score),x.name), reverse=False)
    teamStrings = map(lambda n: "{0}, {1} {2}\n".format(n.name, n.score, 'pt' if n.score == 1 else 'pts'), results)
    return teamStrings


def calc_scores():
    # arguments
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]
    print sys.argv

    # read inputs from file into a dictionary of scores
    teams = {}
    path = os.getcwd() + '\\' + inputFile
    with open(path) as f:
        lines = f.readlines()
        for l in lines:  # type: str
            if (len(l) > 0):  # ignore empty lines
                # loop over the lines and split them into individual team scores
                for n in split_scores(l):

                    if (n.name in teams):
                        teams[n.name].appendScore(n)
                    else:
                        teams[n.name] = n

    # process output results
    teamStrings = create_output(teams)

    # write to output file
    path = os.getcwd() + '\\' + outputFile
    with open(path, 'w') as fileoutput:
        fileoutput.writelines(teamStrings)


if __name__ == '__main__':
    calc_scores()
