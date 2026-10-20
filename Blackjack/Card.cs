namespace Blackjack;

public enum Suit { Spades, Hearts, Diamonds, Clubs }

public enum Rank
{
    Two = 2, Three, Four, Five, Six, Seven, Eight, Nine, Ten,
    Jack, Queen, King, Ace
}

public readonly record struct Card(Rank Rank, Suit Suit)
{
    /// <summary>Blackjack value of the card. Aces are 11 here; <see cref="Hand"/> lowers them as needed.</summary>
    public int Value => Rank switch
    {
        Rank.Ace => 11,
        Rank.Jack or Rank.Queen or Rank.King => 10,
        _ => (int)Rank
    };

    public override string ToString()
    {
        string rank = Rank switch
        {
            Rank.Ace => "A",
            Rank.King => "K",
            Rank.Queen => "Q",
            Rank.Jack => "J",
            _ => ((int)Rank).ToString()
        };
        string suit = Suit switch
        {
            Suit.Spades => "♠",
            Suit.Hearts => "♥",
            Suit.Diamonds => "♦",
            _ => "♣"
        };
        return rank + suit;
    }
}
