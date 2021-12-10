var input = File.ReadAllText("input.txt")
    .Split("\r\n")
    .Select(i => i.Split("|"))
    .ToArray();

string SetToString(HashSet<int> set)
{
    return string.Join("", set.OrderBy(x => x).Select(x => x.ToString()));
}

/*
 1111
2    3
2    3
 4444
5    6
5    6
 7777
 */

var digitsConfiguration = new[]
{
    new HashSet<int>() { 1, 2, 3, 5, 6, 7, },
    new HashSet<int>() { 3, 6 },
    new HashSet<int>() { 1, 3, 4, 5, 7 },
    new HashSet<int>() { 1, 3, 4, 6, 7 },
    new HashSet<int>() { 2, 3, 4, 6 },
    new HashSet<int>() { 1, 2, 4, 6, 7 },
    new HashSet<int>() { 1, 2, 4, 5, 6, 7 },
    new HashSet<int>() { 1, 3, 6 },
    new HashSet<int>() { 1, 2, 3, 4, 5, 6, 7 },
    new HashSet<int>() { 1, 2, 3, 4, 6, 7 },
};
var segmentsToDigit = digitsConfiguration
    .Select(SetToString)
    .Select((i, idx) => new { idx, i })
    .ToDictionary(i => i.i, i => i.idx);

var result = 0;
foreach (var line in input)
{
    var patterns = line[0].Trim()
        .Split(' ')
        .OrderBy(i => i.Length)
        .ToArray();
    var encodedDigits = line[1].Trim();
    var letterToSegmentMapping = Enumerable.Range(0, 7)
        .Select(i => Enumerable.Range(1, 7).ToHashSet())
        .Select((i, idx) => new { idx, i })
        .ToDictionary(i => (char)('a' + i.idx), i => i.i);

    //easy digits (1, 4, 7, 8)
    foreach (var pattern in patterns)
    {
        switch (pattern.Length)
        {
            case 2:
                CorrectMapping(pattern.ToArray(), digitsConfiguration[1]);
                continue;
            case 3:
                CorrectMapping(pattern.ToArray(), digitsConfiguration[7]);
                continue;
            case 4:
                CorrectMapping(pattern.ToArray(), digitsConfiguration[4]);
                continue;
        }
    }

    //5 chars
    var fiveCharsPatterns = patterns
        .Where(i => i.Length == 5)
        .Select(i => i.OrderBy(x => x).ToHashSet())
        .ToArray();
    var commonFiveCharsSymbols =
        fiveCharsPatterns.Aggregate("abcdefg".ToArray(), (a, i) => a.Intersect(i).ToArray());
    CorrectMapping(commonFiveCharsSymbols, new[] { 1, 4, 7 });

    //6 chars
    var sixCharsPatterns = patterns
        .Where(i => i.Length == 6)
        .Select(i => i.OrderBy(x => x).ToHashSet())
        .ToArray();
    var missingChars = sixCharsPatterns.Select(i => "abcdefg".Except(i).Single()).ToArray();
    CorrectMapping(missingChars, new[] { 3, 4, 5 });

    if (letterToSegmentMapping.Any(i => i.Value.Count > 1))
    {
        throw new Exception("Can't decode string " + line[0]);
    }

    var answer = encodedDigits
        .Split(' ')
        .Select(e => e.Select(c => letterToSegmentMapping[c].Single()).ToHashSet())
        .Select(SetToString)
        .Select(i => segmentsToDigit[i])
        .Select((i, idx) => (int) (i * Math.Pow(10, 3 - idx)))
        .Sum();
    Console.WriteLine($"{encodedDigits}: {answer}");
    result += answer;
    
    void CorrectMapping(IReadOnlyCollection<char> chars, IReadOnlyCollection<int> possibleValues)
    {
        foreach (var key in letterToSegmentMapping.Keys)
        {
            if (chars.Contains(key))
            {
                letterToSegmentMapping[key].IntersectWith(possibleValues);
            }
            else
            {
                letterToSegmentMapping[key].ExceptWith(possibleValues);
            }
        }
    }
}
Console.WriteLine(result);