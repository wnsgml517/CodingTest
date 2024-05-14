fun main() {
    val N = readLine()!!.toInt()

    val result = mutableListOf<List<Int>>()

    val r = mutableListOf<Int>()

    for (i in 0 until N) {
        val n = readLine()!!.split(" ").map { it.toInt() }
        result.add(n)
    }

    for ((index, value) in result.withIndex()) {
        var cnt = 0

        for ((i, v) in result.withIndex()) {
            if (i == index) { // 본인 제외
                continue
            }
            if (value[0] < v[0] && value[1] < v[1]) { // 카운트
                cnt++
            }
        }
        r.add(cnt + 1)
    }

    for (i in r) {
        print("$i ")
    }
}