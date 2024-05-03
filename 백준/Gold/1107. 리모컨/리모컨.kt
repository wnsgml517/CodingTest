import kotlin.math.abs

fun possible(c: Int, broken: BooleanArray): Int {
    if (c == 0) {
        return if (broken[0]) 0 else 1
    }
    var len = 0
    var temp = c
    while (temp > 0) {
        if (broken[temp % 10]) return 0
        len++
        temp /= 10
    }
    return len
}

fun main() {
    val n = readLine()!!.toInt() // 이동하려고 하는 채널
    val m = readLine()!!.toInt() // 고장난 버튼의 갯수
    val broken = BooleanArray(10)
    if (m > 0) {
        val brokenButtons = readLine()!!.split(" ").map { it.toInt() } // 고장난 버튼 셋팅
        for (x in brokenButtons) {
            broken[x] = true
        }
    }
    var ans = abs(n - 100) // 정답의 초기값: 수빈이가 100번 채널을 보고 있기 때문
    for (i in n until 1000001) { // n부터 시작하여 가능한 채널까지 확인
        val lenPress = possible(i, broken) // 숫자를 몇 번 눌러야 하는지
        if (lenPress > 0) {
            val press = abs(i - n) // +를 몇 번 눌러야 하는지
            if (ans > lenPress + press) {
                ans = lenPress + press
                break // 가능한 채널을 찾았으므로 더 이상 확인할 필요 없음
            }
        }
    }
    for (i in n downTo 0) { // n부터 시작하여 0까지 내려가며 확인
        val lenPress = possible(i, broken) // 숫자를 몇 번 눌러야 하는지
        if (lenPress > 0) {
            val press = abs(i - n) // -를 몇 번 눌러야 하는지
            if (ans > lenPress + press) {
                ans = lenPress + press
                break // 가능한 채널을 찾았으므로 더 이상 확인할 필요 없음
            }
        }
    }
    println(ans)
}