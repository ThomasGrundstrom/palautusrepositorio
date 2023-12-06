from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or

class Matcher:
    def __init__(self, matchers, new_matcher):
        self._matcher = And(matchers, new_matcher)
    
    def test(self, player):
        return self._matcher.test(player)

class OrMatcher:
    def __init__(self, choices):
        self._choices = choices
    
    def test(self, player):
        for i in range(len(self._choices)-1):
            if Or(self._choices[i], self._choices[i+1]).test(player):
                return True
        return False
        

class QueryBuilder:
    def __init__(self, matcher = All()):
        self._matcher = matcher

    def build(self):
        return self._matcher
    
    def playsIn(self, team):
        return QueryBuilder(Matcher(self._matcher, PlaysIn(team)))
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(Matcher(self._matcher, HasAtLeast(value, attr)))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(Matcher(self._matcher, HasFewerThan(value, attr)))

    def oneOf(self, *choices):
        return QueryBuilder(OrMatcher(choices))