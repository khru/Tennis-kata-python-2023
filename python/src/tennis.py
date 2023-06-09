# -*- coding: utf-8 -*-


class TennisGame1:
    INITIAL_POINTS = 0
    POINT = 1
    MINIMUM_BREAK_POINT_LIMIT = 4
    game_score = {
        0: "Love",
        1: "Fifteen",
        2: "Thirty",
        3: "Forty",
    }
    
    DUCE_SCORE = {
        0: "Love-All",
        1: "Fifteen-All",
        2: "Thirty-All",
    }

    def __init__(self, player_1_name, player_2_name):
        self.player1_name = player_1_name
        self.player2_name = player_2_name
        self.p1_points = self.INITIAL_POINTS
        self.p2_points = self.INITIAL_POINTS

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1_points += self.POINT
        else:
            self.p2_points += self.POINT

    def score(self):
        if self.is_deuce():
            return self.deuce_cases()
        elif self.is_break_point():
            return self.break_point()
        else:
            return self.add_score()

    def add_score(self):
        return f"{self.game_score[self.p1_points]}-{self.game_score[self.p2_points]}"

    def break_point(self):
        minus_result = self.p1_points - self.p2_points
        if minus_result == 1:
            return "Advantage " + self.player1_name
        elif minus_result == -1:
            return "Advantage " + self.player2_name
        elif minus_result >= 2:
            return "Win for " + self.player1_name
        return "Win for " + self.player2_name

    def deuce_cases(self):
        return self.DUCE_SCORE.get(self.p1_points, "Deuce")

    def is_deuce(self):
        return self.p1_points == self.p2_points

    def is_break_point(self):
        return self.p1_points >= self.MINIMUM_BREAK_POINT_LIMIT or self.p2_points >= self.MINIMUM_BREAK_POINT_LIMIT


class TennisGame2:
    def __init__(self, player_1_name, player_2_name):
        self.player_1_name = player_1_name
        self.player_2_name = player_2_name
        self.p1_points = 0
        self.p2_points = 0

    def won_point(self, player_name):
        if player_name == self.player_1_name:
            self.p1_score()
        else:
            self.p2_score()

    def score(self):
        result = ""
        if self.p1_points == self.p2_points and self.p1_points < 3:
            if self.p1_points == 0:
                result = "Love"
            if self.p1_points == 1:
                result = "Fifteen"
            if self.p1_points == 2:
                result = "Thirty"
            result += "-All"
        if self.p1_points == self.p2_points and self.p1_points > 2:
            result = "Deuce"

        P1res = ""
        P2res = ""
        if self.p1_points > 0 and self.p2_points == 0:
            if self.p1_points == 1:
                P1res = "Fifteen"
            if self.p1_points == 2:
                P1res = "Thirty"
            if self.p1_points == 3:
                P1res = "Forty"

            P2res = "Love"
            result = P1res + "-" + P2res
        if self.p2_points > 0 and self.p1_points == 0:
            if self.p2_points == 1:
                P2res = "Fifteen"
            if self.p2_points == 2:
                P2res = "Thirty"
            if self.p2_points == 3:
                P2res = "Forty"

            P1res = "Love"
            result = P1res + "-" + P2res

        if self.p2_points < self.p1_points < 4:
            if self.p1_points == 2:
                P1res = "Thirty"
            if self.p1_points == 3:
                P1res = "Forty"
            if self.p2_points == 1:
                P2res = "Fifteen"
            if self.p2_points == 2:
                P2res = "Thirty"
            result = P1res + "-" + P2res
        if self.p1_points < self.p2_points < 4:
            if self.p2_points == 2:
                P2res = "Thirty"
            if self.p2_points == 3:
                P2res = "Forty"
            if self.p1_points == 1:
                P1res = "Fifteen"
            if self.p1_points == 2:
                P1res = "Thirty"
            result = P1res + "-" + P2res

        if self.p1_points > self.p2_points >= 3:
            result = "Advantage " + self.player_1_name

        if self.p2_points > self.p1_points >= 3:
            result = "Advantage " + self.player_2_name

        if self.p1_points >= 4 and self.p2_points >= 0 and (self.p1_points - self.p2_points) >= 2:
            result = "Win for " + self.player_1_name
        if self.p2_points >= 4 and self.p1_points >= 0 and (self.p2_points - self.p1_points) >= 2:
            result = "Win for " + self.player_2_name
        return result

    def set_p1_score(self, number):
        for i in range(number):
            self.p1_score()

    def set_p2_score(self, number):
        for i in range(number):
            self.p2_score()

    def p1_score(self):
        self.p1_points += 1

    def p2_score(self):
        self.p2_points += 1


class TennisGame3:
    def __init__(self, player1_name, player2_name):
        self.p1N = player1_name
        self.p2N = player2_name
        self.p1 = 0
        self.p2 = 0

    def won_point(self, n):
        if n == self.p1N:
            self.p1 += 1
        else:
            self.p2 += 1

    def score(self):
        if (self.p1 < 4 and self.p2 < 4) and (self.p1 + self.p2 < 6):
            p = ["Love", "Fifteen", "Thirty", "Forty"]
            s = p[self.p1]
            return s + "-All" if (self.p1 == self.p2) else s + "-" + p[self.p2]
        else:
            if self.p1 == self.p2:
                return "Deuce"
            s = self.p1N if self.p1 > self.p2 else self.p2N
            return "Advantage " + s if ((self.p1 - self.p2) * (self.p1 - self.p2) == 1) else "Win for " + s
