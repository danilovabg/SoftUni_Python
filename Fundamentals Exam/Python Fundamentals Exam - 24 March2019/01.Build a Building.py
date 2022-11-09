budget = float(input())
m = float(input())
n = int(input())
investors_money = []
for investor in range(n):
    investors_money.append(float(input()))
    print(f"Investor {investor+1} gave us {investors_money[investor]:.2f}.")
    if m + sum(investors_money) >= budget:
        print(f'We will manage to build it. Start now! Extra money - {(m + sum(investors_money))-budget:.2f}.')
        break
diff = m + sum(investors_money) - budget
if diff < 0:
    print(f"Project can not start. We need{abs(diff): .2f} more.")