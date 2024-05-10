import Foundation

if let input = readLine(), let n = Int(input) {
    var i = 6
    var number = 5
    while true {
        if n <= 6 {
            if n == 1 {
                print("666")
                break
            } else {
                print("\(n-1)666")
                break
            }
        }
        if i == n {
            print("\(number)666")
            break
        }
        if (number + 1) % 10 == 6 {
            if (number + 1) % 100 == 66 {
                if (number + 1) % 1000 == 666 {
                    if (number + 1) % 10000 == 6666 {
                        if i + 10001 > n {
                            if number / 10000 != 0 {
                                print("\(number / 10000)", terminator: "")
                            }
                            print("666", terminator: "")
                            for _ in 0..<(4 - String(n - i - 1).count) {
                                print("0", terminator: "")
                            }
                            print("\(n - i - 1)")
                            break
                        }
                        i += 10001
                    } else {
                        if i + 1001 > n {
                            if number / 1000 != 0 {
                                print("\(number / 1000)", terminator: "")
                            }
                            print("666", terminator: "")
                            for _ in 0..<(3 - String(n - i - 1).count) {
                                print("0", terminator: "")
                            }
                            print("\(n - i - 1)")
                            break
                        }
                        i += 1001
                    }
                } else {
                    if i + 101 > n {
                        if number / 100 != 0 {
                            print("\(number / 100)", terminator: "")
                        }
                        print("666", terminator: "")
                        for _ in 0..<(2 - String(n - i - 1).count) {
                            print("0", terminator: "")
                        }
                        print("\(n - i - 1)")
                        break
                    }
                    i += 101
                }
            } else {
                if i + 11 > n {
                    if number / 10 != 0 {
                        print("\(number / 10)", terminator: "")
                    }
                    print("666", terminator: "")
                    for _ in 0..<(1 - String(n - i - 1).count) {
                        print("0", terminator: "")
                    }
                    print("\(n - i - 1)")
                    break
                }
                i += 11
            }
            number += 2
        } else {
            number += 1
            i += 1
        }
    }
} else {
    print("Invalid input")
}