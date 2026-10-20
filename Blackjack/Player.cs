namespace Blackjack;

public sealed class Player
{
    public Player(string name, decimal bankroll)
    {
        Name = name;
        Bankroll = bankroll;
    }

    public string Name { get; }
    public decimal Bankroll { get; set; }

    /// <summary>A list rather than a single hand so splitting can be added later.</summary>
    public List<Hand> Hands { get; } = new();
}
