from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or

class Matcher:
    def __init__(self, matchers, new_matcher):
        self._matcher = And(matchers, new_matcher)
    
    def test(self, player):
        return self._matcher.test(player)
        

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
