#ex 2-18 from FluentPython
import bisect

def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]

if __name__ == '__main__':
    scores = [33, 99, 77, 70, 89, 90, 100]
    print('Scores: ' , ', '.join('%2d' % n for n in scores))
    print('Grades: ', ', '.join(grade(score) for score in scores))