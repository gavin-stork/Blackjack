import asyncio
import random

def create_deck():
    """Creates and returns a shuffled 52-card deck."""
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [(value, suit) for value in values for suit in suits]
    random.shuffle(deck)
    return deck

def get_card_value(card):
    """Returns the numeric value of a single card."""
    value, suit = card
    match value:
        case 'Jack' | 'Queen' | 'King':
            return 10
        case 'Ace':
            return 11
        case _:
            return int(value)

def deal_card(deck):
    """Removes and returns the top card from the deck."""
    if deck:
        return deck.pop()
    else:
        print("The deck is empty.")
        return None

def display_card(card):
    """Prints a card's value and suit."""
    if card:
        value, suit = card
        print(f"{value} of {suit}")

def check_for_21(hand):
    """Returns True if the hand totals exactly 21."""
    return get_card_sum(hand) == 21

def get_card_sum(hand):
    """
    Returns the best possible total for a hand.
    Chooses the highest valid total under or equal to 21.
    """
    totals = possible_totals(hand)
    valid_totals = [total for total in totals if total <= 21]
    if valid_totals:
        return max(valid_totals)
    else:
        return min(totals)

def possible_totals(hand):
    """Returns all possible totals for a hand, accounting for Aces as 1 or 11."""
    totals = [0]
    for card in hand:
        value = get_card_value(card)
        if card[0] == 'Ace':
            new_totals = []
            for total in totals:
                new_totals.append(total + 1)
                new_totals.append(total + 11)
            totals = new_totals
        else:
            totals = [total + value for total in totals]
    return totals

def format_totals(totals):
    """Formats a list of totals into a readable string for display."""
    valid_totals = [total for total in totals if total <= 21]
    if valid_totals:
        return " or ".join(str(total) for total in valid_totals)
    else:
        return str(min(totals))

async def player_turn(deck, player_hand):
    """
    Handles the player's turn.
    Lets the player hit or stand until they stand or bust.
    """
    while True:
        totals = possible_totals(player_hand)
        print(f"Your total: {format_totals(totals)}\n")
        await asyncio.sleep(1)

        choice = ""
        while choice not in ['h', 's']:
            choice = input("Do you want to hit or stand? (h/s): ").strip().lower()
        print()

        if choice == 'h':
            card = deal_card(deck)
            player_hand.append(card)
            print("You drew: ", end="")
            display_card(card)
            print()
            await asyncio.sleep(1)

            totals = possible_totals(player_hand)
            if all(total > 21 for total in totals):
                print()
                await asyncio.sleep(0.5)
                print(f"Your total is {min(totals)}.")
                await asyncio.sleep(1)
                return "Bust"

        elif choice == 's':
            print(f"You chose to stand at {get_card_sum(player_hand)}\n")
            await asyncio.sleep(1)
            return max(total for total in totals if total <= 21)

async def dealer_turn(deck, dealer_hand):
    """
    Handles the dealer's automated turn.
    Dealer hits until reaching 17 or more, or busts.
    """
    await asyncio.sleep(1)
    print(f"Dealer flips {dealer_hand[1][0]} of {dealer_hand[1][1]}\n")
    await asyncio.sleep(1)
    print("Dealer's hand:")
    for card in dealer_hand:
        print(f"  - {card[0]} of {card[1]}")
    await asyncio.sleep(1)

    while True:
        totals = possible_totals(dealer_hand)
        print(f"\nDealer's total: {format_totals(totals)}\n")
        await asyncio.sleep(1)

        if 17 in totals:
            stand_total = 17
            print(f"Dealer stands at {stand_total}")
            await asyncio.sleep(1)
            return stand_total

        if all(total < 17 for total in totals):
            card = deal_card(deck)
            dealer_hand.append(card)
            print("Dealer drew: ", end="")
            display_card(card)
            await asyncio.sleep(1)

            if get_card_sum(dealer_hand) > 21:
                print(f"Dealer total: {get_card_sum(dealer_hand)}\n")
                await asyncio.sleep(1)
                return "Bust"
        else:
            stand_total = max(total for total in totals if total <= 21)
            print(f"Dealer stands at {stand_total}.\n")
            await asyncio.sleep(1)
            return stand_total

async def blackjack_game():
    """Runs a full game of Blackjack between a player and the dealer."""
    print("=" * 40)
    print("         Welcome to Blackjack!")
    print("=" * 40 + "\n")
    await asyncio.sleep(1)

    print("Goal: Get as close to 21 as possible without going over.")
    print("Rules:")
    print(" - Number cards are worth their value (2-10).")
    print(" - Face cards (Jack, Queen, King) are worth 10 points.")
    print(" - Aces can be worth 1 or 11 points, whichever helps you more.")
    print(" - If you are dealt 21, you win immediately!")
    print(" - If you go over 21, you bust and lose.")
    print(" - Dealer must stand on 17 or higher.")
    print(" - If you and dealer have the same total, it's a tie (push).\n")
    await asyncio.sleep(3)

    deck = create_deck()

    dealer_hand = [deck.pop()]
    player_hand = [deck.pop()]
    dealer_hand.append(deck.pop())
    player_hand.append(deck.pop())

    print(f"Dealer visible card:\n  - {dealer_hand[0][0]} of {dealer_hand[0][1]}\n")
    await asyncio.sleep(1)

    print("Your hand:")
    for card in player_hand:
        print(f"  - {card[0]} of {card[1]}")
    print()
    await asyncio.sleep(1)

    if check_for_21(player_hand):
        print("You win! You got 21!")
        return
    if check_for_21(dealer_hand):
        print(f"Dealer flips {dealer_hand[1][0]} of {dealer_hand[1][1]}")
        print("You lose! Dealer got 21!")
        return

    player_result = await player_turn(deck, player_hand)

    if player_result == "Bust":
        print("=" * 40)
        print("              Final Result")
        print("=" * 40 + "\n")
        print("You bust! Dealer wins!")
        return

    dealer_result = await dealer_turn(deck, dealer_hand)

    print("=" * 40)
    print("              Final Result")
    print("=" * 40 + "\n")
    await asyncio.sleep(1)
    print(f"Your final total: {player_result}")
    print(f"Dealer final total: {dealer_result}\n")
    await asyncio.sleep(1)

    if player_result == "Bust":
        print("You bust! Dealer wins!")
    elif dealer_result == "Bust":
        print("Dealer busts! You win!")
    elif player_result > dealer_result:
        print("You win!")
    elif player_result < dealer_result:
        print("You lose!")
    else:
        print("It's a push (tie)!")

if __name__ == "__main__":
    asyncio.run(blackjack_game())