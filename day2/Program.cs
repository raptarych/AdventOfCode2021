var input = File.ReadAllText("input.txt").Split("\n").Select(i => i.Split(" ")).ToArray();

void Part1()
{
    var x = 0;
    var depth = 0;

    foreach (var line in input)
    {
        var value = int.Parse(line[1]);
        switch (line[0])
        {
            case "forward":
                x += value;
                break;
            case "up":
                depth -= value;
                break;
            case "down":
                depth += value;
                break;
        }
    }

    Console.WriteLine(x * depth);
}

void Part2()
{
    var x = 0;
    var depth = 0;
    var aim = 0;

    foreach (var line in input)
    {
        var value = int.Parse(line[1]);
        switch (line[0])
        {
            case "forward":
                x += value;
                depth += aim * value;
                break;
            case "up":
                aim -= value;
                break;
            case "down":
                aim += value;
                break;
        }
    }

    Console.WriteLine(x * depth);
}

Part1();
Part2();