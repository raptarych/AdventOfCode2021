var input = File.ReadAllText("input.txt").Split("\n").Select(int.Parse).ToArray();

void Part1()
{
    Console.WriteLine(input.Skip(1).Select((i, idx) => i > input[idx] ? 1 : 0).Sum());
}

void Part2()
{
    var movingSum3 = input.Take(input.Length - 2).Select((_, idx) => input.Skip(idx).Take(3).Sum()).ToArray();
    Console.WriteLine(movingSum3.Skip(1).Select((i, idx) => i > movingSum3[idx] ? 1 : 0).Sum());
}
Part1();
Part2();