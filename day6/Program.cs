using System.Diagnostics;

var fishes = File.ReadAllText("input.txt")
    .Split(",")
    .Select(int.Parse)
    .ToList();

var daysCount = 256;

//frequencies approach
void Frequencies()
{
    var frequencies = Enumerable.Range(0, 9).Select(i => fishes.LongCount(f => f == i)).ToList();
    for (var i = 0; i < daysCount; i++)
    {
        var first = frequencies.First();
        frequencies = frequencies.Skip(1).Append(first).ToList();
        frequencies[6] += frequencies[8];
    }
    Console.WriteLine($"Count: {frequencies.Sum()}");
}

//recursive approach (actually solved part 2 good enough)
void Recursive() {
    var cache = new Dictionary<int, long>(); 
    long CalculateCount(int days, int fish)
    {
        var cacheKey = days * 10 + fish;
        if (cache.ContainsKey(cacheKey))
            return cache[cacheKey];
        var baseDaysCount = days - fish - 1;
        if (baseDaysCount < 0)
            return 1;
        var childCount = baseDaysCount / 7 + 1;
        long result = 1;
        var children = Enumerable.Range(0, childCount).Select(i => baseDaysCount - i * 7).ToArray();
        foreach (var child in children)
        {
            result += CalculateCount(child, 8);
        }

        cache[cacheKey] = result;
        return result;
    }
    
    var calculateCount = fishes.Sum(f => CalculateCount(daysCount, f));
    Console.WriteLine($"Count: {calculateCount}");
}


//naive approach (only part 1)
void Naive()
{
    for (var day = 0; day < daysCount; day++)
    {
        var fishStartCount = fishes.Count;
        for (var i = 0; i < fishStartCount; i++)
        {
            var fishTimer = fishes[i];

            if (fishTimer == 0)
            {
                fishes.Add(8);
                fishes[i] = 6;
            }
            else
            {
                fishes[i]--;
            }
        }
    }

    Console.WriteLine("Count: " + fishes.Count);
}

var stopwatch = Stopwatch.StartNew();
stopwatch.Start();
Recursive();
var elapsed = stopwatch.Elapsed;
Console.WriteLine($"(recursion time: {elapsed})");

stopwatch.Reset();
stopwatch.Start();
Frequencies();
elapsed = stopwatch.Elapsed;
Console.WriteLine($"(frequencies time: {elapsed})");

/*stopwatch.Reset();
stopwatch.Start();
Naive();
elapsed = stopwatch.Elapsed;
Console.WriteLine($"(naive time: {elapsed})");*/