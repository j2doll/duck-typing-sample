// duck-typing.go
// article from https://medium.com/@matryer/golang-advent-calendar-day-one-duck-typing-a513aaed544d
// code from https://gist.github.com/khajavi/03823f934c5291ae7cd1a83479eedbc6

package main

import "fmt"

type Speaker interface {
        Say(string)
}

type Person struct {
        name string
}

func (p *Person) Say(message string) {
        fmt.Println(p.name + ":" , message)
}

func SpeakAlphabet(via Speaker) {
        via.Say("abcdefgh")
}

func main() {
        mat := new(Person)
        mat.name = "Mat"
        SpeakAlphabet(mat)
}
