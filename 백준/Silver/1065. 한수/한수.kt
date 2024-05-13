import java.util.Scanner

fun check(i: Int): Boolean {
    if (i < 100) return true // 100미만의 수는 모두 한수

    val numStr = i.toString()
    val diff = numStr[1] - numStr[0]
    
    for (index in 1 until numStr.length) {
        if (diff != numStr[index] - numStr[index - 1]) {
            return false
        }
    }
    return true
}

fun main() {
    val scanner = Scanner(System.`in`)
    val N = scanner.nextInt()
    var cnt = 0

    for (i in 1..N) {
        if (check(i)) {
            cnt++
        }
    }

    println(cnt)
}