import Foundation

struct Hanoi {
    var trial : Int = 0
    var answer : String = ""
    
    mutating func hanoiTower(_ number : Int, from towerName1 : String, temp towerName2 : String, to towerName3 : String) {
        trial += 1
        if number == 1 {
            answer += "\(towerName1) \(towerName3)\n"
        }
        else {
            hanoiTower(number - 1, from: towerName1, temp: towerName3, to: towerName2)
            answer += "\(towerName1) \(towerName3)\n"
            hanoiTower(number - 1, from: towerName2, temp: towerName1, to: towerName3)
        }
    }
}

let n = Int(readLine()!)!
var hanoi = Hanoi()
hanoi.hanoiTower(n, from: "1", temp: "2", to: "3")
print(hanoi.trial)
print(hanoi.answer)
