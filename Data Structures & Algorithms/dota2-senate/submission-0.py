class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)

        r_count = senate.count("R")
        d_count = senate.count("D")

        ban_r = 0
        ban_d = 0

        i = 0

        while r_count > 0 and d_count > 0:
            senator = senate[i]

            if senator == "R":
                if ban_r > 0:
                    senate[i] = "X"
                    ban_r -= 1
                    r_count -= 1
                else:
                    ban_d += 1

            elif senator == "D":
                if ban_d > 0:
                    senate[i] = "X"
                    ban_d -= 1
                    d_count -= 1
                else:
                    ban_r += 1

            i = (i + 1) % len(senate)

        return "Radiant" if r_count > 0 else "Dire"