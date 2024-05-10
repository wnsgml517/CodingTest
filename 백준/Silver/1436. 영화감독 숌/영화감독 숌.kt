fun main() {
    val N = readLine()!!.toInt() // 사용자로부터 입력 받음
    var result = 0 // 답
    var cnt = 0 // 현재까지 찾은 "666"을 포함하는 숫자의 수

    while (true) {
        result++
        if ("666" in result.toString()) {
            cnt++
        }

        if (cnt == N) {
            println(result)
            break
        }
    }
}