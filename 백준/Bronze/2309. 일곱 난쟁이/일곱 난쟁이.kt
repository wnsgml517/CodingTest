fun main() {
    val n = 9
	val a = IntArray(n) {readLine()!!.toInt()}
	a.sort()
	val total = a.sum()

    for (i in 0 until n){
        for (j in i+1 until n){
            if (total - a[i]- a[j]==100){
                for (k in 0 until n){
                    if (i==k || j==k) continue
                    println(a[k])
                }
                return 
            }
        }
    }
}