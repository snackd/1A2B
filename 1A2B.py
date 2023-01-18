from keyboard_tracer import KeyboardTracer
from random import randint


class OneATwoB:
    def generate_ans(self):
        ans_set = set()
        while len(ans_set) < 4:
            ans_set.add(randint(0, 9))

        ans_list = list(ans_set)

        return ans_list

    def check_input(self, guess_ans):
        while not guess_ans.isnumeric() or len(guess_ans) != 4 or len(set(guess_ans)) != 4:
            guess_ans = input("請重新輸入你的答案(4位不重複正整數):")

        guess_ans = list(map(int, guess_ans))

        return guess_ans

    def check_ans(self, guess_ans, ans_list):

        guess_a = 0
        guess_b = 0

        if guess_ans != ans_list:
            for i in range(4):
                if guess_ans[i] == ans_list[i]:
                    guess_a += 1
                if guess_ans[i] in ans_list and guess_ans[i] != ans_list[i]:
                    guess_b += 1
        else:
            guess_a = 4

        return guess_a, guess_b

    def game(self):
        count = 1
        ans_list = self.generate_ans()
        # print("Ans", ans_list)

        while True:
            if count > 4:
                print("Game Over")
                print("已猜了四次，未猜得4A")
                break

            guess_ans = input("請輸入你的答案(4位不重複正整數):")

            guess_ans = self.check_input(guess_ans)

            guess_a, guess_b = self.check_ans(guess_ans, ans_list)

            print("第", count, "次猜數, 猜數為", guess_ans,
                  ",", guess_a, "A", guess_b, "B")

            if guess_a == 4:
                print("恭喜答對，答案為:", ans_list)
                break
            count += 1

        print("-"*10)

    def main(self):
        k = KeyboardTracer()
        k.main()

        print("-"*10)
        print("1A2B，產生4位數不重複的密碼，請在四次之內猜中正確答案：")
        print()
        print("如果猜對一個數字且位置相同，則得1A")
        print("如果猜對一個數字，但是位置不同，則得1B")
        print("目標是猜數得4A")
        print()
        round_count = 1

        while k.game_flag:
            print()
            print("-"*10)
            print("第", round_count, "輪遊戲")
            print("按下 ESC 鍵後，不再進行下輪遊戲")

            self.game()

            round_count += 1

        print("結束遊戲")


if __name__ == "__main__":
    g = OneATwoB()
    g.main()
