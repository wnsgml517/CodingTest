fun main() {
    val (E, S, M) = readLine()!!.split(" ").map { it.toInt() }
    var year = 1

    while (true) {
        if ((year - E) % 15 == 0 && (year - S) % 28 == 0 && (year - M) % 19 == 0) {
            break
        }
        year++
    }

    println(year)
}