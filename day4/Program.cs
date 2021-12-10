var input = File.ReadAllText("input.txt")
    .Split("\r\n")
    .Where(i => !string.IsNullOrEmpty(i));
var numbers = input.First().Split(',').Select(int.Parse);
var bingoTables = input.Skip(1).Chunk(5).Select(i => new BingoTable(i)).ToArray();

foreach (var number in numbers)
{
    foreach (var table in bingoTables)
    {
        if (table.MarkAndReturnIfDrawn(number))
        {
            table.Win = true;
            if (bingoTables.All(i => i.Win))
            {
                var answer = table.CalculateAnswer(number);
                Console.WriteLine(answer);
                return;
            }
        }
    }
}
throw new Exception("No answer");