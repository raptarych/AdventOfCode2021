class BingoTable
{
    class BingoNubmer
    {
        public int Position { get; set; }

        public bool Marked { get; set; }

        public override string ToString()
        {
            return $"Position: {Position} Marked: {Marked}";
        }
    }

    private readonly Dictionary<int, BingoNubmer> numbersInfo = new();

    public BingoTable(string[] table)
    {
        foreach (var line in table)
        {
            foreach (var number in line.Split(' ').Where(i => i != "").Select(int.Parse))
            {
                numbersInfo[number] = new BingoNubmer
                {
                    Position = numbersInfo.Count,
                    Marked = false
                };
            }
        }
    }

    public bool MarkAndReturnIfDrawn(int number)
    {
        if (!numbersInfo.ContainsKey(number))
            return false;
        numbersInfo[number].Marked = true;

        for (var i = 0; i < 5; i++)
        {
            var row = numbersInfo.Skip(i * 5).Take(5);
            if (row.All(x => x.Value.Marked))
                return true;

            var columnIndices = Enumerable.Range(0, 5)
                .Select(x => x * 5 + i)
                .ToHashSet();
            var column = numbersInfo.Where(x => columnIndices.Contains(x.Value.Position));
            if (column.All(x => x.Value.Marked))
                return true;
        }

        return false;
    }

    internal long CalculateAnswer(int number)
    {
        return numbersInfo.Where(i => !i.Value.Marked).Sum(x => x.Key) * number;
    }

    public bool Win { get; set; }
}