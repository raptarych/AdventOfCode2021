using System.Text.RegularExpressions;

var regex = new Regex(@"(\d+),(\d+) -> (\d+),(\d+)");
var input = File
    .ReadAllText("input.txt")
    .Split("\r\n")
    .Select(x => regex.Match(x).Groups.Values.Skip(1).ToArray())
    .Select(x => new Line(x))
    .Where(i => i.IsVertical() || i.IsDiagonal())
    .ToArray();

var pointsToCount = new Dictionary<int, int>();

foreach (var line in input)
{
    var points = line.GetPoints().ToArray();
    foreach (var (x, y) in points)
    {
        var key = y * 1000 + x;
        if (pointsToCount.ContainsKey(key))
            pointsToCount[key] += 1;
        else
        {
            pointsToCount[key] = 1;
        }
    }
}

Console.WriteLine(pointsToCount.Count(i => i.Value > 1));