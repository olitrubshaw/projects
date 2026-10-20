namespace Blackjack;

public sealed class Hand
{
    private readonly List<Card> _cards = new();

    public Hand(decimal bet = 0) => Bet = bet;

    public IReadOnlyList<Card> Cards => _cards;
    public decimal Bet { get; set; }
    public bool DoubledDown { get; set; }

    public void Add(Card card) => _cards.Add(card);

    /// <summary>Best total not exceeding 21 if possible. Aces count as 11 until that would bust.</summary>
    public int Value => Evaluate().Total;

    /// <summary>True if an ace is currently counting as 11.</summary>
    public bool IsSoft => Evaluate().Soft;

    public bool IsBust => Value > 21;

    /// <summary>A natural: exactly two cards totalling 21.</summary>
    public bool IsBlackjack => _cards.Count == 2 && Value == 21;

    private (int Total, bool Soft) Evaluate()
    {
        int total = 0;
        bool hasAce = false;
        foreach (Card c in _cards)
        {
            total += c.Rank == Rank.Ace ? 1 : c.Value; // count every ace as 1 first
            hasAce |= c.Rank == Rank.Ace;
        }

        // Promote one ace to 11 if it doesn't bust the hand. Promoting two would always bust.
        if (hasAce && total + 10 <= 21)
            return (total + 10, true);
        return (total, false);
    }

    public override string ToString() => string.Join(" ", _cards);
}
