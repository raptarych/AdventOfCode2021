var input = File.ReadAllText("input.txt").Split(",").Select(int.Parse).ToArray();

var bruteForceSource = Enumerable.Range(0, input.Max()).ToArray();

void Part1()
{
    var distances = bruteForceSource.Select(x => input.Sum(i => Math.Abs(i - x))).ToArray();
    Console.WriteLine(distances.Min());
}

void Part2()
{
    int ProgressionSum(int end) => (1 + end) * end / 2;
    var distances = bruteForceSource.Select(x => input.Sum(i => ProgressionSum(Math.Abs(i - x)))).ToArray();
    Console.WriteLine(distances.Min());
}

Part1();
Part2();