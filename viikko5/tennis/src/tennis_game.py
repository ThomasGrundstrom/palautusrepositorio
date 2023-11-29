class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        score = ""

        if self.player1_score == self.player2_score:
            score = self.get_equal_score()
        
        elif self.player1_score >= 4 or self.player2_score >= 4:
            score = self.get_score_for_over_fourty()

        else:
            for i in range(1, 3):
                if i == 1:
                    score_to_convert = self.player1_score
                else:
                    score = score + "-"
                    score_to_convert = self.player2_score

                score += self.convert_score(score_to_convert)

        return score

    def get_equal_score(self):
        if self.player1_score == 0:
            score = "Love-All"
        elif self.player1_score == 1:
            score = "Fifteen-All"
        elif self.player1_score == 2:
            score = "Thirty-All"
        else:
            score = "Deuce"
        return score
    
    def get_score_for_over_fourty(self):
        result_difference = self.player1_score - self. player2_score

        if result_difference == 1:
            score = "Advantage player1"
        elif result_difference == -1:
            score = "Advantage player2"
        elif result_difference >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score
    
    def convert_score(self, score_to_convert):
        if score_to_convert == 0:
            return "Love"
        elif score_to_convert == 1:
            return "Fifteen"
        elif score_to_convert == 2:
            return "Thirty"
        elif score_to_convert == 3:
            return "Forty"