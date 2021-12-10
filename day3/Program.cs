var input = File.ReadAllText("input.txt").Split("\r\n").ToArray();

void Part1()
{
    var binaryNumberLength = input[0].Length;
    var numbersCount = input.Length;
    var oneCounts = Enumerable.Range(0, binaryNumberLength)
        .Select(i => input.Select(n => n[i]).Count(n => n == '1'));
    var gammaBinary = new string(oneCounts.Select(i => i > numbersCount / 2 ? '1' : '0').ToArray());
    var epsilonBinary = new string(gammaBinary.Select(i => i == '0' ? '1' : '0').ToArray());
    Console.WriteLine(Convert.ToInt32(gammaBinary, 2) * Convert.ToInt32(epsilonBinary, 2));
}

void Part2()
{
    string GetRating(string[] values, bool isOxygen, int bit = 0)
    {
        var onesCount = values.Count(i => i[bit] == '1');
        var filterBy = (isOxygen ? onesCount >= values.Count() / 2d : onesCount < values.Count() / 2d) ? '1' : '0';
        var filteredValues = values.Where(i => i[bit] == filterBy).ToArray();
        if (filteredValues.Length == 1)
            return filteredValues.First();
        return GetRating(filteredValues, isOxygen, ++bit);
    }

    var oxygen = GetRating(input, isOxygen: true);
    var co2 = GetRating(input, isOxygen: false);

    Console.WriteLine(oxygen + " " + co2);
    Console.WriteLine(Convert.ToInt32(oxygen, 2) * Convert.ToInt32(co2, 2));
}

Part1();
Part2();
