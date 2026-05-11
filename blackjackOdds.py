import random
import matplotlib.pyplot as plt


def game():
    player_total = random.randint(1, 10) + random.randint(1, 10)
    dealer_total = random.randint(1, 10) + random.randint(1, 10)

    while player_total < 17:
        player_total += random.randint(1, 10)

    if player_total > 21:
        return "loss"

    while dealer_total < 17:
        dealer_total += random.randint(1, 10)

    if dealer_total > 21:
        return "win"

    if player_total > dealer_total:
        return "win"
    elif player_total == dealer_total:
        return "push"
    else:
        return "loss"


def main():
    TRIALS = 1_000_000
    STEPS = 500
    wins = 0
    losses = 0
    pushes = 0
    y = []

    for trials in range(1, TRIALS + 1):
        curGame = game()
        if curGame == "win":
            wins += 1
        elif curGame == "loss":
            losses += 1
        else:
            pushes += 1

        if trials % STEPS == 0:
            y.append(wins / trials)

    ev = (wins - losses) / TRIALS
    winChance = wins / TRIALS * 100
    lossChance = losses / TRIALS * 100
    pushChance = pushes / TRIALS * 100

    plt.figure(figsize=(10, 6))

    x = range(1, TRIALS + 1, STEPS)

    plt.plot(x, y)

    plt.axhline(ev, linestyle="--", color="red")

    plt.xlabel("Trials Ran")
    plt.ylabel("Estimated Probability over Trials")
    plt.title("Monte Carlo Convergence Test of Blackjack")

    plt.grid(True)
    plt.show()

    print("Metrics:\n")
    print(f"EV: {ev}")
    print(f"Probability of Winning: {winChance}%")
    print(f"Probability of Losing: {lossChance}%")
    print(f"Probability of Pushes: {pushChance}%")


if __name__ == "__main__":
    main()
