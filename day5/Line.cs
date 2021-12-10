using System.Text.RegularExpressions;

class Line
{
    public Line(IReadOnlyList<Group> groups)
    {
        X1 = int.Parse(groups[0].Value);
        Y1 = int.Parse(groups[1].Value);
        X2 = int.Parse(groups[2].Value);
        Y2 = int.Parse(groups[3].Value);
    }
    public int X1 { get; set; }
    public int Y1 { get; set; }
    public int X2 { get; set; }
    public int Y2 { get; set; }

    public bool IsVertical()
    {
        return X1 == X2 || Y1 == Y2;
    }

    public bool IsDiagonal()
    {
        return Math.Abs(X1 - X2) == Math.Abs(Y1 - Y2);
    }

    public IEnumerable<(int x, int y)> GetPoints()
    {
        if (!IsVertical() && !IsDiagonal())
            throw new NotImplementedException();

        var dx = Math.Sign(X2 - X1);
        var dy = Math.Sign(Y2 - Y1);

        var (x, y) = (X1, Y1);
        yield return (x, y);
        while (x != X2 || y != Y2)
        {
            x += dx;
            y += dy;
            yield return (x, y);
        }
    }
}