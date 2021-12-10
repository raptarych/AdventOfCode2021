var input = File.ReadAllText("input.txt").Split("\r\n").ToArray();

var closeToOpened = new Dictionary<char, char>()
{
    {'}', '{'},
    {')', '('},
    {']', '['},
    {'>', '<'},
};
var penalties = new Dictionary<char, int>()
{
    {'}', 1197},
    {')', 3},
    {']', 57},
    {'>', 25137},
};

var openedScores = new Dictionary<char, int>()
{
    {'{', 3},
    {'(', 1},
    {'[', 2},
    {'<', 4},
};
void Part1()
{
    var totalPenalty = 0;
    foreach (var line in input)
    {
        var stack = new Stack<char>();

        foreach (var c in line)
        {
            if (closeToOpened.ContainsValue(c))
            {
                stack.Push(c);
            }
            else
            {
                var lastOpenedChar = stack.Pop();
                if (closeToOpened[c] != lastOpenedChar)
                {
                    //Console.WriteLine("Corrupted char: " + c + " on " + line);
                    totalPenalty += penalties[c];
                    break;
                }
            }
        }
    }
    Console.WriteLine("Part1 total: " + totalPenalty);
}

void Part2()
{
    var scoresTotal = new List<long>();
    foreach (var line in input)
    {
        var stack = new Stack<char>();
        var score = 0L;
        var incorrectLine = false;
        foreach (var c in line)
        {
            if (closeToOpened.ContainsValue(c))
            {
                stack.Push(c);
            }
            else
            {
                var lastStackItem = stack.Pop();
                if (closeToOpened[c] != lastStackItem)
                {
                    //Console.WriteLine("Corrupted char: " + c + " on " + line);
                    incorrectLine = true;
                    break;
                }
            }
        }

        if (incorrectLine) 
            continue;

        while (stack.Any())
        {
            score = score * 5 + openedScores[stack.Pop()];
        }

        scoresTotal.Add(score);
    }
    Console.WriteLine("Part2 total: " + scoresTotal.OrderBy(i => i).Skip(scoresTotal.Count / 2).First());
}

Part1();
Part2();