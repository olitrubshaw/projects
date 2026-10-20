using System.Globalization;

namespace Blackjack;

/// <summary>Console blackjack: one player against the dealer.</summary>
public sealed class Game
{
    private readonly GameRules _rules;
    private readonly TextReader _in;
    private readonly TextWriter _out;
    private readonly Shoe _shoe;
    private readonly Player _player;

    private int _rounds, _wins, _losses, _pushes, _blackjacks;

    public Game(GameRules rules, TextReader input, TextWriter output, Random? rng = null)
    {
        _rules = rules;
        _in = input;
        _out = output;
        _shoe = new Shoe(rules.Decks, rng);
        _player = new Player("You", rules.StartingBankroll);
    }

    public void Run()
    {
        _out.WriteLine("=== BLACKJACK ===");
        _out.WriteLine($"{_rules.Decks} decks | blackjack pays 3:2 | dealer {(_rules.DealerHitsSoft17 ? "hits" : "stands on")} soft 17");
        _out.WriteLine();

        while (_player.Bankroll >= _rules.MinBet)
        {
            if (!PlayRound()) break;
            _out.WriteLine();
        }

        if (_player.Bankroll < _rules.MinBet)
            _out.WriteLine("You can't cover the minimum bet. Game over!");

        PrintSummary();
    }

    // Returns false if the player chose to quit.
    private bool PlayRound()
    {
        if (_shoe.NeedsShuffle)
        {
            _shoe.Reshuffle();
            _out.WriteLine("(Shuffling the shoe...)");
        }

        decimal? bet = ReadBet();
        if (bet is null) return false;

        var playerHand = new Hand(bet.Value);
        var dealerHand = new Hand();
        _player.Hands.Clear();
        _player.Hands.Add(playerHand);

        // Deal: player, dealer, player, dealer
        playerHand.Add(_shoe.Draw());
        dealerHand.Add(_shoe.Draw());
        playerHand.Add(_shoe.Draw());
        dealerHand.Add(_shoe.Draw());

        _out.WriteLine();
        _out.WriteLine($"Dealer shows: {dealerHand.Cards[0]} [??]");
        _out.WriteLine($"Your hand:    {Describe(playerHand)}");

        // The dealer peeks for blackjack, so a natural on either side ends the round immediately.
        if (playerHand.IsBlackjack || dealerHand.IsBlackjack)
        {
            _out.WriteLine($"Dealer hand:  {Describe(dealerHand)}");
            Settle(playerHand, dealerHand);
            return true;
        }

        foreach (Hand hand in _player.Hands)
            PlayHand(hand);

        if (_player.Hands.Any(h => !h.IsBust))
            PlayDealer(dealerHand);
        else
            _out.WriteLine($"Dealer hand:  {Describe(dealerHand)}");

        foreach (Hand hand in _player.Hands)
            Settle(hand, dealerHand);

        return true;
    }

    private void PlayHand(Hand hand)
    {
        while (hand.Value < 21)
        {
            bool canDouble = hand.Cards.Count == 2 && _player.Bankroll >= hand.Bet * 2;
            string prompt = canDouble ? "(H)it, (S)tand or (D)ouble down? " : "(H)it or (S)tand? ";
            _out.Write(prompt);

            string? line = _in.ReadLine();
            if (line is null) return; // input closed: stand
            string choice = line.Trim().ToLowerInvariant();

            if (choice is "h" or "hit")
            {
                hand.Add(_shoe.Draw());
                _out.WriteLine($"You drew {hand.Cards[^1]}  ->  {Describe(hand)}");
                if (hand.IsBust) return;
            }
            else if (choice is "s" or "stand")
            {
                return;
            }
            else if (canDouble && choice is "d" or "double")
            {
                hand.Bet *= 2;
                hand.DoubledDown = true;
                hand.Add(_shoe.Draw());
                _out.WriteLine($"Doubled to ${Money(hand.Bet)}. You drew {hand.Cards[^1]}  ->  {Describe(hand)}");
                return; // one card only
            }
            else
            {
                _out.WriteLine("Please enter one of the options shown.");
            }
        }
    }

    private void PlayDealer(Hand dealer)
    {
        _out.WriteLine();
        _out.WriteLine($"Dealer reveals: {Describe(dealer)}");
        while (Settlement.DealerShouldHit(dealer, _rules))
        {
            dealer.Add(_shoe.Draw());
            _out.WriteLine($"Dealer draws {dealer.Cards[^1]}  ->  {Describe(dealer)}");
        }
    }

    private void Settle(Hand player, Hand dealer)
    {
        Outcome outcome = Settlement.Evaluate(player, dealer);
        decimal net = Settlement.NetPayout(outcome, player.Bet, _rules);
        _player.Bankroll += net;

        _rounds++;
        switch (outcome)
        {
            case Outcome.Blackjack: _blackjacks++; _wins++; break;
            case Outcome.Win: _wins++; break;
            case Outcome.Loss: _losses++; break;
            default: _pushes++; break;
        }

        string message = outcome switch
        {
            Outcome.Blackjack => $"BLACKJACK! You win ${Money(net)}.",
            Outcome.Win when dealer.IsBust => $"Dealer busts! You win ${Money(net)}.",
            Outcome.Win => $"You win ${Money(net)}.",
            Outcome.Push => "Push. Your bet is returned.",
            _ when player.IsBust => $"Bust! You lose ${Money(-net)}.",
            _ => $"Dealer wins. You lose ${Money(-net)}."
        };

        _out.WriteLine();
        _out.WriteLine(message);
        _out.WriteLine($"Bankroll: ${Money(_player.Bankroll)}");
    }

    private decimal? ReadBet()
    {
        while (true)
        {
            _out.Write($"Bankroll ${Money(_player.Bankroll)}. Bet (min ${Money(_rules.MinBet)}) or 'q' to quit: ");
            string? line = _in.ReadLine()?.Trim();
            if (line is null || line.Equals("q", StringComparison.OrdinalIgnoreCase)) return null;

            if (!decimal.TryParse(line, NumberStyles.Number, CultureInfo.InvariantCulture, out decimal bet))
                _out.WriteLine("Enter a number, e.g. 25.");
            else if (bet < _rules.MinBet)
                _out.WriteLine($"The minimum bet is ${Money(_rules.MinBet)}.");
            else if (bet > _player.Bankroll)
                _out.WriteLine("You can't bet more than your bankroll.");
            else
                return bet;
        }
    }

    private void PrintSummary()
    {
        decimal net = _player.Bankroll - _rules.StartingBankroll;
        _out.WriteLine();
        _out.WriteLine("--- Session summary ---");
        _out.WriteLine($"Hands played: {_rounds}  (won {_wins}, lost {_losses}, pushed {_pushes}, blackjacks {_blackjacks})");
        _out.WriteLine($"Final bankroll: ${Money(_player.Bankroll)} ({(net >= 0 ? "+" : "-")}${Money(Math.Abs(net))})");
    }

    private static string Describe(Hand hand) =>
        $"{hand}  =  {(hand.IsBlackjack ? "Blackjack" : (hand.IsSoft ? "soft " : "") + hand.Value)}";

    private static string Money(decimal amount) => amount.ToString("0.00", CultureInfo.InvariantCulture);
}
