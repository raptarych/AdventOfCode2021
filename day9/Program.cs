

var input = File.ReadAllText("input.txt").Split("\r\n").ToArray();

(int x, int y)[] GetAdjacentCells(int x, int y)
{
    var line = input[y];
    return new (int, int)?[]
        {
            x == 0 ? null : (x - 1, y),
            line.Length - 1 == x ? null : (x + 1, y),
            y == 0 ? null : (x, y - 1),
            input.Length - 1 == y ? null : (x, y + 1),
        }
        .Where(i => i.HasValue)
        .Cast<(int, int)>()
        .ToArray();
}

var holes = new List<int>();
for (var y = 0; y < input.Length; y++)
{
    var line = input[y];
    for (var x = 0; x < line.Length; x++)
    {
        var c = line[x];
        var adjacentCells = GetAdjacentCells(x, y);

        if (adjacentCells.All(i => input[i.y][i.x] > c))
        {
            //part1:
            //holes.Add(c - '0'); 
            //continue;

            var discoveredCells = new List<int>() { y * 100 + x };
            var queue = new Queue<(int, int)>(new[] { (x, y) });

            while (queue.Any())
            {
                var (currentX, currentY) = queue.Dequeue();
                var currentAdjacents = GetAdjacentCells(currentX, currentY);
                foreach (var (aX, aY) in currentAdjacents)
                {
                    var cell = input[aY][aX];
                    if (cell != '9' && !discoveredCells.Contains(aY * 100 + aX))
                    {
                        discoveredCells.Add(aY * 100 + aX);
                        queue.Enqueue((aX, aY));
                    }
                }
            }
            holes.Add(discoveredCells.Count);
        }
    }
}
Console.WriteLine(holes.OrderByDescending(i => i).Take(3).Aggregate(1, (i, x) => i * x));