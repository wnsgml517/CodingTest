import java.io.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()
    val c = Array(n) { br.readLine().toCharArray() }

    fun checkCurMaxNum(): Int {
        var maxCnt = 1
        for (i in 0 until n) {
            // 가로 확인
            var cnt = 1
            for (j in 1 until n) {
                if (c[i][j] == c[i][j - 1]) {
                    cnt++
                } else {
                    cnt = 1
                }
                maxCnt = maxOf(cnt, maxCnt)
            }
            // 세로 확인
            cnt = 1
            for (j in 1 until n) {
                if (c[j][i] == c[j - 1][i]) {
                    cnt++
                } else {
                    cnt = 1
                }
                maxCnt = maxOf(cnt, maxCnt)
            }
        }
        return maxCnt
    }

    var result = 1
    for (i in 0 until n) {
        for (j in 0 until n - 1) {
            // 오른쪽과 swap
            if (j + 1 < n && c[i][j] != c[i][j + 1]) {
                c[i][j] = c[i][j + 1].also { c[i][j + 1] = c[i][j] } // swap
                result = maxOf(result, checkCurMaxNum())
                c[i][j] = c[i][j + 1].also { c[i][j + 1] = c[i][j] } // 되돌리기
            }
            // 아래쪽과 swap
            if (i + 1 < n && c[i][j] != c[i + 1][j]) {
                c[i][j] = c[i + 1][j].also { c[i + 1][j] = c[i][j] } // swap
                result = maxOf(result, checkCurMaxNum())
                c[i][j] = c[i + 1][j].also { c[i + 1][j] = c[i][j] } // 되돌리기
            }
        }
    }

    println(result)
}