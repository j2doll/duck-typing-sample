# Duck typing

- https://en.wikipedia.org/wiki/Duck_typing
- https://stackoverflow.com/questions/4205130/what-is-duck-typing
- https://medium.com/@matryer/golang-advent-calendar-day-one-duck-typing-a513aaed544d
- https://gist.github.com/khajavi/03823f934c5291ae7cd1a83479eedbc6

It is a term used in [dynamic languages](http://en.wikipedia.org/wiki/Dynamic_programming_language) that do not have [strong typing](http://en.wikipedia.org/wiki/Strong_typing).

The idea is that you don't need a type in order to invoke an existing method on an object - if a method is defined on it, you can invoke it.

The name comes from the phrase "If it looks like a duck and quacks like a duck, it's a duck".

[Wikipedia](https://en.wikipedia.org/wiki/Duck_typing) has much more information.

```python
# duck-typing.py
class Parrot:
	def fly(self):
		print("Parrot flying")

class Airplane:
	def fly(self):
		print("Airplane flying")

class Whale:
	def swim(self):
		print("Whale swimming")

def lift_off(entity):
	entity.fly()

parrot = Parrot()
airplane = Airplane()
whale = Whale()

lift_off(parrot) # prints `Parrot flying`
lift_off(airplane) # prints `Airplane flying`
lift_off(whale) # Throws the error `'Whale' object has no attribute 'fly'`
```

```go
// duck-typing.go
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
```
