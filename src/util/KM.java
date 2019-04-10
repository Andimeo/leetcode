import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.StreamTokenizer;

public class KM {
    public static int INF = 0x7fffffff;

    public Main(int n, int graph[][]) {
        this.n = n;
        this.graph = graph;
        this.Lx = new int[n];
        this.Ly = new int[n];
        this.matched = new int[n];
        for (int i = 0; i < n; i++) {
            this.Lx[i] = -INF;
            for (int j = 0; j < n; j++) {
                this.Lx[i] = Math.max(this.Lx[i], graph[i][j]);
            }
            this.Ly[i] = 0;
            this.matched[i] = -1;
        }
    }

    public int km() {
        for (int i = 0; i < n; i++) {
            slack = new int[n];
            for (int j = 0; j < n; j++)
                slack[j] = INF;
            while (true) {
                S = new boolean[n];
                T = new boolean[n];
                if (match(i))
                    break;
                else
                    update();
            }
        }
        int result = 0;
        for (int i = 0; i < n; i++) {
            if (matched[i] != -1)
                result += graph[matched[i]][i];
        }
        return result;
    }

    private boolean match(int u) {
        S[u] = true;
        for (int v = 0; v < n; v++) {
            if (T[v])
                continue;
            int t = Lx[u] + Ly[v] - graph[u][v];
            if (t == 0) {
                T[v] = true;
                if (matched[v] == -1 || match(matched[v])) {
                    matched[v] = u;
                    return true;
                }
            } else {
                slack[v] = Math.min(slack[v], t);
            }
        }
        return false;
    }

    private void update() {
        int d = INF;
        for (int i = 0; i < n; i++) {
            if (!T[i])
                d = Math.min(d, slack[i]);
        }
        for (int i = 0; i < n; i++)
            if (S[i])
                Lx[i] -= d;
        for (int i = 0; i < n; i++)
            if (T[i])
                Ly[i] += d;
            else
                slack[i] -= d;

    }

    private int n;
    private int graph[][];
    private int Lx[];
    private int Ly[];
    private int slack[];
    private boolean S[];
    private boolean T[];
    private int matched[];

    // http://acm.hdu.edu.cn/showproblem.php?pid=2255
    public static void main(String[] args) throws IOException {
        int maxn = 456;
        StreamTokenizer in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        int graph[][] = new int[maxn][maxn];
        String line;
        while (in.nextToken() != StreamTokenizer.TT_EOF) {
            int n = (int)in.nval;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    int a = in.nextToken();
                    graph[i][j] = (int) in.nval;
                }
            }

            System.out.println(new KM(n, graph).km());
        }
    }
}